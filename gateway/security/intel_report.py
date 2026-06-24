# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Competitive Intelligence Report — Schema, Integrity, and Store (B.2)

IEC 62443 FR6 (Audit Log / Accountability): competitive intelligence reports
stored in the gateway-data volume carry hash-chain integrity so any tampering
is detectable before reports are consumed by downstream automation or the
/api/intel/competitive dashboard endpoint.

IEC 62443 FR3 (System Integrity): every report is validated against a Pydantic
schema at ingest; malformed reports raise ValidationError rather than silently
corrupting downstream processing.

Design
------
``CompetitiveIntelReport`` — immutable Pydantic model; ``content_hash`` is
derived from the serialized content fields at model construction time so it
cannot be forged without also recomputing the hash.

``IntelReportStore`` — persists reports as individual JSON files in a
configurable directory.  Tracks a simple hash chain: each report stores the
``previous_hash`` of the chronologically prior report (genesis hash = "0"*64).

``verify_integrity()`` — per-report SHA-256 re-computation.
``store.verify_chain()`` — full chain walk across all persisted reports.
"""

from __future__ import annotations

import hashlib
import json
import logging
import time
from pathlib import Path
from typing import Optional

from pydantic import BaseModel, Field, field_validator, model_validator

logger = logging.getLogger("agentshroud.security.intel_report")

_GENESIS_HASH = "0" * 64


# ---------------------------------------------------------------------------
# Exceptions
# ---------------------------------------------------------------------------


class ReportIntegrityError(Exception):
    """Raised when a loaded report fails its hash integrity check."""


# ---------------------------------------------------------------------------
# Schema
# ---------------------------------------------------------------------------


class CompetitorEntry(BaseModel):
    """A single competitor record in a competitive intel report."""

    name: str = Field(..., min_length=1, description="Competitor platform name")
    security_score: int = Field(..., ge=0, le=200, description="Modules implemented (0–200)")
    module_count: int = Field(..., ge=0, description="Total modules or features count")
    notes: str = Field(default="", description="Analyst notes")


class CompetitiveIntelReport(BaseModel):
    """Schema for a Hermes-generated competitive intelligence report.

    The ``content_hash`` field is computed at construction from the canonical
    content fields and stored immutably.  Calling ``verify_integrity()`` later
    recomputes the hash and compares — any post-construction mutation is detected.
    """

    model_config = {"frozen": True}

    report_id: str = Field(..., min_length=1, description="Unique report identifier")
    generated_at: float = Field(..., description="UNIX timestamp of report generation")
    source: str = Field(..., min_length=1, description="Report source (e.g. 'hermes-cron')")
    summary: str = Field(default="", description="Executive summary of the report")
    competitors: list[CompetitorEntry] = Field(
        default_factory=list, description="Competitor entries"
    )
    agentshroud_score: Optional[int] = Field(
        default=None, ge=0, description="AgentShroud module count at report time"
    )
    lead_delta: Optional[int] = Field(
        default=None, description="Modules ahead of closest competitor"
    )

    # --- Hash chain fields (set by model_validator) ---
    content_hash: str = Field(default="", description="SHA-256 of canonical content fields")
    previous_hash: str = Field(
        default=_GENESIS_HASH, description="SHA-256 of the previous report in the chain"
    )

    @field_validator("report_id")
    @classmethod
    def report_id_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("report_id must not be blank")
        return v

    @field_validator("source")
    @classmethod
    def source_not_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("source must not be blank")
        return v

    @model_validator(mode="after")
    def _compute_content_hash(self) -> "CompetitiveIntelReport":
        """Derive content_hash from the canonical content fields.

        Only computed when content_hash is empty (i.e. at initial construction,
        not when deserializing a stored report that already carries its hash).
        """
        if not self.content_hash:
            computed = _compute_hash(self)
            # Bypass frozen model to set the derived field
            object.__setattr__(self, "content_hash", computed)
        return self

    # ------------------------------------------------------------------
    # Integrity
    # ------------------------------------------------------------------

    def verify_integrity(self) -> bool:
        """Return True iff the stored content_hash matches recomputation."""
        return _compute_hash(self) == self.content_hash


def _compute_hash(report: CompetitiveIntelReport) -> str:
    """Compute SHA-256 over the canonical content fields of a report.

    Fields included: report_id, generated_at, source, summary,
    competitors (as sorted JSON), agentshroud_score, lead_delta.
    Fields excluded: content_hash, previous_hash (chain metadata).
    """
    competitors_payload = json.dumps(
        [c.model_dump() for c in report.competitors], sort_keys=True
    )
    payload = "|".join([
        report.report_id,
        f"{report.generated_at:.6f}",
        report.source,
        report.summary,
        competitors_payload,
        str(report.agentshroud_score),
        str(report.lead_delta),
    ])
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Store
# ---------------------------------------------------------------------------


class IntelReportStore:
    """Persistent store for competitive intelligence reports.

    Each report is saved as a JSON file named ``{timestamp_ns}_{report_id}.json``
    so chronological ordering is recoverable via filename sort.

    The store maintains a simple SHA-256 hash chain: each report records the
    ``previous_hash`` of its chronological predecessor.  The chain can be
    verified end-to-end via ``verify_chain()``.
    """

    def __init__(self, store_path: Path | str = Path("./gateway-data/intel-reports")) -> None:
        self.store_path = Path(store_path)

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def save(self, report: CompetitiveIntelReport) -> Path:
        """Persist *report* to the store, linking it to the previous report.

        Sets report.previous_hash to the content_hash of the current latest
        report before saving, maintaining the chain.
        """
        self.store_path.mkdir(parents=True, exist_ok=True)

        # Determine previous_hash for chain linking
        prev_hash = _GENESIS_HASH
        latest = self._load_latest_file()
        if latest is not None:
            try:
                stored = CompetitiveIntelReport.model_validate_json(latest.read_text())
                prev_hash = stored.content_hash
            except Exception as exc:
                logger.warning("IntelReportStore: could not read previous hash: %s", exc)

        # Rebuild report with updated previous_hash (unfreeze via model_copy)
        linked_report = report.model_copy(update={"previous_hash": prev_hash})

        # Use nanosecond timestamp for uniqueness in rapid succession
        ts_ns = time.time_ns()
        filename = f"{ts_ns:020d}_{report.report_id}.json"
        path = self.store_path / filename
        path.write_text(linked_report.model_dump_json(indent=2))
        logger.debug("IntelReportStore: saved report %s → %s", report.report_id, path.name)
        return path

    def load_latest(self, verify: bool = False) -> Optional[CompetitiveIntelReport]:
        """Load the most recently saved report.

        Args:
            verify: If True, raise ReportIntegrityError if integrity check fails.

        Returns:
            The latest CompetitiveIntelReport, or None if the store is empty.
        """
        latest = self._load_latest_file()
        if latest is None:
            return None
        report = CompetitiveIntelReport.model_validate_json(latest.read_text())
        if verify and not report.verify_integrity():
            raise ReportIntegrityError(
                f"Report {report.report_id} failed integrity check (content_hash mismatch). "
                "The file may have been tampered with."
            )
        return report

    def load_all(self) -> list[CompetitiveIntelReport]:
        """Load all reports in chronological order (oldest first)."""
        if not self.store_path.exists():
            return []
        files = sorted(self.store_path.glob("*.json"))
        reports = []
        for f in files:
            try:
                reports.append(CompetitiveIntelReport.model_validate_json(f.read_text()))
            except Exception as exc:
                logger.warning("IntelReportStore: skipping malformed file %s: %s", f.name, exc)
        return reports

    # ------------------------------------------------------------------
    # Chain verification
    # ------------------------------------------------------------------

    def verify_chain(self) -> tuple[bool, str]:
        """Walk the entire report chain and verify hash linkage.

        Returns:
            (True, "Chain valid (N reports)") or (False, "error description").
        """
        reports = self.load_all()
        if not reports:
            return True, "Empty store"

        # Verify each report's own integrity
        for i, report in enumerate(reports):
            if not report.verify_integrity():
                return (
                    False,
                    f"Report {i} ({report.report_id}): content_hash mismatch — tampered",
                )

        # Verify chain linkage
        expected_prev = _GENESIS_HASH
        for i, report in enumerate(reports):
            if report.previous_hash != expected_prev:
                return (
                    False,
                    f"Report {i} ({report.report_id}): previous_hash mismatch "
                    f"(expected {expected_prev[:16]}… got {report.previous_hash[:16]}…)",
                )
            expected_prev = report.content_hash

        return True, f"Chain valid ({len(reports)} reports)"

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _load_latest_file(self) -> Optional[Path]:
        """Return the most recent JSON file in the store, or None."""
        if not self.store_path.exists():
            return None
        files = sorted(self.store_path.glob("*.json"))
        return files[-1] if files else None
