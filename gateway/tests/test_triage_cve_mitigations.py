# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Tests for scripts/triage-cve-mitigations.py — Phase 2 mitigation-triage engine.

Covers the deterministic core (no security theatre):
  * classify(): each vulnerability class matched from representative advisory text.
  * version compare + source_fix: fixed_in <= running image is honestly patched.
  * triage_entry(): status/defense_layers/mitigation/confidence rules — including
    the honest GAP paths (not_mitigated for uncovered classes; under_review for
    low-confidence / unknown) and the apply-threshold gate.
  * defense_layers reuse: every layer written comes from the existing 293-entry
    vocabulary — NO invented layer names.
  * rewrite_registry_text(): idempotent, in-place field replacement that touches
    ONLY the targeted ids and never another agent's list.
  * per-agent isolation: triage_agent('openclaw') never reads the Hermes list.
  * live-registry consistency: applying the engine keeps get_agent_cve_summary
    counts internally consistent and leaves Hermes untouched.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

_MOD_NAME = "scripts._triage_cve_mitigations"
_MOD_PATH = REPO_ROOT / "scripts" / "triage-cve-mitigations.py"

if _MOD_NAME not in sys.modules:
    _spec = importlib.util.spec_from_file_location(_MOD_NAME, _MOD_PATH)
    assert _spec is not None
    _mod = importlib.util.module_from_spec(_spec)
    sys.modules[_MOD_NAME] = _mod
    _spec.loader.exec_module(_mod)  # type: ignore[union-attr]


def _t():
    return sys.modules[_MOD_NAME]


def _entry(
    entry_id="ASH-OCLAW-999",
    title="Path Traversal in media download",
    description="",
    fixed_in="2026.3.1",
    status="under_review",
):
    return {
        "id": entry_id,
        "ghsa_id": "GHSA-test-test-test",
        "cve_id": None,
        "title": title,
        "cvss": None,
        "severity": "HIGH",
        "disclosed": "2026-03-01",
        "fixed_in": fixed_in,
        "description": description,
        "status": status,
        "mitigation": "",
        "defense_layers": [],
    }


# ── classification ────────────────────────────────────────────────────────────


class TestClassify:
    @pytest.mark.parametrize(
        "title, expected",
        [
            ("Path Traversal in Feishu Media Download", "path_traversal"),
            (
                "Avatar symlink traversal exposes out-of-workspace files",
                "path_traversal",
            ),
            (
                "Zip extraction symlink traversal writes outside destination",
                "path_traversal",
            ),
            ("SSRF via gateway fetch pivot to internal network", "ssrf"),
            ("Sandbox network isolation bypass via docker.network", "ssrf"),
            ("Remote Code Execution via Node Invoke Approval Bypass", "rce"),
            (
                "safeBins PATH-hijack allowed trojan binaries to bypass allowlist",
                "command_injection",
            ),
            (
                "Workspace .env could inject OpenClaw runtime-control variables",
                "command_injection",
            ),
            (
                "ACP resource_link metadata prompt interpolation allowed prompt-injection",
                "prompt_tool_injection",
            ),
            ("Allow-Always Wrapper Persistence approval bypass", "approval_bypass"),
            (
                "1-Click Authentication Token Exfiltration From gatewayUrl",
                "token_exfil",
            ),
            (
                "Nostr privateKey config redaction bypass leaks plaintext signing key",
                "token_exfil",
            ),
            (
                "Unauthorized Senders Trigger Media Download before access check",
                "auth_bypass",
            ),
            (
                "operator.write chat.send could reach admin-only config writes",
                "auth_bypass",
            ),
            ("Telegram webhook bodies read before secret validation", "auth_bypass"),
            (
                "session_status let sandboxed subagents access parent session state",
                "privilege_escalation",
            ),
            ("ReDoS via catastrophic backtracking in parser", "redos"),
            ("Voice-call realtime WebSocket accepted oversized frames", "dos"),
            ("Exported session HTML could keep unsafe markdown links", "xss"),
            ("CSRF on gateway state-changing endpoint", "csrf"),
            ("Unsafe deserialization of pickle payload", "deserialization"),
            (
                "ClawHub package downloads are not enforced with integrity verification",
                "supply_chain",
            ),
            (
                "Plugin install commands could allow non-owner persistence",
                "supply_chain",
            ),
        ],
    )
    def test_representative_titles(self, title, expected):
        t = _t()
        assert t.classify(title, "").value == expected

    def test_unmatched_is_unknown(self):
        t = _t()
        assert (
            t.classify("Totally opaque advisory headline", "no keywords here")
            is t.VulnClass.UNKNOWN
        )

    def test_classification_is_deterministic(self):
        t = _t()
        title = "SSRF via gateway fetch pivot"
        first = t.classify(title, "desc")
        for _ in range(5):
            assert t.classify(title, "desc") == first

    def test_priority_rce_before_generic_injection(self):
        # An advisory that mentions both "code execution" and "injection" is RCE.
        t = _t()
        cls = t.classify(
            "Remote code execution via command injection", "arbitrary code execution"
        )
        assert cls is t.VulnClass.RCE


