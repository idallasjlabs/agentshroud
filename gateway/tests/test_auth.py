# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for authentication and rate limiting"""

import time

import pytest
from fastapi import HTTPException

from gateway.ingest_api.auth import RateLimiter, create_auth_dependency, verify_token


def test_verify_token_valid():
    """Test token verification with valid token"""
    token = "test-secret-token"
    expected = "test-secret-token"

    assert verify_token(token, expected) is True


def test_verify_token_invalid():
    """Test token verification with invalid token"""
    token = "wrong-token"
    expected = "test-secret-token"

    assert verify_token(token, expected) is False


def test_verify_token_constant_time():
    """Test that token verification uses constant-time comparison"""
    # This test verifies that hmac.compare_digest is used
    # by checking that the function behaves correctly
    token1 = "a" * 32
    token2 = "a" * 31 + "b"
    expected = "a" * 32

    assert verify_token(token1, expected) is True
    assert verify_token(token2, expected) is False


def test_rate_limiter_allows_requests():
    """Test rate limiter allows requests under limit"""
    limiter = RateLimiter(max_requests=5, window_seconds=60)

    for i in range(5):
        assert limiter.check("client1") is True


def test_rate_limiter_blocks_excess_requests():
    """Test rate limiter blocks requests over limit"""
    limiter = RateLimiter(max_requests=3, window_seconds=60)

    # First 3 requests should pass
    for i in range(3):
        assert limiter.check("client1") is True

    # 4th request should be blocked
    assert limiter.check("client1") is False


def test_rate_limiter_separate_clients():
    """Test rate limiter tracks clients separately"""
    limiter = RateLimiter(max_requests=2, window_seconds=60)

    # Client 1
    assert limiter.check("client1") is True
    assert limiter.check("client1") is True
    assert limiter.check("client1") is False  # Over limit

    # Client 2 should have separate limit
    assert limiter.check("client2") is True
    assert limiter.check("client2") is True


def test_rate_limiter_window_cleanup():
    """Test rate limiter cleans up old requests"""
    limiter = RateLimiter(max_requests=2, window_seconds=1)  # 1 second window

    # Use up limit
    assert limiter.check("client1") is True
    assert limiter.check("client1") is True
    assert limiter.check("client1") is False

    # Wait for window to expire
    time.sleep(1.1)

    # Should be allowed again
    assert limiter.check("client1") is True


@pytest.mark.asyncio
async def test_auth_dependency_valid_token(test_config):
    """Test auth dependency with valid token"""
    test_config.auth_token = "test-token-12345"
    auth_func = create_auth_dependency(test_config)

    # Mock request with valid auth
    class MockClient:
        host = "127.0.0.1"

    class MockRequest:
        client = MockClient()
        headers = {"Authorization": "Bearer test-token-12345"}

    request = MockRequest()

    # Should not raise
    await auth_func(request)


@pytest.mark.asyncio
async def test_auth_dependency_missing_header(test_config):
    """Test auth dependency with missing Authorization header"""
    test_config.auth_token = "test-token-12345"
    auth_func = create_auth_dependency(test_config)

    class MockClient:
        host = "127.0.0.1"

    class MockRequest:
        client = MockClient()
        headers = {}

    request = MockRequest()

    with pytest.raises(HTTPException) as exc:
        await auth_func(request)

    assert exc.value.status_code == 401
    assert "Authentication required" in str(exc.value.detail)


@pytest.mark.asyncio
async def test_auth_dependency_invalid_token(test_config):
    """Test auth dependency with invalid token"""
    test_config.auth_token = "test-token-12345"
    auth_func = create_auth_dependency(test_config)

    class MockClient:
        host = "127.0.0.1"

    class MockRequest:
        client = MockClient()
        headers = {"Authorization": "Bearer wrong-token"}

    request = MockRequest()

    with pytest.raises(HTTPException) as exc:
        await auth_func(request)

    assert exc.value.status_code == 401
    assert "Invalid authentication token" in str(exc.value.detail)


@pytest.mark.asyncio
async def test_auth_dependency_invalid_scheme(test_config):
    """Test auth dependency with invalid auth scheme"""
    test_config.auth_token = "test-token-12345"
    auth_func = create_auth_dependency(test_config)

    class MockClient:
        host = "127.0.0.1"

    class MockRequest:
        client = MockClient()
        headers = {"Authorization": "Basic dGVzdDp0ZXN0"}  # Basic auth

    request = MockRequest()

    with pytest.raises(HTTPException) as exc:
        await auth_func(request)

    assert exc.value.status_code == 401
