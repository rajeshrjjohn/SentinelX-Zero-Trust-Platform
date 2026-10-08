# 🛡 SentinelX Zero Trust Platform v3.0

<p align="center">

<img src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python">

<img src="https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask">

<img src="https://img.shields.io/badge/Scapy-Packet%20Capture-red?style=for-the-badge">

<img src="https://img.shields.io/badge/Scikit--Learn-Isolation%20Forest-green?style=for-the-badge">

<img src="https://img.shields.io/badge/Plotly-Interactive%20Charts-blueviolet?style=for-the-badge">

<img src="https://img.shields.io/badge/Kali%20Linux-Security%20Platform-success?style=for-the-badge">

<img src="https://img.shields.io/badge/Version-v3.0-brightgreen?style=for-the-badge">

</p>

---

# 🚀 AI-Powered Zero Trust Network Threat Intelligence Platform

SentinelX is an enterprise-inspired cybersecurity platform that performs **real-time network monitoring**, **AI-powered anomaly detection**, **Zero Trust traffic analysis**, and **automated security reporting**.

The platform continuously captures live network packets, analyzes traffic using Machine Learning, classifies potential threats, and presents security insights through an interactive Security Operations Center (SOC) dashboard.

SentinelX was developed as a practical cybersecurity project to demonstrate modern concepts such as:

- Zero Trust Architecture
- AI-based Threat Detection
- Network Traffic Analysis
- Threat Intelligence
- Security Automation
- Security Reporting

---

# 📑 Table of Contents

- Project Overview
- Why SentinelX?
- Key Features
- Technology Stack
- System Architecture
- Workflow
- Project Structure
- Installation Guide
- Requirements
- Running the Project
- Dashboard Overview
- AI Threat Detection
- Packet Capture Module
- Threat Intelligence
- AI Security Insights
- Protocol Distribution
- Threat Trend Analytics
- Live Packet Activity
- System Health Monitoring
- PDF Report Generator
- Report History
- Screenshots
- Future Improvements
- License
- Author
- Acknowledgements

---

# 📌 Project Overview

Modern organizations generate millions of network packets every day.

Traditional monitoring solutions often require expensive commercial software and complex infrastructure.

SentinelX demonstrates how an intelligent security monitoring platform can be built using open-source technologies.

The platform combines:

- Real-Time Packet Capture
- Machine Learning
- Zero Trust Security
- Threat Intelligence
- Interactive Visualization
- Automated Reporting

into a single lightweight solution.

---

# ❓ Why SentinelX?

Most student cybersecurity projects focus on only one area:

- Packet Capture
- Machine Learning
- Dashboard
- Reporting

SentinelX combines all of these into one integrated platform.

It provides:

- Continuous monitoring
- AI-assisted threat detection
- Real-time visualization
- Automated report generation
- Security analytics
- System monitoring

making it resemble a lightweight Security Operations Center (SOC).

---

# ✨ Key Features

## 🌐 Network Monitoring

- Live Packet Capture using Scapy
- Source IP Detection
- Destination IP Detection
- Protocol Identification
- Packet Size Analysis
- Continuous Monitoring

---

## 🤖 AI Threat Detection

- Isolation Forest Machine Learning Model
- Anomaly Detection
- Risk Score Calculation
- Threat Classification
- Zero Trust Decision Engine

---

## 📊 Interactive Dashboard

Professional Flask Dashboard including:

- Network Statistics
- Threat Counters
- Trust Score
- CPU Monitoring
- RAM Monitoring
- Disk Monitoring
- Threat Charts
- Protocol Distribution
- Live Traffic Table
- AI Security Insights

---

## 📈 Analytics

SentinelX automatically generates

- Threat Trend Analytics
- Protocol Statistics
- Top Source IPs
- Top Destination IPs
- Packet Statistics
- Trust Score Analytics

---

## 🛡 Threat Intelligence

Displays

- Top Attacker
- Top Target
- Most Used Protocol
- Average Packet Size
- Threat Severity
- Threat Distribution

---

## 📄 Professional PDF Reports

Automatically generates numbered security reports.

Each report includes