# ── version compare / source_fix ──────────────────────────────────────────────


class TestVersion:
    def test_parse_numeric(self):
        assert _t().parse_version("2026.4.11") == (2026, 4, 11)

    def test_parse_none_and_empty(self):
        assert _t().parse_version(None) is None
        assert _t().parse_version("") is None

    def test_parse_non_numeric(self):
        assert _t().parse_version("2026.4.x") is None

    def test_source_fixed_older(self):
        assert _t().is_source_fixed("2026.3.1") is True

    def test_source_fixed_equal(self):
        assert _t().is_source_fixed("2026.4.11") is True

    def test_not_source_fixed_newer(self):
        assert _t().is_source_fixed("2026.5.1") is False

    def test_unparseable_is_not_source_fixed(self):
        assert _t().is_source_fixed(None) is False


# ── triage_entry status logic ─────────────────────────────────────────────────


class TestTriageEntry:
    def test_source_fixed_full_class_is_fully_mitigated(self):
        t = _t()
        r = t.triage_entry(_entry(fixed_in="2026.3.1", title="Path Traversal"))
        assert r.status == "fully_mitigated"
        assert r.source_fixed is True
        assert r.defense_layers[0] == "source_fix"
        assert "defense_in_depth" in r.defense_layers
        assert r.applied is True

    def test_not_source_fixed_full_class_is_fully_mitigated_without_source_fix(self):
        t = _t()
        r = t.triage_entry(
            _entry(fixed_in="2026.9.9", title="SSRF to internal metadata")
        )
        assert r.status == "fully_mitigated"
        assert r.source_fixed is False
        assert "source_fix" not in r.defense_layers
        assert "egress_filter" in r.defense_layers

    def test_not_source_fixed_partial_class_is_partially_mitigated(self):
        t = _t()
        r = t.triage_entry(
            _entry(
                fixed_in="2026.9.9",
                title="operator.write reached admin-only config",
                description="authorization mismatch lets write-scope reach admin",
            )
        )
        assert r.status == "partially_mitigated"
        assert r.applied is True

    def test_source_fixed_partial_class_upgrades_to_fully(self):
        t = _t()
        r = t.triage_entry(
            _entry(
                fixed_in="2026.3.1", title="operator.write reached admin-only config"
            )
        )
        assert r.status == "fully_mitigated"
        assert "source_fix" in r.defense_layers

    def test_uncovered_class_not_source_fixed_is_gap(self):
        t = _t()
        r = t.triage_entry(
            _entry(
                fixed_in="2026.9.9",
                title="ClawHub package integrity verification missing",
            )
        )
        assert r.vuln_class is t.VulnClass.SUPPLY_CHAIN
        assert r.status == "not_mitigated"
        assert r.defense_layers == []
        assert r.applied is True  # a confident gap is recorded honestly

    def test_uncovered_class_source_fixed_uses_source_fix(self):
        t = _t()
        r = t.triage_entry(
            _entry(fixed_in="2026.3.1", title="Supply chain: malicious dependency")
        )
        assert r.status == "fully_mitigated"
        assert r.defense_layers == ["source_fix", "defense_in_depth"]

    def test_unknown_class_not_source_fixed_stays_under_review(self):
        t = _t()
        r = t.triage_entry(
            _entry(
                fixed_in="2026.9.9", title="Opaque headline", description="no signal"
            )
        )
        assert r.vuln_class is t.VulnClass.UNKNOWN
        assert t.final_status(r) == "under_review"
        assert r.applied is False

    def test_low_confidence_partial_stays_under_review(self):
        # XSS base_confidence is below the apply threshold; not source-fixed →
        # honest under_review rather than an unearned partial claim.
        t = _t()
        r = t.triage_entry(
            _entry(
                fixed_in="2026.9.9", title="Exported HTML keeps unsafe markdown links"
            )
        )
        assert r.vuln_class is t.VulnClass.XSS
        assert t.final_status(r) == "under_review"

    def test_mitigation_narrative_nonempty_when_applied(self):
        t = _t()
        r = t.triage_entry(_entry(fixed_in="2026.3.1"))
        assert r.mitigation.strip() != ""

    def test_confidence_is_bounded(self):
        t = _t()
        r = t.triage_entry(_entry(fixed_in="2026.3.1"))
        assert 0.0 <= r.confidence <= 1.0


