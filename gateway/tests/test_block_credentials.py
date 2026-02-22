# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for block_credentials method in PIISanitizer.

TDD approach: Tests written first for credential blocking behavior.
"""

import pytest
from gateway.ingest_api.sanitizer import PIISanitizer
from gateway.ingest_api.config import PIIConfig


@pytest.fixture
def sanitizer():
    config = PIIConfig(engine="regex", entities=["US_SSN", "EMAIL_ADDRESS"], enabled=True)
    return PIISanitizer(config)


# === Trusted sources should NOT block ===

@pytest.mark.asyncio
async def test_console_source_not_blocked(sanitizer):
    """Console is a trusted source — credentials should pass through."""
    content = 'password: MyS3cretP@ss!'
    result, blocked = await sanitizer.block_credentials(content, source="console")
    assert blocked is False
    assert result == content


@pytest.mark.asyncio
async def test_localhost_source_not_blocked(sanitizer):
    """Localhost is a trusted source."""
    content = 'password: MyS3cretP@ss!'
    result, blocked = await sanitizer.block_credentials(content, source="localhost")
    assert blocked is False


@pytest.mark.asyncio
async def test_control_ui_source_not_blocked(sanitizer):
    """Control UI is a trusted source."""
    content = 'token: abcdefghijklmnopqrstuvwxyz1234'
    result, blocked = await sanitizer.block_credentials(content, source="control_ui")
    assert blocked is False


@pytest.mark.asyncio
async def test_api_source_not_blocked(sanitizer):
    """API is a trusted source."""
    content = 'secret: verylongsecretstring12345678'
    result, blocked = await sanitizer.block_credentials(content, source="api")
    assert blocked is False


# === Untrusted sources SHOULD block ===

@pytest.mark.asyncio
async def test_telegram_blocks_password(sanitizer):
    """Telegram should block password display."""
    content = 'password: MyS3cretP@ss!Word'
    result, blocked = await sanitizer.block_credentials(content, source="telegram")
    assert blocked is True
    assert "REDACTED" in result


@pytest.mark.asyncio
async def test_telegram_blocks_openai_api_key(sanitizer):
    """Telegram should block OpenAI API keys."""
    content = 'Your key is sk-abcdefghijklmnopqrstuvwxyz1234567890'
    result, blocked = await sanitizer.block_credentials(content, source="telegram")
    assert blocked is True


@pytest.mark.asyncio
async def test_telegram_blocks_github_token(sanitizer):
    """Telegram should block GitHub tokens."""
    content = 'Token: ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh'
    result, blocked = await sanitizer.block_credentials(content, source="telegram")
    assert blocked is True


@pytest.mark.asyncio
async def test_telegram_blocks_aws_key(sanitizer):
    """Telegram should block AWS access keys."""
    content = 'Access key: AKIAIOSFODNN7EXAMPLE'
    result, blocked = await sanitizer.block_credentials(content, source="telegram")
    assert blocked is True


@pytest.mark.asyncio
async def test_telegram_blocks_ssh_private_key(sanitizer):
    """Telegram should block SSH private keys."""
    content = '-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEA...'
    result, blocked = await sanitizer.block_credentials(content, source="telegram")
    assert blocked is True


@pytest.mark.asyncio
async def test_telegram_blocks_json_password(sanitizer):
    """Telegram should block JSON-formatted passwords (from op item get)."""
    content = '"value": "Ea7WnN77Ahs4zGA2ZUTN"'
    result, blocked = await sanitizer.block_credentials(content, source="telegram")
    assert blocked is True


@pytest.mark.asyncio
async def test_external_api_blocks_credentials(sanitizer):
    """External API source should also block."""
    content = 'password: SuperSecret123!'
    result, blocked = await sanitizer.block_credentials(content, source="external_api")
    assert blocked is True


# === False positive avoidance ===

@pytest.mark.asyncio
async def test_normal_text_not_blocked(sanitizer):
    """Normal text should not be blocked on any source."""
    content = "The weather is nice today. Meeting at 3pm."
    result, blocked = await sanitizer.block_credentials(content, source="telegram")
    assert blocked is False
    assert result == content


@pytest.mark.asyncio
async def test_six_digit_number_not_blocked(sanitizer):
    """Regular 6-digit numbers (zip codes, IDs) should NOT be blocked."""
    content = "Your order 123456 has shipped to zip code 90210."
    result, blocked = await sanitizer.block_credentials(content, source="telegram")
    assert blocked is False


@pytest.mark.asyncio
async def test_normal_technical_content_not_blocked(sanitizer):
    """Technical content without actual credentials should pass."""
    content = "The server returned status code 200. Port 8080 is open."
    result, blocked = await sanitizer.block_credentials(content, source="telegram")
    assert blocked is False


@pytest.mark.asyncio
async def test_short_password_field_not_blocked(sanitizer):
    """Short values after 'password:' should not trigger (< 8 chars)."""
    content = "password: short"
    result, blocked = await sanitizer.block_credentials(content, source="telegram")
    assert blocked is False


# === Blocking message format ===

@pytest.mark.asyncio
async def test_blocked_message_contains_guidance(sanitizer):
    """Blocked responses should contain helpful guidance."""
    content = 'password: SuperSecretPassword123!'
    result, blocked = await sanitizer.block_credentials(content, source="telegram")
    assert blocked is True
    assert "REDACTED" in result
    assert "Console" in result or "console" in result
    assert "Control UI" in result or "localhost" in result
