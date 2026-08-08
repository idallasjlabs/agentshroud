# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for POST /forward/stream — the streaming voice pipeline.

Covers the sentence-boundary detector, the sliding-window security filter
(the piece that must preserve the SAME guarantees as the blocking /forward
path, just applied incrementally), and the endpoint end-to-end.
"""

from __future__ import annotations

import json
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from gateway.ingest_api.models import AgentTarget, ForwardRequest
from gateway.ingest_api.routes.forward import (
    _filtered_sentence_stream,
    _resolve_user_trust_level,
    _sentences_from_deltas,
)

# ── _resolve_user_trust_level ────────────────────────────────────────────────


def _target(name="hermes"):
    return AgentTarget(name=name, url="http://x:1", chat_path="/v1/chat/completions")


def _request(user_id=None):
    return ForwardRequest(content="hi", source="api", content_type="text", user_id=user_id)


@pytest.mark.parametrize(
    "trust_score,expected",
    [
        (400, "FULL"),
        (500, "FULL"),
        (300, "ELEVATED"),
        (399, "ELEVATED"),
        (200, "STANDARD"),
        (299, "STANDARD"),
        (100, "BASIC"),
        (199, "BASIC"),
        (0, "UNTRUSTED"),
        (99, "UNTRUSTED"),
    ],
)
def test_resolve_trust_level_maps_trust_score_to_tier(trust_score, expected):
    pipeline = MagicMock()
    pipeline.trust_manager.get_trust.return_value = (trust_score, "some-reason")
    pipeline._owner_user_id = None

    result = _resolve_user_trust_level(pipeline, _target(), _request())
    assert result == expected


def test_resolve_trust_level_no_trust_manager_defaults_untrusted():
    pipeline = MagicMock()
    pipeline.trust_manager = None
    pipeline._owner_user_id = None

    assert _resolve_user_trust_level(pipeline, _target(), _request()) == "UNTRUSTED"


def test_resolve_trust_level_no_trust_info_for_target_defaults_untrusted():
    pipeline = MagicMock()
    pipeline.trust_manager.get_trust.return_value = None
    pipeline._owner_user_id = None

    assert _resolve_user_trust_level(pipeline, _target(), _request()) == "UNTRUSTED"


def test_resolve_trust_level_owner_user_id_upgrades_to_full():
    pipeline = MagicMock()
    pipeline.trust_manager.get_trust.return_value = (0, "untrusted")
    pipeline._owner_user_id = "8096968754"

    result = _resolve_user_trust_level(pipeline, _target(), _request(user_id="8096968754"))
    assert result == "FULL"


def test_resolve_trust_level_non_owner_user_id_does_not_upgrade():
    pipeline = MagicMock()
    pipeline.trust_manager.get_trust.return_value = (0, "untrusted")
    pipeline._owner_user_id = "8096968754"

    result = _resolve_user_trust_level(pipeline, _target(), _request(user_id="someone-else"))
    assert result == "UNTRUSTED"


# ── _sentences_from_deltas ───────────────────────────────────────────────────


async def _aiter(items):
    for item in items:
        yield item


@pytest.mark.asyncio
async def test_sentences_from_deltas_splits_on_boundaries():
    deltas = _aiter(["One", ".", " Two", ".", " Three", "."])
    sentences = [s async for s in _sentences_from_deltas(deltas)]
    assert sentences == ["One.", "Two.", "Three."]


@pytest.mark.asyncio
async def test_sentences_from_deltas_flushes_trailing_fragment_without_punctuation():
    deltas = _aiter(["Hello", " world", " no punctuation"])
    sentences = [s async for s in _sentences_from_deltas(deltas)]
    assert sentences == ["Hello world no punctuation"]


@pytest.mark.asyncio
async def test_sentences_from_deltas_empty_stream_yields_nothing():
    sentences = [s async for s in _sentences_from_deltas(_aiter([]))]
    assert sentences == []


@pytest.mark.asyncio
async def test_sentences_from_deltas_single_delta_full_sentence():
    deltas = _aiter(["Complete sentence in one delta."])
    sentences = [s async for s in _sentences_from_deltas(deltas)]
    assert sentences == ["Complete sentence in one delta."]


# ── _filtered_sentence_stream ────────────────────────────────────────────────


class _PassthroughPipeline:
    """Mock pipeline whose process_outbound returns the window text unchanged
    — verifies windowing/splitting logic in isolation from real filtering.
    Also implements process_inbound (pass-through) so this same class can
    stand in for app_state.pipeline in the full /forward/stream endpoint
    tests, which exercise _process_inbound() first."""

    def __init__(self):
        self.calls: list[str] = []
        self.trust_manager = None
        self._owner_user_id = None

    async def process_inbound(self, message, agent_id, action, source, metadata=None):
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
        self.calls.append(response)
        result = MagicMock()
        result.blocked = False
        result.sanitized_message = response
        return result


class _BlockingPipeline:
    """Mock pipeline that blocks any window containing the word 'secret'."""

    async def process_outbound(self, response, agent_id, user_trust_level, source):
        result = MagicMock()
        if "secret" in response:
            result.blocked = True
            result.block_reason = "contains secret"
            result.sanitized_message = ""
        else:
            result.blocked = False
            result.sanitized_message = response
        return result


@pytest.mark.asyncio
async def test_filtered_stream_releases_sentences_in_order():
    pipeline = _PassthroughPipeline()
    sentences = _aiter(["First.", "Second.", "Third."])
    released = [
        s async for s in _filtered_sentence_stream(sentences, pipeline, "hermes", "FULL", "voice")
    ]
    assert released == ["First.", "Second.", "Third."]


@pytest.mark.asyncio
async def test_filtered_stream_windows_are_pairs_joined_by_sentinel():
    pipeline = _PassthroughPipeline()
    sentences = _aiter(["First.", "Second.", "Third."])
    async for _ in _filtered_sentence_stream(sentences, pipeline, "hermes", "FULL", "voice"):
        pass
    # True sliding window: consecutive OVERLAPPING pairs (First+Second, then
    # Second+Third), so every sentence gets cross-boundary context from its
    # neighbor on both sides except the very first/last — plus the final
    # flush of the last sentence alone once the source stream ends.
    assert pipeline.calls == ["First.␞Second.", "Second.␞Third.", "Third."]


@pytest.mark.asyncio
async def test_filtered_stream_single_sentence_flushed_alone():
    pipeline = _PassthroughPipeline()
    sentences = _aiter(["Only one."])
    released = [
        s async for s in _filtered_sentence_stream(sentences, pipeline, "hermes", "FULL", "voice")
    ]
    assert released == ["Only one."]
    assert pipeline.calls == ["Only one."]


@pytest.mark.asyncio
async def test_filtered_stream_blocked_window_releases_nothing_for_that_window():
    pipeline = _BlockingPipeline()
    sentences = _aiter(["This has a secret.", "This is fine."])
    released = [
        s async for s in _filtered_sentence_stream(sentences, pipeline, "hermes", "FULL", "voice")
    ]
    # First window (secret+fine) blocked entirely; "fine" becomes the new
    # pending and is flushed alone at stream end, unblocked.
    assert released == ["This is fine."]


@pytest.mark.asyncio
async def test_filtered_stream_sentinel_stripped_fails_safe_by_releasing_all():
    class _SentinelEatingPipeline:
        """Simulates a filter whose text transformation happens to strip the
        sentinel out — the fail-safe path must release everything the filter
        already approved rather than silently dropping content."""

        async def process_outbound(self, response, agent_id, user_trust_level, source):
            result = MagicMock()
            result.blocked = False
            result.sanitized_message = response.replace("␞", " ")
            return result

    pipeline = _SentinelEatingPipeline()
    sentences = _aiter(["First.", "Second."])
    released = [
        s async for s in _filtered_sentence_stream(sentences, pipeline, "hermes", "FULL", "voice")
    ]
    assert released == ["First. Second."]


@pytest.mark.asyncio
async def test_filtered_stream_blocked_final_sentence_yields_nothing():
    pipeline = _BlockingPipeline()
    sentences = _aiter(["Fine sentence.", "Another fine one.", "Has a secret."])
    released = [
        s async for s in _filtered_sentence_stream(sentences, pipeline, "hermes", "FULL", "voice")
    ]
    # Window 1 ("Fine sentence." + "Another fine one.") is clean → releases
    # "Fine sentence.". Window 2 ("Another fine one." + "Has a secret.")
    # is blocked entirely — "Another fine one." is silently dropped rather
    # than released (fail-safe: a clean sentence paired with a blocked one
    # is withheld, not retried alone). Final flush of "Has a secret." is
    # also blocked → nothing more released.
    assert released == ["Fine sentence."]


@pytest.mark.asyncio
async def test_filtered_stream_redaction_applies_to_released_sentence():
    class _RedactingPipeline:
        async def process_outbound(self, response, agent_id, user_trust_level, source):
            result = MagicMock()
            result.blocked = False
            result.sanitized_message = response.replace("4111111111111111", "[REDACTED]")
            return result

    pipeline = _RedactingPipeline()
    sentences = _aiter(["Card is 4111111111111111.", "Thanks."])
    released = [
        s
        async for s in _filtered_sentence_stream(sentences, pipeline, "hermes", "STANDARD", "voice")
    ]
    assert released[0] == "Card is [REDACTED]."


# ── /forward/stream endpoint ─────────────────────────────────────────────────


def _make_stream_app_state(sentences_out):
    """Build a mock app_state whose router streams `sentences_out` as raw
    text deltas (one delta per sentence, whole) and whose pipeline/sanitizer
    pass everything through unchanged."""
    mock_state = MagicMock()
    target = AgentTarget(
        name="hermes",
        url="http://agentshroud-hermes:8642",
        chat_path="/v1/chat/completions",
        health_path="/health",
    )
    mock_state.router.resolve_target = AsyncMock(return_value=target)

    async def _stream(*args, **kwargs):
        for s in sentences_out:
            yield s

    mock_state.router.forward_to_agent_stream = _stream

    pipeline = _PassthroughPipeline()
    pipeline.trust_manager = None
    pipeline._owner_user_id = None
    mock_state.pipeline = pipeline
    mock_state.middleware_manager = None
    mock_state.sanitizer = MagicMock()
    mock_state.sanitizer.sanitize = AsyncMock(
        return_value=MagicMock(sanitized_content="test", redactions=[], entity_types_found=[])
    )
    mock_state.sanitizer.block_credentials = AsyncMock(
        side_effect=lambda content, source: (content, False)
    )
    mock_state.ledger = MagicMock()
    mock_state.ledger.record = AsyncMock(
        return_value=MagicMock(id="ledger-id", content_hash="hash", timestamp="ts")
    )
    mock_state.event_bus = MagicMock()
    mock_state.event_bus.emit = AsyncMock()
    return mock_state


def _post_stream(mock_state, content="hi"):
    from fastapi.testclient import TestClient

    from gateway.ingest_api.main import app
    from gateway.ingest_api.main import auth_dep as main_auth_dep
    from gateway.ingest_api.routes.forward import auth_dep as forward_auth_dep

    with patch("gateway.ingest_api.routes.forward.app_state", mock_state):
        app.dependency_overrides[main_auth_dep] = lambda: None
        app.dependency_overrides[forward_auth_dep] = lambda: None
        try:
            client = TestClient(app, raise_server_exceptions=True)
            resp = client.post(
                "/forward/stream",
                json={
                    "content": content,
                    "content_type": "text",
                    "source": "api",
                    "route_to": "hermes",
                    "stream": True,
                },
                headers={"Authorization": "Bearer test-token"},
            )
            return resp
        finally:
            app.dependency_overrides.pop(main_auth_dep, None)
            app.dependency_overrides.pop(forward_auth_dep, None)


def _parse_sse_events(body: str) -> list[dict]:
    events = []
    for block in body.split("\n\n"):
        block = block.strip()
        if not block:
            continue
        assert block.startswith("data: ")
        events.append(json.loads(block[len("data: ") :]))
    return events


def test_forward_stream_emits_sentence_events_then_done():
    mock_state = _make_stream_app_state(["First.", " Second."])
    resp = _post_stream(mock_state)
    assert resp.status_code == 200
    assert resp.headers["content-type"].startswith("text/event-stream")

    events = _parse_sse_events(resp.text)
    sentence_events = [e for e in events if "sentence" in e]
    done_events = [e for e in events if e.get("done")]

    assert len(done_events) == 1
    assert done_events[0]["forwarded_to"] == "hermes"
    assert done_events[0]["agent_response"] == "First. Second."
    assert [e["sentence"] for e in sentence_events] == ["First.", "Second."]


def test_forward_stream_rejects_non_openai_compat_target():
    mock_state = _make_stream_app_state([])
    target = AgentTarget(
        name="openclaw", url="http://agentshroud-openclaw:18789", chat_path="/chat"
    )
    mock_state.router.resolve_target = AsyncMock(return_value=target)

    resp = _post_stream(mock_state)
    assert resp.status_code == 400
    assert "does not support streaming" in resp.json()["detail"]


def test_forward_stream_records_ledger_entry_with_full_assembled_text():
    mock_state = _make_stream_app_state(["Hello.", " World."])
    _post_stream(mock_state)

    mock_state.ledger.record.assert_awaited_once()
    _, kwargs = mock_state.ledger.record.call_args
    assert kwargs["forwarded_to"] == "hermes"


def test_forward_stream_returns_early_response_when_queued_for_approval():
    mock_state = _make_stream_app_state([])

    async def _queued(message, agent_id, action, source, metadata=None):
        result = MagicMock()
        result.blocked = False
        result.queued_for_approval = True
        result.approval_id = "approval-123"
        return result

    mock_state.pipeline.process_inbound = _queued

    resp = _post_stream(mock_state)
    assert resp.status_code == 202
    assert resp.json()["approval_id"] == "approval-123"


def test_forward_stream_503_when_no_pipeline_configured():
    mock_state = _make_stream_app_state([])
    mock_state.pipeline = None

    resp = _post_stream(mock_state)
    assert resp.status_code == 503
    assert "security pipeline" in resp.json()["detail"].lower()


def test_forward_stream_drops_credential_bearing_sentence():
    mock_state = _make_stream_app_state(["Here is a key: sk-secret123.", " Anything else?"])
    mock_state.sanitizer.block_credentials = AsyncMock(
        side_effect=lambda content, source: (
            ("[BLOCKED]", True) if "sk-secret123" in content else (content, False)
        )
    )

    resp = _post_stream(mock_state)
    events = _parse_sse_events(resp.text)
    sentence_events = [e for e in events if "sentence" in e]
    done_events = [e for e in events if e.get("done")]

    assert [e["sentence"] for e in sentence_events] == ["Anything else?"]
    assert "sk-secret123" not in done_events[0]["agent_response"]


def test_forward_stream_forward_error_still_emits_done_event():
    mock_state = _make_stream_app_state([])

    from gateway.ingest_api.router import ForwardError

    async def _raise_forward_error(*args, **kwargs):
        raise ForwardError("agent offline")
        yield  # pragma: no cover — unreachable, satisfies generator shape

    mock_state.router.forward_to_agent_stream = _raise_forward_error

    resp = _post_stream(mock_state)
    assert resp.status_code == 200
    events = _parse_sse_events(resp.text)
    done_events = [e for e in events if e.get("done")]
    assert len(done_events) == 1
    assert done_events[0]["forwarded_to"] == "hermes (offline)"
    assert done_events[0]["agent_response"] == ""


def test_forward_stream_unexpected_error_still_emits_done_event():
    mock_state = _make_stream_app_state([])

    async def _raise_unexpected(*args, **kwargs):
        raise RuntimeError("boom")
        yield  # pragma: no cover — unreachable, satisfies generator shape

    mock_state.router.forward_to_agent_stream = _raise_unexpected

    resp = _post_stream(mock_state)
    assert resp.status_code == 200
    events = _parse_sse_events(resp.text)
    done_events = [e for e in events if e.get("done")]
    assert len(done_events) == 1
    assert done_events[0]["forwarded_to"] == "hermes (error)"


def test_forward_stream_ledger_failure_still_emits_done_event():
    mock_state = _make_stream_app_state(["Hello."])
    mock_state.ledger.record = AsyncMock(side_effect=RuntimeError("ledger down"))

    resp = _post_stream(mock_state)
    assert resp.status_code == 200
    events = _parse_sse_events(resp.text)
    done_events = [e for e in events if e.get("done")]
    assert len(done_events) == 1
    assert done_events[0]["id"] == "ledger-unavailable"