# ── defense-layer vocabulary reuse (NO invented names) ────────────────────────


class TestDefenseLayerVocabulary:
    def test_all_mapped_layers_exist_in_registry(self):
        """Every layer the engine can emit must already be used by a mitigated
        entry in the shipped registry (plus source_fix/defense_in_depth)."""
        t = _t()
        from gateway.security.agent_cve_registry import _OPENCLAW_CVE_REGISTRY

        known: set[str] = set()
        for e in _OPENCLAW_CVE_REGISTRY:
            known.update(e.get("defense_layers") or [])

        emitted: set[str] = set()
        for profile in t.CLASS_PROFILE.values():
            emitted.update(profile.defense_layers)
        emitted.add("source_fix")
        emitted.add("defense_in_depth")

        invented = emitted - known
        assert invented == set(), f"invented defense layers: {sorted(invented)}"


# ── rewrite idempotency + isolation ───────────────────────────────────────────

_SAMPLE_SOURCE = """\
_OPENCLAW_CVE_REGISTRY = [
    {
        "id": "ASH-OCLAW-294",
        "ghsa_id": "GHSA-aaaa",
        "cve_id": None,
        "title": "Path Traversal example",
        "fixed_in": "2026.3.1",
        "status": "under_review",
        "mitigation": "",
        "defense_layers": [],
    },
    {
        "id": "ASH-OCLAW-295",
        "ghsa_id": "GHSA-bbbb",
        "cve_id": None,
        "title": "Supply chain malicious dependency",
        "fixed_in": "2026.9.9",
        "status": "under_review",
        "mitigation": "",
        "defense_layers": [],
    },
]
_HERMES_CVE_REGISTRY = [
    {
        "id": "ASH-HERMES-001",
        "status": "under_review",
        "mitigation": "",
        "defense_layers": [],
    },
]
"""


class TestRewrite:
    def _results(self):
        t = _t()
        e1 = _entry(
            "ASH-OCLAW-294", title="Path Traversal example", fixed_in="2026.3.1"
        )
        e2 = _entry(
            "ASH-OCLAW-295",
            title="Supply chain malicious dependency",
            fixed_in="2026.9.9",
        )
        r1 = t.triage_entry(e1)
        r2 = t.triage_entry(e2)
        return {r1.entry_id: r1, r2.entry_id: r2}

    def test_rewrite_sets_status_and_layers(self):
        t = _t()
        out = t.rewrite_registry_text(_SAMPLE_SOURCE, self._results())
        assert '"status": "fully_mitigated"' in out  # 294 path traversal
        assert '"status": "not_mitigated"' in out  # 295 supply chain gap
        assert '"defense_layers": ["source_fix", "defense_in_depth"' in out

    def test_rewrite_is_idempotent(self):
        t = _t()
        results = self._results()
        once = t.rewrite_registry_text(_SAMPLE_SOURCE, results)
        twice = t.rewrite_registry_text(once, results)
        assert once == twice

    def test_rewrite_never_touches_hermes(self):
        t = _t()
        out = t.rewrite_registry_text(_SAMPLE_SOURCE, self._results())
        # The Hermes entry is not in results → its fields stay pristine.
        assert '"id": "ASH-HERMES-001",\n        "status": "under_review",' in out
        # Hermes mitigation stays empty (never populated by this run).
        hermes_block = out.split("_HERMES_CVE_REGISTRY")[1]
        assert '"mitigation": "",' in hermes_block
        assert '"defense_layers": [],' in hermes_block

    def test_rewrite_untargeted_id_unchanged(self):
        t = _t()
        # Only pass 294; 295 must be byte-identical to input.
        results = self._results()
        partial = {"ASH-OCLAW-294": results["ASH-OCLAW-294"]}
        out = t.rewrite_registry_text(_SAMPLE_SOURCE, partial)
        # The 295 block (id..status) appears verbatim, untouched.
        expected_295 = "\n".join(
            [
                '        "id": "ASH-OCLAW-295",',
                '        "ghsa_id": "GHSA-bbbb",',
                '        "cve_id": None,',
                '        "title": "Supply chain malicious dependency",',
                '        "fixed_in": "2026.9.9",',
                '        "status": "under_review",',
            ]
        )
        assert expected_295 in out


# ── driver + per-agent isolation on the live registry ─────────────────────────


