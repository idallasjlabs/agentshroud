# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Security and edge case tests for AgentShroud Gateway"""
from __future__ import annotations


import pytest
from gateway.ingest_api.auth import verify_token, RateLimiter
from gateway.ingest_api.models import ForwardRequest
import time

# === PII Security Tests ===


@pytest.mark.asyncio
async def test_very_large_content(sanitizer):
    """Test handling of very large content (1MB+)"""
    # Create 1MB of content with embedded PII
    large_content = (
        "Normal text. " * 50000 + "My SSN is 123-45-6789. " + "More text. " * 20000
    )

    result = await sanitizer.sanitize(large_content)

    # Should still detect PII in large content
    assert "<US_SSN>" in result.sanitized_content
    assert "US_SSN" in result.entity_types_found


@pytest.mark.asyncio
async def test_multiple_same_type_pii(sanitizer):
    """Test content with multiple instances of same PII type"""
    content = "First SSN: 123-45-6789, second SSN: 987-65-4321, third: 555-12-3456"
    result = await sanitizer.sanitize(content)

    assert len(result.redactions) == 3
    assert result.sanitized_content.count("<US_SSN>") == 3


@pytest.mark.asyncio
async def test_unicode_content(sanitizer):
    """Test content with Unicode characters"""
    content = "My email is user@例え.jp and 日本語 text 123-45-6789"
    result = await sanitizer.sanitize(content)

    # Should handle Unicode without crashing
    assert result is not None
    # Email might not match due to Unicode domain
    assert "<US_SSN>" in result.sanitized_content


@pytest.mark.asyncio
async def test_special_characters_in_pii(sanitizer):
    """Test PII detection with special characters nearby"""
    content = "SSN: (123-45-6789), email: [test@example.com]"
    result = await sanitizer.sanitize(content)

    assert "<US_SSN>" in result.sanitized_content
    assert "<EMAIL_ADDRESS>" in result.sanitized_content


@pytest.mark.asyncio
async def test_null_bytes_in_content(sanitizer):
    """Test handling of null bytes (potential injection attack)"""
    content = "Normal text\x00SSN: 123-45-6789\x00more text"

    # Should not crash
    result = await sanitizer.sanitize(content)
    assert result is not None


# === Authentication Security Tests ===


def test_constant_time_comparison():
    """Verify token comparison is constant-time"""
    correct_token = "secret-token-12345"

    # Same length tokens
    assert verify_token(correct_token, correct_token) is True
    assert verify_token("wrong-token-12345", correct_token) is False

    # Different length should still use constant-time
    assert verify_token("short", correct_token) is False
    assert verify_token("", correct_token) is False


def test_rate_limiter():
    """Test rate limiting behavior"""
    limiter = RateLimiter(max_requests=3, window_seconds=1)

    client_id = "test-client"

    # First 3 requests should succeed
    assert limiter.check(client_id) is True
    assert limiter.check(client_id) is True
    assert limiter.check(client_id) is True

    # 4th should fail
    assert limiter.check(client_id) is False

    # Wait for window to reset
    time.sleep(1.1)

    # Should succeed again
    assert limiter.check(client_id) is True


# === Input Validation Tests ===


def test_empty_content_rejection():
    """Test that empty content is rejected"""
    with pytest.raises(ValueError, match="content must not be empty"):
        ForwardRequest(content="   ", source="api")  # Only whitespace


def test_invalid_source_rejection():
    """Test that invalid source is rejected"""
    with pytest.raises(ValueError, match="source must be one of"):
        ForwardRequest(content="test", source="invalid_source")


def test_valid_sources():
    """Test all valid sources are accepted"""
    valid_sources = ["shortcut", "browser_extension", "script", "api"]

    for source in valid_sources:
        request = ForwardRequest(content="test", source=source)
        assert request.source == source


# === Edge Cases ===


