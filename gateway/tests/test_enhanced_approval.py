# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for Enhanced Approval Queue with Tool Risk Tiers"""

from __future__ import annotations

import asyncio
import tempfile

import pytest
import pytest_asyncio

from gateway.approval_queue.enhanced_queue import EnhancedApprovalQueue
from gateway.approval_queue.store import ApprovalStore
from gateway.ingest_api.config import (
    ApprovalQueueConfig,
    ToolRiskConfig,
    ToolRiskPolicy,
)
from gateway.ingest_api.models import ApprovalRequest
from gateway.proxy.mcp_proxy import MCPProxy, MCPToolCall


@pytest_asyncio.fixture
async def temp_store():
    """Create a temporary SQLite store for testing."""
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
        store = ApprovalStore(f.name)
        await store.initialize()
        yield store
        try:
            await asyncio.wait_for(store.close(), timeout=2)
        except (asyncio.TimeoutError, Exception):
            pass


@pytest.fixture
def tool_risk_config():
    """Create a test tool risk configuration."""
    return ToolRiskConfig(
        enforce_mode=True,
        monitor_only_mode=False,
        owner_user_id="test_owner",
        critical=ToolRiskPolicy(
            require_approval=True,
            timeout_seconds=300,
            timeout_action="deny",
            notify_channels=["websocket", "telegram_admin"],
            owner_bypass=False,
        ),
        high=ToolRiskPolicy(
            require_approval=True,
            timeout_seconds=300,
            timeout_action="deny",
            notify_channels=["websocket"],
            owner_bypass=True,
        ),
        medium=ToolRiskPolicy(
            require_approval=False,
            timeout_seconds=300,
            timeout_action="deny",
            notify_channels=["websocket"],
            owner_bypass=True,
        ),
        low=ToolRiskPolicy(
            require_approval=False,
            timeout_seconds=300,
            timeout_action="deny",
            notify_channels=["websocket"],
            owner_bypass=True,
        ),
        tool_classifications={
            "exec": "critical",
            "cron": "critical",
            "sessions_send": "critical",
            "nodes": "high",
            "browser": "high",
            "apply_patch": "high",
            "subagents": "high",
            "grep": "medium",
            "find": "medium",
            "sessions_list": "medium",
            "sessions_history": "medium",
            "session_status": "medium",
            "ls": "low",
            "canvas": "low",
            "process": "low",
        },
    )


@pytest_asyncio.fixture
async def enhanced_queue(temp_store, tool_risk_config):
    """Create an enhanced approval queue for testing."""
    config = ApprovalQueueConfig(enabled=True, timeout_seconds=300)
    queue = EnhancedApprovalQueue(config, tool_risk_config, temp_store)
    await queue.initialize()
    yield queue
    await queue.close()


class TestToolRiskClassification:
    """Test tool risk tier classification."""

    @pytest.mark.asyncio
    async def test_get_tool_risk_tier(self, enhanced_queue):
        """Test risk tier lookup."""
        assert enhanced_queue.get_tool_risk_tier("exec") == "critical"
        assert enhanced_queue.get_tool_risk_tier("nodes") == "high"
        assert enhanced_queue.get_tool_risk_tier("grep") == "medium"
        assert enhanced_queue.get_tool_risk_tier("ls") == "low"
        assert enhanced_queue.get_tool_risk_tier("unknown_tool") == "low"

    @pytest.mark.asyncio
    async def test_requires_approval(self, enhanced_queue):
        """Test approval requirement logic."""
        # Critical tools always require approval
        assert enhanced_queue.requires_approval("exec")
        assert enhanced_queue.requires_approval("cron")

        # High tools require approval except with owner bypass
        assert enhanced_queue.requires_approval("nodes")
        assert not enhanced_queue.requires_approval("nodes", "test_owner")

        # Medium/low don't require approval
        assert not enhanced_queue.requires_approval("grep")
        assert not enhanced_queue.requires_approval("ls")

    @pytest.mark.asyncio
    async def test_enforce_mode_disabled(self, tool_risk_config, temp_store):
        """Test that approval is bypassed when enforce mode is disabled."""
        tool_risk_config.enforce_mode = False
        config = ApprovalQueueConfig(enabled=True)
        queue = EnhancedApprovalQueue(config, tool_risk_config, temp_store)

        # Should not require approval even for critical tools
        assert not queue.requires_approval("exec")
        assert not queue.requires_approval("cron")


