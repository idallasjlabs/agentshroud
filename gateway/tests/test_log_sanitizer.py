# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Test Log Sanitizer - verify PII and credential scrubbing from log output."""

import logging
from gateway.security.log_sanitizer import LogSanitizer, install_log_sanitizer


class TestLogSanitizer:
    def setup_method(self):
        self.sanitizer = LogSanitizer()

    def _filter_msg(self, msg):
        rec = logging.LogRecord("test", logging.INFO, "", 0, msg, (), None)
        self.sanitizer.filter(rec)
        return rec.msg

    def test_ssn_redacted(self):
        result = self._filter_msg("User SSN is 123-45-6789")
        assert "123-45-6789" not in result
        assert "REDACTED" in result

    def test_credit_card_redacted(self):
        result = self._filter_msg("CC: 4532-1234-5678-9012")
        assert "4532-1234-5678-9012" not in result
        assert "REDACTED" in result

    def test_aws_key_redacted(self):
        result = self._filter_msg("AWS key: AKIAEXAMPLEKEY123456")
        assert "AKIAEXAMPLEKEY123456" not in result
        assert "REDACTED" in result

    def test_openai_key_redacted(self):
        # OpenAI keys are sk- followed by 48 alphanumeric chars
        key = "sk-" + "a" * 48
        result = self._filter_msg(f"Key: {key}")
        assert key not in result
        assert "REDACTED" in result

    def test_password_assignment_redacted(self):
        result = self._filter_msg("password=mypassword123")
        assert "mypassword123" not in result

    def test_token_assignment_redacted(self):
        result = self._filter_msg('token="abc123xyz789"')
        assert "abc123xyz789" not in result

    def test_secret_assignment_redacted(self):
        result = self._filter_msg('secret = "topsecret456"')
        assert "topsecret456" not in result

    def test_user_path_redacted(self):
        result = self._filter_msg("File at /home/isaiah/docs/secret.txt")
        assert "isaiah" not in result
        assert "[USER]" in result

    def test_clean_message_unchanged(self):
        msg = "This is a clean log message with no sensitive data"
        result = self._filter_msg(msg)
        assert result == msg

    def test_filter_always_returns_true(self):
        rec = logging.LogRecord("test", logging.INFO, "", 0, "test", (), None)
        assert self.sanitizer.filter(rec) is True

    def test_install_log_sanitizer_no_error(self):
        install_log_sanitizer()  # Should not raise
