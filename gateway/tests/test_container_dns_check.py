# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Gateway DNS-server check in colima-health-check.sh (4c) and post-deploy-check.sh (P8).

On 2026-10-24 the gateway's first configured DNS server (AGENTSHROUD_DNS_PRIMARY
in docker/.env) was the Pi-hole's old address, which no longer answered. Every
lookup waited on it, the gateway logged gaierror(-3), Telegram and Slack
tunnels failed, and it was read for hours as "host DNS is broken". These tests
drive the real blocks against a fake ``docker`` whose ``exec`` probe answers
for every server except those listed in $DEAD.
"""

from __future__ import annotations

import os
import shutil
import stat
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent.parent
HEALTH_CHECK = REPO_ROOT / "docker" / "scripts" / "colima-health-check.sh"
POST_DEPLOY = REPO_ROOT / "scripts" / "post-deploy-check.sh"

pytestmark = pytest.mark.skipif(shutil.which("bash") is None, reason="needs bash")

# `docker inspect` prints $DNS (the container's HostConfig.Dns); `docker exec
# <c> python3 -c <probe> <ip>` fails when <ip> is in $DEAD and logs each probe.
_FAKE_DOCKER = """#!/usr/bin/env bash
case "$1" in
  inspect) printf '%s\\n' "$DNS" ;;
  exec)
    ip="${@: -1}"
    echo "$ip" >> "$PROBES"
    for d in $DEAD; do [ "$d" = "$ip" ] && exit 1; done
    exit 0 ;;
esac
"""


def _block(path: Path, start: str, end: str) -> str:
    text = path.read_text()
    return text[text.index(start) : text.index(end)]


def _run(tmp_path: Path, prelude: str, body: str, epilogue: str, dns: str, dead: str = ""):
    bindir = tmp_path / "bin"
    bindir.mkdir()
    fake = bindir / "docker"
    fake.write_text(_FAKE_DOCKER)
    fake.chmod(fake.stat().st_mode | stat.S_IXUSR)
    script = tmp_path / "block.sh"
    script.write_text(prelude + body + epilogue)
    probes = tmp_path / "probes"
    env = {
        "PATH": f"{bindir}:{os.environ['PATH']}",
        "DNS": dns,
        "DEAD": dead,
        "PROBES": str(probes),
    }
    proc = subprocess.run(
        ["bash", str(script)], env=env, capture_output=True, text=True, timeout=30
    )
    return proc, probes.read_text().split() if probes.exists() else []


# ── colima-health-check.sh step 4c ───────────────────────────────────────────
_HC_PRELUDE = """set -u
log() { echo "LOG: $1"; }
FAILURES=()
GATEWAY_CONTAINER=gw
"""
_HC_EPILOGUE = """
for f in "${FAILURES[@]+"${FAILURES[@]}"}"; do echo "FAILURE: $f"; done
"""


def _run_hc(tmp_path, dns, dead=""):
    body = _block(HEALTH_CHECK, "# 4c. The gateway's configured DNS servers", "# 5. Run container")
    return _run(tmp_path, _HC_PRELUDE, body, _HC_EPILOGUE, dns, dead)


class TestHealthCheckDnsServers:
    def test_all_servers_answer(self, tmp_path):
        proc, probes = _run_hc(tmp_path, "192.168.7.46 192.168.7.1 1.1.1.1")
        assert proc.returncode == 0, proc.stderr
        assert "FAILURE" not in proc.stdout
        assert probes == ["192.168.7.46", "192.168.7.1", "1.1.1.1"]

    def test_dead_server_is_a_failure_that_names_it(self, tmp_path):
        proc, probes = _run_hc(tmp_path, "192.168.7.45 192.168.7.1 1.1.1.1", dead="192.168.7.45")
        failures = [line for line in proc.stdout.splitlines() if line.startswith("FAILURE")]
        assert len(failures) == 1
        assert "192.168.7.45" in failures[0] and "192.168.7.1" not in failures[0]
        assert "not host DNS" in failures[0]
        # One retry before calling a server dead; healthy ones are asked once.
        assert probes.count("192.168.7.45") == 2
        assert probes.count("1.1.1.1") == 1

    def test_never_restarts_anything(self, tmp_path):
        body = _block(
            HEALTH_CHECK, "# 4c. The gateway's configured DNS servers", "# 5. Run container"
        )
        assert "docker restart" not in body and "docker rm" not in body

    def test_container_without_dns_override_passes(self, tmp_path):
        proc, probes = _run_hc(tmp_path, "")
        assert "FAILURE" not in proc.stdout
        assert probes == []


# ── post-deploy-check.sh P8 ──────────────────────────────────────────────────
_PD_PRELUDE = """set -euo pipefail
pass=0; fail=0; errors=()
check() {
  if [[ "$2" == "true" ]]; then echo "PASS: $1"; else echo "FAIL: $1 (${3:-})"; fi
}
GATEWAY_CONTAINER=gw
"""


def _run_pd(tmp_path, dns, dead=""):
    body = _block(POST_DEPLOY, "# ── P8: Gateway's configured DNS servers", "# ── F1-F4")
    return _run(tmp_path, _PD_PRELUDE, body, "", dns, dead)


class TestPostDeployDnsServers:
    def test_all_servers_answer(self, tmp_path):
        proc, _ = _run_pd(tmp_path, "192.168.7.46 1.1.1.1")
        assert proc.returncode == 0, proc.stderr
        assert "PASS: P8" in proc.stdout and "FAIL" not in proc.stdout

    def test_dead_server_fails_the_deploy_and_is_named(self, tmp_path):
        proc, _ = _run_pd(tmp_path, "192.168.7.45 1.1.1.1", dead="192.168.7.45")
        fails = [line for line in proc.stdout.splitlines() if line.startswith("FAIL")]
        assert len(fails) == 1 and "192.168.7.45" in fails[0]

    def test_probe_matches_the_health_check(self):
        # Two copies of one probe; they must not drift apart.
        hc = _block(HEALTH_CHECK, "_DNS_PROBE='", "'\n")
        pd = _block(POST_DEPLOY, "_DNS_PROBE='", "'\n")
        assert hc == pd
