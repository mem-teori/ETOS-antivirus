from __future__ import annotations

import argparse
import random
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from security.security_mapper import map_event_to_tensions


# Importer din motor – tilpas sti
try:
    from core.idk_engine import ConstitutionConfig, DecisionEngine
except ImportError:
    print("Advarsel: core.idk_engine ikke fundet – bruger placeholder-motor.")

    class ConstitutionConfig:
        def __init__(self, version: str = "security-demo-0.1") -> None:
            self.version = version

    class DecisionEngine:
        def __init__(self, config: ConstitutionConfig) -> None:
            self.config = config

        def evaluate(self, tensions: dict) -> dict:
            score = sum(tensions.values()) / 30
            return {
                "mode": "emergency" if sum(tensions.values()) > 15 else "normal",
                "score": score,
            }


def build_engine() -> DecisionEngine:
    return DecisionEngine(ConstitutionConfig(version="security-demo-0.1"))


def random_event() -> dict:
    return {
        "process": random.choice(
            ["powershell.exe", "cmd.exe", "explorer.exe", "malware.exe"]
        ),
        "cmd": "suspicious" if random.random() > 0.7 else "normal",
        "time_hour": random.randint(0, 23),
        "anomaly_score": random.uniform(0, 1),
        "whitelist_match": random.random() > 0.8,
        "impact_guess": random.choice(["low", "medium", "high", "critical"]),
        "network_conn": random.choice(["", "", "", "C2 server"]),
        "file_drop": random.random() > 0.7,
        "confidence": random.uniform(0.55, 0.95),
    }


def run_demo(iterations: int | None = None, sleep_seconds: float = 2.5) -> int:
    engine = build_engine()
    print("ETOS-Antivirus sikkerheds-demo starter ... (Ctrl+C for at stoppe)\n")

    loop_count = 0
    try:
        while iterations is None or loop_count < iterations:
            event = random_event()
            tensions = map_event_to_tensions(event)
            result = engine.evaluate(tensions)

            print(f"[{time.strftime('%H:%M:%S')}] Event: {event['process']}")
            print(f"   Tensions: {tensions}")
            print(f"   Mode: {result.get('mode', 'ukendt')}")
            print(f"   Divergence/score: {float(result.get('score', 0)):.2f}")
            print("-" * 60)

            loop_count += 1
            if iterations is None or loop_count < iterations:
                time.sleep(sleep_seconds)
    except KeyboardInterrupt:
        print("\nDemo stoppet.")
        return 130

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="ETOS-Antivirus demo runner")
    parser.add_argument(
        "--once",
        action="store_true",
        help="Kør præcis ét event og stop (god til CI/smoke test).",
    )
    parser.add_argument(
        "--iterations",
        type=int,
        default=None,
        help="Kør et bestemt antal iterationer og stop.",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=2.5,
        help="Pause mellem events i sekunder.",
    )
    args = parser.parse_args()

    iterations = 1 if args.once else args.iterations
    return run_demo(iterations=iterations, sleep_seconds=args.sleep)


if __name__ == "__main__":
    raise SystemExit(main())
