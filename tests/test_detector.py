"""
Tests for sentinelx.detector.live_detector.detect_packet

Run with: python -m pytest tests/ -v
(must be run from the project root so sentinelx is importable)
"""

import pytest
from sentinelx.detector.live_detector import detect_packet, PROTOCOL_MAP


VALID_STATUSES = {"NORMAL", "THREAT", "ERROR"}
VALID_SEVERITIES = {"NONE", "LOW", "MEDIUM", "HIGH", "CRITICAL", "UNKNOWN"}
VALID_ACTIONS = {"ALLOW", "MONITOR", "BLOCK", "MODEL NOT LOADED"}


@pytest.mark.parametrize("length,protocol", [
    (60, "TCP"),
    (120, "UDP"),
    (500, "TCP"),
    (1500, "UDP"),
    (80, "ICMP"),
])
def test_detect_packet_returns_well_formed_result(length, protocol):
    result = detect_packet(length, protocol)
    assert isinstance(result, dict)
    assert set(result.keys()) >= {"status", "severity", "risk_score", "action"}
    assert result["status"] in VALID_STATUSES
    assert result["severity"] in VALID_SEVERITIES
    assert result["action"] in VALID_ACTIONS
    assert isinstance(result["risk_score"], (int, float))
    assert 0 <= result["risk_score"] <= 100


def test_detect_packet_handles_lowercase_protocol():
    result_upper = detect_packet(60, "TCP")
    result_lower = detect_packet(60, "tcp")
    assert result_upper["status"] == result_lower["status"]


def test_detect_packet_handles_unknown_protocol():
    result = detect_packet(100, "GARBAGE")
    assert result["status"] in VALID_STATUSES


def test_protocol_map_has_expected_entries():
    assert PROTOCOL_MAP["TCP"] == 6
    assert PROTOCOL_MAP["UDP"] == 17
    assert PROTOCOL_MAP["ICMP"] == 1
