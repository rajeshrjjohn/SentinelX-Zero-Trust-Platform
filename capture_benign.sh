#!/bin/bash
# Run as root from the project root
IFACE=eth0   # change if your default route uses another interface

restore() {
  kill $TCPDUMP_PID 2>/dev/null
  iptables -D OUTPUT -p udp --dport 443 -j REJECT 2>/dev/null
  sysctl -qw net.ipv6.conf.all.disable_ipv6=0
  sysctl -qw net.ipv6.conf.default.disable_ipv6=0
  echo "Settings restored."
}
trap restore EXIT

sysctl -qw net.ipv6.conf.all.disable_ipv6=1
sysctl -qw net.ipv6.conf.default.disable_ipv6=1
iptables -I OUTPUT -p udp --dport 443 -j REJECT

rm -f data/raw/benign.pcap
tcpdump -i $IFACE -w data/raw/benign.pcap ip 2>/dev/null &
TCPDUMP_PID=$!
sleep 2

echo "Capturing for ~8 minutes. Browse normally in your browser too."
for i in $(seq 1 40); do
  curl -4 -s -o /dev/null https://example.com
  curl -4 -s -o /dev/null https://www.wikipedia.org
  curl -4 -s -o /dev/null https://en.wikipedia.org/wiki/Computer_security
  curl -4 -s -o /dev/null http://neverssl.com
  nslookup github.com > /dev/null 2>&1
  ping -4 -c 3 8.8.8.8 > /dev/null
  [ $((i % 10)) -eq 0 ] && apt-get update > /dev/null 2>&1
  echo "round $i/40, packets so far: $(tcpdump -nr data/raw/benign.pcap 2>/dev/null | wc -l)"
  sleep 8
done