- Executive Summary
- Network Statistics
- Threat Summary
- Threat Intelligence
- AI Security Insights
- Trust Score
- Timestamp
- Platform Version

Example

security_report_001.pdf

security_report_002.pdf

security_report_003.pdf

...

security_report_010.pdf

---

## 📂 Report History

Maintains a searchable report history.

Features include

- Automatic Numbering
- Search
- Download
- Storage Usage
- Latest Report
- Report Statistics

---

# 🛠 Technology Stack

| Category | Technology |
|------------|----------------|
| Language | Python 3.13 |
| Framework | Flask |
| Packet Capture | Scapy |
| Machine Learning | Scikit-Learn |
| AI Algorithm | Isolation Forest |
| Data Processing | Pandas |
| Charts | Plotly |
| Reports | ReportLab |
| Operating System | Kali Linux |
| Version Control | Git & GitHub |

---

# 🏗 System Architecture

```text
                   Internet

                       │

                       ▼

            Scapy Packet Capture

                       │

                       ▼

              Traffic Collection

                       │

                       ▼

             Feature Extraction

                       │

                       ▼

        Isolation Forest AI Engine

                       │

            ┌──────────┼──────────┐

            ▼          ▼          ▼

      Threat Engine Dashboard PDF Reports

                       │

                       ▼

              Report History
```

---

# 🔄 System Workflow

```text
Capture Packets

        │

        ▼

Extract Features

        │

        ▼

AI Prediction

        │

        ▼

Threat Classification

        │

        ▼

Threat Intelligence

        │

        ▼

Dashboard Visualization

        │

        ▼

Generate Security Report

        │

        ▼

Store Report History
```

---

# 📂 Project Structure

```text
SentinelX-Zero-Trust-Platform

│

├── collector/

├── dashboard/

│   ├── templates/

│   ├── static/

│   └── utils/

├── detector/

├── models/

├── data/

├── logs/

├── reports/

├── screenshots/

├── zerotrust/

├── report_generator.py

├── pdf_report_generator.py

├── run.py

├── requirements.txt

└── README.md
```
---

# ⚙️ Installation Guide

## Prerequisites

Before running SentinelX, ensure the following software is installed.

| Software | Version |
|----------|---------|
| Python | 3.13+ |
| Git | Latest |
| Kali Linux | Recommended |
| pip | Latest |

---

## Clone Repository

```bash
git clone https://github.com/rajeshrjjohn/SentinelX-Zero-Trust-Platform.git

cd SentinelX-Zero-Trust-Platform
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Project Requirements

The project uses the following major libraries.

- Flask
- Scapy
- Pandas
- NumPy
- Plotly
- Scikit-Learn
- ReportLab
- Joblib
- Psutil

Install manually if required:

```bash
pip install flask scapy pandas numpy plotly scikit-learn reportlab joblib psutil
```

---

# 🚀 Running SentinelX

## Step 1

Start Packet Capture

```bash
python3 collector/packet_capture.py
```

---

## Step 2

Run AI Detection

```bash
python3 detector/live_detector.py
```

---

## Step 3

Launch Dashboard

```bash
python3 dashboard/app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## Step 4

Generate Security Report

Click

```
Generate PDF Report
```

or

```bash
python3 pdf_report_generator.py
```

---

# 📊 Dashboard Overview

The SentinelX dashboard provides complete visibility into the monitored network.

Main dashboard modules include

- Network Packet Statistics
- Threat Event Counter
- Trusted Traffic Counter
- Trust Score
- CPU Usage
- RAM Usage
- Disk Usage
- Threat Severity Summary
- Interactive Charts
- Threat Intelligence
- AI Security Insights
- Live Packet Activity
- Report History
- PDF Report Generator

---

# 🤖 AI Threat Detection

SentinelX uses the **Isolation Forest** machine learning algorithm for anomaly detection.

### Detection Workflow

```
Captured Packet

        │

        ▼

Feature Extraction

        │

        ▼

Isolation Forest Prediction

        │

        ▼

Threat Classification

        │

        ▼

Dashboard Update

        │

        ▼

Security Report
```

### Threat Levels

| Severity | Action |
|-----------|---------|
| Low | Monitor |
| Medium | Monitor |
| High | Block |
| Critical | Block |

