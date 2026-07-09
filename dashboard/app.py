"""
==========================================================
SentinelX v2.0
AI-Powered Zero Trust Threat Detection Platform
Dashboard Application
==========================================================
"""

import os
import sys

# ==========================================================
# Add Project Root to Python Path
# ==========================================================
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# ==========================================================
# Imports
# ==========================================================
from flask import Flask, render_template

from dashboard.utils.analytics import dashboard_summary

from dashboard.utils.charts import (
    protocol_chart,
    source_ip_chart,
    destination_ip_chart,
    trust_score_gauge,
    threat_chart
)

# ==========================================================
# Flask App
# ==========================================================
app = Flask(__name__)

# ==========================================================
# Dashboard
# ==========================================================
@app.route("/")
def dashboard():

    summary = dashboard_summary()

    protocol_graph = protocol_chart(
        summary["protocols"]
    )

    source_graph = source_ip_chart(
        summary["top_sources"]
    )

    destination_graph = destination_ip_chart(
        summary["top_destinations"]
    )

    trust_graph = trust_score_gauge(
        summary["trust_score"]
    )

    threat_graph = threat_chart(
        summary["threats"],
        summary["trusted"]
    )

    return render_template(

        "index.html",

        packets=summary["packets"],

        threats=summary["threats"],

        trusted=summary["trusted"],

        trust_score=summary["trust_score"],

        average_packet_size=summary["average_packet_size"],

        alerts=summary["recent_alerts"],

        protocol_graph=protocol_graph,

        source_graph=source_graph,

        destination_graph=destination_graph,

        trust_graph=trust_graph,

        threat_graph=threat_graph,

        top_sources=summary["top_sources"],

        top_destinations=summary["top_destinations"]

    )


# ==========================================================
# Health API
# ==========================================================
@app.route("/health")
def health():

    return {

        "Platform": "SentinelX",

        "Version": "2.0",

        "Status": "ACTIVE",

        "AI Engine": "Isolation Forest",

        "Dashboard": "Online"

    }


# ==========================================================
# Run Server
# ==========================================================
if __name__ == "__main__":

    print("=" * 60)
    print("SentinelX Zero Trust Platform")
    print("AI-Powered Network Threat Intelligence")
    print("=" * 60)

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )
