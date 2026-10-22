# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""scripts/update-conduit-push.sh — pinned installer for Hermes's conduit_push plugin.

conduit_push was hand-installed into the hermes-config volume on 2026-10-16
(unpinned, revision 1c9075ba22, 0.41.0) and nothing in the repo tracked it, so
the Sunday upgrade never saw it. The owner's policy (2026-10-22): install only
the commit pinned in docker/versions.env; bumping the pin is a reviewed PR.

These tests drive the real script against a fake ``docker`` whose container
state lives in files, so install, restart and every proof are observable.
"""

from __future__ import annotations

import os
import re
import shutil
import stat
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent.parent
SCRIPT = REPO_ROOT / "scripts" / "update-conduit-push.sh"
VERSIONS = REPO_ROOT / "docker" / "versions.env"

OLD_REF = "1c9075ba22777f69294b07771cfbc3a78995bfdd"
NEW_REF = "f56bbb963f001c58a83fb02909eb8b44173ed668"

pytestmark = pytest.mark.skipif(shutil.which("bash") is None, reason="needs bash")

# Fake docker. State dir $S: version, ref, status (enabled/disabled), pulse
# (absent|false|true), log of every call. `exec ... hermes plugins install`
# moves version/ref to $S/install_version / $S/install_ref unless
# $S/install_fails exists. `restart` is logged; `inspect` reports healthy.
_FAKE_DOCKER = r"""#!/usr/bin/env bash
S="$FAKE_STATE"
echo "$*" >> "$S/calls"
case "$1" in
  inspect) echo healthy ;;
  restart) echo restarted >> "$S/restarts" ;;
  exec)
    shift
    while [ "${1#-}" != "$1" ]; do [ "$1" = "-u" ] && shift; shift; done
    shift  # container
    cmd="$*"
    case "$cmd" in
      *"plugins show conduit_push"*)
        printf 'conduit_push v%s\nStatus: %s\n' "$(cat "$S/version")" "$(cat "$S/status")" ;;
      *"chown -R hermes:hermes"*) echo hermes > "$S/owner" ;;
      *"plugins install"*)
        [ -f "$S/install_fails" ] && { echo "install failed" >&2; exit 1; }
        # The hermes CLI shim drops root to uid 10000; it cannot move a
        # root-owned plugin dir aside (prod 2026-10-22, EACCES in _swap_in_plugin).
        [ "$(cat "$S/owner")" = hermes ] || { echo "PermissionError: [Errno 13]" >&2; exit 1; }
        ref=$(echo "$cmd" | sed -n 's/.*--ref \([0-9a-f]\{40\}\).*/\1/p')
        echo "$ref" > "$S/ref"
        if [ "$ref" = "$(cat "$S/install_ref" 2>/dev/null)" ]; then
          cat "$S/install_version" > "$S/version"
        else
          cat "$S/old_version" > "$S/version"
        fi
        echo enabled > "$S/status" ;;
      *install-metadata.json*) cat "$S/ref" ;;
      *conduit-pulse.db*) cat "$S/pulse" ;;
      *) echo "unexpected exec: $cmd" >&2; exit 9 ;;
    esac ;;
