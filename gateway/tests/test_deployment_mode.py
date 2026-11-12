# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Deployment mode (AGENTSHROUD_DEPLOYMENT): local agents, hosted (cloud) agents, or both.

scripts/lib/deployment-mode.sh is sourced by scripts/asb (which containers to start)
and scripts/post-deploy-check.sh (which containers must be running). These tests run
the real library under bash.
"""

from __future__ import annotations

import subprocess
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[2]
LIB = REPO / "scripts" / "lib" / "deployment-mode.sh"


def _bash(script: str, env: dict | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["bash", "-c", f'. "{LIB}"; {script}'],
        capture_output=True,
        text=True,
        env={"PATH": "/usr/bin:/bin", **(env or {})},
        check=False,
    )


def test_default_is_local_so_existing_hosts_are_unchanged():
    out = _bash("deployment_mode_resolve")
    assert out.returncode == 0 and out.stdout.strip() == "local"


@pytest.mark.parametrize("mode", ["local", "cloud", "hybrid"])
def test_environment_value_wins(mode):
    out = _bash("deployment_mode_resolve", {"AGENTSHROUD_DEPLOYMENT": mode})
    assert out.stdout.strip() == mode


def test_reads_env_file_without_sourcing_it(tmp_path):
    env_file = tmp_path / ".env"
    # A line that would run a command if the file were sourced.
    env_file.write_text('TOUCHED=$(touch pwned)\nAGENTSHROUD_DEPLOYMENT="hybrid"\n')
    out = subprocess.run(
        ["bash", "-c", f'. "{LIB}"; deployment_mode_resolve "{env_file}"'],
        capture_output=True,
        text=True,
        cwd=tmp_path,
        env={"PATH": "/usr/bin:/bin"},
        check=False,
    )
    assert out.stdout.strip() == "hybrid"
    assert not (tmp_path / "pwned").exists()


def test_environment_overrides_env_file(tmp_path):
    env_file = tmp_path / ".env"
    env_file.write_text("AGENTSHROUD_DEPLOYMENT=hybrid\n")  # pragma: allowlist secret
    out = _bash(f'deployment_mode_resolve "{env_file}"', {"AGENTSHROUD_DEPLOYMENT": "cloud"})
    assert out.stdout.strip() == "cloud"


@pytest.mark.parametrize("bad", ["Cloud", "both", "local;rm -rf /", " "])
def test_unknown_mode_fails_closed(bad):
    out = _bash("deployment_mode_resolve", {"AGENTSHROUD_DEPLOYMENT": bad})
    assert out.returncode != 0
    assert out.stdout.strip() == ""
    assert "must be local, cloud or hybrid" in out.stderr


@pytest.mark.parametrize(
    "mode,local_agents,edge",
    [("local", True, False), ("cloud", False, True), ("hybrid", True, True)],
)
def test_what_each_mode_runs(mode, local_agents, edge):
    loc = _bash(f"deployment_runs_local_agents {mode}").returncode == 0
    edg = _bash(f"deployment_runs_edge {mode}").returncode == 0
    assert (loc, edg) == (local_agents, edge)


@pytest.mark.parametrize(
    "mode,profile,up",
    [
        ("local", "", ""),
        ("cloud", "--profile edge", "--scale openclaw=0"),
        ("hybrid", "--profile edge", ""),
    ],
)
def test_compose_flags_per_mode(mode, profile, up):
    assert _bash(f"deployment_profile_flags {mode}").stdout.strip() == profile
    assert _bash(f"deployment_up_flags {mode}").stdout.strip() == up


def test_gateway_is_told_the_mode_for_the_command_center():
    compose = yaml.safe_load((REPO / "docker" / "docker-compose.yml").read_text())
    env = compose["services"]["gateway"]["environment"]
    assert "AGENTSHROUD_DEPLOYMENT=${AGENTSHROUD_DEPLOYMENT:-local}" in env


def _asb_setup(mode: str, want_hermes: str, profile_flag: str) -> dict:
    """Run scripts/asb's real _deployment_setup and report the variables it leaves."""
    text = (REPO / "scripts" / "asb").read_text()
    start = text.index("_deployment_setup() {")
    body = text[start : text.index("\n}\n", start) + 3]
    script = (
        f'. "{LIB}"; REPO_DIR=/nonexistent; '
        f'_WANT_HERMES={want_hermes}; _PROFILE_FLAG="{profile_flag}"; '
        f"{body}\n_deployment_setup >/dev/null; "
        'printf "%s|%s|%s|%s|%s" "$_WANT_HERMES" "$_PROFILE_FLAG" "$_DEPLOY_PROFILE" '
        '"$_DEPLOY_UP" "${AGENTSHROUD_INBOUND_EDGE:-unset}"'
    )
    out = subprocess.run(
        ["bash", "-c", script],
        capture_output=True,
        text=True,
        env={"PATH": "/usr/bin:/bin", "AGENTSHROUD_DEPLOYMENT": mode},
        check=True,
    )
    keys = ("hermes", "profile", "deploy_profile", "deploy_up", "inbound_edge")
    return dict(zip(keys, out.stdout.split("|")))


def test_asb_local_mode_keeps_full_stack_and_leaves_edge_alone():
    got = _asb_setup("local", "1", "--profile voice")
    assert got == {
        "hermes": "1",
        "profile": "--profile voice",
        "deploy_profile": "",
        "deploy_up": "",
        "inbound_edge": "unset",
    }


def test_asb_cloud_mode_drops_local_agents_even_for_full():
    got = _asb_setup("cloud", "1", "--profile voice")
    assert got == {
        "hermes": "0",
        "profile": "",
        "deploy_profile": "--profile edge",
        "deploy_up": "--scale openclaw=0",
        "inbound_edge": "1",
    }


def test_asb_hybrid_mode_adds_edge_to_full_stack():
    got = _asb_setup("hybrid", "1", "--profile voice")
    assert got == {
        "hermes": "1",
        "profile": "--profile voice",
        "deploy_profile": "--profile edge",
        "deploy_up": "",
        "inbound_edge": "1",
    }


def test_asb_build_and_up_carry_the_deployment_flags():
    text = (REPO / "scripts" / "asb").read_text()
    assert text.count("_deployment_setup\n") == 3  # up, rebuild, clean-rebuild
    assert "$COMPOSE $_PROFILE_FLAG up -d\n" not in text
    assert text.count("$COMPOSE $_PROFILE_FLAG $_DEPLOY_PROFILE up -d $_DEPLOY_UP") == 3
    assert text.count("$COMPOSE $_PROFILE_FLAG $_DEPLOY_PROFILE build --no-cache") == 2


def test_asb_and_post_deploy_check_use_the_library():
    for script in ("scripts/asb", "scripts/post-deploy-check.sh"):
        text = (REPO / script).read_text()
        assert "scripts/lib/deployment-mode.sh" in text, script
        assert "deployment_mode_resolve" in text, script
