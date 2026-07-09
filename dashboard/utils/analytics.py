import os
import pandas as pd

# ======================================================
# SentinelX Analytics Engine
# AI-Powered Network Threat Intelligence
# ======================================================

# Project Root Directory
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

# Data Files
NETWORK_FILE = os.path.join(BASE_DIR, "data", "network.csv")
ALERT_FILE = os.path.join(BASE_DIR, "logs", "alerts.log")


# ======================================================
# Load Network Traffic
# ======================================================
def load_network_data():

    if not os.path.exists(NETWORK_FILE):
        return pd.DataFrame(
            columns=[
                "Source_IP",
                "Destination_IP",
                "Protocol",
                "Packet_Size"
            ]
        )

    try:
        df = pd.read_csv(NETWORK_FILE)

        # Remove completely empty rows
        df = df.dropna(how="all")

        return df

    except Exception as e:
        print("Error Loading Network Data :", e)

        return pd.DataFrame(
            columns=[
                "Source_IP",
                "Destination_IP",
                "Protocol",
                "Packet_Size"
            ]
        )


# ======================================================
# Packet Statistics
# ======================================================
def get_packet_count(df):
    return len(df)


def get_average_packet_size(df):

    if df.empty:
        return 0

    return round(df["Packet_Size"].mean(), 2)


# ======================================================
# Protocol Statistics
# ======================================================
def get_protocol_stats(df):

    if df.empty:
        return {}

    return df["Protocol"].value_counts().to_dict()


# ======================================================
# Top Source IP
# ======================================================
def get_top_source_ips(df, limit=5):

    if df.empty:
        return {}

    return df["Source_IP"].value_counts().head(limit).to_dict()


# ======================================================
# Top Destination IP
# ======================================================
def get_top_destination_ips(df, limit=5):

    if df.empty:
        return {}

    return df["Destination_IP"].value_counts().head(limit).to_dict()


# ======================================================
# Threat Count
# ======================================================
def get_threat_count():

    if not os.path.exists(ALERT_FILE):
        return 0

    try:

        with open(ALERT_FILE, "r") as f:
            return len(f.readlines())

    except Exception:

        return 0


# ======================================================
# Recent Alerts (Structured)
# ======================================================
def get_recent_alerts(limit=10):

    if not os.path.exists(ALERT_FILE):
        return []

    alerts = []

    try:

        with open(ALERT_FILE, "r") as file:

            lines = file.readlines()[-limit:]

            for line in lines:

                line = line.strip()

                if not line:
                    continue

                parts = line.split(",")

                if len(parts) >= 8:

                    alerts.append({

                        "time": parts[0],

                        "source": parts[1],

                        "destination": parts[2],

                        "protocol": parts[3],

                        "packet_size": parts[4],

                        "severity": parts[5],

                        "risk_score": parts[6],

                        "action": parts[7]

                    })

        return alerts

    except Exception as e:

        print("Alert Parsing Error:", e)

        return []

# ======================================================
# Trust Score
# ======================================================
def calculate_trust_score(total_packets, threats):

    if total_packets == 0:
        return 100

    score = ((total_packets - threats) / total_packets) * 100

    return round(score, 2)


# ======================================================
# Dashboard Summary
# ======================================================
def dashboard_summary():

    df = load_network_data()

    packets = get_packet_count(df)
    threats = get_threat_count()

    # Load Recent Alerts
    alerts = get_recent_alerts()

    # ======================================================
    # Threat Severity Statistics
    # ======================================================

    critical = 0
    high = 0
    medium = 0
    low = 0

    for alert in alerts:

        severity = alert["severity"].upper()

        if severity == "CRITICAL":
            critical += 1

        elif severity == "HIGH":
            high += 1

        elif severity == "MEDIUM":
            medium += 1

        elif severity == "LOW":
            low += 1

    return {

        "packets": packets,

        "threats": threats,

        "trusted": packets - threats,

        "trust_score": calculate_trust_score(
            packets,
            threats
        ),

        "average_packet_size": get_average_packet_size(df),

        "protocols": get_protocol_stats(df),

        "top_sources": get_top_source_ips(df),

        "top_destinations": get_top_destination_ips(df),

        "recent_alerts": alerts,

        "critical": critical,

        "high": high,

        "medium": medium,

        "low": low

    }
