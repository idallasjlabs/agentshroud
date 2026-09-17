"""Tests for scripts/auto_remediate_cves.py — automated CVE remediation planning.

Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
Patent Pending — U.S. Provisional Application No. 64/018,744

These cover the PURE planning/pin-rewrite core. The deploy arm delegates to
scripts/sunday-upgrade-apply.sh (already gated + smoke-tested separately);
nothing here builds an image or talks to Docker.

The invariant that matters most, and the reason this module exists: a CVE may
only be reported as remediated when the vulnerable code is actually gone from
the running image. That means the version pin and the registry must never be
allowed to disagree — if a deploy fails and rolls back, the pin must roll back
with it, or the next triage run would read a version that is not running and
promote advisories on false evidence.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_REPO_ROOT / "scripts"))

from auto_remediate_cves import (  # noqa: E402
    RemediationPlan,
    plan_remediation,
    read_pin,
    write_pin,
)


def _entry(ghsa: str, fixed_in: str | None, status: str = "under_review", **kw):
    """Minimal registry entry shaped like agent_cve_registry.py's dicts."""
    e = {
        "id": ghsa,
        "ghsa_id": ghsa,
        "title": f"title for {ghsa}",
        "fixed_in": fixed_in,
        "status": status,
        "severity": kw.get("severity", "HIGH"),
        "cvss": kw.get("cvss", 7.5),
    }
    e.update(kw)
    return e


class TestPlanRemediation:
    """The planner decides WHAT bump remediates WHICH advisories."""

    def test_picks_minimum_version_clearing_every_remediable_advisory(self):
        registry = [
            _entry("GHSA-a", "2026.8.1"),
            _entry("GHSA-b", "2026.8.11"),
            _entry("GHSA-c", "2026.9.3"),
        ]
        plan = plan_remediation(registry, current_version="2026.7.1-2")
        # 2026.9.3 is the lowest version that clears all three.
        assert plan.target_version == "2026.9.3"
        assert {e["ghsa_id"] for e in plan.cleared} == {"GHSA-a", "GHSA-b", "GHSA-c"}
        assert plan.remaining == []

    def test_separates_advisories_already_fixed_at_the_current_pin(self):
        """fixed_in <= pin means the vulnerable code is not present at all.

        These are mis-filed as under_review and must NOT be counted as
        motivating an upgrade — reporting them as 'cleared by the bump' would
        overstate what the bump achieved.
        """
        registry = [
            _entry("GHSA-old", "2026.5.0"),
            _entry("GHSA-pin", "2026.7.1"),
            _entry("GHSA-new", "2026.8.1"),
        ]
        plan = plan_remediation(registry, current_version="2026.7.1-2")
        assert {e["ghsa_id"] for e in plan.already_fixed} == {"GHSA-old", "GHSA-pin"}
        assert {e["ghsa_id"] for e in plan.cleared} == {"GHSA-new"}
        assert plan.target_version == "2026.8.1"

    def test_downstream_build_suffix_on_the_pin_is_ignored(self):
        """'2026.7.1-2' is AgentShroud's own rebuild counter, not upstream semver.

        An advisory fixed in 2026.7.1 is fixed at pin 2026.7.1-2.
        """
        registry = [_entry("GHSA-x", "2026.7.1")]
        plan = plan_remediation(registry, current_version="2026.7.1-2")
        assert plan.cleared == []
        assert {e["ghsa_id"] for e in plan.already_fixed} == {"GHSA-x"}
        assert plan.target_version is None

    def test_advisory_without_a_fixed_in_is_not_claimed_remediable(self):
        """No upstream fix means no version bump can honestly clear it."""
        registry = [_entry("GHSA-nofix", None), _entry("GHSA-fix", "2026.8.1")]
        plan = plan_remediation(registry, current_version="2026.7.1-2")
        assert {e["ghsa_id"] for e in plan.remaining} == {"GHSA-nofix"}
        assert {e["ghsa_id"] for e in plan.cleared} == {"GHSA-fix"}

    def test_unparseable_fixed_in_is_treated_as_not_remediable(self):
        registry = [_entry("GHSA-junk", "not-a-version")]
        plan = plan_remediation(registry, current_version="2026.7.1-2")
        assert {e["ghsa_id"] for e in plan.remaining} == {"GHSA-junk"}
        assert plan.target_version is None

    def test_no_upgrade_needed_yields_no_target(self):
        registry = [_entry("GHSA-a", "2026.1.0")]
        plan = plan_remediation(registry, current_version="2026.7.1-2")
        assert plan.target_version is None
        assert plan.cleared == []

    def test_only_under_review_entries_are_considered(self):
        """Already-triaged entries are somebody's assessed verdict — a version
        bump planner must not silently re-open or re-claim them."""
        registry = [
            _entry("GHSA-done", "2026.9.9", status="fully_mitigated"),
            _entry("GHSA-open", "2026.8.1", status="under_review"),
        ]
        plan = plan_remediation(registry, current_version="2026.7.1-2")
        assert {e["ghsa_id"] for e in plan.cleared} == {"GHSA-open"}
        assert plan.target_version == "2026.8.1"

    def test_max_target_caps_the_bump(self):
        """An operator may cap how far forward an unattended job may jump."""
        registry = [
            _entry("GHSA-a", "2026.8.1"),
            _entry("GHSA-c", "2026.9.3"),
        ]
        plan = plan_remediation(registry, current_version="2026.7.1-2", max_target="2026.8.1")
        assert plan.target_version == "2026.8.1"
        assert {e["ghsa_id"] for e in plan.cleared} == {"GHSA-a"}
        # The one beyond the cap is honestly reported as still outstanding.
        assert {e["ghsa_id"] for e in plan.remaining} == {"GHSA-c"}

    def test_empty_registry_is_a_no_op_plan(self):
        plan = plan_remediation([], current_version="2026.7.1-2")
        assert plan.target_version is None
        assert plan.cleared == plan.remaining == plan.already_fixed == []

    def test_plan_is_serialisable_for_the_unattended_audit_trail(self):
        registry = [_entry("GHSA-a", "2026.8.1")]
        plan = plan_remediation(registry, current_version="2026.7.1-2")
        d = plan.to_dict()
        assert d["current_version"] == "2026.7.1-2"
        assert d["target_version"] == "2026.8.1"
        assert d["cleared_ids"] == ["GHSA-a"]
        assert d["cleared_count"] == 1


