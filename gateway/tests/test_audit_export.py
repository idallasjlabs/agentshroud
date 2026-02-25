# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for audit export functionality."""

import json
import pytest
from datetime import datetime, timezone
from io import StringIO

from gateway.security.audit_store import AuditStore, AuditEvent
from gateway.security.audit_export import AuditExporter, AuditExportConfig


class TestAuditEvent:
    """Test AuditEvent functionality."""

    def test_event_creation(self):
        """Test basic audit event creation."""
        event = AuditEvent(
            event_type="security_alert",
            severity="HIGH",
            details={"source": "test", "message": "test alert"},
            source_module="test_module"
        )
        
        assert event.event_type == "security_alert"
        assert event.severity == "HIGH"
        assert event.source_module == "test_module"
        assert event.details == {"source": "test", "message": "test alert"}
        assert event.event_id.startswith("audit_")
        assert event.timestamp is not None

    def test_content_hash(self):
        """Test content hash computation."""
        event = AuditEvent(
            event_type="test",
            severity="LOW",
            details={"data": "value"},
            source_module="test",
            event_id="test_123",
            timestamp="2026-01-01T12:00:00Z"
        )
        
        # Hash should be deterministic for same content
        hash1 = event.compute_content_hash()
        hash2 = event.compute_content_hash()
        assert hash1 == hash2
        assert len(hash1) == 64  # SHA-256 hex length

    def test_entry_hash_chain(self):
        """Test hash chain computation."""
        event = AuditEvent(
            event_type="test",
            severity="LOW",
            details={},
            source_module="test",
            event_id="test_123"
        )
        
        # First event (no previous hash)
        hash1 = event.compute_entry_hash(None)
        
        # Second event (with previous hash)
        hash2 = event.compute_entry_hash(hash1)
        
        assert hash1 != hash2
        assert len(hash1) == 64
        assert len(hash2) == 64


class TestAuditStore:
    """Test AuditStore functionality."""

    @pytest.fixture
    async def audit_store(self):
        """Create in-memory audit store for testing."""
        store = AuditStore(":memory:")
        await store.initialize()
        yield store
        await store.close()

    @pytest.mark.asyncio
    async def test_log_event(self, audit_store):
        """Test logging audit events."""
        event = await audit_store.log_event(
            event_type="test_event",
            severity="MEDIUM",
            details={"test": "data"},
            source_module="test_module"
        )
        
        assert event.event_type == "test_event"
        assert event.severity == "MEDIUM"
        assert event.entry_hash is not None
        assert event.prev_hash is None  # First event

    @pytest.mark.asyncio
    async def test_hash_chain_integrity(self, audit_store):
        """Test hash chain maintains integrity."""
        # Log several events
        events = []
        for i in range(3):
            event = await audit_store.log_event(
                event_type=f"event_{i}",
                severity="LOW",
                details={"sequence": i},
                source_module="test"
            )
            events.append(event)
        
        # First event should have no previous hash
        assert events[0].prev_hash is None
        
        # Subsequent events should chain properly
        assert events[1].prev_hash == events[0].entry_hash
        assert events[2].prev_hash == events[1].entry_hash
        
        # Verify chain integrity
        valid, message = await audit_store.verify_hash_chain()
        assert valid
        assert "3 events" in message

    @pytest.mark.asyncio
    async def test_query_events(self, audit_store):
        """Test querying events with filters."""
        # Log events with different types and severities
        await audit_store.log_event("login", "INFO", {"user": "test1"}, "auth")
        await audit_store.log_event("security_alert", "HIGH", {"threat": "xss"}, "security")
        await audit_store.log_event("login", "INFO", {"user": "test2"}, "auth")
        
        # Query all events
        all_events = await audit_store.query_events()
        assert len(all_events) == 3
        
        # Query by event type
        login_events = await audit_store.query_events(event_type="login")
        assert len(login_events) == 2
        
        # Query by severity
        high_events = await audit_store.query_events(severity_min="HIGH")
        assert len(high_events) == 1
        assert high_events[0].event_type == "security_alert"

    @pytest.mark.asyncio
    async def test_stats(self, audit_store):
        """Test audit store statistics."""
        # Initially empty
        stats = await audit_store.get_stats()
        assert stats["total_events"] == 0
        
        # Log some events
        await audit_store.log_event("test1", "CRITICAL", {}, "test")
        await audit_store.log_event("test2", "CRITICAL", {}, "test")
        await audit_store.log_event("test3", "LOW", {}, "test")
        
        stats = await audit_store.get_stats()
        assert stats["total_events"] == 3
        assert stats["severity_counts"]["CRITICAL"] == 2
        assert stats["severity_counts"]["LOW"] == 1


