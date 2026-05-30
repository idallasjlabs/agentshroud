# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for gateway/security/agent_cve_registry.py — multi-agent CVE registry.

Covers:
- Backward-compat: AGENT_CVE_REGISTRY alias, WRAPPED_AGENT constant
- get_agent_cve_summary() with no args defaults to openclaw
- get_agent_cve_summary("openclaw") returns all existing OpenClaw CVEs
- get_agent_cve_summary("hermes") returns 7 Hermes CVEs with correct schema
- list_cve_agents() returns ["openclaw", "hermes"]
- Unknown bot_id raises KeyError
- All Hermes CVE entries contain required schema fields
- HERMES_CVE_REGISTRY public alias is non-empty
"""

from __future__ import annotations

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

# ── Required CVE dict fields (every entry in every registry must have these) ──
_REQUIRED_FIELDS = frozenset(
    {
        "id",
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

# IDs of CVEs that must be present in the Hermes registry (task spec).
_HERMES_REQUIRED_IDS = {
    "CVE-2026-7396",
    "CVE-2026-7397",
    "CVE-2026-6829",
    "CVE-2026-9352",
    "CVE-2026-9367",
    "CVE-2026-7112",
    "CVE-2026-7113",
}


# ─────────────────────────────────────────────────────────────────────────────
# Backward-compatibility constants
# ─────────────────────────────────────────────────────────────────────────────


def test_wrapped_agent_constant_unchanged() -> None:
    """WRAPPED_AGENT must remain 'OpenClaw' for downstream consumers."""
    assert WRAPPED_AGENT == "OpenClaw"


def test_agent_cve_registry_alias_nonempty() -> None:
    """Public AGENT_CVE_REGISTRY alias still exposes the OpenClaw list."""
    assert len(AGENT_CVE_REGISTRY) > 0


def test_agent_cve_registry_alias_is_openclaw_list() -> None:
    """AGENT_CVE_REGISTRY must be the exact same object as _OPENCLAW_CVE_REGISTRY."""
    assert AGENT_CVE_REGISTRY is _OPENCLAW_CVE_REGISTRY


def test_hermes_cve_registry_public_alias() -> None:
    """HERMES_CVE_REGISTRY public alias must be non-empty and match private list."""
    assert len(HERMES_CVE_REGISTRY) > 0
    assert HERMES_CVE_REGISTRY is _HERMES_CVE_REGISTRY


# ─────────────────────────────────────────────────────────────────────────────
# list_cve_agents()
# ─────────────────────────────────────────────────────────────────────────────


def test_list_cve_agents_returns_both() -> None:
    """list_cve_agents() must return exactly ['openclaw', 'hermes']."""
    agents = list_cve_agents()
    assert agents == ["openclaw", "hermes"]


def test_list_cve_agents_is_list_of_str() -> None:
    agents = list_cve_agents()
    assert isinstance(agents, list)
    assert all(isinstance(a, str) for a in agents)


# ─────────────────────────────────────────────────────────────────────────────
# get_agent_cve_summary() — default / no-arg (backward compat)
# ─────────────────────────────────────────────────────────────────────────────


def test_default_summary_equals_openclaw_summary() -> None:
    """Calling with no args must produce the same result as bot_id='openclaw'."""
    default = get_agent_cve_summary()
    explicit = get_agent_cve_summary("openclaw")
    # Compare everything except the 'cves' list identity (both point at same list)
    assert default["total_cves"] == explicit["total_cves"]
    assert default["by_status"] == explicit["by_status"]
    assert default["by_severity"] == explicit["by_severity"]
    assert default["wrapped_agent"] == explicit["wrapped_agent"]
    assert default["cves"] is explicit["cves"]


def test_default_summary_wrapped_agent_openclaw() -> None:
    summary = get_agent_cve_summary()
    assert summary["wrapped_agent"] == "OpenClaw"


# ─────────────────────────────────────────────────────────────────────────────
# get_agent_cve_summary("openclaw")
# ─────────────────────────────────────────────────────────────────────────────


def test_openclaw_summary_keys() -> None:
    summary = get_agent_cve_summary("openclaw")
    assert set(summary.keys()) == {
        "wrapped_agent",
        "total_cves",
        "by_status",
        "by_severity",
        "cves",
    }


def test_openclaw_summary_count_matches_registry() -> None:
    summary = get_agent_cve_summary("openclaw")
    assert summary["total_cves"] == len(_OPENCLAW_CVE_REGISTRY)


def test_openclaw_summary_cves_is_openclaw_list() -> None:
    summary = get_agent_cve_summary("openclaw")
    assert summary["cves"] is _OPENCLAW_CVE_REGISTRY


def test_openclaw_cve_22171_present() -> None:
    """CVE-2026-22171 is the first manually curated OpenClaw entry; verify it exists."""
    ids = {cve["id"] for cve in get_agent_cve_summary("openclaw")["cves"]}
    assert "CVE-2026-22171" in ids


def test_openclaw_all_cves_have_required_fields() -> None:
    # Six pre-existing OpenClaw entries (e.g. CVE-2026-30741) were authored
    # without a 'fixed_in' key — 'fixed_in' is absent, not None.  We do not
    # modify those legacy entries (task constraint: keep all OpenClaw CVEs
    # unchanged).  Verify the mandatory subset that all entries have.
    _OPENCLAW_REQUIRED = _REQUIRED_FIELDS - {"fixed_in"}
    for cve in _OPENCLAW_CVE_REGISTRY:
        missing = _OPENCLAW_REQUIRED - set(cve.keys())
        assert not missing, f"{cve.get('id')} missing fields: {missing}"


def test_openclaw_all_statuses_valid() -> None:
    for cve in _OPENCLAW_CVE_REGISTRY:
        assert cve["status"] in _VALID_STATUSES, f"{cve['id']} has invalid status: {cve['status']}"


def test_openclaw_all_severities_valid() -> None:
    for cve in _OPENCLAW_CVE_REGISTRY:
        assert (
            cve["severity"] in _VALID_SEVERITIES
        ), f"{cve['id']} has invalid severity: {cve['severity']}"


def test_openclaw_by_status_totals_match() -> None:
    summary = get_agent_cve_summary("openclaw")
    assert sum(summary["by_status"].values()) == summary["total_cves"]


def test_openclaw_by_severity_totals_match() -> None:
    summary = get_agent_cve_summary("openclaw")
    assert sum(summary["by_severity"].values()) == summary["total_cves"]


# ─────────────────────────────────────────────────────────────────────────────
# get_agent_cve_summary("hermes")
# ─────────────────────────────────────────────────────────────────────────────


def test_hermes_summary_keys() -> None:
    summary = get_agent_cve_summary("hermes")
    assert set(summary.keys()) == {
        "wrapped_agent",
        "total_cves",
        "by_status",
        "by_severity",
        "cves",
    }


def test_hermes_summary_count_is_seven() -> None:
    """Hermes registry must contain exactly the 7 CVEs specified in M1."""
    summary = get_agent_cve_summary("hermes")
    assert summary["total_cves"] == 7


def test_hermes_summary_count_matches_registry() -> None:
    summary = get_agent_cve_summary("hermes")
    assert summary["total_cves"] == len(_HERMES_CVE_REGISTRY)


def test_hermes_summary_cves_is_hermes_list() -> None:
    summary = get_agent_cve_summary("hermes")
    assert summary["cves"] is _HERMES_CVE_REGISTRY


def test_hermes_summary_wrapped_agent_is_hermes() -> None:
    summary = get_agent_cve_summary("hermes")
    assert summary["wrapped_agent"] == "Hermes"


def test_hermes_all_required_ids_present() -> None:
    ids = {cve["id"] for cve in _HERMES_CVE_REGISTRY}
    missing = _HERMES_REQUIRED_IDS - ids
    assert not missing, f"Hermes registry missing required CVE IDs: {missing}"


def test_hermes_all_cves_have_required_fields() -> None:
    for cve in _HERMES_CVE_REGISTRY:
        missing = _REQUIRED_FIELDS - set(cve.keys())
        assert not missing, f"{cve.get('id')} missing fields: {missing}"


def test_hermes_all_statuses_valid() -> None:
    for cve in _HERMES_CVE_REGISTRY:
        assert cve["status"] in _VALID_STATUSES, f"{cve['id']} has invalid status: {cve['status']}"


def test_hermes_all_severities_valid() -> None:
    for cve in _HERMES_CVE_REGISTRY:
        assert (
            cve["severity"] in _VALID_SEVERITIES
        ), f"{cve['id']} has invalid severity: {cve['severity']}"


def test_hermes_all_cvss_are_numeric() -> None:
    for cve in _HERMES_CVE_REGISTRY:
        assert isinstance(
            cve["cvss"], (int, float)
        ), f"{cve['id']} cvss must be numeric, got {type(cve['cvss'])}"
        assert 0.0 <= cve["cvss"] <= 10.0, f"{cve['id']} cvss {cve['cvss']} out of range [0, 10]"


def test_hermes_all_defense_layers_are_lists() -> None:
    for cve in _HERMES_CVE_REGISTRY:
        assert isinstance(cve["defense_layers"], list), f"{cve['id']} defense_layers must be a list"
        assert len(cve["defense_layers"]) > 0, f"{cve['id']} defense_layers must be non-empty"


def test_hermes_by_status_totals_match() -> None:
    summary = get_agent_cve_summary("hermes")
    assert sum(summary["by_status"].values()) == summary["total_cves"]


def test_hermes_by_severity_totals_match() -> None:
    summary = get_agent_cve_summary("hermes")
    assert sum(summary["by_severity"].values()) == summary["total_cves"]


def test_hermes_7396_fully_mitigated() -> None:
    cve = next(c for c in _HERMES_CVE_REGISTRY if c["id"] == "CVE-2026-7396")
    assert cve["status"] == "fully_mitigated"
    assert "read_only_container" in cve["defense_layers"]


def test_hermes_7397_fully_mitigated_with_upstream_fix() -> None:
    cve = next(c for c in _HERMES_CVE_REGISTRY if c["id"] == "CVE-2026-7397")
    assert cve["status"] == "fully_mitigated"
    assert cve["fixed_in"] == "0.9.0"
    assert "upstream_fix" in cve["defense_layers"]


def test_hermes_9367_high_severity_fully_mitigated() -> None:
    cve = next(c for c in _HERMES_CVE_REGISTRY if c["id"] == "CVE-2026-9367")
    assert cve["severity"] == "HIGH"
    assert cve["status"] == "fully_mitigated"
    assert "tool_acl_deny" in cve["defense_layers"]
    assert "command_injection_pattern_scan" in cve["defense_layers"]
    assert "approval_queue" in cve["defense_layers"]
    assert "network_isolation" in cve["defense_layers"]


def test_hermes_7112_and_7113_gateway_auth_gate() -> None:
    for cve_id in ("CVE-2026-7112", "CVE-2026-7113"):
        cve = next(c for c in _HERMES_CVE_REGISTRY if c["id"] == cve_id)
        assert cve["status"] == "fully_mitigated"
        assert "gateway_auth_gate" in cve["defense_layers"]


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
