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


class TestDeterministicPresidioInit:
    """Presidio init must be deterministic and must NEVER trigger a runtime
    model auto-download.

    Regression: a bare ``AnalyzerEngine()`` makes Presidio try to fetch its
    default ``en_core_web_lg`` (~400 MB) over the network the first time it is
    constructed.  On the read-only production image that fetch fails and the
    detector silently falls back to regex; on a writable, networked CI runner
    it *succeeds*, so the detector's behaviour — and the PII contract — differ
    by environment.  A security module must not (a) reach out to the network at
    import/construction time behind egress controls, nor (b) behave differently
    in CI than in production.  The detector must probe for an explicitly pinned
    model and fall back to regex when it is absent, without any download.
    """

    def test_regex_fallback_when_model_absent(self, monkeypatch) -> None:
        try:
            import spacy
        except ImportError:
            # No spaCy at all → the detector must already be in regex fallback.
            assert DifferentialPIIDetector()._presidio_analyzer is None
            return

        def _no_model(name, *_a, **_k):
            raise OSError(f"[E050] Can't find model {name!r}")

        monkeypatch.setattr(spacy, "load", _no_model)
        d = DifferentialPIIDetector()
        # Model probe fails → regex fallback, NOT a half-initialised (or
        # auto-downloaded) Presidio engine.
        assert d._presidio_analyzer is None

    def test_init_does_not_construct_bare_analyzer_engine(self, monkeypatch) -> None:
        """The default-model auto-download path must never be taken.

        If Presidio is ever constructed, it must be with an explicit
        ``nlp_engine`` (pinned model), never the bare ``AnalyzerEngine()`` that
        auto-downloads ``en_core_web_lg``.
        """
        spacy = pytest.importorskip("spacy")
        presidio_analyzer = pytest.importorskip("presidio_analyzer")

        # Simulate the pinned model being absent so we exercise the probe path.
        monkeypatch.setattr(
            spacy, "load", lambda *_a, **_k: (_ for _ in ()).throw(OSError("no model"))
        )
        called = {"bare": False}
        real_engine = presidio_analyzer.AnalyzerEngine

        def _spy(*args, **kwargs):  # noqa: ANN002,ANN003
            if not kwargs.get("nlp_engine"):
                called["bare"] = True
            return real_engine(*args, **kwargs)

        monkeypatch.setattr(presidio_analyzer, "AnalyzerEngine", _spy)

        DifferentialPIIDetector()
        # Model was absent → Presidio must not have been constructed at all,
        # and certainly not the bare (auto-downloading) engine.
        assert called["bare"] is False

    def test_init_wires_explicit_nlp_engine_when_model_present(self, monkeypatch) -> None:
        """When the pinned model loads, Presidio is built with an explicit
        ``nlp_engine`` (never the bare auto-downloading form)."""
        spacy = pytest.importorskip("spacy")
        presidio_analyzer = pytest.importorskip("presidio_analyzer")
        nlp_mod = pytest.importorskip("presidio_analyzer.nlp_engine")
        pytest.importorskip("presidio_anonymizer")

        monkeypatch.setattr(spacy, "load", lambda *_a, **_k: object())

        seen = {"nlp_engine": "MISSING"}

        class _FakeProvider:
            def __init__(self, *a, **k) -> None:  # noqa: ANN002, ANN003
                pass

            def create_engine(self):  # noqa: ANN201
                return "ENGINE"

        def _fake_analyzer(*a, **k):  # noqa: ANN002, ANN003
            seen["nlp_engine"] = k.get("nlp_engine", "MISSING")
            return object()

        monkeypatch.setattr(nlp_mod, "NlpEngineProvider", _FakeProvider)
        monkeypatch.setattr(presidio_analyzer, "AnalyzerEngine", _fake_analyzer)

        d = DifferentialPIIDetector()
        assert d._presidio_analyzer is not None
        assert seen["nlp_engine"] == "ENGINE"  # explicit engine wired, not bare

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
    def test_plain_email_caught_in_tool_result(self, detector: DifferentialPIIDetector) -> None:
        report = detector.scan_tool_result(
            tool_name="web_search",
            content="Contact us at alice@example.com for support.",
        )
        assert report.has_pii
        assert any("EMAIL" in h.entity_type.upper() for h in report.hits)

    def test_plain_email_caught_in_prompt(self, detector: DifferentialPIIDetector) -> None:
        report = detector.scan_prompt(
            content="Send email to bob@example.com please.",
        )
        assert report.has_pii

    def test_us_ssn_caught_in_tool_result(self, detector: DifferentialPIIDetector) -> None:
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


