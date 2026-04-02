# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Approval Queue Stress Tests — concurrent requests and timeouts."""

from __future__ import annotations

import asyncio
import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest
import pytest_asyncio

from gateway.approval_queue.queue import ApprovalQueue
from gateway.approval_queue.store import ApprovalStore
from gateway.ingest_api.config import ApprovalQueueConfig
from gateway.ingest_api.models import ApprovalRequest


@pytest_asyncio.fixture
async def queue():
    config = ApprovalQueueConfig(enabled=True, actions=["email_sending"], timeout_seconds=5)
    return ApprovalQueue(config)


@pytest_asyncio.fixture
async def store():
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp:
        tmp_path = Path(tmp.name)
    s = ApprovalStore(db_path=tmp_path)
    await s.initialize()
    yield s
    await s.close()
    tmp_path.unlink(missing_ok=True)


class TestConcurrentApprovalRequests:
    """100 concurrent approval requests."""

    @pytest.mark.asyncio
    async def test_100_concurrent_submissions(self, queue):
        """Submit 100 requests concurrently — all should succeed."""

        async def submit_one(i):
            req = ApprovalRequest(
                action_type="email_sending",
                description=f"Send email #{i}",
                details={"recipient": f"user{i}@example.com"},
                agent_id=f"agent-{i % 5}",
            )
            return await queue.submit(req)

        results = await asyncio.gather(*[submit_one(i) for i in range(100)])
        assert len(results) == 100
        # All should have unique IDs
        ids = {r.request_id for r in results}
        assert len(ids) == 100

    @pytest.mark.asyncio
    async def test_concurrent_submit_and_decide(self, queue):
        """Submit and decide requests concurrently."""
        # Submit 20 requests
        items = []
        for i in range(20):
            req = ApprovalRequest(
                action_type="file_deletion",
                description=f"Delete file #{i}",
                agent_id="agent-1",
            )
            item = await queue.submit(req)
            items.append(item)

        # Approve half, reject half concurrently
        async def decide(item, approved):
            return await queue.decide(item.request_id, approved=approved)

        tasks = []
        for i, item in enumerate(items):
            tasks.append(decide(item, i % 2 == 0))

        results = await asyncio.gather(*tasks)
        approved = sum(1 for r in results if r.status == "approved")
        rejected = sum(1 for r in results if r.status == "rejected")
        assert approved == 10
        assert rejected == 10


class TestApprovalTimeout:
    """Timeout handling for approval requests."""

    @pytest.mark.asyncio
    async def test_expired_request_cannot_be_decided(self, queue):
        """Expired request raises ValueError on decide."""
        # Submit with very short timeout (queue has 5s timeout)
        req = ApprovalRequest(
            action_type="email_sending",
            description="Expiring request",
            agent_id="agent-1",
        )
        item = await queue.submit(req)

        # Manually expire it
        item.expires_at = (
            (datetime.now(timezone.utc) - timedelta(seconds=10)).isoformat().replace("+00:00", "Z")
        )

        with pytest.raises(ValueError, match="expired"):
            await queue.decide(item.request_id, approved=True)

    @pytest.mark.asyncio
    async def test_get_pending_expires_stale(self, queue):
        """get_pending should expire stale items."""
        req = ApprovalRequest(
            action_type="email_sending",
            description="Will expire",
            agent_id="agent-1",
        )
        item = await queue.submit(req)
        # Manually expire
        item.expires_at = (
            (datetime.now(timezone.utc) - timedelta(seconds=10)).isoformat().replace("+00:00", "Z")
        )

        pending = await queue.get_pending()
        # The expired item should not be in pending
        pending_ids = {p.request_id for p in pending}
        assert item.request_id not in pending_ids


class TestApprovalStorePersistence:
    """Queue persistence across restart."""

    @pytest.mark.asyncio
    async def test_store_save_and_load(self, store):
        """Items saved to store can be reloaded."""
        from gateway.ingest_api.models import ApprovalQueueItem

        now = datetime.now(timezone.utc)
        item = ApprovalQueueItem(
            request_id="test-001",
            action_type="email_sending",
            description="Test email",
            details={"to": "user@example.com"},
            agent_id="agent-1",
            submitted_at=now.isoformat().replace("+00:00", "Z"),
            expires_at=(now + timedelta(hours=1)).isoformat().replace("+00:00", "Z"),
            status="pending",
        )
        await store.save(item)

        loaded = await store.load_pending()
        assert len(loaded) == 1
        assert loaded[0].request_id == "test-001"

    @pytest.mark.asyncio
    async def test_store_persists_across_reopen(self):
        """Items survive store close/reopen cycle."""
        with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp:
            tmp_path = Path(tmp.name)

        try:
            # First session: save item
            store1 = ApprovalStore(db_path=tmp_path)
            await store1.initialize()

            from gateway.ingest_api.models import ApprovalQueueItem

            now = datetime.now(timezone.utc)
            item = ApprovalQueueItem(
                request_id="persist-001",
                action_type="file_deletion",
                description="Delete important file",
                details={},
                agent_id="agent-1",
                submitted_at=now.isoformat().replace("+00:00", "Z"),
                expires_at=(now + timedelta(hours=1)).isoformat().replace("+00:00", "Z"),
                status="pending",
            )
            await store1.save(item)
            await store1.close()

            # Second session: reload
            store2 = ApprovalStore(db_path=tmp_path)
            await store2.initialize()
            loaded = await store2.load_pending()
            assert len(loaded) == 1
            assert loaded[0].request_id == "persist-001"
            await store2.close()
        finally:
            tmp_path.unlink(missing_ok=True)

    @pytest.mark.asyncio
    async def test_store_expires_old_items(self, store):
        """Store marks expired items on load."""
        from gateway.ingest_api.models import ApprovalQueueItem

        past = datetime.now(timezone.utc) - timedelta(hours=2)
        item = ApprovalQueueItem(
            request_id="expired-001",
            action_type="email_sending",
            description="Old request",
            details={},
            agent_id="agent-1",
            submitted_at=past.isoformat().replace("+00:00", "Z"),
            expires_at=(past + timedelta(seconds=10)).isoformat().replace("+00:00", "Z"),
            status="pending",
        )
        await store.save(item)

        loaded = await store.load_pending()
        assert len(loaded) == 0  # Should be expired

    @pytest.mark.asyncio
    async def test_store_update_status(self, store):
        """Status updates persist."""
        from gateway.ingest_api.models import ApprovalQueueItem

        now = datetime.now(timezone.utc)
        item = ApprovalQueueItem(
            request_id="status-001",
            action_type="email_sending",
            description="Test",
            details={},
            agent_id="agent-1",
            submitted_at=now.isoformat().replace("+00:00", "Z"),
            expires_at=(now + timedelta(hours=1)).isoformat().replace("+00:00", "Z"),
            status="pending",
        )
        await store.save(item)
        await store.update_status("status-001", "approved", "looks good")

        all_items = await store.load_all()
        assert len(all_items) == 1
        assert all_items[0].status == "approved"


class TestAutoExpire:
    """Auto-expire old requests."""

    @pytest.mark.asyncio
    async def test_double_decide_raises(self, queue):
        """Deciding on already-decided request raises ValueError."""
        req = ApprovalRequest(
            action_type="email_sending",
            description="Test",
            agent_id="agent-1",
        )
        item = await queue.submit(req)
        await queue.decide(item.request_id, approved=True)

        with pytest.raises(ValueError, match="already"):
            await queue.decide(item.request_id, approved=False)
