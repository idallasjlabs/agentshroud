# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""
Slack Socket Mode client — receives Slack events via outbound WebSocket.

No inbound port needed. The gateway opens an outbound WSS connection to Slack;
Slack pushes events over that connection. Events are fed into the same
SlackAPIProxy.handle_event() pipeline as the HTTP Events API path.

Protocol:
  1. POST apps.connections.open (app token) → get WSS URL
  2. Connect to WSS URL
  3. Receive JSON envelopes: {"type": "events_api", "envelope_id": "...", "payload": {...}}
  4. Acknowledge each envelope immediately: {"envelope_id": "..."}
  5. Process payload in background via SlackAPIProxy.handle_event()
  6. On {"type": "disconnect"}: reconnect (Slack rotates connections every few hours)
"""

from __future__ import annotations

import asyncio
import json
import logging
import random
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from gateway.proxy.slack_proxy import SlackAPIProxy

logger = logging.getLogger("agentshroud.proxy.slack_socket")

CONNECTIONS_OPEN_URL = "https://slack.com/api/apps.connections.open"
# Capped exponential backoff parameters for the reconnect loop
_BACKOFF_BASE = 1.0  # seconds
_BACKOFF_CAP = 60.0  # seconds


def compute_backoff(
    attempt: int,
    base: float = _BACKOFF_BASE,
    cap: float = _BACKOFF_CAP,
    rand: Callable[[], float] = random.random,
) -> float:
    """Capped exponential backoff with jitter for reconnect attempts.

    Returns a wait between 50% and 100% of min(cap, base * 2**attempt) so
    repeated network blips don't produce a fixed-interval retry storm and
    reconnecting clients don't thunder-herd Slack at the same instant.
    """
    ceiling = min(cap, base * (2 ** min(attempt, 16)))
    return ceiling * (0.5 + 0.5 * rand())


class SlackSocketClient:
    """Maintains a persistent Socket Mode WebSocket connection to Slack.

    Call run() as an asyncio background task. Call stop() to shut it down.
    """

    def __init__(self, proxy: "SlackAPIProxy", app_token: str):
        self._proxy = proxy
        self._app_token = app_token
        self._running = False
        self._ws = None
        self._connect_ok = False  # True once a WSS connection was established

    async def run(self) -> None:
        """Main reconnect loop. Runs until stop() is called."""
        self._running = True
        attempt = 0
        logger.info("Slack Socket Mode client starting")

        while self._running:
            try:
                self._connect_ok = False
                wss_url = await self._get_wss_url()
                await self._connect_and_handle(wss_url)
                attempt = 0  # clean disconnect (Slack rotation) — reconnect at once
            except asyncio.CancelledError:
                break
            except Exception as exc:
                # Reset backoff only after a successful WSS connection — a
                # successful apps.connections.open alone must not reset it, or
                # repeated WSS failures retry at a fixed short interval.
                if self._connect_ok:
                    attempt = 0
                wait = compute_backoff(attempt)
                logger.error("Slack Socket Mode error: %s — reconnecting in %.1fs", exc, wait)
                attempt += 1
                await asyncio.sleep(wait)

        logger.info("Slack Socket Mode client stopped")

    def stop(self) -> None:
        """Signal the run loop to exit."""
        self._running = False

    async def _get_wss_url(self) -> str:
        """Call apps.connections.open to get a fresh WSS URL."""
        import httpx

        async with httpx.AsyncClient(timeout=15.0) as client:
            resp = await client.post(
                CONNECTIONS_OPEN_URL,
                headers={
                    "Authorization": f"Bearer {self._app_token}",
                    "Content-Type": "application/x-www-form-urlencoded",
                },
            )
            data = resp.json()
        if not data.get("ok"):
            raise RuntimeError(f"apps.connections.open failed: {data.get('error', 'unknown')}")
        return data["url"]

    async def _connect_and_handle(self, wss_url: str) -> None:
        """Open the WebSocket and process events until Slack requests disconnect."""
        import websockets

        logger.info("Slack Socket Mode: connecting to WSS endpoint")
        async with websockets.connect(wss_url, ping_interval=30, ping_timeout=10) as ws:
            self._ws = ws
            self._connect_ok = True  # connection established — run() may reset backoff
            async for raw_message in ws:
                if not self._running:
                    break
                try:
                    envelope = json.loads(raw_message)
                except json.JSONDecodeError:
                    logger.warning("Slack Socket Mode: received non-JSON message")
                    continue

                msg_type = envelope.get("type")
                logger.debug("Slack Socket Mode: received message type=%r", msg_type)

                if msg_type == "hello":
                    conns = envelope.get("num_connections", "?")
                    logger.info("Slack Socket Mode: connected (%s active connection(s))", conns)
                    continue

                if msg_type == "disconnect":
                    reason = envelope.get("reason", "unknown")
                    logger.info(
                        "Slack Socket Mode: disconnect requested (%s) — will reconnect",
                        reason,
                    )
                    break  # Exit to outer loop which will reconnect

                if msg_type == "events_api":
                    envelope_id = envelope.get("envelope_id", "")
                    # Acknowledge immediately — Slack requires this within 3 seconds
                    await ws.send(json.dumps({"envelope_id": envelope_id}))
                    # Process event in background (don't block the receive loop)
                    payload = envelope.get("payload", {})
                    asyncio.create_task(self._proxy.handle_event(payload))
                    continue

                # Ignore all other message types (slash_commands, interactive, etc.)
                logger.debug("Slack Socket Mode: unhandled message type %r", msg_type)

        self._ws = None
