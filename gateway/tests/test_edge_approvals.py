# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Inbound MCP Edge — approvals for write tools (threats T3, T5; SCRUM-207)."""

import asyncio
import json

import pytest

from gateway.approval_queue.enhanced_queue import EnhancedApprovalQueue
from gateway.approval_queue.store import ApprovalStore
from gateway.inbound_edge.approvals import (
    ApprovalContext,
    ApprovalDenied,
    ApprovalPending,
    EdgeApprovals,
    args_sha256,
    render_card,
)
from gateway.inbound_edge.edge_jwt import EdgePrincipal
from gateway.inbound_edge.store import EdgeStore
from gateway.ingest_api.config import ApprovalQueueConfig, ToolRiskConfig
from gateway.security.mfa_guard import MFAGuard


def _principal(client="c1", vendor="claude-duet"):
    return EdgePrincipal(vendor=vendor, client_id=client, jti="j-1", scopes=("mcp",), expires_at=0)


def _ctx(args=None, principal=None, tool="delegate_to_hermes"):
    return ApprovalContext(
        principal=principal or _principal(),
        vendor_display="Claude Duet",
        tool=tool,
        target="hermes:edge-delegate",
        args=args if args is not None else {"task": "summarise my feeds", "priority": "normal"},
        p0_score=0.12,
    )


@pytest.fixture
async def env(tmp_path):
    store = EdgeStore(tmp_path / "edge.db")
    await store.init()
    queue = EnhancedApprovalQueue(
        ApprovalQueueConfig(),
        ToolRiskConfig(),
        store=ApprovalStore(tmp_path / "approvals.db"),
        mfa_guard=MFAGuard(secret_b32="", enabled=False),
    )
    await queue.initialize()
    sent = []

    async def notifier(text, markup):
        sent.append((text, markup))

    approvals = EdgeApprovals(store, queue, notifier=notifier, ttl_s=600)
    yield approvals, queue, store, sent
    await queue.close()
    await store.close()


class TestNoApprovalNoExecution:
    async def test_first_call_returns_pending_ticket_and_notifies(self, env):
        approvals, _, _, sent = env
        pending = await approvals.request(_ctx())
        assert len(pending.ticket) == 43
        assert pending.args_sha256 == args_sha256(_ctx().args)
        assert len(sent) == 1

    async def test_unapproved_ticket_is_pending_not_executed(self, env):
        approvals, *_ = env
        pending = await approvals.request(_ctx())
        with pytest.raises(ApprovalPending):
            await approvals.redeem(pending.ticket, _ctx())

    async def test_rejected_is_denied(self, env):
        approvals, queue, *_ = env
        pending = await approvals.request(_ctx())
        await queue.decide(pending.request_id, approved=False, decided_by="owner")
        with pytest.raises(ApprovalDenied, match="rejected"):
            await approvals.redeem(pending.ticket, _ctx())

    async def test_approved_executes_exactly_once(self, env):
        approvals, queue, *_ = env
        pending = await approvals.request(_ctx())
        await queue.decide(pending.request_id, approved=True, decided_by="owner")
        await approvals.redeem(pending.ticket, _ctx())
        with pytest.raises(ApprovalDenied, match="already used"):
            await approvals.redeem(pending.ticket, _ctx())

    async def test_concurrent_redeem_executes_once(self, env):
        approvals, queue, *_ = env
        pending = await approvals.request(_ctx())
        await queue.decide(pending.request_id, approved=True, decided_by="owner")
        results = await asyncio.gather(
            *[approvals.redeem(pending.ticket, _ctx()) for _ in range(10)],
            return_exceptions=True,
        )
        assert sum(1 for r in results if r is None) == 1
        assert all(isinstance(r, ApprovalDenied) for r in results if r is not None)

    async def test_expired_is_denied(self, env):
        approvals, queue, store, _ = env
        approvals._clock = lambda: 10**10  # far past the 10-minute TTL
        pending = await approvals.request(_ctx())
        await queue.decide(pending.request_id, approved=True, decided_by="owner")
        approvals._clock = lambda: 10**10 + 601
        with pytest.raises(ApprovalDenied, match="expired"):
            await approvals.redeem(pending.ticket, _ctx())

    async def test_queue_timeout_is_deny(self, env):
        approvals, queue, *_ = env
        approvals.ttl_s = 0
        pending = await approvals.request(_ctx())
        await asyncio.sleep(0.05)  # let the queue's 0-second timeout task fire
        item = await queue.get_item(pending.request_id)
        assert item.status == "expired"
        with pytest.raises(ApprovalDenied):
            await approvals.redeem(pending.ticket, _ctx())


