# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for CollaboratorGreeter (gateway/proxy/collaborator_greeter.py)."""
from __future__ import annotations

import asyncio
import json
import time
import unittest.mock
from pathlib import Path

import httpx
import pytest
import pytest_asyncio

from gateway.proxy.collaborator_greeter import CollaboratorGreeter, _CAPTION_MAX


# ── helpers ────────────────────────────────────────────────────────────────────

def _make_greeter(tmp_path, taglines=None, mock_client=None, cooldown=86400):
    taglines_path = tmp_path / "taglines.json"
    if taglines is not None:
        taglines_path.write_text(json.dumps(taglines))
    else:
        taglines_path.write_text(json.dumps(["Test tagline."]))

    logo_path = tmp_path / "logo.png"
    logo_path.write_bytes(b"\x89PNG\r\n")  # minimal PNG header

    state_path = str(tmp_path / "greetings.json")

    return CollaboratorGreeter(
        state_path=state_path,
        taglines_path=str(taglines_path),
        logo_path=str(logo_path),
        gateway_telegram_base="http://gateway:8080/telegram-api",
        cooldown_seconds=cooldown,
        http_client=mock_client,
    )


def _ok_response():
    resp = unittest.mock.AsyncMock(spec=httpx.Response)
    resp.status_code = 200
    return resp


def _err_response(status=500):
    resp = unittest.mock.AsyncMock(spec=httpx.Response)
    resp.status_code = status
    resp.text = "internal error"
    return resp


# ── happy path ─────────────────────────────────────────────────────────────────

@pytest.mark.asyncio
async def test_first_call_sends_greeting_and_persists_state(tmp_path):
    mock_client = unittest.mock.AsyncMock(spec=httpx.AsyncClient)
    mock_client.post.return_value = _ok_response()
    g = _make_greeter(tmp_path, mock_client=mock_client)

    result = await g.maybe_greet(
        bot_token="TOKEN", bot_id="hermes", user_id="123", first_name="Isaiah"
    )

    assert result is True
    mock_client.post.assert_called_once()
    state = json.loads(Path(g._state_path).read_text())
    assert "hermes:123" in state


@pytest.mark.asyncio
async def test_repeat_within_24h_is_suppressed(tmp_path):
    mock_client = unittest.mock.AsyncMock(spec=httpx.AsyncClient)
    mock_client.post.return_value = _ok_response()
    g = _make_greeter(tmp_path, mock_client=mock_client, cooldown=86400)
    # Pre-seed state with a recent epoch (1 hour ago)
    g._state["hermes:456"] = time.time() - 3600
    g._persist_state()

    result = await g.maybe_greet(
        bot_token="TOKEN", bot_id="hermes", user_id="456", first_name="Bob"
    )

    assert result is False
    mock_client.post.assert_not_called()


@pytest.mark.asyncio
async def test_repeat_after_24h_greets_again(tmp_path):
    mock_client = unittest.mock.AsyncMock(spec=httpx.AsyncClient)
    mock_client.post.return_value = _ok_response()
    g = _make_greeter(tmp_path, mock_client=mock_client, cooldown=86400)
    g._state["hermes:789"] = time.time() - 86401  # 24h + 1s ago
    g._persist_state()

    result = await g.maybe_greet(
        bot_token="TOKEN", bot_id="hermes", user_id="789", first_name="Alice"
    )

    assert result is True
    mock_client.post.assert_called_once()


@pytest.mark.asyncio
async def test_random_tagline_pulled_from_file(tmp_path):
    taglines = ["First tagline.", "Second tagline.", "Third tagline."]
    mock_client = unittest.mock.AsyncMock(spec=httpx.AsyncClient)
    mock_client.post.return_value = _ok_response()
    g = _make_greeter(tmp_path, taglines=taglines, mock_client=mock_client)

    with unittest.mock.patch("random.choice", return_value="Second tagline.") as mc:
        await g.maybe_greet(
            bot_token="TOKEN", bot_id="hermes", user_id="111", first_name="Test"
        )
        mc.assert_called_once_with(taglines)

    call_kwargs = mock_client.post.call_args
    files = call_kwargs.kwargs.get("files") or call_kwargs[1].get("files", {})
    caption = files.get("caption", (None, ""))[1]
    assert "Second tagline." in caption


