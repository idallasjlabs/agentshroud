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

logger = logging.getLogger("agentshroud.proxy.slack")

SLACK_API_BASE = "https://slack.com/api"

# Message methods whose text content must be scanned before forwarding to Slack
_CONTENT_METHODS = frozenset({"chat.postMessage", "chat.update", "chat.meMessage"})


def _read_secret_static(name: str, default: str = "") -> str:
    """Read a Docker secret from /run/secrets/<name>."""
    try:
        with open(f"/run/secrets/{name}", "r") as fh:
            return fh.read().strip()
    except (FileNotFoundError, OSError):
        return default


class SlackAPIProxy:
    """Proxies bot Slack Web API calls through SecurityPipeline.

    Outbound flow (bot-initiated Slack API call):
        Bot -> POST /slack-api/<method> -> pipeline.process_outbound -> slack.com/api/<method>
    """

    def __init__(
        self,
        pipeline=None,
        middleware_manager=None,
        sanitizer=None,
        tracker=None,
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

        self._stats: dict[str, int] = {
            "outbound_forwarded": 0,
            "outbound_blocked": 0,
        }

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
                    if result.sanitized_message and "text" in payload:
                        payload["text"] = result.sanitized_message
                except Exception as exc:
                    logger.error(f"Slack proxy: pipeline outbound error: {exc}")

        # Forward to Slack API
        response = await self._call_slack_api(method, payload)
        self._stats["outbound_forwarded"] += 1

        # Log bot responses to collaborator activity tracker for /collabs reports.
        # Only track chat.postMessage (actual message sends, not edits or reactions).
        # The Slack channel field is used as the user_id key; for DMs this is the
        # user's member ID (U...), for channels it's the channel ID (C...).
        if method == "chat.postMessage" and not is_system and self.tracker:
            try:
                _channel = payload.get("channel", "")
                _text = payload.get("text", "")
                if isinstance(_text, (list, dict)):
                    import json as _json
                    _text = _json.dumps(_text)
                if _channel and _text:
                    self.tracker.record_activity(
                        user_id=str(_channel),
                        username="bot",
                        message_preview=str(_text)[:80],
                        source="slack",
                        direction="outbound",
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

    def get_stats(self) -> dict:
        return dict(self._stats)
