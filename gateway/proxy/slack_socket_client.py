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
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gateway.proxy.slack_proxy import SlackAPIProxy

logger = logging.getLogger("agentshroud.proxy.slack_socket")

CONNECTIONS_OPEN_URL = "https://slack.com/api/apps.connections.open"
# Seconds to wait before reconnect after error
_RECONNECT_BACKOFF = [2, 5, 10, 30, 60]


class SlackSocketClient:
    """Maintains a persistent Socket Mode WebSocket connection to Slack.

    Call run() as an asyncio background task. Call stop() to shut it down.
    """

    def __init__(self, proxy: "SlackAPIProxy", app_token: str):
        self._proxy = proxy
        self._app_token = app_token
        self._running = False
        self._ws = None

    async def run(self) -> None:
        """Main reconnect loop. Runs until stop() is called."""
        self._running = True
        backoff_idx = 0
        logger.info("Slack Socket Mode client starting")

        while self._running:
            try:
                wss_url = await self._get_wss_url()
                backoff_idx = 0  # reset backoff on successful URL fetch
                await self._connect_and_handle(wss_url)
            except asyncio.CancelledError:
                break
            except Exception as exc:
                wait = _RECONNECT_BACKOFF[min(backoff_idx, len(_RECONNECT_BACKOFF) - 1)]
                logger.error(
                    "Slack Socket Mode error: %s — reconnecting in %ds", exc, wait
                )
                backoff_idx += 1
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
            raise RuntimeError(
                f"apps.connections.open failed: {data.get('error', 'unknown')}"
            )
        return data["url"]

    async def _connect_and_handle(self, wss_url: str) -> None:
        """Open the WebSocket and process events until Slack requests disconnect."""
        import websockets

        logger.info("Slack Socket Mode: connecting to WSS endpoint")
        async with websockets.connect(wss_url, ping_interval=30, ping_timeout=10) as ws:
            self._ws = ws
            async for raw_message in ws:
                if not self._running:
                    break
                try:
                    envelope = json.loads(raw_message)
                except json.JSONDecodeError:
                    logger.warning("Slack Socket Mode: received non-JSON message")
                    continue

                msg_type = envelope.get("type")

                if msg_type == "hello":
                    conns = envelope.get("num_connections", "?")
                    logger.info(
                        "Slack Socket Mode: connected (%s active connection(s))", conns
                    )
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