@pytest.mark.asyncio
async def test_missing_taglines_falls_back_to_default(tmp_path):
    mock_client = unittest.mock.AsyncMock(spec=httpx.AsyncClient)
    mock_client.post.return_value = _ok_response()
    logo_path = tmp_path / "logo.png"
    logo_path.write_bytes(b"\x89PNG")
    g = CollaboratorGreeter(
        state_path=str(tmp_path / "state.json"),
        taglines_path=str(tmp_path / "nonexistent.json"),
        logo_path=str(logo_path),
        http_client=mock_client,
    )
    assert g._taglines == ["Your agent can do anything— except get away with it."]


@pytest.mark.asyncio
async def test_first_name_none_uses_there_fallback(tmp_path):
    mock_client = unittest.mock.AsyncMock(spec=httpx.AsyncClient)
    mock_client.post.return_value = _ok_response()
    g = _make_greeter(tmp_path, mock_client=mock_client)

    await g.maybe_greet(
        bot_token="TOKEN", bot_id="hermes", user_id="222", first_name=None
    )

    files = mock_client.post.call_args.kwargs.get("files") or {}
    caption = files.get("caption", (None, ""))[1]
    assert caption.startswith("Hello, there")


@pytest.mark.asyncio
async def test_send_failure_does_not_persist_state(tmp_path):
    mock_client = unittest.mock.AsyncMock(spec=httpx.AsyncClient)
    mock_client.post.return_value = _err_response(500)
    g = _make_greeter(tmp_path, mock_client=mock_client)

    result = await g.maybe_greet(
        bot_token="TOKEN", bot_id="hermes", user_id="333", first_name="Dave"
    )

    assert result is False
    assert "hermes:333" not in g._state  # state NOT written on failure


@pytest.mark.asyncio
async def test_bot_isolation(tmp_path):
    mock_client = unittest.mock.AsyncMock(spec=httpx.AsyncClient)
    mock_client.post.return_value = _ok_response()
    g = _make_greeter(tmp_path, mock_client=mock_client, cooldown=86400)

    # Greet on hermes — state written for hermes:999
    await g.maybe_greet(bot_token="T1", bot_id="hermes", user_id="999", first_name="X")
    assert "hermes:999" in g._state

    # Immediately greet on openclaw — independent cooldown, should send
    mock_client.post.return_value = _ok_response()
    result = await g.maybe_greet(
        bot_token="T2", bot_id="openclaw", user_id="999", first_name="X"
    )
    assert result is True
    assert "openclaw:999" in g._state


@pytest.mark.asyncio
async def test_state_file_corruption_recovers(tmp_path):
    mock_client = unittest.mock.AsyncMock(spec=httpx.AsyncClient)
    mock_client.post.return_value = _ok_response()
    state_path = tmp_path / "state.json"
    state_path.write_text("{corrupt json[}")  # intentionally malformed

    logo_path = tmp_path / "logo.png"
    logo_path.write_bytes(b"\x89PNG")
    taglines_path = tmp_path / "t.json"
    taglines_path.write_text('["tag"]')

    g = CollaboratorGreeter(
        state_path=str(state_path),
        taglines_path=str(taglines_path),
        logo_path=str(logo_path),
        http_client=mock_client,
    )
    # Greeter should have recovered with empty state
    assert g._state == {}
    result = await g.maybe_greet(
        bot_token="T", bot_id="hermes", user_id="1", first_name="Y"
    )
    assert result is True


def test_caption_length_clamped(tmp_path):
    very_long_tagline = "A" * 2000
    logo_path = tmp_path / "logo.png"
    logo_path.write_bytes(b"\x89PNG")
    taglines_path = tmp_path / "t.json"
    taglines_path.write_text(json.dumps([very_long_tagline]))
    g = CollaboratorGreeter(
        state_path=str(tmp_path / "s.json"),
        taglines_path=str(taglines_path),
        logo_path=str(logo_path),
    )
    with unittest.mock.patch("random.choice", return_value=very_long_tagline):
        raw = f"Hello, Test — AgentShroud at your service.\n\n{very_long_tagline}"
        clamped = raw[:_CAPTION_MAX]
        assert len(clamped) == _CAPTION_MAX


@pytest.mark.asyncio
async def test_missing_logo_returns_false(tmp_path):
    mock_client = unittest.mock.AsyncMock(spec=httpx.AsyncClient)
    taglines_path = tmp_path / "t.json"
    taglines_path.write_text('["tag"]')
    g = CollaboratorGreeter(
        state_path=str(tmp_path / "s.json"),
        taglines_path=str(taglines_path),
        logo_path="/nonexistent/logo.png",
        http_client=mock_client,
    )
    result = await g.maybe_greet(
        bot_token="T", bot_id="hermes", user_id="1", first_name="Test"
    )
    assert result is False
    mock_client.post.assert_not_called()


