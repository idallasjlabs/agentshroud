# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Approval Queue for AgentShroud Gateway

In-memory queue for agent actions requiring human approval.
WebSocket broadcast for real-time notifications.
"""


import asyncio
import json
import logging
import os
import uuid
from datetime import datetime, timedelta
from typing import Any

from fastapi import WebSocket

from ..ingest_api.config import ApprovalQueueConfig
from ..ingest_api.models import ApprovalQueueItem, ApprovalRequest
from ..security.mfa_guard import MFAGuard

logger = logging.getLogger("agentshroud.gateway.approval_queue")


class ApprovalQueue:
    """In-memory approval queue with WebSocket notifications

    Actions requiring approval:
    - email_sending
    - file_deletion
    - external_api_calls
    - skill_installation
    """

    def __init__(self, config: ApprovalQueueConfig, mfa_guard: MFAGuard | None = None):
        """Initialize approval queue

        Args:
            config: Approval queue configuration
            mfa_guard: Optional MFAGuard for second-factor enforcement on
                high-risk approvals (IEC 62443 FR1). Defaults to one built from
                the environment (disabled unless AGENTSHROUD_MFA_ENABLED is set),
                so existing deployments are unchanged.
        """
        self.config = config
        self.mfa_guard = mfa_guard if mfa_guard is not None else MFAGuard.from_env()
        self.pending: dict[str, ApprovalQueueItem] = {}
        self.connected_clients: set[WebSocket] = set()
        self._lock = asyncio.Lock()
        self._audit_path = os.environ.get(
            "AGENTSHROUD_APPROVAL_AUDIT_PATH",
            "/app/data/approval_queue_history.jsonl",
        )
        self._store_path = os.environ.get(
            "AGENTSHROUD_APPROVAL_STORE_PATH",
            "/app/data/approval_queue_store.json",
        )
        self._load_pending_store()

        logger.info(
            f"Approval queue initialized (timeout={config.timeout_seconds}s, "
            f"enabled={config.enabled}, mfa={self.mfa_guard.enabled})"
        )

    async def submit(self, request: ApprovalRequest) -> ApprovalQueueItem:
        """Add an action to the approval queue

        Args:
            request: Approval request from agent

        Returns:
            ApprovalQueueItem with request details
        """
        async with self._lock:
            # Generate ID and timestamps
            from datetime import timezone

            request_id = str(uuid.uuid4())
            now = datetime.now(timezone.utc)
            submitted_at = now.isoformat().replace("+00:00", "Z")
            expires_at = (
                (now + timedelta(seconds=self.config.timeout_seconds))
                .isoformat()
                .replace("+00:00", "Z")
            )

            # Create queue item
            item = ApprovalQueueItem(
                request_id=request_id,
                action_type=request.action_type,
                description=request.description,
                details=request.details,
                agent_id=request.agent_id,
                submitted_at=submitted_at,
                expires_at=expires_at,
                status="pending",
            )

            # Add to pending
            self.pending[request_id] = item
            self._persist_pending_store()

            logger.info(
                f"Approval request submitted: {request_id} "
                f"({request.action_type} from {request.agent_id})"
            )
            self._append_audit_event(
                {
                    "event": "submitted",
                    "request_id": request_id,
                    "action_type": request.action_type,
                    "agent_id": request.agent_id,
                    "submitted_at": submitted_at,
                    "expires_at": expires_at,
                    "status": item.status,
                }
            )

            # Broadcast to WebSocket clients. SCRUM-154: create_task, not
            # await — we're still holding self._lock here, matching the
            # pattern already used by _expire_stale below (a dead client's
            # send() must never wedge every future queue call).
            asyncio.create_task(self.broadcast({"type": "new_request", "data": item.model_dump()}))

            return item

    async def decide(
        self,
        request_id: str,
        approved: bool,
        reason: str = "",
        mfa_code: str | None = None,
    ) -> ApprovalQueueItem:
        """Process an approval decision

        Args:
            request_id: Request UUID
            approved: Whether to approve or reject
            reason: Optional reason for decision
            mfa_code: Second-factor (TOTP) code supplied by the owner. Required
                to APPROVE a high-risk action when MFA is enabled
                (IEC 62443 FR1). Ignored when rejecting or when MFA is disabled.

        Returns:
            Updated ApprovalQueueItem

        Raises:
            KeyError: If request_id not found
            ValueError: If request already decided or expired
            PermissionError: If MFA is required to approve this action and the
                second factor is missing / invalid / replayed (fail-closed).
        """
        async with self._lock:
            if request_id not in self.pending:
                raise KeyError(f"Approval request {request_id} not found")

            item = self.pending[request_id]

            # Check if already decided
            if item.status in ["approved", "rejected", "expired"]:
                raise ValueError(f"Approval request {request_id} already {item.status}")

            # Check if expired
            expires_dt = datetime.fromisoformat(item.expires_at.replace("Z", "+00:00"))
            if datetime.now(expires_dt.tzinfo) > expires_dt:
                item.status = "expired"
                raise ValueError(f"Approval request {request_id} has expired")

            # IEC 62443 FR1 — second factor for high-risk APPROVALS (fail-closed).
            # Only approvals of high-risk actions are gated; rejections always
            # proceed so the owner can always decline. Disabled by default.
            if approved and self.mfa_guard.is_required(item.action_type):
                mfa = self.mfa_guard.verify(action_type=item.action_type, code=mfa_code)
                if not mfa.allowed:
                    logger.warning(
                        "Approval %s DENIED second factor (%s) for action_type=%s",
                        request_id,
                        mfa.reason,
                        item.action_type,
                    )
                    self._append_audit_event(
                        {
                            "event": "mfa_denied",
                            "request_id": request_id,
                            "action_type": item.action_type,
                            "agent_id": item.agent_id,
                            "reason": mfa.reason,
                        }
                    )
                    raise PermissionError(f"MFA required to approve: {mfa.reason}")

            # Update status
            item.status = "approved" if approved else "rejected"
            self._persist_pending_store()

            logger.info(
                f"Approval request {request_id} {item.status} " f"(reason: {reason or 'none'})"
            )
            self._append_audit_event(
                {
                    "event": "decided",
                    "request_id": request_id,
                    "action_type": item.action_type,
                    "agent_id": item.agent_id,
                    "status": item.status,
                    "reason": reason,
                }
            )

            # Broadcast decision. SCRUM-154: create_task, not await — see
            # submit()'s broadcast for why (still holding self._lock here).
            asyncio.create_task(
                self.broadcast(
                    {
                        "type": "decision",
                        "data": {
                            "request_id": request_id,
                            "status": item.status,
                            "reason": reason,
                        },
                    }
                )
            )

            # Decided items remain in self.pending for in-session lookups and are
            # persisted to the JSON store via _persist_pending_store(). Call
            # cleanup_decided() periodically to prune old decided items from memory.

            return item

    async def get_pending(self) -> list[ApprovalQueueItem]:
        """Get all pending (not expired, not decided) items

        First expires any stale items.

        Returns:
            List of pending approval items
        """
        async with self._lock:
            # Expire stale items first
            await self._expire_stale()

            # Return pending items
            return [item for item in self.pending.values() if item.status == "pending"]

    async def get_item(self, request_id: str) -> ApprovalQueueItem | None:
        """Fetch a single queue item by ID

        Args:
            request_id: Request UUID

        Returns:
            ApprovalQueueItem if found, None otherwise
        """
        async with self._lock:
            return self.pending.get(request_id)

    async def cleanup_decided(self, max_age_seconds: int = 3600) -> int:
        """Remove decided (approved/rejected/expired) items older than max_age_seconds.

        Decided items are already persisted to the JSON store and audit log.
        This method only prunes the in-memory dict to prevent unbounded growth
        in long-running processes.

        Args:
            max_age_seconds: Items decided longer ago than this are removed.

        Returns:
            Number of items removed.
        """
        from datetime import timezone

        cutoff = datetime.now(timezone.utc) - timedelta(seconds=max_age_seconds)
        decided_statuses = {"approved", "rejected", "expired"}
        to_remove = []

        async with self._lock:
            for request_id, item in self.pending.items():
                if item.status not in decided_statuses:
                    continue
                try:
                    submitted = datetime.fromisoformat(item.submitted_at.replace("Z", "+00:00"))
                    if submitted < cutoff:
                        to_remove.append(request_id)
                except (ValueError, AttributeError):
                    to_remove.append(request_id)

            for request_id in to_remove:
                del self.pending[request_id]
            if to_remove:
                self._persist_pending_store()

        if to_remove:
            logger.info("Approval queue cleanup removed %d decided item(s)", len(to_remove))
        return len(to_remove)

    async def _expire_stale(self) -> list[str]:
        """Check all pending items and expire those past timeout

        Returns:
            List of expired request IDs
        """
        # NOTE: Called within _lock context
        from datetime import timezone

        now = datetime.now(timezone.utc)
        expired_ids = []

        for request_id, item in self.pending.items():
            if item.status != "pending":
                continue

            expires_dt = datetime.fromisoformat(item.expires_at.replace("Z", "+00:00"))
            if now > expires_dt:
                item.status = "expired"
                expired_ids.append(request_id)
                self._persist_pending_store()

                logger.info(f"Approval request {request_id} expired")
                self._append_audit_event(
                    {
                        "event": "expired",
                        "request_id": request_id,
                        "action_type": item.action_type,
                        "agent_id": item.agent_id,
                        "status": item.status,
                    }
                )

                # Broadcast expiry (don't await - already in lock)
                asyncio.create_task(
                    self.broadcast(
                        {
                            "type": "request_expired",
                            "data": {"request_id": request_id},
                        }
                    )
                )

        return expired_ids

    # === WebSocket Management ===

    async def connect(self, websocket: WebSocket) -> None:
        """Accept a WebSocket connection and add to connected set

        Args:
            websocket: WebSocket connection
        """
        await websocket.accept()
        self.connected_clients.add(websocket)
        logger.info(f"WebSocket client connected (total: {len(self.connected_clients)})")

    async def disconnect(self, websocket: WebSocket) -> None:
        """Remove a WebSocket connection from connected set

        Args:
            websocket: WebSocket connection
        """
        self.connected_clients.discard(websocket)
        logger.info(f"WebSocket client disconnected (remaining: {len(self.connected_clients)})")

    async def broadcast(self, message: dict[str, Any]) -> None:
        """Send a JSON message to all connected WebSocket clients

        Silently removes clients that have disconnected.

        SCRUM-154: bounds each client's send with a timeout so a single dead
        client (closed laptop, VPN blip, backgrounded tab) can never hang
        this call indefinitely — callers that fire this off via
        asyncio.create_task while holding self._lock still depend on it
        eventually returning.

        Args:
            message: Dictionary to send as JSON
        """
        disconnected = set()

        for client in list(self.connected_clients):
            try:
                await asyncio.wait_for(client.send_json(message), timeout=5.0)
            except (Exception, asyncio.TimeoutError) as e:
                logger.warning(f"Failed to send to WebSocket client: {e}")
                disconnected.add(client)

        # Remove disconnected clients
        for client in disconnected:
            self.connected_clients.discard(client)

    def _append_audit_event(self, event: dict[str, Any]) -> None:
        """Best-effort JSONL persistence for queue lifecycle events."""
        try:
            from datetime import timezone

            payload = {
                "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
                **event,
            }
            directory = os.path.dirname(self._audit_path)
            if directory:
                os.makedirs(directory, exist_ok=True)
            with open(self._audit_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(payload, separators=(",", ":")) + "\n")
        except Exception as exc:
            logger.warning("Approval queue audit write failed: %s", exc)

    def _persist_pending_store(self) -> None:
        """Persist queue items to disk for restart durability (best effort).

        Uses atomic write-then-rename so a crash mid-write cannot corrupt
        the store file (os.replace is atomic on POSIX for same-filesystem).
        """
        try:
            directory = os.path.dirname(self._store_path)
            if directory:
                os.makedirs(directory, exist_ok=True)
            payload = {
                "version": 1,
                "items": [item.model_dump() for item in self.pending.values()],
            }
            tmp_path = self._store_path + ".tmp"
            with open(tmp_path, "w", encoding="utf-8") as f:
                json.dump(payload, f, ensure_ascii=False, separators=(",", ":"))
                f.flush()
                os.fsync(f.fileno())
            os.replace(tmp_path, self._store_path)
        except Exception as exc:
            logger.warning("Approval queue store write failed: %s", exc)

    def _load_pending_store(self) -> None:
        """Load queue items from store file when present."""
        try:
            if not os.path.exists(self._store_path):
                return
            with open(self._store_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            items = data.get("items", []) if isinstance(data, dict) else []
            loaded = 0
            for raw in items:
                try:
                    item = ApprovalQueueItem.model_validate(raw)
                    self.pending[item.request_id] = item
                    loaded += 1
                except Exception:
                    continue
            if loaded:
                logger.info("Approval queue restored %d item(s) from store", loaded)
        except Exception as exc:
            logger.warning("Approval queue store load failed: %s", exc)
