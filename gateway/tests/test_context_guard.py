"""
Test Context Window Poisoning Defense - verify pattern stuffing and oversized messages are blocked.
"""

import pytest
import sys
import os

# Add the parent directory to the path to import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from security.context_guard import check_message, ContextGuard


class TestContextGuard:
    """Test the Context Window Poisoning Defense functionality."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.context_guard = ContextGuard()
    
    def test_check_message_normal_message(self):
        """Test that normal messages pass through."""
        message = "This is a normal message with reasonable content."
        allowed, findings = check_message(message)
        assert allowed
        assert "passed all security checks" in findings[0]
    
    def test_check_message_repeated_pattern_stuffing(self):
        """Test detection of repeated pattern stuffing (50+ chars repeated >10 times)."""
        # Create a pattern that's 50+ characters repeated more than 10 times
        pattern = "A" * 50 + "B" * 10  # 60 character pattern
        repeated_message = pattern * 15  # Repeat 15 times (more than 10)
        
        allowed, findings = check_message(repeated_message)
        assert not allowed
        assert any("repeated pattern" in finding.lower() for finding in findings)
    
    def test_check_message_short_repeated_pattern_allowed(self):
        """Test that short repeated patterns (<50 chars) are allowed."""
        pattern = "A" * 30  # Less than 50 characters
        repeated_message = pattern * 15  # Even if repeated many times
        
        allowed, findings = check_message(repeated_message)
        # This should pass since pattern is < 50 chars
        # (though it might trigger other checks depending on implementation)
        # The key is that it shouldn't trigger the "repeated pattern" check specifically
        if not allowed:
            assert not any("repeated pattern" in finding.lower() for finding in findings)
    
    def test_check_message_few_repetitions_allowed(self):
        """Test that few repetitions (<=10) are allowed."""
        pattern = "A" * 60  # 60 character pattern (>50)
        repeated_message = pattern * 5  # Repeat only 5 times (<=10)
        
        allowed, findings = check_message(repeated_message)
        # Should pass since repetitions <= 10
        if not allowed:
            assert not any("repeated pattern" in finding.lower() for finding in findings)
    
    def test_check_message_oversized_message(self):
        """Test blocking of oversized messages (>500KB)."""
        # Create a message larger than 500KB
        large_message = "A" * (500 * 1024 + 1000)  # 500KB + 1000 bytes
        
        allowed, findings = check_message(large_message)
        assert not allowed
        assert any("too large" in finding.lower() for finding in findings)
        assert any("500" in finding for finding in findings)  # Should mention the limit
    
    def test_check_message_max_size_boundary(self):
        """Test message exactly at 500KB boundary."""
        # Create a message exactly at 500KB
        boundary_message = "A" * (500 * 1024)  # Exactly 500KB
        
        allowed, findings = check_message(boundary_message)
        assert allowed or "too large" not in str(findings).lower()
    
    def test_check_message_instruction_dilution_low_entropy(self):
        """Test detection of instruction dilution via low entropy."""
        # Create a long message with very low entropy (mostly repeated characters)
        low_entropy_message = "A" * 2000  # 2000 'A's - very low entropy
        
        allowed, findings = check_message(low_entropy_message)
        assert not allowed
        assert any("entropy" in finding.lower() for finding in findings)
    
    def test_check_message_instruction_dilution_normal_entropy(self):
        """Test that normal entropy messages pass."""
        # Create a message with normal entropy
        normal_message = "The quick brown fox jumps over the lazy dog. " * 30  # Repeated but diverse
        
        allowed, findings = check_message(normal_message)
        # Should pass entropy check (though might fail other checks)
        if not allowed:
            assert not any("entropy" in finding.lower() for finding in findings)
    
    def test_check_message_short_message_no_entropy_check(self):
        """Test that short messages (<1000 chars) skip entropy check."""
        # Create a short message with low entropy
        short_low_entropy = "A" * 500  # 500 'A's but less than 1000 chars
        
        allowed, findings = check_message(short_low_entropy)
        # Should pass since message is too short for entropy check
        if not allowed:
            assert not any("entropy" in finding.lower() for finding in findings)
    
    def test_check_message_multiple_violations(self):
        """Test message that violates multiple rules."""
        # Create message that's both oversized and has repeated patterns
        pattern = "B" * 60  # 60 char pattern
        huge_repeated = pattern * 10000  # Creates a huge message with repetition
        
        allowed, findings = check_message(huge_repeated)
        assert not allowed
        # Should detect multiple issues
        assert len(findings) > 1
    
    def test_check_message_edge_cases(self):
        """Test various edge cases."""
        # Empty message
        allowed, findings = check_message("")
        assert allowed
        
        # Single character
        allowed, findings = check_message("A")
        assert allowed
        
        # Unicode message
        allowed, findings = check_message("Hello 世界 🌍")
        assert allowed
    
    def test_context_guard_instance_methods(self):
        """Test ContextGuard instance methods."""
        # Test analyze_message method
        attacks = self.context_guard.analyze_message("test_session", "Normal message")
        assert isinstance(attacks, list)
        
        # Test should_block_message method
        should_block, reasons = self.context_guard.should_block_message("test_session", "Normal message")
        assert isinstance(should_block, bool)
        assert isinstance(reasons, list)
    
    def test_check_message_comprehensive(self):
        """Comprehensive test with various message types."""
        test_cases = [
            ("Normal short message", True),
            ("A" * 100, True),  # Longer but still reasonable
            ("The quick brown fox jumps over the lazy dog. " * 10, True),  # Repeated but diverse
        ]
        
        for message, should_pass in test_cases:
            allowed, findings = check_message(message)
            if should_pass:
                assert allowed, f"Message should have passed: '{message[:50]}...'"
            # If should_pass is False, we expect it to be blocked


if __name__ == '__main__':
    pytest.main([__file__])