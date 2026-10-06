import csv
import os
from datetime import datetime

CSV_FILE = "data/network.csv"


# ======================================================
# Initialize CSV File
# ======================================================
def initialize_csv():

    if not os.path.exists(CSV_FILE):

        with open(CSV_FILE, "w", newline="") as f:

            writer = csv.writer(f)

            writer.writerow([
                "Time",
                "Source_IP",
                "Destination_IP",
                "Protocol",
                "Packet_Size"
            ])


# ======================================================
# Log Packet
# ======================================================
def log_packet(src, dst, proto, size):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(CSV_FILE, "a", newline="") as f:

        writer = csv.writer(f)

        writer.writerow([
            timestamp,
            src,
            dst,
            proto,
            size
        ])
