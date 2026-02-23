# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Unit tests for pipeline components."""
from __future__ import annotations


from gateway.proxy.pipeline import AuditChain


class TestAuditChain:
    """Tests for the SHA-256 hash chain."""

    def test_genesis(self):
        chain = AuditChain()
        assert chain.last_hash == AuditChain.GENESIS_HASH
        assert len(chain) == 0

    def test_append_single(self):
        chain = AuditChain()
        entry = chain.append("hello", "inbound")
        assert entry.previous_hash == AuditChain.GENESIS_HASH
        assert entry.chain_hash != AuditChain.GENESIS_HASH
        assert len(chain) == 1

    def test_append_chain(self):
        chain = AuditChain()
        e1 = chain.append("first", "inbound")
        e2 = chain.append("second", "outbound")
        assert e2.previous_hash == e1.chain_hash
        assert len(chain) == 2

    def test_verify_valid(self):
        chain = AuditChain()
        for i in range(20):
            chain.append(f"msg-{i}", "inbound" if i % 2 == 0 else "outbound")
        valid, msg = chain.verify_chain()
        assert valid is True
        assert "20 entries" in msg

    def test_verify_tampered_chain_hash(self):
        chain = AuditChain()
        for i in range(5):
            chain.append(f"msg-{i}", "inbound")
        chain._entries[2].chain_hash = "bad" * 16 + "00" * 8
        valid, msg = chain.verify_chain()
        assert valid is False
        assert "mismatch" in msg.lower()

    def test_verify_tampered_previous_hash(self):
        chain = AuditChain()
        for i in range(5):
            chain.append(f"msg-{i}", "inbound")
        chain._entries[3].previous_hash = "bad" * 16 + "00" * 8
        valid, msg = chain.verify_chain()
        assert valid is False

    def test_entries_returns_copy(self):
        chain = AuditChain()
        chain.append("test", "inbound")
        entries = chain.entries
        assert len(entries) == 1
        entries.clear()
        assert len(chain) == 1  # Original unmodified

    def test_metadata(self):
        chain = AuditChain()
        entry = chain.append("test", "inbound", {"source": "telegram"})
        assert entry.metadata == {"source": "telegram"}

    def test_content_hash_deterministic(self):
        chain = AuditChain()
        import hashlib

        expected = hashlib.sha256("test".encode()).hexdigest()
        entry = chain.append("test", "inbound")
        assert entry.content_hash == expected

    def test_different_content_different_hash(self):
        chain = AuditChain()
        e1 = chain.append("hello", "inbound")
        e2 = chain.append("world", "inbound")
        assert e1.content_hash != e2.content_hash
        assert e1.chain_hash != e2.chain_hash
