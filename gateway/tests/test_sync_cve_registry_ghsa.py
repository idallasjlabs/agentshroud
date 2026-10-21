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


# A minimal registry file in the real file's layout: per-agent lists plus the
# _AGENT_CVE_REGISTRIES dict the sync script resolves list names from.
_FAKE_REGISTRY = (
    "X = [\n]\n\n# ── Hermes Agent CVE Registry\nY = [\n]\n\n"
    '_AGENT_CVE_REGISTRIES = {"openclaw": X, "hermes": Y}\n'
)


def _exec_registry(src: str) -> dict:
    ns: dict = {}
    exec(compile(src, "<registry>", "exec"), ns)  # noqa: S102 — trusted, test-only
    return ns


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

    @pytest.mark.parametrize(
        "text, quote",
        [
            ("plain text", '"'),
            ('a "remote" policy', "'"),  # more " than ': black uses single quotes
            ("policy file's path", '"'),
            ('it\'s "x" and "y"', "'"),
            ("line\r\nbreak\tand \\ backslash — ünïcode", '"'),
        ],
    )
    def test_string_literals_match_black_quote_preference(self, text, quote):
        """CI runs black on gateway/; an appended registry block must already be clean."""
        mod = _sync()
        lit = mod._py_str(text)
        assert lit[0] == quote and lit[-1] == quote
        assert eval(lit) == text  # noqa: S307 — trusted, test-only

    def test_entry_to_py_handles_none_cvss(self):
        mod = _sync()
        out = mod.process_ghsa_advisories([_adv(cvss_score=None)], [], "ASH-OCLAW")
        src = mod._ghsa_entry_to_py(out[0])
        parsed = eval(src.strip().rstrip(","))  # noqa: S307
        assert parsed["cvss"] is None

    def test_append_targets_correct_agent_list(self, tmp_path, monkeypatch):
        mod = _sync()
        monkeypatch.setattr(mod, "REPO_ROOT", tmp_path)
        (tmp_path / "gateway" / "security").mkdir(parents=True)
        target = tmp_path / "gateway" / "security" / "agent_cve_registry.py"
        target.write_text(_FAKE_REGISTRY)
        out = mod.process_ghsa_advisories([_adv()], [], "ASH-OCLAW")
        n = mod.append_ghsa_entries(out, "openclaw", dry_run=False)
        assert n == 1
        ns = _exec_registry(target.read_text())
        # The new entry lands in the OpenClaw list only, never the Hermes one.
        assert [e["ghsa_id"] for e in ns["X"]] == ["GHSA-aaaa-bbbb-cccc"]
        assert ns["Y"] == []

    def test_dry_run_writes_nothing(self, tmp_path, monkeypatch):
        mod = _sync()
        monkeypatch.setattr(mod, "REPO_ROOT", tmp_path)
        (tmp_path / "gateway" / "security").mkdir(parents=True)
        target = tmp_path / "gateway" / "security" / "agent_cve_registry.py"
        original = _FAKE_REGISTRY
        target.write_text(original)
        out = mod.process_ghsa_advisories([_adv()], [], "ASH-OCLAW")
        n = mod.append_ghsa_entries(out, "openclaw", dry_run=True)
        assert n == 1
        assert target.read_text() == original  # unchanged


# ── list locator (syntax-tree based, survives reformatting) ───────────────────
#
# The previous implementation found each list's end by literal text such as
# "]\n\n# ── Falco CVE Registry". A formatter wrapped the tool lists in
# parentheses and the markers stopped matching; the script printed ERROR,
# returned 0 and exited 0 for every run. These tests pin the replacement.


_ONE = '    {"id": "A-1", "ghsa_id": "GHSA-0000-0000-0001"},\n'


