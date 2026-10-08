FROM python:3.13-slim

WORKDIR /app

# System deps for scapy/pandas builds (kept minimal)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpcap-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY sentinelx/ sentinelx/
COPY models/ models/
COPY data/network.csv data/network.csv

RUN mkdir -p logs reports

ENV FLASK_DEBUG=0
EXPOSE 5000

CMD ["python", "-m", "sentinelx.dashboard.app"]
