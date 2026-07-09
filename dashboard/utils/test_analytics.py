# ==========================================================
# SentinelX Analytics Engine Test
# ==========================================================

from analytics import (
    dashboard_summary,
    load_network_data,
    get_packet_count,
    get_threat_count,
    get_average_packet_size,
    get_protocol_stats,
    get_top_source_ips,
    get_top_destination_ips,
    calculate_trust_score,
    get_recent_alerts
)

print("=" * 70)
print("         SentinelX Analytics Engine Test")
print("=" * 70)

# Load network data
df = load_network_data()

# Basic Statistics
packets = get_packet_count(df)
threats = get_threat_count()
average_size = get_average_packet_size(df)
trust_score = calculate_trust_score(packets, threats)

print(f"\n📦 Total Packets          : {packets}")
print(f"🚨 Total Threats          : {threats}")
print(f"📏 Average Packet Size    : {average_size} bytes")
print(f"🛡 Trust Score            : {trust_score}%")

print("\n" + "=" * 70)
print("Protocol Statistics")
print("=" * 70)

protocols = get_protocol_stats(df)

if protocols:
    for protocol, count in protocols.items():
        print(f"{protocol:<10} : {count}")
else:
    print("No protocol data found.")

print("\n" + "=" * 70)
print("Top Source IPs")
print("=" * 70)

sources = get_top_source_ips(df)

if sources:
    for ip, count in sources.items():
        print(f"{ip:<20} {count} packets")
else:
    print("No source IPs found.")

print("\n" + "=" * 70)
print("Top Destination IPs")
print("=" * 70)

destinations = get_top_destination_ips(df)

if destinations:
    for ip, count in destinations.items():
        print(f"{ip:<20} {count} packets")
else:
    print("No destination IPs found.")

print("\n" + "=" * 70)
print("Recent Threat Alerts")
print("=" * 70)

alerts = get_recent_alerts()

if alerts:
    for alert in alerts:
        print(alert.strip())
else:
    print("No alerts found.")

print("\n" + "=" * 70)
print("Dashboard Summary Dictionary")
print("=" * 70)

summary = dashboard_summary()

for key, value in summary.items():
    print(f"{key} : {value}")

print("\n" + "=" * 70)
print("✅ SentinelX Analytics Engine Test Completed Successfully")
print("=" * 70)