class TestDriverIsolation:
    def test_triage_agent_openclaw_all_under_review_processed(self):
        t = _t()
        from gateway.security.agent_cve_registry import _AGENT_CVE_REGISTRIES

        n_ur = sum(
            1
            for e in _AGENT_CVE_REGISTRIES["openclaw"]
            if e["status"] == "under_review"
        )
        results = t.triage_agent("openclaw")
        assert len(results) == n_ur

    def test_triage_agent_does_not_read_hermes(self):
        t = _t()
        # Every result id is an OpenClaw synthetic id; none are Hermes.
        results = t.triage_agent("openclaw")
        assert all(r.entry_id.startswith("ASH-OCLAW-") for r in results)
        assert not any(r.entry_id.startswith("ASH-HERMES-") for r in results)

    def test_summary_counts_sum_to_total(self):
        t = _t()
        results = t.triage_agent("openclaw")
        s = t.summarize(results)
        assert sum(s["by_status"].values()) == len(results)

    def test_gaps_are_honest_not_mitigated_or_under_review(self):
        t = _t()
        results = t.triage_agent("openclaw")
        s = t.summarize(results)
        for g in s["gaps"]:
            assert t.final_status(g) in ("not_mitigated", "under_review")

    def test_gap_report_renders_and_lists_gaps(self):
        t = _t()
        results = t.triage_agent("openclaw")
        md = t.render_gap_report("openclaw", results)
        assert "Development Plan" in md
        assert "Resulting status breakdown" in md
        # At least the supply-chain gaps must appear as a development task.
        assert "not_mitigated" in md


# ── CLI main() ────────────────────────────────────────────────────────────────


class TestMain:
    def test_dry_run_writes_nothing(self, tmp_path, monkeypatch, capsys):
        t = _t()
        reg = tmp_path / "registry.py"
        gap = tmp_path / "gaps.md"
        reg.write_text("SENTINEL = 1\n")
        monkeypatch.setattr(t, "_REGISTRY_PATH", reg)
        monkeypatch.setattr(t, "_GAP_REPORT_PATH", gap)
        rc = t.main(["--agent", "openclaw", "--dry-run"])
        assert rc == 0
        # registry untouched, gap not written
        assert reg.read_text() == "SENTINEL = 1\n"
        assert not gap.exists()
        out = capsys.readouterr().out
        assert "Triaged" in out
        assert "[dry-run]" in out

    def test_apply_writes_registry_and_gap(self, tmp_path, monkeypatch):
        t = _t()
        # Hermetic: drive main() off a controlled single-entry registry so the
        # test never depends on the shared live registry's mutable state (other
        # CVE tests append/flip entries in the module-level list).
        entry = _entry("ASH-OCLAW-294", title="Path Traversal", fixed_in="2026.3.1")
        monkeypatch.setitem(t._AGENT_CVE_REGISTRIES, "openclaw", [entry])
        reg = tmp_path / "registry.py"
        reg.write_text(
            "_OPENCLAW_CVE_REGISTRY = [\n"
            "    {\n"
            '        "id": "ASH-OCLAW-294",\n'
            '        "status": "under_review",\n'
            '        "mitigation": "",\n'
            '        "defense_layers": [],\n'
            "    },\n"
            "]\n"
        )
        gap = tmp_path / "sub" / "gaps.md"
        monkeypatch.setattr(t, "_REGISTRY_PATH", reg)
        monkeypatch.setattr(t, "_GAP_REPORT_PATH", gap)
        rc = t.main([])
        assert rc == 0
        written = reg.read_text()
        # ASH-OCLAW-294 (RCE, source-fixed) → fully_mitigated with source_fix.
        assert '"status": "fully_mitigated"' in written
        assert '"source_fix"' in written
        assert gap.exists()
        assert "Development Plan" in gap.read_text()

    def test_unknown_agent_errors(self, monkeypatch):
        t = _t()
        with pytest.raises(SystemExit):
            t.main(["--agent", "does-not-exist"])


class TestConsumeFieldEdge:
    def test_unterminated_field_returns_end(self):
        # A field value that never closes (defensive fallthrough) returns EOF idx.
        t = _t()
        lines = ['        "mitigation": (\n', "            unterminated\n"]
        assert t._consume_field(lines, 0) == len(lines)

    def test_multiline_parenthesised_value_consumed(self):
        t = _t()
        lines = [
            '        "mitigation": (\n',
            '            "line one "\n',
            '            "line two"\n',
            "        ),\n",
            '        "next": 1,\n',
        ]
        # Field ends at the closing "),"" line → index 4.
        assert t._consume_field(lines, 0) == 4
