# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""wazuh-manager daemon watchdog (docker/wazuh/services.d/wazuh-watchdog/run).

The manager image starts its daemons ONCE, from cont-init. On 2026-10-21 a
Colima VM bounce left dev's manager with no Wazuh daemon at all for hours,
while s6 kept filebeat alive and nothing restarted the rest. These tests drive
the real script against a fake ``wazuh-control`` whose daemon state lives in
a file, so restarts are observable without a container.
"""

from __future__ import annotations

import os
import shutil
import stat
import subprocess
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).parent.parent.parent
WATCHDOG = REPO_ROOT / "docker" / "wazuh" / "services.d" / "wazuh-watchdog" / "run"
REQUIRED = ("wazuh-remoted", "wazuh-authd", "wazuh-analysisd", "wazuh-db")

pytestmark = pytest.mark.skipif(shutil.which("sh") is None, reason="needs a POSIX sh")

# Fake wazuh-control: `status` prints from $STATE (one "name state" per line);
# `restart` appends to $CALLS and marks every daemon running unless
# $RESTART_FAILS is set.
_FAKE_CTL = """#!/bin/sh
case "$1" in
  status)
    while read -r name st; do
      [ -n "$name" ] && echo "$name is $st..."
    done < "$STATE"
    ;;
  restart)
    echo restart >> "$CALLS"
    if [ -z "$RESTART_FAILS" ]; then
      sed 's/ .*/ running/' "$STATE" > "$STATE.new" && mv "$STATE.new" "$STATE"
    fi
    ;;
