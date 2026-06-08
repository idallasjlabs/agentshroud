# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""
Quota-exhaustion detector for cloud LLM providers.

Pure-function module — no I/O, no side effects. Takes a raw HTTP status code
and response body; returns (is_quota_error, stable_token) where the token
identifies the provider and error class for logging/telemetry.

Stable tokens:
  "anthropic_credit_balance"  — Anthropic credit balance / extra-usage exhausted
  "openai_quota"              — OpenAI insufficient_quota / billing limit
  "google_quota"              — Google Quota exceeded / RESOURCE_EXHAUSTED

Returns (False, "") for all non-quota errors, including transient rate-limits
(e.g. "Too many requests" 429s that ARE retryable) so callers don't misroute.
"""

from __future__ import annotations

import json

# ---------------------------------------------------------------------------
# Anthropic quota fingerprints
# ---------------------------------------------------------------------------

# These substrings in the body conclusively indicate a billing/quota wall,
# not a transient request-rate limit.
_ANTHROPIC_QUOTA_SUBSTRINGS = (
    "out of extra usage",
    "credit balance is too low",
    "Your credit balance is too low",
    "add more at claude.ai/settings/usage",
)

# If error.type == "rate_limit_error" we need a second check: the message must
# contain one of these to distinguish billing quota from request-rate limits.
_ANTHROPIC_RATE_LIMIT_QUOTA_MARKERS = (
    "credit balance",
    "out of extra usage",
    "billing",
    "usage limit",
)


def _is_anthropic_quota(status: int, body: bytes) -> bool:
    if status not in (429, 402):
        return False
    text = body.decode("utf-8", errors="replace")

    # Fast path — plain substring match covers the most common responses
    for substr in _ANTHROPIC_QUOTA_SUBSTRINGS:
        if substr in text:
            return True

    # Structured path — error.type == "rate_limit_error" with quota marker
    try:
        parsed = json.loads(text)
        err = parsed.get("error", {})
        if err.get("type") == "rate_limit_error":
            msg = (err.get("message") or "").lower()
            return any(marker in msg for marker in _ANTHROPIC_RATE_LIMIT_QUOTA_MARKERS)
    except (json.JSONDecodeError, AttributeError):
        pass

    return False


# ---------------------------------------------------------------------------
# OpenAI quota fingerprints
# ---------------------------------------------------------------------------

_OPENAI_QUOTA_SUBSTRINGS = (
    "insufficient_quota",
    "You exceeded your current quota",
    "exceeded your current quota",
)


def _is_openai_quota(status: int, body: bytes) -> bool:
    if status not in (429, 402):
        return False
    text = body.decode("utf-8", errors="replace")
    return any(substr in text for substr in _OPENAI_QUOTA_SUBSTRINGS)


# ---------------------------------------------------------------------------
# Google quota fingerprints
# ---------------------------------------------------------------------------

_GOOGLE_QUOTA_SUBSTRINGS = (
    "RESOURCE_EXHAUSTED",
    "Quota exceeded",
    "rateLimitExceeded",
)


def _is_google_quota(status: int, body: bytes) -> bool:
    if status not in (429, 403):
        return False
    text = body.decode("utf-8", errors="replace")
    return any(substr in text for substr in _GOOGLE_QUOTA_SUBSTRINGS)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def is_quota_exhausted(status: int, body: bytes) -> tuple[bool, str]:
    """Return (True, token) if the response indicates a billing/quota wall.

    The stable token identifies provider and error class for logging; callers
    must not parse it further (treat as opaque string).

    Returns (False, "") for transient rate limits, auth errors, or any
    non-quota 4xx/5xx so callers never misroute on false positives.
    """
    if _is_anthropic_quota(status, body):
        return True, "anthropic_credit_balance"
    if _is_openai_quota(status, body):
        return True, "openai_quota"
    if _is_google_quota(status, body):
        return True, "google_quota"
    return False, ""
