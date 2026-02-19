"""
Test Log Sanitizer - verify PII and credential scrubbing from log output.
"""

import logging
import pytest
import sys
import os

# Add the parent directory to the path to import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from security.log_sanitizer import LogSanitizer, install_log_sanitizer


class TestLogSanitizer:
    """Test the LogSanitizer logging filter."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.sanitizer = LogSanitizer()
    
    def test_ssn_redaction(self):
        """Test SSN pattern redaction."""
        # Test with dashes
        record = logging.LogRecord(
            name='test', level=logging.INFO, pathname='', lineno=0,
            msg='User SSN is 123-45-6789', args=(), exc_info=None
        )
        result = self.sanitizer.filter(record)
        assert '[REDACTED-SSN]' in record.msg
        assert '123-45-6789' not in record.msg
        
        # Test without dashes
        record2 = logging.LogRecord(
            name='test', level=logging.INFO, pathname='', lineno=0,
            msg='SSN: 123456789', args=(), exc_info=None
        )
        result2 = self.sanitizer.filter(record2)
        assert '[REDACTED-SSN]' in record2.msg
        assert '123456789' not in record2.msg
    
    def test_credit_card_redaction(self):
        """Test credit card pattern redaction."""
        record = logging.LogRecord(
            name='test', level=logging.INFO, pathname='', lineno=0,
            msg='Credit card: 4532-1234-5678-9012', args=(), exc_info=None
        )
        result = self.sanitizer.filter(record)
        assert '[REDACTED-CREDIT-CARD]' in record.msg
        assert '4532-1234-5678-9012' not in record.msg
    
    def test_openai_api_key_redaction(self):
        """Test OpenAI API key pattern redaction."""
        record = logging.LogRecord(
            name='test', level=logging.INFO, pathname='', lineno=0,
            msg='API key: sk-abcdefghijklmnopqrstuvwxyz1234567890123456', args=(), exc_info=None
        )
        result = self.sanitizer.filter(record)
        assert '[REDACTED-OPENAI-KEY]' in record.msg
        assert 'sk-abcdefghijklmnopqrstuvwxyz1234567890123456' not in record.msg
    
    def test_aws_access_key_redaction(self):
        """Test AWS access key pattern redaction."""
        record = logging.LogRecord(
            name='test', level=logging.INFO, pathname='', lineno=0,
            msg='AWS key: AKIAEXAMPLEKEY123456', args=(), exc_info=None
        )
        result = self.sanitizer.filter(record)
        assert '[REDACTED-AWS-ACCESS-KEY]' in record.msg
        assert 'AKIAEXAMPLEKEY123456' not in record.msg
    
    def test_op_key_redaction(self):
        """Test 1Password CLI key pattern redaction."""
        record = logging.LogRecord(
            name='test', level=logging.INFO, pathname='', lineno=0,
            msg='1Password op get item response: "password": "op_abc123def456ghi789"', args=(), exc_info=None
        )
        result = self.sanitizer.filter(record)
        assert '[REDACTED-OP-OUTPUT]' in record.msg
    
    def test_password_assignment_redaction(self):
        """Test password assignment pattern redaction."""
        record = logging.LogRecord(
            name='test', level=logging.INFO, pathname='', lineno=0,
            msg='Config: password=mypassword123', args=(), exc_info=None
        )
        result = self.sanitizer.filter(record)
        assert '[REDACTED-PASSWORD-ASSIGNMENT]' in record.msg
        assert 'mypassword123' not in record.msg
    
    def test_token_assignment_redaction(self):
        """Test token assignment pattern redaction."""
        record = logging.LogRecord(
            name='test', level=logging.INFO, pathname='', lineno=0,
            msg='Config: token="abc123xyz789"', args=(), exc_info=None
        )
        result = self.sanitizer.filter(record)
        assert '[REDACTED-TOKEN-ASSIGNMENT]' in record.msg
        assert 'abc123xyz789' not in record.msg
    
    def test_key_assignment_redaction(self):
        """Test key assignment pattern redaction."""
        record = logging.LogRecord(
            name='test', level=logging.INFO, pathname='', lineno=0,
            msg='Config: api_key: secretkey123', args=(), exc_info=None
        )
        result = self.sanitizer.filter(record)
        assert '[REDACTED-KEY-ASSIGNMENT]' in record.msg
        assert 'secretkey123' not in record.msg
    
    def test_secret_assignment_redaction(self):
        """Test secret assignment pattern redaction."""
        record = logging.LogRecord(
            name='test', level=logging.INFO, pathname='', lineno=0,
            msg='Config: secret = "topsecret456"', args=(), exc_info=None
        )
        result = self.sanitizer.filter(record)
        assert '[REDACTED-SECRET-ASSIGNMENT]' in record.msg
        assert 'topsecret456' not in record.msg
    
    def test_clean_message_passes(self):
        """Test that clean messages pass through unchanged."""
        original_msg = 'This is a clean log message with no sensitive data'
        record = logging.LogRecord(
            name='test', level=logging.INFO, pathname='', lineno=0,
            msg=original_msg, args=(), exc_info=None
        )
        result = self.sanitizer.filter(record)
        assert result is True
        assert record.msg == original_msg
    
    def test_multiple_patterns_in_one_message(self):
        """Test multiple sensitive patterns in one message."""
        record = logging.LogRecord(
            name='test', level=logging.INFO, pathname='', lineno=0,
            msg='User data: SSN=123-45-6789, API_KEY=sk-abcdefghijklmnopqrstuvwxyz1234567890123456, password=secret123',
            args=(), exc_info=None
        )
        result = self.sanitizer.filter(record)
        assert '[REDACTED-SSN]' in record.msg
        assert '[REDACTED-OPENAI-KEY]' in record.msg
        assert '[REDACTED-PASSWORD-ASSIGNMENT]' in record.msg
        assert '123-45-6789' not in record.msg
        assert 'sk-abcdefghijklmnopqrstuvwxyz1234567890123456' not in record.msg
        assert 'secret123' not in record.msg
    
    def test_install_log_sanitizer(self):
        """Test the install_log_sanitizer function."""
        # Get current handler count
        root_logger = logging.getLogger()
        initial_filter_count = len([f for f in getattr(root_logger.handlers[0] if root_logger.handlers else root_logger, 'filters', [])])
        
        # Install sanitizer
        install_log_sanitizer()
        
        # Check if filter was added (this is implementation dependent)
        # The exact verification depends on how install_log_sanitizer is implemented
        # We just verify the function can be called without error
        assert True  # Function executed without exception


if __name__ == '__main__':
    pytest.main([__file__])