esac
"""


def _run(tmp_path: Path, states: dict[str, str], loops: int, **env: str):
    ctl = tmp_path / "wazuh-control"
    ctl.write_text(_FAKE_CTL)
    ctl.chmod(ctl.stat().st_mode | stat.S_IXUSR)
    state = tmp_path / "state"
    state.write_text("".join(f"{k} {v}\n" for k, v in states.items()))
    calls = tmp_path / "calls"
    run_env = {
        "PATH": os.environ["PATH"],
        "WAZUH_CONTROL": str(ctl),
        "WAZUH_WATCHDOG_INTERVAL": "0",
        "WAZUH_WATCHDOG_MAX_LOOPS": str(loops),
        "STATE": str(state),
        "CALLS": str(calls),
        **env,
    }
    proc = subprocess.run(
        ["sh", str(WATCHDOG)], env=run_env, capture_output=True, text=True, timeout=30
    )
    restarts = len(calls.read_text().splitlines()) if calls.exists() else 0
    return proc, restarts


def _all(st: str) -> dict[str, str]:
    return {d: st for d in REQUIRED}


class TestWatchdogBehaviour:
    def test_healthy_manager_is_left_alone(self, tmp_path):
        proc, restarts = _run(tmp_path, _all("running"), loops=5)
        assert proc.returncode == 0, proc.stderr
        assert restarts == 0

    def test_all_daemons_dead_is_restarted_after_grace(self, tmp_path):
        # The 2026-10-21 dev state: nothing running.
        proc, restarts = _run(tmp_path, _all("not running"), loops=2)
        assert restarts == 1
        assert "restored" in proc.stderr

    def test_one_missing_daemon_is_enough(self, tmp_path):
        states = _all("running") | {"wazuh-analysisd": "not running"}
        proc, restarts = _run(tmp_path, states, loops=2)
        assert restarts == 1
        assert "wazuh-analysisd" in proc.stderr

    def test_single_miss_within_grace_does_not_restart(self, tmp_path):
        _, restarts = _run(tmp_path, _all("not running"), loops=1)
        assert restarts == 0

    def test_daemons_it_does_not_require_are_ignored(self, tmp_path):
        # Single-node deployment never runs these; they must not cause restarts.
        states = _all("running") | {"wazuh-clusterd": "not running", "wazuh-maild": "not running"}
        _, restarts = _run(tmp_path, states, loops=4)
        assert restarts == 0

    def test_failed_restart_is_reported_not_claimed(self, tmp_path):
        proc, restarts = _run(tmp_path, _all("not running"), loops=2, RESTART_FAILS="1")
        assert restarts == 1
        assert "still not running" in proc.stderr
        assert "restored" not in proc.stderr

    def test_keeps_retrying_while_still_down(self, tmp_path):
        _, restarts = _run(tmp_path, _all("not running"), loops=4, RESTART_FAILS="1")
        assert restarts == 2


class TestWatchdogWiring:
    def test_script_is_executable_in_git(self):
        # s6 runs services.d/<name>/run directly; a 0644 file never starts.
        mode = subprocess.run(
            ["git", "ls-files", "-s", str(WATCHDOG.relative_to(REPO_ROOT))],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.split()[0]
        assert mode == "100755"

    def test_required_daemons_match_the_healthcheck(self):
        compose = yaml.safe_load((REPO_ROOT / "docker" / "docker-compose.yml").read_text())
        hc = " ".join(compose["services"]["wazuh-manager"]["healthcheck"]["test"])
        for daemon in REQUIRED:
            assert f"{daemon} is running" in hc
            assert daemon in WATCHDOG.read_text()

    def test_mounted_into_manager_services_d(self):
        compose = yaml.safe_load((REPO_ROOT / "docker" / "docker-compose.yml").read_text())
        vols = compose["services"]["wazuh-manager"]["volumes"]
        assert "./wazuh/services.d/wazuh-watchdog:/etc/services.d/wazuh-watchdog:ro" in vols


# ── colima-health-check.sh step 4b (dev host backstop) ───────────────────────

HEALTH_CHECK = REPO_ROOT / "docker" / "scripts" / "colima-health-check.sh"

# Stubs for everything 4b touches. `docker inspect` reads $D/<name>; `docker
# restart` logs to $D/restarts and makes the container healthy unless
# $D/<name>.stuck exists. The agent turns healthy on its own once the manager
# has been restarted, unless $D/agent.independent exists.
_4B_PRELUDE = r"""
set -uo pipefail
D="$1"
log() { echo "$*"; }
sleep() { :; }
_upgrade_in_progress() { [ -f "$D/upgrade" ]; }
docker() {
  case "$1" in
    inspect) c="${@: -1}"
      if [ "$c" = "$WAZUH_AGENT_CONTAINER" ] && [ ! -f "$D/agent.independent" ] \
         && grep -qx "$WAZUH_MANAGER_CONTAINER" "$D/restarts" 2>/dev/null; then
        echo healthy; return 0
      fi
      cat "$D/$c" ;;
    restart) echo "$2" >> "$D/restarts"
      [ -f "$D/$2.stuck" ] || echo healthy > "$D/$2" ;;
  esac
}
WAZUH_MANAGER_CONTAINER=mgr
WAZUH_AGENT_CONTAINER=agt
HEALED=false
COLIMA_STARTED="${COLIMA_STARTED:-false}"
FAILURES=()
"""
_4B_EPILOGUE = r"""
echo "HEALED=$HEALED FAILURES=${#FAILURES[@]}"
"""


def _step_4b() -> str:
    text = HEALTH_CHECK.read_text()
    start = text.index("# 4b. Wazuh manager + agent")
    end = text.index("\ndone\n", start) + len("\ndone\n")
    return text[start:end]


def _run_4b(tmp_path: Path, mgr: str, agt: str, *flags: str, **env: str):
    (tmp_path / "mgr").write_text(mgr + "\n")
    (tmp_path / "agt").write_text(agt + "\n")
    for f in flags:
        (tmp_path / f).touch()
    script = tmp_path / "step4b.sh"
    script.write_text(_4B_PRELUDE + _step_4b() + _4B_EPILOGUE)
    proc = subprocess.run(
        ["bash", str(script), str(tmp_path)],
        capture_output=True,
        text=True,
        timeout=30,
        env={"PATH": os.environ["PATH"], **env},
    )
    restarts_file = tmp_path / "restarts"
    restarts = restarts_file.read_text().split() if restarts_file.exists() else []
    return proc, restarts


@pytest.mark.skipif(shutil.which("bash") is None, reason="needs bash")
class TestHealthCheckWazuhStep:
    def test_healthy_wazuh_is_checked_and_left_alone(self, tmp_path):
        proc, restarts = _run_4b(tmp_path, "healthy", "healthy")
        assert restarts == []
        assert "mgr: healthy" in proc.stdout and "agt: healthy" in proc.stdout
        assert "FAILURES=0" in proc.stdout

    def test_dead_manager_is_restarted_and_agent_is_not(self, tmp_path):
        # The 2026-10-21 dev state: both unhealthy, the agent only because of the manager.
        proc, restarts = _run_4b(tmp_path, "unhealthy", "unhealthy")
        assert restarts == ["mgr"]
        assert "agt: healthy" in proc.stdout or "recovered once the manager" in proc.stdout
        assert "HEALED=true FAILURES=0" in proc.stdout

    def test_independently_broken_agent_is_restarted(self, tmp_path):
        proc, restarts = _run_4b(tmp_path, "healthy", "unhealthy")
        assert restarts == ["agt"]
        assert "HEALED=true FAILURES=0" in proc.stdout

    def test_restart_that_does_not_recover_is_a_failure(self, tmp_path):
        proc, restarts = _run_4b(tmp_path, "unhealthy", "healthy", "mgr.stuck")
        assert restarts == ["mgr"]
        assert "HEALED=false FAILURES=1" in proc.stdout

    def test_missing_container_is_a_failure_not_silence(self, tmp_path):
        proc, restarts = _run_4b(tmp_path, "missing", "healthy")
        assert restarts == []
        assert "FAILURES=1" in proc.stdout

    def test_no_restart_while_an_upgrade_holds_the_lock(self, tmp_path):
        proc, restarts = _run_4b(tmp_path, "unhealthy", "healthy", "upgrade")
        assert restarts == []
        assert "FAILURES=1" in proc.stdout

    def test_no_restart_on_a_run_that_just_booted_colima(self, tmp_path):
        proc, restarts = _run_4b(tmp_path, "unhealthy", "healthy", COLIMA_STARTED="true")
        assert restarts == []
        assert "FAILURES=1" in proc.stdout

    def test_colima_started_is_initialised_for_set_u(self):
        # 4b reads it on every run; it used to be set only when Docker was down.
        text = HEALTH_CHECK.read_text()
        assert text.index("COLIMA_STARTED=false") < text.index("# 1. Check Colima is running")