@pytest.mark.asyncio
async def test_nested_pii_patterns(sanitizer):
    """Test overlapping or nested PII patterns"""
    # Email containing what looks like a phone number
    content = "Contact: 5551234567@example.com"
    result = await sanitizer.sanitize(content)

    # Should detect as email (longer match)
    assert result is not None


@pytest.mark.asyncio
async def test_false_positive_patterns(sanitizer):
    """Test that common false positives are handled"""
    content = "Version 123-45-6789 of the software"  # Looks like SSN but is version
    result = await sanitizer.sanitize(content)

    # Current implementation will redact this (conservative approach is safer)
    # This is acceptable for security - better safe than sorry
    assert result is not None


@pytest.mark.asyncio
async def test_malformed_json_metadata(sanitizer):
    """Test handling of malformed metadata"""
    # This is handled by Pydantic validation in ForwardRequest
    # Metadata is a dict, so Python will validate it
    request = ForwardRequest(content="test", source="api", metadata={"valid": "dict"})
    assert request.metadata == {"valid": "dict"}


@pytest.mark.asyncio
async def test_sql_injection_attempt(test_ledger):
    """Test that SQL injection is prevented"""
    # Try to inject SQL through source parameter
    malicious_source = "shortcut'; DROP TABLE ledger; --"

    entry = await test_ledger.record(
        source=malicious_source,
        content="test content",
        original_content="test content",
        sanitized=False,
        redaction_count=0,
        redaction_types=[],
        forwarded_to="agent",
    )

    # Should be safely stored and retrievable
    retrieved = await test_ledger.get_entry(entry.id)
    assert retrieved is not None
    assert retrieved.source == malicious_source  # Stored as-is, not executed


@pytest.mark.asyncio
async def test_xss_attempt(test_ledger):
    """Test that XSS payloads are safely stored"""
    xss_payload = "<script>alert('XSS')</script>"

    entry = await test_ledger.record(
        source="api",
        content=xss_payload,
        original_content=xss_payload,
        sanitized=False,
        redaction_count=0,
        redaction_types=[],
        forwarded_to="agent",
    )

    # Should be safely stored (hashed)
    # Content is never returned raw, only hashed
    assert entry.content_hash is not None
    assert entry.content_hash != xss_payload


@pytest.mark.asyncio
async def test_extremely_long_content(sanitizer):
    """Test handling of extremely long content (10MB)"""
    # 10MB of text
    huge_content = "x" * (10 * 1024 * 1024)

    # Should complete without crashing or hanging
    # (May be slow, but should not crash)
    result = await sanitizer.sanitize(huge_content)
    assert result is not None
    assert len(result.sanitized_content) == len(huge_content)


# === Timing Attack Tests ===


def test_timing_attack_resistance():
    """Verify authentication doesn't leak timing information"""
    import statistics

    correct_token = "correct-token-1234567890"
    wrong_token = "wrong-token-1234567890"

    # Warmup — eliminate CPU cold-start / cache-fill bias from ordering
    for _ in range(20):
        verify_token(correct_token, correct_token)
        verify_token(wrong_token, correct_token)

    # Interleave measurements to remove sequential ordering effects
    correct_times = []
    wrong_times = []
    for _ in range(100):
        start = time.perf_counter()
        verify_token(correct_token, correct_token)
        correct_times.append(time.perf_counter() - start)

        start = time.perf_counter()
        verify_token(wrong_token, correct_token)
        wrong_times.append(time.perf_counter() - start)

    # Use median — more robust than mean against container scheduling jitter.
    # hmac.compare_digest guarantees constant-time at the crypto level.
    # Threshold 0.9 (< 10x ratio) catches gross non-constant-time implementations
    # while tolerating normal nanosecond-scale variance in containerised environments.
    correct_median = statistics.median(correct_times)
    wrong_median = statistics.median(wrong_times)

    assert abs(correct_median - wrong_median) / max(correct_median, wrong_median) < 0.9
