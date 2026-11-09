# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for PII sanitizer"""

from __future__ import annotations

import pytest


@pytest.mark.asyncio
async def test_ssn_detection(sanitizer):
    """Test SSN redaction"""
    content = "My SSN is 123-45-6789"
    result = await sanitizer.sanitize(content)

    assert result.sanitized_content == "My SSN is <US_SSN>"
    assert "US_SSN" in result.entity_types_found
    assert len(result.redactions) == 1
    assert result.redactions[0].entity_type == "US_SSN"


@pytest.mark.asyncio
async def test_email_detection(sanitizer):
    """Test email address redaction"""
    content = "Contact me at test@example.com for details"
    result = await sanitizer.sanitize(content)

    assert "<EMAIL_ADDRESS>" in result.sanitized_content
    assert "EMAIL_ADDRESS" in result.entity_types_found


@pytest.mark.asyncio
async def test_phone_detection(sanitizer):
    """Test phone number redaction"""
    content = "Call me at (555) 123-4567"
    result = await sanitizer.sanitize(content)

    assert "<PHONE_NUMBER>" in result.sanitized_content
    assert "PHONE_NUMBER" in result.entity_types_found


@pytest.mark.asyncio
async def test_credit_card_detection(sanitizer):
    """Test credit card redaction"""
    content = "My card is 4111-1111-1111-1111"
    result = await sanitizer.sanitize(content)

    assert "<CREDIT_CARD>" in result.sanitized_content
    assert "CREDIT_CARD" in result.entity_types_found


@pytest.mark.asyncio
async def test_no_pii(sanitizer):
    """Test content with no PII"""
    content = "The weather is nice today"
    result = await sanitizer.sanitize(content)

    assert result.sanitized_content == content
    assert len(result.redactions) == 0
    assert len(result.entity_types_found) == 0


@pytest.mark.asyncio
async def test_mixed_pii(sanitizer):
    """Test content with multiple PII types"""
    content = "My SSN is 123-45-6789 and email is test@example.com"
    result = await sanitizer.sanitize(content)

    assert "<US_SSN>" in result.sanitized_content
    assert "<EMAIL_ADDRESS>" in result.sanitized_content
    assert "US_SSN" in result.entity_types_found
    assert "EMAIL_ADDRESS" in result.entity_types_found
    assert len(result.redactions) == 2


@pytest.mark.asyncio
async def test_empty_content(sanitizer):
    """Test empty content handling"""
    content = ""
    result = await sanitizer.sanitize(content)

    assert result.sanitized_content == ""
    assert len(result.redactions) == 0


# ── Telegram UID / phone regression (Bug A) ───────────────────────────────────


@pytest.mark.asyncio
async def test_telegram_uid_not_redacted_as_phone(sanitizer):
    """Bare 10-digit Telegram UID must pass through unchanged — no <PHONE_NUMBER>."""
    result = await sanitizer.sanitize("UID 8506022825 sent a message")
    assert "<PHONE_NUMBER>" not in result.sanitized_content
    assert "8506022825" in result.sanitized_content


@pytest.mark.asyncio
async def test_real_phone_still_redacted(sanitizer):
    """Phone number with separator must still be redacted."""
    result = await sanitizer.sanitize("Call me at (415) 555-1234")
    assert "<PHONE_NUMBER>" in result.sanitized_content
    assert "415" not in result.sanitized_content.replace("<PHONE_NUMBER>", "")


@pytest.mark.asyncio
async def test_uid_inside_parens_preserved(sanitizer):
    """UID in parens — as written in contributor logs — must not be redacted."""
    result = await sanitizer.sanitize("Brett Galura (8506022825) — 45 msgs")
    assert "<PHONE_NUMBER>" not in result.sanitized_content
    assert "8506022825" in result.sanitized_content


@pytest.mark.asyncio
async def test_regex_fallback_requires_separator(sanitizer):
    """Regex-only path must not match bare 10-digit digit string as phone number."""
    # Exercise _sanitize_regex directly by temporarily forcing regex mode.
    import asyncio

    original_mode = sanitizer.mode
    sanitizer.mode = "regex"
    try:
        result = await asyncio.wait_for(sanitizer._sanitize_regex("8506022825"), timeout=5)
    finally:
        sanitizer.mode = original_mode
    assert "<PHONE_NUMBER>" not in result.sanitized_content
    assert "8506022825" in result.sanitized_content


# === SCRUM-202: enforcement_action=block, monitor mode, per-call raise-only threshold ===

SSN_TEXT = "My SSN is 123-45-6789"


def _regex_sanitizer(mode: str = "enforce", action: str = "redact"):
    from gateway.ingest_api.config import PIIConfig
    from gateway.ingest_api.sanitizer import PIISanitizer

    return PIISanitizer(PIIConfig(engine="regex"), mode=mode, action=action)


class _FakeRecognizerResult:
    def __init__(self, entity_type: str, start: int, end: int, score: float):
        self.entity_type = entity_type
        self.start = start
        self.end = end
        self.score = score


class _FakeAnalyzer:
    """Returns a single PERSON hit at a fixed score (0.92, just above the floor)."""

    def __init__(self, score: float = 0.92):
        self.score = score

    def analyze(self, text, entities, language):
        idx = text.find("Alice")
        if idx < 0:
            return []
        return [_FakeRecognizerResult("PERSON", idx, idx + 5, self.score)]


