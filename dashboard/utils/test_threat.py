from dashboard.utils.threat import classify_threat

samples = [
    (80, "UDP"),
    (250, "UDP"),
    (650, "TCP"),
    (1500, "UDP"),
    (120, "ICMP")
]

print("=" * 60)
print("SentinelX Threat Intelligence Test")
print("=" * 60)

for packet_size, protocol in samples:

    result = classify_threat(packet_size, protocol)

    print(f"""
Packet Size : {packet_size}
Protocol    : {protocol}
Severity    : {result['severity']}
Risk Score  : {result['risk_score']}
Action      : {result['action']}
----------------------------------------
""")
