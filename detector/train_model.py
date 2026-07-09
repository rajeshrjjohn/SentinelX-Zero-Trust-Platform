import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest

df = pd.read_csv(
    "data/network.csv"
)

X = df[
    [
        "packet_length",
        "protocol"
    ]
]

model = IsolationForest(
    contamination=0.05,
    random_state=42
)

model.fit(X)

joblib.dump(
    model,
    "models/anomaly_model.pkl"
)

print("Model Saved Successfully")
