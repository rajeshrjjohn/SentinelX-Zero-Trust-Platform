"""
==========================================================
SentinelX v3.0
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
from flask import (
    Flask,
    render_template,
    send_file
)

from datetime import datetime

from dashboard.utils.monitor import get_system_info
from dashboard.utils.analytics import (
    dashboard_summary,
    get_ai_insights
)

from dashboard.utils.reports import (
    get_report_history,
    get_report_statistics
)

from dashboard.utils.charts import (
    protocol_chart,
    source_ip_chart,
    destination_ip_chart,
    trust_score_gauge,
    threat_chart,
    threat_trend_chart
)

from pdf_report_generator import generate_pdf_report

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

    ai_insights = get_ai_insights()

    system = get_system_info()

    reports = get_report_history()

    report_stats = get_report_statistics()

    current_time = datetime.now().strftime("%d %b %Y %H:%M:%S")

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

    trend_graph = threat_trend_chart(
        summary["packets"],
        summary["threats"]
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

        trend_graph=trend_graph,

        top_sources=summary["top_sources"],

        top_destinations=summary["top_destinations"],

        cpu=system["cpu"],

        ram=system["ram"],

        disk=system["disk"],

        hostname=system["hostname"],

        os_name=system["os"],

        system_status=system["status"],

        recent_packets=summary["recent_packets"],

        top_attacker=summary["top_attacker"],

        top_target=summary["top_target"],

        top_protocol=summary["top_protocol"],

        average_packet=summary["average_packet"],

        critical=summary["critical"],

        high=summary["high"],

        medium=summary["medium"],

        low=summary["low"],

        ai_insights=ai_insights,

        reports=reports,

        report_stats=report_stats,

        current_time=current_time,


    )

# ==========================================================
# Generate PDF Report
# ==========================================================

@app.route("/generate_report")
def generate_report_route():

    pdf_file = generate_pdf_report()

    return send_file(
        pdf_file,
        as_attachment=True
    )

# ==========================================================
# Download Existing Report
# ==========================================================

@app.route("/download_report/<filename>")
def download_report(filename):

    reports_dir = os.path.join(PROJECT_ROOT, "reports")

    file_path = os.path.join(reports_dir, filename)

    if not os.path.exists(file_path):

        return "Report not found.", 404

    return send_file(
        file_path,
        as_attachment=True
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
