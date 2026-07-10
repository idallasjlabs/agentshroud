# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™ All rights reserved.
# SPDX-License-Identifier: Proprietary
#
# gateway/tests/test_llm_quota_detector.py
# Unit tests for gateway/proxy/llm_quota_detector.py
# Pure-function tests — no mocks required.

from __future__ import annotations

import json

from gateway.proxy.llm_quota_detector import (
    is_quota_exhausted,
)


def test_detect_anthropic_extra_usage():
    body = b"Your account is out of extra usage for this period."
    result = is_quota_exhausted(429, body)
    assert result == (True, "anthropic_credit_balance")


def test_detect_anthropic_credit_balance_substring():
    body = b"credit balance is too low to complete this request."
    exhausted, _ = is_quota_exhausted(429, body)
    assert exhausted is True


def test_detect_anthropic_settings_url():
    body = b"Please add more at claude.ai/settings/usage to continue."
    exhausted, reason = is_quota_exhausted(429, body)
    assert exhausted is True
    assert reason == "anthropic_credit_balance"


def test_detect_anthropic_rate_limit_type_quota_message():
    payload = json.dumps(
        {
            "error": {
                "type": "rate_limit_error",
                "message": "Your credit balance has been exhausted.",
            }
        }
    ).encode()
    result = is_quota_exhausted(429, payload)
    assert result == (True, "anthropic_credit_balance")


def test_detect_anthropic_400_oauth_extra_usage():
    """Anthropic returns the Claude.ai OAuth quota copy with HTTP 400
    (wrapped as invalid_request_error), not 429/402. Observed 2026-06-15
    when the user exhausted their monthly Claude.ai usage cap and every
    hermes cron run died with this 400 in a generic retry loop."""
    payload = json.dumps(
        {
            "type": "error",
            "error": {
                "type": "invalid_request_error",
                "message": "You're out of extra usage. Add more at claude.ai/settings/usage and keep going.",
            },
        }
    ).encode()
    result = is_quota_exhausted(400, payload)
    assert result == (True, "anthropic_credit_balance")


def test_400_without_quota_substring_not_flagged():
    """Generic 400 validation errors must NOT trigger failover."""
    payload = json.dumps(
        {
            "type": "error",
            "error": {"type": "invalid_request_error", "message": "messages: field required"},
        }
    ).encode()
    assert is_quota_exhausted(400, payload) == (False, "")


def test_no_false_positive_on_anthropic_request_rate_limit():
    payload = json.dumps(
        {
            "error": {
                "type": "rate_limit_error",
                "message": "Too many requests. Please slow down.",
            }
        }
    ).encode()
    result = is_quota_exhausted(429, payload)
    assert result == (False, "")


def test_detect_openai_insufficient_quota():
    body = b'{"error": {"code": "insufficient_quota", "message": "..."}}'
    result = is_quota_exhausted(429, body)
    assert result == (True, "openai_quota")


def test_detect_google_resource_exhausted():
    body = b'{"error": {"status": "RESOURCE_EXHAUSTED", "message": "Quota exceeded for project."}}'
    result = is_quota_exhausted(429, body)
    assert result == (True, "google_quota")


def test_200_never_triggers():
    body = b"credit balance is too low; insufficient_quota; RESOURCE_EXHAUSTED"
    result = is_quota_exhausted(200, body)
    assert result == (False, "")


def test_500_never_triggers():
    body = b"credit balance is too low for this request"
    result = is_quota_exhausted(500, body)
    assert result == (False, "")


def test_non_json_body_anthropic_429_no_substring_match():
    body = b"internal error occurred on the server"
    result = is_quota_exhausted(429, body)
    assert result == (False, "")


# ---------------------------------------------------------------------------
# is_overloaded — provider "overloaded" envelopes (incl. HTTP-200 variant)
# ---------------------------------------------------------------------------

from gateway.proxy.llm_quota_detector import is_overloaded  # noqa: E402

_OVERLOADED_BODY = json.dumps(
    {
        "type": "error",
        "error": {"details": None, "type": "overloaded_error", "message": "Overloaded"},
        "request_id": "req_011Cbwg5qYrMghCZJc4JBL8G",
    }
).encode()


class TestIsOverloaded:
    def test_http_200_with_overloaded_body(self):
        hit, token = is_overloaded(200, _OVERLOADED_BODY)
        assert hit and token == "anthropic_overloaded"

    def test_http_529_with_overloaded_body(self):
        hit, token = is_overloaded(529, _OVERLOADED_BODY)
        assert hit and token == "anthropic_overloaded"

    def test_http_503_with_overloaded_body(self):
        hit, token = is_overloaded(503, _OVERLOADED_BODY)
        assert hit and token == "anthropic_overloaded"

    def test_normal_200_message_body_not_flagged(self):
        body = json.dumps({"type": "message", "content": [{"type": "text", "text": "hi"}]}).encode()
        assert is_overloaded(200, body) == (False, "")

    def test_other_error_types_not_flagged(self):
        body = json.dumps(
            {"type": "error", "error": {"type": "invalid_request_error", "message": "bad"}}
        ).encode()
        assert is_overloaded(200, body) == (False, "")

    def test_quota_statuses_not_claimed(self):
        # 429/402 belong to is_quota_exhausted; is_overloaded must not claim them
        assert is_overloaded(429, _OVERLOADED_BODY) == (False, "")

    def test_mention_in_content_not_flagged(self):
        # "overloaded_error" appearing deep in legit content must not trigger
        body = json.dumps(
            {
                "type": "message",
                "content": [{"type": "text", "text": "x" * 4000 + "overloaded_error"}],
            }
        ).encode()
        assert is_overloaded(200, body) == (False, "")

    def test_empty_and_garbage_bodies(self):
        assert is_overloaded(200, b"") == (False, "")
        assert is_overloaded(529, b"not json overloaded_error") == (False, "")


