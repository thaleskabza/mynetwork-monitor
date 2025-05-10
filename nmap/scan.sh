#!/bin/sh
echo "Running hourly Nmap scan..."
nmap -sn 192.168.0.1 -oX /nmap/scan_result.xml
echo "Scan complete."