@pytest.mark.asyncio
async def test_exception_in_maybe_greet_returns_false(tmp_path):
    """Unexpected exception in maybe_greet must be caught and return False."""
    mock_client = unittest.mock.AsyncMock(spec=httpx.AsyncClient)
    mock_client.post.side_effect = RuntimeError("network borked")
    g = _make_greeter(tmp_path, mock_client=mock_client)
    result = await g.maybe_greet(
        bot_token="T", bot_id="hermes", user_id="500", first_name="Z"
    )
    assert result is False


def test_load_taglines_with_non_list_json_falls_back(tmp_path):
    """_load_taglines falls back to default when JSON is valid but not a list."""
    taglines_path = tmp_path / "bad.json"
    taglines_path.write_text('{"key": "value"}')
    logo_path = tmp_path / "logo.png"
    logo_path.write_bytes(b"\x89PNG")
    g = CollaboratorGreeter(
        state_path=str(tmp_path / "s.json"),
        taglines_path=str(taglines_path),
        logo_path=str(logo_path),
    )
    assert g._taglines == ["Your agent can do anything— except get away with it."]


def test_load_state_non_dict_json_returns_empty(tmp_path):
    """_load_state returns {} when state file is a JSON list (not a dict)."""
    state_path = tmp_path / "state.json"
    state_path.write_text('[1, 2, 3]')  # valid JSON but not a dict
    logo_path = tmp_path / "logo.png"
    logo_path.write_bytes(b"\x89PNG")
    taglines_path = tmp_path / "t.json"
    taglines_path.write_text('["tag"]')
    g = CollaboratorGreeter(
        state_path=str(state_path),
        taglines_path=str(taglines_path),
        logo_path=str(logo_path),
    )
    assert g._state == {}


def test_persist_state_exception_is_swallowed(tmp_path):
    """_persist_state failure must not raise."""
    logo_path = tmp_path / "logo.png"
    logo_path.write_bytes(b"\x89PNG")
    taglines_path = tmp_path / "t.json"
    taglines_path.write_text('["tag"]')
    g = CollaboratorGreeter(
        state_path="/nonexistent_dir/state.json",
        taglines_path=str(taglines_path),
        logo_path=str(logo_path),
    )
    g._state["k"] = 1.0
    g._persist_state()  # must not raise despite unwritable path


def test_load_state_write_empty_fails_silently(tmp_path):
    """When state JSON is corrupt AND writing the empty recovery file fails, no exception."""
    state_path = tmp_path / "state.json"
    state_path.write_text("{bad}")  # corrupt JSON
    logo_path = tmp_path / "logo.png"
    logo_path.write_bytes(b"\x89PNG")
    taglines_path = tmp_path / "t.json"
    taglines_path.write_text('["tag"]')
    with unittest.mock.patch("pathlib.Path.write_text", side_effect=OSError("disk full")):
        g = CollaboratorGreeter(
            state_path=str(state_path),
            taglines_path=str(taglines_path),
            logo_path=str(logo_path),
        )
    assert g._state == {}


def test_load_state_loads_existing_valid_dict(tmp_path):
    """_load_state reads and returns a pre-existing valid JSON dict."""
    state_path = tmp_path / "state.json"
    state_path.write_text(json.dumps({"hermes:999": 1234567890.0}))
    logo_path = tmp_path / "logo.png"
    logo_path.write_bytes(b"\x89PNG")
    taglines_path = tmp_path / "t.json"
    taglines_path.write_text('["tag"]')
    g = CollaboratorGreeter(
        state_path=str(state_path),
        taglines_path=str(taglines_path),
        logo_path=str(logo_path),
    )
    assert g._state == {"hermes:999": 1234567890.0}


def test_get_client_creates_own_when_not_injected(tmp_path):
    """CollaboratorGreeter creates its own httpx client lazily."""
    logo_path = tmp_path / "logo.png"
    logo_path.write_bytes(b"\x89PNG")
    taglines_path = tmp_path / "t.json"
    taglines_path.write_text('["tag"]')
    g = CollaboratorGreeter(
        state_path=str(tmp_path / "s.json"),
        taglines_path=str(taglines_path),
        logo_path=str(logo_path),
        http_client=None,  # explicitly no injected client
    )
    assert g._http_client is None
    assert g._own_client is None
    client1 = g._get_client()
    client2 = g._get_client()
    assert isinstance(client1, httpx.AsyncClient)
    assert client1 is client2  # same lazy-created instance