class TestAuditExporter:
    """Test AuditExporter functionality."""

    @pytest.fixture
    async def audit_store(self):
        """Create audit store with test data."""
        store = AuditStore(":memory:")
        await store.initialize()
        
        # Add test events
        await store.log_event("user_login", "INFO", {"user": "alice", "ip": "192.168.1.1"}, "auth")
        await store.log_event("security_alert", "HIGH", {"type": "injection", "blocked": True}, "security")
        await store.log_event("data_access", "MEDIUM", {"table": "users", "records": 10}, "database")
        
        yield store
        await store.close()

    @pytest.fixture
    def export_config(self):
        """Create test export configuration."""
        return AuditExportConfig(
            cef_vendor="TestVendor",
            cef_product="TestProduct", 
            cef_version="1.0",
            include_hash_verification=True
        )

    @pytest.mark.asyncio
    async def test_export_json(self, audit_store, export_config):
        """Test JSON export format."""
        exporter = AuditExporter(export_config, audit_store)
        
        result = await exporter.export_events(format_type="json")
        
        assert result["format"] == "json"
        assert result["record_count"] == 3
        assert result["hash_verification"]["verified"] is True
        
        # Parse the exported content
        export_data = json.loads(result["export_content"])
        assert "export_metadata" in export_data
        assert "events" in export_data
        assert len(export_data["events"]) == 3

    @pytest.mark.asyncio 
    async def test_export_cef(self, audit_store, export_config):
        """Test CEF export format."""
        exporter = AuditExporter(export_config, audit_store)
        
        result = await exporter.export_events(format_type="cef")
        
        assert result["format"] == "cef"
        assert result["record_count"] == 3
        
        # Check CEF format
        cef_lines = result["export_content"].strip().split("\n")
        assert len(cef_lines) == 3
        
        for line in cef_lines:
            assert line.startswith("CEF:0|TestVendor|TestProduct|1.0|")
            assert "entryHash=" in line

    @pytest.mark.asyncio
    async def test_export_json_ld(self, audit_store, export_config):
        """Test JSON-LD export format."""
        exporter = AuditExporter(export_config, audit_store)
        
        result = await exporter.export_events(format_type="json-ld")
        
        assert result["format"] == "json-ld"
        assert result["record_count"] == 3
        
        # Parse JSON-LD
        jsonld_data = json.loads(result["export_content"])
        assert "@context" in jsonld_data
        assert "@type" in jsonld_data
        assert jsonld_data["@type"] == "AuditExport"
        assert len(jsonld_data["events"]) == 3

    @pytest.mark.asyncio
    async def test_export_filtering(self, audit_store, export_config):
        """Test export with filters."""
        exporter = AuditExporter(export_config, audit_store)
        
        # Filter by event type
        result = await exporter.export_events(
            format_type="json",
            event_type="security_alert"
        )
        export_data = json.loads(result["export_content"])
        assert len(export_data["events"]) == 1
        assert export_data["events"][0]["event_type"] == "security_alert"
        
        # Filter by severity
        result = await exporter.export_events(
            format_type="json", 
            severity_min="HIGH"
        )
        export_data = json.loads(result["export_content"])
        assert len(export_data["events"]) == 1

    @pytest.mark.asyncio
    async def test_verify_export_integrity(self, audit_store, export_config):
        """Test export integrity verification."""
        exporter = AuditExporter(export_config, audit_store)
        
        # Export in JSON format
        result = await exporter.export_events(format_type="json")
        export_content = result["export_content"]
        
        # Verify the export
        verification = await exporter.verify_export_integrity(export_content, "json")
        assert verification["verified"] is True
        assert "3 events" in verification["message"]

    @pytest.mark.asyncio
    async def test_tamper_detection(self, audit_store, export_config):
        """Test tamper detection in exports."""
        exporter = AuditExporter(export_config, audit_store)
        
        # Export and tamper with content
        result = await exporter.export_events(format_type="json")
        export_data = json.loads(result["export_content"])
        
        # Tamper with an event hash
        export_data["events"][0]["entry_hash"] = "tampered_hash"
        tampered_content = json.dumps(export_data)
        
        # Verification should detect tampering
        verification = await exporter.verify_export_integrity(tampered_content, "json")
        assert verification["verified"] is False
        assert "Entry hash mismatch" in verification["message"]