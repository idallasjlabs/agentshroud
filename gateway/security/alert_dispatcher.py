"""Alert dispatcher for security findings.

Routes alerts by severity: CRITICAL/HIGH → immediate notification,
MEDIUM/LOW → daily digest. Includes deduplication and rate limiting.
"""

import json
import logging
import time
from collections import deque
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

DEFAULT_LOG_DIR = Path("/var/log/security/alerts")
DEFAULT_ALERT_LOG = DEFAULT_LOG_DIR / "alerts.jsonl"

# Rate limiting
MAX_ALERTS_PER_HOUR = 10
RATE_WINDOW_SECONDS = 3600

# Dedup window (seconds) — don't re-alert same ID within this window
DEDUP_WINDOW_SECONDS = 86400  # 24 hours


class AlertDispatcher:
    """Dispatches security alerts with dedup and rate limiting."""

    def __init__(
        self,
        alert_log: Path = DEFAULT_ALERT_LOG,
        gateway_url: str = "http://localhost:8080",
        max_per_hour: int = MAX_ALERTS_PER_HOUR,
        dedup_window: int = DEDUP_WINDOW_SECONDS,
    ):
        self.alert_log = alert_log
        self.gateway_url = gateway_url
        self.max_per_hour = max_per_hour
        self.dedup_window = dedup_window

        # In-memory state
        self._sent_times: deque[float] = deque()  # timestamps of sent alerts
        self._seen_ids: dict[str, float] = {}  # alert_id → last_seen_timestamp
        self._digest_buffer: list[dict[str, Any]] = []

        # Ensure log dir exists
        self.alert_log.parent.mkdir(parents=True, exist_ok=True)

    def dispatch(self, alert: dict[str, Any]) -> dict[str, str]:
        """Dispatch an alert based on severity.

        Args:
            alert: Alert dict with at least 'severity' and 'id' fields.

        Returns:
            Dict with 'action' taken: 'notified', 'buffered', 'deduped', 'rate_limited'.
        """
        alert_id = alert.get("id", "")
        severity = alert.get("severity", "MEDIUM").upper()
        now = time.time()

        # Always log to JSONL
        self._log_alert(alert)

        # Dedup check
        if alert_id and self._is_duplicate(alert_id, now):
            logger.debug("Deduped alert: %s", alert_id)
            return {"action": "deduped", "alert_id": alert_id}

        # Mark as seen
        if alert_id:
            self._seen_ids[alert_id] = now

        # Route by severity
        if severity in ("CRITICAL", "HIGH"):
            # Rate limit check
            if self._is_rate_limited(now):
                logger.warning("Rate limited — alert buffered: %s", alert_id)
                self._digest_buffer.append(alert)
                return {"action": "rate_limited", "alert_id": alert_id}

            # Send immediate notification
            self._sent_times.append(now)
            success = self._send_notification(alert)
            return {
                "action": "notified" if success else "notify_failed",
                "alert_id": alert_id,
            }
        else:
            # Buffer for daily digest
            self._digest_buffer.append(alert)
            return {"action": "buffered", "alert_id": alert_id}

    def _is_duplicate(self, alert_id: str, now: float) -> bool:
        """Check if alert was already seen within dedup window."""
        last_seen = self._seen_ids.get(alert_id)
        if last_seen is None:
            return False
        return (now - last_seen) < self.dedup_window

    def _is_rate_limited(self, now: float) -> bool:
        """Check if we've exceeded the rate limit."""
        # Clean old entries
        cutoff = now - RATE_WINDOW_SECONDS
        while self._sent_times and self._sent_times[0] < cutoff:
            self._sent_times.popleft()
        return len(self._sent_times) >= self.max_per_hour

    def _log_alert(self, alert: dict[str, Any]) -> None:
        """Append alert to JSONL log file."""
        try:
            entry = {
                "logged_at": datetime.now(timezone.utc).isoformat(),
                **alert,
            }
            with open(self.alert_log, "a") as f:
                f.write(json.dumps(entry) + "\n")
        except OSError as e:
            logger.error("Failed to log alert: %s", e)

    def _send_notification(self, alert: dict[str, Any]) -> bool:
        """Send immediate notification via gateway API.

        Args:
            alert: Alert dict.

        Returns:
            True if notification sent successfully.
        """
        try:
            import urllib.request
            import urllib.error

            payload = json.dumps(
                {
                    "type": "security_alert",
                    "severity": alert.get("severity", "UNKNOWN"),
                    "tool": alert.get("tool", "unknown"),
                    "message": self._format_alert_message(alert),
                    "alert_id": alert.get("id", ""),
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                }
            ).encode()

            req = urllib.request.Request(
                f"{self.gateway_url}/api/alerts",
                data=payload,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            urllib.request.urlopen(req, timeout=10)
            logger.info("Alert notification sent: %s", alert.get("id", ""))
            return True
        except Exception as e:
            logger.error("Failed to send alert notification: %s", e)
            return False

    def _format_alert_message(self, alert: dict[str, Any]) -> str:
        """Format alert as human-readable message."""
        severity = alert.get("severity", "UNKNOWN")
        tool = alert.get("tool", "unknown")
        title = alert.get("title", alert.get("rule", alert.get("id", "Unknown")))
        details = alert.get("details", "")

        icon = {"CRITICAL": "🔴", "HIGH": "🟠"}.get(severity, "⚠️")
        msg = f"{icon} [{severity}] {tool.upper()}: {title}"
        if details:
            msg += f"\n{details}"
        return msg

    def get_digest(self, clear: bool = True) -> list[dict[str, Any]]:
        """Get buffered alerts for daily digest.

        Args:
            clear: Clear buffer after retrieval.

        Returns:
            List of buffered alerts.
        """
        digest = list(self._digest_buffer)
        if clear:
            self._digest_buffer.clear()
        return digest

    def get_stats(self) -> dict[str, Any]:
        """Get dispatcher statistics."""
        now = time.time()
        cutoff = now - RATE_WINDOW_SECONDS
        while self._sent_times and self._sent_times[0] < cutoff:
            self._sent_times.popleft()

        return {
            "alerts_sent_this_hour": len(self._sent_times),
            "rate_limit": self.max_per_hour,
            "digest_buffer_size": len(self._digest_buffer),
            "known_alert_ids": len(self._seen_ids),
        }

    def cleanup_seen(self) -> int:
        """Remove expired entries from seen IDs cache.

        Returns:
            Number of entries removed.
        """
        now = time.time()
        expired = [
            k for k, v in self._seen_ids.items() if (now - v) > self.dedup_window
        ]
        for k in expired:
            del self._seen_ids[k]
        return len(expired)
