# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Tests for scripts/sync-cve-registry.py — Phase 1 GHSA under_review auto-register.

Covers the honest-under_review pipeline:
  * process_ghsa_advisories(): a new advisory becomes an under_review entry with
    correct fields; NEVER auto-claimed mitigated; ids come straight from the feed.
  * dedup by ghsa_id, then cve_id — idempotent on re-run.
  * never fabricates ids: advisory without a ghsa_id is skipped.
  * per-agent separation: OpenClaw advisories diff only against the OpenClaw list.
  * append_ghsa_entries(): serialized entry parses back to the expected dict and
    targets the correct per-agent list marker.

All HTTP is mocked — no real GitHub calls.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

# Load the hyphenated script as a module.
_MOD_NAME = "scripts._sync_cve_registry"
_MOD_PATH = REPO_ROOT / "scripts" / "sync-cve-registry.py"

if _MOD_NAME not in sys.modules:
    _spec = importlib.util.spec_from_file_location(_MOD_NAME, _MOD_PATH)
    assert _spec is not None
    _mod = importlib.util.module_from_spec(_spec)
    sys.modules[_MOD_NAME] = _mod
    _spec.loader.exec_module(_mod)  # type: ignore[union-attr]


def _sync():
    return sys.modules[_MOD_NAME]


def _adv(
    ghsa_id="GHSA-aaaa-bbbb-cccc",
    cve_id=None,
    summary="Test advisory summary line",
    severity="high",
    published_at="2026-06-01T00:00:00Z",
    cvss_score=7.5,
    patched="2026.5.1",
):
    return {
        "ghsa_id": ghsa_id,
        "cve_id": cve_id,
        "summary": summary,
        "description": "A longer description of the advisory.",
        "severity": severity,
        "published_at": published_at,
        "cvss": {"score": cvss_score} if cvss_score is not None else None,
        "vulnerabilities": [{"patched_versions": patched}] if patched else [],
    }


# ── process_ghsa_advisories ───────────────────────────────────────────────────


class TestProcessGhsaAdvisories:
    def test_new_advisory_becomes_under_review(self):
        mod = _sync()
        registry: list[dict] = []
        out = mod.process_ghsa_advisories([_adv()], registry, "ASH-OCLAW")
        assert len(out) == 1
        e = out[0]
        assert e["status"] == "under_review"
        # HONEST: no mitigation claimed.
        assert e["mitigation"] == ""
        assert e["defense_layers"] == []
        # Real feed ids passed through, never fabricated.
        assert e["ghsa_id"] == "GHSA-aaaa-bbbb-cccc"
        assert e["cve_id"] is None
        assert e["cvss"] == 7.5
        assert e["severity"] == "HIGH"
        assert e["disclosed"] == "2026-06-01"
        assert e["fixed_in"] == "2026.5.1"
        assert e["id"] == "ASH-OCLAW-001"

    def test_id_numbering_continues_from_max(self):
        mod = _sync()
        registry = [{"id": "ASH-OCLAW-042", "ghsa_id": "GHSA-old-old-old"}]
        out = mod.process_ghsa_advisories([_adv()], registry, "ASH-OCLAW")
        assert out[0]["id"] == "ASH-OCLAW-043"

    def test_dedup_by_ghsa_id(self):
        mod = _sync()
        registry = [{"id": "ASH-OCLAW-001", "ghsa_id": "GHSA-aaaa-bbbb-cccc"}]
        out = mod.process_ghsa_advisories([_adv()], registry, "ASH-OCLAW")
        assert out == []

    def test_dedup_by_cve_id(self):
        mod = _sync()
        registry = [{"id": "ASH-OCLAW-001", "ghsa_id": None, "cve_id": "CVE-2026-1"}]
        out = mod.process_ghsa_advisories(
            [_adv(ghsa_id="GHSA-new1-new1-new1", cve_id="CVE-2026-1")],
            registry,
            "ASH-OCLAW",
        )
        assert out == []

    def test_never_fabricates_ids_skips_advisory_without_ghsa(self):
        mod = _sync()
        adv = _adv()
        adv["ghsa_id"] = None
        out = mod.process_ghsa_advisories([adv], [], "ASH-OCLAW")
        assert out == []

    def test_idempotent_on_rerun(self):
        mod = _sync()
        registry: list[dict] = []
        first = mod.process_ghsa_advisories([_adv()], registry, "ASH-OCLAW")
        # Simulate the entry now being in the registry.
        registry.extend(first)
        second = mod.process_ghsa_advisories([_adv()], registry, "ASH-OCLAW")
        assert second == []

    def test_cvss_none_when_absent(self):
        mod = _sync()
        out = mod.process_ghsa_advisories([_adv(cvss_score=None)], [], "ASH-OCLAW")
        assert out[0]["cvss"] is None

    def test_duplicate_within_same_feed_page_registered_once(self):
        mod = _sync()
        out = mod.process_ghsa_advisories([_adv(), _adv()], [], "ASH-OCLAW")
        assert len(out) == 1

    def test_per_agent_prefix_applied(self):
        mod = _sync()
        out = mod.process_ghsa_advisories([_adv(ghsa_id="GHSA-herm-herm-herm")], [], "ASH-HERMES")
        assert out[0]["id"] == "ASH-HERMES-001"


