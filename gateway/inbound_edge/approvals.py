# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Human approval for edge write tools (SCRUM-207, threats T3 and T5).

Every ``write`` tool call from a hosted agent goes through the existing
:class:`EnhancedApprovalQueue`. The MCP Python SDK has no Tasks extension yet, and an
elicitation answer from a hosted agent proves nothing about a human, so the flow is:

1. First call → :meth:`EdgeApprovals.request` queues the item (10-minute TTL, no
   decision = denied), sends the owner a card, and returns an opaque ticket.
2. The agent repeats the *identical* call with ``approval_ticket``.
3. :meth:`EdgeApprovals.redeem` checks the ticket belongs to the same principal,
   tool and argument hash, that the owner approved it, and consumes it atomically.
   One approval executes exactly once, however many tickets point at it.

The card (:func:`render_card`) is built only from structured fields — vendor, client,
token ``jti``, tool, target, P0 score, the SHA-256 of the canonical arguments and the
raw arguments as JSON. There is no parameter through which agent-written prose could
reach it: an agent cannot "explain" its way past the owner (OWASP ASI09).

IEC 62443 alignment: FR2 (Use Control) — SR 2.1 authorisation enforcement with a
human in the loop for state-changing actions.
"""

import hashlib
import json
import logging
import secrets
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Any, Awaitable, Callable, Dict, Optional, Tuple

from gateway.approval_queue.enhanced_queue import EnhancedApprovalQueue
from gateway.inbound_edge.descriptors import canonical_bytes
from gateway.inbound_edge.edge_jwt import EdgePrincipal
from gateway.inbound_edge.store import EdgeStore
from gateway.ingest_api.config import ToolRiskPolicy
from gateway.ingest_api.models import ApprovalRequest

logger = logging.getLogger("agentshroud.inbound_edge.approvals")

DEFAULT_TTL_S = 600
CARD_ARGS_LIMIT = 2048
CALLBACK_PREFIX = "edge_appr:"

Notifier = Callable[[str, Dict[str, Any]], Awaitable[None]]


class ApprovalPending(Exception):
    """The owner has not decided yet. Not an error for the caller — try again later."""


class ApprovalDenied(Exception):
    """The ticket cannot authorise this call. ``str(exc)`` is safe to return."""


@dataclass(frozen=True)
class ApprovalContext:
    principal: EdgePrincipal
    vendor_display: str
    tool: str
    target: str
    args: Dict[str, Any]
    p0_score: float


@dataclass(frozen=True)
class PendingApproval:
    request_id: str
    ticket: str
    expires_at: str
    args_sha256: str


def args_sha256(args: Dict[str, Any]) -> str:
    """Hash of the canonical arguments, excluding the ticket itself."""
    clean = {k: v for k, v in args.items() if k != "approval_ticket"}
    return hashlib.sha256(canonical_bytes(clean)).hexdigest()


def _iso(ts: float) -> str:
    return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat().replace("+00:00", "Z")


def render_card(
    ctx: ApprovalContext, request_id: str, args_hash: str, expires_at: str
) -> Tuple[str, Dict[str, Any]]:
    """Plain-text card (no parse mode, so nothing in the args can format it)."""
    clean = {k: v for k, v in ctx.args.items() if k != "approval_ticket"}
    pretty = json.dumps(clean, indent=2, sort_keys=True, ensure_ascii=False)
    if len(pretty) > CARD_ARGS_LIMIT:
        pretty = (
            pretty[:CARD_ARGS_LIMIT]
            + f"\n[truncated: showing {CARD_ARGS_LIMIT} of {len(pretty)} characters; "
            "verify with the SHA-256]"
        )
    text = "\n".join(
        [
            "AgentShroud — Inbound Edge approval",
            f"Vendor: {ctx.vendor_display} ({ctx.principal.vendor})",
            f"Client: {ctx.principal.client_id}",
            f"Token jti: {ctx.principal.jti}",
            f"Tool: {ctx.tool} → {ctx.target}",
            f"P0 risk score: {ctx.p0_score:.2f}",
            f"Args SHA-256: {args_hash}",
            "Raw arguments:",
            pretty,
            f"Expires: {expires_at} — no decision means denied.",
            f"Request: {request_id}",
        ]
    )
    markup = {
        "inline_keyboard": [
            [
                {"text": "✅ Approve", "callback_data": f"{CALLBACK_PREFIX}{request_id}:a"},
                {"text": "❌ Deny", "callback_data": f"{CALLBACK_PREFIX}{request_id}:d"},
            ]
        ]
    }
    return text, markup


class EdgeApprovals:
    def __init__(
        self,
        store: EdgeStore,
        queue: EnhancedApprovalQueue,
        notifier: Optional[Notifier] = None,
        ttl_s: int = DEFAULT_TTL_S,
        clock: Callable[[], float] = time.time,
    ):
        self._store = store
        self._queue = queue
        self._notifier = notifier
        self.ttl_s = ttl_s
        self._clock = clock

    @staticmethod
    def _idem_key(ctx: ApprovalContext, args_hash: str) -> str:
        raw = f"{ctx.principal.principal_id}\x00{ctx.tool}\x00{args_hash}"
        return hashlib.sha256(raw.encode()).hexdigest()

    async def _status(self, request_id: str) -> str:
        item = await self._queue.get_item(request_id)
        return item.status if item is not None else "missing"

    async def request(self, ctx: ApprovalContext) -> PendingApproval:
        """Queue (or re-use) the approval for this exact call and issue a ticket."""
        args_hash = args_sha256(ctx.args)
        idem = self._idem_key(ctx, args_hash)
        request_id = await self._store.open_approval_for(idem)
        if request_id is not None and await self._status(request_id) not in (
            "pending",
            "approved",
        ):
            request_id = None

        if request_id is None:
            expires_ts = self._clock() + self.ttl_s
            policy = ToolRiskPolicy(
                require_approval=True,
                timeout_seconds=self.ttl_s,
                timeout_action="deny",
                notify_channels=["websocket"],
                owner_bypass=False,
            )
            item = await self._queue.submit(
                ApprovalRequest(
                    action_type=f"edge_tool:{ctx.tool}",
                    description=(
                        f"Inbound edge write: {ctx.principal.vendor} → {ctx.tool} "
                        f"(args sha256 {args_hash[:16]}…)"
                    ),
                    details={
                        "source": "inbound_edge",
                        "vendor": ctx.principal.vendor,
                        "client_id": ctx.principal.client_id,
                        "jti": ctx.principal.jti,
                        "tool_name": ctx.tool,
                        "target": ctx.target,
                        "p0_score": ctx.p0_score,
                        "args_sha256": args_hash,
                        "args": {k: v for k, v in ctx.args.items() if k != "approval_ticket"},
                        "risk_tier": "critical",
                    },
                    agent_id=ctx.principal.principal_id,
                ),
                policy=policy,
            )
            request_id = item.request_id
            await self._store.put_approval(
                request_id, idem, ctx.principal.principal_id, ctx.tool, args_hash, expires_ts
            )
            if self._notifier is not None:
                text, markup = render_card(ctx, request_id, args_hash, _iso(expires_ts))
                try:
                    await self._notifier(text, markup)
                except Exception as exc:  # the queue item stands; the SOC tab still shows it
                    logger.error("edge approval card delivery failed: %s", exc)

        ticket = secrets.token_urlsafe(32)
        await self._store.add_ticket(ticket, request_id)
        record = await self._store.approval_for_ticket(ticket)
        assert record is not None
        return PendingApproval(
            request_id=request_id,
            ticket=ticket,
            expires_at=_iso(record["expires_at"]),
            args_sha256=args_hash,
        )

    async def redeem(self, ticket: str, ctx: ApprovalContext) -> None:
        """Authorise exactly one execution, or raise. Never returns on a bad ticket."""
        record = await self._store.approval_for_ticket(ticket)
        if record is None:
            raise ApprovalDenied("unknown approval ticket")
        if record["principal"] != ctx.principal.principal_id:
            raise ApprovalDenied("ticket belongs to a different principal")
        if record["tool"] != ctx.tool:
            raise ApprovalDenied("ticket was issued for a different tool")
        if record["args_sha256"] != args_sha256(ctx.args):
            raise ApprovalDenied("arguments differ from the approved call")
        if record["consumed_at"] is not None:
            raise ApprovalDenied("approval already used")
        if self._clock() >= record["expires_at"]:
            raise ApprovalDenied("approval expired")
        status = await self._status(record["request_id"])
        if status == "pending":
            raise ApprovalPending("awaiting human approval")
        if status != "approved":
            raise ApprovalDenied(f"approval {status}")
        if not await self._store.consume_approval(record["request_id"]):
            raise ApprovalDenied("approval already used")

    async def handle_callback(self, data: str, user_id: str, is_owner: bool) -> str:
        """Telegram inline-button handler. Returns the toast text to show."""
        if not is_owner:
            logger.warning("edge approval callback from non-owner %s ignored", user_id)
            return "Not authorized for approval actions"
        try:
            _, rest = data.split(":", 1)
            request_id, verb = rest.rsplit(":", 1)
        except ValueError:
            return "Invalid approval action"
        if verb not in ("a", "d"):
            return "Invalid approval action"
        approved = verb == "a"
        try:
            await self._queue.decide(
                request_id,
                approved=approved,
                reason="telegram button",
                decided_by=f"telegram:{user_id}",
            )
        except KeyError:
            return "Approval not found or already decided"
        except PermissionError as exc:
            return f"MFA required — decide in the Command Center ({exc})"
        return "✅ Approved" if approved else "❌ Denied"
