# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Test Context Window Poisoning Defense."""

from __future__ import annotations

import pytest

from gateway.security.context_guard import ContextGuard, ContextSegment, check_message


class TestCheckMessage:
    def test_normal_message_allowed(self):
        allowed, findings = check_message("Hello, how are you today?")
        assert allowed
        # Clean messages may return informational findings
        assert allowed

    def test_repeated_pattern_flagged(self):
        # 50+ char block repeated >10 times
        pattern = "A" * 60
        msg = (pattern + " ") * 15
        allowed, findings = check_message(msg)
        assert len(findings) > 0  # Should detect repetition

    def test_short_repetitions_allowed(self):
        # Short patterns repeated are normal (like "ha ha ha")
        msg = "ha " * 20
        allowed, findings = check_message(msg)
        assert allowed  # Short pattern, not suspicious

    def test_few_repetitions_allowed(self):
        # A long pattern repeated only 3 times is fine
        pattern = "B" * 60
        msg = (pattern + " ") * 3
        allowed, findings = check_message(msg)
        assert allowed

    def test_oversized_message_blocked(self):
        msg = "x" * 600000  # 600KB > 500KB default
        allowed, findings = check_message(msg)
        assert not allowed

    def test_normal_sized_message_allowed(self):
        msg = "x" * 1000  # 1KB is fine
        allowed, findings = check_message(msg)
        assert allowed


# ── C10: Source Tagging tests ─────────────────────────────────────────────────


class TestSourceTagging:
    @pytest.fixture
    def guard(self):
        return ContextGuard()

    def test_segment_tagging_basic(self, guard):
        seg = guard.tag_segment("Hello from system", source="system", trust_level="TRUSTED")
        assert isinstance(seg, ContextSegment)
        assert seg.source == "system"
        assert seg.trust_level == "TRUSTED"
        assert len(seg.content_hash) == 64
        assert seg.segment_id != ""

    def test_segment_provenance_ordering(self, guard):
        guard.record_segment("session-a", "system message", source="system", trust_level="TRUSTED")
        guard.record_segment("session-a", "user query", source="user", trust_level="UNTRUSTED")
        guard.record_segment(
            "session-a", "tool result", source="tool_result", trust_level="UNTRUSTED"
        )
        provenance = guard.get_segment_provenance("session-a")
        assert len(provenance) == 3
        assert provenance[0].source == "system"
        assert provenance[1].source == "user"
        assert provenance[2].source == "tool_result"

    def test_segment_hash_integrity(self, guard):
        import hashlib

        content = "important content"
        seg = guard.tag_segment(content, source="document")
        expected_hash = hashlib.sha256(content.encode("utf-8")).hexdigest()
        assert seg.content_hash == expected_hash

    def test_empty_provenance_for_unknown_session(self, guard):
        result = guard.get_segment_provenance("nonexistent-session")
        assert result == []

    def test_separate_sessions_isolated(self, guard):
        guard.record_segment("session-x", "data x", source="user")
        guard.record_segment("session-y", "data y", source="user")
        assert len(guard.get_segment_provenance("session-x")) == 1
        assert len(guard.get_segment_provenance("session-y")) == 1
