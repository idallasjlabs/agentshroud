# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Stale-callback handling for EgressTelegramNotifier (kaizen fix).

Telegram callback_query IDs expire after ~60 minutes; pressing an old
approval button raises HTTP 400 "query is too old". Same goes for editing
the original message after it's too old or already edited. These are not
bugs in our code — they're user-driven expirations. Log at DEBUG rather
than ERROR so the gateway log isn't noisy with non-actionable failures.
"""

from __future__ import annotations

import io
import logging
from unittest.mock import patch
from urllib.error import HTTPError

import pytest

from gateway.proxy.telegram_egress_notify import (
    EgressTelegramNotifier,
    _is_stale_callback_error,
    _is_stale_edit_error,
)


def _stale_callback_err():
    body = (
        b'{"ok":false,"error_code":400,'
        b'"description":"Bad Request: query is too old and response timeout '
        b'expired or query ID is invalid"}'
    )
    return HTTPError(url="x", code=400, msg="Bad Request", hdrs=None, fp=io.BytesIO(body))


def _stale_edit_err():
    body = b'{"description":"Bad Request: message to edit not found"}'
    return HTTPError(url="x", code=400, msg="Bad Request", hdrs=None, fp=io.BytesIO(body))


def _real_err():
    body = b'{"description":"Unauthorized"}'
    return HTTPError(url="x", code=401, msg="Unauthorized", hdrs=None, fp=io.BytesIO(body))


def test_stale_detectors():
    # HTTPError wraps a BytesIO fp; close each one we construct or the
    # ResourceWarning gate (pytest.ini) escalates on finalize.
    cb = [_stale_callback_err(), _stale_edit_err(), _real_err(), _real_err()]
    try:
        assert _is_stale_callback_error(cb[0]) is True
        assert _is_stale_edit_error(cb[1]) is True
        assert _is_stale_callback_error(cb[2]) is False
        assert _is_stale_edit_error(cb[3]) is False
        assert _is_stale_callback_error(RuntimeError("connection refused")) is False
    finally:
        for c in cb:
            try:
                c.close()
            except Exception:
                pass


@pytest.mark.asyncio
async def test_answer_callback_stale_logs_debug_not_error(caplog):
    n = EgressTelegramNotifier(bot_token="t", owner_chat_id="0", base_url="http://localhost:0")
    err = _stale_callback_err()
    try:
        with patch.object(n, "_async_send", side_effect=err):
            caplog.set_level(logging.DEBUG, logger="agentshroud.proxy.telegram_egress_notify")
            ok = await n.answer_callback("cqid-1", "approved")
            assert ok is False
        errors = [r for r in caplog.records if r.levelno >= logging.ERROR]
        assert not errors, f"unexpected ERROR-level logs: {[r.message for r in errors]}"
        debug_msgs = [r.message for r in caplog.records if r.levelno == logging.DEBUG]
        assert any("expired" in m or "TTL" in m for m in debug_msgs)
    finally:
        err.close()


@pytest.mark.asyncio
async def test_answer_callback_real_error_still_logs_error(caplog):
    n = EgressTelegramNotifier(bot_token="t", owner_chat_id="0", base_url="http://localhost:0")
    err = _real_err()
    try:
        with patch.object(n, "_async_send", side_effect=err):
            caplog.set_level(logging.DEBUG)
            ok = await n.answer_callback("cqid-1", "approved")
            assert ok is False
        errors = [r for r in caplog.records if r.levelno >= logging.ERROR]
        assert any("Failed to answer callback" in r.message for r in errors)
    finally:
        err.close()


@pytest.mark.asyncio
async def test_edit_decision_message_stale_logs_debug_not_error(caplog):
    n = EgressTelegramNotifier(bot_token="t", owner_chat_id="0", base_url="http://localhost:0")
    err = _stale_edit_err()
    try:
        with patch.object(n, "_async_send", side_effect=err):
            caplog.set_level(logging.DEBUG, logger="agentshroud.proxy.telegram_egress_notify")
            ok = await n.edit_decision_message("chat-1", 99, "decided")
            assert ok is False
        errors = [r for r in caplog.records if r.levelno >= logging.ERROR]
        assert not errors, f"unexpected ERROR logs: {[r.message for r in errors]}"
    finally:
        err.close()


@pytest.mark.asyncio
async def test_edit_decision_message_real_error_still_logs_error(caplog):
    n = EgressTelegramNotifier(bot_token="t", owner_chat_id="0", base_url="http://localhost:0")
    err = _real_err()
    try:
        with patch.object(n, "_async_send", side_effect=err):
            caplog.set_level(logging.DEBUG)
            ok = await n.edit_decision_message("chat-1", 99, "decided")
            assert ok is False
        errors = [r for r in caplog.records if r.levelno >= logging.ERROR]
        assert any("Failed to edit egress decision message" in r.message for r in errors)
    finally:
        err.close()
