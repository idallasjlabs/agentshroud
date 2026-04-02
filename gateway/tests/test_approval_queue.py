# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for approval queue"""

from __future__ import annotations

import asyncio

import pytest

from gateway.approval_queue.queue import ApprovalQueue
from gateway.ingest_api.config import ApprovalQueueConfig
from gateway.ingest_api.models import ApprovalRequest


@pytest.fixture
def queue_config():
    """Create approval queue configuration for testing"""
    return ApprovalQueueConfig(
        enabled=True,
        actions=["email_sending", "file_deletion"],
        timeout_seconds=2,  # Short timeout for testing
    )


@pytest.fixture
def approval_queue(queue_config, tmp_path, monkeypatch):
    """Create approval queue instance for testing"""
    monkeypatch.setenv(
        "AGENTSHROUD_APPROVAL_AUDIT_PATH",
        str(tmp_path / "approval_queue_history.jsonl"),
    )
    monkeypatch.setenv(
        "AGENTSHROUD_APPROVAL_STORE_PATH",
        str(tmp_path / "approval_queue_store.json"),
    )
    return ApprovalQueue(queue_config)


@pytest.mark.asyncio
async def test_submit_approval_request(approval_queue):
    """Test submitting an approval request"""
    request = ApprovalRequest(
        action_type="email_sending",
        description="Send email to test@example.com",
        details={"to": "test@example.com", "subject": "Test"},
        agent_id="test-agent",
    )

    item = await approval_queue.submit(request)

    assert item.request_id is not None
    assert item.action_type == "email_sending"
    assert item.status == "pending"
    assert item.agent_id == "test-agent"


