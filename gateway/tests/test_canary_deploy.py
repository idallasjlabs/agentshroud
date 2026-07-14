# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Tests for scripts/canary-deploy.sh (SCRUM-62 blue/green canary).

Exercised via subprocess — no containers are built and no host is touched
(every check runs with --dry-run or relies on the non-green-user guard).
"""

from __future__ import annotations

import subprocess
from pathlib import Path

_SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "canary-deploy.sh"


def _run(*args, env=None):
    return subprocess.run(
        ["bash", str(_SCRIPT), *args],
        capture_output=True,
        text=True,
        env=env,
        timeout=30,
    )


def test_script_exists_and_is_executable() -> None:
    assert _SCRIPT.exists()
    assert _SCRIPT.stat().st_mode & 0o111, "canary-deploy.sh must be executable"


def test_syntax_is_valid() -> None:
    r = subprocess.run(["bash", "-n", str(_SCRIPT)], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr


class TestGuard:
    def test_refuses_when_not_green_user(self) -> None:
        # Real mode (no --dry-run) as a non-'agentshroud-bot' user must abort
        # BEFORE touching anything — blue/prod is off-limits to this script.
        import os

        env = dict(os.environ, USER="ijefferson.admin")
        r = _run("--ref", "origin/main", env=env)
        assert r.returncode == 1
        assert "agentshroud-bot" in r.stderr
        assert "off-limits" in r.stderr.lower()

    def test_dry_run_allowed_for_any_user(self) -> None:
        import os

        env = dict(os.environ, USER="somebody-else")
        r = _run("--dry-run", "--ref", "origin/main", env=env)
        assert r.returncode == 0


class TestDryRun:
    def test_dry_run_changes_nothing_and_previews_actions(self) -> None:
        r = _run("--dry-run", "--ref", "origin/main")
        assert r.returncode == 0
        out = r.stdout
        # Previews the deploy + rollback-anchor tag, never executes.
        assert "[dry-run]" in out
        assert "asb rebuild" in out
        assert "pre-deploy-" in out  # rollback anchor tag
        # Deploys to GREEN and leaves BLUE promotion human-gated.
        assert "GREEN canary healthy" in out
        assert "promote BLUE/prod" in out

    def test_tag_fetch_uses_force(self) -> None:
        # Regression (SCRUM-62, marvin 2026-07-14): a GREEN checkout may carry
        # local version tags diverging from origin. Without --force, `git fetch
        # --tags` exits non-zero on "would clobber existing tag" and aborts the
        # deploy before asb rebuild. The fetch MUST be forced.
        r = _run("--dry-run", "--ref", "origin/main")
        assert r.returncode == 0
        out = r.stdout
        assert "fetch --tags --force --prune" in out, (
            "canary fetch must use --force so divergent GREEN tags cannot abort the deploy"
        )

    def test_dry_run_targets_green_ports_not_blue(self) -> None:
        # The script must never invoke anything against the blue/prod checkout;
        # it operates only in the green repo path (default $HOME/agentshroud).
        r = _run("--dry-run", "--ref", "origin/main", "--repo", "/tmp/green-xyz")
        assert r.returncode == 0
        assert "/tmp/green-xyz" in r.stdout

    def test_unknown_arg_rejected(self) -> None:
        r = _run("--bogus")
        assert r.returncode == 2


def test_help_prints_usage() -> None:
    r = _run("--help")
    assert r.returncode == 0
    assert "canary-deploy.sh" in r.stdout
    assert "auto-roll" in r.stdout.lower() or "rollback" in r.stdout.lower()
