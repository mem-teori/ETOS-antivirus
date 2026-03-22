# security/security_mapper.py
"""
Mapper der konverterer sikkerheds-events til IDK-parametre (0–5 skala)
Genbruger eksisterende DecisionEngine uden at ændre den.
"""

def map_event_to_tensions(event: dict) -> dict:
    """
    event eksempel:
    {
        "process": "powershell.exe",
        "cmd": "encoded base64 ...",
        "time_hour": 3,
        "user": "admin",
        "file_drop": True,
        "network_conn": "C2 server",
        "impact_guess": "high",   # fra heuristik/ML
        "anomaly_score": 0.87,
        "whitelist_match": False,
    }
    """
    tensions = {}

    # coercion → containment_aggressiveness
    if event.get("network_conn") or event.get("ransomware_indicators"):
        tensions["coercion"] = 5
    elif event.get("file_drop") or "powershell" in event.get("process", "").lower():
        tensions["coercion"] = 4
    else:
        tensions["coercion"] = 1 + int(event.get("anomaly_score", 0) * 4)

    # refusal → false_positive_risk
    if event.get("whitelist_match") or event.get("signed", False):
        tensions["refusal"] = 4  # høj risiko for FP
    else:
        tensions["refusal"] = 1

    # capacity → detection_confidence (inverteret: høj usikkerhed = høj værdi)
    tensions["capacity"] = int((1 - event.get("confidence", 0.8)) * 5)

    # risk → impact_potential
    impact_map = {"low": 1, "medium": 3, "high": 5, "critical": 5}
    tensions["risk"] = impact_map.get(event.get("impact_guess", "medium"), 3)

    # time → response_urgency
    if event.get("time_hour", 12) in (0, 1, 2, 3, 4):
        tensions["time"] = 5  # nat = høj urgency
    elif "live" in event.get("network_conn", ""):
        tensions["time"] = 5
    else:
        tensions["time"] = 2

    # advance_directive → policy / known-good
    tensions["advance_directive"] = 5 if event.get("whitelist_match") else 0

    return tensions