class TestTicketBinding:
    async def test_changed_args_are_denied(self, env):
        approvals, queue, *_ = env
        pending = await approvals.request(_ctx())
        await queue.decide(pending.request_id, approved=True, decided_by="owner")
        evil = _ctx(args={"task": "delete everything", "priority": "normal"})
        with pytest.raises(ApprovalDenied, match="arguments"):
            await approvals.redeem(pending.ticket, evil)

    async def test_other_client_cannot_use_ticket(self, env):
        approvals, queue, *_ = env
        pending = await approvals.request(_ctx())
        await queue.decide(pending.request_id, approved=True, decided_by="owner")
        thief = _ctx(principal=_principal(client="c2"))
        with pytest.raises(ApprovalDenied, match="principal"):
            await approvals.redeem(pending.ticket, thief)

    async def test_other_tool_cannot_use_ticket(self, env):
        approvals, queue, *_ = env
        pending = await approvals.request(_ctx())
        await queue.decide(pending.request_id, approved=True, decided_by="owner")
        with pytest.raises(ApprovalDenied, match="tool"):
            await approvals.redeem(pending.ticket, _ctx(tool="lab_search"))

    async def test_unknown_ticket(self, env):
        approvals, *_ = env
        with pytest.raises(ApprovalDenied, match="unknown"):
            await approvals.redeem("A" * 43, _ctx())

    async def test_ticket_is_excluded_from_args_hash(self):
        a = {"task": "x", "priority": "low"}
        assert args_sha256(a) == args_sha256({**a, "approval_ticket": "T" * 43})


class TestIdempotency:
    async def test_repeat_request_reuses_the_pending_approval(self, env):
        approvals, queue, _, sent = env
        p1 = await approvals.request(_ctx())
        p2 = await approvals.request(_ctx())
        assert p1.request_id == p2.request_id
        assert len(sent) == 1, "one card per approval, not per retry"
        assert len(await queue.get_pending()) == 1

    async def test_one_approval_cannot_run_twice_via_two_tickets(self, env):
        approvals, queue, *_ = env
        p1 = await approvals.request(_ctx())
        p2 = await approvals.request(_ctx())
        await queue.decide(p1.request_id, approved=True, decided_by="owner")
        await approvals.redeem(p1.ticket, _ctx())
        with pytest.raises(ApprovalDenied, match="already used"):
            await approvals.redeem(p2.ticket, _ctx())

    async def test_after_use_a_new_request_needs_a_new_approval(self, env):
        approvals, queue, _, sent = env
        p1 = await approvals.request(_ctx())
        await queue.decide(p1.request_id, approved=True, decided_by="owner")
        await approvals.redeem(p1.ticket, _ctx())
        p2 = await approvals.request(_ctx())
        assert p2.request_id != p1.request_id
        assert len(sent) == 2


