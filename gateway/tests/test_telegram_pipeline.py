# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
"""Integration tests: SecurityPipeline wired into TelegramAPIProxy message paths.

Verifies that every Telegram message (inbound and outbound) flows through the
full security pipeline — PromptGuard, HeuristicClassifier, PII sanitizer, etc.
"""
from __future__ import annotations

import json
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from gateway.proxy.pipeline import PipelineAction, PipelineResult
from gateway.proxy.telegram_proxy import TelegramAPIProxy


# ── Helpers ──────────────────────────────────────────────────────────────────

def _make_pipeline_result(
    *,
    blocked: bool = False,
    block_reason: str = "",
    sanitized_message: str = "original text",
    pii_redactions: list[str] | None = None,
) -> PipelineResult:
    return PipelineResult(
        original_message="original text",
        sanitized_message=sanitized_message,
        action=PipelineAction.BLOCK if blocked else PipelineAction.FORWARD,
        blocked=blocked,
        block_reason=block_reason,
        pii_redactions=pii_redactions or [],
    )


def _make_proxy(*, pipeline=None, sanitizer=None, owner_user_id="99999"):
    """Build a TelegramAPIProxy with mocked RBAC and rate limiter.

    RBACConfig and RateLimiter are imported inside __init__, so we patch at
    their source module paths, not at the telegram_proxy module attribute.
    """
    with (
        patch("gateway.security.rbac_config.RBACConfig") as mock_rbac_cls,
        patch("gateway.ingest_api.auth.RateLimiter") as mock_rl_cls,
    ):
        mock_rbac = MagicMock()
        mock_rbac.is_owner.side_effect = lambda uid: uid == owner_user_id
        mock_rbac.owner_user_id = owner_user_id
        # Include the default test user_id as a collaborator so messages reach the pipeline
        # (unknown users are dropped before the pipeline at the RBAC gate)
        mock_rbac.collaborator_user_ids = ["42"]
        mock_rbac_cls.return_value = mock_rbac

        mock_rl = MagicMock()
        mock_rl.check.return_value = True  # no rate limiting by default
        mock_rl_cls.return_value = mock_rl

        proxy = TelegramAPIProxy(pipeline=pipeline, sanitizer=sanitizer)
        proxy._bot_token = ""  # suppress real HTTP calls
        return proxy


def _make_update(text: str, user_id: str = "42", chat_id: int = 100) -> dict:
    return {
        "message": {
            "text": text,
            "from": {"id": int(user_id)},
            "chat": {"id": chat_id},
        }
    }


def _getUpdates_response(updates: list[dict]) -> dict:
    return {"ok": True, "result": updates}


# ── Test 1: inbound → pipeline.process_inbound called with skip_context_guard=True ──

class TestInboundPipelineWired:
    @pytest.mark.asyncio
    async def test_pipeline_process_inbound_called_with_skip_context_guard(self):
        pipeline = MagicMock()
        pipeline.process_inbound = AsyncMock(
            return_value=_make_pipeline_result(sanitized_message="original text")
        )
        proxy = _make_proxy(pipeline=pipeline)

        response = _getUpdates_response([_make_update("process the quarterly update", user_id="42")])
        await proxy._filter_inbound_updates(response)

        pipeline.process_inbound.assert_called_once()
        call_kwargs = pipeline.process_inbound.call_args.kwargs
        assert call_kwargs.get("skip_context_guard") is True
        assert call_kwargs.get("source") == "telegram"
        assert call_kwargs.get("message") == "process the quarterly update"


# ── Test 2: blocked non-owner message → dropped, stats incremented ──

class TestInboundPipelineBlockedNonOwner:
    @pytest.mark.asyncio
    async def test_blocked_non_owner_drops_update_and_increments_stats(self):
        pipeline = MagicMock()
        pipeline.process_inbound = AsyncMock(
            return_value=_make_pipeline_result(
                blocked=True, block_reason="Prompt injection detected"
            )
        )
        proxy = _make_proxy(pipeline=pipeline, owner_user_id="99999")
        proxy._notify_user_blocked = AsyncMock()

        response = _getUpdates_response([_make_update("inject this", user_id="42")])
        result = await proxy._filter_inbound_updates(response)

        # Blocked collaborator message is dropped (bot never receives it);
        # user is notified via _notify_user_blocked and stats are incremented.
        assert len(result["result"]) == 0
        assert proxy._stats["messages_blocked"] == 1
        proxy._notify_user_blocked.assert_called_once()


# ── Test 3: blocked owner message → allowed through, sanitized text applied ──

class TestInboundPipelineBlockedOwner:
    @pytest.mark.asyncio
    async def test_blocked_owner_message_allowed_through_with_sanitized_text(self):
        pipeline = MagicMock()
        pipeline.process_inbound = AsyncMock(
            return_value=_make_pipeline_result(
                blocked=True,
                block_reason="Prompt injection detected",
                sanitized_message="original text",  # unchanged — no PII
            )
        )
        proxy = _make_proxy(pipeline=pipeline, owner_user_id="99999")

        response = _getUpdates_response([_make_update("inject this", user_id="99999")])
        result = await proxy._filter_inbound_updates(response)

        # Owner's update must pass through
        assert len(result["result"]) == 1
        assert proxy._stats["messages_blocked"] == 0


