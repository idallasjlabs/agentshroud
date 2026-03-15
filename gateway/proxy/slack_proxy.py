# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Slack API Proxy — intercepts all bot <-> Slack traffic.

Inbound: Slack Events API pushes message events to /slack-events.
         Gateway verifies signing secret, applies RBAC + SecurityPipeline,
         then forwards sanitized payload to the bot's /webhook endpoint.
Outbound: Bot Slack API calls (chat.postMessage etc.) are proxied through
          /slack-api/<method>. Gateway scans content and injects the bot token.

Bot sets SLACK_API_BASE_URL=http://gateway:8080/slack-api.
"""
from __future__ import annotations

import asyncio
import hashlib
import hmac
import json
import logging
import os
import time
from typing import Any, Optional

from gateway.security.rbac_config import RBACConfig

logger = logging.getLogger("agentshroud.proxy.slack")

SLACK_API_BASE = "https://slack.com/api"

# Slack signing secret version string (Slack spec)
_SLACK_SIG_VERSION = "v0"
# Maximum age of a Slack request before it is rejected (replay attack prevention)
_SLACK_MAX_TIMESTAMP_AGE_SECONDS = 300
# Event deduplication TTL — matches Slack's retry window
_EVENT_DEDUP_TTL_SECONDS = 600

# Message methods whose text content must be scanned before forwarding to Slack
_CONTENT_METHODS = frozenset({"chat.postMessage", "chat.update", "chat.meMessage"})

# Owner-only slash commands
_COLLABORATOR_BLOCKED_COMMANDS = frozenset({
    "/approve", "/deny", "/revoke", "/addcollab", "/restorecollabs",
    "/pending", "/collabs",
})

# Disclosure notice sent to collaborators on their first message
_DISCLOSURE_MESSAGE = (
    ":shield: *AgentShroud Notice*\n\n"
    "This conversation is logged and may be reviewed as part of the AgentShroud\u2122 "
    "project. By continuing, you acknowledge this. Questions? Reach out to Isaiah directly."
)


def _read_secret_static(name: str, default: str = "") -> str:
    """Read a Docker secret from /run/secrets/<name>."""
    try:
        with open(f"/run/secrets/{name}", "r") as fh:
            return fh.read().strip()
    except (FileNotFoundError, OSError):
        return default


class SlackAPIProxy:
    """Proxies Slack Events API inbound and Slack Web API outbound through SecurityPipeline.

    Inbound flow (Events API push):
        Slack -> POST /slack-events -> verify_signature -> RBAC -> pipeline -> bot /webhook

    Outbound flow (bot-initiated Slack API call):
        Bot -> POST /slack-api/<method> -> pipeline.process_outbound -> slack.com/api/<method>
    """

    def __init__(
        self,
        pipeline=None,
        middleware_manager=None,
        sanitizer=None,
        bot_webhook_url: Optional[str] = None,
    ):
        self.pipeline = pipeline
        self.middleware_manager = middleware_manager
        self.sanitizer = sanitizer

        # Bot token: gateway holds it; bot never sees the raw token
        self._bot_token = (
            os.environ.get("SLACK_BOT_TOKEN", "")
            or _read_secret_static("slack_bot_token")
        )
        # Signing secret: used to verify Slack webhook requests
        self._signing_secret = (
            os.environ.get("SLACK_SIGNING_SECRET", "")
            or _read_secret_static("slack_signing_secret")
        )

        # Where to forward sanitized inbound messages
        self._bot_webhook_url = (
            bot_webhook_url
            or os.environ.get("AGENTSHROUD_BOT_WEBHOOK_URL", "http://agentshroud:18789/webhook")
        )

        # RBAC: same RBACConfig used by Telegram proxy
        try:
            self._rbac = RBACConfig()
        except Exception:
            self._rbac = None

        # Per-user rate limiters (same defaults as Telegram proxy)
        from gateway.ingest_api.auth import RateLimiter
        self._collaborator_rate_limiter = RateLimiter(
            max_requests=int(os.environ.get("AGENTSHROUD_COLLAB_RATE_LIMIT_MAX_REQUESTS", "5000")),
            window_seconds=int(os.environ.get("AGENTSHROUD_COLLAB_RATE_LIMIT_WINDOW_SECONDS", "3600")),
        )
        self._stranger_rate_limiter = RateLimiter(
            max_requests=int(os.environ.get("AGENTSHROUD_STRANGER_RATE_LIMIT_MAX_REQUESTS", "5")),
            window_seconds=int(os.environ.get("AGENTSHROUD_STRANGER_RATE_LIMIT_WINDOW_SECONDS", "3600")),
        )

        # Event dedup cache: event_id -> received_at_epoch
        self._event_dedup: dict[str, float] = {}

        # Track which users have already received the disclosure notice
        self._disclosure_sent: set[str] = set()

        # Track collaborators waiting for owner approval: user_id -> request timestamp
        self._pending_access_requests: dict[str, float] = {}

        # Runtime-revoked collaborator IDs
        self._runtime_revoked: set[str] = set()

        # Dynamic collaborators added at runtime (survive only until restart)
        self._runtime_collaborators: set[str] = set()

        self._stats = {
            "events_received": 0,
            "events_blocked": 0,
            "events_forwarded": 0,
            "outbound_blocked": 0,
            "outbound_forwarded": 0,
        }

    # ─────────────────────────────────────────────────────────────────────────
    # Signature Verification
    # ─────────────────────────────────────────────────────────────────────────

    def verify_signature(self, timestamp: str, raw_body: bytes, signature: str) -> bool:
        """Verify the X-Slack-Signature header.

        Uses Slack's signing secret + HMAC-SHA256. Rejects requests older than
        5 minutes to prevent replay attacks.

        Returns True if valid (or if no signing secret configured — test mode).
        """
        if not self._signing_secret:
            logger.warning("Slack proxy: no signing secret configured — skipping verification (test mode)")
            return True

        # Replay protection
        try:
            age = abs(time.time() - float(timestamp))
            if age > _SLACK_MAX_TIMESTAMP_AGE_SECONDS:
                logger.warning(f"Slack proxy: request timestamp too old ({age:.0f}s) — rejecting")
                return False
        except (ValueError, TypeError):
            logger.warning("Slack proxy: invalid timestamp in request — rejecting")
            return False

        # HMAC-SHA256: sig_basestring = "v0:{timestamp}:{body}"
        sig_basestring = f"{_SLACK_SIG_VERSION}:{timestamp}:".encode() + raw_body
        expected = f"{_SLACK_SIG_VERSION}=" + hmac.new(
            self._signing_secret.encode("utf-8"),
            sig_basestring,
            hashlib.sha256,
        ).hexdigest()

        return hmac.compare_digest(expected, signature)

    # ─────────────────────────────────────────────────────────────────────────
    # Inbound: Slack Events API
    # ─────────────────────────────────────────────────────────────────────────

    async def handle_event(self, payload: dict) -> dict:
        """Process an inbound Slack Events API event.

        Called asynchronously from the /slack-events route AFTER the 200 has been
        returned to Slack (to satisfy the 3-second deadline).

        url_verification is handled synchronously by the route handler before
        this method is called.
        """
        self._stats["events_received"] += 1

        event_id = payload.get("event_id", "")
        event = payload.get("event", {})
        if not isinstance(event, dict):
            return {"status": "skipped", "reason": "no event object"}

        # Skip non-message events
        event_type = event.get("type", "")
        if event_type != "message":
            return {"status": "skipped", "reason": f"event type {event_type!r} not handled"}

        # Skip message subtypes (edits, deletes, joins, bot messages, etc.)
        if event.get("subtype") is not None:
            return {"status": "skipped", "reason": "message subtype ignored"}

        # Skip bot messages to prevent response loops
        if event.get("bot_id"):
            return {"status": "skipped", "reason": "bot message ignored"}

        # Event deduplication
        self._purge_stale_dedup()
        if event_id and event_id in self._event_dedup:
            logger.debug(f"Slack proxy: duplicate event {event_id} — skipping")
            return {"status": "skipped", "reason": "duplicate event_id"}
        if event_id:
            self._event_dedup[event_id] = time.time()

        user_id = str(event.get("user", ""))
        channel = str(event.get("channel", ""))
        text = str(event.get("text", "")).strip()
        # thread_ts: reply in the same thread as the triggering message
        thread_ts = event.get("thread_ts") or event.get("ts") or ""

        if not user_id:
            return {"status": "skipped", "reason": "no user_id in event"}
        if not text:
            return {"status": "skipped", "reason": "empty message text"}

        # RBAC resolution
        is_owner = self._rbac.is_owner(user_id) if self._rbac else False
        is_revoked = user_id in self._runtime_revoked
        is_collaborator = (
            not is_owner
            and not is_revoked
            and self._rbac is not None
            and (
                user_id in {str(uid) for uid in (self._rbac.collaborator_user_ids or [])}
                or user_id in self._runtime_collaborators
            )
        )

        logger.info(
            f"Slack inbound: user={user_id} channel={channel} "
            f"owner={is_owner} collab={is_collaborator} text_len={len(text)}"
        )

        # ── Stranger path ───────────────────────────────────────────────────
        if not is_owner and not is_collaborator:
            if not self._stranger_rate_limiter.check(user_id):
                await self._send_slack_message(
                    channel,
                    "Access request rate limit reached. Please try again later.",
                    thread_ts=thread_ts,
                )
                self._stats["events_blocked"] += 1
                return {"status": "blocked", "reason": "stranger rate limit"}

            # Queue access request for owner
            if user_id not in self._pending_access_requests:
                self._pending_access_requests[user_id] = time.time()
                owner_msg = (
                    f":bust_in_silhouette: *Access Request*\n"
                    f"Slack user `{user_id}` is requesting access.\n"
                    f"• `/approve {user_id}` — grant collaborator access\n"
                    f"• `/deny {user_id}` — reject"
                )
                await self._notify_owner(owner_msg)

            await self._send_slack_message(
                channel,
                "Your access request has been queued. The owner will review it shortly.",
                thread_ts=thread_ts,
            )
            self._stats["events_blocked"] += 1
            return {"status": "blocked", "reason": "stranger pending approval"}

        # ── Collaborator path ────────────────────────────────────────────────
        if is_collaborator:
            if not self._collaborator_rate_limiter.check(user_id):
                reset_at = self._collaborator_rate_limiter.reset_time(user_id)
                reset_str = (
                    time.strftime("%H:%M UTC", time.gmtime(reset_at)) if reset_at else "soon"
                )
                await self._send_slack_message(
                    channel,
                    f"Rate limit reached. Your access resets at {reset_str}.",
                    thread_ts=thread_ts,
                )
                self._stats["events_blocked"] += 1
                return {"status": "blocked", "reason": "collaborator rate limit"}

            # Disclosure notice on first contact
            if user_id not in self._disclosure_sent:
                self._disclosure_sent.add(user_id)
                await self._send_slack_message(channel, _DISCLOSURE_MESSAGE, thread_ts=thread_ts)

            # Block owner-only commands
            cmd = text.split()[0].lower() if text else ""
            if cmd in _COLLABORATOR_BLOCKED_COMMANDS:
                await self._send_slack_message(
                    channel,
                    "That command is restricted to the owner.",
                    thread_ts=thread_ts,
                )
                self._stats["events_blocked"] += 1
                return {"status": "blocked", "reason": "collaborator blocked command"}

        # ── Local command handling (owner + collaborator) ───────────────────
        if text.startswith("/"):
            handled = await self._handle_local_command(text, user_id, channel, thread_ts, is_owner)
            if handled:
                return {"status": "handled_locally"}

        # ── SecurityPipeline inbound scan ───────────────────────────────────
        if self.pipeline:
            try:
                result = await self.pipeline.process_inbound(
                    message=text,
                    agent_id="default",
                    source="slack",
                    metadata={"user_id": user_id, "channel": channel},
                )
                if result.blocked:
                    self._stats["events_blocked"] += 1
                    await self._send_slack_message(
                        channel,
                        "Your message could not be processed.",
                        thread_ts=thread_ts,
                    )
                    return {"status": "blocked", "reason": result.block_reason}
                sanitized_text = result.sanitized_message or text
            except Exception as exc:
                logger.error(f"Slack proxy: pipeline inbound error: {exc}")
                sanitized_text = text
        else:
            sanitized_text = text

        # ── Forward sanitized message to bot ───────────────────────────────
        bot_payload = {
            "source": "slack",
            "channel": channel,
            "thread_ts": thread_ts,
            "user_id": user_id,
            "text": sanitized_text,
        }
        await self._forward_to_bot(bot_payload)
        self._stats["events_forwarded"] += 1
        return {"status": "forwarded"}

    # ─────────────────────────────────────────────────────────────────────────
    # Outbound: Bot → Slack API proxy
    # ─────────────────────────────────────────────────────────────────────────

    async def proxy_outbound(self, method: str, body: bytes, content_type: str, is_system: bool = False) -> dict:
        """Proxy a bot Slack Web API call through the security pipeline.

        For message-sending methods (chat.postMessage, chat.update, chat.meMessage):
          - Extracts text from request body
          - Runs SecurityPipeline.process_outbound()
          - On BLOCK: returns synthetic Slack error to bot
          - On PASS: injects Authorization header and forwards to slack.com
        For all other methods: forwards directly (no content scanning needed).
        """
        if not self._bot_token:
            logger.error("Slack proxy: no bot token — cannot proxy outbound request")
            return {"ok": False, "error": "not_configured"}

        # Parse body
        payload: dict = {}
        if body:
            try:
                if "application/json" in (content_type or ""):
                    payload = json.loads(body.decode("utf-8", errors="replace"))
                elif "application/x-www-form-urlencoded" in (content_type or ""):
                    from urllib.parse import parse_qs
                    qs = parse_qs(body.decode("utf-8", errors="replace"))
                    payload = {k: v[0] for k, v in qs.items()}
            except Exception as exc:
                logger.warning(f"Slack proxy outbound: could not parse body for {method}: {exc}")

        # Content scan for message-sending methods (skipped for system notifications)
        if method in _CONTENT_METHODS and self.pipeline and not is_system:
            text = payload.get("text", "") or payload.get("blocks", "")
            if isinstance(text, (list, dict)):
                # Block Kit payload — convert to string for scanning
                text = json.dumps(text)
            if text:
                try:
                    result = await self.pipeline.process_outbound(
                        response=str(text),
                        agent_id="default",
                        metadata={"source": "slack_outbound", "method": method},
                    )
                    if result.blocked:
                        self._stats["outbound_blocked"] += 1
                        logger.warning(
                            f"Slack proxy: outbound {method} BLOCKED: {result.block_reason}"
                        )
                        return {"ok": False, "error": "content_policy_violation"}
                    # Replace text with sanitized version
                    if result.sanitized_message and "text" in payload:
                        payload["text"] = result.sanitized_message
                except Exception as exc:
                    logger.error(f"Slack proxy: pipeline outbound error: {exc}")

        # Forward to Slack API
        response = await self._call_slack_api(method, payload)
        self._stats["outbound_forwarded"] += 1
        return response

    # ─────────────────────────────────────────────────────────────────────────
    # Local command handling
    # ─────────────────────────────────────────────────────────────────────────

    async def _handle_local_command(
        self,
        text: str,
        user_id: str,
        channel: str,
        thread_ts: str,
        is_owner: bool,
    ) -> bool:
        """Handle gateway-level slash commands. Returns True if command was handled."""
        parts = text.strip().split()
        cmd = parts[0].lower()
        args = parts[1:]

        if cmd == "/status":
            rbac_status = "RBAC: enabled" if self._rbac else "RBAC: disabled"
            pipeline_status = "Pipeline: active" if self.pipeline else "Pipeline: inactive"
            await self._send_slack_message(
                channel,
                f":shield: *AgentShroud Status*\n• {rbac_status}\n• {pipeline_status}",
                thread_ts=thread_ts,
            )
            return True

        if cmd == "/whoami":
            if self._rbac:
                role = self._rbac.get_user_role(user_id)
                await self._send_slack_message(
                    channel,
                    f":bust_in_silhouette: User `{user_id}` — role: *{role.value}*",
                    thread_ts=thread_ts,
                )
            else:
                await self._send_slack_message(channel, "RBAC not configured.", thread_ts=thread_ts)
            return True

        # Owner-only commands below
        if not is_owner:
            return False

        if cmd == "/approve" and args:
            target = args[0]
            self._pending_access_requests.pop(target, None)
            self._runtime_revoked.discard(target)
            self._runtime_collaborators.add(target)
            if self._rbac and target not in self._rbac.collaborator_user_ids:
                self._rbac.collaborator_user_ids.append(target)
                from gateway.security.rbac_config import Role
                self._rbac.user_roles[target] = Role.COLLABORATOR
            await self._send_slack_message(
                channel, f":white_check_mark: `{target}` approved as collaborator.", thread_ts=thread_ts
            )
            return True

        if cmd == "/deny" and args:
            target = args[0]
            self._pending_access_requests.pop(target, None)
            self._runtime_revoked.add(target)
            await self._send_slack_message(
                channel, f":x: `{target}` denied.", thread_ts=thread_ts
            )
            return True

        if cmd == "/revoke" and args:
            target = args[0]
            self._runtime_revoked.add(target)
            self._runtime_collaborators.discard(target)
            if self._rbac and target in self._rbac.collaborator_user_ids:
                self._rbac.collaborator_user_ids.remove(target)
                self._rbac.user_roles.pop(target, None)
            await self._send_slack_message(
                channel, f":no_entry: `{target}` revoked.", thread_ts=thread_ts
            )
            return True

        if cmd == "/addcollab" and args:
            target = args[0]
            self._runtime_revoked.discard(target)
            self._runtime_collaborators.add(target)
            if self._rbac and target not in self._rbac.collaborator_user_ids:
                self._rbac.collaborator_user_ids.append(target)
                from gateway.security.rbac_config import Role
                self._rbac.user_roles[target] = Role.COLLABORATOR
            await self._send_slack_message(
                channel, f":white_check_mark: `{target}` added as collaborator.", thread_ts=thread_ts
            )
            return True

        if cmd == "/pending":
            if self._pending_access_requests:
                lines = "\n".join(
                    f"• `{uid}` (since {time.strftime('%H:%M UTC', time.gmtime(ts))})"
                    for uid, ts in self._pending_access_requests.items()
                )
                await self._send_slack_message(
                    channel, f":hourglass: *Pending access requests:*\n{lines}", thread_ts=thread_ts
                )
            else:
                await self._send_slack_message(
                    channel, "No pending access requests.", thread_ts=thread_ts
                )
            return True

        if cmd == "/collabs":
            ids = list(self._rbac.collaborator_user_ids) if self._rbac else []
            if ids:
                lines = "\n".join(f"• `{uid}`" for uid in ids)
                await self._send_slack_message(
                    channel, f":busts_in_silhouette: *Collaborators:*\n{lines}", thread_ts=thread_ts
                )
            else:
                await self._send_slack_message(channel, "No collaborators configured.", thread_ts=thread_ts)
            return True

        return False

    # ─────────────────────────────────────────────────────────────────────────
    # HTTP helpers
    # ─────────────────────────────────────────────────────────────────────────

    async def _send_slack_message(
        self, channel: str, text: str, thread_ts: Optional[str] = None
    ) -> None:
        """Send a gateway-originated Slack message (not subject to pipeline filtering)."""
        if not self._bot_token or not channel:
            return
        body: dict[str, Any] = {"channel": channel, "text": text}
        if thread_ts:
            body["thread_ts"] = thread_ts
        try:
            await self._call_slack_api("chat.postMessage", body)
        except Exception as exc:
            logger.warning(f"Slack proxy: _send_slack_message failed: {exc}")

    async def _notify_owner(self, text: str) -> None:
        """Send a notification to the owner's Slack DM or configured channel."""
        # Owner DM: use the owner's Slack user ID as the channel (Slack supports this)
        owner_slack_id = os.environ.get("AGENTSHROUD_SLACK_OWNER_USER_ID", "")
        if owner_slack_id:
            await self._send_slack_message(owner_slack_id, text)

    async def _forward_to_bot(self, payload: dict) -> None:
        """POST a sanitized inbound payload to the bot's /webhook endpoint."""
        try:
            import httpx
            async with httpx.AsyncClient(timeout=30.0) as client:
                await client.post(
                    self._bot_webhook_url,
                    json=payload,
                    headers={"Content-Type": "application/json"},
                )
        except Exception as exc:
            logger.error(f"Slack proxy: failed to forward to bot: {exc}")

    async def _call_slack_api(self, method: str, body: dict) -> dict:
        """POST to https://slack.com/api/<method> with the bot token."""
        url = f"{SLACK_API_BASE}/{method}"
        try:
            import httpx
            async with httpx.AsyncClient(timeout=15.0) as client:
                resp = await client.post(
                    url,
                    json=body,
                    headers={
                        "Content-Type": "application/json; charset=utf-8",
                        "Authorization": f"Bearer {self._bot_token}",
                    },
                )
                return resp.json()
        except Exception as exc:
            logger.error(f"Slack proxy: _call_slack_api {method} failed: {exc}")
            return {"ok": False, "error": str(exc)}

    # ─────────────────────────────────────────────────────────────────────────
    # Housekeeping
    # ─────────────────────────────────────────────────────────────────────────

    def _purge_stale_dedup(self) -> None:
        """Remove expired entries from the event dedup cache."""
        cutoff = time.time() - _EVENT_DEDUP_TTL_SECONDS
        stale = [k for k, v in self._event_dedup.items() if v < cutoff]
        for k in stale:
            del self._event_dedup[k]

    def get_stats(self) -> dict:
        return dict(self._stats)