class TestListLocator:
    @pytest.mark.parametrize(
        "src",
        [
            # plain list
            "R: list = [\n" + _ONE + "]\n",
            # formatter-wrapped list, as the tool registries are today
            "R: list = (\n    [\n    " + _ONE + "    ]\n)\n",
            # concatenated batches: insert into the last literal
            "R = [\n" + _ONE + '] + [\n    {"id": "A-2"},\n]\n',
            # empty inline list (OpenSCAP / ClamAV / Semgrep)
            "R: list = []\n",
            # inline list whose last element has no trailing comma
            'R = [{"id": "A-1"}]\n',
        ],
        ids=["plain", "parenthesised", "concatenated", "empty", "inline-no-comma"],
    )
    def test_insert_adds_exactly_n_entries_and_still_parses(self, src):
        mod = _sync()
        before = len(_exec_registry(src)["R"])
        entries = [
            {"id": "N-1", "ghsa_id": "GHSA-1111-1111-1111"},
            {"id": "N-2", "ghsa_id": "GHSA-2222-2222-2222"},
        ]
        new = mod._insert_into_list(
            src, "R", lambda indent: "\n".join(f"{' ' * indent}{e!r}," for e in entries)
        )
        after = _exec_registry(new)["R"]
        assert len(after) == before + 2
        assert after[-1]["id"] == "N-2"
        assert mod._count_list_entries(new, "R") == before + 2

    def test_missing_variable_raises(self):
        mod = _sync()
        with pytest.raises(mod.RegistryLayoutError):
            mod._insert_into_list("Q = []\n", "R", lambda indent: "")

    def test_non_list_value_raises(self):
        mod = _sync()
        with pytest.raises(mod.RegistryLayoutError):
            mod._insert_into_list("R = make()\n", "R", lambda indent: "")

    def test_agent_var_resolved_from_registry_dict(self):
        mod = _sync()
        assert mod._registry_var_for(_FAKE_REGISTRY, "hermes") == "Y"
        with pytest.raises(mod.RegistryLayoutError):
            mod._registry_var_for(_FAKE_REGISTRY, "nosuchagent")


class TestLiveRegistryLayout:
    """Runs against the REAL gateway/security/agent_cve_registry.py.

    Every registered agent's list must be locatable, and an append into a copy
    of the real file must add exactly N entries and still import. This is the
    check that would have caught 200 silent "marker not found" runs.
    """

    def test_every_agent_list_accepts_an_append(self):
        mod = _sync()
        from gateway.security.agent_cve_registry import _AGENT_CVE_REGISTRIES

        live = (REPO_ROOT / "gateway" / "security" / "agent_cve_registry.py").read_text()
        for agent_id, entries in _AGENT_CVE_REGISTRIES.items():
            var = mod._registry_var_for(live, agent_id)
            assert mod._count_list_entries(live, var) == len(entries), agent_id
            adv = _adv(ghsa_id=f"GHSA-test-{agent_id[:4]:x<4}-live")
            new_entries = mod.process_ghsa_advisories([adv], [], "ASH-TEST")
            new = mod._insert_into_list(
                live,
                var,
                lambda indent: "\n".join(mod._ghsa_entry_to_py(e, indent) for e in new_entries),
            )
            assert mod._count_list_entries(new, var) == len(entries) + 1, agent_id
            compile(new, "agent_cve_registry.py", "exec")


class TestNvdAppend:
    """The NVD source appends to the OpenClaw / Hermes lists through the same locator."""

    def _nvd_entry(self, cid="CVE-2026-0001"):
        return {
            "id": cid,
            "title": "t",
            "cvss": 7.5,
            "severity": "HIGH",
            "disclosed": "2026-10-01",
            "fixed_in": "1.2.3",
            "description": "d",
            "status": "under_review",
            "mitigation": "",
            "defense_layers": [],
        }

    @pytest.fixture
    def registry(self, tmp_path, monkeypatch):
        mod = _sync()
        monkeypatch.setattr(mod, "REPO_ROOT", tmp_path)
        (tmp_path / "gateway" / "security").mkdir(parents=True)
        target = tmp_path / "gateway" / "security" / "agent_cve_registry.py"
        target.write_text(
            "_OPENCLAW_CVE_REGISTRY = [\n]\n_HERMES_CVE_REGISTRY: list = (\n    [\n    ]\n)\n"
        )
        return target

    def test_openclaw_and_hermes_lists_each_get_their_own_entry(self, registry):
        mod = _sync()
        assert mod.append_to_registry([self._nvd_entry("CVE-A")], False, "2026.10.4") == 1
        assert mod.append_to_hermes_registry([self._nvd_entry("CVE-H")], False, "v0.22") == 1
        ns = _exec_registry(registry.read_text())
        assert [e["id"] for e in ns["_OPENCLAW_CVE_REGISTRY"]] == ["CVE-A"]
        assert [e["id"] for e in ns["_HERMES_CVE_REGISTRY"]] == ["CVE-H"]

    def test_dry_run_reports_count_and_writes_nothing(self, registry):
        mod = _sync()
        before = registry.read_text()
        assert mod.append_to_registry([self._nvd_entry()], True, "2026.10.4") == 1
        assert registry.read_text() == before

    def test_empty_input_is_a_no_op(self, registry):
        mod = _sync()
        assert mod.append_to_hermes_registry([], False, "v0.22") == 0


