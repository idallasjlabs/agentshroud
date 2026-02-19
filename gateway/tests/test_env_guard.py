"""
Test Environment Leakage Guard - verify dangerous commands blocked and API keys scrubbed.
"""

import pytest
import sys
import os

# Add the parent directory to the path to import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from security.env_guard import check_command, scrub_output, EnvironmentGuard


class TestEnvironmentGuard:
    """Test the Environment Leakage Guard functionality."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.env_guard = EnvironmentGuard()
    
    def test_check_command_proc_self_environ(self):
        """Test blocking /proc/self/environ access."""
        allowed, reason = check_command("cat /proc/self/environ")
        assert not allowed
        assert "environment access detected" in reason.lower()
    
    def test_check_command_proc_star_environ(self):
        """Test blocking /proc/*/environ access."""
        allowed, reason = check_command("cat /proc/1234/environ")
        assert not allowed
        assert "environment access detected" in reason.lower()
    
    def test_check_command_printenv(self):
        """Test blocking printenv command."""
        allowed, reason = check_command("printenv")
        assert not allowed
        assert "environment access detected" in reason.lower()
    
    def test_check_command_env_pipe(self):
        """Test blocking 'env |' command."""
        allowed, reason = check_command("env | grep PATH")
        assert not allowed
        assert "environment access detected" in reason.lower()
    
    def test_check_command_dollar_env(self):
        """Test blocking $ENV{ patterns."""
        allowed, reason = check_command('echo $ENV{PATH}')
        assert not allowed
        assert "environment variable access detected" in reason.lower()
    
    def test_check_command_safe_command(self):
        """Test that safe commands are allowed."""
        allowed, reason = check_command("ls -la")
        assert allowed
        assert "allowed" in reason.lower()
    
    def test_check_command_safe_with_env_in_name(self):
        """Test that commands with 'env' in filename are allowed."""
        allowed, reason = check_command("python environment_setup.py")
        assert allowed
        assert "allowed" in reason.lower()
    
    def test_scrub_output_openai_key(self):
        """Test scrubbing OpenAI API keys from output."""
        text = "Your API key is: sk-abcdefghijklmnopqrstuvwxyz1234567890123456"
        scrubbed = scrub_output(text)
        assert "sk-abcdefghijklmnopqrstuvwxyz1234567890123456" not in scrubbed
        assert "[SCRUBBED-OPENAI_KEY]" in scrubbed
    
    def test_scrub_output_aws_access_key(self):
        """Test scrubbing AWS access keys from output."""
        text = "AWS_ACCESS_KEY_ID=AKIAEXAMPLEKEY123456"
        scrubbed = scrub_output(text)
        assert "AKIAEXAMPLEKEY123456" not in scrubbed
        assert "[SCRUBBED-AWS_ACCESS_KEY]" in scrubbed
    
    def test_scrub_output_aws_secret_key(self):
        """Test scrubbing AWS secret keys from output."""
        text = "AWS_SECRET_ACCESS_KEY=wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY"
        scrubbed = scrub_output(text)
        assert "wJalrXUtnFEMI/K7MDENG/bPxRfiCYzEXAMPLEKEY" not in scrubbed
        assert "[SCRUBBED-AWS_SECRET_KEY]" in scrubbed
    
    def test_scrub_output_github_token(self):
        """Test scrubbing GitHub tokens from output."""
        text = "GITHUB_TOKEN=ghp_abcdefghijklmnopqrstuvwxyz123456"
        scrubbed = scrub_output(text)
        assert "ghp_abcdefghijklmnopqrstuvwxyz123456" not in scrubbed
        assert "[SCRUBBED-GITHUB_TOKEN]" in scrubbed
    
    def test_scrub_output_op_key(self):
        """Test scrubbing 1Password keys from output."""
        text = "1Password key: op_abcdefghijklmnopqrstuvwx"
        scrubbed = scrub_output(text)
        assert "op_abcdefghijklmnopqrstuvwx" not in scrubbed
        assert "[SCRUBBED-OP_KEY]" in scrubbed
    
    def test_scrub_output_multiple_keys(self):
        """Test scrubbing multiple API keys from same output."""
        text = """
        OpenAI: sk-abcdefghijklmnopqrstuvwxyz1234567890123456
        AWS: AKIAEXAMPLEKEY123456
        GitHub: ghp_abcdefghijklmnopqrstuvwxyz123456
        """
        scrubbed = scrub_output(text)
        assert "sk-abcdefghijklmnopqrstuvwxyz1234567890123456" not in scrubbed
        assert "AKIAEXAMPLEKEY123456" not in scrubbed
        assert "ghp_abcdefghijklmnopqrstuvwxyz123456" not in scrubbed
        assert "[SCRUBBED-OPENAI_KEY]" in scrubbed
        assert "[SCRUBBED-AWS_ACCESS_KEY]" in scrubbed
        assert "[SCRUBBED-GITHUB_TOKEN]" in scrubbed
    
    def test_scrub_output_clean_text(self):
        """Test that clean text passes through unchanged."""
        text = "This is clean output with no API keys or secrets."
        scrubbed = scrub_output(text)
        assert text == scrubbed
    
    def test_scrub_output_partial_matches(self):
        """Test that partial matches don't trigger false positives."""
        text = "The word 'key' and 'sk' should not trigger scrubbing."
        scrubbed = scrub_output(text)
        assert text == scrubbed
    
    def test_env_guard_instance_methods(self):
        """Test EnvironmentGuard instance methods."""
        # Test check_command_execution method
        allowed = self.env_guard.check_command_execution("ls -la", "test_agent")
        assert allowed
        
        blocked = self.env_guard.check_command_execution("printenv", "test_agent")
        assert not blocked


if __name__ == '__main__':
    pytest.main([__file__])