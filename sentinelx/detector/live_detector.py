"""
==========================================================
SentinelX v3.0
AI Live Detection Engine
AI-Powered Zero Trust Threat Detection
==========================================================
"""

import joblib
import pandas as pd

from dashboard.utils.threat import classify_threat

# ==========================================================
# Load Trained Isolation Forest Model
# ==========================================================

try:
    model = joblib.load("models/anomaly_model.pkl")
    print("✅ AI Model Loaded Successfully")

except Exception as e:
    print(f"❌ Failed to Load Model: {e}")
    model = None


# ==========================================================
# Protocol Encoding
# ==========================================================

PROTOCOL_MAP = {
    "TCP": 6,
    "UDP": 17,
    "ICMP": 1,
    "OTHER": 0
}


# ==========================================================
# Detect Network Packet
# ==========================================================

def detect_packet(packet_length, protocol):
    """
    Detect whether a packet is normal or anomalous.

    Parameters:
        packet_length (int): Packet size in bytes
        protocol (str): TCP / UDP / ICMP

    Returns:
        dict
    """

    if model is None:
        return {
            "status": "ERROR",
            "severity": "UNKNOWN",
            "risk_score": 0,
            "action": "MODEL NOT LOADED"
        }

    protocol = protocol.upper()

    protocol_value = PROTOCOL_MAP.get(protocol, 0)

    sample = pd.DataFrame({
        "packet_length": [packet_length],
        "protocol": [protocol_value]
    })

    prediction = model.predict(sample)

    # ======================================================
    # NORMAL Traffic
    # ======================================================

    if prediction[0] == 1:

        return {
            "status": "NORMAL",
            "severity": "NONE",
            "risk_score": 0,
            "action": "ALLOW"
        }

    # ======================================================
    # THREAT Traffic
    # ======================================================

    threat = classify_threat(packet_length, protocol)

    return {
        "status": "THREAT",
        "severity": threat["severity"],
        "risk_score": threat["risk_score"],
        "action": threat["action"]
    }


# ==========================================================
# Manual Test
# ==========================================================

if __name__ == "__main__":

    samples = [

        (60, "TCP"),

        (120, "UDP"),

        (350, "UDP"),

        (650, "TCP"),

        (1500, "UDP"),

        (80, "ICMP")

    ]

    print("=" * 65)
    print("SentinelX AI Threat Detection Engine")
    print("=" * 65)

    for length, protocol in samples:

        result = detect_packet(length, protocol)

        print(f"""
Packet Length : {length}
Protocol      : {protocol}
Status        : {result['status']}
Severity      : {result['severity']}
Risk Score    : {result['risk_score']}
Action        : {result['action']}
-------------------------------------------------------------
""")
