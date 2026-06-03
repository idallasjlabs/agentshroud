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
