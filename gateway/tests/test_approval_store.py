"""Tests for SQLite-backed approval queue persistence."""

from datetime import datetime, timedelta, timezone
from pathlib import Path

import pytest
import pytest_asyncio

from gateway.approval_queue.store import ApprovalStore
from gateway.ingest_api.models import ApprovalQueueItem


def _make_item(
    request_id: str = "test-001",
    status: str = "pending",
    expires_minutes: int = 60,
) -> ApprovalQueueItem:
    now = datetime.now(timezone.utc)
    return ApprovalQueueItem(
        request_id=request_id,
        action_type="email_sending",
        description="Send email to test@example.com",
        details={"to": "test@example.com", "subject": "Hello"},
        agent_id="openclaw-main",
        submitted_at=now.isoformat().replace("+00:00", "Z"),
        expires_at=(now + timedelta(minutes=expires_minutes))
        .isoformat()
        .replace("+00:00", "Z"),
        status=status,
    )


@pytest_asyncio.fixture
async def store(tmp_path: Path):
    db = tmp_path / "test_approval.db"
    s = ApprovalStore(db)
    await s.initialize()
    yield s
    await s.close()


@pytest.mark.asyncio
async def test_persist_and_reload(tmp_path: Path):
    """Items saved by one store instance are visible to another."""
    db = tmp_path / "persist.db"

    store1 = ApprovalStore(db)
    await store1.initialize()
    item = _make_item("persist-001")
    await store1.save(item)
    await store1.close()

    store2 = ApprovalStore(db)
    await store2.initialize()
    items = await store2.load_pending()
    await store2.close()

    assert len(items) == 1
    assert items[0].request_id == "persist-001"
    assert items[0].details == {"to": "test@example.com", "subject": "Hello"}


@pytest.mark.asyncio
async def test_decide_persists(tmp_path: Path):
    """Deciding an item persists the new status."""
    db = tmp_path / "decide.db"

    store1 = ApprovalStore(db)
    await store1.initialize()
    await store1.save(_make_item("decide-001"))
    await store1.update_status("decide-001", "approved", "looks good")
    await store1.close()

    store2 = ApprovalStore(db)
    await store2.initialize()
    pending = await store2.load_pending()
    all_items = await store2.load_all()
    await store2.close()

    assert len(pending) == 0  # no longer pending
    assert len(all_items) == 1
    assert all_items[0].status == "approved"


@pytest.mark.asyncio
async def test_expired_items_on_reload(tmp_path: Path):
    """Expired items are marked expired during load_pending."""
    db = tmp_path / "expire.db"

    store1 = ApprovalStore(db)
    await store1.initialize()
    # Create item that expired 5 minutes ago
    await store1.save(_make_item("expire-001", expires_minutes=-5))
    await store1.close()

    store2 = ApprovalStore(db)
    await store2.initialize()
    pending = await store2.load_pending()
    all_items = await store2.load_all()
    await store2.close()

    assert len(pending) == 0
    assert all_items[0].status == "expired"


@pytest.mark.asyncio
async def test_store_survives_restart(tmp_path: Path):
    """Simulates a full restart cycle: save, close, reopen, verify."""
    db = tmp_path / "restart.db"

    # First "run"
    s = ApprovalStore(db)
    await s.initialize()
    await s.save(_make_item("restart-001"))
    await s.save(_make_item("restart-002"))
    await s.update_status("restart-002", "rejected", "not allowed")
    await s.close()

    # Second "run" — fresh instance
    s2 = ApprovalStore(db)
    await s2.initialize()
    pending = await s2.load_pending()
    all_items = await s2.load_all()
    await s2.close()

    assert len(pending) == 1
    assert pending[0].request_id == "restart-001"
    assert len(all_items) == 2
