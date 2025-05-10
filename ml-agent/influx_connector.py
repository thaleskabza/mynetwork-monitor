from influxdb import InfluxDBClient
import pandas as pd

def fetch_metrics():
    client = InfluxDBClient(host="influxdb", port=8086, database="network_monitor")
    query = "SELECT mean(usage_system) AS cpu, mean(used_percent) AS mem FROM cpu,mem WHERE time > now() - 6h GROUP BY time(1m) fill(null)"
    result = client.query(query)
    cpu_points = result.get_points(measurement="cpu")
    mem_points = result.get_points(measurement="mem")

    df_cpu = pd.DataFrame(cpu_points)
    df_mem = pd.DataFrame(mem_points)
    df = pd.merge(df_cpu, df_mem, on='time')
    return df.dropna()
