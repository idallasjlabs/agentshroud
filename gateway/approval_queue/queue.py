# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Approval Queue for AgentShroud Gateway

In-memory queue for agent actions requiring human approval.
WebSocket broadcast for real-time notifications.
"""


import asyncio
import logging
import os
import json
import uuid
from datetime import datetime, timedelta
from typing import Any

from fastapi import WebSocket

from ..ingest_api.config import ApprovalQueueConfig
from ..ingest_api.models import ApprovalQueueItem, ApprovalRequest

logger = logging.getLogger("agentshroud.gateway.approval_queue")


class ApprovalQueue:
    """In-memory approval queue with WebSocket notifications

    Actions requiring approval:
    - email_sending
    - file_deletion
    - external_api_calls
    - skill_installation
    """

    def __init__(self, config: ApprovalQueueConfig):
        """Initialize approval queue

        Args:
            config: Approval queue configuration
        """
        self.config = config
        self.pending: dict[str, ApprovalQueueItem] = {}
        self.connected_clients: set[WebSocket] = set()
        self._lock = asyncio.Lock()
        self._audit_path = os.environ.get(
            "AGENTSHROUD_APPROVAL_AUDIT_PATH",
            "/app/data/approval_queue_history.jsonl",
        )

        logger.info(
            f"Approval queue initialized (timeout={config.timeout_seconds}s, "
            f"enabled={config.enabled})"
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

            # Broadcast to WebSocket clients
            await self.broadcast({"type": "new_request", "data": item.model_dump()})

            return item

    async def decide(
        self, request_id: str, approved: bool, reason: str = ""
    ) -> ApprovalQueueItem:
        """Process an approval decision

        Args:
            request_id: Request UUID
            approved: Whether to approve or reject
            reason: Optional reason for decision

        Returns:
            Updated ApprovalQueueItem

        Raises:
            KeyError: If request_id not found
            ValueError: If request already decided or expired
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

            # Update status
            item.status = "approved" if approved else "rejected"

            logger.info(
                f"Approval request {request_id} {item.status} "
                f"(reason: {reason or 'none'})"
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

            # Broadcast decision
            await self.broadcast(
                {
                    "type": "decision",
                    "data": {
                        "request_id": request_id,
                        "status": item.status,
                        "reason": reason,
                    },
                }
            )

            # Remove from pending after a delay (keep for audit)
            # For now, just keep in memory until cleanup
            # TODO: Consider persisting approved/rejected items

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
        logger.info(
            f"WebSocket client connected (total: {len(self.connected_clients)})"
        )

    async def disconnect(self, websocket: WebSocket) -> None:
        """Remove a WebSocket connection from connected set

        Args:
            websocket: WebSocket connection
        """
        self.connected_clients.discard(websocket)
        logger.info(
            f"WebSocket client disconnected (remaining: {len(self.connected_clients)})"
        )

    async def broadcast(self, message: dict[str, Any]) -> None:
        """Send a JSON message to all connected WebSocket clients

        Silently removes clients that have disconnected.

        Args:
            message: Dictionary to send as JSON
        """
        disconnected = set()

        for client in self.connected_clients:
            try:
                await client.send_json(message)
            except Exception as e:
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