class TestOverloadedMultiProvider:
    """SCRUM-60: in-body overload envelopes from OpenAI and Gemini must fail
    over exactly like Anthropic's overloaded_error — a provider capacity
    error that escapes status-code handling kills cron jobs silently."""

    def test_openai_server_error_503(self):
        body = json.dumps(
            {
                "error": {
                    "message": "The server is currently overloaded.",
                    "type": "server_error",
                    "param": None,
                    "code": None,
                }
            }
        ).encode()
        assert is_overloaded(503, body) == (True, "openai_overloaded")

    def test_openai_server_error_500_requires_capacity_wording(self):
        # At 500, server_error is OpenAI's blanket internal-error class —
        # deterministic request-caused 500s must NOT fail over (review
        # finding 2026-07-09); capacity wording is required.
        generic = json.dumps(
            {
                "error": {
                    "message": "The server had an error processing your request.",
                    "type": "server_error",
                    "param": None,
                    "code": None,
                }
            }
        ).encode()
        assert is_overloaded(500, generic) == (False, "")
        capacity = json.dumps(
            {
                "error": {
                    "message": "The engine is currently overloaded.",
                    "type": "server_error",
                    "param": None,
                    "code": None,
                }
            }
        ).encode()
        assert is_overloaded(500, capacity) == (True, "openai_overloaded")

    def test_anthropic_api_error_500_not_flagged(self):
        # The gateway itself emits api_error envelopes and Anthropic uses
        # api_error for internal 500s — adding 500 to the status gate must
        # not make these fail over.
        body = json.dumps(
            {
                "error": {
                    "type": "api_error",
                    "message": "An internal server error occurred.",
                }
            }
        ).encode()
        assert is_overloaded(500, body) == (False, "")

    def test_openai_overloaded_message_http_200(self):
        # In-body error with 200 status — the exact class that bypasses
        # status-based retry (Anthropic precedent, 2026-06-11).
        body = json.dumps(
            {
                "error": {
                    "message": "That model is currently overloaded with other requests.",
                    "type": "requests",
                    "param": None,
                    "code": None,
                }
            }
        ).encode()
        assert is_overloaded(200, body) == (True, "openai_overloaded")

    def test_openai_invalid_request_not_flagged(self):
        body = json.dumps(
            {
                "error": {
                    "message": "Invalid value for max_tokens",
                    "type": "invalid_request_error",
                    "param": "max_tokens",
                    "code": None,
                }
            }
        ).encode()
        assert is_overloaded(503, body) == (False, "")

    def test_gemini_unavailable_503(self):
        body = json.dumps(
            {
                "error": {
                    "code": 503,
                    "message": "The model is overloaded. Please try again later.",
                    "status": "UNAVAILABLE",
                }
            }
        ).encode()
        assert is_overloaded(503, body) == (True, "gemini_overloaded")

    def test_gemini_unavailable_http_200(self):
        body = json.dumps(
            {
                "error": {
                    "code": 503,
                    "message": "The service is currently unavailable.",
                    "status": "UNAVAILABLE",
                }
            }
        ).encode()
        assert is_overloaded(200, body) == (True, "gemini_overloaded")

    def test_gemini_resource_exhausted_stays_quota_territory(self):
        # 429 RESOURCE_EXHAUSTED is quota/rate territory — is_overloaded
        # must not claim it even though the shape is a Google error envelope.
        body = json.dumps(
            {
                "error": {
                    "code": 429,
                    "message": "Resource has been exhausted",
                    "status": "RESOURCE_EXHAUSTED",
                }
            }
        ).encode()
        assert is_overloaded(429, body) == (False, "")

    def test_gemini_invalid_argument_not_flagged(self):
        body = json.dumps(
            {
                "error": {
                    "code": 400,
                    "message": "Invalid JSON payload",
                    "status": "INVALID_ARGUMENT",
                }
            }
        ).encode()
        assert is_overloaded(503, body) == (False, "")

    def test_overloaded_word_in_chat_content_not_flagged(self):
        # A model TALKING about overload in a normal completion must not
        # trigger failover (no top-level error envelope).
        body = json.dumps(
            {
                "id": "chatcmpl-1",
                "choices": [
                    {
                        "message": {
                            "role": "assistant",
                            "content": "The server is currently overloaded is an OpenAI server_error.",
                        }
                    }
                ],
            }
        ).encode()
        assert is_overloaded(200, body) == (False, "")

    def test_anthropic_detection_unchanged(self):
        assert is_overloaded(200, _OVERLOADED_BODY) == (True, "anthropic_overloaded")

    def test_non_dict_json_body_not_flagged(self):
        # Valid JSON that isn't an object (list/string) — parse succeeds,
        # shape check must reject.
        assert is_overloaded(503, b'["server_error overloaded"]') == (False, "")

    def test_unrecognized_error_shape_not_flagged(self):
        # Top-level error dict but no provider signature — e.g. a proxy's
        # own error format mentioning UNAVAILABLE only in free text keys.
        body = json.dumps({"error": {"detail": "backend UNAVAILABLE", "origin": "envoy"}}).encode()
        assert is_overloaded(503, body) == (False, "")

    def test_openai_server_error_503_without_capacity_wording(self):
        # At 503 the bare server_error class IS a capacity signal — no
        # message wording required (only 500 needs the extra evidence).
        body = json.dumps(
            {
                "error": {
                    "message": "The server had an error.",
                    "type": "server_error",
                    "param": None,
                    "code": None,
                }
            }
        ).encode()
        assert is_overloaded(503, body) == (True, "openai_overloaded")
