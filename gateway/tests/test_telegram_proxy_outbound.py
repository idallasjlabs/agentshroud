"""Tests for TelegramAPIProxy outbound security pipeline integration.

Proves that _filter_outbound() runs the full security pipeline
(PII sanitizer, OutboundInfoFilter, OutputCanary) on all outbound messages.

Created: 2026-03-08 — Fixes C-0 (outbound pipeline bypass)
"""
import json
import pytest
from gateway.proxy.telegram_proxy import TelegramAPIProxy
from gateway.ingest_api.sanitizer import PIISanitizer
from gateway.ingest_api.config import PIIConfig


def _make_sanitizer():
    """Create a PIISanitizer with default enforce config."""
    config = PIIConfig()
    return PIISanitizer(config, mode="enforce", action="redact")


class TestOutboundPipelineIntegration:
    """Tests that _filter_outbound calls the full security pipeline."""

    @pytest.mark.asyncio
    async def test_pii_redacted_on_outbound(self):
        """Phone numbers in outbound messages must be redacted by PII sanitizer.

        Regression test for the collaborator privacy leak where all 10
        authorized sender phone numbers were exposed unredacted.
        """
        sanitizer = _make_sanitizer()
        proxy = TelegramAPIProxy(sanitizer=sanitizer)

        body = json.dumps({
            "chat_id": "7614658040",
            "text": "The authorized senders are: 8096968754, 8506022825, 8545356403"
        }).encode()

        result = await proxy._filter_outbound(body, "application/json")
        result_data = json.loads(result)

        assert "8096968754" not in result_data["text"], "Phone number leaked through outbound filter"
        assert "8506022825" not in result_data["text"], "Phone number leaked through outbound filter"
        assert "8545356403" not in result_data["text"], "Phone number leaked through outbound filter"

    @pytest.mark.asyncio
    async def test_ssn_redacted_on_outbound(self):
        """SSN in outbound messages must be redacted."""
        sanitizer = _make_sanitizer()
        proxy = TelegramAPIProxy(sanitizer=sanitizer)

        body = json.dumps({
            "chat_id": "12345",
            "text": "Your SSN is 987-65-4321 as requested."
        }).encode()

        result = await proxy._filter_outbound(body, "application/json")
        result_data = json.loads(result)

        assert "987-65-4321" not in result_data["text"], "SSN leaked through outbound filter"

    @pytest.mark.asyncio
    async def test_outbound_pipeline_called_when_available(self):
        """When pipeline is set, process_outbound must be called on outbound messages."""
        pipeline_called = False

        class MockPipeline:
            async def process_outbound(self, text, **kwargs):
                nonlocal pipeline_called
                pipeline_called = True
                from dataclasses import dataclass
                @dataclass
                class Result:
                    blocked = False
                    sanitized_message = text
                    block_reason = ""
                return Result()

        sanitizer = _make_sanitizer()
        proxy = TelegramAPIProxy(pipeline=MockPipeline(), sanitizer=sanitizer)

        body = json.dumps({
            "chat_id": "12345",
            "text": "Hello world"
        }).encode()

        await proxy._filter_outbound(body, "application/json")
        assert pipeline_called, "Pipeline.process_outbound must be called for outbound messages"

    @pytest.mark.asyncio
    async def test_outbound_fails_closed_for_non_owner(self):
        """If pipeline crashes, non-owner messages must be blocked."""
        class CrashingPipeline:
            async def process_outbound(self, text, **kwargs):
                raise RuntimeError("Intentional crash")

        sanitizer = _make_sanitizer()
        proxy = TelegramAPIProxy(pipeline=CrashingPipeline(), sanitizer=sanitizer)

        class MockRBAC:
            owner_user_id = "9999999999"
        proxy._rbac = MockRBAC()

        body = json.dumps({
            "chat_id": "7614658040",
            "text": "Some response with secrets"
        }).encode()

        result = await proxy._filter_outbound(body, "application/json")
        result_data = json.loads(result)

        assert "security pipeline" in result_data["text"].lower(),             "Non-owner messages must be blocked when pipeline crashes"
        assert "Some response with secrets" not in result_data["text"],             "Original content must not leak through on pipeline crash"

    @pytest.mark.asyncio
    async def test_outbound_owner_exempt_from_fail_closed(self):
        """If pipeline crashes, owner messages should still go through."""
        class CrashingPipeline:
            async def process_outbound(self, text, **kwargs):
                raise RuntimeError("Intentional crash")

        sanitizer = _make_sanitizer()
        proxy = TelegramAPIProxy(pipeline=CrashingPipeline(), sanitizer=sanitizer)

        class MockRBAC:
            owner_user_id = "8096968754"
        proxy._rbac = MockRBAC()

        body = json.dumps({
            "chat_id": "8096968754",
            "text": "Owner response should pass through"
        }).encode()

        result = await proxy._filter_outbound(body, "application/json")
        result_data = json.loads(result)

        assert "security pipeline" not in result_data["text"].lower(),             "Owner messages should not be blocked on pipeline crash"
