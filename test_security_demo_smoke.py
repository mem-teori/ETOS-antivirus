import subprocess
import sys
from pathlib import Path


def test_demo_runs_once_successfully():
    repo_root = Path(__file__).resolve().parents[1]
    demo_file = repo_root / "security" / "security_etos_demo.py"

    result = subprocess.run(
        [sys.executable, str(demo_file), "--once", "--sleep", "0"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        timeout=20,
    )

    assert result.returncode == 0, result.stderr
    assert "ETOS-Antivirus sikkerheds-demo starter" in result.stdout
    assert "Divergence/score:" in result.stdout