class TestApprovalWorkflow:
    """Test the complete approval workflow."""

    @pytest.mark.asyncio
    async def test_critical_tool_approval_flow(self, enhanced_queue):
        """Test full approval flow for critical tool."""
        # Submit tool request
        request_id, requires_wait = await enhanced_queue.submit_tool_request(
            "exec", {"command": "ls -la"}, "test_agent"
        )

        assert requires_wait
        assert request_id != ""

        # Check pending items
        pending = await enhanced_queue.get_pending()
        assert len(pending) == 1
        assert pending[0].request_id == request_id
        assert pending[0].details["tool_name"] == "exec"
        assert pending[0].details["risk_tier"] == "critical"

        # Approve the request
        item = await enhanced_queue.decide(request_id, True, "Test approval")
        assert item.status == "approved"

        # Should no longer be pending
        pending = await enhanced_queue.get_pending()
        assert len(pending) == 0

    @pytest.mark.asyncio
    @pytest.mark.asyncio
    async def test_critical_tool_denial_flow(self, enhanced_queue):
        """Test denial flow for critical tool."""
        request_id, requires_wait = await enhanced_queue.submit_tool_request(
            "cron", {"schedule": "0 */6 * * *", "command": "backup.sh"}, "test_agent"
        )

        assert requires_wait

        # Deny the request
        item = await enhanced_queue.decide(request_id, False, "Security risk")
        assert item.status == "rejected"

    @pytest.mark.asyncio
    @pytest.mark.asyncio
    async def test_timeout_auto_deny(self, enhanced_queue):
        """Test timeout with auto-deny."""
        # Submit request with very short timeout
        tier = enhanced_queue.get_tool_risk_tier("exec")
        policy = enhanced_queue.get_policy_for_tier(tier)
        policy.timeout_seconds = 1  # 1 second timeout

        request = ApprovalRequest(
            action_type="tool_call_critical",
            description="Execute critical-tier tool: exec",
            details={
                "tool_name": "exec",
                "parameters": {"command": "rm -rf /"},
                "risk_tier": "critical",
            },
            agent_id="test_agent",
        )

        item = await enhanced_queue.submit(request, policy)

        # Wait longer than timeout to let asyncio task fire
        await asyncio.sleep(1.5)

        # Check if expired
        updated_item = await enhanced_queue.get_item(item.request_id)
        assert updated_item.status == "expired"

    @pytest.mark.asyncio
    async def test_wait_for_decision(self, enhanced_queue):
        """Test waiting for approval decision."""
        request_id, requires_wait = await enhanced_queue.submit_tool_request(
            "exec", {"command": "whoami"}, "test_agent"
        )

        # Start waiting in background
        async def approve_after_delay():
            await asyncio.sleep(0.1)
            await enhanced_queue.decide(request_id, True, "Approved after delay")

        task = asyncio.create_task(approve_after_delay())

        # Wait for decision
        approved = await enhanced_queue.wait_for_decision(request_id, timeout=1.0)
        assert approved

        await task

    @pytest.mark.asyncio
    @pytest.mark.asyncio
    async def test_low_risk_tool_no_approval(self, enhanced_queue):
        """Test that low-risk tools don't require approval."""
        request_id, requires_wait = await enhanced_queue.submit_tool_request(
            "ls", {"path": "/tmp"}, "test_agent"
        )

        assert not requires_wait
        assert request_id == ""

        # No pending items should exist
        pending = await enhanced_queue.get_pending()
        assert len(pending) == 0


class TestMCPProxyIntegration:
    """Test MCP proxy integration with approval queue."""

    @pytest.fixture
    def mcp_proxy_with_approval(self, enhanced_queue):
        """Create an MCP proxy with approval queue."""
        proxy = MCPProxy(approval_queue=enhanced_queue)
        yield proxy

    @pytest.mark.asyncio
    async def test_critical_tool_requires_approval(self, mcp_proxy_with_approval):
        """Test that critical tools are identified as requiring approval."""
        # Verify the approval queue correctly classifies critical tools
        queue = mcp_proxy_with_approval.approval_queue
        tier = queue.get_tool_risk_tier("exec")
        assert tier == "critical"
        assert queue.requires_approval("exec")

        # Submit and verify it creates a pending request
        request_id, requires_wait = await queue.submit_tool_request(
            "exec", {"command": "cat /etc/passwd"}, "test_agent"
        )
        assert requires_wait

        # Verify pending
        pending = await queue.get_pending()
        assert len(pending) >= 1
        assert any(p.request_id == request_id for p in pending)

    @pytest.mark.asyncio
    @pytest.mark.asyncio
    async def test_low_risk_tool_allowed(self, mcp_proxy_with_approval):
        """Test that low-risk tools are allowed without approval."""
        tool_call = MCPToolCall(
            id="test-1",
            server_name="test_server",
            tool_name="ls",
            parameters={"path": "/tmp"},
            agent_id="test_agent",
        )

        result = await mcp_proxy_with_approval.process_tool_call(tool_call, execute=False)

        # Should be allowed
        assert result.allowed
        assert not result.blocked

    @pytest.mark.asyncio
    @pytest.mark.asyncio
    async def test_owner_bypass(self, mcp_proxy_with_approval):
        """Test owner bypass for high-tier tools."""
        tool_call = MCPToolCall(
            id="test-1",
            server_name="test_server",
            tool_name="nodes",  # High tier tool with owner bypass
            parameters={"action": "list"},
            agent_id="test_owner",  # Owner agent ID
        )

        result = await mcp_proxy_with_approval.process_tool_call(tool_call, execute=False)

        # Should be allowed due to owner bypass
        assert result.allowed
        assert not result.blocked