---

# 📡 Scapy Packet Capture

Scapy is responsible for real-time network monitoring.

Captured information includes

- Source IP
- Destination IP
- Protocol
- Packet Size
- Timestamp

Supported protocols

- TCP
- UDP
- ICMP

---

# 🛡 Threat Intelligence

SentinelX continuously generates threat intelligence.

The dashboard displays

- Top Attacker
- Top Target
- Most Active Protocol
- Average Packet Size
- Threat Distribution
- Trust Score

This allows administrators to quickly identify suspicious activity.

---

# 🧠 AI Security Insights

The AI Insights engine provides recommendations based on observed traffic.

Example insights

- Network operating normally.
- No active threats detected.
- ICMP traffic dominates the network.
- Continue monitoring suspicious hosts.
- Maintain Zero Trust policy.

---

# 📈 Threat Trend Analytics

Interactive Plotly charts provide

- Threat Trend
- Protocol Distribution
- Source IP Analysis
- Destination IP Analysis
- Trust Score Visualization

All charts update automatically with new data.

---

# 🌐 Protocol Distribution

The platform visualizes network protocols.

Supported visualization

- TCP
- UDP
- ICMP

This helps identify unusual protocol usage.

---

# 📦 Live Packet Activity

Displays recently captured packets.

Each record contains

- Time
- Source IP
- Destination IP
- Protocol
- Packet Size

The table updates automatically as traffic is captured.

---

# 💻 System Health Monitoring

SentinelX also monitors system resources.

Metrics include

- CPU Usage
- RAM Usage
- Disk Usage
- Platform Version
- System Status

This helps ensure the monitoring server remains healthy.

---

# 📄 PDF Report Generator

SentinelX automatically generates professional security reports.

Each generated report contains

- Executive Summary
- Network Statistics
- Threat Summary
- Trust Score
- Threat Intelligence
- AI Security Insights
- System Health
- Generation Time
- Platform Version

Reports are automatically numbered.

Example

```
security_report_001.pdf

security_report_002.pdf

security_report_003.pdf

...

security_report_010.pdf
```

---

# 📂 Report History

All generated reports are stored in the Report History module.

Features

- Search
- Download
- Automatic Numbering
- Storage Statistics
- Latest Report Information

This allows previous reports to be reviewed at any time.

---

# 📸 Screenshots

## Dashboard

```
screenshots/dashboard_home.png
```

---

## Threat Intelligence

```
screenshots/threat_intelligence.png
```

---

## Live Packet Activity

```
screenshots/live_packet_activity.png
```

---

## AI Security Insights

```
screenshots/ai_security_insights.png
```

---

## Report History

```
screenshots/report_history.png
```

---

## PDF Report

```
screenshots/pdf_report.png
```

---

# 🚀 Future Improvements

Future versions of SentinelX may include

- Email Alert Notifications
- SMS Alerting
- SIEM Integration
- Threat Feed Integration
- MITRE ATT&CK Mapping
- User Authentication
- Role-Based Access Control
- Docker Deployment
- Kubernetes Support
- Cloud Deployment
- REST API
- Mobile Dashboard
- Threat Hunting Module

---

# 👨‍💻 Author

**Rajesh**

Cybersecurity Engineer

Specializations

- Penetration Testing
- Network Security
- Zero Trust Security
- Threat Detection
- Python Development
- Machine Learning for Cybersecurity

GitHub

https://github.com/rajeshrjjohn

---

# 📜 License

This project is released under the MIT License.

Feel free to learn from it, modify it, and contribute while giving appropriate credit.

---

# 🙏 Acknowledgements

Special thanks to

- Flask
- Scapy
- Plotly
- Scikit-Learn
- ReportLab
- Python Community
- Kali Linux Team
- Open Source Community

---

# ⭐ Support

If you found this project useful,

⭐ Star this repository

🍴 Fork the repository

🐛 Report issues

💡 Suggest improvements

---

# 🛡 SentinelX Zero Trust Platform v3.0

> "Trust Nothing. Verify Everything."

Built with ❤️ using Python, Flask, Machine Learning, and Zero Trust Security.
