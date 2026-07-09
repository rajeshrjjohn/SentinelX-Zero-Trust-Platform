from dashboard.utils.monitor import get_system_health

print("=" * 50)
print("SentinelX System Monitor")
print("=" * 50)

health = get_system_health()

for key, value in health.items():
    print(f"{key:15}: {value}")
