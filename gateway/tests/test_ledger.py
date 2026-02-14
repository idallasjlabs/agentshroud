"""Tests for data ledger"""

import pytest


@pytest.mark.asyncio
async def test_record_entry(test_ledger):
    """Test creating a ledger entry"""
    entry = await test_ledger.record(
        source="shortcut",
        content="sanitized content",
        original_content="original content",
        sanitized=True,
        redaction_count=2,
        redaction_types=["US_SSN", "EMAIL_ADDRESS"],
        forwarded_to="test-agent",
        content_type="text",
        metadata={"foo": "bar"},
    )

    assert entry.id is not None
    assert entry.source == "shortcut"
    assert entry.sanitized is True
    assert entry.redaction_count == 2


@pytest.mark.asyncio
async def test_get_entry(test_ledger):
    """Test retrieving a ledger entry by ID"""
    created = await test_ledger.record(
        source="shortcut",
        content="test content",
        original_content="test content",
        sanitized=False,
        redaction_count=0,
        redaction_types=[],
        forwarded_to="test-agent",
    )

    retrieved = await test_ledger.get_entry(created.id)

    assert retrieved is not None
    assert retrieved.id == created.id
    assert retrieved.source == "shortcut"


@pytest.mark.asyncio
async def test_query_ledger(test_ledger):
    """Test paginated ledger query"""
    # Create multiple entries
    for i in range(5):
        await test_ledger.record(
            source="shortcut",
            content=f"content {i}",
            original_content=f"content {i}",
            sanitized=False,
            redaction_count=0,
            redaction_types=[],
            forwarded_to="test-agent",
        )

    # Query first page
    result = await test_ledger.query(page=1, page_size=3)

    assert result.total == 5
    assert len(result.entries) == 3
    assert result.page == 1
    assert result.page_size == 3


@pytest.mark.asyncio
async def test_query_with_filter(test_ledger):
    """Test ledger query with source filter"""
    # Create entries from different sources
    await test_ledger.record(
        source="shortcut",
        content="from shortcut",
        original_content="from shortcut",
        sanitized=False,
        redaction_count=0,
        redaction_types=[],
        forwarded_to="agent-1",
    )

    await test_ledger.record(
        source="browser_extension",
        content="from browser",
        original_content="from browser",
        sanitized=False,
        redaction_count=0,
        redaction_types=[],
        forwarded_to="agent-1",
    )

    # Query for shortcut only
    result = await test_ledger.query(source="shortcut")

    assert result.total == 1
    assert result.entries[0].source == "shortcut"


@pytest.mark.asyncio
async def test_delete_entry(test_ledger):
    """Test deleting a ledger entry"""
    created = await test_ledger.record(
        source="shortcut",
        content="to be deleted",
        original_content="to be deleted",
        sanitized=False,
        redaction_count=0,
        redaction_types=[],
        forwarded_to="test-agent",
    )

    # Delete
    deleted = await test_ledger.delete_entry(created.id)
    assert deleted is True

    # Verify it's gone
    retrieved = await test_ledger.get_entry(created.id)
    assert retrieved is None


@pytest.mark.asyncio
async def test_delete_nonexistent(test_ledger):
    """Test deleting a non-existent entry"""
    deleted = await test_ledger.delete_entry("nonexistent-id")
    assert deleted is False


@pytest.mark.asyncio
async def test_get_stats(test_ledger):
    """Test stats calculation"""
    # Create entries
    await test_ledger.record(
        source="shortcut",
        content="content",
        original_content="content",
        sanitized=True,
        redaction_count=1,
        redaction_types=["US_SSN"],
        forwarded_to="agent-1",
    )

    stats = await test_ledger.get_stats()

    assert stats["total_entries"] == 1
    assert "by_source" in stats
    assert stats["by_source"]["shortcut"] == 1
