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

Security posture (adversarial review 2026-07-10):
- Telegram is an EXTERNAL service: outgoing text passes through the injected
  ``sanitize_fn`` (presidio in production) so scanner findings that embed
  matched secrets/PII are redacted before egress.
- The ``tool`` field is attacker-influenceable via the unauthenticated
  loopback /api/alerts endpoint: control characters are stripped and the
  value is length-capped so a crafted tool name cannot visually forge other
  gateway notifications under the trusted alert banner.
- Rate-cap exhaustion is NOT silent: one final "suppressed" notice is sent
  per window, and critical alerts retain budget that warnings cannot burn.
- Dedup keys include the alert source, so a spoofed pre-send from another
  source cannot suppress a genuine scanner's alert for 24 h.
- The Telegram send runs in a background task: a slow/unreachable Telegram
  (blocking urllib, 10 s socket timeout) must never stall EventBus.emit or
  the /api/alerts request path.
- A subscriber must NEVER break the bus: every failure is logged and
  swallowed (the bus also guards, belt-and-braces).
"""

from __future__ import annotations

import asyncio
import hashlib
import inspect
import logging
import re
import time
from typing import Any, Awaitable, Callable

logger = logging.getLogger("agentshroud.gateway.alert_telegram_relay")

_SEVERITY_MARKERS = {"critical": "🔴", "warning": "🟠"}
_DEDUP_WINDOW_SECONDS = 24 * 3600
_DEFAULT_MAX_PER_HOUR = 10
_TOOL_MAX_LEN = 64
_TEXT_MAX_LEN = 4000  # Telegram hard limit is 4096; leave margin
_CONTROL_CHARS = re.compile(r"[\x00-\x1f\x7f]")


class AlertTelegramRelay:
    """Subscribe to the gateway EventBus; relay security alerts to Telegram."""

    def __init__(
        self,
        send_fn: Callable[[str, str], Awaitable[None]],
        owner_chat_id: str,
        max_per_hour: int = _DEFAULT_MAX_PER_HOUR,
        sanitize_fn: Callable[[str], Any] | None = None,
    ) -> None:
        self._send = send_fn
        self._owner_chat_id = str(owner_chat_id)
        self._max_per_hour = max_per_hour
        self._sanitize = sanitize_fn
        self._sent_stamps: list[float] = []
        self._dedup: dict[str, float] = {}
        self._suppressed_since_notice = 0
        self._cap_notice_sent_at: float = 0.0
        # Strong refs so fire-and-forget send tasks aren't GC'd mid-flight.
        self._tasks: set[asyncio.Task] = set()

    async def __call__(self, event: Any) -> None:
        try:
            self._handle(event)
        except Exception as exc:  # never propagate into the bus
            logger.warning("Alert Telegram relay failed: %s", exc)

    def _handle(self, event: Any) -> None:
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
        # Priority budget: warnings may use only half the hourly cap, so a
        # warning flood can never starve critical alerts (review finding).
        budget = self._max_per_hour if severity == "critical" else self._max_per_hour // 2
        if len(self._sent_stamps) >= budget:
            self._suppressed_since_notice += 1
            logger.warning(
                "Alert Telegram relay rate limit (%d/h for %s) — suppressed: %s",
                budget,
                severity,
                summary[:120],
            )
            # The owner must KNOW suppression is happening — one notice per
            # hour window, sent outside the normal budget accounting.
            if now - self._cap_notice_sent_at > 3600:
                self._cap_notice_sent_at = now
                n = self._suppressed_since_notice
                self._suppressed_since_notice = 0
                self._spawn_send(
                    f"⚠️ AgentShroud alert relay: rate limit reached — "
                    f"{n} alert(s) suppressed this hour. Check the gateway "
                    f"alert log for the full stream."
                )
            return

        marker = _SEVERITY_MARKERS[severity]
        tool = self._clean_tool(details.get("tool", "gateway"))
        # Fixed trusted header; attacker-influenceable text demarcated below.
        # Sanitization happens inside the send task — presidio is async and
        # must not block the event-bus emit path.
        header = f"{marker} AgentShroud alert — {tool}"
        body = summary[:800]

        # Optimistically record BEFORE the async send so a burst of identical
        # events can't race N duplicate sends; rolled back on send failure so
        # a later genuine alert can retry.
        self._sent_stamps.append(now)
        self._dedup[key] = now
        if len(self._dedup) > 512:
            self._dedup = {k: v for k, v in self._dedup.items() if now - v < _DEDUP_WINDOW_SECONDS}
        self._spawn_send(header, body=body, rollback_key=key)

    # ------------------------------------------------------------------
    # Send plumbing — background task so Telegram latency (blocking urllib,
    # 10 s timeout) never stalls EventBus.emit or the /api/alerts request.
    # ------------------------------------------------------------------

    def _spawn_send(
        self, header: str, body: str | None = None, rollback_key: str | None = None
    ) -> None:
        async def _do_send() -> None:
            try:
                text = header
                if body is not None:
                    cleaned = body
                    if self._sanitize is not None:
                        result = self._sanitize(cleaned)
                        if inspect.isawaitable(result):
                            result = await result
                        cleaned = str(result)
                    text = f"{header}\n{cleaned}"
                await self._send(self._owner_chat_id, text[:_TEXT_MAX_LEN])
            except Exception as exc:
                logger.warning("Alert Telegram send failed: %s", exc)
                if rollback_key is not None:
                    self._dedup.pop(rollback_key, None)
                    if self._sent_stamps:
                        self._sent_stamps.pop()

        try:
            task = asyncio.get_running_loop().create_task(_do_send())
            self._tasks.add(task)
            task.add_done_callback(self._tasks.discard)
        except RuntimeError:
            # No running loop (sync test context) — degrade to best effort.
            logger.warning("Alert Telegram relay: no event loop; alert dropped")

    async def flush(self) -> None:
        """Await in-flight sends (test/shutdown helper)."""
        if self._tasks:
            await asyncio.gather(*list(self._tasks), return_exceptions=True)

    # ------------------------------------------------------------------

    @staticmethod
    def _clean_tool(tool: Any) -> str:
        cleaned = _CONTROL_CHARS.sub("", str(tool))
        return cleaned[:_TOOL_MAX_LEN] or "gateway"

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
        # Source included so a spoofed pre-send from another origin cannot
        # dedup-poison a genuine scanner alert (review finding).
        raw = (
            f"{details.get('source', '')}|{details.get('tool', '')}|"
            f"{details.get('message', '') or summary}"
        )
        return hashlib.sha256(raw.encode()).hexdigest()[:16]
