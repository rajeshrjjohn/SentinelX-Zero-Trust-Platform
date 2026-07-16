"""
==========================================================
SentinelX v3.0
Charts Engine
AI-Powered Zero Trust Threat Detection Platform
==========================================================
"""

import plotly.express as px
import plotly.graph_objects as go


# ==========================================================
# Protocol Distribution
# ==========================================================
def protocol_chart(protocols):

    if not protocols:
        return "<h3>No Protocol Data Available</h3>"

    fig = px.pie(
        names=list(protocols.keys()),
        values=list(protocols.values()),
        hole=0.45,
        title="Protocol Distribution"
    )

    fig.update_layout(
        paper_bgcolor="#161b22",
        plot_bgcolor="#161b22",
        font_color="white",
        height=420
    )

    return fig.to_html(full_html=False)


# ==========================================================
# Top Source IP Chart
# ==========================================================
def source_ip_chart(source_ips):

    if not source_ips:
        return "<h3>No Source IP Data</h3>"

    fig = px.bar(
        x=list(source_ips.keys()),
        y=list(source_ips.values()),
        labels={
            "x": "Source IP",
            "y": "Packets"
        },
        title="Top Source IPs"
    )

    fig.update_layout(
        paper_bgcolor="#161b22",
        plot_bgcolor="#161b22",
        font_color="white",
        height=400
    )

    return fig.to_html(full_html=False)


# ==========================================================
# Top Destination IP Chart
# ==========================================================
def destination_ip_chart(destination_ips):

    if not destination_ips:
        return "<h3>No Destination IP Data</h3>"

    fig = px.bar(
        x=list(destination_ips.keys()),
        y=list(destination_ips.values()),
        labels={
            "x": "Destination IP",
            "y": "Packets"
        },
        title="Top Destination IPs"
    )

    fig.update_layout(
        paper_bgcolor="#161b22",
        plot_bgcolor="#161b22",
        font_color="white",
        height=400
    )

    return fig.to_html(full_html=False)


# ==========================================================
# Trust Score Gauge
# ==========================================================
def trust_score_gauge(score):

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=score,

        title={"text": "Network Trust Score"},

        gauge={
            "axis": {
                "range": [0, 100]
            },

            "bar": {
                "color": "limegreen"
            },

            "steps": [

                {
                    "range": [0, 40],
                    "color": "#ff4444"
                },

                {
                    "range": [40, 70],
                    "color": "#ffaa00"
                },

                {
                    "range": [70, 100],
                    "color": "#00cc66"
                }

            ]
        }

    ))

    fig.update_layout(
        paper_bgcolor="#161b22",
        font_color="white",
        height=420
    )

    return fig.to_html(full_html=False)


# ==========================================================
# Threat Summary
# ==========================================================
def threat_chart(threats, trusted):

    fig = px.bar(

        x=["Threats", "Trusted"],

        y=[threats, trusted],

        color=["Threats", "Trusted"],

        title="Threat Summary"

    )

    fig.update_layout(

        paper_bgcolor="#161b22",

        plot_bgcolor="#161b22",

        font_color="white",

        showlegend=False,

        height=400

    )


# ======================================================
# Threat Trend Chart
# ======================================================

import plotly.graph_objects as go


def threat_trend_chart(total_packets, threats):

    trusted = total_packets - threats

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=["Packets", "Threats", "Trusted"],
        y=[total_packets, threats, trusted],
        mode="lines+markers",
        name="Network Activity"
    ))

    fig.update_layout(

        title="Threat Trend Analytics",

        template="plotly_dark",

        height=350,

        margin=dict(l=20, r=20, t=50, b=20)

    )

    return fig.to_html(full_html=False)
