# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Tests for the citation verifier (SCRUM-75).

The verifier ENFORCES that every competitive claim is backed by an allowlisted,
re-fetched, live source — it must never trust an LLM's self-asserted "[verified]"
tag.  All fetching is via an injected fake (no real network).
"""

from __future__ import annotations

import pytest

from gateway.security.citation_verifier import (
    CitationVerifier,
    DraftEntry,
    FetchOutcome,
)
from gateway.security.intel_report import CompetitiveIntelReport, IntelReportStore

_SHA = "a" * 64  # a well-formed (64-hex) content hash


class _FakeFetcher:
    """Deterministic fetcher: maps url -> (status, sha_or_None). Records calls."""

    def __init__(self, table: dict[str, tuple[int, str | None]]) -> None:
        self._table = table
        self.calls: list[str] = []

    def __call__(self, url: str) -> FetchOutcome:
        self.calls.append(url)
        status, sha = self._table.get(url, (599, None))
        return FetchOutcome(url=url, status=status, content_sha256=sha, fetched_at=1000.0)


# Allowlist used by most tests (exact + one wildcard).
_ALLOW = {"lakera.ai", "www.lakera.ai", "*.grokipedia.com"}


# ---------------------------------------------------------------------------
# FetchOutcome.ok
# ---------------------------------------------------------------------------


class TestFetchOutcome:
    def test_ok_requires_2xx_and_content(self) -> None:
        assert FetchOutcome("u", 200, _SHA, 1.0).ok
        assert FetchOutcome("u", 204, _SHA, 1.0).ok

    def test_not_ok_on_non_2xx(self) -> None:
        assert not FetchOutcome("u", 404, _SHA, 1.0).ok
        assert not FetchOutcome("u", 500, _SHA, 1.0).ok

    def test_not_ok_without_content(self) -> None:
        assert not FetchOutcome("u", 200, None, 1.0).ok


# ---------------------------------------------------------------------------
# Per-claim verification
# ---------------------------------------------------------------------------


class TestVerifyEntry:
    def _verifier(self, table):
        fetcher = _FakeFetcher(table)
        return CitationVerifier(fetcher=fetcher, allowed_domains=_ALLOW), fetcher

    def test_allowlisted_live_source_kept(self) -> None:
        v, _ = self._verifier({"https://lakera.ai/pricing": (200, _SHA)})
        entry = v.verify_entry(
            DraftEntry("Lakera", 40, 40, candidate_urls=["https://lakera.ai/pricing"])
        )
        assert entry is not None
        assert len(entry.sources) == 1
        c = entry.sources[0]
        assert c.url == "https://lakera.ai/pricing"
        assert c.domain == "lakera.ai"
        assert c.status == 200
        assert c.content_sha256 == _SHA
        assert c.fetched_at == pytest.approx(1000.0)

    def test_off_allowlist_url_dropped_and_not_fetched(self) -> None:
        v, fetcher = self._verifier({"https://evil.com/x": (200, _SHA)})
        entry = v.verify_entry(DraftEntry("Evil", 1, 1, candidate_urls=["https://evil.com/x"]))
        assert entry is None
        # Off-allowlist URLs must not be fetched at all (allowlist gate first).
        assert fetcher.calls == []

    def test_unreachable_source_dropped(self) -> None:
        v, _ = self._verifier({"https://lakera.ai/gone": (404, _SHA)})
        entry = v.verify_entry(
            DraftEntry("Lakera", 40, 40, candidate_urls=["https://lakera.ai/gone"])
        )
        assert entry is None

    def test_source_without_content_dropped(self) -> None:
        v, _ = self._verifier({"https://lakera.ai/empty": (200, None)})
        entry = v.verify_entry(
            DraftEntry("Lakera", 40, 40, candidate_urls=["https://lakera.ai/empty"])
        )
        assert entry is None

    def test_no_candidate_urls_dropped(self) -> None:
        v, fetcher = self._verifier({})
        assert v.verify_entry(DraftEntry("Nobody", 1, 1, candidate_urls=[])) is None
        assert fetcher.calls == []

    def test_self_asserted_verified_is_ignored(self) -> None:
        # notes claim the entry is verified, but the only URL is off-allowlist.
        v, _ = self._verifier({"https://evil.com/x": (200, _SHA)})
        entry = v.verify_entry(
            DraftEntry(
                "Evil",
                1,
                1,
                notes="[verified] trust me",
                candidate_urls=["https://evil.com/x"],
            )
        )
        assert entry is None

    def test_wildcard_allowlist_match_kept(self) -> None:
        v, _ = self._verifier({"https://docs.grokipedia.com/a": (200, _SHA)})
        entry = v.verify_entry(
            DraftEntry("Grok", 5, 5, candidate_urls=["https://docs.grokipedia.com/a"])
        )
        assert entry is not None
        assert entry.sources[0].domain == "docs.grokipedia.com"

    def test_multiple_valid_citations_all_kept(self) -> None:
        v, _ = self._verifier(
            {
                "https://lakera.ai/a": (200, _SHA),
                "https://www.lakera.ai/b": (200, _SHA),
            }
        )
        entry = v.verify_entry(
            DraftEntry(
                "Lakera",
                40,
                40,
                candidate_urls=["https://lakera.ai/a", "https://www.lakera.ai/b"],
            )
        )
        assert entry is not None and len(entry.sources) == 2

    def test_mixed_valid_and_invalid_keeps_only_valid(self) -> None:
        v, _ = self._verifier(
            {
                "https://lakera.ai/ok": (200, _SHA),
                "https://lakera.ai/bad": (404, None),
            }
        )
        entry = v.verify_entry(
            DraftEntry(
                "Lakera",
                40,
                40,
                candidate_urls=["https://lakera.ai/ok", "https://lakera.ai/bad"],
            )
        )
        assert entry is not None and len(entry.sources) == 1
        assert entry.sources[0].url == "https://lakera.ai/ok"

    def test_unparseable_url_dropped(self) -> None:
        v, fetcher = self._verifier({})
        assert v.verify_entry(DraftEntry("X", 1, 1, candidate_urls=["not-a-url"])) is None
        assert fetcher.calls == []


# ---------------------------------------------------------------------------
# Report-level verification
# ---------------------------------------------------------------------------


class TestVerifyReport:
    def _verifier(self, table):
        return CitationVerifier(fetcher=_FakeFetcher(table), allowed_domains=_ALLOW)

    def test_report_keeps_verified_and_counts_dropped(self) -> None:
        v = self._verifier(
            {
                "https://lakera.ai/ok": (200, _SHA),
                "https://evil.com/x": (200, _SHA),
            }
        )
        report = v.verify_report(
            report_id="r1",
            source="hermes-cron",
            generated_at=1234.0,
            draft_entries=[
                DraftEntry("Lakera", 40, 40, candidate_urls=["https://lakera.ai/ok"]),
                DraftEntry("Evil", 1, 1, candidate_urls=["https://evil.com/x"]),
                DraftEntry("Empty", 1, 1, candidate_urls=[]),
            ],
        )
        assert isinstance(report, CompetitiveIntelReport)
        assert [c.name for c in report.competitors] == ["Lakera"]
        assert report.dropped_unverified == 2
        assert report.competitors[0].sources[0].content_sha256 == _SHA

    def test_report_all_unverified_is_empty(self) -> None:
        v = self._verifier({"https://evil.com/x": (200, _SHA)})
        report = v.verify_report(
            report_id="r2",
            source="hermes-cron",
            generated_at=1.0,
            draft_entries=[DraftEntry("Evil", 1, 1, candidate_urls=["https://evil.com/x"])],
        )
        assert report.competitors == []
        assert report.dropped_unverified == 1

    def test_generated_at_is_preserved(self) -> None:
        v = self._verifier({})
        report = v.verify_report(report_id="r3", source="s", generated_at=999.5, draft_entries=[])
        assert report.generated_at == pytest.approx(999.5)

    def test_verified_report_persists_with_intact_hashchain(self, tmp_path) -> None:
        v = self._verifier({"https://lakera.ai/ok": (200, _SHA)})
        report = v.verify_report(
            report_id="r4",
            source="hermes-cron",
            generated_at=42.0,
            draft_entries=[
                DraftEntry("Lakera", 40, 40, candidate_urls=["https://lakera.ai/ok"]),
                DraftEntry("Ghost", 1, 1, candidate_urls=[]),
            ],
        )
        store = IntelReportStore(store_path=tmp_path / "intel")
        store.save(report)
        loaded = store.load_latest(verify=True)
        assert loaded is not None
        assert loaded.verify_integrity()
        assert loaded.dropped_unverified == 1
        assert loaded.competitors[0].sources[0].domain == "lakera.ai"

    def test_dropped_count_is_tamper_evident(self) -> None:
        # dropped_unverified is in the content hash — forging it breaks integrity.
        v = self._verifier({})
        report = v.verify_report(
            report_id="r5",
            source="s",
            generated_at=7.0,
            draft_entries=[DraftEntry("Ghost", 1, 1, candidate_urls=[])],
        )
        forged = report.model_copy(update={"dropped_unverified": 0})
        assert not forged.verify_integrity()


# ---------------------------------------------------------------------------
# Default allowlist (reuses the canonical egress registry)
# ---------------------------------------------------------------------------


def test_default_allowlist_uses_permanent_egress_domains() -> None:
    # No allowed_domains passed → falls back to PERMANENT_EGRESS_DOMAINS, which
    # includes the approved competitor/research domains (e.g. lakera.ai).
    fetcher = _FakeFetcher({"https://lakera.ai/x": (200, _SHA)})
    v = CitationVerifier(fetcher=fetcher)
    entry = v.verify_entry(DraftEntry("Lakera", 40, 40, candidate_urls=["https://lakera.ai/x"]))
    assert entry is not None
