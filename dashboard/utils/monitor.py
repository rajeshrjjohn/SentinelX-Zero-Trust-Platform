import psutil
import socket
import platform
from datetime import datetime


def get_system_health():

    cpu = psutil.cpu_percent(interval=1)

    ram = psutil.virtual_memory().percent

    disk = psutil.disk_usage("/").percent

    hostname = socket.gethostname()

    os_name = platform.system() + " " + platform.release()

    current_time = datetime.now().strftime("%d %b %Y %H:%M:%S")

    return {
        "cpu": cpu,
        "ram": ram,
        "disk": disk,
        "hostname": hostname,
        "os": os_name,
        "time": current_time,
        "status": "ACTIVE"
    }