class TestNvdReportOnly:
    """The NVD path emits the pre-migration schema (id=CVE-…, no ghsa_id/cve_id).

    2026-10-21 auto-PR #524 wrote 724 such entries and broke
    test_agent_cve_registry.py on main. Until it emits the ASH-ref schema it
    must report its backlog and write nothing.
    """

    def _run(self, monkeypatch, capsys, oc_ids, hermes_ids):
        import argparse

        mod = _sync()
        feeds = {mod.NVD_KEYWORD: oc_ids, mod.NVD_KEYWORD_HERMES: hermes_ids}
        monkeypatch.setattr(
            mod, "fetch_nvd_cves", lambda kw: [{"cve": {"id": i}} for i in feeds[kw]]
        )

        def _no_write(*a, **k):
            raise AssertionError("NVD path must not write the registry")

        monkeypatch.setattr(mod, "append_to_registry", _no_write)
        monkeypatch.setattr(mod, "append_to_hermes_registry", _no_write)
        monkeypatch.setattr(mod, "_insert_into_list", _no_write)
        args = argparse.Namespace(dry_run=False, openclaw_version="2026.10.4", hermes_version="v0")
        mod._run_nvd_sync(args)
        return mod, capsys.readouterr().out

    def test_never_writes_and_says_so(self, monkeypatch, capsys):
        _, out = self._run(monkeypatch, capsys, ["CVE-2099-0001"], ["CVE-2099-0002"])
        assert "NOT written" in out

    def test_known_cves_matched_by_cve_id_not_id(self, monkeypatch, capsys):
        mod = _sync()
        known = next(e["cve_id"] for e in mod.AGENT_CVE_REGISTRY if e.get("cve_id"))
        _, out = self._run(monkeypatch, capsys, [known, "CVE-2099-0001"], [])
        assert "OpenClaw: 1 NVD CVE(s) not in the registry" in out

    @staticmethod
    def _page(total, n):
        import io
        import json

        body = {"totalResults": total, "vulnerabilities": [{"cve": {"id": i}} for i in range(n)]}
        return io.BytesIO(json.dumps(body).encode("utf-8"))

    def test_transient_read_timeout_is_retried(self, monkeypatch):
        mod = _sync()
        monkeypatch.setattr(mod.time, "sleep", lambda s: None)
        calls = {"n": 0}

        def _fake_urlopen(req, timeout=30):
            calls["n"] += 1
            if calls["n"] == 1:
                raise TimeoutError("The read operation timed out")
            return self._page(2, 2)

        monkeypatch.setattr(mod.urllib.request, "urlopen", _fake_urlopen)
        assert len(mod.fetch_nvd_cves("x")) == 2
        assert calls["n"] == 2

    def test_persistent_failure_exits_non_zero(self, monkeypatch):
        mod = _sync()
        monkeypatch.setattr(mod.time, "sleep", lambda s: None)
        calls = {"n": 0}

        def _fake_urlopen(req, timeout=30):
            calls["n"] += 1
            raise TimeoutError("The read operation timed out")

        monkeypatch.setattr(mod.urllib.request, "urlopen", _fake_urlopen)
        with pytest.raises(SystemExit) as exc:
            mod.fetch_nvd_cves("x")
        assert exc.value.code != 0
        assert calls["n"] == mod.NVD_FETCH_ATTEMPTS