class TestPersistence:
    """Test SQLite persistence across restarts."""

    @pytest.mark.asyncio
    async def test_restore_pending_items(self, tool_risk_config):
        """Test that pending items are restored after restart."""
        with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
            store_path = f.name

        # Create first queue instance and submit request
        config = ApprovalQueueConfig(enabled=True)
        store1 = ApprovalStore(store_path)
        await store1.initialize()

        queue1 = EnhancedApprovalQueue(config, tool_risk_config, store1)
        await queue1.initialize()

        request_id, requires_wait = await queue1.submit_tool_request(
            "exec", {"command": "test"}, "test_agent"
        )

        assert requires_wait
        pending1 = await queue1.get_pending()
        assert len(pending1) == 1

        await queue1.close()

        # Create second queue instance (simulating restart)
        store2 = ApprovalStore(store_path)
        await store2.initialize()

        queue2 = EnhancedApprovalQueue(config, tool_risk_config, store2)
        await queue2.initialize()

        # Should restore pending items
        pending2 = await queue2.get_pending()
        assert len(pending2) == 1
        assert pending2[0].request_id == request_id

        await queue2.close()

    @pytest.mark.asyncio
    async def test_restart_recovery_preserves_timeout_action(self):
        """SCRUM-110: restart recovery must reschedule the timeout with the
        item's ORIGINAL policy timeout_action, not silently fall back to the
        hardcoded 'deny' default used when no policy is threaded through.

        Uses timeout_action="approve" specifically because "deny" is
        indistinguishable from the pre-fix bug's hardcoded fallback — a test
        using "deny" would pass even with the recovery bug present.
        """
        with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
            store_path = f.name

        config = ApprovalQueueConfig(enabled=True)
        approve_on_timeout_config = ToolRiskConfig(
            enforce_mode=True,
            monitor_only_mode=False,
            owner_user_id="test_owner",
            critical=ToolRiskPolicy(
                require_approval=True,
                timeout_seconds=1,
                timeout_action="approve",
                notify_channels=["websocket"],
                owner_bypass=False,
            ),
            high=ToolRiskPolicy(
                require_approval=False,
                timeout_seconds=300,
                timeout_action="deny",
                notify_channels=["websocket"],
                owner_bypass=True,
            ),
            medium=ToolRiskPolicy(
                require_approval=False,
                timeout_seconds=300,
                timeout_action="deny",
                notify_channels=["websocket"],
                owner_bypass=True,
            ),
            low=ToolRiskPolicy(
                require_approval=False,
                timeout_seconds=300,
                timeout_action="deny",
                notify_channels=["websocket"],
                owner_bypass=True,
            ),
            tool_classifications={"exec": "critical"},
        )

        store1 = ApprovalStore(store_path)
        await store1.initialize()
        queue1 = EnhancedApprovalQueue(config, approve_on_timeout_config, store1)
        await queue1.initialize()

        request_id, requires_wait = await queue1.submit_tool_request(
            "exec", {"command": "test"}, "test_agent"
        )
        assert requires_wait

        # Persisted details must carry the timeout_action forward.
        item = await queue1.get_item(request_id)
        assert item.details.get("_timeout_action") == "approve"

        # Cancel queue1's own in-memory timeout task so it cannot resolve the
        # request itself — only the restart-recovered schedule on queue2 may.
        task = queue1._timeout_tasks.pop(request_id, None)
        if task:
            task.cancel()
        await queue1.close()

        # Simulate restart: a fresh queue instance recovers pending items and
        # reschedules their timeouts from persisted state alone.
        store2 = ApprovalStore(store_path)
        await store2.initialize()
        queue2 = EnhancedApprovalQueue(config, approve_on_timeout_config, store2)
        await queue2.initialize()

        future = queue2._pending_futures[request_id]
        result = await asyncio.wait_for(future, timeout=5)

        # If recovery dropped timeout_action (pre-fix bug), _schedule_timeout's
        # unconditional "deny" default would resolve this False instead.
        assert result is True

        await queue2.close()