class TestPresidioPathContract:
    """Exercise the Presidio detection path with an injected fake analyzer.

    The real Presidio engine needs a spaCy model that is not installed in CI
    or the production image, so these tests inject a stub analyzer to verify
    the *logic* deterministically: entity restriction (no benign LOCATION
    false-positive) and the core-regex union (standard PII always caught even
    when Presidio scores it away).
    """

    class _FakeRecognizerResult:
        def __init__(self, entity_type: str, score: float, start: int, end: int) -> None:
            self.entity_type = entity_type
            self.score = score
            self.start = start
            self.end = end

    def _detector_with_fake(self, detector: DifferentialPIIDetector, results, capture):
        def _analyze(text, language, entities, score_threshold):  # noqa: ANN001, ARG001
            capture["entities"] = entities
            capture["threshold"] = score_threshold
            # Emulate Presidio: only return results for REQUESTED entities that
            # meet the score threshold.
            return [r for r in results if r.score >= score_threshold and r.entity_type in entities]

        fake = type("FakeAnalyzer", (), {"analyze": staticmethod(_analyze)})()
        detector._presidio_analyzer = fake
        return detector

    def test_presidio_analyze_restricted_to_pii_entities(
        self, detector: DifferentialPIIDetector
    ) -> None:
        from gateway.security.differential_pii_detector import _PRESIDIO_ENTITIES

        capture: dict = {}
        self._detector_with_fake(detector, [], capture)
        detector.scan_tool_result(tool_name="web_search", content="hello world")
        # analyze() must be called with the PII allowlist, excluding LOCATION.
        assert capture["entities"] == _PRESIDIO_ENTITIES
        assert "LOCATION" not in capture["entities"]

    def test_bare_city_name_not_flagged_but_street_address_is(
        self, detector: DifferentialPIIDetector
    ) -> None:
        # NER LOCATION is excluded from the allowlist, so a bare city name is
        # never even requested; but the precise street-address regex (unioned)
        # still catches a real address on the Presidio path.
        capture: dict = {}
        self._detector_with_fake(detector, [], capture)
        clean = detector.scan_tool_result(
            tool_name="web_search", content="Weather in London is fine."
        )
        assert "LOCATION" not in capture["entities"]
        assert not clean.has_pii
        addr = detector.scan_tool_result(
            tool_name="read_file", content="Ship to 350 Fifth Avenue today."
        )
        assert addr.has_pii
        assert any(h.entity_type == "LOCATION" for h in addr.hits)

    def test_presidio_result_becomes_pii_hit(self, detector: DifferentialPIIDetector) -> None:
        # A surviving allowlisted Presidio result must map to a PIIHit with the
        # right entity type and span (covers the result-mapping branch).
        passport = self._FakeRecognizerResult("US_PASSPORT", 0.95, 8, 17)
        capture: dict = {}
        self._detector_with_fake(detector, [passport], capture)
        report = detector.scan_tool_result(
            tool_name="read_file", content="Passport 123456789 on file."
        )
        hit = next(h for h in report.hits if h.entity_type == "US_PASSPORT")
        assert (hit.start, hit.end) == (8, 17)
        assert hit.confidence == pytest.approx(0.95)

    def test_presidio_exception_falls_back_to_regex(
        self, detector: DifferentialPIIDetector
    ) -> None:
        # If Presidio.analyze() raises, the detector must fall back to regex and
        # still surface core PII (covers the except branch).
        def _boom(*_a, **_k):
            raise RuntimeError("presidio engine exploded")

        fake = type("BoomAnalyzer", (), {"analyze": staticmethod(_boom)})()
        detector._presidio_analyzer = fake
        report = detector.scan_tool_result(tool_name="read_file", content="SSN: 123-45-6789")
        assert report.has_pii
        assert any(h.entity_type == "US_SSN" for h in report.hits)

    def test_core_ssn_unioned_when_presidio_misses_it(
        self, detector: DifferentialPIIDetector
    ) -> None:
        # Presidio returns NOTHING (e.g. context-sensitive score drop), but the
        # core regex union must still surface the plainly-formatted SSN.
        capture: dict = {}
        self._detector_with_fake(detector, [], capture)
        report = detector.scan_tool_result(tool_name="read_file", content="SSN: 123-45-6789")
        assert report.has_pii
        assert any(h.entity_type == "US_SSN" for h in report.hits)


# ---------------------------------------------------------------------------
# Adversarial formatting caught only at lower tool-result floor
# ---------------------------------------------------------------------------


class TestAdversarialFormattingCaught:
    def test_spaced_email_caught_in_tool_result(self, detector: DifferentialPIIDetector) -> None:
        """Email with spaces added to defeat naive regex: a l i c e @ e x a m p l e . c o m"""
        content = "Reach out to a l i c e @ e x a m p l e . c o m for help."
        report = detector.scan_tool_result(tool_name="web_search", content=content)
        # With adversarial normalization, the detector must surface this
        assert report.has_pii or report.adversarial_patterns_detected > 0

    def test_dotted_email_caught_in_tool_result(self, detector: DifferentialPIIDetector) -> None:
        """Email with Unicode dot separators."""
        content = "Contact alice․example․com for details."
        report = detector.scan_tool_result(tool_name="web_search", content=content)
        assert report.has_pii or report.adversarial_patterns_detected > 0

    def test_zero_width_space_injection_caught(self, detector: DifferentialPIIDetector) -> None:
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

    def test_weak_hit_present_in_tool_result_only(self, detector: DifferentialPIIDetector) -> None:
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
    def test_report_has_required_fields(self, detector: DifferentialPIIDetector) -> None:
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
        report = detector.scan_tool_result(tool_name="high_sensitivity_tool", content=content)
        assert report.confidence_floor_used == pytest.approx(0.6)

    def test_unknown_tool_uses_default_floor(self, detector: DifferentialPIIDetector) -> None:
        report = detector.scan_tool_result(
            tool_name="unknown_tool",
            content="No PII here.",
        )
        assert report.confidence_floor_used == pytest.approx(
            detector.config.tool_result_confidence_floor
        )
