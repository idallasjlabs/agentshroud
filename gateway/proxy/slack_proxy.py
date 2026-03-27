# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Slack API Proxy — secures outbound bot → Slack traffic.

Outbound: Bot Slack API calls (chat.postMessage etc.) are proxied through
          /slack-api/<method>. Gateway scans content and injects the bot token.

Bot sets SLACK_API_BASE_URL=http://gateway:8080/slack-api.

Inbound Slack events are handled natively by OpenClaw's Slack channel integration
(Socket Mode). The gateway's role is outbound-only: content filtering and token
injection for all Slack Web API calls the bot makes.
"""
from __future__ import annotations

import json
import logging
import os
import secrets as _secrets

from gateway.utils.secrets import read_secret as _read_secret_static
from .collaborator_responses import COLLAB_OUTSIDE_SCOPE  # noqa: F401 — re-exported for Slack use

logger = logging.getLogger("agentshroud.proxy.slack")

SLACK_API_BASE = "https://slack.com/api"

# Internal WebSocket relay host — bot connects here for Socket Mode relay.
# Must match the gateway service hostname inside the Docker network.
_GATEWAY_WS_HOST = os.environ.get("AGENTSHROUD_GATEWAY_WS_HOST", "gateway:8080")

# Message methods whose text content must be scanned before forwarding to Slack
_CONTENT_METHODS = frozenset({"chat.postMessage", "chat.update", "chat.meMessage"})


class SlackAPIProxy:
    """Proxies bot Slack Web API calls through SecurityPipeline.

    Outbound flow (bot-initiated Slack API call):
        Bot -> POST /slack-api/<method> -> pipeline.process_outbound -> slack.com/api/<method>

    Trust model:
        Owner channel (DM to owner's Slack User ID): pipeline with FULL trust.
        All other channels: pre-check + pipeline with UNTRUSTED trust + fail-closed.
    """

    def __init__(
        self,
        pipeline=None,
        middleware_manager=None,
        sanitizer=None,
        tracker=None,
        owner_slack_user_id: str = "",
    ):
        self.pipeline = pipeline
        self.middleware_manager = middleware_manager
        self.sanitizer = sanitizer
        self.tracker = tracker  # CollaboratorActivityTracker for outbound message logging

        # Bot token: gateway holds it; bot never sees the raw token
        self._bot_token = (
            os.environ.get("SLACK_BOT_TOKEN", "")
            or _read_secret_static("slack_bot_token")
        )

        # Owner's Slack User ID (e.g. "U01J37F6YT0") — messages to this channel
        # receive FULL trust; all other channels are treated as UNTRUSTED collaborators.
        self._owner_slack_user_id = (
            owner_slack_user_id
            or os.environ.get("AGENTSHROUD_SLACK_OWNER_USER_ID", "")
        )

        # Relay tokens issued by _intercept_connections_open.
        # Key: one-time token string; Value: real Slack WSS URL.
        # Consumed (popped) by the /slack-ws-relay WebSocket endpoint.
        self._relay_tokens: dict[str, str] = {}

        # Map str(channel) → (correlation_id, timestamp) for inbound→outbound pairing (TTL 5 min)
        self._last_inbound_corr: dict[str, tuple] = {}

        self._stats: dict[str, int] = {
            "outbound_forwarded": 0,
            "outbound_blocked": 0,
        }

    def _is_owner_channel(self, channel: str) -> bool:
        """Return True if channel is a DM with the configured owner.

        In Slack, DM channels for a specific user are addressed by the user's
        member ID (e.g. "U01J37F6YT0").  Owner messages use that ID directly.
        """
        if not self._owner_slack_user_id or not channel:
            return False
        return channel == self._owner_slack_user_id

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

        # Socket Mode relay: intercept apps.connections.open and rewrite the WSS URL
        # so the bot's WebSocket connects through our relay instead of directly to Slack.
        if method == "apps.connections.open":
            return await self._intercept_connections_open(payload)

        # Content scan for message-sending methods (skipped for system notifications)
        if method in _CONTENT_METHODS and self.pipeline and not is_system:
            channel = payload.get("channel", "")
            is_owner = self._is_owner_channel(channel)
            text = payload.get("text", "") or payload.get("blocks", "")
            if isinstance(text, (list, dict)):
                text = json.dumps(text)
            if text:
                # Pre-pipeline fast-path: reject obvious infrastructure leakage to
                # non-owner channels before running the full pipeline.
                if not is_owner:
                    from .telegram_proxy import TelegramAPIProxy as _TelegramAPIProxy
                    if _TelegramAPIProxy._contains_high_risk_collaborator_leakage(str(text)):
                        logger.warning(
                            "Slack outbound BLOCKED: high-risk leakage detected for non-owner channel %s",
                            channel,
                        )
                        self._stats["outbound_blocked"] += 1
                        return {"ok": False, "error": "content_policy_violation"}

                trust_level = "FULL" if is_owner else "UNTRUSTED"
                try:
                    result = await self.pipeline.process_outbound(
                        response=str(text),
                        agent_id="default",
                        metadata={"source": "slack_outbound", "method": method},
                        user_trust_level=trust_level,
                    )
                    if result.blocked:
                        self._stats["outbound_blocked"] += 1
                        logger.warning(
                            "Slack proxy: outbound %s BLOCKED: %s", method, result.block_reason
                        )
                        return {"ok": False, "error": "content_policy_violation"}
                    # For non-owner channels: block if the info filter redacted anything.
                    # Sending a sanitized (redacted) response to a collaborator confirms
                    # that the original response contained infrastructure data.
                    if not is_owner:
                        try:
                            rc = getattr(result, "info_filter_redaction_count", None)
                            if isinstance(rc, int) and rc > 0:
                                self._stats["outbound_blocked"] += 1
                                logger.warning(
                                    "Slack proxy: outbound %s BLOCKED: info redaction (count=%d) for non-owner",
                                    method, rc,
                                )
                                return {"ok": False, "error": "content_policy_violation"}
                        except Exception:
                            pass
                    if result.sanitized_message and "text" in payload:
                        payload["text"] = result.sanitized_message
                except Exception as exc:
                    if not is_owner:
                        # Fail-closed: block non-owner delivery on any pipeline error.
                        self._stats["outbound_blocked"] += 1
                        logger.error(
                            "Slack proxy: pipeline error for non-owner channel %s — blocking: %s",
                            channel, exc,
                        )
                        return {"ok": False, "error": "content_policy_violation"}
                    logger.error("Slack proxy: pipeline outbound error (owner channel): %s", exc)

        # Forward to Slack API
        response = await self._call_slack_api(method, payload)
        self._stats["outbound_forwarded"] += 1

        # Log bot responses to collaborator activity tracker for /collabs reports.
        # Only track chat.postMessage (actual message sends, not edits or reactions).
        # When the bot replies, recover the user's original message via conversations.replies
        # (inbound tracking — replaces the removed Socket Mode parallel listener).
        if method == "chat.postMessage" and not is_system and self.tracker:
            try:
                import time as _time_mod
                _channel = payload.get("channel", "")
                _text = payload.get("text", "")
                _thread_ts = payload.get("thread_ts", "")
                if isinstance(_text, (list, dict)):
                    import json as _json
                    _text = _json.dumps(_text)
                if _channel and _text:
                    # --- Recover inbound query from Slack API ---
                    # Without Socket Mode, we look up the user's original message by fetching
                    # conversations.replies (if thread reply) or conversations.history (DM).
                    _corr_pair = self._last_inbound_corr.get(str(_channel))
                    _inbound_corr_id = _corr_pair[0] if _corr_pair else None
                    if not _inbound_corr_id:
                        try:
                            if _thread_ts:
                                _hist = await self._call_slack_api(
                                    "conversations.replies",
                                    {"channel": _channel, "ts": _thread_ts, "limit": 1, "inclusive": True},
                                )
                            else:
                                _hist = await self._call_slack_api(
                                    "conversations.history",
                                    {"channel": _channel, "limit": 5},
                                )
                            _msgs = _hist.get("messages", []) if _hist.get("ok") else []
                            # Find the most recent non-bot message (subtype absent = user message)
                            _user_msg = next(
                                (m for m in _msgs if m.get("user") and not m.get("subtype") and not m.get("bot_id")),
                                None,
                            )
                            if _user_msg:
                                _uid = _user_msg.get("user", "")
                                _utext = _user_msg.get("text", "")
                                _uts = _user_msg.get("ts", "")
                                _inbound_corr_id = f"{_uid}:{_uts.replace('.', '')}"
                                _now = _time_mod.time()
                                self._last_inbound_corr[str(_channel)] = (_inbound_corr_id, _now)
                                self.tracker.record_activity(
                                    user_id=_uid,
                                    username=_uid,
                                    message_preview=_utext[:80],
                                    source="slack",
                                    direction="inbound",
                                    correlation_id=_inbound_corr_id,
                                )
                        except Exception as _re:
                            logger.debug("Slack inbound recovery error (non-fatal): %s", _re)
                    # --- Record outbound bot response ---
                    _out_uid = str(_channel)
                    if _inbound_corr_id:
                        # Use the actual user ID extracted from inbound if available
                        _inbound_uid = _inbound_corr_id.split(":")[0] if ":" in _inbound_corr_id else _out_uid
                        _out_uid = _inbound_uid
                    self.tracker.record_activity(
                        user_id=_out_uid,
                        username="bot",
                        message_preview=str(_text)[:80],
                        source="slack",
                        direction="outbound",
                        correlation_id=_inbound_corr_id,
                    )
            except Exception as _se:
                logger.debug("Slack outbound tracker error (non-fatal): %s", _se)

        return response

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

    async def _intercept_connections_open(self, payload: dict) -> dict:
        """Intercept apps.connections.open: rewrite the returned WSS URL to route
        the bot's Socket Mode WebSocket through the gateway relay.

        Flow:
          1. Call Slack's real apps.connections.open with the app-level token.
          2. Extract the WSS URL from the response.
          3. Store it under a one-time relay token.
          4. Replace the URL with ws://gateway:8080/slack-ws-relay?t=<token>.
          5. Return the modified response to the bot.

        On reconnect the bot calls apps.connections.open again, issuing a fresh token.
        """
        real_response = await self._call_slack_api("apps.connections.open", payload)
        if not real_response.get("ok"):
            return real_response
        real_url = real_response.get("url", "")
        if not real_url:
            return real_response

        token = _secrets.token_urlsafe(24)
        self._relay_tokens[token] = real_url
        logger.info("Slack relay: apps.connections.open intercepted — relay token issued")

        relay_response = dict(real_response)
        relay_response["url"] = f"ws://{_GATEWAY_WS_HOST}/slack-ws-relay?t={token}"
        return relay_response

    def consume_relay_token(self, token: str) -> str | None:
        """Pop and return the real WSS URL for a relay token (one-time use).

        Returns None if the token is unknown or already consumed.
        """
        return self._relay_tokens.pop(token, None)

    async def handle_event(self, payload: dict) -> None:
        """Handle an inbound Slack event payload received via Socket Mode.

        Called by SlackSocketClient for each ``events_api`` envelope.  Records
        collaborator inbound activity so the daily digest and SOC Activity tab
        reflect Slack messages even when the bot handles them natively.
        """
        event = payload.get("event", {})
        if event.get("type") != "message":
            return
        user_id = event.get("user", "")
        text = str(event.get("text", ""))
        if not user_id:
            return
        if self.tracker:
            try:
                import time as _time_mod
                _ts_id = str(event.get("ts", _time_mod.time())).replace(".", "")
                _corr_id = f"{user_id}:{_ts_id}"
                _now = _time_mod.time()
                self._last_inbound_corr = {
                    k: v for k, v in self._last_inbound_corr.items()
                    if _now - v[1] < 300
                }
                channel = event.get("channel", user_id)
                self._last_inbound_corr[str(channel)] = (_corr_id, _now)
                self.tracker.record_activity(
                    user_id=user_id,
                    username=user_id,
                    message_preview=text[:80],
                    source="slack",
                    direction="inbound",
                    correlation_id=_corr_id,
                )
            except Exception as exc:
                logger.debug("Slack handle_event tracker error (non-fatal): %s", exc)

    def get_stats(self) -> dict:
        return dict(self._stats)

    async def provision_group_channel(self, group_id: str, name: str) -> Optional[str]:
        """Create a Slack channel for a group. Returns channel_id or None on failure.

        Channel name is sanitized to Slack's lowercase, no-space format.
        """
        if not self._bot_token:
            return None
        safe_name = name.lower().replace(" ", "-").replace("_", "-")
        safe_name = "".join(c for c in safe_name if c.isalnum() or c == "-")[:80]
        result = await self._call_slack_api("conversations.create", {
            "name": f"group-{safe_name}",
            "is_private": False,
        })
        if result.get("ok"):
            channel_id = result.get("channel", {}).get("id")
            logger.info("Slack channel created for group %r: %s", group_id, channel_id)
            return channel_id
        logger.warning("Slack channel creation failed for group %r: %s", group_id, result.get("error"))
        return None

    async def invite_channel_member(self, channel_id: str, slack_user_id: str) -> bool:
        """Invite a Slack user to a channel. Returns True on success."""
        if not self._bot_token or not channel_id or not slack_user_id:
            return False
        result = await self._call_slack_api("conversations.invite", {
            "channel": channel_id,
            "users": slack_user_id,
        })
        if result.get("ok"):
            return True
        err = result.get("error", "")
        if err == "already_in_channel":
            return True  # idempotent
        logger.warning("Slack invite failed: channel=%s user=%s error=%s", channel_id, slack_user_id, err)
        return False

    async def kick_channel_member(self, channel_id: str, slack_user_id: str) -> bool:
        """Remove a Slack user from a channel. Returns True on success."""
        if not self._bot_token or not channel_id or not slack_user_id:
            return False
        result = await self._call_slack_api("conversations.kick", {
            "channel": channel_id,
            "user": slack_user_id,
        })
        if result.get("ok"):
            return True
        err = result.get("error", "")
        if err in ("not_in_channel", "cant_kick_self"):
            return True  # idempotent
        logger.warning("Slack kick failed: channel=%s user=%s error=%s", channel_id, slack_user_id, err)
        return False