class TestVersionPinIO:
    """Reading and rewriting docker/versions.env."""

    def test_read_pin_returns_the_pinned_value(self, tmp_path):
        env = tmp_path / "versions.env"
        env.write_text("# comment\nOPENCLAW_VERSION=2026.7.1-2\nOTHER=x\n")
        assert read_pin(env, "OPENCLAW_VERSION") == "2026.7.1-2"

    def test_read_pin_missing_key_returns_none(self, tmp_path):
        env = tmp_path / "versions.env"
        env.write_text("OTHER=x\n")
        assert read_pin(env, "OPENCLAW_VERSION") is None

    def test_write_pin_replaces_only_the_target_line(self, tmp_path):
        env = tmp_path / "versions.env"
        env.write_text("# header\nOPENCLAW_VERSION=2026.7.1-2\nHERMES_VERSION=0.20.1\n")
        write_pin(env, "OPENCLAW_VERSION", "2026.9.3")
        text = env.read_text()
        assert "OPENCLAW_VERSION=2026.9.3\n" in text
        assert "HERMES_VERSION=0.20.1\n" in text
        assert "# header\n" in text
        assert "2026.7.1-2" not in text

    def test_write_pin_is_idempotent(self, tmp_path):
        env = tmp_path / "versions.env"
        env.write_text("OPENCLAW_VERSION=2026.9.3\n")
        write_pin(env, "OPENCLAW_VERSION", "2026.9.3")
        assert env.read_text() == "OPENCLAW_VERSION=2026.9.3\n"

    def test_write_pin_refuses_an_absent_key(self, tmp_path):
        """Silently appending a new key could create a pin nothing consumes."""
        env = tmp_path / "versions.env"
        env.write_text("OTHER=x\n")
        with pytest.raises(KeyError):
            write_pin(env, "OPENCLAW_VERSION", "2026.9.3")

    def test_write_pin_round_trips_through_read_pin(self, tmp_path):
        env = tmp_path / "versions.env"
        env.write_text("OPENCLAW_VERSION=2026.7.1-2\n")
        write_pin(env, "OPENCLAW_VERSION", "2026.9.3")
        assert read_pin(env, "OPENCLAW_VERSION") == "2026.9.3"

    def test_pin_revert_restores_the_exact_original_string(self, tmp_path):
        """The rollback path: a failed deploy must restore the pin verbatim,
        downstream '-N' suffix included, so the registry never claims
        remediation against a version that is not running."""
        env = tmp_path / "versions.env"
        env.write_text("OPENCLAW_VERSION=2026.7.1-2\n")
        original = read_pin(env, "OPENCLAW_VERSION")
        write_pin(env, "OPENCLAW_VERSION", "2026.9.3")
        write_pin(env, "OPENCLAW_VERSION", original)
        assert read_pin(env, "OPENCLAW_VERSION") == "2026.7.1-2"


class TestPlanAgainstRealRegistry:
    """Sanity-check the planner against the real committed registry."""

    def test_real_registry_plan_is_internally_consistent(self):
        from gateway.security.agent_cve_registry import _OPENCLAW_CVE_REGISTRY

        plan = plan_remediation(
            _OPENCLAW_CVE_REGISTRY,
            current_version=read_pin(_REPO_ROOT / "docker" / "versions.env", "OPENCLAW_VERSION")
            or "2026.7.1-2",
        )
        under_review = [c for c in _OPENCLAW_CVE_REGISTRY if c.get("status") == "under_review"]
        # Every under_review advisory lands in exactly one bucket.
        total = len(plan.cleared) + len(plan.remaining) + len(plan.already_fixed)
        assert total == len(under_review)
        ids = (
            [e["ghsa_id"] for e in plan.cleared]
            + [e["ghsa_id"] for e in plan.remaining]
            + [e["ghsa_id"] for e in plan.already_fixed]
        )
        assert len(ids) == len(set(ids)), "an advisory was bucketed twice"
