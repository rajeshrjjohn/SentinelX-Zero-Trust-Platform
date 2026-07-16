"""
==========================================================
SentinelX v3.0
Threat Intelligence Engine
==========================================================
"""

def classify_threat(packet_size, protocol):
    """
    Threat Classification Engine

    Returns:
        severity
        risk_score
        action
    """

    protocol = protocol.upper()

    # -----------------------------
    # Default
    # -----------------------------
    severity = "LOW"
    risk_score = 20
    action = "MONITOR"

    # -----------------------------
    # Packet Size Classification
    # -----------------------------
    if packet_size >= 1000:

        severity = "CRITICAL"
        risk_score = 95
        action = "BLOCK"

    elif packet_size >= 500:

        severity = "HIGH"
        risk_score = 80
        action = "BLOCK"

    elif packet_size >= 200:

        severity = "MEDIUM"
        risk_score = 60
        action = "MONITOR"

    else:

        severity = "LOW"
        risk_score = 20
        action = "MONITOR"

    # -----------------------------
    # Protocol Risk Adjustment
    # -----------------------------
    if protocol == "ICMP":

        risk_score = min(risk_score + 10, 100)

    # -----------------------------
    # Final Policy Decision
    # -----------------------------
    if risk_score >= 90:

        severity = "CRITICAL"
        action = "BLOCK"

    elif risk_score >= 70:

        severity = "HIGH"
        action = "BLOCK"

    elif risk_score >= 40:

        severity = "MEDIUM"
        action = "MONITOR"

    else:

        severity = "LOW"
        action = "MONITOR"

    return {

        "severity": severity,

        "risk_score": risk_score,

        "action": action

    }
