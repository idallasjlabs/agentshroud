# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for SlackSocketClient — gateway-side Slack Socket Mode listener.

Verifies that the client correctly processes events_api envelopes, acknowledges
them, calls proxy.handle_event(), and handles disconnect/reconnect cycles.
"""

from __future__ import annotations

import asyncio
import json
from unittest.mock import AsyncMock, MagicMock, call, patch

import pytest

from gateway.proxy.slack_socket_client import SlackSocketClient, compute_backoff


def _make_client(proxy=None) -> SlackSocketClient:
    if proxy is None:
        proxy = MagicMock()
        proxy.handle_event = AsyncMock()
    return SlackSocketClient(proxy=proxy, app_token="xapp-test-token")


class TestComputeBackoff:
    """Unit tests for the reconnect backoff calculation."""

    def test_grows_exponentially_with_attempt(self):
        """With jitter pinned to max, backoff doubles per attempt until the cap."""
        waits = [compute_backoff(a, base=1.0, cap=60.0, rand=lambda: 1.0) for a in range(7)]
        assert waits == [1.0, 2.0, 4.0, 8.0, 16.0, 32.0, 60.0]

    def test_capped_at_cap_for_large_attempts(self):
        """Backoff never exceeds the cap, even for huge attempt counts."""
        assert compute_backoff(50, base=1.0, cap=60.0, rand=lambda: 1.0) == 60.0
        assert compute_backoff(10_000, base=1.0, cap=60.0, rand=lambda: 1.0) == 60.0

    def test_jitter_stays_within_half_to_full_ceiling(self):
        """Jitter scales the wait between 50% and 100% of the ceiling."""
        assert compute_backoff(3, base=1.0, cap=60.0, rand=lambda: 0.0) == 4.0
        assert compute_backoff(3, base=1.0, cap=60.0, rand=lambda: 1.0) == 8.0
        for _ in range(50):
            wait = compute_backoff(3, base=1.0, cap=60.0)  # real random jitter
            assert 4.0 <= wait <= 8.0

    def test_first_attempt_uses_base(self):
        """Attempt 0 waits at most the base interval (1s default)."""
        assert compute_backoff(0, rand=lambda: 1.0) == 1.0
        assert compute_backoff(0, rand=lambda: 0.0) == 0.5

    @pytest.mark.asyncio
    async def test_run_resets_backoff_after_successful_connect(self, monkeypatch):
        """A successful WSS connection resets the attempt counter to 0."""
        client = _make_client()
        sleeps: list[float] = []
        backoff_attempts: list[int] = []

        async def fake_get_wss_url():
            return "wss://example"

        connect_count = 0

        async def fake_connect_and_handle(url):
            nonlocal connect_count
            connect_count += 1
            if connect_count <= 2:
                # Two straight failures before any connection is established
                raise ConnectionError("blip")
            if connect_count == 3:
                # Successful connection, then the link drops
                client._connect_ok = True
                raise ConnectionError("dropped after connect")
            client.stop()

        async def fake_sleep(wait):
            sleeps.append(wait)

        def fake_backoff(attempt):
            backoff_attempts.append(attempt)
            return 0.0

        monkeypatch.setattr(client, "_get_wss_url", fake_get_wss_url)
        monkeypatch.setattr(client, "_connect_and_handle", fake_connect_and_handle)
        monkeypatch.setattr(
            "gateway.proxy.slack_socket_client.compute_backoff", fake_backoff
        )
        monkeypatch.setattr(
            "gateway.proxy.slack_socket_client.asyncio.sleep", fake_sleep
        )

        await client.run()

        # Attempts 0, 1 for the two pre-connect failures; reset to 0 after the
        # successful connection on the third try.
        assert backoff_attempts == [0, 1, 0]
        assert len(sleeps) == 3


class TestSlackSocketClient:
    """Unit tests for SlackSocketClient."""

    def test_stop_sets_running_false(self):
        """stop() signals the run loop to exit."""
        client = _make_client()
        client._running = True
        client.stop()
        assert client._running is False

    @pytest.mark.asyncio
    async def test_get_wss_url_returns_url_on_success(self, monkeypatch):
        """_get_wss_url returns the WSS URL from apps.connections.open."""
        client = _make_client()
        expected_url = "wss://wss-primary.slack.com/link?ticket=abc"

        mock_resp = MagicMock()
        mock_resp.json.return_value = {"ok": True, "url": expected_url}

        class MockAsyncClient:
            async def __aenter__(self):
                return self

            async def __aexit__(self, *args):
                pass

            async def post(self, *args, **kwargs):
                return mock_resp

        monkeypatch.setattr("httpx.AsyncClient", lambda **kw: MockAsyncClient())
        url = await client._get_wss_url()
        assert url == expected_url

    @pytest.mark.asyncio
    async def test_get_wss_url_raises_on_api_error(self, monkeypatch):
        """_get_wss_url raises RuntimeError when apps.connections.open fails."""
        client = _make_client()
        mock_resp = MagicMock()
        mock_resp.json.return_value = {"ok": False, "error": "invalid_auth"}

        class MockAsyncClient:
            async def __aenter__(self):
                return self

            async def __aexit__(self, *args):
                pass

            async def post(self, *args, **kwargs):
                return mock_resp

        monkeypatch.setattr("httpx.AsyncClient", lambda **kw: MockAsyncClient())
        with pytest.raises(RuntimeError, match="invalid_auth"):
            await client._get_wss_url()

    @pytest.mark.asyncio
    async def test_events_api_envelope_dispatches_handle_event(self, monkeypatch):
        """events_api envelopes call proxy.handle_event with the payload."""
        proxy = MagicMock()
        proxy.handle_event = AsyncMock()
        client = _make_client(proxy)

        payload = {"event": {"type": "message", "user": "U123", "text": "hi"}}
        envelope = json.dumps(
            {
                "type": "events_api",
                "envelope_id": "env-001",
                "payload": payload,
            }
        )

        sent_acks = []

        class FakeWS:
            def __init__(self):
                self._items = iter([envelope])

            def __aiter__(self):
                return self

            async def __anext__(self):
                try:
                    return next(self._items)
                except StopIteration:
                    raise StopAsyncIteration

            async def send(self, data):
                sent_acks.append(json.loads(data))

        class FakeCM:
            async def __aenter__(self):
                return FakeWS()

            async def __aexit__(self, *a):
                pass

        monkeypatch.setattr("websockets.connect", lambda url, **kw: FakeCM())
        client._running = True
        await client._connect_and_handle("wss://fake-url")
        # Flush pending asyncio tasks so create_task(handle_event) executes
        await asyncio.sleep(0)

        # Ack was sent
        assert any(a.get("envelope_id") == "env-001" for a in sent_acks)
        # handle_event was called with the payload
        proxy.handle_event.assert_awaited_once_with(payload)

    @pytest.mark.asyncio
    async def test_hello_message_not_dispatched(self, monkeypatch):
        """hello messages are silently consumed without calling handle_event."""
        proxy = MagicMock()
        proxy.handle_event = AsyncMock()
        client = _make_client(proxy)

        hello = json.dumps({"type": "hello", "num_connections": 1})

        class FakeWS:
            def __init__(self):
                self._items = iter([hello])

            def __aiter__(self):
                return self

            async def __anext__(self):
                try:
                    return next(self._items)
                except StopIteration:
                    raise StopAsyncIteration

            async def send(self, data):
                pass

        class FakeCM:
            async def __aenter__(self):
                return FakeWS()

            async def __aexit__(self, *a):
                pass

        monkeypatch.setattr("websockets.connect", lambda url, **kw: FakeCM())
        client._running = True
        await client._connect_and_handle("wss://fake-url")

        proxy.handle_event.assert_not_awaited()
