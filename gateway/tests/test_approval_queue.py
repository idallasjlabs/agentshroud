"""Tests for approval queue"""

import asyncio

import pytest

from gateway.ingest_api.config import ApprovalQueueConfig
from gateway.ingest_api.models import ApprovalRequest
from gateway.approval_queue.queue import ApprovalQueue


@pytest.fixture
def queue_config():
    """Create approval queue configuration for testing"""
    return ApprovalQueueConfig(
        enabled=True,
        actions=["email_sending", "file_deletion"],
        timeout_seconds=2,  # Short timeout for testing
    )


@pytest.fixture
def approval_queue(queue_config):
    """Create approval queue instance for testing"""
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
    updated = await approval_queue.decide(
        item.request_id, approved=False, reason="Too risky"
    )

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
    from fastapi import WebSocket
    from unittest.mock import AsyncMock, MagicMock

    websocket = MagicMock(spec=WebSocket)
    websocket.accept = AsyncMock()

    await approval_queue.connect(websocket)

    assert websocket in approval_queue.connected_clients
    websocket.accept.assert_called_once()


@pytest.mark.asyncio
async def test_websocket_disconnect(approval_queue):
    """Test WebSocket client disconnection"""
    from fastapi import WebSocket
    from unittest.mock import MagicMock

    websocket = MagicMock(spec=WebSocket)

    # Add client
    approval_queue.connected_clients.add(websocket)

    # Disconnect
    await approval_queue.disconnect(websocket)

    assert websocket not in approval_queue.connected_clients


@pytest.mark.asyncio
async def test_broadcast_with_failed_client(approval_queue):
    """Test broadcast handles failed client sends"""
    from unittest.mock import MagicMock, AsyncMock

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
