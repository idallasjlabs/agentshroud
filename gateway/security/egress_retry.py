# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""
Resilient Egress Retry — exponential backoff wrapper for transient egress failures.

DuckDuckGo (and other search backends) intermittently timeout or rate-limit
requests through the egress proxy. This module provides a configurable retry
mechanism with exponential backoff and jitter that wraps any outbound HTTP
request through the proxy.

Usage in the proxy pipeline:
    from gateway.security.egress_retry import RetryConfig, retry_request

    result = await retry_request(
        make_request,   # async callable that makes the HTTP request
        config=RetryConfig(max_attempts=3, base_delay=1.0),
    )
"""

import asyncio
import logging
import random
import time
from dataclasses import dataclass, field
from typing import Any, Callable, Optional, TypeVar

logger = logging.getLogger("agentshroud.security.egress_retry")

T = TypeVar("T")


@dataclass
class RetryConfig:
    """Configuration for egress retry behavior."""
    max_attempts: int = 3                # Total attempts (1 = no retry)
    base_delay: float = 1.0             # Base delay in seconds
    max_delay: float = 30.0             # Maximum delay between retries
    backoff_factor: float = 2.0         # Exponential backoff multiplier
    jitter: float = 0.5                 # Random jitter range (0-1)
    retryable_status_codes: set[int] = field(
        default_factory=lambda: {408, 429, 500, 502, 503, 504}
    )
    retryable_exceptions: tuple = field(
        default_factory=lambda: (
            asyncio.TimeoutError,
            ConnectionError,
            OSError,
        )
    )


@dataclass
class RetryResult:
    """Result of a retried operation."""
    success: bool
    value: Any = None
    attempts: int = 0
    total_delay: float = 0.0
    last_error: Optional[str] = None
    history: list[dict] = field(default_factory=list)


def calculate_delay(attempt: int, config: RetryConfig) -> float:
    """Calculate delay with exponential backoff and jitter."""
    delay = config.base_delay * (config.backoff_factor ** attempt)
    delay = min(delay, config.max_delay)
    jitter_range = delay * config.jitter
    delay += random.uniform(-jitter_range, jitter_range)
    return max(0.1, delay)


async def retry_request(
    request_fn: Callable[..., Any],
    config: RetryConfig | None = None,
    *args: Any,
    **kwargs: Any,
) -> RetryResult:
    """Execute a request with exponential backoff retry on transient failures.

    Args:
        request_fn: Async callable that performs the HTTP request.
                    Should raise on failure or return a response object
                    with a .status attribute.
        config: Retry configuration. Uses defaults if not provided.
        *args, **kwargs: Passed through to request_fn.

    Returns:
        RetryResult with success status, value, and retry history.
    """
    cfg = config or RetryConfig()
    result = RetryResult()
    total_delay = 0.0

    for attempt in range(cfg.max_attempts):
        result.attempts = attempt + 1
        attempt_start = time.time()

        try:
            response = await request_fn(*args, **kwargs)

            # Check if the response status is retryable
            status = getattr(response, "status", getattr(response, "status_code", 200))
            if status in cfg.retryable_status_codes and attempt < cfg.max_attempts - 1:
                delay = calculate_delay(attempt, cfg)
                total_delay += delay
                result.history.append({
                    "attempt": attempt + 1,
                    "status": status,
                    "action": "retry",
                    "delay": round(delay, 2),
                })
                logger.warning(
                    "Egress retry: attempt %d/%d returned %d, retrying in %.1fs",
                    attempt + 1, cfg.max_attempts, status, delay,
                )
                await asyncio.sleep(delay)
                continue

            result.success = True
            result.value = response
            result.total_delay = total_delay
            result.history.append({
                "attempt": attempt + 1,
                "status": status,
                "action": "success",
                "duration": round(time.time() - attempt_start, 2),
            })
            return result

        except cfg.retryable_exceptions as exc:
            delay = calculate_delay(attempt, cfg)
            total_delay += delay
            error_name = type(exc).__name__
            result.last_error = f"{error_name}: {exc}"
            result.history.append({
                "attempt": attempt + 1,
                "error": error_name,
                "action": "retry" if attempt < cfg.max_attempts - 1 else "exhausted",
                "delay": round(delay, 2),
            })
            logger.warning(
                "Egress retry: attempt %d/%d failed with %s, retrying in %.1fs",
                attempt + 1, cfg.max_attempts, error_name, delay,
            )
            if attempt < cfg.max_attempts - 1:
                await asyncio.sleep(delay)
            continue

        except Exception as exc:
            # Non-retryable exception — fail immediately
            result.success = False
            result.last_error = f"{type(exc).__name__}: {exc}"
            result.history.append({
                "attempt": attempt + 1,
                "error": type(exc).__name__,
                "action": "failed_non_retryable",
            })
            result.total_delay = total_delay
            return result

    # All attempts exhausted
    result.success = False
    result.total_delay = total_delay
    logger.error(
        "Egress retry exhausted: %d attempts, total delay %.1fs, last error: %s",
        cfg.max_attempts, total_delay, result.last_error,
    )
    return result


# Synchronous wrapper for non-async contexts
def retry_request_sync(
    request_fn: Callable[..., Any],
    config: RetryConfig | None = None,
    *args: Any,
    **kwargs: Any,
) -> RetryResult:
    """Synchronous version of retry_request for non-async contexts."""
    cfg = config or RetryConfig()
    result = RetryResult()
    total_delay = 0.0

    for attempt in range(cfg.max_attempts):
        result.attempts = attempt + 1

        try:
            response = request_fn(*args, **kwargs)
            status = getattr(response, "status", getattr(response, "status_code", 200))

            if status in cfg.retryable_status_codes and attempt < cfg.max_attempts - 1:
                delay = calculate_delay(attempt, cfg)
                total_delay += delay
                result.history.append({
                    "attempt": attempt + 1, "status": status,
                    "action": "retry", "delay": round(delay, 2),
                })
                time.sleep(delay)
                continue

            result.success = True
            result.value = response
            result.total_delay = total_delay
            return result

        except cfg.retryable_exceptions as exc:
            delay = calculate_delay(attempt, cfg)
            total_delay += delay
            result.last_error = f"{type(exc).__name__}: {exc}"
            result.history.append({
                "attempt": attempt + 1, "error": type(exc).__name__,
                "action": "retry" if attempt < cfg.max_attempts - 1 else "exhausted",
                "delay": round(delay, 2),
            })
            if attempt < cfg.max_attempts - 1:
                time.sleep(delay)
            continue

        except Exception as exc:
            result.success = False
            result.last_error = f"{type(exc).__name__}: {exc}"
            result.total_delay = total_delay
            return result

    result.success = False
    result.total_delay = total_delay
    return result