class TestFailsLoudly:
    def test_edit_that_does_not_add_n_entries_is_rejected(self, tmp_path, monkeypatch):
        mod = _sync()
        monkeypatch.setattr(mod, "REPO_ROOT", tmp_path)
        (tmp_path / "gateway" / "security").mkdir(parents=True)
        target = tmp_path / "gateway" / "security" / "agent_cve_registry.py"
        target.write_text("R = [\n]\n")
        # An insertion that silently produces nothing must not count as success.
        monkeypatch.setattr(mod, "_insert_into_list", lambda content, var, render: content)
        with pytest.raises(mod.RegistryLayoutError):
            mod._append_verified("R", lambda indent: "", 1, dry_run=False)
        assert target.read_text() == "R = [\n]\n"

    def test_nvd_layout_failure_exits_nonzero(self, monkeypatch):
        mod = _sync()

        def _boom(args):
            raise mod.RegistryLayoutError("list not found")

        monkeypatch.setattr(mod, "_run_nvd_sync", _boom)
        monkeypatch.setattr(sys, "argv", ["sync-cve-registry.py", "--source", "nvd"])
        with pytest.raises(SystemExit) as exc:
            mod.main()
        assert exc.value.code == 2

    def test_append_on_unlocatable_list_exits_nonzero(self, tmp_path, monkeypatch):
        mod = _sync()
        monkeypatch.setattr(mod, "REPO_ROOT", tmp_path)
        (tmp_path / "gateway" / "security").mkdir(parents=True)
        target = tmp_path / "gateway" / "security" / "agent_cve_registry.py"
        # _AGENT_CVE_REGISTRIES names a list that does not exist.
        target.write_text('_AGENT_CVE_REGISTRIES = {"openclaw": MISSING}\n')
        out = mod.process_ghsa_advisories([_adv()], [], "ASH-OCLAW")
        with pytest.raises(mod.RegistryLayoutError):
            mod.append_ghsa_entries(out, "openclaw", dry_run=False)

    def test_main_exits_nonzero_when_an_agent_fails(self, monkeypatch):
        mod = _sync()

        def _boom(*a, **k):
            raise mod.RegistryLayoutError("list not found")

        monkeypatch.setattr(mod, "sync_agent_ghsa", _boom)
        monkeypatch.setattr(
            "gateway.security.agent_cve_registry.list_cve_agents", lambda: ["openclaw"]
        )
        monkeypatch.setattr(sys, "argv", ["sync-cve-registry.py", "--source", "ghsa"])
        with pytest.raises(SystemExit) as exc:
            mod.main()
        assert exc.value.code == 2

    def test_feed_fetch_failure_is_not_reported_as_zero_new(self, monkeypatch):
        """An unreachable feed must fail the run, not print '0 new' and exit 0."""
        mod = _sync()

        def _timeout(*a, **k):
            raise mod.urllib.error.URLError("timed out")

        monkeypatch.setattr(mod, "fetch_ghsa_advisories", _timeout)
        monkeypatch.setattr(
            "gateway.security.agent_cve_registry.list_cve_agents", lambda: ["wazuh"]
        )
        monkeypatch.setattr(sys, "argv", ["sync-cve-registry.py", "--source", "ghsa"])
        with pytest.raises(SystemExit) as exc:
            mod.main()
        assert exc.value.code == 2


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

    @staticmethod
    def _json_resp(body):
        import io
        import json

        class _Resp(io.BytesIO):
            headers = {"Link": ""}

        return _Resp(json.dumps(body).encode("utf-8"))

    def test_token_refused_retries_public_endpoint_without_token(self):
        """aquasecurity/trivy 403s the Actions token but serves the public feed."""
        import urllib.error

        mod = _sync()
        sent_auth = []

        def _fake_urlopen(req, timeout=30):
            auth = req.get_header("Authorization")
            sent_auth.append(auth)
            if auth:
                raise urllib.error.HTTPError(req.full_url, 403, "Forbidden", {}, None)
            return self._json_resp([_adv(ghsa_id="GHSA-t1t1-t1t1-t1t1")])

        with patch.object(mod.urllib.request, "urlopen", _fake_urlopen):
            out = mod.fetch_ghsa_advisories("aquasecurity/trivy", github_token="tok")
        assert [a["ghsa_id"] for a in out] == ["GHSA-t1t1-t1t1-t1t1"]
        assert sent_auth == ["Bearer tok", None]

    def test_403_without_token_still_raises(self):
        import urllib.error

        mod = _sync()

        def _fake_urlopen(req, timeout=30):
            raise urllib.error.HTTPError(req.full_url, 403, "Forbidden", {}, None)

        with patch.object(mod.urllib.request, "urlopen", _fake_urlopen):
            with pytest.raises(urllib.error.HTTPError):
                mod.fetch_ghsa_advisories("aquasecurity/trivy")

    def test_other_http_errors_are_not_retried(self):
        import urllib.error

        mod = _sync()
        calls = []

        def _fake_urlopen(req, timeout=30):
            calls.append(req.get_header("Authorization"))
            raise urllib.error.HTTPError(req.full_url, 500, "Server Error", {}, None)

        with patch.object(mod.urllib.request, "urlopen", _fake_urlopen):
            with pytest.raises(urllib.error.HTTPError):
                mod.fetch_ghsa_advisories("aquasecurity/trivy", github_token="tok")
        assert calls == ["Bearer tok"]


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
