import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest
from sentinelx.config import DATA_DIR, MODELS_DIR

PROTOCOL_MAP = {"TCP": 6, "UDP": 17, "ICMP": 1}

df = pd.read_csv(DATA_DIR / "network.csv")
df["packet_length"] = df["Packet_Size"]
df["protocol"] = df["Protocol"].map(PROTOCOL_MAP).fillna(0)

X = df[["packet_length", "protocol"]]

model = IsolationForest(contamination=0.05, random_state=42)
model.fit(X)

joblib.dump(model, MODELS_DIR / "anomaly_model.pkl")
print("Model Saved Successfully")
