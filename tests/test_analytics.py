"""Tests for sentinelx.dashboard.utils.analytics — contract/smoke tests.

These check that each function runs without error and returns a
reasonably-shaped result, against whatever is currently in data/network.csv
and logs/alerts.log. They don't assert exact values since those depend on
live data, but a crash or a wrong return type here means something broke.
"""
from sentinelx.dashboard.utils.analytics import (
    dashboard_summary,
    load_network_data,
    get_packet_count,
    get_threat_count,
    get_average_packet_size,
    get_protocol_stats,
    get_top_source_ips,
    get_top_destination_ips,
    calculate_trust_score,
    get_recent_alerts,
)


def test_load_network_data_returns_dataframe():
    df = load_network_data()
    assert df is not None
    assert hasattr(df, "columns")


def test_get_packet_count_is_non_negative_int():
    df = load_network_data()
    count = get_packet_count(df)
    assert isinstance(count, int)
    assert count >= 0


def test_get_threat_count_is_non_negative_int():
    count = get_threat_count()
    assert isinstance(count, int)
    assert count >= 0


def test_get_average_packet_size_is_non_negative_number():
    df = load_network_data()
    avg = get_average_packet_size(df)
    assert isinstance(avg, (int, float))
    assert avg >= 0


def test_get_protocol_stats_returns_dict_like():
    df = load_network_data()
    stats = get_protocol_stats(df)
    assert stats is not None
    assert hasattr(stats, "items")


def test_get_top_source_and_destination_ips_return_dict_like():
    df = load_network_data()
    sources = get_top_source_ips(df)
    destinations = get_top_destination_ips(df)
    assert hasattr(sources, "items")
    assert hasattr(destinations, "items")


def test_calculate_trust_score_is_bounded():
    score = calculate_trust_score(100, 5)
    assert isinstance(score, (int, float))
    assert 0 <= score <= 100


def test_calculate_trust_score_zero_threats_scores_higher_than_many_threats():
    high_trust = calculate_trust_score(100, 0)
    low_trust = calculate_trust_score(100, 50)
    assert high_trust >= low_trust


def test_get_recent_alerts_returns_list_like():
    alerts = get_recent_alerts()
    assert alerts is not None
    assert hasattr(alerts, "__iter__")


def test_dashboard_summary_returns_dict():
    summary = dashboard_summary()
    assert isinstance(summary, dict)
    assert len(summary) > 0
