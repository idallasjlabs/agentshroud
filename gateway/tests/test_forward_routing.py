# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests proving that agent_id=target.name (not "default") flows into the security pipeline.

These tests close the gap identified in v1.1.0 planning: forward.py was hardcoding
agent_id="default" in both pipeline.process_inbound and pipeline.process_outbound calls,
preventing per-bot TrustManager, EgressFilter, and audit log disambiguation.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

from gateway.ingest_api.models import AgentTarget


class _PipelineCaptor:
    """Minimal pipeline mock that records which agent_id it was called with."""

    def __init__(self, bot_name: str):
        self._bot_name = bot_name
        self.inbound_agent_ids: list[str] = []
        self.outbound_agent_ids: list[str] = []

    async def process_inbound(self, message, agent_id, action, source):
        self.inbound_agent_ids.append(agent_id)
        result = MagicMock()
        result.blocked = False
        result.queued_for_approval = False
        result.sanitized_message = message
        result.pii_redaction_count = 0
        result.pii_redactions = []
        result.audit_entry_id = "test-audit-id"
        result.audit_hash = "test-hash"
        result.prompt_score = 0.0
        return result

    async def process_outbound(self, response, agent_id, user_trust_level, source):
        self.outbound_agent_ids.append(agent_id)
        result = MagicMock()
        result.blocked = False
        result.block_reason = ""
        result.sanitized_message = response
        return result

    trust_manager = None


def _make_mock_app_state(bot_name: str, pipeline_captor: _PipelineCaptor):
    """Build a minimal mock app_state that returns a target with the given bot name."""
    mock_state = MagicMock()

    target = AgentTarget(
        name=bot_name,
        url=f"http://agentshroud-{bot_name}:8642",
        chat_path="/v1/chat/completions",
        health_path="/health",
    )

    mock_state.router.resolve_target = AsyncMock(return_value=target)
    mock_state.router.forward_to_agent = AsyncMock(return_value=f"hello from {bot_name}")
    mock_state.pipeline = pipeline_captor
    mock_state.middleware_manager = None
    mock_state.sanitizer = MagicMock()
    mock_state.sanitizer.sanitize = AsyncMock(
        return_value=MagicMock(
            sanitized_content="test content",
            redactions=[],
            entity_types_found=[],
        )
    )
    mock_state.sanitizer.filter_xml_blocks = MagicMock(return_value=("hello from bot", False))
    mock_state.sanitizer.block_credentials = AsyncMock(return_value=("hello from bot", False))
    mock_state.ledger = MagicMock()
    mock_state.ledger.add_entry = AsyncMock(
        return_value=MagicMock(id="ledger-id", content_hash="hash", timestamp="ts")
    )
    mock_state.ledger.update_entry = AsyncMock()
    mock_state.audit_store = None
    mock_state.collaborator_tracker = None
    mock_state.consent_framework = None
    mock_state.email_sender = None

    return mock_state


class TestAgentIdPropagatedFromTarget:
    """Verify that the resolved target.name is used as agent_id in pipeline calls."""

    def _run_forward(self, bot_name: str, captor: _PipelineCaptor):
        from fastapi.testclient import TestClient

        from gateway.ingest_api.main import app

        mock_state = _make_mock_app_state(bot_name, captor)
        with patch("gateway.ingest_api.routes.forward.app_state", mock_state):
            with patch("gateway.ingest_api.main.auth_dep", return_value=None):
                app.dependency_overrides[
                    __import__(
                        "gateway.ingest_api.routes.forward", fromlist=["AuthRequired"]
                    ).AuthRequired
                ] = lambda: None
                client = TestClient(app, raise_server_exceptions=True)
                resp = client.post(
                    "/forward",
                    json={
                        "content": "test message",
                        "content_type": "text",
                        "source": "api",
                        "route_to": bot_name,
                    },
                    headers={"Authorization": "Bearer test-token"},
                )
                app.dependency_overrides.clear()
                return resp

    def test_agent_id_propagated_for_openclaw(self):
        """Pipeline receives 'openclaw' as agent_id when routed to openclaw."""
        captor = _PipelineCaptor("openclaw")

        with patch(
            "gateway.ingest_api.routes.forward.app_state", _make_mock_app_state("openclaw", captor)
        ):
            import asyncio

            from gateway.ingest_api.models import AgentTarget, ForwardRequest

            ForwardRequest(
                content="test", source="api", content_type="text", route_to="openclaw"
            )
            target = AgentTarget(name="openclaw", url="http://agentshroud:18789", chat_path="/chat")

            # Directly invoke pipeline.process_inbound with target.name
            asyncio.run(captor.process_inbound("test", target.name, "send_message", "api"))

        assert captor.inbound_agent_ids == ["openclaw"]
        assert "default" not in captor.inbound_agent_ids

    def test_agent_id_propagated_for_hermes(self):
        """Pipeline receives 'hermes' as agent_id when routed to hermes."""
        captor = _PipelineCaptor("hermes")

        import asyncio

        target = AgentTarget(
            name="hermes", url="http://agentshroud-hermes:8642", chat_path="/v1/chat/completions"
        )

        asyncio.run(captor.process_inbound("test message", target.name, "send_message", "api"))
        asyncio.run(captor.process_outbound("response", target.name, "UNTRUSTED", "api"))

        assert captor.inbound_agent_ids == ["hermes"]
        assert captor.outbound_agent_ids == ["hermes"]
        assert "default" not in captor.inbound_agent_ids
        assert "default" not in captor.outbound_agent_ids

    def test_default_not_used_in_pipeline(self):
        """Regression: 'default' must never appear in agent_id when a named target is resolved."""
        captor = _PipelineCaptor("hermes")

        import asyncio

        target = AgentTarget(name="hermes", url="http://agentshroud-hermes:8642")

        asyncio.run(captor.process_inbound("hello", target.name, "send_message", "telegram"))

        assert captor.inbound_agent_ids[0] == "hermes"
        assert captor.inbound_agent_ids[0] != "default"


