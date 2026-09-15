"""Tests for scripts/discover_upstream_versions.py — latest-release discovery.

Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
Patent Pending — U.S. Provisional Application No. 64/018,744

Why this module exists at all: for seven weeks every Sunday upgrade reported
PASS while rebuilding the SAME upstream version, because nothing in the
pipeline ever asked what the latest release was — version selection was left to
an LLM session's judgement and silently never happened. OPENCLAW_VERSION moved
exactly once between 2026-07-29 and 2026-09-15, and only to a downstream
rebuild counter.

These cover the PURE selection logic (which version wins, which are rejected).
Network fetches are exercised via injected payloads — no test here touches npm
or Docker Hub.
"""

from __future__ import annotations

import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO_ROOT / "scripts"))

from discover_upstream_versions import (  # noqa: E402
    is_stable,
    pick_latest_hermes_tag,
    pick_latest_stable,
)


class TestIsStable:
    """Pre-release builds must never be shipped to production automatically."""

    def test_plain_releases_are_stable(self):
        assert is_stable("2026.9.4")
        assert is_stable("2026.8.1")

    def test_downstream_rebuild_counter_is_stable(self):
        """'2026.7.1-2' is a real published OpenClaw release, not a prerelease
        marker — the running container reports exactly this string."""
        assert is_stable("2026.7.1-2")

    def test_beta_rc_alpha_are_not_stable(self):
        assert not is_stable("2026.9.1-beta.1")
        assert not is_stable("2026.8.1-beta.3")
        assert not is_stable("2026.7.2-rc.1")
        assert not is_stable("2026.7.2-alpha")
        assert not is_stable("1.0.0-dev")
        assert not is_stable("2026.9.1-NEXT")  # case-insensitive

    def test_empty_is_not_stable(self):
        assert not is_stable("")
        assert not is_stable(None)


class TestPickLatestStable:
    """Selecting the newest shippable npm release."""

    def test_picks_the_highest_stable_version(self):
        versions = ["2026.8.1", "2026.9.4", "2026.9.2", "2026.8.2"]
        assert pick_latest_stable(versions) == "2026.9.4"

    def test_ignores_prereleases_even_when_numerically_highest(self):
        versions = ["2026.9.4", "2026.9.5-beta.1", "2026.9.5-rc.2"]
        assert pick_latest_stable(versions) == "2026.9.4"

    def test_real_openclaw_tail_picks_2026_9_4(self):
        """The actual npm tail as of 2026-09-15."""
        versions = [
            "2026.7.2-beta.6",
            "2026.7.2-beta.7",
            "2026.8.1-beta.1",
            "2026.8.1-beta.2",
            "2026.8.1-beta.3",
            "2026.8.1",
            "2026.8.2",
            "2026.9.1-beta.1",
            "2026.9.1",
            "2026.9.2",
            "2026.9.3",
            "2026.9.4",
        ]
        assert pick_latest_stable(versions) == "2026.9.4"

    def test_numeric_ordering_not_lexicographic(self):
        """'2026.10.1' must beat '2026.9.4' — string compare gets this wrong."""
        assert pick_latest_stable(["2026.9.4", "2026.10.1"]) == "2026.10.1"

    def test_downstream_counter_sorts_above_its_base_release(self):
        """2026.7.1-2 is a patch published after 2026.7.1, so it must win."""
        assert pick_latest_stable(["2026.7.1", "2026.7.1-2"]) == "2026.7.1-2"

    def test_unparseable_entries_are_skipped_not_crashed_on(self):
        assert pick_latest_stable(["garbage", "2026.9.4", ""]) == "2026.9.4"

    def test_no_stable_versions_returns_none(self):
        assert pick_latest_stable(["1.0.0-beta.1", "2.0.0-rc.1"]) is None

    def test_empty_returns_none(self):
        assert pick_latest_stable([]) is None


class TestPickLatestHermesTag:
    """Hermes publishes date-based image tags (vYYYY.M.D)."""

    def test_picks_newest_date_tag(self):
        tags = ["latest", "main", "v2026.9.14", "v2026.9.11", "v2026.8.31"]
        assert pick_latest_hermes_tag(tags) == "v2026.9.14"

    def test_rejects_floating_tags(self):
        """'latest'/'main' float and would defeat the whole point of pinning."""
        assert pick_latest_hermes_tag(["latest", "main"]) is None

    def test_handles_four_component_tags(self):
        tags = ["v2026.8.16", "v2026.8.16.2"]
        assert pick_latest_hermes_tag(tags) == "v2026.8.16.2"

    def test_real_hermes_tail_picks_latest_date(self):
        tags = [
            "latest",
            "main",
            "v2026.9.14",
            "v2026.9.11",
            "v2026.9.7",
            "v2026.8.31",
            "v2026.8.16.2",
            "v2026.7.7.2",
        ]
        assert pick_latest_hermes_tag(tags) == "v2026.9.14"

    def test_empty_returns_none(self):
        assert pick_latest_hermes_tag([]) is None
