# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Test Environment Leakage Guard."""
from __future__ import annotations


from gateway.security.env_guard import check_command, scrub_output


class TestCheckCommand:
    def test_blocks_proc_environ(self):
        allowed, reason = check_command("cat /proc/self/environ")
        assert not allowed

    def test_blocks_proc_star_environ(self):
        allowed, reason = check_command("cat /proc/1/environ")
        assert not allowed

    def test_blocks_printenv(self):
        allowed, reason = check_command("printenv SECRET_KEY")
        assert not allowed

    def test_blocks_env_pipe(self):
        allowed, reason = check_command("env | grep PASSWORD")
        assert not allowed

    def test_blocks_dollar_env(self):
        allowed, reason = check_command('perl -e "print $ENV{SECRET}"')
        assert not allowed

    def test_allows_safe_command(self):
        allowed, reason = check_command("ls -la /tmp")
        assert allowed

    def test_allows_env_in_name(self):
        allowed, reason = check_command("cat environment.txt")
        assert allowed


class TestScrubOutput:
    def test_scrubs_openai_key(self):
        key = "sk-" + "a" * 48
        result = scrub_output(f"Found key: {key}")
        assert key not in result

    def test_scrubs_aws_key(self):
        result = scrub_output("Key: AKIAIOSFODNN7EXAMPLE")
        assert "AKIAIOSFODNN7EXAMPLE" not in result

    def test_scrubs_github_token(self):
        token = "ghp_" + "a" * 36
        result = scrub_output(f"Token: {token}")
        assert token not in result

    def test_clean_text_unchanged(self):
        text = "This is clean output with no secrets"
        result = scrub_output(text)
        assert result == text

    def test_scrubs_multiple_keys(self):
        aws = "AKIAIOSFODNN7EXAMPLE"
        text = f"Keys: {aws} and ghp_{'b' * 36}"
        result = scrub_output(text)
        assert aws not in result
