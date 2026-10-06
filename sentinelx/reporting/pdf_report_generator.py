"""
==========================================================
SentinelX PDF Security Report Generator
==========================================================
"""

import os
from datetime import datetime

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

from dashboard.utils.analytics import (
    dashboard_summary,
    get_ai_insights
)

# ======================================================
# PDF Styles
# ======================================================

styles = getSampleStyleSheet()

# ======================================================
# Get Next Report Name
# ======================================================

def get_next_report_name():

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    reports_dir = os.path.join(BASE_DIR, "reports")

    os.makedirs(reports_dir, exist_ok=True)

    existing = [

        file

        for file in os.listdir(reports_dir)

        if file.startswith("security_report_")
        and file.endswith(".pdf")

    ]

    if not existing:

        return os.path.join(
            reports_dir,
            "security_report_001.pdf"
        )

    numbers = []

    for file in existing:

        try:

            number = int(

                file.replace(
                    "security_report_",
                    ""
                ).replace(".pdf", "")

            )

            numbers.append(number)

        except ValueError:

            pass

    next_number = max(numbers) + 1 if numbers else 1

    return os.path.join(

        reports_dir,

        f"security_report_{next_number:03d}.pdf"

    )


# ======================================================
# Generate PDF Report
# ======================================================

def generate_pdf_report():

    summary = dashboard_summary()

    insights = get_ai_insights()

    pdf_file = get_next_report_name()

    doc = SimpleDocTemplate(pdf_file)

    story = []

    # ==================================================
    # Title
    # ==================================================

    story.append(

        Paragraph(

            "<b>SentinelX Zero Trust Security Report</b>",

            styles["Title"]

        )

    )

    story.append(

        Paragraph(

            f"Generated On : {datetime.now().strftime('%d %b %Y %H:%M:%S')}",

            styles["BodyText"]

        )

    )

    story.append(Spacer(1, 20))

    # ==================================================
    # Network Summary
    # ==================================================

    story.append(

        Paragraph(

            "<b>Network Summary</b>",

            styles["Heading2"]

        )

    )

    story.append(
        Paragraph(
            f"Total Packets : {summary['packets']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Threat Events : {summary['threats']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Trusted Traffic : {summary['trusted']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Trust Score : {summary['trust_score']}%",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Average Packet Size : {summary['average_packet_size']} Bytes",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 20))

    # ==================================================
    # Threat Severity
    # ==================================================

    story.append(

        Paragraph(

            "<b>Threat Severity</b>",

            styles["Heading2"]

        )

    )

    story.append(
        Paragraph(
            f"Critical : {summary['critical']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"High : {summary['high']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Medium : {summary['medium']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Low : {summary['low']}",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 20))

    # ==================================================
    # Threat Intelligence
    # ==================================================

    story.append(

        Paragraph(

            "<b>Threat Intelligence</b>",

            styles["Heading2"]

        )

    )

    story.append(
        Paragraph(
            f"Top Attacker : {summary['top_attacker']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Top Target : {summary['top_target']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Top Protocol : {summary['top_protocol']}",
            styles["BodyText"]
        )
    )

    story.append(
        Paragraph(
            f"Average Packet : {summary['average_packet']} Bytes",
            styles["BodyText"]
        )
    )

    story.append(Spacer(1, 20))

    # ==================================================
    # AI Security Insights
    # ==================================================

    story.append(

        Paragraph(

            "<b>AI Security Insights</b>",

            styles["Heading2"]

        )

    )

    for insight in insights:

        story.append(

            Paragraph(

                f"• {insight}",

                styles["BodyText"]

            )

        )

    story.append(Spacer(1, 20))

    # ==================================================
    # Footer
    # ==================================================

    story.append(

        Paragraph(

            "<b>SentinelX Zero Trust Platform</b>",

            styles["Heading2"]

        )

    )

    story.append(

        Paragraph(

            "AI-Powered Network Threat Intelligence",

            styles["BodyText"]

        )

    )

    doc.build(story)

    print("=" * 60)
    print("✅ PDF Report Generated Successfully")
    print(f"📄 Saved As : {pdf_file}")
    print("=" * 60)


    return pdf_file

# ======================================================
# Main
# ======================================================

if __name__ == "__main__":

    generate_pdf_report()
