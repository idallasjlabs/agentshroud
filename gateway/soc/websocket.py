# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""SOC unified WebSocket stream — /ws/soc.

Replaces the 5 separate /ws/* endpoints with a single filtered stream.
Clients send a subscription filter on connect; the server fans out matching
events from the EventBus ring buffer.
"""
from __future__ import annotations

import asyncio
import json
import logging
import time
from typing import Optional, Set

from fastapi import WebSocket, WebSocketDisconnect

from .auth import redeem_ws_token, _get_config_token
from .models import WSEvent, WSEventType

logger = logging.getLogger("agentshroud.soc.websocket")

_KEEPALIVE_INTERVAL = 30  # seconds


class SOCWebSocketHandler:
    """Manages a single /ws/soc client connection."""

    def __init__(self, ws: WebSocket, user_id: str):
        self.ws = ws
        self.user_id = user_id
        self.subscriptions: Set[str] = set()  # empty = all events

    async def _send_event(self, event: WSEvent) -> None:
        try:
            await self.ws.send_text(event.model_dump_json())
        except Exception:
            pass

    async def _keepalive_loop(self) -> None:
        while True:
            await asyncio.sleep(_KEEPALIVE_INTERVAL)
            try:
                await self._send_event(WSEvent(type=WSEventType.KEEPALIVE, summary="ping"))
            except Exception:
                break

    async def _event_fan_out(self, event_bus) -> None:
        """Subscribe to EventBus and forward matching events to the client."""
        if event_bus is None:
            return
        async for raw in event_bus.subscribe():
            if raw is None:
                continue
            try:
                ev = _coerce_to_ws_event(raw)
                if not ev:
                    continue
                # Apply subscription filter
                if self.subscriptions and ev.type.value not in self.subscriptions:
                    continue
                await self._send_event(ev)
            except Exception as exc:
                logger.debug("ws_soc fan-out error: %s", exc)

    async def run(self, event_bus) -> None:
        """Main connection loop."""
        # Read optional subscription filter from initial client message
        try:
            msg_text = await asyncio.wait_for(self.ws.receive_text(), timeout=2.0)
            try:
                msg = json.loads(msg_text)
                if isinstance(msg.get("subscribe"), list):
                    self.subscriptions = set(str(s) for s in msg["subscribe"])
                    logger.debug("ws_soc %s subscribed to %s", self.user_id, self.subscriptions)
            except Exception:
                pass
        except asyncio.TimeoutError:
            pass  # No subscription filter — subscribe to all

        keepalive_task = asyncio.create_task(self._keepalive_loop())
        fan_out_task = asyncio.create_task(self._event_fan_out(event_bus))

        try:
            # Wait until client disconnects
            while True:
                try:
                    data = await asyncio.wait_for(self.ws.receive_text(), timeout=60.0)
                    # Clients may send command messages (e.g. change subscription)
                    try:
                        cmd = json.loads(data)
                        if isinstance(cmd.get("subscribe"), list):
                            self.subscriptions = set(str(s) for s in cmd["subscribe"])
                    except Exception:
                        pass
                except asyncio.TimeoutError:
                    continue
                except WebSocketDisconnect:
                    break
        finally:
            keepalive_task.cancel()
            fan_out_task.cancel()
            try:
                await keepalive_task
            except (asyncio.CancelledError, Exception):
                pass
            try:
                await fan_out_task
            except (asyncio.CancelledError, Exception):
                pass


def _coerce_to_ws_event(raw) -> Optional[WSEvent]:
    """Convert an EventBus item to WSEvent, return None if conversion fails."""
    if isinstance(raw, WSEvent):
        return raw
    if isinstance(raw, dict):
        try:
            etype_raw = raw.get("type", raw.get("event_type", "security_event"))
            # Map legacy event type names to WSEventType
            type_map = {
                "security_event": WSEventType.SECURITY_EVENT,
                "egress_event": WSEventType.EGRESS_EVENT,
                "egress_denied": WSEventType.EGRESS_EVENT,
                "egress_allowed": WSEventType.EGRESS_EVENT,
                "approval_event": WSEventType.APPROVAL_EVENT,
                "service_event": WSEventType.SERVICE_EVENT,
                "log_event": WSEventType.LOG_EVENT,
                "inbound_blocked": WSEventType.SECURITY_EVENT,
                "inbound_allowed": WSEventType.SECURITY_EVENT,
                "anomaly_detected": WSEventType.SECURITY_EVENT,
            }
            etype = type_map.get(str(etype_raw).lower(), WSEventType.SECURITY_EVENT)
            from .models import Severity
            sev_raw = raw.get("severity", "info")
            sev_map = {
                "critical": Severity.CRITICAL,
                "high": Severity.HIGH,
                "medium": Severity.MEDIUM,
                "low": Severity.LOW,
                "info": Severity.INFO,
            }
            sev = sev_map.get(str(sev_raw).lower(), Severity.INFO)
            return WSEvent(
                type=etype,
                severity=sev,
                summary=raw.get("summary", raw.get("message", "")),
                details={k: v for k, v in raw.items() if k not in {"type", "severity", "summary", "message", "timestamp"}},
                source_module=raw.get("source_module", raw.get("source", "")),
                timestamp=raw.get("timestamp", ""),
            )
        except Exception:
            return None
    return None


async def ws_soc_endpoint(websocket: WebSocket) -> None:
    """FastAPI WebSocket route handler for /ws/soc."""
    # Authenticate via ?token= query param or first message
    token = websocket.query_params.get("token", "")
    user_id: Optional[str] = None
    if token:
        user_id = redeem_ws_token(token)

    # Fallback: check bearer header
    if not user_id:
        auth_header = websocket.headers.get("authorization", "")
        if auth_header.startswith("Bearer "):
            candidate = auth_header[7:].strip()
            user_id = redeem_ws_token(candidate)

    if not user_id:
        # Compatibility fallback: accept raw gateway password directly as token
        import hmac
        gateway_token = _get_config_token()
        if gateway_token and token and hmac.compare_digest(token.encode(), gateway_token.encode()):
            from ..security.rbac_config import RBACConfig
            user_id = RBACConfig().owner_user_id

    if not user_id:
        await websocket.close(code=4003, reason="Unauthorized")
        return

    await websocket.accept()
    logger.info("ws_soc: client connected (user_id=%s)", user_id)

    try:
        from ..ingest_api.state import app_state
        event_bus = getattr(app_state, "event_bus", None)
    except Exception:
        event_bus = None

    handler = SOCWebSocketHandler(ws=websocket, user_id=user_id)
    try:
        await handler.run(event_bus)
    except WebSocketDisconnect:
        pass
    except Exception as exc:
        logger.warning("ws_soc error: %s", exc)
    finally:
        logger.info("ws_soc: client disconnected (user_id=%s)", user_id)