esac
"""


def _versions_file(tmp_path: Path, ref: str = NEW_REF, version: str = "0.58.0") -> Path:
    p = tmp_path / "versions.env"
    p.write_text(
        "CONDUIT_PUSH_REPO=kaishi00/hermes-conduit-notifier\n"
        f"CONDUIT_PUSH_REF={ref}\n"
        f"CONDUIT_PUSH_VERSION={version}\n"
    )
    return p


def _run(tmp_path, *, version="0.41.0", ref=OLD_REF, pulse="absent", flags=(), versions=None):
    state = tmp_path / "state"
    state.mkdir()
    (state / "version").write_text(version)
    (state / "old_version").write_text(version)
    (state / "ref").write_text(ref)
    (state / "status").write_text("enabled")
    (state / "pulse").write_text(pulse)
    (state / "owner").write_text("root")  # as hand-installed on 2026-10-16
    (state / "install_ref").write_text(NEW_REF)
    (state / "install_version").write_text("0.58.0")
    for f in flags:
        (state / f).touch()
    bindir = tmp_path / "bin"
    bindir.mkdir()
    docker = bindir / "docker"
    docker.write_text(_FAKE_DOCKER)
    docker.chmod(docker.stat().st_mode | stat.S_IXUSR)
    env = {
        "PATH": f"{bindir}:{os.environ['PATH']}",
        "FAKE_STATE": str(state),
        "CONDUIT_PUSH_VERSIONS_FILE": str(versions or _versions_file(tmp_path)),
        "CONDUIT_PUSH_HEALTH_TIMEOUT": "2",
        "CONDUIT_PUSH_POLL": "0",
    }
    proc = subprocess.run(
        ["bash", str(SCRIPT)], env=env, capture_output=True, text=True, timeout=60
    )
    calls = (state / "calls").read_text() if (state / "calls").exists() else ""
    restarts = len((state / "restarts").read_text().split()) if (state / "restarts").exists() else 0
    return proc, calls, restarts, state


class TestUpgrade:
    def test_upgrades_to_the_pin_and_reports_from_to(self, tmp_path):
        proc, calls, restarts, state = _run(tmp_path)
        assert proc.returncode == 0, proc.stderr
        assert f"--ref {NEW_REF}" in calls
        assert "kaishi00/hermes-conduit-notifier" in calls
        assert restarts == 1
        out = proc.stdout
        assert "0.41.0 (1c9075ba22) -> 0.58.0 (f56bbb963f)" in out
        assert "UPGRADED" in out

    def test_installs_only_by_immutable_ref(self, tmp_path):
        _, calls, _, _ = _run(tmp_path)
        install = [line for line in calls.splitlines() if "plugins install" in line]
        assert len(install) == 1
        assert re.search(r"--ref [0-9a-f]{40}\b", install[0])
        assert "plugins update" not in calls  # `update` pulls floating latest

    def test_root_owned_install_is_handed_to_hermes_before_installing(self, tmp_path):
        proc, calls, _, state = _run(tmp_path)
        assert proc.returncode == 0, proc.stderr
        lines = calls.splitlines()
        chown = next(i for i, c in enumerate(lines) if "chown -R hermes:hermes" in c)
        install = next(i for i, c in enumerate(lines) if "plugins install" in c)
        assert chown < install
        assert "/opt/data/plugins/conduit_push" in lines[chown]
        assert "/opt/data/plugins/.install-metadata.json" in lines[chown]
        assert (state / "owner").read_text().strip() == "hermes"

    def test_already_at_pin_is_a_distinct_no_op(self, tmp_path):
        proc, calls, restarts, _ = _run(tmp_path, version="0.58.0", ref=NEW_REF)
        assert proc.returncode == 25
        assert "ALREADY_AT_PIN" in proc.stdout
        assert "plugins install" not in calls
        assert restarts == 0


class TestProvesTheOutcome:
    def test_install_that_lands_the_wrong_version_fails_and_rolls_back(self, tmp_path):
        # Upstream plugin.yaml at the pinned ref disagrees with the pinned version.
        versions = _versions_file(tmp_path, version="0.59.9")
        proc, calls, _, state = _run(tmp_path, versions=versions)
        assert proc.returncode == 1
        assert "expected 0.59.9" in proc.stderr
        assert f"--ref {OLD_REF}" in calls  # rolled back to what was there
        assert (state / "ref").read_text().strip() == OLD_REF

    def test_failed_install_fails_and_rolls_back(self, tmp_path):
        proc, calls, _, state = _run(tmp_path, flags=("install_fails",))
        assert proc.returncode == 1
        assert "UPGRADED" not in proc.stdout

    def test_pulse_switched_on_is_a_failure(self, tmp_path):
        proc, _, _, _ = _run(tmp_path, pulse="true")
        assert proc.returncode == 1
        assert "Pulse is enabled" in proc.stderr

    @pytest.mark.parametrize("pulse", ["absent", "false"])
    def test_pulse_off_passes(self, tmp_path, pulse):
        proc, _, _, _ = _run(tmp_path, pulse=pulse)
        assert proc.returncode == 0, proc.stderr
        assert "Pulse: off" in proc.stdout


class TestPinIsValidated:
    @pytest.mark.parametrize(
        "ref", ["main", "f56bbb963f", "F56BBB963F001C58A83FB02909EB8B44173ED668", ""]
    )
    def test_non_sha_pin_is_refused_before_touching_hermes(self, tmp_path, ref):
        proc, calls, _, _ = _run(tmp_path, versions=_versions_file(tmp_path, ref=ref))
        assert proc.returncode == 2
        assert "exec" not in calls and "restart" not in calls


class TestRepoPin:
    def test_versions_env_pins_conduit_push_to_a_full_sha(self):
        text = VERSIONS.read_text()
        assert re.search(r"^CONDUIT_PUSH_REPO=kaishi00/hermes-conduit-notifier$", text, re.M)
        assert re.search(r"^CONDUIT_PUSH_REF=[0-9a-f]{40}$", text, re.M)
        assert re.search(r"^CONDUIT_PUSH_VERSION=\d+\.\d+\.\d+$", text, re.M)

    def test_script_is_executable_in_git(self):
        mode = subprocess.run(
            ["git", "ls-files", "-s", "scripts/update-conduit-push.sh"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout.split()[0]
        assert mode == "100755"
