"""Tests for sentinelx.dashboard.utils.monitor.get_system_info"""
from sentinelx.dashboard.utils.monitor import get_system_info


def test_get_system_info_returns_dict():
    info = get_system_info()
    assert isinstance(info, dict)
    assert len(info) > 0


def test_get_system_info_values_are_simple_types():
    info = get_system_info()
    for key, value in info.items():
        assert isinstance(key, str)
        assert isinstance(value, (str, int, float, bool))
