"""
==========================================================
SentinelX v2.1
System Monitoring Engine
==========================================================
"""

import platform
import socket
from datetime import datetime

import psutil


# ==========================================================
# System Information
# ==========================================================
def get_system_info():
    """
    Returns current system information for the dashboard.
    """

    return {

        "cpu": round(psutil.cpu_percent(interval=1), 1),

        "ram": round(psutil.virtual_memory().percent, 1),

        "disk": round(psutil.disk_usage("/").percent, 1),

        "hostname": socket.gethostname(),

        "os": f"{platform.system()} {platform.release()}",

        "time": datetime.now().strftime("%d %b %Y %H:%M:%S"),

        "status": "ACTIVE"

    }


# ==========================================================
# Manual Test
# ==========================================================
if __name__ == "__main__":

    system = get_system_info()

    print("=" * 50)
    print("SentinelX System Monitor")
    print("=" * 50)

    for key, value in system.items():

        print(f"{key:12}: {value}")