# ── Test 4: pipeline exception → non-owner blocked (fail-closed) ──

class TestInboundPipelineExceptionNonOwner:
    @pytest.mark.asyncio
    async def test_pipeline_exception_fails_closed_for_non_owner(self):
        pipeline = MagicMock()
        pipeline.process_inbound = AsyncMock(side_effect=RuntimeError("guard crashed"))
        proxy = _make_proxy(pipeline=pipeline, owner_user_id="99999")
        proxy._notify_user_blocked = AsyncMock()

        response = _getUpdates_response([_make_update("process the quarterly update", user_id="42")])
        result = await proxy._filter_inbound_updates(response)

        # Fail-closed: blocked collaborator message is dropped (bot never receives it);
        # user is notified via _notify_user_blocked and stats are incremented.
        assert len(result["result"]) == 0
        assert proxy._stats["messages_blocked"] == 1
        proxy._notify_user_blocked.assert_called_once()


# ── Test 5: pipeline exception → owner allowed through ──

class TestInboundPipelineExceptionOwner:
    @pytest.mark.asyncio
    async def test_pipeline_exception_allows_owner_through(self):
        pipeline = MagicMock()
        pipeline.process_inbound = AsyncMock(side_effect=RuntimeError("guard crashed"))
        proxy = _make_proxy(pipeline=pipeline, owner_user_id="99999")

        response = _getUpdates_response([_make_update("hello", user_id="99999")])
        result = await proxy._filter_inbound_updates(response)

        # Owner's update must pass through even on pipeline error
        assert len(result["result"]) == 1
        assert proxy._stats["messages_blocked"] == 0


# ── Test 6: outbound → pipeline.process_outbound called ──

class TestOutboundPipelineWired:
    @pytest.mark.asyncio
    async def test_pipeline_process_outbound_called_for_send_message(self):
        pipeline = MagicMock()
        pipeline.process_outbound = AsyncMock(
            return_value=_make_pipeline_result(sanitized_message="safe reply")
        )
        proxy = _make_proxy(pipeline=pipeline)

        body = json.dumps({"chat_id": 100, "text": "bot reply"}).encode()
        await proxy._filter_outbound(body, "application/json")

        pipeline.process_outbound.assert_called_once()
        call_kwargs = pipeline.process_outbound.call_args.kwargs
        assert call_kwargs.get("source") == "telegram"
        assert call_kwargs.get("response") == "bot reply"

    @pytest.mark.asyncio
    async def test_send_message_draft_also_runs_outbound_filtering(self):
        """sendMessageDraft must be suppressed to prevent draft flicker leaks."""
        pipeline = MagicMock()
        pipeline.process_outbound = AsyncMock(
            return_value=_make_pipeline_result(sanitized_message="clean draft")
        )
        proxy = _make_proxy(pipeline=pipeline)

        captured = {}

        async def fake_forward(url, body, content_type):
            captured["body"] = json.loads(body.decode())
            return {"ok": True, "result": {"message_id": 1}}

        proxy._forward_to_telegram = fake_forward
        body = json.dumps({"chat_id": 100, "text": "draft text"}).encode()
        result = await proxy.proxy_request(
            bot_token="dummy",
            method="sendMessageDraft",
            body=body,
            content_type="application/json",
        )

        pipeline.process_outbound.assert_not_called()
        assert captured == {}
        assert result.get("ok") is True
        assert result.get("result", {}).get("suppressed") is True


# ── Test 7: outbound blocked → replacement text set ──

class TestOutboundPipelineBlocked:
    @pytest.mark.asyncio
    async def test_outbound_blocked_replaces_text(self):
        pipeline = MagicMock()
        pipeline.process_outbound = AsyncMock(
            return_value=_make_pipeline_result(
                blocked=True, block_reason="PromptProtection: critical disclosure"
            )
        )
        proxy = _make_proxy(pipeline=pipeline)

        body = json.dumps({"chat_id": 100, "text": "secret: sk-abc123"}).encode()
        result_body = await proxy._filter_outbound(body, "application/json")

        result_data = json.loads(result_body)
        assert any(
            kw in result_data["text"].lower()
            for kw in ("blocked", "security policy", "protected", "not allowed")
        )
        assert proxy._stats["outbound_filtered"] == 1


# ── Test 8: pipeline=None fallback → direct sanitizer used (inbound) ──

class TestInboundFallbackToDirectSanitizer:
    @pytest.mark.asyncio
    async def test_no_pipeline_falls_back_to_direct_sanitizer(self):
        sanitizer = MagicMock()
        sanitize_return = MagicMock(
            sanitized_content="redacted text",
            entity_types_found=["EMAIL"],
            redactions=[("EMAIL", 0, 5)],
        )
        sanitizer.sanitize = AsyncMock(return_value=sanitize_return)

        proxy = _make_proxy(pipeline=None, sanitizer=sanitizer)

        response = _getUpdates_response([_make_update("email@example.com", user_id="42")])
        result = await proxy._filter_inbound_updates(response)

        sanitizer.sanitize.assert_called_once()
        assert proxy._stats["messages_sanitized"] == 1
        assert result["result"][0]["message"]["text"] == "redacted text"
