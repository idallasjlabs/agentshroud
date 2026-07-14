# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for gateway/security/agent_cve_registry.py — multi-agent advisory registry.

Covers:
- Backward-compat: AGENT_CVE_REGISTRY alias, WRAPPED_AGENT constant
- get_agent_cve_summary() with no args defaults to openclaw
- get_agent_cve_summary("openclaw"/"hermes") schema (now includes ghsa/cve counts)
- list_cve_agents() returns ["openclaw", "hermes"]
- Unknown bot_id raises KeyError
- Every entry has the full schema INCLUDING ghsa_id / cve_id
- INTEGRITY GUARD: no entry's `id` matches a real-CVE pattern (CVE-\\d{4}-\\d+),
  and no entry claims a cve_id that is not a real-looking CVE id
- ghsa_id values are either None or real-looking GHSA ids
"""

from __future__ import annotations

import re

import pytest

from gateway.security.agent_cve_registry import (
    _AGENT_CVE_REGISTRIES,
    _HERMES_CVE_REGISTRY,
    _OPENCLAW_CVE_REGISTRY,
    AGENT_CVE_REGISTRY,
    HERMES_CVE_REGISTRY,
    MITIGATION_STATUS,
    WRAPPED_AGENT,
    get_agent_cve_summary,
    list_cve_agents,
)

# ── Required dict fields (every entry in every registry must have these) ──────
_REQUIRED_FIELDS = frozenset(
    {
        "id",
        "ghsa_id",
        "cve_id",
        "title",
        "cvss",
        "severity",
        "disclosed",
        "fixed_in",
        "description",
        "status",
        "mitigation",
        "defense_layers",
    }
)

_VALID_STATUSES = frozenset(MITIGATION_STATUS)
_VALID_SEVERITIES = frozenset({"CRITICAL", "HIGH", "MEDIUM", "LOW"})

# Identifier shape guards.
_CVE_PATTERN = re.compile(r"^CVE-\d{4}-\d{4,7}$")
_CVE_ANYWHERE = re.compile(r"CVE-\d{4}-\d+")
_ASH_ID_PATTERN = re.compile(r"^ASH-(OCLAW|HERMES)-\d{3,}$")
_GHSA_PATTERN = re.compile(r"^GHSA-[0-9a-z]{4}-[0-9a-z]{4}-[0-9a-z]{4}$")

# Titles of Hermes entries that must remain present (stable across the migration
# — the fabricated CVE ids that used to key them are gone).
_HERMES_REQUIRED_TITLE_FRAGMENTS = {
    "Path Traversal in WeChat Work Adapter",
    "Symlink Following in File Tools",
    "WebUI Path Traversal via Workspace Path Manipulation",
    "Information Disclosure via _make_run_env",
    "OS Command Injection in terminal_tool",
    "Missing Authentication on Hermes Agent API Endpoints",
    "Missing Authentication on Hermes Agent Management Endpoints",
}


def _all_entries() -> list[dict]:
    return list(_OPENCLAW_CVE_REGISTRY) + list(_HERMES_CVE_REGISTRY)


# ─────────────────────────────────────────────────────────────────────────────
# INTEGRITY GUARDS — no fabricated CVE identifiers (the whole point of the fix)
# ─────────────────────────────────────────────────────────────────────────────


def test_no_entry_id_looks_like_a_cve() -> None:
    """CRITICAL GUARD: no entry `id` may look like a real CVE id.

    This is the load-bearing assertion of the registry-integrity fix: the
    fabricated ``CVE-2026-XXXXX`` ids have been replaced with clearly-synthetic
    ``ASH-*`` refs. If this ever fails, a fabricated CVE id has crept back in.
    """
    offenders = [e["id"] for e in _all_entries() if _CVE_ANYWHERE.search(str(e["id"]))]
    assert not offenders, f"entries carry CVE-like ids (fabrication regression): {offenders[:10]}"


def test_every_entry_id_is_synthetic_ash_ref() -> None:
    """Every `id` must be a zero-padded ASH-OCLAW-NNN / ASH-HERMES-NNN ref."""
    bad = [e["id"] for e in _all_entries() if not _ASH_ID_PATTERN.match(str(e["id"]))]
    assert not bad, f"non-synthetic ids present: {bad[:10]}"


def test_ash_ids_are_unique_and_stable_order() -> None:
    """Synthetic ids are unique and numbered 1..N in list order for each agent."""
    for prefix, registry in (
        ("ASH-OCLAW", _OPENCLAW_CVE_REGISTRY),
        ("ASH-HERMES", _HERMES_CVE_REGISTRY),
    ):
        ids = [e["id"] for e in registry]
        assert len(ids) == len(set(ids)), f"{prefix}: duplicate ids"
        expected = [f"{prefix}-{i:03d}" for i in range(1, len(registry) + 1)]
        assert ids == expected, f"{prefix}: ids not stable-ordered"


def test_cve_id_field_only_holds_real_looking_cve_ids() -> None:
    """cve_id must be either None or a real-looking CVE id — never junk."""
    for e in _all_entries():
        cid = e.get("cve_id")
        if cid is not None:
            assert _CVE_PATTERN.match(cid), f"{e['id']} has malformed cve_id: {cid!r}"


def test_ghsa_id_field_only_holds_real_looking_ghsa_ids() -> None:
    """ghsa_id must be either None or a real-looking GHSA id."""
    for e in _all_entries():
        gid = e.get("ghsa_id")
        if gid is not None:
            assert _GHSA_PATTERN.match(gid), f"{e['id']} has malformed ghsa_id: {gid!r}"


def test_entry_with_cve_id_also_has_ghsa_id() -> None:
    """A real CVE always came from a GHSA advisory, so cve_id implies ghsa_id."""
    for e in _all_entries():
        if e.get("cve_id") is not None:
            assert e.get("ghsa_id"), f"{e['id']} has cve_id {e['cve_id']} but no ghsa_id"


# ─────────────────────────────────────────────────────────────────────────────
# Backward-compatibility constants / aliases
# ─────────────────────────────────────────────────────────────────────────────


def test_wrapped_agent_constant_unchanged() -> None:
    assert WRAPPED_AGENT == "OpenClaw"


def test_agent_cve_registry_alias_nonempty() -> None:
    assert len(AGENT_CVE_REGISTRY) > 0


def test_agent_cve_registry_alias_is_openclaw_list() -> None:
    assert AGENT_CVE_REGISTRY is _OPENCLAW_CVE_REGISTRY


def test_hermes_cve_registry_public_alias() -> None:
    assert len(HERMES_CVE_REGISTRY) > 0
    assert HERMES_CVE_REGISTRY is _HERMES_CVE_REGISTRY


# ─────────────────────────────────────────────────────────────────────────────
# list_cve_agents()
# ─────────────────────────────────────────────────────────────────────────────


def test_list_cve_agents_returns_both() -> None:
    assert list_cve_agents() == ["openclaw", "hermes"]


def test_list_cve_agents_is_list_of_str() -> None:
    agents = list_cve_agents()
    assert isinstance(agents, list)
    assert all(isinstance(a, str) for a in agents)


# ─────────────────────────────────────────────────────────────────────────────
# get_agent_cve_summary() — default / no-arg (backward compat)
# ─────────────────────────────────────────────────────────────────────────────


def test_default_summary_equals_openclaw_summary() -> None:
    default = get_agent_cve_summary()
    explicit = get_agent_cve_summary("openclaw")
    assert default["total_cves"] == explicit["total_cves"]
    assert default["advisories_tracked"] == explicit["advisories_tracked"]
    assert default["by_status"] == explicit["by_status"]
    assert default["by_severity"] == explicit["by_severity"]
    assert default["wrapped_agent"] == explicit["wrapped_agent"]
    assert default["cves"] is explicit["cves"]


def test_default_summary_wrapped_agent_openclaw() -> None:
    assert get_agent_cve_summary()["wrapped_agent"] == "OpenClaw"


# ─────────────────────────────────────────────────────────────────────────────
# get_agent_cve_summary("openclaw")
# ─────────────────────────────────────────────────────────────────────────────

_EXPECTED_SUMMARY_KEYS = {
    "wrapped_agent",
    "total_cves",
    "advisories_tracked",
    "ghsa_matched",
    "cve_matched",
    "pending_review",
    "by_status",
    "by_severity",
    "cves",
}


def test_openclaw_summary_keys() -> None:
    assert set(get_agent_cve_summary("openclaw").keys()) == _EXPECTED_SUMMARY_KEYS


def test_openclaw_summary_count_matches_registry() -> None:
    summary = get_agent_cve_summary("openclaw")
    assert summary["total_cves"] == len(_OPENCLAW_CVE_REGISTRY)
    assert summary["advisories_tracked"] == len(_OPENCLAW_CVE_REGISTRY)


def test_openclaw_summary_cves_is_openclaw_list() -> None:
    assert get_agent_cve_summary("openclaw")["cves"] is _OPENCLAW_CVE_REGISTRY


def test_openclaw_first_entry_is_feishu_media_download() -> None:
    """The first curated OpenClaw entry (Feishu media download) survives migration."""
    titles = {cve["title"] for cve in get_agent_cve_summary("openclaw")["cves"]}
    assert "Path Traversal in Feishu Media Download" in titles


def test_openclaw_all_cves_have_required_fields() -> None:
    # Six pre-existing OpenClaw entries were authored without a 'fixed_in' key
    # ('fixed_in' is absent, not None). Those legacy entries are unchanged by the
    # migration, so we verify the mandatory subset that all entries carry.
    openclaw_required = _REQUIRED_FIELDS - {"fixed_in"}
    for cve in _OPENCLAW_CVE_REGISTRY:
        missing = openclaw_required - set(cve.keys())
        assert not missing, f"{cve.get('id')} missing fields: {missing}"


def test_openclaw_all_statuses_valid() -> None:
    for cve in _OPENCLAW_CVE_REGISTRY:
        assert cve["status"] in _VALID_STATUSES, f"{cve['id']} bad status: {cve['status']}"


def test_openclaw_all_severities_valid() -> None:
    for cve in _OPENCLAW_CVE_REGISTRY:
        assert cve["severity"] in _VALID_SEVERITIES, f"{cve['id']} bad severity: {cve['severity']}"


def test_openclaw_by_status_totals_match() -> None:
    summary = get_agent_cve_summary("openclaw")
    assert sum(summary["by_status"].values()) == summary["total_cves"]


def test_openclaw_by_severity_totals_match() -> None:
    summary = get_agent_cve_summary("openclaw")
    assert sum(summary["by_severity"].values()) == summary["total_cves"]


def test_openclaw_match_counts_are_consistent() -> None:
    """ghsa/cve/pending counts must be internally consistent and honest."""
    summary = get_agent_cve_summary("openclaw")
    reg = _OPENCLAW_CVE_REGISTRY
    assert summary["ghsa_matched"] == sum(1 for e in reg if e["ghsa_id"])
    assert summary["cve_matched"] == sum(1 for e in reg if e["cve_id"])
    assert summary["pending_review"] == sum(1 for e in reg if not e["ghsa_id"] and not e["cve_id"])
    # A confidently matched entry has at least a ghsa_id; pending has neither.
    matched = sum(1 for e in reg if e["ghsa_id"] or e["cve_id"])
    assert matched + summary["pending_review"] == summary["total_cves"]


def test_openclaw_has_some_confident_ghsa_matches() -> None:
    """The migration produced a real (non-zero) verified GHSA match set."""
    assert get_agent_cve_summary("openclaw")["ghsa_matched"] > 0


# ─────────────────────────────────────────────────────────────────────────────
# get_agent_cve_summary("hermes")
# ─────────────────────────────────────────────────────────────────────────────


def test_hermes_summary_keys() -> None:
    assert set(get_agent_cve_summary("hermes").keys()) == _EXPECTED_SUMMARY_KEYS


def test_hermes_summary_count_is_seven() -> None:
    assert get_agent_cve_summary("hermes")["total_cves"] == 7


def test_hermes_summary_count_matches_registry() -> None:
    assert get_agent_cve_summary("hermes")["total_cves"] == len(_HERMES_CVE_REGISTRY)


def test_hermes_summary_cves_is_hermes_list() -> None:
    assert get_agent_cve_summary("hermes")["cves"] is _HERMES_CVE_REGISTRY


def test_hermes_summary_wrapped_agent_is_hermes() -> None:
    assert get_agent_cve_summary("hermes")["wrapped_agent"] == "Hermes"


def test_hermes_all_required_titles_present() -> None:
    titles = " ||| ".join(cve["title"] for cve in _HERMES_CVE_REGISTRY)
    for fragment in _HERMES_REQUIRED_TITLE_FRAGMENTS:
        assert fragment in titles, f"Hermes registry missing entry titled ~{fragment!r}"


def test_hermes_all_cves_have_required_fields() -> None:
    for cve in _HERMES_CVE_REGISTRY:
        missing = _REQUIRED_FIELDS - set(cve.keys())
        assert not missing, f"{cve.get('id')} missing fields: {missing}"


def test_hermes_all_statuses_valid() -> None:
    for cve in _HERMES_CVE_REGISTRY:
        assert cve["status"] in _VALID_STATUSES, f"{cve['id']} bad status: {cve['status']}"


def test_hermes_all_severities_valid() -> None:
    for cve in _HERMES_CVE_REGISTRY:
        assert cve["severity"] in _VALID_SEVERITIES, f"{cve['id']} bad severity: {cve['severity']}"


def test_hermes_all_cvss_are_numeric() -> None:
    for cve in _HERMES_CVE_REGISTRY:
        assert isinstance(cve["cvss"], (int, float)), f"{cve['id']} cvss not numeric"
        assert 0.0 <= cve["cvss"] <= 10.0, f"{cve['id']} cvss out of range"


def test_hermes_all_defense_layers_are_lists() -> None:
    for cve in _HERMES_CVE_REGISTRY:
        assert isinstance(cve["defense_layers"], list), f"{cve['id']} defense_layers not list"
        assert len(cve["defense_layers"]) > 0, f"{cve['id']} defense_layers empty"


def test_hermes_by_status_totals_match() -> None:
    summary = get_agent_cve_summary("hermes")
    assert sum(summary["by_status"].values()) == summary["total_cves"]


def test_hermes_by_severity_totals_match() -> None:
    summary = get_agent_cve_summary("hermes")
    assert sum(summary["by_severity"].values()) == summary["total_cves"]


def _hermes_by_title(fragment: str) -> dict:
    return next(c for c in _HERMES_CVE_REGISTRY if fragment in c["title"])


def test_hermes_wechat_adapter_fully_mitigated() -> None:
    cve = _hermes_by_title("Path Traversal in WeChat Work Adapter")
    assert cve["status"] == "fully_mitigated"
    assert "read_only_container" in cve["defense_layers"]


def test_hermes_symlink_entry_upstream_fix() -> None:
    cve = _hermes_by_title("Symlink Following in File Tools")
    assert cve["status"] == "fully_mitigated"
    assert cve["fixed_in"] == "0.9.0"
    assert "upstream_fix" in cve["defense_layers"]


def test_hermes_command_injection_high_severity() -> None:
    cve = _hermes_by_title("OS Command Injection in terminal_tool")
    assert cve["severity"] == "HIGH"
    assert cve["status"] == "fully_mitigated"
    for layer in (
        "tool_acl_deny",
        "command_injection_pattern_scan",
        "approval_queue",
        "network_isolation",
    ):
        assert layer in cve["defense_layers"]


def test_hermes_auth_entries_use_gateway_auth_gate() -> None:
    for fragment in (
        "Missing Authentication on Hermes Agent API Endpoints",
        "Missing Authentication on Hermes Agent Management Endpoints",
    ):
        cve = _hermes_by_title(fragment)
        assert cve["status"] == "fully_mitigated"
        assert "gateway_auth_gate" in cve["defense_layers"]


def test_hermes_all_entries_pending_review() -> None:
    """No public Hermes advisory feed exists, so all Hermes entries are unmatched."""
    for cve in _HERMES_CVE_REGISTRY:
        assert cve["ghsa_id"] is None
        assert cve["cve_id"] is None


# ─────────────────────────────────────────────────────────────────────────────
# Unknown bot_id raises KeyError
# ─────────────────────────────────────────────────────────────────────────────


def test_unknown_bot_id_raises_key_error() -> None:
    with pytest.raises(KeyError):
        get_agent_cve_summary("nonexistent_agent")


def test_empty_bot_id_raises_key_error() -> None:
    with pytest.raises(KeyError):
        get_agent_cve_summary("")


# ─────────────────────────────────────────────────────────────────────────────
# Internal registry dict
# ─────────────────────────────────────────────────────────────────────────────


def test_agent_cve_registries_contains_both() -> None:
    assert "openclaw" in _AGENT_CVE_REGISTRIES
    assert "hermes" in _AGENT_CVE_REGISTRIES


def test_agent_cve_registries_objects_match_lists() -> None:
    assert _AGENT_CVE_REGISTRIES["openclaw"] is _OPENCLAW_CVE_REGISTRY
    assert _AGENT_CVE_REGISTRIES["hermes"] is _HERMES_CVE_REGISTRY
