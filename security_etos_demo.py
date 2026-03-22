# security/security_etos_demo.py
import time
import random
from security_mapper import map_event_to_tensions

# Importer din motor – tilpas sti
try:
    from idk_engine import DecisionEngine, ConstitutionConfig
except ImportError:
    print("Advarsel: idk_engine ikke fundet – brug placeholder")

    class ConstitutionConfig:
        def __init__(self, version="security-demo-0.1"):
            self.version = version

    class DecisionEngine:
        def __init__(self, config):
            self.config = config

        def evaluate(self, tensions):
            return {
                "mode": "emergency" if sum(tensions.values()) > 15 else "normal",
                "score": sum(tensions.values()) / 30,
            }

engine = DecisionEngine(ConstitutionConfig(version="security-demo-0.1"))

def random_event():
    return {
        "process": random.choice(["powershell.exe", "cmd.exe", "explorer.exe", "malware.exe"]),
        "cmd": "suspicious" if random.random() > 0.7 else "normal",
        "time_hour": random.randint(0, 23),
        "anomaly_score": random.uniform(0, 1),
        "whitelist_match": random.random() > 0.8,
        "impact_guess": random.choice(["low", "medium", "high", "critical"]),
    }

print("ETOS-AD sikkerheds-demo starter ... (Ctrl+C for at stoppe)\n")

try:
    while True:
        event = random_event()
        tensions = map_event_to_tensions(event)
        result = engine.evaluate(tensions)

        print(f"[{time.strftime('%H:%M:%S')}] Event: {event['process']}")
        print(f"   Tensions: {tensions}")
        print(f"   Mode: {result.get('mode', 'ukendt')}")
        print(f"   Divergence/score: {result.get('score', 0):.2f}")
        print("-" * 60)

        time.sleep(2.5)
except KeyboardInterrupt:
    print("\nDemo stoppet.")
