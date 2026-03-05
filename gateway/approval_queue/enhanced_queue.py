# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations
import os

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Enhanced Approval Queue for AgentShroud Gateway

Enforce-mode approval queue with SQLite persistence and tool risk tier support.
"""

import asyncio
import logging
import uuid
from datetime import datetime, timedelta, timezone
from typing import Any, Optional

from fastapi import WebSocket

from gateway.ingest_api.config import ApprovalQueueConfig, ToolRiskConfig, ToolRiskPolicy
from gateway.ingest_api.models import ApprovalQueueItem, ApprovalRequest
from gateway.approval_queue.store import ApprovalStore

logger = logging.getLogger("agentshroud.gateway.approval_queue.enhanced")


class EnhancedApprovalQueue:
    """Enhanced approval queue with enforce mode and tool risk tiers.
    
    Features:
    - SQLite persistence via ApprovalStore
    - Tool risk tier-based policies
    - Timeout with auto-deny/auto-approve
    - WebSocket notifications
    - Telegram notifications for critical tier
    - Owner bypass support
    """

    def __init__(
        self, 
        config: ApprovalQueueConfig, 
        tool_risk_config: ToolRiskConfig,
        store: Optional[ApprovalStore] = None
    ):
        """Initialize enhanced approval queue.

        Args:
            config: Basic approval queue configuration
            tool_risk_config: Tool risk tier configuration
            store: Optional ApprovalStore instance (auto-created if None)
        """
        self.config = config
        self.tool_risk_config = tool_risk_config
        import tempfile as _tf; self.store = store or ApprovalStore(os.path.join(os.environ.get("AGENTSHROUD_DATA_DIR", _tf.gettempdir()), "approvals.db"))
        self.connected_clients: set[WebSocket] = set()
        self._lock = asyncio.Lock()
        self._pending_futures: dict[str, asyncio.Future] = {}
        self._timeout_tasks: dict[str, asyncio.Task] = {}
        
        logger.info(
            f"Enhanced approval queue initialized "
            f"(enforce_mode={tool_risk_config.enforce_mode})"
        )

    async def initialize(self):
        """Initialize the store and restore pending items."""
        await self.store.initialize()
        
        # Restore pending items and recreate timeout tasks
        pending_items = await self.store.load_pending()
        for item in pending_items:
            self._pending_futures[item.request_id] = asyncio.Future()
            self._schedule_timeout(item.request_id, item.expires_at)
            
        logger.info(f"Restored {len(pending_items)} pending approval items")

    async def close(self):
        """Close the store and cancel timeout tasks."""
        # Cancel all pending timeout tasks
        for task in self._timeout_tasks.values():
            if not task.done():
                task.cancel()
        
        await self.store.close()

    def get_tool_risk_tier(self, tool_name: str) -> str:
        """Get the risk tier for a tool."""
        return self.tool_risk_config.tool_classifications.get(tool_name, "low")

    def get_policy_for_tier(self, tier: str) -> ToolRiskPolicy:
        """Get the policy for a risk tier."""
        return getattr(self.tool_risk_config, tier, self.tool_risk_config.low)

    def requires_approval(self, tool_name: str, agent_id: str = "default") -> bool:
        """Check if a tool requires approval based on risk tier and policy."""
        if not self.tool_risk_config.enforce_mode:
            return False
            
        tier = self.get_tool_risk_tier(tool_name)
        policy = self.get_policy_for_tier(tier)
        
        # Check owner bypass
        if (policy.owner_bypass and 
            self.tool_risk_config.owner_user_id and 
            agent_id == self.tool_risk_config.owner_user_id):
            return False
            
        return policy.require_approval

    async def submit_tool_request(
        self, 
        tool_name: str,
        parameters: dict[str, Any],
        agent_id: str = "default"
    ) -> tuple[str, bool]:
        """Submit a tool call request for approval.
        
        Returns:
            (request_id, requires_wait) - If requires_wait is False, tool can proceed immediately
        """
        if not self.requires_approval(tool_name, agent_id):
            return "", False
            
        tier = self.get_tool_risk_tier(tool_name) 
        policy = self.get_policy_for_tier(tier)
        
        # Create approval request
        request = ApprovalRequest(
            action_type=f"tool_call_{tier}",
            description=f"Execute {tier}-tier tool: {tool_name}",
            details={
                "tool_name": tool_name,
                "parameters": parameters,
                "risk_tier": tier,
            },
            agent_id=agent_id,
        )
        
        item = await self.submit(request, policy)
        return item.request_id, True

    async def submit(
        self, 
        request: ApprovalRequest, 
        policy: Optional[ToolRiskPolicy] = None
    ) -> ApprovalQueueItem:
        """Add an action to the approval queue with policy-based timeout."""
        async with self._lock:
            # Generate ID and timestamps
            request_id = str(uuid.uuid4())
            now = datetime.now(timezone.utc)
            submitted_at = now.isoformat().replace("+00:00", "Z")
            
            # Use policy timeout if provided, otherwise use default config
            timeout_seconds = policy.timeout_seconds if policy else self.config.timeout_seconds
            expires_at = (
                (now + timedelta(seconds=timeout_seconds))
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

            # Save to store
            await self.store.save(item)
            
            # Create future for waiting
            self._pending_futures[request_id] = asyncio.Future()
            
            # Schedule timeout
            self._schedule_timeout(request_id, expires_at, policy)

            logger.info(
                f"Approval request submitted: {request_id} "
                f"({request.action_type} from {request.agent_id}) "
                f"timeout={timeout_seconds}s"
            )

            # Broadcast to WebSocket clients
            await self.broadcast({
                "type": "new_request", 
                "data": {
                    **item.model_dump(),
                    "risk_tier": request.details.get("risk_tier", "unknown"),
                    "tool_name": request.details.get("tool_name", "unknown"),
                }
            })
            
            # Send Telegram notification for critical tier
            if policy and "telegram_admin" in policy.notify_channels:
                await self._notify_telegram(item, request.details.get("risk_tier", "unknown"))

            return item

    def _schedule_timeout(self, request_id: str, expires_at: str, policy: Optional[ToolRiskPolicy] = None):
        """Schedule a timeout task for a request."""
        expires_dt = datetime.fromisoformat(expires_at.replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)
        delay = max(0, (expires_dt - now).total_seconds())
        
        timeout_action = policy.timeout_action if policy else "deny"
        
        async def timeout_handler():
            await asyncio.sleep(delay)
            await self._timeout_request(request_id, timeout_action)
        
        self._timeout_tasks[request_id] = asyncio.create_task(timeout_handler())

    async def _timeout_request(self, request_id: str, action: str = "deny"):
        """Handle timeout for a pending request."""
        async with self._lock:
            if request_id not in self._pending_futures:
                return  # Already resolved
                
            # Update status in store
            await self.store.update_status(request_id, "expired", f"timeout (action: {action})")
            
            # Resolve future
            future = self._pending_futures.pop(request_id, None)
            if future and not future.done():
                future.set_result(action == "approve")
                
            # Clean up timeout task
            self._timeout_tasks.pop(request_id, None)
            
            logger.info(f"Approval request {request_id} timed out (action: {action})")
            
            # Broadcast timeout
            await self.broadcast({
                "type": "request_expired",
                "data": {
                    "request_id": request_id,
                    "timeout_action": action,
                }
            })

    async def wait_for_decision(self, request_id: str, timeout: float = 300) -> bool:
        """Wait for an approval decision.
        
        Returns:
            True if approved, False if denied/timed out
        """
        future = self._pending_futures.get(request_id)
        if not future:
            # Request doesn't exist or already resolved
            return False
            
        try:
            return await asyncio.wait_for(future, timeout=timeout)
        except asyncio.TimeoutError:
            return False

    async def decide(
        self, request_id: str, approved: bool, reason: str = "", decided_by: str = "admin"
    ) -> ApprovalQueueItem:
        """Process an approval decision."""
        async with self._lock:
            # Check if we have this request
            future = self._pending_futures.get(request_id)
            if not future:
                raise KeyError(f"Approval request {request_id} not found or already decided")
                
            # Update status in store
            status = "approved" if approved else "rejected"
            await self.store.update_status(request_id, status, reason)
            
            # Resolve future
            if not future.done():
                future.set_result(approved)
                
            # Clean up
            self._pending_futures.pop(request_id, None)
            timeout_task = self._timeout_tasks.pop(request_id, None)
            if timeout_task and not timeout_task.done():
                timeout_task.cancel()

            logger.info(
                f"Approval request {request_id} {status} by {decided_by} "
                f"(reason: {reason or 'none'})"
            )

            # Broadcast decision
            await self.broadcast({
                "type": "decision",
                "data": {
                    "request_id": request_id,
                    "status": status,
                    "reason": reason,
                    "decided_by": decided_by,
                }
            })
            
            # Load the updated item to return
            items = await self.store.load_all()
            for item in items:
                if item.request_id == request_id:
                    return item
                    
            raise ValueError(f"Failed to load updated item {request_id}")

    async def get_pending(self) -> list[ApprovalQueueItem]:
        """Get all pending approval items."""
        return await self.store.load_pending()

    async def get_item(self, request_id: str) -> ApprovalQueueItem | None:
        """Fetch a single queue item by ID."""
        items = await self.store.load_all()
        for item in items:
            if item.request_id == request_id:
                return item
        return None

    async def _notify_telegram(self, item: ApprovalQueueItem, risk_tier: str):
        """Send Telegram notification for approval requests."""
        # TODO: Implement Telegram notification
        # For now, just log that we would send a notification
        logger.info(
            f"Would send Telegram notification for {risk_tier} approval: "
            f"{item.request_id} - {item.description}"
        )

    # === WebSocket Management ===

    async def connect(self, websocket: WebSocket) -> None:
        """Accept a WebSocket connection and add to connected set."""
        await websocket.accept()
        self.connected_clients.add(websocket)
        logger.info(f"WebSocket client connected (total: {len(self.connected_clients)})")

    async def disconnect(self, websocket: WebSocket) -> None:
        """Remove a WebSocket connection from connected set."""
        self.connected_clients.discard(websocket)
        logger.info(f"WebSocket client disconnected (remaining: {len(self.connected_clients)})")

    async def broadcast(self, message: dict[str, Any]) -> None:
        """Send a JSON message to all connected WebSocket clients."""
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