import csv
import os

CSV_FILE = "data/network.csv"

def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "Source_IP",
                "Destination_IP",
                "Protocol",
                "Packet_Size"
            ])

def log_packet(src, dst, proto, size):
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([src, dst, proto, size])
