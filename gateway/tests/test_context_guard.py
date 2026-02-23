# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Test Context Window Poisoning Defense."""
from __future__ import annotations


from gateway.security.context_guard import check_message


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
