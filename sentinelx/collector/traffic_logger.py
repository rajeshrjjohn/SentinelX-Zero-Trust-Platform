import csv
import os
from datetime import datetime
from sentinelx.config import DATA_DIR

CSV_FILE = DATA_DIR / "network.csv"


def initialize_csv():
    if not CSV_FILE.exists():
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Time", "Source_IP", "Destination_IP", "Protocol", "Packet_Size"])


def log_packet(src, dst, proto, size):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, src, dst, proto, size])
