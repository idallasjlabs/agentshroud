# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Tests for scripts/generate-cve-page.py — M7: Hermes CVE section.

Covers:
- _build_heading(): correct H2 text for both agents.
- _build_table(): correct sentinel markers and tbody id.
- generate(): given a fake index.html with both OpenClaw + Hermes markers,
  the output contains the correct H2 text for each agent and no stale markers.
- generate() fallback: when list_cve_agents is not available, the function still
  produces a valid OpenClaw section (legacy path).
"""

from __future__ import annotations

import importlib
import importlib.util
import sys
from pathlib import Path
from unittest.mock import patch

# ── helpers ───────────────────────────────────────────────────────────────────


REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# Load generate-cve-page.py via importlib because the filename contains a hyphen.
_GEN_MOD_NAME = "scripts._generate_cve_page"
_GEN_MOD_PATH = REPO_ROOT / "scripts" / "generate-cve-page.py"

_SCRIPT_MISSING = not _GEN_MOD_PATH.exists()

if not _SCRIPT_MISSING and _GEN_MOD_NAME not in sys.modules:
    try:
        _spec = importlib.util.spec_from_file_location(_GEN_MOD_NAME, _GEN_MOD_PATH)
        if _spec is not None:
            _gen_mod = importlib.util.module_from_spec(_spec)
            sys.modules[_GEN_MOD_NAME] = _gen_mod
            _spec.loader.exec_module(_gen_mod)  # type: ignore[union-attr]
        else:
            _SCRIPT_MISSING = True
    except Exception:
        _SCRIPT_MISSING = True

# Note: if the script is missing, tests will fail at _get_mod() call (KeyError).
# This is intentional — visibility over silence (no pytest.skip markers per policy).


def _get_mod():
    """Return the generate-cve-page module (already loaded above)."""
    return sys.modules[_GEN_MOD_NAME]


def _make_cve(
    cve_id: str = "CVE-2026-99999",
    title: str = "Test Vuln",
    cvss: float = 7.5,
    severity: str = "HIGH",
    disclosed: str = "2026-03-01",
    status: str = "fully_mitigated",
) -> dict:
    return {
        "id": cve_id,
        "title": title,
        "cvss": cvss,
        "severity": severity,
        "disclosed": disclosed,
        "fixed_in": "",
        "description": "A test vulnerability.",
        "status": status,
        "mitigation": "Mitigated by AgentShroud.",
        "defense_layers": ["network_isolation"],
    }


# Minimal index.html template containing all four sentinel pairs
_TEMPLATE_HTML = """\
<!DOCTYPE html>
<html>
<body>
<section id="cves">
  <div class="container">
    <!-- CVE_HEADING_START -->
    <h2>0 OpenClaw CVEs</h2>
    <!-- CVE_HEADING_END -->
    <!-- CVE_TABLE_START -->
    <!-- placeholder -->
    <!-- CVE_TABLE_END -->
  </div>
</section>
<section id="cves-hermes">
  <div class="container">
    <!-- HERMES_CVE_HEADING_START -->
    <h2>0 Hermes Agent CVEs</h2>
    <!-- HERMES_CVE_HEADING_END -->
    <!-- HERMES_CVE_TABLE_START -->
    <!-- placeholder -->
    <!-- HERMES_CVE_TABLE_END -->
  </div>