# ── serialization / append ────────────────────────────────────────────────────


class TestSerialization:
    def test_entry_to_py_roundtrips(self):
        mod = _sync()
        out = mod.process_ghsa_advisories([_adv()], [], "ASH-OCLAW")
        src = mod._ghsa_entry_to_py(out[0])
        # Evaluate the serialized dict literal (strip trailing comma).
        parsed = eval(src.strip().rstrip(","))  # noqa: S307 — trusted, test-only
        assert parsed["status"] == "under_review"
        assert parsed["ghsa_id"] == "GHSA-aaaa-bbbb-cccc"
        assert parsed["mitigation"] == ""
        assert parsed["defense_layers"] == []
        assert parsed["cvss"] == 7.5

    def test_entry_to_py_handles_none_cvss(self):
        mod = _sync()
        out = mod.process_ghsa_advisories([_adv(cvss_score=None)], [], "ASH-OCLAW")
        src = mod._ghsa_entry_to_py(out[0])
        parsed = eval(src.strip().rstrip(","))  # noqa: S307
        assert parsed["cvss"] is None

    def test_append_targets_correct_agent_marker(self, tmp_path, monkeypatch):
        mod = _sync()
        fake_registry = tmp_path / "agent_cve_registry.py"
        fake_registry.write_text(
            "X = [\n]\n\n# ── Hermes Agent CVE Registry\nY = [\n"
            "]\n\n# ── Multi-agent registry lookup\n"
        )
        monkeypatch.setattr(mod, "REPO_ROOT", tmp_path)
        # Point the append at our fake file layout.
        (tmp_path / "gateway" / "security").mkdir(parents=True)
        (tmp_path / "gateway" / "security" / "agent_cve_registry.py").write_text(
            fake_registry.read_text()
        )
        out = mod.process_ghsa_advisories([_adv()], [], "ASH-OCLAW")
        n = mod.append_ghsa_entries(out, "openclaw", dry_run=False)
        assert n == 1
        written = (tmp_path / "gateway" / "security" / "agent_cve_registry.py").read_text()
        # The new entry lands before the OpenClaw list marker, not the Hermes one.
        oc_idx = written.index("# ── Hermes Agent CVE Registry")
        assert "under_review" in written[:oc_idx]

    def test_dry_run_writes_nothing(self, tmp_path, monkeypatch):
        mod = _sync()
        monkeypatch.setattr(mod, "REPO_ROOT", tmp_path)
        (tmp_path / "gateway" / "security").mkdir(parents=True)
        target = tmp_path / "gateway" / "security" / "agent_cve_registry.py"
        original = (
            "X = [\n]\n\n# ── Hermes Agent CVE Registry\nY = [\n"
            "]\n\n# ── Multi-agent registry lookup\n"
        )
        target.write_text(original)
        out = mod.process_ghsa_advisories([_adv()], [], "ASH-OCLAW")
        n = mod.append_ghsa_entries(out, "openclaw", dry_run=True)
        assert n == 1
        assert target.read_text() == original  # unchanged


# ── fetch (HTTP mocked) ───────────────────────────────────────────────────────


class TestFetch:
    def test_fetch_paginates_via_link_cursor(self):
        mod = _sync()
        pages = [
            (
                [_adv(ghsa_id="GHSA-p1p1-p1p1-p1p1")],
                '<https://api.github.com/next>; rel="next"',
            ),
            ([_adv(ghsa_id="GHSA-p2p2-p2p2-p2p2")], ""),
        ]
        calls = {"i": 0}

        class _Resp:
            def __init__(self, body, link):
                self._body = body
                self.headers = {"Link": link}

            def read(self):
                import json

                return json.dumps(self._body).encode("utf-8")

            def __enter__(self):
                return self

            def __exit__(self, *a):
                return False

        def _fake_urlopen(req, timeout=30):
            body, link = pages[calls["i"]]
            calls["i"] += 1
            return _Resp(body, link)

        with patch.object(mod.urllib.request, "urlopen", _fake_urlopen):
            out = mod.fetch_ghsa_advisories("openclaw/openclaw")
        ghsa_ids = {a["ghsa_id"] for a in out}
        assert ghsa_ids == {"GHSA-p1p1-p1p1-p1p1", "GHSA-p2p2-p2p2-p2p2"}
        assert calls["i"] == 2  # followed the cursor once


