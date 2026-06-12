# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™ All rights reserved.
# SPDX-License-Identifier: Proprietary
#
# gateway/tests/test_llm_quota_detector.py
# Unit tests for gateway/proxy/llm_quota_detector.py
# Pure-function tests — no mocks required.

from __future__ import annotations

import json

import pytest

from gateway.proxy.llm_quota_detector import (
    _is_anthropic_quota,
    _is_google_quota,
    _is_openai_quota,
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
