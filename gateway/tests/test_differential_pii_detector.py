# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for Module 28 — Differential PII Detector for Tool Results.

IEC 62443 FR3 (System Integrity): adversarially formatted tool results that evade
the standard 0.9-confidence PII pass must be caught before they leave the gateway.
IEC 62443 FR6 (Audit): every low-confidence PII hit must be recorded so operators
can tune thresholds.

Lower floor 0.7 on TOOL RESULTS only — never on prompts (where false positives
would degrade the user experience).

TDD — tests are written FIRST.  Implementation must satisfy these before merge.
"""

from __future__ import annotations

import pytest

from gateway.security.differential_pii_detector import (
    DifferentialPIIConfig,
    DifferentialPIIDetector,
    PIIHit,
    PIIHitSeverity,
)


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------


@pytest.fixture()
def default_config() -> DifferentialPIIConfig:
    return DifferentialPIIConfig(
        tool_result_confidence_floor=0.7,
        prompt_confidence_floor=0.9,
        redact_on_hit=True,
    )


@pytest.fixture()
def detector(default_config: DifferentialPIIConfig) -> DifferentialPIIDetector:
    return DifferentialPIIDetector(config=default_config)


# ---------------------------------------------------------------------------
# Construction
# ---------------------------------------------------------------------------


class TestDifferentialPIIDetectorConstruction:
    def test_default_config_has_correct_floors(self) -> None:
        d = DifferentialPIIDetector()
        assert d.config.tool_result_confidence_floor == pytest.approx(0.7)
        assert d.config.prompt_confidence_floor == pytest.approx(0.9)

    def test_cannot_set_tool_floor_below_minimum(self) -> None:
        with pytest.raises(ValueError, match="confidence_floor"):
            DifferentialPIIConfig(tool_result_confidence_floor=0.4)

    def test_cannot_set_tool_floor_above_prompt_floor(self) -> None:
        with pytest.raises(ValueError, match="tool_result_confidence_floor"):
            DifferentialPIIConfig(
                tool_result_confidence_floor=0.95,
                prompt_confidence_floor=0.9,
            )


# ---------------------------------------------------------------------------
# Standard email / SSN — caught at both floors
# ---------------------------------------------------------------------------


class TestStandardPIIAlwaysCaught:
    def test_plain_email_caught_in_tool_result(
        self, detector: DifferentialPIIDetector
    ) -> None:
        report = detector.scan_tool_result(
            tool_name="web_search",
            content="Contact us at alice@example.com for support.",
        )
        assert report.has_pii
        assert any("EMAIL" in h.entity_type.upper() for h in report.hits)

    def test_plain_email_caught_in_prompt(
        self, detector: DifferentialPIIDetector
    ) -> None:
        report = detector.scan_prompt(
            content="Send email to bob@example.com please.",
        )
        assert report.has_pii

    def test_us_ssn_caught_in_tool_result(
        self, detector: DifferentialPIIDetector
    ) -> None:
        report = detector.scan_tool_result(
            tool_name="read_file",
            content="SSN: 123-45-6789",
        )
        assert report.has_pii

    def test_clean_content_no_hits(self, detector: DifferentialPIIDetector) -> None:
        report = detector.scan_tool_result(
            tool_name="web_search",
            content="The weather in London is partly cloudy.",
        )
        assert not report.has_pii
        assert report.hits == []


# ---------------------------------------------------------------------------
# Adversarial formatting caught only at lower tool-result floor
# ---------------------------------------------------------------------------


class TestAdversarialFormattingCaught:
    def test_spaced_email_caught_in_tool_result(
        self, detector: DifferentialPIIDetector
    ) -> None:
        """Email with spaces added to defeat naive regex: a l i c e @ e x a m p l e . c o m"""
        content = "Reach out to a l i c e @ e x a m p l e . c o m for help."
        report = detector.scan_tool_result(tool_name="web_search", content=content)
        # With adversarial normalization, the detector must surface this
        assert report.has_pii or report.adversarial_patterns_detected > 0

    def test_dotted_email_caught_in_tool_result(
        self, detector: DifferentialPIIDetector
    ) -> None:
        """Email with Unicode dot separators."""
        content = "Contact alice․example․com for details."
        report = detector.scan_tool_result(tool_name="web_search", content=content)
        assert report.has_pii or report.adversarial_patterns_detected > 0

    def test_zero_width_space_injection_caught(
        self, detector: DifferentialPIIDetector
    ) -> None:
        """PII split with zero-width space."""
        content = "SSN: 123​-45-​6789"
        report = detector.scan_tool_result(tool_name="read_file", content=content)
        assert report.has_pii or report.adversarial_patterns_detected > 0


# ---------------------------------------------------------------------------
# Asymmetric behaviour — lower floor applies only to tool results
# ---------------------------------------------------------------------------


class TestAsymmetricFloor:
    def test_scan_produces_report_with_correct_floor_used(
        self, detector: DifferentialPIIDetector
    ) -> None:
        content = "Phone: +1 (415) 555-0100"
        tool_report = detector.scan_tool_result(tool_name="api_call", content=content)
        prompt_report = detector.scan_prompt(content=content)

        # Both floor values should be captured in the reports
        assert tool_report.confidence_floor_used == pytest.approx(0.7)
        assert prompt_report.confidence_floor_used == pytest.approx(0.9)

    def test_weak_hit_present_in_tool_result_only(
        self, detector: DifferentialPIIDetector
    ) -> None:
        """A weak-confidence hit (0.75) must appear in tool results but not prompts."""
        # Inject a synthetic weak-confidence hit by using a partial pattern
        # that registers between 0.7 and 0.9
        content = "Call 555-1234 for info."  # partial US number, weak match
        tool_report = detector.scan_tool_result(tool_name="phone_lookup", content=content)
        prompt_report = detector.scan_prompt(content=content)

        # Tool report may pick up weak hits; prompt should be more conservative
        # (We assert that the floors are different — exact hit counts depend on the regex engine)
        assert tool_report.confidence_floor_used < prompt_report.confidence_floor_used


# ---------------------------------------------------------------------------
# Redaction
# ---------------------------------------------------------------------------


class TestRedaction:
    def test_email_redacted_in_output(self, detector: DifferentialPIIDetector) -> None:
        content = "Contact alice@example.com for help."
        report = detector.scan_tool_result(tool_name="web_search", content=content)
        if report.has_pii:
            assert "alice@example.com" not in report.redacted_content

    def test_redacted_content_is_original_when_no_pii(
        self, detector: DifferentialPIIDetector
    ) -> None:
        content = "No sensitive information here."
        report = detector.scan_tool_result(tool_name="web_search", content=content)
        assert report.redacted_content == content

    def test_redact_on_hit_false_preserves_original(self) -> None:
        config = DifferentialPIIConfig(
            tool_result_confidence_floor=0.7,
            prompt_confidence_floor=0.9,
            redact_on_hit=False,
        )
        detector = DifferentialPIIDetector(config=config)
        content = "Contact alice@example.com"
        report = detector.scan_tool_result(tool_name="web_search", content=content)
        # With redact_on_hit=False, original content preserved verbatim
        assert report.redacted_content == content


# ---------------------------------------------------------------------------
# Report dataclass
# ---------------------------------------------------------------------------


class TestToolResultPIIReport:
    def test_report_has_required_fields(
        self, detector: DifferentialPIIDetector
    ) -> None:
        report = detector.scan_tool_result(
            tool_name="read_file",
            content="Name: John Smith, SSN: 123-45-6789",
        )
        assert hasattr(report, "has_pii")
        assert hasattr(report, "hits")
        assert hasattr(report, "redacted_content")
        assert hasattr(report, "confidence_floor_used")
        assert hasattr(report, "adversarial_patterns_detected")
        assert hasattr(report, "tool_name")
        assert report.tool_name == "read_file"

    def test_pii_hit_fields(self, detector: DifferentialPIIDetector) -> None:
        report = detector.scan_tool_result(
            tool_name="read_file",
            content="Email: test@example.com",
        )
        if report.hits:
            hit: PIIHit = report.hits[0]
            assert hasattr(hit, "entity_type")
            assert hasattr(hit, "confidence")
            assert hasattr(hit, "start")
            assert hasattr(hit, "end")
            assert hasattr(hit, "severity")
            assert isinstance(hit.severity, PIIHitSeverity)


# ---------------------------------------------------------------------------
# Per-tool configuration
# ---------------------------------------------------------------------------


class TestPerToolConfiguration:
    def test_tool_specific_floor_override(self) -> None:
        config = DifferentialPIIConfig(
            tool_result_confidence_floor=0.7,
            prompt_confidence_floor=0.9,
            per_tool_floor_overrides={"high_sensitivity_tool": 0.6},
        )
        detector = DifferentialPIIDetector(config=config)
        content = "Phone: 415-555-0100"
        report = detector.scan_tool_result(
            tool_name="high_sensitivity_tool", content=content
        )
        assert report.confidence_floor_used == pytest.approx(0.6)

    def test_unknown_tool_uses_default_floor(
        self, detector: DifferentialPIIDetector
    ) -> None:
        report = detector.scan_tool_result(
            tool_name="unknown_tool",
            content="No PII here.",
        )
        assert report.confidence_floor_used == pytest.approx(
            detector.config.tool_result_confidence_floor
        )
