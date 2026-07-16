"""
==========================================================
SentinelX Security Report Generator
==========================================================
"""

import os
from datetime import datetime

from dashboard.utils.analytics import (
    dashboard_summary,
    get_ai_insights
)


# ==========================================================
# Generate Security Report
# ==========================================================
def generate_report():

    summary = dashboard_summary()
    insights = get_ai_insights()

    report = []

    # ======================================================
    # Header
    # ======================================================

    report.append("=" * 60)
    report.append("      SentinelX Zero Trust Security Report")
    report.append("=" * 60)
    report.append("")
    report.append(
        f"Generated On : {datetime.now().strftime('%d %b %Y %H:%M:%S')}"
    )
    report.append("")

    # ======================================================
    # Network Summary
    # ======================================================

    report.append("=" * 60)
    report.append("Network Summary")
    report.append("-" * 60)

    report.append(f"Total Packets       : {summary['packets']}")
    report.append(f"Threat Events       : {summary['threats']}")
    report.append(f"Trusted Traffic     : {summary['trusted']}")
    report.append(f"Trust Score         : {summary['trust_score']}%")
    report.append(f"Average Packet Size : {summary['average_packet_size']} Bytes")
    report.append("")

    # ======================================================
    # Threat Severity
    # ======================================================

    report.append("=" * 60)
    report.append("Threat Severity")
    report.append("-" * 60)

    report.append(f"Critical Threats    : {summary['critical']}")
    report.append(f"High Threats        : {summary['high']}")
    report.append(f"Medium Threats      : {summary['medium']}")
    report.append(f"Low Threats         : {summary['low']}")
    report.append("")

    # ======================================================
    # Threat Intelligence
    # ======================================================

    report.append("=" * 60)
    report.append("Threat Intelligence")
    report.append("-" * 60)

    report.append(f"Top Attacker IP     : {summary['top_attacker']}")
    report.append(f"Top Target IP       : {summary['top_target']}")
    report.append(f"Top Protocol        : {summary['top_protocol']}")
    report.append(f"Average Packet Size : {summary['average_packet']} Bytes")
    report.append("")

    # ======================================================
    # AI Security Insights
    # ======================================================

    report.append("=" * 60)
    report.append("AI Security Insights")
    report.append("-" * 60)

    for insight in insights:
        report.append(f"• {insight}")

    report.append("")
    report.append("=" * 60)
    report.append("SentinelX Zero Trust Platform")
    report.append("AI-Powered Network Threat Intelligence")
    report.append("=" * 60)

    # ======================================================
    # Print Report
    # ======================================================

    report_text = "\n".join(report)

    print(report_text)

    # ======================================================
    # Save Report
    # ======================================================

    os.makedirs("reports", exist_ok=True)

    report_path = "reports/security_report.txt"

    with open(report_path, "w") as file:
        file.write(report_text)

    print(f"\n✅ Report saved successfully: {report_path}")


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    generate_report()
