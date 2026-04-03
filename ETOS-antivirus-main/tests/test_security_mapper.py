from security.security_mapper import map_event_to_tensions


def test_high_risk_network_event_maps_to_strong_response():
    event = {
        "process": "powershell.exe",
        "network_conn": "C2 server",
        "ransomware_indicators": True,
        "time_hour": 3,
        "impact_guess": "critical",
        "anomaly_score": 0.91,
        "whitelist_match": False,
        "confidence": 0.2,
    }

    tensions = map_event_to_tensions(event)

    assert tensions["coercion"] == 5
    assert tensions["risk"] == 5
    assert tensions["time"] == 5
    assert tensions["advance_directive"] == 0
    assert 0 <= tensions["capacity"] <= 5


def test_whitelisted_signed_event_increases_false_positive_protection():
    event = {
        "process": "explorer.exe",
        "signed": True,
        "whitelist_match": True,
        "impact_guess": "low",
        "time_hour": 14,
        "confidence": 0.95,
    }

    tensions = map_event_to_tensions(event)

    assert tensions["refusal"] == 4
    assert tensions["advance_directive"] == 5
    assert tensions["risk"] == 1
