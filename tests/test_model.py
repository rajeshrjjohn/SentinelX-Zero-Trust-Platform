"""
Tests for the saved anomaly detection model (models/anomaly_model.pkl).

Run with: python -m pytest tests/ -v
"""

import joblib
import pytest
from sentinelx.config import MODELS_DIR

MODEL_PATH = MODELS_DIR / "anomaly_model.pkl"


@pytest.fixture(scope="module")
def model():
    if not MODEL_PATH.exists():
        pytest.skip(f"Model file not found at {MODEL_PATH} — train it first with train_model.py")
    return joblib.load(MODEL_PATH)


def test_model_file_exists():
    assert MODEL_PATH.exists(), f"Expected trained model at {MODEL_PATH}"


def test_model_has_expected_feature_count(model):
    assert model.n_features_in_ == 2


def test_model_has_expected_feature_names(model):
    if hasattr(model, "feature_names_in_"):
        names = list(model.feature_names_in_)
        assert names == ["packet_length", "protocol"], (
            f"Model was trained on {names}, but live_detector.py feeds it "
            f"['packet_length', 'protocol'] — retrain if these don't match."
        )


def test_model_predicts_without_error(model):
    import pandas as pd
    sample = pd.DataFrame({"packet_length": [100], "protocol": [6]})
    prediction = model.predict(sample)
    assert prediction[0] in (-1, 1)
