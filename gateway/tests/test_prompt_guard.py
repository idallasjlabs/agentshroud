# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for PromptGuard security component"""

import pytest
from gateway.security.prompt_guard import PromptGuard, ThreatAction


@pytest.fixture
def prompt_guard():
    """Create a PromptGuard instance for testing"""
    return PromptGuard(block_threshold=0.8, warn_threshold=0.4)


def test_prompt_guard_init():
    """Test PromptGuard initialization"""
    guard = PromptGuard(block_threshold=0.9, warn_threshold=0.5)
    assert guard.block_threshold == 0.9
    assert guard.warn_threshold == 0.5
    assert len(guard.patterns) > 0


def test_benign_message(prompt_guard):
    """Test that normal messages pass through"""
    result = prompt_guard.scan("Hello, how are you today?")
    assert not result.blocked
    assert result.score < 0.4
    assert result.action == ThreatAction.LOG
    assert result.sanitized_input == "Hello, how are you today?"
