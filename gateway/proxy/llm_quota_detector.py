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
    # Anthropic returns the Claude.ai OAuth "out of extra usage" copy with HTTP 400
    # (wrapped as invalid_request_error), not 429/402. Observed 2026-06-15 with the
    # hermes competitive-intel cron after the user exhausted their monthly Claude.ai
    # usage cap. 400/403 are validation errors generally, so we only accept them
    # when the body carries the explicit quota substring.
    if status not in (429, 402, 400, 403):
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


# ---------------------------------------------------------------------------
# Overloaded detection — capacity errors that warrant cloud→local failover.
# Anthropic can return HTTP 200 with an error envelope in the body, which
# bypasses all status-code-based handling (observed 2026-06-11: cron jobs
# died on "HTTP 200: Overloaded" after 3 client retries).
# ---------------------------------------------------------------------------

_OVERLOADED_STATUSES = (200, 503, 529)


def is_overloaded(status: int, body: bytes) -> tuple[bool, str]:
    """Return (True, "anthropic_overloaded") for an overloaded_error envelope.

    Only claims statuses outside is_quota_exhausted's domain (429/402 are
    quota territory). The error envelope is compact, so a fast substring
    check on the body head avoids JSON-parsing large legitimate responses;
    a full parse then confirms error.type to avoid content false-positives.
    """
    if status not in _OVERLOADED_STATUSES or not body:
        return False, ""
    if b"overloaded_error" not in body[:2048]:
        return False, ""
    try:
        parsed = json.loads(body.decode("utf-8", errors="replace"))
    except json.JSONDecodeError:
        return False, ""
    if not isinstance(parsed, dict):
        return False, ""
    err = parsed.get("error")
    if isinstance(err, dict) and err.get("type") == "overloaded_error":
        return True, "anthropic_overloaded"
    return False, ""


# ---------------------------------------------------------------------------
# Post-retry rate-limit failover — the response we propagate to the caller
# already survived the upstream retry loop (_RETRYABLE = {429, 503, 529} at
# llm_proxy.py:1142). A final 429 here is not a quota wall (those are caught
# by is_quota_exhausted) and not a capacity flag in the body (caught by
# is_overloaded) — it's persistent rate-limit. Hermes's SDK turns this into
# AssertionError → cron jobs miss (observed 2026-06-13/14/15). Failover so
# the run completes on local rather than die.
# ---------------------------------------------------------------------------


def is_rate_limited_post_retry(status: int, body: bytes) -> tuple[bool, str]:
    """Return (True, "anthropic_rate_limit"/"openai_rate_limit"/...) for a
    persistent 429 that escaped the upstream retry loop.

    Caller must invoke is_quota_exhausted and is_overloaded first so this
    only fires for the residual rate-limit case (otherwise we'd mis-label
    quota walls as rate limits in telemetry)."""
    if status != 429:
        return False, ""
    # The body for a plain 429 may still carry provider hints — preserve the
    # token so failover telemetry can distinguish providers.
    text = body.decode("utf-8", errors="replace") if body else ""
    lower = text.lower()
    # Anthropic — request IDs prefixed with "req_011", error.type "rate_limit_error"
    if "anthropic" in lower or "req_011" in lower or "rate_limit_error" in lower:
        return True, "anthropic_rate_limit"
    if "openai" in lower or "insufficient" in lower:
        return True, "openai_rate_limit"
    if "google" in lower or "RESOURCE" in text:
        return True, "google_rate_limit"
    return True, "cloud_rate_limit"
