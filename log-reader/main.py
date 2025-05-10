import time
import os

def monitor_log(file_path):
    print(f"Watching {file_path} for suspicious activity...")
    with open(file_path, 'r') as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if not line:
                time.sleep(1)
                continue
            if "unauthorized" in line.lower() or "dns flood" in line.lower():
                print(f"ALERT: {line.strip()}")  # Expand to email, Telegram, etc.

if __name__ == "__main__":
    monitor_log("/logs/pihole.log")