class _FakeAnonymizer:
    def anonymize(self, text, analyzer_results, operators):
        out = text
        for r in sorted(analyzer_results, key=lambda r: r.start, reverse=True):
            out = out[: r.start] + f"<{r.entity_type}>" + out[r.end :]
        return type("Anon", (), {"text": out})()


def _presidio_sanitizer(score: float = 0.92):
    from gateway.ingest_api.config import PIIConfig
    from gateway.ingest_api.sanitizer import PIISanitizer

    s = PIISanitizer(PIIConfig(engine="regex", entities=["PERSON", "US_SSN"]))
    s.mode = "presidio"
    s.analyzer = _FakeAnalyzer(score)
    s.anonymizer = _FakeAnonymizer()
    return s


@pytest.mark.asyncio
async def test_block_action_blocks_and_withholds_pii():
    s = _regex_sanitizer(action="block")
    result = await s.sanitize(SSN_TEXT)
    assert result.blocked is True
    assert "123-45-6789" not in result.sanitized_content
    assert result.entity_types_found == ["US_SSN"]
    assert len(result.redactions) == 1


@pytest.mark.asyncio
async def test_block_action_clean_content_passes_unchanged():
    s = _regex_sanitizer(action="block")
    result = await s.sanitize("The weather is nice today")
    assert result.blocked is False
    assert result.sanitized_content == "The weather is nice today"


@pytest.mark.asyncio
async def test_redact_action_unchanged_and_not_blocked():
    s = _regex_sanitizer(action="redact")
    result = await s.sanitize(SSN_TEXT)
    assert result.blocked is False
    assert result.sanitized_content == "My SSN is <US_SSN>"


@pytest.mark.asyncio
async def test_per_call_action_override():
    redactor = _regex_sanitizer(action="redact")
    blocked = await redactor.sanitize(SSN_TEXT, action="block")
    assert blocked.blocked is True
    assert "123-45-6789" not in blocked.sanitized_content

    blocker = _regex_sanitizer(action="block")
    redacted = await blocker.sanitize(SSN_TEXT, action="redact")
    assert redacted.blocked is False
    assert redacted.sanitized_content == "My SSN is <US_SSN>"


@pytest.mark.asyncio
async def test_per_call_invalid_action_rejected():
    s = _regex_sanitizer()
    with pytest.raises(ValueError):
        await s.sanitize(SSN_TEXT, action="allow")


@pytest.mark.asyncio
@pytest.mark.parametrize("action", ["redact", "block"])
async def test_monitor_mode_reports_but_never_mutates(action):
    s = _regex_sanitizer(mode="monitor", action=action)
    result = await s.sanitize(SSN_TEXT)
    assert result.sanitized_content == SSN_TEXT
    assert result.blocked is False
    assert result.entity_types_found == ["US_SSN"]
    assert len(result.redactions) == 1


@pytest.mark.asyncio
async def test_disabled_config_not_blocked():
    from gateway.ingest_api.config import PIIConfig
    from gateway.ingest_api.sanitizer import PIISanitizer

    s = PIISanitizer(PIIConfig(engine="regex", enabled=False), action="block")
    result = await s.sanitize(SSN_TEXT)
    assert result.blocked is False
    assert result.sanitized_content == SSN_TEXT


@pytest.mark.asyncio
@pytest.mark.parametrize("value", [0.0, 0.5, 0.89, 0.8999])
async def test_min_confidence_cannot_be_lowered_below_floor(value):
    s = _regex_sanitizer()
    with pytest.raises(ValueError):
        await s.sanitize(SSN_TEXT, min_confidence=value)


@pytest.mark.asyncio
async def test_min_confidence_above_one_rejected():
    s = _regex_sanitizer()
    with pytest.raises(ValueError):
        await s.sanitize(SSN_TEXT, min_confidence=1.5)


@pytest.mark.asyncio
async def test_min_confidence_at_floor_is_identical_to_default():
    s = _presidio_sanitizer(score=0.92)
    default = await s.sanitize("Hi Alice")
    explicit = await s.sanitize("Hi Alice", min_confidence=0.9)
    assert default.sanitized_content == "Hi <PERSON>"
    assert explicit.sanitized_content == default.sanitized_content


@pytest.mark.asyncio
async def test_min_confidence_can_be_raised():
    s = _presidio_sanitizer(score=0.92)
    raised = await s.sanitize("Hi Alice", min_confidence=0.95)
    assert raised.sanitized_content == "Hi Alice"
    assert raised.entity_types_found == []
    # Raising never weakens the regex pass (regex hits score 1.0).
    raised_ssn = await s.sanitize(SSN_TEXT, min_confidence=0.99)
    assert raised_ssn.sanitized_content == "My SSN is <US_SSN>"


@pytest.mark.asyncio
async def test_raised_threshold_with_block_only_blocks_above_threshold():
    s = _presidio_sanitizer(score=0.92)
    low = await s.sanitize("Hi Alice", action="block", min_confidence=0.95)
    assert low.blocked is False
    hit = await s.sanitize("Hi Alice", action="block")
    assert hit.blocked is True
    assert "Alice" not in hit.sanitized_content