@pytest.mark.asyncio
@pytest.mark.asyncio
async def test_websocket_notifications():
    """Test that approval events are generated for WebSocket notification."""
    import tempfile

    store = ApprovalStore(tempfile.mktemp(suffix=".db"))
    await store.initialize()

    config = ToolRiskConfig()
    queue = EnhancedApprovalQueue(
        store=store, config=ApprovalQueueConfig(enforce_mode=True), tool_risk_config=config
    )

    # Submit a critical request — should generate notification event
    request_id, requires_wait = await queue.submit_tool_request(
        "exec", {"command": "test"}, "test_agent"
    )
    assert requires_wait

    # Verify the item exists and has notification metadata
    item = await queue.get_item(request_id)
    assert item is not None
    assert item.status == "pending"

    try:
        import asyncio as _aio

        await _aio.wait_for(store.close(), timeout=1.0)
    except Exception:
        pass


class _HangingWebSocket:
    """A WebSocket stand-in whose send_json never returns.

    Models a real-world dead client — laptop closed, VPN blip, backgrounded
    tab — that stops reading without a clean TCP close, so the OS-level send
    buffer fills and the write blocks forever.
    """

    async def send_json(self, message: dict) -> None:
        await asyncio.Event().wait()  # never set — hangs until cancelled


@pytest.mark.asyncio
async def test_submit_does_not_deadlock_on_hung_websocket_client():
    """SCRUM-154: a dead WebSocket client must never wedge the approval lock.

    submit()/decide()/_timeout_request() broadcast to connected SOC/dashboard
    clients while holding self._lock. Before the fix, a single client whose
    send_json() never returns (dead socket, full send buffer) held the lock
    forever, blocking every future submit()/decide()/_timeout_request() call
    — i.e. every approval-gated action from either bot, indefinitely, with
    no exception ever raised and no CPU/memory pressure to signal the hang.
    """
    import tempfile

    store = ApprovalStore(tempfile.mktemp(suffix=".db"))
    await store.initialize()

    config = ToolRiskConfig()
    queue = EnhancedApprovalQueue(
        store=store, config=ApprovalQueueConfig(enforce_mode=True), tool_risk_config=config
    )
    queue.connected_clients.add(_HangingWebSocket())

    try:
        request_id, requires_wait = await asyncio.wait_for(
            queue.submit_tool_request("exec", {"command": "test"}, "test_agent"),
            timeout=3.0,
        )
    except asyncio.TimeoutError:
        pytest.fail(
            "submit() deadlocked with a hung WebSocket client still holding "
            "the approval lock — SCRUM-154 regression"
        )
    assert requires_wait
    assert request_id

    # decide() must also not deadlock with the same hung client still attached.
    try:
        await asyncio.wait_for(
            queue.decide(request_id, approved=True, decided_by="test"),
            timeout=3.0,
        )
    except asyncio.TimeoutError:
        pytest.fail(
            "decide() deadlocked with a hung WebSocket client still holding "
            "the approval lock — SCRUM-154 regression"
        )

    try:
        await asyncio.wait_for(store.close(), timeout=1.0)
    except Exception:
        pass


@pytest.mark.asyncio
async def test_broadcast_does_not_hang_forever_on_dead_client():
    """broadcast() itself must bound its wait per-client, not just rely on
    callers moving it off the lock — defense in depth so an orphaned
    fire-and-forget broadcast task can't accumulate forever either."""
    import tempfile

    store = ApprovalStore(tempfile.mktemp(suffix=".db"))
    await store.initialize()

    config = ToolRiskConfig()
    queue = EnhancedApprovalQueue(
        store=store, config=ApprovalQueueConfig(enforce_mode=True), tool_risk_config=config
    )
    queue.connected_clients.add(_HangingWebSocket())

    # broadcast()'s own per-client bound is 5s; give the outer wait headroom
    # above that so this only fails if broadcast() itself hangs indefinitely,
    # not merely takes as long as its documented per-client timeout.
    try:
        await asyncio.wait_for(queue.broadcast({"type": "test", "data": {}}), timeout=8.0)
    except asyncio.TimeoutError:
        pytest.fail("broadcast() hung indefinitely on a dead client — SCRUM-154 regression")

    try:
        await asyncio.wait_for(store.close(), timeout=1.0)
    except Exception:
        pass
