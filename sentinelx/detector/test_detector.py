from live_detector import detect_packet

tests = [
    (60, "TCP"),
    (120, "UDP"),
    (500, "TCP"),
    (1500, "UDP"),
    (80, "ICMP")
]

for length, proto in tests:
    result = detect_packet(length, proto)
    print(f"{length} bytes | {proto} -> {result}")
