# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Authentication and rate limiting for AgentShroud Gateway

Implements Bearer token authentication with constant-time comparison
and simple token-bucket rate limiting.
"""
from __future__ import annotations


import hmac
import logging
import time
from collections import defaultdict
from typing import Callable

from fastapi import HTTPException, Request, status
from fastapi.security import HTTPBearer

from .config import GatewayConfig

logger = logging.getLogger("agentshroud.gateway.auth")

security = HTTPBearer()


class RateLimiter:
    """Simple token-bucket rate limiter

    Limits requests per client IP to prevent runaway automation.
    Since gateway binds to 127.0.0.1, this is primarily a safety net.
    """

    def __init__(self, max_requests: int = 100, window_seconds: int = 60):
        """
        Args:
            max_requests: Maximum requests allowed in the time window
            window_seconds: Time window in seconds
        """
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests: dict[str, list[float]] = defaultdict(list)

    def check(self, client_id: str) -> bool:
        """Check if client is within rate limit

        Args:
            client_id: Usually client IP address

        Returns:
            True if request allowed, False if rate limited
        """
        now = time.time()
        cutoff = now - self.window_seconds

        # Clean old requests
        self.requests[client_id] = [
            req_time for req_time in self.requests[client_id] if req_time > cutoff
        ]

        # Check limit
        if len(self.requests[client_id]) >= self.max_requests:
            return False

        # Record this request
        self.requests[client_id].append(now)
        return True


# Global rate limiter instance
rate_limiter = RateLimiter(max_requests=100, window_seconds=60)


def verify_token(token: str, expected_token: str) -> bool:
    """Verify token using constant-time comparison

    Uses hmac.compare_digest to prevent timing attacks.

    Args:
        token: Token from Authorization header
        expected_token: Expected token from configuration

    Returns:
        True if tokens match
    """
    return hmac.compare_digest(token, expected_token)


async def get_auth_dependency(config: GatewayConfig) -> Callable:
    """Factory that returns authentication dependency for FastAPI

    This allows us to inject the config into the auth dependency.

    Returns:
        Async function that validates Bearer tokens
    """

    async def auth_check(request: Request) -> None:
        """Verify Bearer token from Authorization header

        Raises:
            HTTPException 401: If token is missing or invalid
            HTTPException 403: If token format is wrong
            HTTPException 429: If rate limit exceeded
        """
        # Check rate limit first
        client_ip = request.client.host if request.client else "unknown"
        if not rate_limiter.check(client_ip):
            logger.warning(f"Rate limit exceeded for {client_ip}")
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Rate limit exceeded. Try again later.",
                headers={"Retry-After": "60"},
            )

        # Extract Authorization header
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authentication required",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Check Bearer scheme
        parts = auth_header.split()
        if len(parts) != 2 or parts[0].lower() != "bearer":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication scheme. Expected 'Bearer <token>'",
                headers={"WWW-Authenticate": "Bearer"},
            )

        token = parts[1]

        # Verify token (constant-time comparison)
        if not verify_token(token, config.auth_token):
            logger.warning(f"Invalid token attempt from {client_ip}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication token",
                headers={"WWW-Authenticate": "Bearer"},
            )

        # Auth success - continue
        logger.debug(f"Authenticated request from {client_ip}")

    return auth_check


def create_auth_dependency(config: GatewayConfig) -> Callable:
    """Create authentication dependency callable

    This is a synchronous wrapper that creates the async dependency.

    Args:
        config: Gateway configuration containing auth_token

    Returns:
        Callable suitable for FastAPI Depends()
    """

    async def dependency(request: Request) -> None:
        auth_func = await get_auth_dependency(config)
        await auth_func(request)

    return dependency