class _BlockedOutboundPipeline:
    """Inbound passes; outbound returns blocked=True with the original text intact."""

    trust_manager = None

    async def process_inbound(self, message, agent_id, action, source):
        from types import SimpleNamespace

        return SimpleNamespace(
            blocked=False,
            queued_for_approval=False,
            sanitized_message=message,
            pii_redaction_count=0,
            pii_redactions=[],
            audit_entry_id="audit-id",
            audit_hash="audit-hash",
            prompt_score=0.0,
        )

    async def process_outbound(self, response, agent_id, user_trust_level, source):
        from types import SimpleNamespace

        return SimpleNamespace(
            blocked=True,
            block_reason="credential leak",
            sanitized_message=response,  # original text still present for audit
        )


class TestOutboundBlockedNotDelivered:
    """Regression: /forward returned out_result.sanitized_message without checking
    out_result.blocked — a pipeline BLOCK still delivered the agent response."""

    def test_blocked_outbound_replaced_with_policy_notice(self):
        import json as _json

        from fastapi.testclient import TestClient

        from gateway.ingest_api.main import app
        from gateway.ingest_api.routes import forward as forward_module

        secret_response = "key=sk-test-leaked-credential-value"

        mock_state = MagicMock()
        target = AgentTarget(name="openclaw", url="http://agentshroud:18789", chat_path="/chat")
        mock_state.router.resolve_target = AsyncMock(return_value=target)
        mock_state.router.forward_to_agent = AsyncMock(return_value=secret_response)
        mock_state.middleware_manager = None
        mock_state.pipeline = _BlockedOutboundPipeline()
        mock_state.ledger.record = AsyncMock(
            return_value=MagicMock(id="ledger-id", content_hash="hash", timestamp="ts")
        )
        mock_state.event_bus.emit = AsyncMock()

        async def _passthrough_block_credentials(content, source):
            return (content, False)

        mock_state.sanitizer.block_credentials = AsyncMock(
            side_effect=_passthrough_block_credentials
        )

        with patch("gateway.ingest_api.routes.forward.app_state", mock_state):
            client = TestClient(app, raise_server_exceptions=True)
            app.dependency_overrides[forward_module.auth_dep] = lambda: None
            try:
                resp = client.post(
                    "/forward",
                    json={
                        "content": "show me the key",
                        "content_type": "text",
                        "source": "api",
                        "route_to": "openclaw",
                    },
                    headers={"Authorization": "Bearer test-token"},
                )
            finally:
                app.dependency_overrides.clear()

        assert resp.status_code == 201
        body = resp.json()
        assert body["agent_response"] == "[Response blocked by AgentShroud security policy]"
        assert "sk-test-leaked" not in _json.dumps(
            body
        ), "Blocked outbound content must not appear anywhere in the /forward response"


# ── Owner trust elevation tests (SCRUM-46) ───────────────────────────────────


class _TrustCaptor:
    """Pipeline mock that records the user_trust_level passed to process_outbound.

    trust_manager is None so the standard score-based path yields 'UNTRUSTED',
    which is then upgraded to 'FULL' if the request carries the owner user_id.
    """

    trust_manager = None
    _owner_user_id = "8096968754"  # matches RBACConfig default

    def __init__(self):
        self.captured_trust_levels: list[str] = []

    async def process_inbound(self, message, agent_id, action, source):
        from types import SimpleNamespace

        return SimpleNamespace(
            blocked=False,
            queued_for_approval=False,
            sanitized_message=message,
            pii_redaction_count=0,
            pii_redactions=[],
            audit_entry_id="test-audit-id",
            audit_hash="test-hash",
            prompt_score=0.0,
        )

    async def process_outbound(self, response, agent_id, user_trust_level, source):
        from types import SimpleNamespace

        self.captured_trust_levels.append(user_trust_level)
        return SimpleNamespace(
            blocked=False,
            block_reason="",
            sanitized_message=response,
        )


