# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Regression tests for cron job prompt content and SSH config.

These tests guard against prompt regressions that would cause:
- Upstream cron classifiers to reject legitimate summaries (Bug D)
- Fixture UIDs leaking into production reports (Bug B cron layer)
- SSH connections to Tailscale FQDNs being blocked (Bug E)
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

# Primary cron config used by running containers.
_CRON_JSON = (
    Path(__file__).parent.parent.parent / "docker" / "config" / "openclaw" / "cron" / "jobs.json"
)
# First-boot bootstrap copy (kept in sync with primary).
_CRON_JSON_BOTS = (
    Path(__file__).parent.parent.parent
    / "docker"
    / "bots"
    / "openclaw"
    / "config"
    / "cron"
    / "jobs.json"
)
_SSH_CONFIG = Path(__file__).parent.parent.parent / "docker" / "config" / "ssh" / "config"

_COLLAB_JOB_NAMES = {
    "Collaborator Report - Morning",
    "Collaborator Report - Evening",
    "Collaborator Daily Digest",
}


def _load_jobs(path: Path) -> list[dict]:
    data = json.loads(path.read_text())
    return data.get("jobs", [])


def _collab_jobs(jobs: list[dict]) -> list[dict]:
    return [j for j in jobs if j.get("name") in _COLLAB_JOB_NAMES]


# ── T11: denial-token avoidance ───────────────────────────────────────────────


def test_cron_prompts_warn_against_denied_token():
    """Every collaborator report prompt must instruct the LLM to avoid 'denied'."""
    jobs = _load_jobs(_CRON_JSON)
    collab = _collab_jobs(jobs)
    assert collab, "No collaborator report jobs found in cron jobs.json"
    for job in collab:
        msg = job.get("payload", {}).get("message", "")
        assert (
            "Do NOT use the words" in msg
        ), f"Job '{job['name']}' is missing denial-token avoidance instruction"


# ── T12: fixture UID exclusion ────────────────────────────────────────────────


def test_cron_prompts_exclude_short_uids():
    """Every collaborator report prompt must instruct LLM to exclude short UIDs."""
    jobs = _load_jobs(_CRON_JSON)
    collab = _collab_jobs(jobs)
    assert collab, "No collaborator report jobs found in cron jobs.json"
    for job in collab:
        msg = job.get("payload", {}).get("message", "")
        assert (
            "shorter than 7 digits" in msg
        ), f"Job '{job['name']}' is missing short-UID exclusion instruction"


# ── T11/T12 mirrored for bots bootstrap copy ─────────────────────────────────


def test_bots_cron_prompts_warn_against_denied_token():
    """Bootstrap cron copy must also have denial-token avoidance."""
    jobs = _load_jobs(_CRON_JSON_BOTS)
    collab = _collab_jobs(jobs)
    assert collab, "No collaborator report jobs found in bots cron jobs.json"
    for job in collab:
        msg = job.get("payload", {}).get("message", "")
        assert (
            "Do NOT use the words" in msg
        ), f"Bots job '{job['name']}' is missing denial-token avoidance instruction"


def test_bots_cron_prompts_exclude_short_uids():
    """Bootstrap cron copy must also exclude short UIDs."""
    jobs = _load_jobs(_CRON_JSON_BOTS)
    collab = _collab_jobs(jobs)
    assert collab, "No collaborator report jobs found in bots cron jobs.json"
    for job in collab:
        msg = job.get("payload", {}).get("message", "")
        assert (
            "shorter than 7 digits" in msg
        ), f"Bots job '{job['name']}' is missing short-UID exclusion instruction"


# ── T13: SSH config routes Tailnet FQDN ──────────────────────────────────────


def test_ssh_config_routes_tailnet_fqdn():
    """SSH config must have a Host *.tail240ea8.ts.net block BEFORE Host * block."""
    text = _SSH_CONFIG.read_text()
    tailnet_pos = text.find("Host *.tail240ea8.ts.net")
    wildcard_pos = text.find("\nHost *\n")
    assert tailnet_pos != -1, "No 'Host *.tail240ea8.ts.net' block found in ssh/config"
    assert wildcard_pos != -1, "No wildcard 'Host *' block found in ssh/config"
    assert (
        tailnet_pos < wildcard_pos
    ), "Host *.tail240ea8.ts.net block must appear BEFORE the Host * fallback block"


def test_ssh_tailnet_block_has_proxy_command():
    """Tailnet Host block must route through the gateway CONNECT proxy."""
    text = _SSH_CONFIG.read_text()
    # Find the actual Host directive (not comments mentioning the pattern)
    tailnet_start = text.find("Host *.tail240ea8.ts.net")
    assert tailnet_start != -1, "No 'Host *.tail240ea8.ts.net' directive found"
    # Extract text between tailnet block and next Host block
    next_host = text.find("\nHost ", tailnet_start + 1)
    tailnet_section = text[tailnet_start:next_host] if next_host != -1 else text[tailnet_start:]
    assert (
        "ProxyCommand" in tailnet_section
    ), "Tailnet Host block must include a ProxyCommand directive"
    assert "gateway:8181" in tailnet_section, "Tailnet ProxyCommand must route through gateway:8181"
