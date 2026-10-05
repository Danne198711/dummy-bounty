import os
import subprocess
import sys


def test_original_baseline_is_red(tmp_path, request):
    (tmp_path / "calculator.py").write_text(
        "def add_numbers(a, b):\n    return a - b\n"
    )
    (tmp_path / "test_original.py").write_text(
        "from calculator import add_numbers\n\n"
        "def test_add():\n    assert add_numbers(2, 2) == 4\n"
    )
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "test_original.py"],
        cwd=tmp_path,
        env={**os.environ, "PYTHONPATH": str(tmp_path),
             "PYTEST_DISABLE_PLUGIN_AUTOLOAD": "1"},
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert result.returncode == 1, result.stdout + result.stderr
    assert "1 failed" in result.stdout, result.stdout
    request.config.pluginmanager.get_plugin("terminalreporter").write_line(
        "BASELINE_RED: original subtraction bug reproduced; 1 failed"
    )