@pytest.mark.asyncio
async def test_decide_approval_approve(approval_queue):
    """Test approving a pending request"""
    request = ApprovalRequest(
        action_type="email_sending",
        description="Test email",
        details={},
    )

    item = await approval_queue.submit(request)

    # Approve it
    updated = await approval_queue.decide(item.request_id, approved=True, reason="OK")

    assert updated.status == "approved"
    assert updated.request_id == item.request_id

    audit_path = approval_queue._audit_path
    with open(audit_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    assert any('"event":"submitted"' in line for line in lines)
    assert any('"event":"decided"' in line and '"status":"approved"' in line for line in lines)


@pytest.mark.asyncio
async def test_decide_approval_reject(approval_queue):
    """Test rejecting a pending request"""
    request = ApprovalRequest(
        action_type="file_deletion",
        description="Delete important file",
        details={},
    )

    item = await approval_queue.submit(request)

    # Reject it
    updated = await approval_queue.decide(item.request_id, approved=False, reason="Too risky")

    assert updated.status == "rejected"


@pytest.mark.asyncio
async def test_decide_nonexistent_request(approval_queue):
    """Test deciding on nonexistent request raises KeyError"""
    with pytest.raises(KeyError):
        await approval_queue.decide("nonexistent-id", approved=True)


@pytest.mark.asyncio
async def test_decide_already_decided(approval_queue):
    """Test deciding on already-decided request raises ValueError"""
    request = ApprovalRequest(
        action_type="email_sending",
        description="Test",
        details={},
    )

    item = await approval_queue.submit(request)

    # Decide once
    await approval_queue.decide(item.request_id, approved=True)

    # Try to decide again
    with pytest.raises(ValueError) as exc:
        await approval_queue.decide(item.request_id, approved=False)

    assert "already approved" in str(exc.value)


@pytest.mark.asyncio
async def test_get_pending(approval_queue):
    """Test getting all pending requests"""
    # Submit multiple requests
    for i in range(3):
        request = ApprovalRequest(
            action_type="email_sending",
            description=f"Request {i}",
            details={},
        )
        await approval_queue.submit(request)

    pending = await approval_queue.get_pending()

    assert len(pending) == 3
    assert all(item.status == "pending" for item in pending)


@pytest.mark.asyncio
async def test_get_pending_excludes_decided(approval_queue):
    """Test that get_pending excludes decided requests"""
    # Submit two requests
    request1 = ApprovalRequest(
        action_type="email_sending",
        description="Request 1",
        details={},
    )
    item1 = await approval_queue.submit(request1)

    request2 = ApprovalRequest(
        action_type="email_sending",
        description="Request 2",
        details={},
    )
    await approval_queue.submit(request2)

    # Decide on first one
    await approval_queue.decide(item1.request_id, approved=True)

    # Get pending should only return second one
    pending = await approval_queue.get_pending()

    assert len(pending) == 1
    assert pending[0].description == "Request 2"


@pytest.mark.asyncio
async def test_request_expiration(approval_queue):
    """Test that requests expire after timeout"""
    request = ApprovalRequest(
        action_type="email_sending",
        description="Test",
        details={},
    )

    await approval_queue.submit(request)

    # Wait for expiration (timeout is 2 seconds)
    await asyncio.sleep(2.5)

    # Get pending should expire stale items
    pending = await approval_queue.get_pending()

    assert len(pending) == 0
    with open(approval_queue._audit_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert '"event":"expired"' in content


@pytest.mark.asyncio
async def test_get_item(approval_queue):
    """Test getting a specific item by ID"""
    request = ApprovalRequest(
        action_type="email_sending",
        description="Test",
        details={},
    )

    item = await approval_queue.submit(request)

    # Retrieve it
    retrieved = await approval_queue.get_item(item.request_id)

    assert retrieved is not None
    assert retrieved.request_id == item.request_id
    assert retrieved.description == "Test"


@pytest.mark.asyncio
async def test_get_item_nonexistent(approval_queue):
    """Test getting nonexistent item returns None"""
    item = await approval_queue.get_item("nonexistent-id")

    assert item is None


@pytest.mark.asyncio
async def test_concurrent_decisions(approval_queue):
    """Test that concurrent decision attempts are handled correctly"""
    request = ApprovalRequest(
        action_type="email_sending",
        description="Test",
        details={},
    )

    item = await approval_queue.submit(request)

    # Try to decide concurrently
    async def decide_approve():
        try:
            await approval_queue.decide(item.request_id, approved=True)
            return "approved"
        except ValueError:
            return "error"

    async def decide_reject():
        try:
            await approval_queue.decide(item.request_id, approved=False)
            return "rejected"
        except ValueError:
            return "error"

    # Run both concurrently
    results = await asyncio.gather(decide_approve(), decide_reject())

    # One should succeed, one should error
    assert "error" in results
    assert "approved" in results or "rejected" in results


@pytest.mark.asyncio
async def test_decide_expired_request(approval_queue):
    """Test deciding on an expired request raises ValueError"""
    request = ApprovalRequest(
        action_type="email_sending",
        description="Test",
        details={},
    )

    item = await approval_queue.submit(request)

    # Wait for expiration (timeout is 2 seconds)
    await asyncio.sleep(2.5)

    # Try to decide on expired request
    with pytest.raises(ValueError, match="expired"):
        await approval_queue.decide(item.request_id, approved=True)


@pytest.mark.asyncio
async def test_websocket_connect(approval_queue):
    """Test WebSocket client connection"""
    from unittest.mock import AsyncMock, MagicMock

    from fastapi import WebSocket

    websocket = MagicMock(spec=WebSocket)
    websocket.accept = AsyncMock()

    await approval_queue.connect(websocket)

    assert websocket in approval_queue.connected_clients
    websocket.accept.assert_called_once()


@pytest.mark.asyncio
async def test_websocket_disconnect(approval_queue):
    """Test WebSocket client disconnection"""
    from unittest.mock import MagicMock

    from fastapi import WebSocket

    websocket = MagicMock(spec=WebSocket)

    # Add client
    approval_queue.connected_clients.add(websocket)

    # Disconnect
    await approval_queue.disconnect(websocket)

    assert websocket not in approval_queue.connected_clients


@pytest.mark.asyncio
async def test_broadcast_with_failed_client(approval_queue):
    """Test broadcast handles failed client sends"""
    from unittest.mock import AsyncMock, MagicMock

    # Add two mock websockets
    ws1 = MagicMock()
    ws1.send_json = AsyncMock()

    ws2 = MagicMock()
    ws2.send_json = AsyncMock(side_effect=Exception("Connection lost"))

    approval_queue.connected_clients.add(ws1)
    approval_queue.connected_clients.add(ws2)

    # Broadcast message
    await approval_queue.broadcast({"type": "test", "data": {}})

    # ws1 should succeed
    ws1.send_json.assert_called_once()

    # ws2 should fail and be removed
    assert ws2 not in approval_queue.connected_clients
    assert ws1 in approval_queue.connected_clients


@pytest.mark.asyncio
async def test_store_persists_submit_and_decision(queue_config, tmp_path, monkeypatch):
    """Queue store file should persist items and status transitions."""
    monkeypatch.setenv("AGENTSHROUD_APPROVAL_AUDIT_PATH", str(tmp_path / "audit.jsonl"))
    store_path = tmp_path / "store.json"
    monkeypatch.setenv("AGENTSHROUD_APPROVAL_STORE_PATH", str(store_path))
    queue = ApprovalQueue(queue_config)

    item = await queue.submit(
        ApprovalRequest(
            action_type="email_sending",
            description="persist me",
            details={},
        )
    )
    assert store_path.exists()
    with open(store_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert '"status":"pending"' in content

    await queue.decide(item.request_id, approved=True)
    with open(store_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert '"status":"approved"' in content


def test_store_restores_items_on_init(queue_config, tmp_path, monkeypatch):
    """Queue should restore persisted items from store file on startup."""
    monkeypatch.setenv("AGENTSHROUD_APPROVAL_AUDIT_PATH", str(tmp_path / "audit.jsonl"))
    store_path = tmp_path / "store.json"
    monkeypatch.setenv("AGENTSHROUD_APPROVAL_STORE_PATH", str(store_path))
    store_path.write_text(
        '{"version":1,"items":[{"request_id":"r1","action_type":"email_sending","description":"d","details":{},"agent_id":"a","submitted_at":"2026-03-10T00:00:00Z","expires_at":"2099-03-10T00:00:00Z","status":"pending"}]}',
        encoding="utf-8",
    )

    queue = ApprovalQueue(queue_config)
    assert "r1" in queue.pending
    assert queue.pending["r1"].status == "pending"


@pytest.mark.asyncio
async def test_cleanup_decided_removes_old_decided_items(approval_queue):
    """cleanup_decided() should remove approved/rejected items older than threshold."""
    from datetime import timezone

    request = ApprovalRequest(
        action_type="email_sending",
        description="cleanup test",
        details={},
    )
    item = await approval_queue.submit(request)
    await approval_queue.decide(item.request_id, approved=True)

    # Backdate the decided item so it appears old
    decided_item = approval_queue.pending[item.request_id]
    decided_item.submitted_at = "2020-01-01T00:00:00Z"

    removed = await approval_queue.cleanup_decided(max_age_seconds=3600)

    assert item.request_id not in approval_queue.pending
    assert removed == 1


@pytest.mark.asyncio
async def test_cleanup_decided_keeps_recent_decided_items(approval_queue):
    """cleanup_decided() should not remove decided items newer than threshold."""
    request = ApprovalRequest(
        action_type="file_deletion",
        description="recent decided",
        details={},
    )
    item = await approval_queue.submit(request)
    await approval_queue.decide(item.request_id, approved=False)

    # Item was just decided — submitted_at is recent
    removed = await approval_queue.cleanup_decided(max_age_seconds=3600)

    assert item.request_id in approval_queue.pending
    assert removed == 0


@pytest.mark.asyncio
async def test_cleanup_decided_keeps_pending_items(approval_queue):
    """cleanup_decided() must not remove pending items regardless of age."""
    request = ApprovalRequest(
        action_type="email_sending",
        description="still pending",
        details={},
    )
    item = await approval_queue.submit(request)

    # Backdate the item
    approval_queue.pending[item.request_id].submitted_at = "2020-01-01T00:00:00Z"

    removed = await approval_queue.cleanup_decided(max_age_seconds=0)

    assert item.request_id in approval_queue.pending
    assert removed == 0
