import joblib

model = joblib.load("models/anomaly_model.pkl")

print("Model Type:", type(model))

if hasattr(model, "feature_names_in_"):
    print("Feature Names:", model.feature_names_in_)
else:
    print("No feature names stored.")

print("Number of Features:", model.n_features_in_)
