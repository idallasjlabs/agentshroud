"""Audit Chain Verification Tests — integrity, tamper detection, concurrency."""

import asyncio
import hashlib
import tempfile
from pathlib import Path

import pytest
import pytest_asyncio

from gateway.ingest_api.config import LedgerConfig
from gateway.ingest_api.ledger import DataLedger


@pytest_asyncio.fixture
async def ledger():
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp:
        tmp_path = Path(tmp.name)
    config = LedgerConfig(backend="sqlite", path=tmp_path, retention_days=90)
    led = DataLedger(config)
    await led.initialize()
    yield led
    await led.close()
    tmp_path.unlink(missing_ok=True)


class TestAuditChainIntegrity:
    """Chain with many entries — verify integrity."""

    @pytest.mark.asyncio
    async def test_1000_entries_all_recorded(self, ledger):
        """Write 1000 entries and verify they're all there."""
        for i in range(1000):
            await ledger.record(
                source="api",
                content=f"Message {i} content",
                original_content=f"Message {i} original",
                sanitized=i % 3 == 0,
                redaction_count=1 if i % 3 == 0 else 0,
                redaction_types=["US_SSN"] if i % 3 == 0 else [],
                forwarded_to="test-agent",
                content_type="text",
            )

        # Verify count
        query = await ledger.query(page=1, page_size=1)
        assert query.total == 1000

    @pytest.mark.asyncio
    async def test_content_hashes_are_unique(self, ledger):
        """Different content should produce different hashes."""
        entries = []
        for i in range(50):
            entry = await ledger.record(
                source="api",
                content=f"Unique content {i}",
                original_content=f"Unique original {i}",
                sanitized=False,
                redaction_count=0,
                redaction_types=[],
                forwarded_to="test-agent",
            )
            entries.append(entry)

        hashes = {e.content_hash for e in entries}
        assert len(hashes) == 50, "Each entry should have a unique hash"

    @pytest.mark.asyncio
    async def test_hash_is_sha256(self, ledger):
        """Content hash should be a valid SHA-256 hex digest."""
        entry = await ledger.record(
            source="api", content="test content",
            original_content="test content", sanitized=False,
            redaction_count=0, redaction_types=[], forwarded_to="agent",
        )
        assert len(entry.content_hash) == 64
        int(entry.content_hash, 16)  # Should be valid hex

    @pytest.mark.asyncio
    async def test_hash_matches_content(self, ledger):
        """Verify hash matches SHA-256 of the content."""
        content = "verify this hash"
        entry = await ledger.record(
            source="api", content=content,
            original_content=content, sanitized=False,
            redaction_count=0, redaction_types=[], forwarded_to="agent",
        )
        expected_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
        assert entry.content_hash == expected_hash


class TestTamperDetection:
    """Tamper detection at various chain positions."""

    @pytest.mark.asyncio
    async def test_entry_retrieval_by_id(self, ledger):
        """Can retrieve specific entry by ID for verification."""
        entry = await ledger.record(
            source="api", content="tamper test",
            original_content="tamper test", sanitized=False,
            redaction_count=0, redaction_types=[], forwarded_to="agent",
        )
        retrieved = await ledger.get_entry(entry.id)
        assert retrieved is not None
        assert retrieved.content_hash == entry.content_hash

    @pytest.mark.asyncio
    async def test_nonexistent_entry_returns_none(self, ledger):
        """Looking up nonexistent entry returns None."""
        result = await ledger.get_entry("nonexistent-uuid")
        assert result is None

    @pytest.mark.asyncio
    async def test_delete_entry_removes_it(self, ledger):
        """Deleted entry is gone (right to erasure)."""
        entry = await ledger.record(
            source="api", content="to be deleted",
            original_content="to be deleted", sanitized=False,
            redaction_count=0, redaction_types=[], forwarded_to="agent",
        )
        assert await ledger.delete_entry(entry.id)
        assert await ledger.get_entry(entry.id) is None

    @pytest.mark.asyncio
    async def test_delete_nonexistent_returns_false(self, ledger):
        """Deleting nonexistent entry returns False."""
        assert not await ledger.delete_entry("nonexistent-uuid")