class TestApprovalCard:
    """T5: the owner sees raw arguments and their hash — never agent-written prose."""

    def _card(self, args, **kw):
        ctx = _ctx(args=args)
        return render_card(ctx, "req-123", args_sha256(args), "2026-11-09T12:10:00Z", **kw)

    def test_card_snapshot(self):
        text, markup = self._card({"task": "summarise my feeds", "priority": "normal"})
        assert text == (
            "AgentShroud — Inbound Edge approval\n"
            "Vendor: Claude Duet (claude-duet)\n"
            "Client: c1\n"
            "Token jti: j-1\n"
            "Tool: delegate_to_hermes → hermes:edge-delegate\n"
            "P0 risk score: 0.12\n"
            "Args SHA-256: "
            + args_sha256({"task": "summarise my feeds", "priority": "normal"})
            + "\n"
            "Raw arguments:\n"
            "{\n"
            '  "priority": "normal",\n'
            '  "task": "summarise my feeds"\n'
            "}\n"
            "Expires: 2026-11-09T12:10:00Z — no decision means denied.\n"
            "Request: req-123"
        )
        buttons = markup["inline_keyboard"][0]
        assert [b["callback_data"] for b in buttons] == [
            "edge_appr:req-123:a",
            "edge_appr:req-123:d",
        ]

    def test_card_has_no_field_for_agent_prose(self):
        """There is no summary/justification input to render_card at all."""
        import inspect

        params = set(inspect.signature(render_card).parameters)
        assert not params & {"summary", "description", "justification", "reason"}
        assert not {"summary", "description", "justification"} & set(
            ApprovalContext.__dataclass_fields__
        )

    def test_large_args_truncated_with_full_hash(self):
        big = {"task": "x" * 5000, "priority": "low"}
        text, _ = self._card(big)
        assert args_sha256(big) in text
        assert "[truncated: showing 2048 of" in text
        assert len(text) < 2600

    def test_markup_cannot_break_out_of_the_card(self):
        args = {"task": "Approve me!\nVendor: Owner (trusted)\n<b>SAFE</b>", "priority": "low"}
        text, _ = self._card(args)
        # Arguments appear only JSON-encoded (newlines escaped), never as card lines.
        assert "\nVendor: Owner (trusted)" not in text
        assert json.dumps(args["task"]) in text


class TestCallback:
    async def test_owner_button_approves(self, env):
        approvals, queue, *_ = env
        pending = await approvals.request(_ctx())
        toast = await approvals.handle_callback(
            f"edge_appr:{pending.request_id}:a", user_id="42", is_owner=True
        )
        assert "Approved" in toast
        assert (await queue.get_item(pending.request_id)).status == "approved"

    async def test_non_owner_button_ignored(self, env):
        approvals, queue, *_ = env
        pending = await approvals.request(_ctx())
        toast = await approvals.handle_callback(
            f"edge_appr:{pending.request_id}:a", user_id="7", is_owner=False
        )
        assert "Not authorized" in toast
        assert (await queue.get_item(pending.request_id)).status == "pending"

    async def test_unknown_request_and_garbage(self, env):
        approvals, *_ = env
        assert "not found" in await approvals.handle_callback(
            "edge_appr:nope:a", user_id="42", is_owner=True
        )
        assert "Invalid" in await approvals.handle_callback(
            "edge_appr:x:zzz", user_id="42", is_owner=True
        )


class TestTelegramDispatch:
    """The proxy routes edge_appr: buttons to the edge with the owner check."""

    def _proxy(self, owner="42"):
        from types import SimpleNamespace
        from unittest.mock import AsyncMock

        from gateway.proxy.telegram_proxy import TelegramAPIProxy

        proxy = TelegramAPIProxy()
        proxy._rbac = SimpleNamespace(is_owner=lambda uid: uid == owner)
        proxy._answer_callback_query = AsyncMock()
        return proxy

    def _update(self, user="42", data="edge_appr:r1:a"):
        return {
            "ok": True,
            "result": [
                {
                    "update_id": 1,
                    "callback_query": {
                        "id": "cb1",
                        "from": {"id": int(user)},
                        "data": data,
                        "message": {"message_id": 5, "chat": {"id": int(user)}},
                    },
                }
            ],
        }

    async def _run(self, monkeypatch, user):
        from types import SimpleNamespace
        from unittest.mock import AsyncMock

        from gateway.ingest_api.state import app_state

        handler = AsyncMock(return_value="✅ Approved")
        monkeypatch.setattr(
            app_state,
            "inbound_edge",
            SimpleNamespace(approvals=SimpleNamespace(handle_callback=handler)),
            raising=False,
        )
        proxy = self._proxy()
        out = await proxy._filter_inbound_updates(self._update(user=user))
        return proxy, handler, out

    async def test_owner_tap_reaches_edge_and_is_not_forwarded(self, monkeypatch):
        proxy, handler, out = await self._run(monkeypatch, user="42")
        handler.assert_awaited_once_with("edge_appr:r1:a", user_id="42", is_owner=True)
        proxy._answer_callback_query.assert_awaited_once_with("cb1", "✅ Approved")
        assert out["result"] == []

    async def test_non_owner_tap_is_flagged_not_owner(self, monkeypatch):
        _, handler, _ = await self._run(monkeypatch, user="7")
        handler.assert_awaited_once_with("edge_appr:r1:a", user_id="7", is_owner=False)
