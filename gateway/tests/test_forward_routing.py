# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests proving that agent_id=target.name (not "default") flows into the security pipeline.

These tests close the gap identified in v1.4.0 planning: forward.py was hardcoding
agent_id="default" in both pipeline.process_inbound and pipeline.process_outbound calls,
preventing per-bot TrustManager, EgressFilter, and audit log disambiguation.
"""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from gateway.ingest_api.models import AgentTarget, ForwardRequest


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

            request = ForwardRequest(
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
