# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Alert → owner Telegram relay (SCRUM-61).

Event-bus subscriber that forwards ``security_alert`` events of critical or
warning severity to the owner's Telegram chat within seconds of emission.
This is the delivery half of cron/job failure alerting: any source that
reaches the event bus (AlertDispatcher → /api/alerts → emit, the cron state
monitor, ResourceGuard, security sidecars) gets owner-visible notification
without its own Telegram plumbing.

Design constraints:
- A subscriber must NEVER break the bus: every failure is logged and
  swallowed (the bus also guards, belt-and-braces).
- Dedup (24 h, by tool+message) and a per-hour send cap keep a flapping
  job from flooding the owner — mirrors AlertDispatcher's own limits.
- The Telegram send function is injected so tests need no network and the
  caller decides the transport (EgressTelegramNotifier in production).
"""

from __future__ import annotations

import hashlib
import logging
import time
from typing import Any, Awaitable, Callable

logger = logging.getLogger("agentshroud.gateway.alert_telegram_relay")

_SEVERITY_MARKERS = {"critical": "🔴", "warning": "🟠"}
_DEDUP_WINDOW_SECONDS = 24 * 3600
_DEFAULT_MAX_PER_HOUR = 10


class AlertTelegramRelay:
    """Subscribe to the gateway EventBus; relay security alerts to Telegram."""

    def __init__(
        self,
        send_fn: Callable[[str, str], Awaitable[None]],
        owner_chat_id: str,
        max_per_hour: int = _DEFAULT_MAX_PER_HOUR,
    ) -> None:
        self._send = send_fn
        self._owner_chat_id = str(owner_chat_id)
        self._max_per_hour = max_per_hour
        self._sent_stamps: list[float] = []
        self._dedup: dict[str, float] = {}

    async def __call__(self, event: Any) -> None:
        try:
            await self._handle(event)
        except Exception as exc:  # never propagate into the bus
            logger.warning("Alert Telegram relay failed: %s", exc)

    async def _handle(self, event: Any) -> None:
        etype, severity, summary, details = self._coerce(event)
        if etype != "security_alert":
            return
        if severity not in _SEVERITY_MARKERS:
            return

        key = self._dedup_key(details, summary)
        now = time.time()
        last = self._dedup.get(key)
        if last is not None and (now - last) < _DEDUP_WINDOW_SECONDS:
            return

        self._sent_stamps = [t for t in self._sent_stamps if now - t < 3600]
        if len(self._sent_stamps) >= self._max_per_hour:
            logger.warning(
                "Alert Telegram relay rate limit reached (%d/h) — dropped: %s",
                self._max_per_hour,
                summary[:120],
            )
            return

        marker = _SEVERITY_MARKERS[severity]
        tool = details.get("tool", "gateway")
        text = f"{marker} AgentShroud alert — {tool}\n{summary[:800]}"
        await self._send(self._owner_chat_id, text)
        self._sent_stamps.append(now)
        self._dedup[key] = now
        # Bound the dedup map — expired entries are useless.
        if len(self._dedup) > 512:
            self._dedup = {k: v for k, v in self._dedup.items() if now - v < _DEDUP_WINDOW_SECONDS}

    @staticmethod
    def _coerce(event: Any) -> tuple[str, str, str, dict]:
        """Accept GatewayEvent objects or plain dicts from legacy emitters."""
        if isinstance(event, dict):
            return (
                str(event.get("type") or event.get("event_type") or ""),
                str(event.get("severity", "")).lower(),
                str(event.get("summary", "")),
                event.get("details") or {},
            )
        return (
            str(getattr(event, "type", "")),
            str(getattr(event, "severity", "")).lower(),
            str(getattr(event, "summary", "")),
            getattr(event, "details", None) or {},
        )

    @staticmethod
    def _dedup_key(details: dict, summary: str) -> str:
        raw = f"{details.get('tool', '')}|{details.get('message', '') or summary}"
        return hashlib.sha256(raw.encode()).hexdigest()[:16]
