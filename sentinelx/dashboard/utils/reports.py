"""
==========================================================
Report History Utilities
==========================================================
"""

import os
from datetime import datetime

BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../.."
    )
)

REPORTS_DIR = os.path.join(BASE_DIR, "reports")


def get_report_history():

    reports = []

    if not os.path.exists(REPORTS_DIR):
        return reports

    for file in sorted(
        os.listdir(REPORTS_DIR),
        reverse=True
    ):

        if not file.endswith(".pdf"):
            continue

        path = os.path.join(REPORTS_DIR, file)

        created = datetime.fromtimestamp(
            os.path.getmtime(path)
        ).strftime("%d %b %Y %H:%M")

        reports.append({

            "name": file,

            "created": created

        })

    return reports

# ==========================================================
# Report Statistics
# ==========================================================

def get_report_statistics():

    reports = get_report_history()

    total_reports = len(reports)

    latest_report = reports[0]["name"] if reports else "None"

    total_size = 0

    for report in reports:

        path = os.path.join(REPORTS_DIR, report["name"])

        total_size += os.path.getsize(path)

    total_size = round(total_size / (1024 * 1024), 2)

    return {

        "total_reports": total_reports,

        "latest_report": latest_report,

        "storage": total_size

    }
