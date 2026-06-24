# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for B.2 — Competitive Intel Pipeline (schema validation + hash integrity).

IEC 62443 FR6 (Audit): competitive intelligence reports stored in the gateway-data
volume must carry hash-chain integrity so tampering is detectable.
IEC 62443 FR3 (System Integrity): report schema must be validated at ingest so
malformed reports do not silently produce garbage in downstream automation.

TDD — tests are written FIRST.  Implementation must satisfy these before merge.
"""

from __future__ import annotations

import hashlib
import json
import tempfile
import time
from pathlib import Path

import pytest
from pydantic import ValidationError

from gateway.security.intel_report import (
    CompetitorEntry,
    CompetitiveIntelReport,
    IntelReportStore,
    ReportIntegrityError,
)


# ---------------------------------------------------------------------------
# Schema validation
# ---------------------------------------------------------------------------


class TestCompetitiveIntelReportSchema:
    """Tests for Pydantic model validation."""

    def test_minimal_valid_report(self) -> None:
        report = CompetitiveIntelReport(
            report_id="rpt-001",
            generated_at=time.time(),
            source="hermes-cron",
            summary="Market analysis Q2 2026",
            competitors=[],
        )
        assert report.report_id == "rpt-001"
        assert report.source == "hermes-cron"

    def test_full_valid_report(self) -> None:
        report = CompetitiveIntelReport(
            report_id="rpt-002",
            generated_at=time.time(),
            source="hermes-cron",
            summary="Full analysis",
            competitors=[
                CompetitorEntry(
                    name="Zetherion",
                    security_score=4,
                    module_count=4,
                    notes="Partial egress filtering only",
                ),
                CompetitorEntry(
                    name="CogniShield",
                    security_score=3,
                    module_count=3,
                    notes="No audit chain",
                ),
            ],
            agentshroud_score=28,
            lead_delta=24,
        )
        assert len(report.competitors) == 2
        assert report.agentshroud_score == 28

    def test_missing_required_fields_raises(self) -> None:
        with pytest.raises(ValidationError):
            CompetitiveIntelReport(
                # report_id missing
                generated_at=time.time(),
                source="hermes-cron",
                summary="incomplete",
                competitors=[],
            )

    def test_negative_security_score_rejected(self) -> None:
        with pytest.raises(ValidationError):
            CompetitorEntry(
                name="BadBot",
                security_score=-1,
                module_count=0,
                notes="invalid",
            )

    def test_security_score_above_max_rejected(self) -> None:
        with pytest.raises(ValidationError):
            CompetitorEntry(
                name="BadBot",
                security_score=1000,
                module_count=0,
                notes="invalid",
            )

    def test_empty_report_id_rejected(self) -> None:
        with pytest.raises(ValidationError):
            CompetitiveIntelReport(
                report_id="",
                generated_at=time.time(),
                source="hermes-cron",
                summary="test",
                competitors=[],
            )

    def test_empty_source_rejected(self) -> None:
        with pytest.raises(ValidationError):
            CompetitiveIntelReport(
                report_id="rpt-x",
                generated_at=time.time(),
                source="",
                summary="test",
                competitors=[],
            )

    def test_report_serialises_to_json(self) -> None:
        report = CompetitiveIntelReport(
            report_id="rpt-003",
            generated_at=1000000.0,
            source="hermes-cron",
            summary="serialization test",
            competitors=[],
        )
        payload = report.model_dump_json()
        parsed = json.loads(payload)
        assert parsed["report_id"] == "rpt-003"

    def test_report_roundtrips_via_json(self) -> None:
        report = CompetitiveIntelReport(
            report_id="rpt-004",
            generated_at=1000001.0,
            source="hermes-cron",
            summary="roundtrip test",
            competitors=[
                CompetitorEntry(
                    name="Zetherion",
                    security_score=4,
                    module_count=4,
                    notes="partial",
                )
            ],
        )
        payload = report.model_dump_json()
        reloaded = CompetitiveIntelReport.model_validate_json(payload)
        assert reloaded.report_id == report.report_id
        assert len(reloaded.competitors) == 1


# ---------------------------------------------------------------------------
# Hash chain integrity
# ---------------------------------------------------------------------------


class TestIntelReportHashIntegrity:
    def test_report_has_content_hash(self) -> None:
        report = CompetitiveIntelReport(
            report_id="rpt-h1",
            generated_at=time.time(),
            source="hermes-cron",
            summary="hash test",
            competitors=[],
        )
        assert len(report.content_hash) == 64  # SHA-256 hex

    def test_content_hash_is_deterministic(self) -> None:
        kwargs = dict(
            report_id="rpt-h2",
            generated_at=1234567890.0,
            source="hermes-cron",
            summary="determinism test",
            competitors=[],
        )
        r1 = CompetitiveIntelReport(**kwargs)
        r2 = CompetitiveIntelReport(**kwargs)
        assert r1.content_hash == r2.content_hash

    def test_different_content_different_hash(self) -> None:
        base = dict(
            generated_at=1234567890.0,
            source="hermes-cron",
            competitors=[],
        )
        r1 = CompetitiveIntelReport(report_id="rpt-ha", summary="version A", **base)
        r2 = CompetitiveIntelReport(report_id="rpt-hb", summary="version B", **base)
        assert r1.content_hash != r2.content_hash

    def test_verify_integrity_passes_for_valid_report(self) -> None:
        report = CompetitiveIntelReport(
            report_id="rpt-v1",
            generated_at=time.time(),
            source="hermes-cron",
            summary="verify test",
            competitors=[],
        )
        assert report.verify_integrity()

    def test_verify_integrity_fails_after_tampering(self) -> None:
        report = CompetitiveIntelReport(
            report_id="rpt-v2",
            generated_at=time.time(),
            source="hermes-cron",
            summary="tamper test",
            competitors=[],
        )
        # Tamper with the summary after construction
        object.__setattr__(report, "summary", "TAMPERED SUMMARY")
        assert not report.verify_integrity()


# ---------------------------------------------------------------------------
# IntelReportStore — persistence + hash chain
# ---------------------------------------------------------------------------


class TestIntelReportStore:
    @pytest.fixture()
    def store_dir(self, tmp_path: Path) -> Path:
        return tmp_path / "intel-reports"

    @pytest.fixture()
    def store(self, store_dir: Path) -> IntelReportStore:
        return IntelReportStore(store_path=store_dir)

    def _make_report(self, report_id: str = "rpt-s1") -> CompetitiveIntelReport:
        return CompetitiveIntelReport(
            report_id=report_id,
            generated_at=time.time(),
            source="hermes-cron",
            summary="store test",
            competitors=[],
        )

    def test_store_creates_directory(self, store: IntelReportStore, store_dir: Path) -> None:
        store.save(self._make_report())
        assert store_dir.exists()

    def test_save_and_load_latest(self, store: IntelReportStore) -> None:
        report = self._make_report("rpt-latest")
        store.save(report)
        loaded = store.load_latest()
        assert loaded is not None
        assert loaded.report_id == "rpt-latest"

    def test_load_latest_returns_none_when_empty(
        self, store: IntelReportStore
    ) -> None:
        assert store.load_latest() is None

    def test_multiple_saves_latest_is_newest(self, store: IntelReportStore) -> None:
        store.save(self._make_report("rpt-old"))
        time.sleep(0.01)
        store.save(self._make_report("rpt-new"))
        latest = store.load_latest()
        assert latest is not None
        assert latest.report_id == "rpt-new"

    def test_integrity_check_passes_for_saved_report(
        self, store: IntelReportStore
    ) -> None:
        report = self._make_report("rpt-int")
        store.save(report)
        loaded = store.load_latest()
        assert loaded is not None
        assert loaded.verify_integrity()

    def test_integrity_check_fails_for_tampered_file(
        self, store: IntelReportStore, store_dir: Path
    ) -> None:
        report = self._make_report("rpt-tamper")
        store.save(report)

        # Tamper with the stored file on disk
        files = list(store_dir.glob("*.json"))
        assert len(files) == 1
        data = json.loads(files[0].read_text())
        data["summary"] = "TAMPERED"
        files[0].write_text(json.dumps(data))

        with pytest.raises(ReportIntegrityError):
            store.load_latest(verify=True)

    def test_load_all_returns_all_reports(self, store: IntelReportStore) -> None:
        for i in range(3):
            time.sleep(0.01)
            store.save(self._make_report(f"rpt-multi-{i}"))
        reports = store.load_all()
        assert len(reports) == 3

    def test_chain_hash_links_reports(self, store: IntelReportStore) -> None:
        r1 = self._make_report("rpt-chain-1")
        time.sleep(0.01)
        r2 = self._make_report("rpt-chain-2")

        store.save(r1)
        store.save(r2)

        all_reports = store.load_all()
        assert len(all_reports) == 2

        # The chain hash on the second report must reference the first
        first = all_reports[0]  # oldest
        second = all_reports[1]  # newest
        expected_prev_hash = first.content_hash
        assert second.previous_hash == expected_prev_hash

    def test_verify_chain_passes_for_intact_store(
        self, store: IntelReportStore
    ) -> None:
        for i in range(3):
            time.sleep(0.01)
            store.save(self._make_report(f"rpt-cv-{i}"))
        valid, msg = store.verify_chain()
        assert valid, msg

    def test_verify_chain_fails_for_tampered_entry(
        self, store: IntelReportStore, store_dir: Path
    ) -> None:
        for i in range(3):
            time.sleep(0.01)
            store.save(self._make_report(f"rpt-ct-{i}"))

        # Tamper with the middle file
        files = sorted(store_dir.glob("*.json"))
        assert len(files) == 3
        data = json.loads(files[1].read_text())
        data["summary"] = "INJECTED"
        files[1].write_text(json.dumps(data))

        valid, msg = store.verify_chain()
        assert not valid

    def test_load_all_skips_malformed_files(
        self, store: IntelReportStore, store_dir: Path
    ) -> None:
        store.save(self._make_report("rpt-good"))
        # Write a malformed JSON file alongside the valid one
        (store_dir / "00000000000000000000_bad.json").write_text("{not valid json")
        reports = store.load_all()
        # The malformed file is skipped — only the valid report returned
        assert len(reports) == 1
        assert reports[0].report_id == "rpt-good"

    def test_verify_chain_empty_store_is_valid(
        self, store: IntelReportStore
    ) -> None:
        valid, msg = store.verify_chain()
        assert valid
        assert "Empty" in msg

    def test_report_with_whitespace_only_id_rejected(self) -> None:
        with pytest.raises(ValidationError):
            CompetitiveIntelReport(
                report_id="   ",
                generated_at=time.time(),
                source="hermes-cron",
                summary="test",
                competitors=[],
            )

    def test_report_with_whitespace_only_source_rejected(self) -> None:
        with pytest.raises(ValidationError):
            CompetitiveIntelReport(
                report_id="rpt-ws",
                generated_at=time.time(),
                source="   ",
                summary="test",
                competitors=[],
            )

    def test_save_with_corrupt_previous_file_falls_back_to_genesis(
        self, store: IntelReportStore, store_dir: Path
    ) -> None:
        """If the previous report file is corrupt, save must not raise."""
        store_dir.mkdir(parents=True, exist_ok=True)
        (store_dir / "00000000000000000000_broken.json").write_text("{bad json")
        # Save should succeed, falling back to genesis hash for prev
        path = store.save(self._make_report("rpt-fallback"))
        assert path.exists()
