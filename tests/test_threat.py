"""Tests for sentinelx.dashboard.utils.threat.classify_threat"""
import pytest
from sentinelx.dashboard.utils.threat import classify_threat

VALID_SEVERITIES = {"NONE", "LOW", "MEDIUM", "HIGH", "CRITICAL"}


@pytest.mark.parametrize("packet_size,protocol", [
    (80, "UDP"),
    (250, "UDP"),
    (650, "TCP"),
    (1500, "UDP"),
    (120, "ICMP"),
])
def test_classify_threat_returns_well_formed_result(packet_size, protocol):
    result = classify_threat(packet_size, protocol)
    assert isinstance(result, dict)
    assert set(result.keys()) >= {"severity", "risk_score", "action"}
    assert result["severity"] in VALID_SEVERITIES
    assert isinstance(result["risk_score"], (int, float))
    assert 0 <= result["risk_score"] <= 100


def test_classify_threat_larger_packets_tend_toward_higher_risk():
    """Sanity check: a 1500-byte packet shouldn't score lower risk than a 80-byte one,
    given the severity tiers observed in live_detector.py (MEDIUM/HIGH/CRITICAL by size)."""
    small = classify_threat(80, "UDP")
    large = classify_threat(1500, "UDP")
    assert large["risk_score"] >= small["risk_score"]