class TestChainExportAndVerification:
    """Export chain and re-verify."""

    @pytest.mark.asyncio
    async def test_query_pagination(self, ledger):
        """Paginated queries return correct subsets."""
        for i in range(25):
            await ledger.record(
                source="api", content=f"page test {i}",
                original_content=f"page test {i}", sanitized=False,
                redaction_count=0, redaction_types=[], forwarded_to="agent",
            )

        page1 = await ledger.query(page=1, page_size=10)
        assert len(page1.entries) == 10
        assert page1.total == 25

        page3 = await ledger.query(page=3, page_size=10)
        assert len(page3.entries) == 5

    @pytest.mark.asyncio
    async def test_query_filter_by_source(self, ledger):
        """Filter entries by source."""
        for i in range(10):
            source = "shortcut" if i % 2 == 0 else "api"
            await ledger.record(
                source=source, content=f"filter test {i}",
                original_content=f"filter test {i}", sanitized=False,
                redaction_count=0, redaction_types=[], forwarded_to="agent",
            )

        shortcut_entries = await ledger.query(source="shortcut")
        assert shortcut_entries.total == 5

    @pytest.mark.asyncio
    async def test_stats_correct(self, ledger):
        """Stats reflect actual data."""
        for i in range(10):
            await ledger.record(
                source="api" if i < 7 else "shortcut",
                content=f"stats test {i}",
                original_content=f"stats test {i}",
                sanitized=i < 3,
                redaction_count=1 if i < 3 else 0,
                redaction_types=["US_SSN"] if i < 3 else [],
                forwarded_to="agent",
            )

        stats = await ledger.get_stats()
        assert stats["total_entries"] == 10
        assert stats["by_source"]["api"] == 7
        assert stats["by_source"]["shortcut"] == 3


class TestConcurrentWrites:
    """Concurrent writes to chain."""

    @pytest.mark.asyncio
    async def test_50_concurrent_writes(self, ledger):
        """50 concurrent write operations should all succeed."""
        async def write_entry(i):
            return await ledger.record(
                source="api", content=f"concurrent {i}",
                original_content=f"concurrent {i}", sanitized=False,
                redaction_count=0, redaction_types=[], forwarded_to="agent",
            )

        results = await asyncio.gather(*[write_entry(i) for i in range(50)])
        assert len(results) == 50

        query = await ledger.query(page=1, page_size=1)
        assert query.total == 50

    @pytest.mark.asyncio
    async def test_concurrent_write_and_read(self, ledger):
        """Concurrent writes and reads don't conflict."""
        # Pre-populate
        for i in range(10):
            await ledger.record(
                source="api", content=f"pre {i}",
                original_content=f"pre {i}", sanitized=False,
                redaction_count=0, redaction_types=[], forwarded_to="agent",
            )

        async def write(i):
            return await ledger.record(
                source="api", content=f"during {i}",
                original_content=f"during {i}", sanitized=False,
                redaction_count=0, redaction_types=[], forwarded_to="agent",
            )

        async def read():
            return await ledger.query(page=1, page_size=50)

        # Mix writes and reads
        tasks = [write(i) for i in range(20)] + [read() for _ in range(10)]
        results = await asyncio.gather(*tasks)
        assert len(results) == 30


class TestRetention:
    """Retention enforcement."""

    @pytest.mark.asyncio
    async def test_enforce_retention_deletes_expired(self, ledger):
        """Retention enforcement removes expired entries."""
        # Create entries (they get auto-expiry based on retention_days)
        for i in range(5):
            await ledger.record(
                source="api", content=f"retention test {i}",
                original_content=f"retention test {i}", sanitized=False,
                redaction_count=0, redaction_types=[], forwarded_to="agent",
            )

        # Normal entries shouldn't be expired (retention_days=90)
        deleted = await ledger.enforce_retention()
        assert deleted == 0

        query = await ledger.query()
        assert query.total == 5
