#!/usr/bin/env python3

"""
==========================================================
SentinelX v3.0
AI-Powered Zero Trust Threat Detection Platform
Live Packet Capture Engine
==========================================================
"""

import os
import sys
from datetime import datetime

# ==========================================================
# Add Project Root to Python Path
# ==========================================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# ==========================================================
# Imports
# ==========================================================

from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

from collector.traffic_logger import (
    initialize_csv,
    log_packet
)

from detector.live_detector import detect_packet

# ==========================================================
# Log Files
# ==========================================================

LOG_DIR = os.path.join(PROJECT_ROOT, "logs")
ALERT_FILE = os.path.join(LOG_DIR, "alerts.log")

os.makedirs(LOG_DIR, exist_ok=True)

initialize_csv()

# ==========================================================
# Packet Processing
# ==========================================================

def packet_callback(packet):

    if IP not in packet:
        return

    src = packet[IP].src
    dst = packet[IP].dst

    packet_length = len(packet)

    # -----------------------------
    # Protocol Detection
    # -----------------------------

    if TCP in packet:
        protocol = "TCP"

    elif UDP in packet:
        protocol = "UDP"

    elif ICMP in packet:
        protocol = "ICMP"

    else:
        protocol = "OTHER"

    # -----------------------------
    # Save Network Traffic
    # -----------------------------

    log_packet(
        src,
        dst,
        protocol,
        packet_length
    )

    # -----------------------------
    # AI Detection
    # -----------------------------

    result = detect_packet(
        packet_length,
        protocol
    )

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    status = result["status"]
    severity = result["severity"]
    risk_score = result["risk_score"]
    action = result["action"]

    # =====================================================
    # Threat
    # =====================================================

    if status == "THREAT":

        print("\n" + "=" * 70)
        print("🚨 THREAT DETECTED")
        print("=" * 70)

        print(f"Time        : {now}")
        print(f"Source IP   : {src}")
        print(f"Destination : {dst}")
        print(f"Protocol    : {protocol}")
        print(f"Packet Size : {packet_length} Bytes")
        print(f"Severity    : {severity}")
        print(f"Risk Score  : {risk_score}")
        print(f"Action      : {action}")

        print("=" * 70)

        with open(ALERT_FILE, "a") as f:

            f.write(
                f"{now},"
                f"{src},"
                f"{dst},"
                f"{protocol},"
                f"{packet_length},"
                f"{severity},"
                f"{risk_score},"
                f"{action}\n"
            )

    # =====================================================
    # Normal
    # =====================================================

    else:

        print(
            f"[{now}] "
            f"✅ NORMAL | "
            f"{src} -> {dst} | "
            f"{protocol} | "
            f"{packet_length} bytes"
        )

# ==========================================================
# Main Function
# ==========================================================

def main():

    print("=" * 70)
    print(" SentinelX v3.0 ")
    print(" AI-Powered Zero Trust Threat Detection Platform ")
    print("=" * 70)

    print("Status : ACTIVE")
    print("AI Engine : Isolation Forest")
    print("Threat Intelligence : ENABLED")
    print("Packet Capture : Scapy")
    print("Logging : ENABLED")
    print("")

    print("Capturing Live Network Packets...")
    print("Press Ctrl+C to Stop.\n")

    try:

        sniff(

            prn=packet_callback,

            store=False

        )

    except KeyboardInterrupt:

        print("\nCapture Stopped Successfully.")

    except Exception as e:

        print(f"\nError : {e}")

# ==========================================================
# Start
# ==========================================================

if __name__ == "__main__":
    main()