</section>
</body>
</html>
"""


# ── unit tests: _build_heading ────────────────────────────────────────────────


class TestBuildHeading:
    """_build_heading returns correct H2 text and sentinel markers."""

    def _call(self, cves, h_start, h_end, label):
        mod = _get_mod()
        return mod._build_heading(cves, h_start, h_end, label)

    def test_openclaw_all_mitigated(self):
        cves = [_make_cve(cve_id=f"CVE-2026-{i}", status="fully_mitigated") for i in range(3)]
        html = self._call(cves, "CVE_HEADING_START", "CVE_HEADING_END", "OpenClaw")
        assert "<h2>3 OpenClaw CVEs — all mitigated</h2>" in html
        assert "<!-- CVE_HEADING_START -->" in html
        assert "<!-- CVE_HEADING_END -->" in html

    def test_hermes_all_mitigated(self):
        cves = [
            _make_cve(cve_id="CVE-2026-7396", status="fully_mitigated"),
            _make_cve(cve_id="CVE-2026-7397", status="fully_mitigated"),
        ]
        html = self._call(
            cves,
            "HERMES_CVE_HEADING_START",
            "HERMES_CVE_HEADING_END",
            "Hermes Agent",
        )
        assert "<h2>2 Hermes Agent CVEs — all mitigated</h2>" in html
        assert "<!-- HERMES_CVE_HEADING_START -->" in html
        assert "<!-- HERMES_CVE_HEADING_END -->" in html

    def test_partial_status_phrase(self):
        cves = [
            _make_cve(cve_id="CVE-2026-1", status="fully_mitigated"),
            _make_cve(cve_id="CVE-2026-2", status="partially_mitigated"),
        ]
        html = self._call(cves, "CVE_HEADING_START", "CVE_HEADING_END", "OpenClaw")
        assert "1 mitigated, 1 partial" in html

    def test_open_status_phrase(self):
        cves = [
            _make_cve(cve_id="CVE-2026-1", status="fully_mitigated"),
            _make_cve(cve_id="CVE-2026-2", status="partially_mitigated"),
            _make_cve(cve_id="CVE-2026-3", status="not_mitigated"),
        ]
        html = self._call(cves, "CVE_HEADING_START", "CVE_HEADING_END", "OpenClaw")
        assert "1 mitigated, 1 partial, 1 open" in html

    def test_zero_cves(self):
        html = self._call([], "CVE_HEADING_START", "CVE_HEADING_END", "OpenClaw")
        assert "<h2>0 OpenClaw CVEs" in html

    def test_under_review_in_heading_not_all_mitigated(self):
        """When some advisories are under_review the heading is honest, NOT 'all mitigated'."""
        cves = [_make_cve(cve_id="CVE-2026-1", status="fully_mitigated")] * 293
        cves = cves + [
            _make_cve(cve_id="CVE-2026-A", status="under_review"),
            _make_cve(cve_id="CVE-2026-B", status="under_review"),
        ]
        html = self._call(cves, "CVE_HEADING_START", "CVE_HEADING_END", "OpenClaw")
        assert "all mitigated" not in html
        assert "293 mitigated, 2 under review" in html

    def test_all_mitigated_only_when_no_under_review(self):
        cves = [_make_cve(cve_id=f"CVE-2026-{i}", status="fully_mitigated") for i in range(4)]
        html = self._call(cves, "CVE_HEADING_START", "CVE_HEADING_END", "OpenClaw")
        assert "all mitigated" in html


# ── unit tests: _build_table ──────────────────────────────────────────────────


class TestBuildTable:
    """_build_table returns correct sentinel markers and unique element ids."""

    def _call(self, cves, t_start, t_end, tbody_id, pg_prefix):
        mod = _get_mod()
        return mod._build_table(cves, t_start, t_end, tbody_id, pg_prefix)

    def test_openclaw_markers_and_tbody_id(self):
        cves = [_make_cve()]
        html = self._call(cves, "CVE_TABLE_START", "CVE_TABLE_END", "cve-tbody", "_pg")
        assert "<!-- CVE_TABLE_START -->" in html
        assert "<!-- CVE_TABLE_END -->" in html
        assert 'id="cve-tbody"' in html

    def test_hermes_markers_and_tbody_id(self):
        cves = [_make_cve(cve_id="CVE-2026-7396")]
        html = self._call(
            cves,
            "HERMES_CVE_TABLE_START",
            "HERMES_CVE_TABLE_END",
            "cve-tbody-hermes",
            "_hpg",
        )
        assert "<!-- HERMES_CVE_TABLE_START -->" in html
        assert "<!-- HERMES_CVE_TABLE_END -->" in html
        assert 'id="cve-tbody-hermes"' in html

    def test_cve_row_contains_id_and_title(self):
        cves = [_make_cve(cve_id="CVE-2026-12345", title="Stack Overflow Bug")]
        html = self._call(cves, "CVE_TABLE_START", "CVE_TABLE_END", "cve-tbody", "_pg")
        assert "CVE-2026-12345" in html
        assert "Stack Overflow Bug" in html

    def test_under_review_badge_rendered(self):
        cve = _make_cve(cve_id="ASH-OCLAW-999", status="under_review")
        html = self._call([cve], "CVE_TABLE_START", "CVE_TABLE_END", "cve-tbody", "_pg")
        # Distinct badge class + label, NOT the mitigated/open badges.
        assert "badge-review" in html
        assert "Under Review" in html
        assert ".badge-review {" in html  # CSS present

    def test_under_review_none_cvss_renders_dash(self):
        cve = _make_cve(cve_id="ASH-OCLAW-998", status="under_review")
        cve["cvss"] = None
        # Must not raise on None cvss during sort/render.
        html = self._call([cve], "CVE_TABLE_START", "CVE_TABLE_END", "cve-tbody", "_pg")
        assert "ASH-OCLAW-998" in html

    def test_pagination_js_uses_unique_prefix(self):
        cves = [_make_cve()]
        oc_html = self._call(cves, "CVE_TABLE_START", "CVE_TABLE_END", "cve-tbody", "_pg")
        h_html = self._call(
            cves,
            "HERMES_CVE_TABLE_START",
            "HERMES_CVE_TABLE_END",
            "cve-tbody-hermes",
            "_hpg",
        )
        # OpenClaw uses _pg; Hermes uses _hpg — verify no cross-contamination
        assert "_pgPg" in oc_html or "_pgCur" in oc_html  # legacy name kept for openclaw
        assert "_hpgPg" in h_html or "_hpgCur" in h_html


# ── integration test: generate() with fake filesystem ─────────────────────────


class TestGenerate:
    """generate() rewrites index.html with correct sections for both agents."""

    def _run_generate(
        self,
        tmp_path: Path,
        openclaw_cves: list,
        hermes_cves: list,
        *,
        multi_agent_api: bool = True,
    ) -> str:
        """Write a fake index.html, invoke generate(), return updated HTML."""
        fake_html = tmp_path / "index.html"
        fake_html.write_text(_TEMPLATE_HTML, encoding="utf-8")

        mod = _get_mod()

        # Build the registry map the module will consume
        registries = {"openclaw": openclaw_cves}
        if hermes_cves:
            registries["hermes"] = hermes_cves

        def fake_resolve_registries():
            return registries

        def fake_list_cve_agents():
            return list(registries.keys())

        def fake_get_summary(bot_id="openclaw"):
            return {"cves": registries[bot_id]}

        with (
            patch.object(mod, "INDEX_HTML", fake_html),
            patch.object(mod, "_resolve_registries", fake_resolve_registries),
            patch.object(mod, "_MULTI_AGENT_API", multi_agent_api),
        ):
            if multi_agent_api:
                with (
                    patch.object(mod, "list_cve_agents", fake_list_cve_agents),
                    patch.object(mod, "get_agent_cve_summary", fake_get_summary),
                ):
                    mod.generate(dry_run=False)
            else:
                mod.generate(dry_run=False)

        return fake_html.read_text(encoding="utf-8")

    def test_openclaw_h2_correct(self, tmp_path):
        oc_cves = [_make_cve(cve_id=f"CVE-2026-{i}", status="fully_mitigated") for i in range(5)]
        html = self._run_generate(tmp_path, oc_cves, [])
        assert "<h2>5 OpenClaw CVEs — all mitigated</h2>" in html

    def test_hermes_h2_correct(self, tmp_path):
        h_cves = [
            _make_cve(cve_id="CVE-2026-7396", status="fully_mitigated"),
            _make_cve(cve_id="CVE-2026-7397", status="partially_mitigated"),
        ]
        html = self._run_generate(tmp_path, [_make_cve()], h_cves)
        assert "<h2>2 Hermes Agent CVEs — 1 mitigated, 1 partial</h2>" in html

    def test_no_stale_openclaw_markers(self, tmp_path):
        # Provide CVEs for both sections so both placeholders are replaced.
        oc_cves = [_make_cve()]
        h_cves = [_make_cve(cve_id="CVE-2026-7396")]
        html = self._run_generate(tmp_path, oc_cves, h_cves)
        # Neither section should have the raw placeholder comment left
        assert "<!-- placeholder -->" not in html

    def test_no_stale_hermes_markers(self, tmp_path):
        h_cves = [_make_cve(cve_id="CVE-2026-7396")]
        html = self._run_generate(tmp_path, [_make_cve()], h_cves)
        assert "<!-- placeholder -->" not in html

    def test_all_four_sentinel_pairs_present(self, tmp_path):
        oc_cves = [_make_cve()]
        h_cves = [_make_cve(cve_id="CVE-2026-7396")]
        html = self._run_generate(tmp_path, oc_cves, h_cves)
        for marker in (
            "<!-- CVE_HEADING_START -->",
            "<!-- CVE_HEADING_END -->",
            "<!-- CVE_TABLE_START -->",
            "<!-- CVE_TABLE_END -->",
            "<!-- HERMES_CVE_HEADING_START -->",
            "<!-- HERMES_CVE_HEADING_END -->",
            "<!-- HERMES_CVE_TABLE_START -->",
            "<!-- HERMES_CVE_TABLE_END -->",
        ):
            assert marker in html, f"Missing sentinel: {marker}"

    def test_legacy_fallback_openclaw_only(self, tmp_path):
        """When list_cve_agents is not available, OpenClaw section is still generated."""
        oc_cves = [_make_cve(cve_id=f"CVE-2026-{i}") for i in range(2)]
        html = self._run_generate(
            tmp_path,
            oc_cves,
            [],
            multi_agent_api=False,
        )
        # OpenClaw section should be generated
        assert "<h2>2 OpenClaw CVEs" in html

    def test_generate_returns_true_when_changed(self, tmp_path):
        fake_html = tmp_path / "index.html"
        fake_html.write_text(_TEMPLATE_HTML, encoding="utf-8")
        mod = _get_mod()
        oc_cves = [_make_cve()]

        def fake_resolve():
            return {"openclaw": oc_cves}

        with (
            patch.object(mod, "INDEX_HTML", fake_html),
            patch.object(mod, "_resolve_registries", fake_resolve),
        ):
            changed = mod.generate(dry_run=False)

        assert changed is True

    def test_generate_returns_false_when_no_change(self, tmp_path):
        fake_html = tmp_path / "index.html"
        mod = _get_mod()
        oc_cves = [_make_cve()]

        def fake_resolve():
            return {"openclaw": oc_cves}

        # First run — produces changed file
        fake_html.write_text(_TEMPLATE_HTML, encoding="utf-8")
        with (
            patch.object(mod, "INDEX_HTML", fake_html),
            patch.object(mod, "_resolve_registries", fake_resolve),
        ):
            mod.generate(dry_run=False)

        # Second run on already-updated file — should be idempotent
        with (
            patch.object(mod, "INDEX_HTML", fake_html),
            patch.object(mod, "_resolve_registries", fake_resolve),
        ):
            changed = mod.generate(dry_run=False)

        assert changed is False