# ── per-agent isolation ───────────────────────────────────────────────────────


class TestPerAgentIsolation:
    def test_openclaw_advisory_does_not_touch_hermes_registry(self):
        """An OpenClaw advisory diffed against the Hermes list yields it as 'new'.

        Proves the two registries are separate: an id known to OpenClaw is NOT
        treated as known when processing against the Hermes list.
        """
        mod = _sync()
        openclaw_known = [{"id": "ASH-OCLAW-001", "ghsa_id": "GHSA-aaaa-bbbb-cccc"}]
        hermes_registry: list[dict] = []
        # Same advisory, processed against the (empty) Hermes list — must be new.
        out = mod.process_ghsa_advisories([_adv()], hermes_registry, "ASH-HERMES")
        assert len(out) == 1
        # And against the OpenClaw list that already has it — must be empty.
        out2 = mod.process_ghsa_advisories([_adv()], openclaw_known, "ASH-OCLAW")
        assert out2 == []


# ── real snapshot smoke (offline, committed data) ─────────────────────────────


class TestSnapshotSmoke:
    def test_openclaw_snapshot_registers_backlog_as_under_review(self):
        """The committed snapshot yields a real backlog, all honest under_review.

        Diffs the snapshot against a PRE-backlog baseline reconstructed by dedup
        key (ghsa_id), matching process_ghsa_advisories' own dedup logic exactly
        -- NOT by filtering on status != "under_review". That status-based
        proxy broke once a live triage run resolved every previously-under_review
        entry to fully_mitigated (2026-07-31): the live registry then has zero
        under_review entries, so filtering by status stopped removing anything
        and the reconstructed "baseline" silently became the full post-sync
        registry, masking real advisories as already-known. Filtering by ghsa_id
        instead makes this test's baseline correct regardless of what status the
        live registry's entries currently carry.
        """
        mod = _sync()
        import json

        from gateway.security.agent_cve_registry import _OPENCLAW_CVE_REGISTRY

        snap = json.loads(
            (REPO_ROOT / "scripts" / "data" / "openclaw-ghsa-snapshot.json").read_text()
        )

        # Reconstruct the pre-sync baseline: exclude any registry entry whose
        # ghsa_id is one the snapshot would itself introduce -- the same dedup
        # key process_ghsa_advisories uses, so this baseline is correct no
        # matter what status those entries currently carry in the live registry.
        snapshot_ghsa_ids = {a.get("ghsa_id") for a in snap["openclaw"] if a.get("ghsa_id")}
        baseline = [e for e in _OPENCLAW_CVE_REGISTRY if e.get("ghsa_id") not in snapshot_ghsa_ids]
        out = mod.process_ghsa_advisories(snap["openclaw"], baseline, "ASH-OCLAW")
        assert len(out) > 0
        assert all(e["status"] == "under_review" for e in out)
        assert all(e["mitigation"] == "" for e in out)
        assert all(e["defense_layers"] == [] for e in out)
        # ids are unique.
        ids = [e["id"] for e in out]
        assert len(ids) == len(set(ids))
        # Real GHSA ids only — never fabricated.
        assert all(e["ghsa_id"] and e["ghsa_id"].startswith("GHSA-") for e in out)

    def test_live_registry_is_idempotent_no_new_backlog(self):
        """Re-running against the LIVE registry adds nothing (backlog already synced)."""
        mod = _sync()
        import json

        from gateway.security.agent_cve_registry import _OPENCLAW_CVE_REGISTRY

        snap = json.loads(
            (REPO_ROOT / "scripts" / "data" / "openclaw-ghsa-snapshot.json").read_text()
        )
        out = mod.process_ghsa_advisories(
            snap["openclaw"], list(_OPENCLAW_CVE_REGISTRY), "ASH-OCLAW"
        )
        assert out == []

    def test_hermes_snapshot_zero_new(self):
        mod = _sync()
        import json

        from gateway.security.agent_cve_registry import _HERMES_CVE_REGISTRY

        snap = json.loads(
            (REPO_ROOT / "scripts" / "data" / "openclaw-ghsa-snapshot.json").read_text()
        )
        out = mod.process_ghsa_advisories(
            snap.get("hermes", []), list(_HERMES_CVE_REGISTRY), "ASH-HERMES"
        )
        assert out == []


if __name__ == "__main__":
    sys.exit(pytest.main([__file__, "-v"]))
