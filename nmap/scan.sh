#!/bin/sh
echo "Running hourly Nmap scan..."
nmap -sn 102.217.187.178 -oX /nmap/scan_result.xml
echo "Scan complete."
