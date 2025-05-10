from sklearn.ensemble import IsolationForest
import numpy as np

def detect_anomalies(df):
    model = IsolationForest(contamination=0.01)
    X = df[["cpu", "mem"]].values
    model.fit(X)
    df["anomaly"] = model.predict(X)
    anomalies = df[df["anomaly"] == -1]
    return anomalies
