# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for Tool Result PII Sanitization

Comprehensive tests for the tool result PII scanning system that intercepts
and sanitizes tool results before they reach the agent context.
"""

from __future__ import annotations

import asyncio
from typing import Any, Dict
from unittest.mock import AsyncMock, Mock, patch

import pytest

from gateway.ingest_api.config import PIIConfig
from gateway.ingest_api.middleware import MiddlewareManager
from gateway.ingest_api.models import RedactionDetail, RedactionResult
from gateway.security.tool_result_sanitizer import (
    ToolResultPIIConfig,
    ToolResultSanitizer,
)


class TestToolResultPIIConfig:
    """Test the ToolResultPIIConfig configuration class"""

    def test_default_config(self):
        """Test default configuration"""
        config = ToolResultPIIConfig()
        assert config.enabled is True
        assert config.default_config is not None
        assert config.tool_overrides == {}

    def test_tool_specific_config(self):
        """Test tool-specific configuration overrides"""
        default_config = PIIConfig(entities=["US_SSN", "EMAIL_ADDRESS"], min_confidence=0.8)
        overrides = {
            "icloud": {"entities": ["US_SSN", "CREDIT_CARD", "PHONE_NUMBER"], "min_confidence": 0.7}
        }

        config = ToolResultPIIConfig(default_config=default_config, tool_overrides=overrides)

        # Test default tool config
        default_tool_config = config.get_config_for_tool("unknown_tool")
        assert default_tool_config.entities == ["US_SSN", "EMAIL_ADDRESS"]
        assert default_tool_config.min_confidence == 0.8

        # Test tool-specific config
        icloud_config = config.get_config_for_tool("icloud")
        assert icloud_config.entities == ["US_SSN", "CREDIT_CARD", "PHONE_NUMBER"]
        assert icloud_config.min_confidence == 0.7


class TestToolResultSanitizer:
    """Test the ToolResultSanitizer class"""

    @pytest.fixture
    def default_config(self):
        """Default PII configuration for tests"""
        return PIIConfig(
            entities=["US_SSN", "CREDIT_CARD", "PHONE_NUMBER", "EMAIL_ADDRESS"], min_confidence=0.8
        )

    @pytest.fixture
    def tool_config(self, default_config):
        """Tool result PII configuration for tests"""
        return ToolResultPIIConfig(
            enabled=True,
            default_config=default_config,
            tool_overrides={
                "icloud": {
                    "entities": [
                        "US_SSN",
                        "CREDIT_CARD",
                        "PHONE_NUMBER",
                        "EMAIL_ADDRESS",
                        "LOCATION",
                    ],
                    "min_confidence": 0.7,
                },
                "web_search": {"entities": ["US_SSN", "CREDIT_CARD"], "min_confidence": 0.9},
            },
        )

    @pytest.fixture
    def sanitizer(self, tool_config):
        """Tool result sanitizer instance for tests"""
        return ToolResultSanitizer(tool_config)

    def test_initialization(self, tool_config):
        """Test sanitizer initialization"""
        sanitizer = ToolResultSanitizer(tool_config)
        assert sanitizer.config == tool_config
        assert sanitizer._sanitizers == {}

    def test_extract_scannable_content_string(self, sanitizer):
        """Test content extraction from string results"""
        content = sanitizer._extract_scannable_content("Test string with SSN: 123-45-6789")
        assert content == "Test string with SSN: 123-45-6789"

    def test_extract_scannable_content_dict(self, sanitizer):
        """Test content extraction from dictionary results"""
        test_dict = {
            "name": "John Doe",
            "ssn": "123-45-6789",
            "contact": {"phone": "555-123-4567", "email": "john@example.com"},
            "metadata": {"id": 12345, "active": True},
        }

        content = sanitizer._extract_scannable_content(test_dict)
        assert "John Doe" in content
        assert "123-45-6789" in content
        assert "555-123-4567" in content
        assert "john@example.com" in content
        assert "12345" in content
        # Boolean should be converted to string
        assert "True" in content

    def test_extract_scannable_content_list(self, sanitizer):
        """Test content extraction from list results"""
        test_list = [
            "First item with SSN: 123-45-6789",
            {"email": "test@example.com"},
            "Third item with phone: 555-123-4567",
        ]

        content = sanitizer._extract_scannable_content(test_list)
        assert "123-45-6789" in content
        assert "test@example.com" in content
        assert "555-123-4567" in content

    @pytest.mark.asyncio
    async def test_sanitize_disabled(self, default_config):
        """Test sanitizer when disabled"""
        disabled_config = ToolResultPIIConfig(enabled=False, default_config=default_config)
        sanitizer = ToolResultSanitizer(disabled_config)

        test_content = "SSN: 123-45-6789"
        result, redaction_result = await sanitizer.sanitize_tool_result(
            "test_tool", test_content, "test_session"
        )

        assert result == test_content  # Unchanged
        assert len(redaction_result.redactions) == 0
        assert redaction_result.entity_types_found == []

    @pytest.mark.asyncio
    async def test_sanitize_string_with_pii(self, sanitizer):
        """Test sanitizing string content with PII"""
        test_content = "Contact info: SSN 123-45-6789, email john@example.com"

        # Mock the underlying PIISanitizer
        with patch("gateway.security.tool_result_sanitizer.PIISanitizer") as mock_sanitizer_class:
            mock_sanitizer = AsyncMock()
            mock_sanitizer.sanitize.return_value = RedactionResult(
                sanitized_content="Contact info: SSN <US_SSN>, email <EMAIL_ADDRESS>",
                redactions=[
                    RedactionDetail(
                        entity_type="US_SSN", start=17, end=28, score=0.9, replacement="<US_SSN>"
                    ),
                    RedactionDetail(
                        entity_type="EMAIL_ADDRESS",
                        start=36,
                        end=52,
                        score=0.95,
                        replacement="<EMAIL_ADDRESS>",
                    ),
                ],
                entity_types_found=["US_SSN", "EMAIL_ADDRESS"],
            )
            mock_sanitizer_class.return_value = mock_sanitizer

            result, redaction_result = await sanitizer.sanitize_tool_result(
                "test_tool", test_content, "test_session"
            )

            assert result == "Contact info: SSN <US_SSN>, email <EMAIL_ADDRESS>"
            assert len(redaction_result.redactions) == 2
            assert "US_SSN" in redaction_result.entity_types_found
            assert "EMAIL_ADDRESS" in redaction_result.entity_types_found

    @pytest.mark.asyncio
    async def test_sanitize_dict_with_pii(self, sanitizer):
        """Test sanitizing dictionary content with PII"""
        test_dict = {"user": "John Doe", "ssn": "123-45-6789", "safe_data": "This is fine"}

        with patch("gateway.security.tool_result_sanitizer.PIISanitizer") as mock_sanitizer_class:
            mock_sanitizer = AsyncMock()
            mock_sanitizer.sanitize.return_value = RedactionResult(
                sanitized_content="John Doe\n<US_SSN>\nThis is fine",
                redactions=[
                    RedactionDetail(
                        entity_type="US_SSN", start=9, end=20, score=0.95, replacement="<US_SSN>"
                    )
                ],
                entity_types_found=["US_SSN"],
            )
            mock_sanitizer_class.return_value = mock_sanitizer

            result, redaction_result = await sanitizer.sanitize_tool_result(
                "icloud", test_dict, "test_session"
            )

            # Dictionary with PII should be restructured with sanitized content
            assert isinstance(result, dict)
            assert result["pii_redacted"] is True
            assert result["original_type"] == "dict"
            assert "<US_SSN>" in result["sanitized_result"]
            assert len(redaction_result.redactions) == 1

    @pytest.mark.asyncio
    async def test_tool_specific_configuration(self, sanitizer):
        """Test that different tools get different PII configurations"""
        # This test verifies that the sanitizer creates different PIISanitizer instances
        # for different tools with their specific configurations

        test_content = "Test content"

        with patch("gateway.security.tool_result_sanitizer.PIISanitizer") as mock_sanitizer_class:
            mock_sanitizer = AsyncMock()
            mock_sanitizer.sanitize.return_value = RedactionResult(
                sanitized_content=test_content, redactions=[], entity_types_found=[]
            )
            mock_sanitizer_class.return_value = mock_sanitizer

            # Call with icloud tool
            await sanitizer.sanitize_tool_result("icloud", test_content)

            # Call with web_search tool
            await sanitizer.sanitize_tool_result("web_search", test_content)

            # Should have created two different PIISanitizer instances
            assert mock_sanitizer_class.call_count == 2

            # Verify different configurations were used
            call_configs = [call[1]["config"] for call in mock_sanitizer_class.call_args_list]

            # icloud should have 5 entities with 0.7 confidence
            icloud_config = call_configs[0]
            assert len(icloud_config.entities) == 5
            assert icloud_config.min_confidence == 0.7

            # web_search should have 2 entities with 0.9 confidence
            websearch_config = call_configs[1]
            assert len(websearch_config.entities) == 2
            assert websearch_config.min_confidence == 0.9

    @pytest.mark.asyncio
    async def test_empty_content_handling(self, sanitizer):
        """Test handling of empty or whitespace-only content"""
        empty_cases = ["", "   ", "\n\t  ", None]

        for empty_content in empty_cases:
            result, redaction_result = await sanitizer.sanitize_tool_result(
                "test_tool", empty_content or "", "test_session"
            )

            assert len(redaction_result.redactions) == 0
            assert redaction_result.entity_types_found == []


class TestMiddlewareIntegration:
    """Test integration with MiddlewareManager"""

    @pytest.fixture
    def mock_config(self):
        """Mock configuration for middleware tests"""
        config = Mock()
        config.tool_result_pii = {
            "enabled": True,
            "tool_overrides": {
                "icloud": {"entities": ["US_SSN", "CREDIT_CARD"], "min_confidence": 0.7}
            },
        }
        config.pii = PIIConfig()
        return config

    def test_middleware_set_config(self, mock_config):
        """Test middleware configuration setup"""
        middleware = MiddlewareManager()

        # Should not raise an exception
        middleware.set_config(mock_config)

        # Tool result sanitizer should be configured
        assert middleware.tool_result_sanitizer is not None
        assert middleware.tool_result_sanitizer.config.enabled is True

    def test_middleware_set_config_disabled(self):
        """Test middleware configuration with disabled tool result PII"""
        config = Mock()
        config.tool_result_pii = {"enabled": False}
        config.pii = PIIConfig()

        middleware = MiddlewareManager()
        middleware.set_config(config)

        assert middleware.tool_result_sanitizer is not None
        assert middleware.tool_result_sanitizer.config.enabled is False

    def test_middleware_set_config_missing(self):
        """Test middleware configuration with missing tool_result_pii config"""
        config = Mock()
        config.tool_result_pii = None
        config.pii = PIIConfig()

        middleware = MiddlewareManager()

        # Should handle missing config gracefully
        with patch("gateway.ingest_api.middleware.logger") as mock_logger:
            middleware.set_config(config)
            mock_logger.warning.assert_called_once()

    @pytest.mark.asyncio
    async def test_process_tool_result_success(self, mock_config):
        """Test successful tool result processing"""
        middleware = MiddlewareManager()
        middleware.set_config(mock_config)

        test_content = "Test result with SSN: 123-45-6789"

        with patch.object(
            middleware.tool_result_sanitizer, "sanitize_tool_result"
        ) as mock_sanitize:
            mock_sanitize.return_value = (
                "Test result with SSN: <US_SSN>",
                RedactionResult(
                    sanitized_content="Test result with SSN: <US_SSN>",
                    redactions=[
                        RedactionDetail(
                            entity_type="US_SSN",
                            start=20,
                            end=31,
                            score=0.95,
                            replacement="<US_SSN>",
                        )
                    ],
                    entity_types_found=["US_SSN"],
                ),
            )

            result, was_modified = await middleware.process_tool_result(
                "icloud", test_content, "test_session"
            )

            assert result == "Test result with SSN: <US_SSN>"
            assert was_modified is True
            mock_sanitize.assert_called_once_with(
                tool_name="icloud", tool_result=test_content, session_id="test_session"
            )

    @pytest.mark.asyncio
    async def test_process_tool_result_no_sanitizer(self, mock_config):
        """Test tool result processing when sanitizer not configured"""
        middleware = MiddlewareManager()
        # Don't call set_config, so sanitizer remains None

        test_content = "Test content"

        result, was_modified = await middleware.process_tool_result(
            "test_tool", test_content, "test_session"
        )

        assert result == test_content  # Unchanged
        assert was_modified is False

    @pytest.mark.asyncio
    async def test_process_tool_result_sanitizer_error(self, mock_config):
        """Test tool result processing when sanitizer raises an exception"""
        middleware = MiddlewareManager()
        middleware.set_config(mock_config)

        test_content = "Test content"

        with patch.object(
            middleware.tool_result_sanitizer, "sanitize_tool_result"
        ) as mock_sanitize:
            mock_sanitize.side_effect = Exception("Sanitizer error")

            result, was_modified = await middleware.process_tool_result(
                "test_tool", test_content, "test_session"
            )

            # Should fail gracefully and return original content
            assert result == test_content
            assert was_modified is False


class TestConfigurationLoading:
    """Test configuration loading and validation"""

    def test_config_with_tool_result_pii(self):
        """Test that configuration includes tool result PII settings"""
        # This test would ideally load from an actual config file
        # For now, we test the structure
        from gateway.ingest_api.config import GatewayConfig

        config = GatewayConfig()

        # Should have tool_result_pii field with defaults
        assert hasattr(config, "tool_result_pii")
        assert isinstance(config.tool_result_pii, dict)
        assert "enabled" in config.tool_result_pii
        assert "tool_overrides" in config.tool_result_pii


# Integration test scenarios
class TestRealWorldScenarios:
    """Test realistic tool result scenarios"""

    @pytest.mark.asyncio
    async def test_icloud_contact_scanning(self):
        """Test scanning iCloud contact data for PII"""
        config = ToolResultPIIConfig(
            enabled=True,
            default_config=PIIConfig(),
            tool_overrides={
                "icloud": {"entities": ["PHONE_NUMBER", "EMAIL_ADDRESS"], "min_confidence": 0.7}
            },
        )
        sanitizer = ToolResultSanitizer(config)

        # Simulate iCloud contacts result
        icloud_result = {
            "contacts": [
                {"name": "John Doe", "phone": "555-123-4567", "email": "john.doe@example.com"},
                {"name": "Jane Smith", "phone": "555-987-6543", "email": "jane.smith@company.com"},
            ],
            "total": 2,
        }

        with patch("gateway.security.tool_result_sanitizer.PIISanitizer") as mock_sanitizer_class:
            mock_sanitizer = AsyncMock()
            mock_sanitizer.sanitize.return_value = RedactionResult(
                sanitized_content="John Doe\n<PHONE_NUMBER>\n<EMAIL_ADDRESS>\nJane Smith\n<PHONE_NUMBER>\n<EMAIL_ADDRESS>\n2",
                redactions=[
                    RedactionDetail(
                        entity_type="PHONE_NUMBER",
                        start=9,
                        end=21,
                        score=0.9,
                        replacement="<PHONE_NUMBER>",
                    ),
                    RedactionDetail(
                        entity_type="EMAIL_ADDRESS",
                        start=22,
                        end=43,
                        score=0.95,
                        replacement="<EMAIL_ADDRESS>",
                    ),
                    RedactionDetail(
                        entity_type="PHONE_NUMBER",
                        start=55,
                        end=67,
                        score=0.9,
                        replacement="<PHONE_NUMBER>",
                    ),
                    RedactionDetail(
                        entity_type="EMAIL_ADDRESS",
                        start=68,
                        end=93,
                        score=0.95,
                        replacement="<EMAIL_ADDRESS>",
                    ),
                ],
                entity_types_found=["PHONE_NUMBER", "EMAIL_ADDRESS"],
            )
            mock_sanitizer_class.return_value = mock_sanitizer

            result, redaction_result = await sanitizer.sanitize_tool_result(
                "icloud", icloud_result, "user_123"
            )

            # Should detect and redact PII from contacts
            assert len(redaction_result.redactions) == 4
            assert "PHONE_NUMBER" in redaction_result.entity_types_found
            assert "EMAIL_ADDRESS" in redaction_result.entity_types_found
            assert isinstance(result, dict)  # Should be restructured due to PII
            assert result["pii_redacted"] is True

    @pytest.mark.asyncio
    async def test_email_content_scanning(self):
        """Test scanning email content for sensitive data"""
        config = ToolResultPIIConfig(
            enabled=True,
            default_config=PIIConfig(),
            tool_overrides={
                "email": {
                    "entities": ["US_SSN", "CREDIT_CARD", "EMAIL_ADDRESS"],
                    "min_confidence": 0.8,
                }
            },
        )
        sanitizer = ToolResultSanitizer(config)

        # Simulate email with sensitive content
        email_content = """
        Subject: Account Information
        
        Dear Customer,
        
        Your account details:
        SSN: 123-45-6789
        Card: 4111-1111-1111-1111
        Contact: support@bank.com
        
        Best regards,
        Customer Service
        """

        with patch("gateway.security.tool_result_sanitizer.PIISanitizer") as mock_sanitizer_class:
            mock_sanitizer = AsyncMock()
            mock_sanitizer.sanitize.return_value = RedactionResult(
                sanitized_content=email_content.replace("123-45-6789", "<US_SSN>")
                .replace("4111-1111-1111-1111", "<CREDIT_CARD>")
                .replace("support@bank.com", "<EMAIL_ADDRESS>"),
                redactions=[
                    RedactionDetail(
                        entity_type="US_SSN", start=0, end=11, score=0.95, replacement="<US_SSN>"
                    ),
                    RedactionDetail(
                        entity_type="CREDIT_CARD",
                        start=0,
                        end=19,
                        score=0.9,
                        replacement="<CREDIT_CARD>",
                    ),
                    RedactionDetail(
                        entity_type="EMAIL_ADDRESS",
                        start=0,
                        end=16,
                        score=0.98,
                        replacement="<EMAIL_ADDRESS>",
                    ),
                ],
                entity_types_found=["US_SSN", "CREDIT_CARD", "EMAIL_ADDRESS"],
            )
            mock_sanitizer_class.return_value = mock_sanitizer

            result, redaction_result = await sanitizer.sanitize_tool_result(
                "email", email_content, "user_456"
            )

            # Should catch all three types of PII
            assert len(redaction_result.redactions) == 3
            entity_types = set(redaction_result.entity_types_found)
            assert entity_types == {"US_SSN", "CREDIT_CARD", "EMAIL_ADDRESS"}


if __name__ == "__main__":
    # Run tests with: python3 -m pytest gateway/tests/test_tool_result_pii.py -v
    pytest.main(["-v", __file__])
