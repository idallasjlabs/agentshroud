"""Event Bus for AgentShroud Gateway

Simple in-process pub/sub event bus for broadcasting gateway events
to WebSocket clients and other subscribers.
"""

import asyncio
import logging
import time
from collections import defaultdict
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Any, Callable

logger = logging.getLogger("agentshroud.gateway.event_bus")


@dataclass
class GatewayEvent:
    """A single gateway event"""

    type: str
    timestamp: str
    summary: str
    details: dict[str, Any] = field(default_factory=dict)
    severity: str = "info"  # info, warning, critical

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


class EventBus:
    """Simple in-process event bus with async support"""

    def __init__(self):
        self._subscribers: list[Callable] = []
        self._lock = asyncio.Lock()
        self._recent_events: list[GatewayEvent] = []
        self._max_recent = 200
        self._event_counts: dict[str, int] = defaultdict(int)
        # Track auth failures for severity escalation
        self._auth_failures: list[float] = []

    async def subscribe(self, callback: Callable) -> None:
        """Subscribe to all events"""
        async with self._lock:
            self._subscribers.append(callback)

    async def unsubscribe(self, callback: Callable) -> None:
        """Unsubscribe from events"""
        async with self._lock:
            try:
                self._subscribers.remove(callback)
            except ValueError:
                pass

    async def emit(self, event: GatewayEvent) -> None:
        """Emit an event to all subscribers"""
        async with self._lock:
            # Track event
            self._recent_events.append(event)
            if len(self._recent_events) > self._max_recent:
                self._recent_events = self._recent_events[-self._max_recent :]
            self._event_counts[event.type] += 1

            # Track auth failures for severity escalation
            if event.type == "auth_failed":
                now = time.time()
                self._auth_failures.append(now)
                # Keep only last 5 minutes
                cutoff = now - 300
                self._auth_failures = [t for t in self._auth_failures if t > cutoff]
                if len(self._auth_failures) >= 3:
                    event.severity = "critical"

            # Copy subscribers under lock
            callbacks = list(self._subscribers)

        # Notify subscribers outside lock to avoid deadlocks
        for callback in callbacks:
            try:
                result = callback(event)
                if asyncio.iscoroutine(result):
                    await result
            except Exception as e:
                logger.warning(f"Event subscriber error: {e}")

    async def get_stats(self) -> dict[str, Any]:
        """Get event statistics"""
        async with self._lock:
            return {
                "total_events": sum(self._event_counts.values()),
                "events_by_type": dict(self._event_counts),
                "recent_count": len(self._recent_events),
            }

    async def get_recent(self, limit: int = 50) -> list[dict[str, Any]]:
        """Get recent events"""
        async with self._lock:
            return [e.to_dict() for e in self._recent_events[-limit:]]


def make_event(
    event_type: str,
    summary: str,
    details: dict[str, Any] | None = None,
    severity: str = "info",
) -> GatewayEvent:
    """Helper to create a GatewayEvent with current timestamp"""
    return GatewayEvent(
        type=event_type,
        timestamp=datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        summary=summary,
        details=details or {},
        severity=severity,
    )