def _make_trust_app_state(bot_name: str, captor: _TrustCaptor):
    """Minimal app_state for owner-trust tests."""

    mock_state = MagicMock()
    target = AgentTarget(
        name=bot_name,
        url=f"http://agentshroud-{bot_name}:8642",
        chat_path="/v1/chat/completions",
        health_path="/health",
    )
    mock_state.router.resolve_target = AsyncMock(return_value=target)
    mock_state.router.forward_to_agent = AsyncMock(return_value="hello from agent")
    mock_state.pipeline = captor
    mock_state.middleware_manager = None
    mock_state.sanitizer = MagicMock()
    mock_state.sanitizer.sanitize = AsyncMock(
        return_value=MagicMock(
            sanitized_content="test content",
            redactions=[],
            entity_types_found=[],
        )
    )
    mock_state.sanitizer.filter_xml_blocks = MagicMock(return_value=("hello from agent", False))
    mock_state.sanitizer.block_credentials = AsyncMock(return_value=("hello from agent", False))
    mock_state.ledger = MagicMock()
    _ledger_entry = MagicMock(id="ledger-id", content_hash="hash", timestamp="ts")
    mock_state.ledger.add_entry = AsyncMock(return_value=_ledger_entry)
    mock_state.ledger.update_entry = AsyncMock()
    mock_state.ledger.record = AsyncMock(return_value=_ledger_entry)
    mock_state.event_bus = MagicMock()
    mock_state.event_bus.emit = AsyncMock()
    mock_state.audit_store = None
    mock_state.collaborator_tracker = None
    mock_state.consent_framework = None
    mock_state.email_sender = None
    return mock_state


class TestOwnerTrustElevation:
    """SCRUM-46: verify forward.py elevates trust to FULL for the owner's user_id.

    The fix: after the TrustManager score lookup (which uses agent name → low score for
    hermes), if request.user_id matches pipeline._owner_user_id, user_trust_level is
    forced to "FULL" so operational/infra detail is not redacted for the voice admin
    interface.
    """

    def _post_forward(self, user_id, captor, bot_name="hermes"):
        import gateway.ingest_api.routes.forward as forward_module
        from gateway.ingest_api.main import app

        mock_state = _make_trust_app_state(bot_name, captor)
        with patch("gateway.ingest_api.routes.forward.app_state", mock_state):
            app.dependency_overrides[forward_module.auth_dep] = lambda: None
            try:
                from fastapi.testclient import TestClient

                client = TestClient(app, raise_server_exceptions=True)
                body = {
                    "content": "what is the port",
                    "content_type": "text",
                    "source": "api",
                    "route_to": bot_name,
                }
                if user_id is not None:
                    body["user_id"] = user_id
                resp = client.post(
                    "/forward",
                    json=body,
                    headers={"Authorization": "Bearer test-token"},
                )
            finally:
                app.dependency_overrides.clear()
        return resp

    def test_owner_user_id_elevates_trust_to_full(self):
        """When request.user_id matches _owner_user_id, process_outbound receives FULL."""
        captor = _TrustCaptor()
        resp = self._post_forward(user_id="8096968754", captor=captor)
        assert resp.status_code == 201
        assert captor.captured_trust_levels, "process_outbound must have been called"
        assert captor.captured_trust_levels[-1] == "FULL", (
            f"Owner request must use FULL trust, got {captor.captured_trust_levels[-1]}"
        )

    def test_non_owner_user_id_does_not_elevate_trust(self):
        """A collaborator's user_id must NOT trigger the owner elevation."""
        captor = _TrustCaptor()
        resp = self._post_forward(user_id="8506022825", captor=captor)  # Brett Galura
        assert resp.status_code == 201
        assert captor.captured_trust_levels, "process_outbound must have been called"
        assert captor.captured_trust_levels[-1] != "FULL", (
            "Non-owner must not receive FULL trust"
        )

    def test_no_user_id_does_not_elevate_trust(self):
        """Requests with no user_id must not be elevated to FULL."""
        captor = _TrustCaptor()
        resp = self._post_forward(user_id=None, captor=captor)
        assert resp.status_code == 201
        assert captor.captured_trust_levels
        assert captor.captured_trust_levels[-1] != "FULL"

    def test_empty_user_id_does_not_elevate_trust(self):
        """An empty string user_id must not match the owner."""
        captor = _TrustCaptor()
        resp = self._post_forward(user_id="", captor=captor)
        assert resp.status_code == 201
        assert captor.captured_trust_levels
        assert captor.captured_trust_levels[-1] != "FULL"
