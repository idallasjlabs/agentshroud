# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Differential PII Detector for Tool Results — Module 28 (v1.2.0)

IEC 62443 FR3 (System Integrity): adversarially formatted exfiltration in tool
RESULTS (web page responses, file reads, API replies) must be caught even when
the PII presentation departs from canonical formats.
IEC 62443 FR6 (Audit): every low-confidence hit is logged so operators can tune
thresholds and review potential leakage vectors.

Key design decision
-------------------
The production prompt-side PII floor is mandated at 0.9 by CLAUDE.md §7.8 ("PII
redaction — presidio engine at 0.9 confidence minimum; do not lower threshold").
That rule applies to PROMPTS where false positives would degrade user experience.

Tool results are a *different* trust surface: the content originates from external
systems (web pages, files, APIs) that an adversary can control. False positives on
a tool result are operationally acceptable (the agent sees [PII_REDACTED] instead
of a value), whereas false negatives allow exfil.

This module therefore applies a LOWER confidence floor (default 0.7) exclusively
to tool results, preserving the 0.9 floor for all prompt-side scanning.

Adversarial normalisation
--------------------------
Before running PII recognition, the detector strips common adversarial encodings
used to defeat naive regex / NER:
  * zero-width spaces / joiners (U+200B, U+200C, U+200D, U+FEFF)
  * Unicode lookalike substitutions (e.g. homoglyphs in email-like strings)
  * excess whitespace injection between characters of a PII token
Detection of these patterns is counted in ``adversarial_patterns_detected``.

Confidence floors
-----------------
  * ``tool_result_confidence_floor`` (default 0.7, min 0.5): applied when
    scanning tool results via ``scan_tool_result()``.
  * ``prompt_confidence_floor`` (default 0.9, fixed): applied when scanning
    prompts via ``scan_prompt()``.  Do NOT set this below 0.9.
  * ``per_tool_floor_overrides``: per-tool-name overrides for high-sensitivity
    tools (e.g. a medical data API might want 0.6).
"""

from __future__ import annotations

import logging
import re
import unicodedata
from dataclasses import dataclass, field
from enum import IntEnum
from typing import Any

logger = logging.getLogger("agentshroud.security.differential_pii_detector")

# ---------------------------------------------------------------------------
# Minimum allowed tool-result confidence floor (below this is dangerously
# permissive — too many false negatives)
# ---------------------------------------------------------------------------
_MINIMUM_TOOL_FLOOR = 0.5


# ---------------------------------------------------------------------------
# Severity mapping
# ---------------------------------------------------------------------------


class PIIHitSeverity(IntEnum):
    """Relative risk of a detected PII entity."""

    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4

    @classmethod
    def from_confidence(cls, confidence: float) -> "PIIHitSeverity":
        if confidence >= 0.95:
            return cls.CRITICAL
        if confidence >= 0.85:
            return cls.HIGH
        if confidence >= 0.70:
            return cls.MEDIUM
        return cls.LOW


# ---------------------------------------------------------------------------
# Result types
# ---------------------------------------------------------------------------


@dataclass
class PIIHit:
    """A single PII detection result."""

    entity_type: str
    confidence: float
    start: int
    end: int
    severity: PIIHitSeverity
    text: str = ""  # Redacted in logs; populated only for internal processing


@dataclass
class ToolResultPIIReport:
    """Full scan result for a tool result or prompt."""

    has_pii: bool
    hits: list[PIIHit]
    redacted_content: str
    confidence_floor_used: float
    adversarial_patterns_detected: int
    tool_name: str  # Empty string for prompt scans


# ---------------------------------------------------------------------------
# Adversarial pattern normalization
# ---------------------------------------------------------------------------

# Zero-width and invisible Unicode code points commonly used for injection
_ZERO_WIDTH_CHARS = re.compile(
    r"[​‌‍﻿­⁠᠎]",
    re.UNICODE,
)

# Unicode homoglyph lookalikes for the @ sign (used in email obfuscation)
_AT_LOOKALIKES = re.compile(r"[＠﹫@]", re.UNICODE)

# Unicode homoglyph lookalikes for dot (period)
_DOT_LOOKALIKES = re.compile(r"[．｡。·•‧∙⋅]", re.UNICODE)

# Excessive whitespace injection (spaces between every character in a token)
# Matches patterns like "a l i c e @ e x a m p l e" (2+ single chars separated by spaces)
_SPACED_TOKEN = re.compile(r"(?:\b\S\s){4,}\S\b")


def _normalize_adversarial(text: str) -> tuple[str, int]:
    """Strip common adversarial encoding tricks, return (normalized, count_removed)."""
    count = 0
    # 1. Zero-width characters
    stripped, n = re.subn(_ZERO_WIDTH_CHARS, "", text)
    count += n
    # 2. Unicode @ lookalikes → ASCII @
    stripped, n = re.subn(_AT_LOOKALIKES, "@", stripped)
    count += n
    # 3. Unicode dot lookalikes → ASCII .
    stripped, n = re.subn(_DOT_LOOKALIKES, ".", stripped)
    count += n
    # 4. NFC normalization resolves many homoglyph substitutions
    normalized = unicodedata.normalize("NFKC", stripped)
    if normalized != stripped:
        count += 1
    # 5. Collapse spaced tokens (e.g. "a l i c e" → "alice")
    def _collapse_spaced(m: re.Match) -> str:
        return m.group(0).replace(" ", "")
    collapsed, n = re.subn(_SPACED_TOKEN, _collapse_spaced, normalized)
    count += n
    return collapsed, count


# ---------------------------------------------------------------------------
# Regex-based PII patterns (confidence-annotated)
# These supplement Presidio when it is unavailable.
# ---------------------------------------------------------------------------

_PII_PATTERNS: list[dict[str, Any]] = [
    # RFC 5322-compliant email (high confidence)
    {
        "entity_type": "EMAIL_ADDRESS",
        "pattern": re.compile(
            r"\b[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}\b",
            re.IGNORECASE,
        ),
        "confidence": 0.95,
    },
    # US SSN  XXX-XX-XXXX
    {
        "entity_type": "US_SSN",
        "pattern": re.compile(r"\b(?!000|666|9\d{2})\d{3}-(?!00)\d{2}-(?!0{4})\d{4}\b"),
        "confidence": 0.92,
    },
    # US phone — (NXX) NXX-XXXX  or  NXX-NXX-XXXX  or  +1NXX...
    {
        "entity_type": "PHONE_NUMBER",
        "pattern": re.compile(
            r"(?:\+?1[-.\s]?)?"
            r"(?:\(?\d{3}\)?[-.\s]?)"
            r"\d{3}[-.\s]?\d{4}\b"
        ),
        "confidence": 0.80,
    },
    # Partial phone (NXX-XXXX) — lower confidence, only at tool-result floor
    {
        "entity_type": "PHONE_NUMBER",
        "pattern": re.compile(r"\b\d{3}[-.\s]\d{4}\b"),
        "confidence": 0.65,
    },
    # Credit card — 4-block format (very conservative)
    {
        "entity_type": "CREDIT_CARD",
        "pattern": re.compile(r"\b(?:4\d{3}|5[1-5]\d{2}|3[47]\d{2}|6011)\s?\d{4}\s?\d{4}\s?\d{4}\b"),
        "confidence": 0.90,
    },
]


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------


@dataclass
class DifferentialPIIConfig:
    """Configuration for DifferentialPIIDetector.

    Attributes:
        tool_result_confidence_floor: Minimum confidence for PII hits when
            scanning tool results.  Must be >= 0.5 and <= prompt_confidence_floor.
        prompt_confidence_floor: Minimum confidence for PII hits in prompts.
            MUST remain at 0.9 per CLAUDE.md §7.8.
        redact_on_hit: If True (default), PII tokens are replaced in the
            returned redacted_content.  If False, the original content is
            returned verbatim (hits are still reported).
        per_tool_floor_overrides: Dict mapping tool_name → confidence_floor
            for tools that handle especially sensitive data (e.g. 0.6).
    """

    tool_result_confidence_floor: float = 0.7
    prompt_confidence_floor: float = 0.9
    redact_on_hit: bool = True
    per_tool_floor_overrides: dict[str, float] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if self.tool_result_confidence_floor < _MINIMUM_TOOL_FLOOR:
            raise ValueError(
                f"confidence_floor {self.tool_result_confidence_floor} is below the minimum "
                f"allowed value of {_MINIMUM_TOOL_FLOOR}. "
                "Setting the floor too low produces excessive false positives."
            )
        if self.tool_result_confidence_floor > self.prompt_confidence_floor:
            raise ValueError(
                f"tool_result_confidence_floor ({self.tool_result_confidence_floor}) "
                f"must be <= prompt_confidence_floor ({self.prompt_confidence_floor}). "
                "The tool-result floor must never exceed the prompt floor."
            )


# ---------------------------------------------------------------------------
# Detector
# ---------------------------------------------------------------------------


class DifferentialPIIDetector:
    """Asymmetric PII detector: lower floor for tool results, 0.9 for prompts.

    This module is wired into the pipeline as an additional scan pass after
    the standard PIISanitizer. It runs on tool RESULTS specifically and
    catches adversarially-formatted PII that evades the standard pass.

    Integration point
    -----------------
    The pipeline's ``process_outbound`` calls this detector when a tool_name
    is present in the metadata, passing the (already-sanitized) tool result
    text.  Any new hits at the lower floor are redacted before the response
    is forwarded.
    """

    def __init__(self, config: DifferentialPIIConfig | None = None) -> None:
        self.config = config or DifferentialPIIConfig()
        self._presidio_analyzer = None
        self._presidio_anonymizer = None
        self._init_presidio()

    def _init_presidio(self) -> None:
        """Attempt to initialise Presidio; fall back to regex silently."""
        try:
            from presidio_analyzer import AnalyzerEngine
            from presidio_anonymizer import AnonymizerEngine

            self._presidio_analyzer = AnalyzerEngine()
            self._presidio_anonymizer = AnonymizerEngine()
            logger.debug("DifferentialPIIDetector: using Presidio engine")
        except Exception as exc:
            logger.debug(
                "DifferentialPIIDetector: Presidio unavailable (%s) — using regex fallback",
                exc,
            )

    # ------------------------------------------------------------------
    # Public interface
    # ------------------------------------------------------------------

    def scan_tool_result(
        self, tool_name: str, content: str
    ) -> ToolResultPIIReport:
        """Scan a tool result with the lower confidence floor.

        Args:
            tool_name: Name of the tool that produced this result.
            content:   Raw tool result text.

        Returns:
            ToolResultPIIReport with hits, redacted_content, and floor used.
        """
        floor = self.config.per_tool_floor_overrides.get(
            tool_name, self.config.tool_result_confidence_floor
        )
        return self._scan(content=content, floor=floor, tool_name=tool_name)

    def scan_prompt(self, content: str) -> ToolResultPIIReport:
        """Scan a prompt with the standard (higher) confidence floor.

        Args:
            content: Prompt text.

        Returns:
            ToolResultPIIReport with hits, redacted_content, and floor used.
        """
        return self._scan(
            content=content,
            floor=self.config.prompt_confidence_floor,
            tool_name="",
        )

    # ------------------------------------------------------------------
    # Internal scanning
    # ------------------------------------------------------------------

    def _scan(
        self, content: str, floor: float, tool_name: str
    ) -> ToolResultPIIReport:
        """Core scan: normalize adversarial patterns, then run PII recognition."""
        normalized, adversarial_count = _normalize_adversarial(content)
        if adversarial_count > 0:
            logger.warning(
                "DifferentialPIIDetector: %d adversarial pattern(s) normalized in tool=%r",
                adversarial_count,
                tool_name or "<prompt>",
            )

        hits = self._detect_pii(normalized, floor)

        redacted = self._redact(normalized, hits) if self.config.redact_on_hit else content

        if hits:
            logger.info(
                "DifferentialPIIDetector: %d PII hit(s) at floor=%.2f in tool=%r: %s",
                len(hits),
                floor,
                tool_name or "<prompt>",
                [h.entity_type for h in hits],
            )

        return ToolResultPIIReport(
            has_pii=bool(hits),
            hits=hits,
            redacted_content=redacted,
            confidence_floor_used=floor,
            adversarial_patterns_detected=adversarial_count,
            tool_name=tool_name,
        )

    def _detect_pii(self, text: str, floor: float) -> list[PIIHit]:
        """Run PII detection, returning hits at or above floor."""
        if self._presidio_analyzer is not None:
            return self._detect_presidio(text, floor)
        return self._detect_regex(text, floor)

    def _detect_presidio(self, text: str, floor: float) -> list[PIIHit]:
        """Use Presidio with the given confidence floor."""
        assert self._presidio_analyzer is not None
        try:
            results = self._presidio_analyzer.analyze(
                text=text,
                language="en",
                score_threshold=floor,
            )
            hits: list[PIIHit] = []
            for r in results:
                hits.append(
                    PIIHit(
                        entity_type=r.entity_type,
                        confidence=r.score,
                        start=r.start,
                        end=r.end,
                        severity=PIIHitSeverity.from_confidence(r.score),
                        text=text[r.start:r.end],
                    )
                )
            return hits
        except Exception as exc:
            logger.error("DifferentialPIIDetector Presidio error: %s — falling back to regex", exc)
            return self._detect_regex(text, floor)

    def _detect_regex(self, text: str, floor: float) -> list[PIIHit]:
        """Regex-based PII detection (Presidio fallback)."""
        hits: list[PIIHit] = []
        for pat_def in _PII_PATTERNS:
            if pat_def["confidence"] < floor:
                continue
            for m in pat_def["pattern"].finditer(text):
                hits.append(
                    PIIHit(
                        entity_type=pat_def["entity_type"],
                        confidence=pat_def["confidence"],
                        start=m.start(),
                        end=m.end(),
                        severity=PIIHitSeverity.from_confidence(pat_def["confidence"]),
                        text=m.group(0),
                    )
                )
        # Deduplicate overlapping hits (keep higher-confidence)
        return self._deduplicate(hits)

    @staticmethod
    def _deduplicate(hits: list[PIIHit]) -> list[PIIHit]:
        """Remove overlapping hits, preferring higher confidence."""
        if len(hits) <= 1:
            return hits
        hits_sorted = sorted(hits, key=lambda h: (-h.confidence, h.start))
        result: list[PIIHit] = []
        for hit in hits_sorted:
            # Check overlap with any already-accepted hit
            overlapping = any(
                not (hit.end <= kept.start or hit.start >= kept.end)
                for kept in result
            )
            if not overlapping:
                result.append(hit)
        return sorted(result, key=lambda h: h.start)

    def _redact(self, text: str, hits: list[PIIHit]) -> str:
        """Replace detected PII tokens with [ENTITY_TYPE] placeholders."""
        if not hits:
            return text
        # Sort hits by start position, process in reverse to preserve offsets
        sorted_hits = sorted(hits, key=lambda h: h.start, reverse=True)
        chars = list(text)
        for hit in sorted_hits:
            placeholder = f"[{hit.entity_type}]"
            chars[hit.start:hit.end] = list(placeholder)
        return "".join(chars)
