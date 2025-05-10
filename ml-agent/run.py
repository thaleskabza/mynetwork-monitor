from influx_connector import fetch_metrics
from model import detect_anomalies

def main():
    df = fetch_metrics()
    anomalies = detect_anomalies(df)
    print("=== ANOMALIES DETECTED ===")
    print(anomalies[["time", "cpu", "mem"]])

if __name__ == "__main__":
    main()
