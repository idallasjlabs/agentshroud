# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for Metadata Channel Guard"""
from __future__ import annotations


from gateway.security.metadata_guard import MetadataGuard


class TestMetadataGuard:

    def setup_method(self):
        self.guard = MetadataGuard()

    def test_sanitize_headers_strips_sensitive(self):
        """Test that sensitive headers are stripped."""
        headers = {
            "Server": "nginx/1.18.0",
            "X-Powered-By": "PHP/7.4.0",
            "Content-Type": "text/html",
        }

        sanitized = self.guard.sanitize_headers(headers)

        assert "Server" not in sanitized
        assert "X-Powered-By" not in sanitized
        assert sanitized["Content-Type"] == "text/html"

    def test_sanitize_headers_redacts_internal_ips(self):
        """Test that internal IPs are redacted from headers."""
        headers = {
            "Via": "1.1 proxy1.internal (Apache), 192.168.1.100:8080",
            "X-Forwarded-For": "203.0.113.0, 10.0.0.1, 172.16.0.1",
            "X-Real-IP": "127.0.0.1",
        }

        sanitized = self.guard.sanitize_headers(headers)

        assert "[REDACTED]" in sanitized["Via"]
        assert "[REDACTED]" in sanitized["X-Forwarded-For"]
        assert "[REDACTED]" in sanitized["X-Real-IP"]
        assert "203.0.113.0" in sanitized["X-Forwarded-For"]  # Public IP preserved

    def test_sanitize_filename_strips_control_chars(self):
        """Test that unicode control characters are stripped."""
        filename = "test\u200bfile\u202ename.txt"
        sanitized = self.guard.sanitize_filename(filename)

        assert "\u200b" not in sanitized
        assert "\u202e" not in sanitized
        assert sanitized == "testfilename.txt"

    def test_sanitize_filename_normalizes_unicode(self):
        """Test that unicode is normalized with NFKC."""
        # Using decomposed unicode characters
        filename = "café.txt"  # With decomposed é
        sanitized = self.guard.sanitize_filename(filename)

        # Should be normalized
        assert sanitized == "café.txt"

    def test_check_for_exif_detects_magic_bytes(self):
        """Test EXIF detection."""
        # Data with EXIF magic bytes
        data_with_exif = b"some data before" + b"Exif\x00\x00" + b"more data"
        data_without_exif = b"just regular image data"

        assert self.guard.check_for_exif(data_with_exif) is True
        assert self.guard.check_for_exif(data_without_exif) is False
        assert self.guard.check_for_exif(b"") is False

    def test_check_oversized_headers_flags_large_headers(self):
        """Test that oversized headers are flagged."""
        # Create headers that exceed 8KB
        large_value = "x" * 9000
        headers = {"Large-Header": large_value}

        result = self.guard.check_oversized_headers(headers)

        assert result is not None
        assert "exceeds limit" in result
        assert "8192" in result

    def test_check_oversized_headers_passes_normal_headers(self):
        """Test that normal-sized headers pass."""
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer token123",
            "User-Agent": "Mozilla/5.0 (compatible)",
        }

        result = self.guard.check_oversized_headers(headers)

        assert result is None

    def test_sanitize_headers_truncates_on_size_limit(self):
        """Test that header sanitization stops at size limit."""
        # Create multiple headers that together exceed limit
        headers = {}
        for i in range(100):
            headers[f"Header-{i}"] = "x" * 100

        sanitized = self.guard.sanitize_headers(headers)

        # Should have fewer headers than input due to size limit
        assert len(sanitized) < len(headers)

    def test_sanitize_image_metadata_removes_exif(self):
        """Test that EXIF metadata is removed from image data."""
        # Create test data with EXIF
        prefix = b"\xff\xd8\xff\xe1"  # JPEG header
        exif_data = b"Exif\x00\x00some exif metadata here"
        suffix = b"\xff\xd9"  # JPEG footer

        original_data = prefix + exif_data + suffix
        sanitized_data = self.guard.sanitize_image_metadata(original_data)

        # EXIF should be removed
        assert b"Exif\x00\x00" not in sanitized_data
        assert len(sanitized_data) < len(original_data)

    def test_sanitize_image_metadata_preserves_non_exif(self):
        """Test that non-EXIF data is preserved."""
        data_without_exif = b"\xff\xd8\xff\xe0regular image data\xff\xd9"

        sanitized_data = self.guard.sanitize_image_metadata(data_without_exif)

        # Data should be unchanged
        assert sanitized_data == data_without_exif

    def test_internal_ip_patterns_comprehensive(self):
        """Test comprehensive internal IP pattern matching."""
        test_cases = [
            ("10.0.0.1", True),
            ("192.168.1.100", True),
            ("172.16.0.1", True),
            ("172.31.255.254", True),
            ("127.0.0.1", True),
            ("169.254.1.1", True),
            ("203.0.113.1", False),  # Public IP
            ("8.8.8.8", False),  # Public IP
            ("172.15.0.1", False),  # Not in private range
            ("172.32.0.1", False),  # Not in private range
        ]

        for ip, should_match in test_cases:
            text = f"Via: proxy {ip}:8080"
            sanitized = self.guard.sanitize_headers({"Via": text})

            if should_match:
                assert "[REDACTED]" in sanitized["Via"], f"Should redact {ip}"
            else:
                assert ip in sanitized["Via"], f"Should preserve {ip}"

    def test_all_unicode_control_chars_stripped(self):
        """Test that all specified unicode control characters are stripped."""
        control_chars = [
            "\u200b",  # Zero width space
            "\u200c",  # Zero width non-joiner
            "\u200d",  # Zero width joiner
            "\u200e",  # Left-to-right mark
            "\u200f",  # Right-to-left mark
            "\u202a",  # Left-to-right embedding
            "\u202b",  # Right-to-left embedding
            "\u202c",  # Pop directional formatting
            "\u202d",  # Left-to-right override
            "\u202e",  # Right-to-left override
        ]

        for char in control_chars:
            filename = f"test{char}file.txt"
            sanitized = self.guard.sanitize_filename(filename)
            assert char not in sanitized
            assert sanitized == "testfile.txt"
