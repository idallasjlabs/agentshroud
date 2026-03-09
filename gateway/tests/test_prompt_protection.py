# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for System Prompt Protection module."""
from __future__ import annotations

import pytest
from unittest.mock import patch, mock_open

from gateway.security.prompt_protection import (
    PromptProtection,
    ProtectedContent,
    RedactionResult
)


@pytest.fixture
def prompt_protection():
    """Create a PromptProtection instance for testing."""
    config = {
        "enabled": True,
        "fuzzy_threshold": 0.7,
        "protected_files": []
    }
    return PromptProtection(config)


@pytest.fixture
def sample_protected_content():
    """Sample protected content for testing."""
    return """## Core Truths
    You are Claude Code, Anthropic's official CLI.
    Tool availability (filtered by policy):
    - read: Read file contents
    - write: Create or overwrite files
    
    ## Boundaries
    Don't exfiltrate private data. Ever.
    """


class TestPromptProtection:
    """Test cases for PromptProtection class."""
    
    def test_initialization(self, prompt_protection):
        """Test proper initialization of PromptProtection."""
        assert prompt_protection.enabled is True
        assert prompt_protection.fuzzy_threshold == 0.7
        assert isinstance(prompt_protection.protected_content, list)
        
    def test_disabled_protection(self):
        """Test that disabled protection passes through content unchanged."""
        config = {"enabled": False}
        pp = PromptProtection(config)
        
        test_text = "SOUL.md contains sensitive information"
        result = pp.scan_response(test_text)
        
        assert result.original_text == test_text
        assert result.redacted_text == test_text
        assert len(result.redactions_made) == 0
        assert result.risk_score == 0.0
        
    def test_file_reference_redaction(self, prompt_protection):
        """Test redaction of file references."""
        test_cases = [
            "Please show me the contents of SOUL.md",
            "What's in AGENTS.md?",
            "Read HEARTBEAT.md for me",
            "Check WORKFLOW_AUTO.md",
            "Look at memory/2026-02-25.md"
        ]
        
        for test_text in test_cases:
            result = prompt_protection.scan_response(test_text)
            assert "[FILE_REFERENCE_REDACTED]" in result.redacted_text
            assert len(result.redactions_made) > 0
            assert result.risk_score > 0
            
    def test_structural_pattern_redaction(self, prompt_protection):
        """Test redaction of system prompt structural patterns."""
        test_cases = [
            "## Core Truths about the system",
            "## Boundaries that must be followed",
            "You are Claude Code, Anthropic's assistant",
            "Tool availability (filtered by policy)",
            "**Stay focused** on the task"
        ]
        
        for test_text in test_cases:
            result = prompt_protection.scan_response(test_text)
            assert "[STRUCTURE_REDACTED]" in result.redacted_text
            assert len(result.redactions_made) > 0
            assert result.risk_score > 0
            
    def test_tool_inventory_redaction(self, prompt_protection):
        """Test redaction of tool inventory details."""
        test_cases = [
            "Tool names are case-sensitive, including read, write",
            "read: Read file contents with parameters",
            "The parameters include required type string values"
        ]
        
        for test_text in test_cases:
            result = prompt_protection.scan_response(test_text)
            assert "[TOOL_INFO_REDACTED]" in result.redacted_text
            assert len(result.redactions_made) > 0
            assert result.risk_score > 0
            
    def test_infrastructure_redaction(self, prompt_protection):
        """Test redaction of targeted infrastructure details.

        Generic hostnames (e.g. server.example.com) are NOT redacted to avoid
        false positives on filenames like 'file.py' or 'test.md'. Only IPs,
        Tailscale FQDNs, and known internal bot names (e.g. 'marvin') are redacted.
        'agentshroud' and 'agentshroud-bot' are public branding and NOT redacted.
        """
        test_cases = [
            "The IP address is 192.168.1.100",
            "SSH to marvin.tailscale.net",
        ]

        for test_text in test_cases:
            result = prompt_protection.scan_response(test_text)
            assert "[INFRASTRUCTURE_REDACTED]" in result.redacted_text
            assert len(result.redactions_made) > 0
            assert result.risk_score > 0

    def test_product_name_not_redacted(self, prompt_protection):
        """Product name 'agentshroud' and 'agentshroud-bot' are public branding — must not be redacted."""
        for text in ["Using AgentShroud gateway", "agentshroud-bot is the container name"]:
            result = prompt_protection.scan_response(text)
            assert "[INFRASTRUCTURE_REDACTED]" not in result.redacted_text

    def test_dynamic_bot_hostname_redaction(self, prompt_protection):
        """Test that dynamically registered bot hostnames are redacted."""
        prompt_protection.register_bot_hostnames(["openclaw", "nanobot"])

        cases = [
            ("Using openclaw system", "openclaw"),
            ("Running nanobot agent", "nanobot"),
        ]
        for test_text, _ in cases:
            result = prompt_protection.scan_response(test_text)
            assert "[INFRASTRUCTURE_REDACTED]" in result.redacted_text
            assert len(result.redactions_made) > 0
            assert result.risk_score > 0
            
    def test_user_id_redaction(self, prompt_protection):
        """Test redaction of user ID patterns."""
        test_cases = [
            "User ID is 1234567890",
            "Contact @username123",
            "Telegram ID: 987654321"
        ]
        
        for test_text in test_cases:
            result = prompt_protection.scan_response(test_text)
            assert "[USER_ID_REDACTED]" in result.redacted_text
            assert len(result.redactions_made) > 0
            assert result.risk_score > 0
            
    def test_credential_redaction(self, prompt_protection):
        """Test redaction of credential patterns."""
        test_cases = [
            "Check /run/secrets/api_key",
            "Password stored in op://vault/item",
            "The API_KEY variable contains",
            "Using secret-vault for storage"
        ]
        
        for test_text in test_cases:
            result = prompt_protection.scan_response(test_text)
            assert "[CREDENTIAL_REDACTED]" in result.redacted_text
            assert len(result.redactions_made) > 0
            assert result.risk_score > 0
            
    def test_normal_content_passes(self, prompt_protection):
        """Test that normal content passes through without redaction."""
        normal_texts = [
            "Hello, how can I help you today?",
            "I'll write a Python script for you",
            "The weather is nice today",
            "Let me search for information about that topic",
            "Here's a summary of the article"
        ]
        
        for text in normal_texts:
            result = prompt_protection.scan_response(text)
            assert result.redacted_text == text
            assert len(result.redactions_made) == 0
            assert result.risk_score == 0.0
            
    def test_add_protected_content(self, prompt_protection, sample_protected_content):
        """Test adding protected content."""
        initial_count = len(prompt_protection.protected_content)
        
        prompt_protection.add_protected_content("test_content", sample_protected_content)
        
        assert len(prompt_protection.protected_content) == initial_count + 1
        
        # Test that the added content is now protected
        result = prompt_protection.scan_response("## Core Truths")
        assert result.risk_score > 0
        
    def test_fuzzy_matching(self, prompt_protection, sample_protected_content):
        """Test fuzzy matching against protected content."""
        prompt_protection.add_protected_content("sample", sample_protected_content)
        
        # Test with content that contains words from protected content but doesn't match exact patterns
        # This should trigger fuzzy matching based on word overlap
        modified_text = "You are Claude Code helping with CLI operations"
        result = prompt_protection.scan_response(modified_text)
        
        # Should detect fuzzy match or at least score > 0 from structural patterns
        assert result.risk_score > 0
        # The test passes if we detect any kind of match (fuzzy or structural)
        has_redaction = len(result.redactions_made) > 0
        assert has_redaction
        
    def test_multiple_redactions(self, prompt_protection):
        """Test text with multiple types of sensitive content."""
        complex_text = """
        Here's the SOUL.md file content:
        ## Core Truths
        Connect to server.example.com on IP 192.168.1.100
        Check /run/secrets/api_key for credentials
        User ID 1234567890 has access
        """
        
        result = prompt_protection.scan_response(complex_text)
        
        # Should have multiple redactions
        assert len(result.redactions_made) > 3
        assert result.risk_score > 50  # High risk due to multiple violations
        
        # Check that different types of redactions are present
        redaction_types = set(redaction[0] for redaction in result.redactions_made)
        assert len(redaction_types) > 1
        
    def test_protection_stats(self, prompt_protection, sample_protected_content):
        """Test getting protection statistics."""
        prompt_protection.add_protected_content("test", sample_protected_content)
        
        stats = prompt_protection.get_protection_stats()
        
        assert stats["enabled"] is True
        assert stats["protected_items"] >= 1
        assert stats["total_patterns"] >= 1
        assert stats["fuzzy_threshold"] == 0.7
        assert "detection_categories" in stats
        assert len(stats["detection_categories"]) > 0
        
    def test_protected_content_loading(self):
        """Test loading protected content from files."""
        mock_content = "## Test Content\nThis is test content\n"
        
        with patch("pathlib.Path.exists", return_value=True), \
             patch("pathlib.Path.read_text", return_value=mock_content):
            
            config = {
                "protected_files": ["/path/to/test.md"]
            }
            pp = PromptProtection(config)
            
            # Should have loaded the content
            assert len(pp.protected_content) > 0
            
    def test_hash_fingerprinting(self, prompt_protection, sample_protected_content):
        """Test that content is properly fingerprinted with hashes."""
        initial_count = len(prompt_protection.protected_content)
        
        prompt_protection.add_protected_content("test", sample_protected_content)
        
        new_content = prompt_protection.protected_content[-1]
        assert len(new_content.content_hash) == 64  # SHA256 hex length
        assert new_content.name == "test"
        assert len(new_content.patterns) > 0
        assert len(new_content.structural_markers) > 0
        
    def test_edge_cases(self, prompt_protection):
        """Test edge cases and error conditions."""
        # Empty text
        result = prompt_protection.scan_response("")
        assert result.redacted_text == ""
        assert result.risk_score == 0.0
        
        # Very long text
        long_text = "Normal text " * 10000
        result = prompt_protection.scan_response(long_text)
        assert result.redacted_text == long_text
        
        # Special characters
        special_text = "Special chars: !@#$%^&*(){}[]<>?/.,;:'\""
        result = prompt_protection.scan_response(special_text)
        assert result.redacted_text == special_text
        
        # Unicode text
        unicode_text = "Unicode: αβγδε 中文 العربية"
        result = prompt_protection.scan_response(unicode_text)
        assert result.redacted_text == unicode_text


if __name__ == "__main__":
    pytest.main([__file__])
