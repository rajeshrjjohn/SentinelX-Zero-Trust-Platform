"""
Build flow-level features from tshark packet CSVs.

Input: CSV with columns
  frame.time_epoch, ip.src, ip.dst, ip.proto,
  tcp.srcport, tcp.dstport, udp.srcport, udp.dstport,
  frame.len, tcp.flags.syn, tcp.flags.ack, tcp.flags.reset

Groups packets into bidirectional flows by 5-tuple (treating A->B and B->A
as the same flow, using a canonical ordering), computes flow-level stats,
and writes one row per flow.
"""

import sys
import pandas as pd
import numpy as np

FLOW_TIMEOUT = 120.0  # seconds of inactivity before a new flow starts for the same 5-tuple


def load_packets(path):
    df = pd.read_csv(path, dtype=str)
    df = df.dropna(subset=["ip.src", "ip.dst"])  # drop ARP / non-IP frames

    df["time"] = df["frame.time_epoch"].astype(float)
    df["proto"] = df["ip.proto"].astype(float).astype("Int64")
    df["len"] = df["frame.len"].astype(float)

    # unify port column: prefer tcp, fall back to udp
    df["srcport"] = df["tcp.srcport"].fillna(df["udp.srcport"])
    df["dstport"] = df["tcp.dstport"].fillna(df["udp.dstport"])
    df["srcport"] = pd.to_numeric(df["srcport"], errors="coerce").fillna(0).astype(int)
    df["dstport"] = pd.to_numeric(df["dstport"], errors="coerce").fillna(0).astype(int)

    flag_map = {"True": 1, "False": 0, "1": 1, "0": 0}
    df["syn"] = df["tcp.flags.syn"].map(flag_map).fillna(0).astype(int)
    df["ack"] = df["tcp.flags.ack"].map(flag_map).fillna(0).astype(int)
    df["rst"] = df["tcp.flags.reset"].map(flag_map).fillna(0).astype(int)

    df = df.sort_values("time").reset_index(drop=True)
    return df


def canonical_key(row):
    a = (row["ip.src"], row["srcport"])
    b = (row["ip.dst"], row["dstport"])
    if a <= b:
        return (a[0], a[1], b[0], b[1], row["proto"])
    else:
        return (b[0], b[1], a[0], a[1], row["proto"])


def build_flows(df, label):
    df = df.copy()
    df["key"] = df.apply(canonical_key, axis=1)

    flows = []
    for key, group in df.groupby("key"):
        group = group.sort_values("time")
        times = group["time"].values
        gap_idx = np.where(np.diff(times) > FLOW_TIMEOUT)[0]
        boundaries = [0] + list(gap_idx + 1) + [len(group)]

        for i in range(len(boundaries) - 1):
            chunk = group.iloc[boundaries[i]:boundaries[i + 1]]
            if len(chunk) == 0:
                continue

            duration = chunk["time"].max() - chunk["time"].min()
            duration = max(duration, 1e-3)
            pkt_count = len(chunk)
            byte_count = chunk["len"].sum()

            flows.append({
                "src_ip": key[0],
                "src_port": key[1],
                "dst_ip": key[2],
                "dst_port": key[3],
                "proto": key[4],
                "duration": duration,
                "pkt_count": pkt_count,
                "byte_count": byte_count,
                "pkts_per_sec": pkt_count / duration,
                "bytes_per_sec": byte_count / duration,
                "avg_pkt_size": byte_count / pkt_count,
                "std_pkt_size": chunk["len"].std() if pkt_count > 1 else 0.0,
                "syn_count": chunk["syn"].sum(),
                "ack_count": chunk["ack"].sum(),
                "rst_count": chunk["rst"].sum(),
                "unique_dst_ports": chunk["dstport"].nunique(),
                "label": label,
            })

    return pd.DataFrame(flows)


if __name__ == "__main__":
    benign_in, attack_in, out_path = sys.argv[1], sys.argv[2], sys.argv[3]

    print(f"Loading {benign_in} ...")
    benign_pkts = load_packets(benign_in)
    print(f"Loading {attack_in} ...")
    attack_pkts = load_packets(attack_in)

    print("Building benign flows ...")
    benign_flows = build_flows(benign_pkts, label=0)
    print(f"  {len(benign_flows)} benign flows")

    print("Building attack flows ...")
    attack_flows = build_flows(attack_pkts, label=1)
    print(f"  {len(attack_flows)} attack flows")

    all_flows = pd.concat([benign_flows, attack_flows], ignore_index=True)
    all_flows.to_csv(out_path, index=False)
    print(f"Wrote {len(all_flows)} total flows to {out_path}")
    print(all_flows["label"].value_counts())
