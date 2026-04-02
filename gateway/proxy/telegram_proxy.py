# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
"""
Telegram API Reverse Proxy — intercepts all bot ↔ Telegram traffic.

The gateway acts as a man-in-the-middle for Telegram Bot API calls:
- Inbound: Messages from users are scanned (PII detection, injection defense)
- Outbound: Bot responses are filtered (credential blocking, XML stripping)

The bot connects to http://gateway:8080/telegram-api/bot<token>/<method>
instead of https://api.telegram.org/bot<token>/<method>.
"""

from __future__ import annotations

import asyncio
import datetime as _dt
import ipaddress
import json
import logging
import math
import os
import re
import ssl
import time
import urllib.error
import urllib.parse
import urllib.request
import uuid
from typing import Any, Optional
from urllib.parse import urlparse

from gateway.security.input_normalizer import normalize_input, strip_markdown_exfil
from gateway.security.rbac_config import RBACConfig, persist_approved_collaborator
from gateway.utils.secrets import read_secret as _read_secret_static

logger = logging.getLogger("agentshroud.proxy.telegram_api")

TELEGRAM_API_BASE = "https://api.telegram.org"
_SUPPRESS_OUTBOUND_TOKEN = "__AGENTSHROUD_SUPPRESS_OUTBOUND__"

# Maximum file size accepted from inbound media (50 MB — matches Telegram Bot API limit).
# Telegram includes a `file_size` field on document/video/audio/voice/photo objects.
# Payloads exceeding this are dropped before reaching the bot (CVE-2026-32049 mitigation).
_MAX_MEDIA_FILE_SIZE = int(os.environ.get("AGENTSHROUD_MAX_MEDIA_BYTES", 50 * 1024 * 1024))

# Media object keys that carry a file_size field in Telegram updates.
_MEDIA_KEYS = ("document", "video", "audio", "voice", "video_note", "animation", "sticker")

# Slash-commands that are forbidden for collaborators (owner-only capabilities)
_COLLABORATOR_BLOCKED_COMMANDS = {
    "/skill",
    "/1password",
    "/op",
    "/exec",
    "/run",
    "/cron",
    "/ssh",
    "/admin",
    "/config",
    "/secret",
    "/key",
    "/token",
    "/memory",
    "/reset",
    "/kill",
    "/restart",
    "/update",
}
_LOCAL_HEALTHCHECK_COMMANDS = {
    "/healthcheck",
    "healthcheck",
    "/self-diagnostic",
    "self-diagnostic",
    "/self-diagnose",
    "self-diagnose",
}
_LOCAL_STATUS_COMMANDS = {
    "/status",
    "status",
}
_LOCAL_MODEL_STATUS_COMMANDS = {
    "/model",
    "model",
    "/model-status",
    "model-status",
}
_LOCAL_WHOAMI_COMMANDS = {
    "/whoami",
    "whoami",
    "/id",
    "id",
}
_LOCAL_START_COMMANDS = {
    "/start",
    "start",
}
_LOCAL_HELP_COMMANDS = {
    "/help",
    "help",
}
_LOCAL_REVOKE_COMMANDS = {
    "/revoke",
    "revoke",
}
_LOCAL_APPROVE_COMMANDS = {
    "/approve",
    "approve",
}
_LOCAL_DENY_COMMANDS = {
    "/deny",
    "deny",
}
_LOCAL_ADD_COLLAB_COMMANDS = {
    "/addcollab",
    "addcollab",
    "/allow",
    "allow",
}
_LOCAL_RESTORE_COLLABS_COMMANDS = {
    "/restorecollabs",
    "restorecollabs",
    "/restore-collaborators",
    "restore-collaborators",
}
_LOCAL_UNLOCK_COMMANDS = {
    "/unlock",
    "unlock",
}
_LOCAL_LOCKED_COMMANDS = {
    "/locked",
    "locked",
    "/lockstatus",
    "lockstatus",
}
_LOCAL_GRANT_IMMUNITY_COMMANDS = {
    "/grant-immunity",
    "grant-immunity",
    "/gi",
    "gi",
}
_LOCAL_REVOKE_IMMUNITY_COMMANDS = {
    "/revoke-immunity",
    "revoke-immunity",
    "/ri",
    "ri",
}
_LOCAL_IMMUNE_COMMANDS = {
    "/immune",
    "immune",
}
_LOCAL_PENDING_COMMANDS = {
    "/pending",
    "pending",
    "/approvals",
    "approvals",
}
_LOCAL_EGRESS_COMMANDS = {
    "/egress",
    "egress",
}
_LOCAL_EGRESS_ALLOW_COMMANDS = {
    "/egress-allow",
    "egress-allow",
}
_LOCAL_SETNAME_COMMANDS = {
    "/setname",
    "setname",
}
_LOCAL_COLLABS_COMMANDS = {
    "/collabs",
    "collabs",
    "/listcollabs",
    "listcollabs",
}
# V9-4F — Group + project commands
_LOCAL_GROUPS_COMMANDS = {"/groups", "groups"}
_LOCAL_GROUPINFO_COMMANDS = {"/groupinfo", "groupinfo"}
_LOCAL_PROJECTS_COMMANDS = {"/projects", "projects"}
_LOCAL_ADDTOGROUP_COMMANDS = {"/addtogroup", "addtogroup"}
_LOCAL_RMFROMGROUP_COMMANDS = {"/rmfromgroup", "rmfromgroup"}
_LOCAL_SETMODE_COMMANDS = {"/setmode", "setmode"}
_LOCAL_DELEGATE_COMMANDS = {"/delegate", "delegate"}
_LOCAL_DELEGATIONS_COMMANDS = {"/delegations", "delegations"}
_LOCAL_REVOKE_DELEGATION_COMMANDS = {
    "/revoke_delegation",
    "revoke_delegation",
    "/revoke-delegation",
    "revoke-delegation",
    "/revokedelegation",
    "revokedelegation",
}

# Group management — owner-only
_LOCAL_NEWGROUP_COMMANDS = {"/newgroup", "newgroup"}
_LOCAL_LINKGROUP_COMMANDS = {"/linkgroup", "linkgroup"}
_LOCAL_ADDMEMBER_COMMANDS = {"/addmember", "addmember", "/addtogroup", "addtogroup"}
_LOCAL_REMOVEMEMBER_COMMANDS = {"/removemember", "removemember", "/kickmember", "kickmember"}
_LOCAL_LISTGROUPS_COMMANDS = {"/listgroups", "listgroups", "/groups", "groups"}
_COLLABORATOR_ALLOWED_SLASH_COMMANDS = {
    "/start",
    "/help",
    "/status",
    "/healthcheck",
    "/self-diagnostic",
    "/self-diagnose",
    "/model",
    "/model-status",
    "/whoami",
    "/id",
    "/groups",
    "/groupinfo",
    "/projects",
    "/setname",
}

_DISCLOSURE_MESSAGE = (
    "\U0001f6e1\ufe0f *AgentShroud Notice*\n\n"
    "This conversation is logged and may be reviewed as part of the AgentShroud\u2122 "
    "project\\. By continuing, you acknowledge this\\. Questions? Reach out to Isaiah directly\\.\n\n"
    "_Bot commands like /skill aren't available in collaborator mode\\. "
    "I'm the collaborator\\-facing assistant with read\\-only access \u2014 if authorized, I can discuss "
    "AgentShroud's features, security concepts, and provide technical advice, but I don't "
    "have access to the full command set\\._"
)

_PROTECT_PREFIX = "🛡️ Protected by AgentShroud"
_PROTECT_HEADER = f"{_PROTECT_PREFIX}\n\n"
_COLLABORATOR_BLOCK_NOTICE = f"{_PROTECT_HEADER}This action is not allowed."
_COLLABORATOR_UNAVAILABLE_NOTICE = f"{_PROTECT_HEADER}I can't do that right now."
_COLLABORATOR_FILE_NOTICE = (
    f"{_PROTECT_HEADER}File/system content access is restricted for collaborators."
)
_COLLABORATOR_SECRET_NOTICE = f"{_PROTECT_HEADER}Sensitive credentials/secrets are restricted."
_COLLABORATOR_EGRESS_NOTICE = (
    f"{_PROTECT_HEADER}"
    "External access requires approval.\n"
    "This request is owner-gated and available when permitted by the owner."
)
_COLLABORATOR_EGRESS_PENDING_NOTICE = (
    f"{_PROTECT_HEADER}" "This request is owner-gated and available when permitted by the owner."
)
_COLLABORATOR_SCOPE_NOTICE = (
    f"{_PROTECT_HEADER}"
    "If authorized, I can discuss system concepts and recommendations, but command/tool execution details are restricted."
)
_PROTECTED_POLICY_NOTICE = f"{_PROTECT_HEADER}Response blocked by security policy."
_COLLABORATOR_SAFE_INFO_NOTICE = (
    f"{_PROTECT_HEADER}"
    "Collaborator safe mode is active.\n"
    "If authorized, I can assist with architecture, security concepts, workflows, and recommendations.\n"
    "Many capabilities are discoverable but owner-gated.\n"
    "I cannot provide command/tool outputs, direct file contents, secrets, or system-level execution."
)

# Owner-friendly labels for known collaborator IDs.
_KNOWN_COLLABORATOR_LABELS: dict[str, str] = {
    "8506022825": "Brett Galura",
    "8545356403": "Chris Shelton",
    "15712621992": "Gabriel Fuentes",
    "8279589982": "Steve Hay",
    "8526379012": "TJ Winter",
    "7614658040": "Isaiah (collaborator test)",
    "8633775668": "Ana",
}
_KNOWN_COLLABORATOR_ALIASES: dict[str, str] = {
    "brett": "8506022825",
    "brettgalura": "8506022825",
    "chris": "8545356403",
    "chrisshelton": "8545356403",
    "gabriel": "15712621992",
    "gabrielfuentes": "15712621992",
    "steve": "8279589982",
    "stevehay": "8279589982",
    "tj": "8526379012",
    "tjwinter": "8526379012",
    "isaiahcollab": "7614658040",
    "ana": "8633775668",
}


class TelegramAPIProxy:
    """Proxies Telegram Bot API calls through the security pipeline."""

    def __init__(self, pipeline=None, middleware_manager=None, sanitizer=None):
        self.pipeline = pipeline
        self.middleware_manager = middleware_manager
        self.sanitizer = sanitizer
        self._stats = {
            "total_requests": 0,
            "messages_scanned": 0,
            "messages_sanitized": 0,
            "messages_blocked": 0,
            "outbound_filtered": 0,
            "inbound_updates_total": 0,
            "inbound_updates_forwarded": 0,
            "inbound_updates_dropped": 0,
        }
        # Read token from env var; fall back to Docker secret so gateway container
        # can send local command responses even without TELEGRAM_BOT_TOKEN in env.
        self._bot_token = os.environ.get("TELEGRAM_BOT_TOKEN", "") or _read_secret_static(
            "telegram_bot_token"
        )
        self._ssl_context = ssl.create_default_context()
        self._max_outbound_chars = int(os.environ.get("AGENTSHROUD_MAX_OUTBOUND_CHARS", "3800"))
        self._block_cascade_seconds = float(
            os.environ.get("AGENTSHROUD_BLOCK_CASCADE_SECONDS", "4.0")
        )
        self._block_cascade_threshold = int(
            os.environ.get("AGENTSHROUD_BLOCK_CASCADE_THRESHOLD", "3")
        )
        self._block_cascade_window_seconds = float(
            os.environ.get("AGENTSHROUD_BLOCK_CASCADE_WINDOW_SECONDS", "300.0")
        )
        self._recent_outbound_blocks_until: dict[str, float] = {}
        self._outbound_block_timestamps: dict[str, list[float]] = {}
        self._system_notice_cooldown_seconds = float(
            os.environ.get("AGENTSHROUD_SYSTEM_NOTICE_COOLDOWN_SECONDS", "120.0")
        )
        self._recent_system_notice_until: dict[tuple[str, str], float] = {}
        self._web_fetch_approval_cooldown_seconds = float(
            os.environ.get("AGENTSHROUD_WEB_FETCH_APPROVAL_COOLDOWN_SECONDS", "20.0")
        )
        self._recent_web_fetch_approval_until: dict[tuple[str, str], float] = {}
        self._no_reply_notice_cooldown_seconds = float(
            os.environ.get("AGENTSHROUD_NO_REPLY_NOTICE_COOLDOWN_SECONDS", "15.0")
        )
        self._recent_no_reply_notice_until: dict[str, float] = {}
        self._rate_limit_notice_cooldown_seconds = float(
            os.environ.get("AGENTSHROUD_RATE_LIMIT_NOTICE_COOLDOWN_SECONDS", "30.0")
        )
        self._recent_rate_limit_notice_until: dict[str, float] = {}
        self._handled_local_command_update_ids: dict[str, float] = {}
        self._local_command_dedupe_ttl_seconds = float(
            os.environ.get("AGENTSHROUD_LOCAL_COMMAND_DEDUPE_TTL_SECONDS", "600.0")
        )

        # Group chat at-mention filter: bot reads ALL group messages for context but only
        # responds when @mentioned. Requires TELEGRAM_BOT_USERNAME (without @).
        # Set AGENTSHROUD_GROUP_MENTION_ONLY=0 to respond to every group message.
        self._bot_username = os.environ.get("TELEGRAM_BOT_USERNAME", "").strip().lstrip("@").lower()
        self._group_mention_only = os.environ.get(
            "AGENTSHROUD_GROUP_MENTION_ONLY", "1"
        ).strip().lower() not in ("0", "false", "no")
        # Tracks whether the bot should respond in each group chat. True = @mentioned,
        # False = context only (suppress outbound). Keyed by chat_id (int).
        self._group_response_eligible: dict[int, bool] = {}

        # Progressive lockdown: per-user cumulative block counter with escalating responses.
        # 3 blocks → owner alert; 5 blocks → double rate limit window; 10 → session suspended.
        try:
            from gateway.security.progressive_lockdown import ProgressiveLockdown

            self._lockdown = ProgressiveLockdown()
        except Exception:
            self._lockdown = None

        # Track which collaborator user IDs have already received the disclosure notice
        # this session. Persisted in-memory only — resets on gateway restart (acceptable).
        self._disclosure_sent: set[str] = set()
        self._runtime_revoked_collaborators: set[str] = set()
        self._pending_collaborator_requests: dict[str, dict[str, Any]] = {}
        # Map str(chat_id) → user_id for known collaborators. Used to attribute
        # outbound bot sendMessage calls to the correct collaborator in activity logs.
        self._collaborator_chat_ids: dict[str, str] = {}
        # Map str(chat_id) → (correlation_id, timestamp) for inbound→outbound pairing
        self._last_inbound_corr: dict[str, tuple] = {}
        self._pending_collaborator_request_cooldown_seconds = float(
            os.environ.get("AGENTSHROUD_COLLAB_REQUEST_COOLDOWN_SECONDS", "90.0")
        )

        # Cache RBAC config to avoid re-instantiating on every message
        try:
            from gateway.security.rbac_config import RBACConfig

            self._rbac = RBACConfig()
        except Exception:
            self._rbac = None

        # Pre-populate collaborator_chat_ids from RBAC so outbound tracking fires
        # even if the collaborator hasn't sent an inbound message this session.
        # In Telegram private chats, chat_id == user_id — safe to pre-seed.
        if self._rbac:
            for _uid in self._rbac.collaborator_user_ids:
                self._collaborator_chat_ids[str(_uid)] = str(_uid)

        # Per-user collaborator rate limiter: configurable (default 1000/hour)
        from gateway.ingest_api.auth import RateLimiter

        self._collaborator_rate_limit_max_requests = int(
            os.environ.get("AGENTSHROUD_COLLAB_RATE_LIMIT_MAX_REQUESTS", "5000")
        )
        self._collaborator_rate_limit_window_seconds = int(
            os.environ.get("AGENTSHROUD_COLLAB_RATE_LIMIT_WINDOW_SECONDS", "3600")
        )
        self._collaborator_rate_limiter = RateLimiter(
            max_requests=self._collaborator_rate_limit_max_requests,
            window_seconds=self._collaborator_rate_limit_window_seconds,
        )

        # Stranger rate limiter: unknown/unapproved users get much stricter limits
        # to prevent access-request queue flooding (default: 5 requests per hour).
        self._stranger_rate_limit_max_requests = int(
            os.environ.get("AGENTSHROUD_STRANGER_RATE_LIMIT_MAX_REQUESTS", "5")
        )
        self._stranger_rate_limit_window_seconds = int(
            os.environ.get("AGENTSHROUD_STRANGER_RATE_LIMIT_WINDOW_SECONDS", "3600")
        )
        self._stranger_rate_limiter = RateLimiter(
            max_requests=self._stranger_rate_limit_max_requests,
            window_seconds=self._stranger_rate_limit_window_seconds,
        )
        self._recent_stranger_rate_limit_until: dict[str, float] = {}
        # Cooldown for "session suspended" drop notices sent to collaborators.
        # Prevents spamming the user on every dropped message; default 5 min.
        self._suspended_drop_notice_cooldown_seconds = float(
            os.environ.get("AGENTSHROUD_SUSPENDED_DROP_NOTICE_COOLDOWN_SECONDS", "300.0")
        )
        self._suspended_drop_notice_until: dict[str, float] = {}
        # Immunity map: user_id → expiry timestamp (0.0 = no expiry).
        # Owner-only; intended for testing collaborator accounts. In-memory only.
        # Default TTL if owner does not specify a duration: 8 hours.
        self._immune_users: dict[str, float] = {}
        self._immunity_default_ttl_seconds: float = float(
            os.environ.get("AGENTSHROUD_IMMUNITY_DEFAULT_TTL_SECONDS", str(8 * 3600))
        )

        # Collaborator self-set display names. Persisted to /app/data/ so they
        # survive gateway restarts. Loaded eagerly at __init__ time.
        self._custom_display_names: dict[str, str] = {}
        self._display_names_path = os.environ.get(
            "AGENTSHROUD_DISPLAY_NAMES_PATH", "/app/data/collaborator_display_names.json"
        )
        try:
            import json as _json

            with open(self._display_names_path, "r", encoding="utf-8") as _dnf:
                self._custom_display_names = _json.load(_dnf)
        except (FileNotFoundError, ValueError):
            pass
        except Exception as _dne:
            logger.debug("Could not load display names: %s", _dne)

    def _is_immune(self, user_id: str) -> bool:
        """Return True if user_id has active (non-expired) immunity."""
        expiry = self._immune_users.get(user_id)
        if expiry is None:
            return False
        if expiry != 0.0 and time.time() >= expiry:
            del self._immune_users[user_id]
            logger.info("Immunity expired for user %s", user_id)
            return False
        return True

    def _is_owner_chat(self, chat_id: str) -> bool:
        """Return True when chat_id belongs to the configured owner.

        Handles both real Telegram owner chat_ids and Slack bridge fake chat_ids.
        Bridge chat_ids are positive integers in the _BRIDGE_BASE range; the bridge
        tracks which Slack user originated each session so we can delegate to rbac.is_owner().
        """
        if not self._rbac:
            return False
        if str(chat_id) == str(getattr(self._rbac, "owner_user_id", "")):
            return True
        return False

    @staticmethod
    def _is_group_message(message: dict) -> bool:
        """Return True if message originates from a group or supergroup chat."""
        return (message.get("chat") or {}).get("type") in ("group", "supergroup")

    @staticmethod
    def _bot_is_mentioned(message: dict, bot_username: str) -> bool:
        """Return True if the bot is @mentioned or a bot_command targets this bot.

        Checks both text entities and caption_entities (media messages with captions).
        """
        if not bot_username:
            return False
        text = message.get("text") or message.get("caption") or ""
        entities = message.get("entities") or message.get("caption_entities") or []
        for entity in entities:
            etype = entity.get("type")
            if etype == "mention":
                offset = entity.get("offset", 0)
                length = entity.get("length", 0)
                mention_text = text[offset : offset + length].lstrip("@").lower()
                if mention_text == bot_username:
                    return True
            elif etype == "bot_command":
                # /command@botname — targeted command for this bot
                offset = entity.get("offset", 0)
                length = entity.get("length", 0)
                cmd_text = text[offset : offset + length].lower()
                if f"@{bot_username}" in cmd_text:
                    return True
        return False

    async def _telegram_create_invite_link(self, chat_id: int) -> Optional[str]:
        """Create a single-use invite link for a Telegram group. Returns URL or None."""
        if not self._bot_token:
            return None
        try:
            url = f"{TELEGRAM_API_BASE}/bot{self._bot_token}/createChatInviteLink"
            body = json.dumps({"chat_id": chat_id, "member_limit": 1}).encode()
            resp = await self._forward_to_telegram(url, body, "application/json")
            if resp.get("ok"):
                return resp.get("result", {}).get("invite_link")
        except Exception as exc:
            logger.debug("createChatInviteLink error: %s", exc)
        return None

    async def _telegram_kick_member(self, chat_id: int, user_id: int) -> bool:
        """Kick (ban + unban) a user from a Telegram group. Returns True on success."""
        if not self._bot_token:
            return False
        try:
            ban_url = f"{TELEGRAM_API_BASE}/bot{self._bot_token}/banChatMember"
            ban_body = json.dumps({"chat_id": chat_id, "user_id": user_id}).encode()
            ban_resp = await self._forward_to_telegram(ban_url, ban_body, "application/json")
            if not ban_resp.get("ok"):
                return False
            # Immediately unban so the user can rejoin later via invite link
            unban_url = f"{TELEGRAM_API_BASE}/bot{self._bot_token}/unbanChatMember"
            unban_body = json.dumps(
                {"chat_id": chat_id, "user_id": user_id, "only_if_banned": True}
            ).encode()
            await self._forward_to_telegram(unban_url, unban_body, "application/json")
            return True
        except Exception as exc:
            logger.debug("Telegram kick error: %s", exc)
        return False

    def _set_outbound_block_cascade(self, chat_id: str, *, force: bool = False) -> None:
        """Activate per-chat cascade window to prevent streaming-fragment leak-through.

        Args:
            force: When True, activates the cascade window immediately (used for
                   deterministic blocks like over-length). When False, activates only
                   after _block_cascade_threshold blocks within _block_cascade_window_seconds
                   (default: 3 in 5 min) — prevents one pipeline false-positive from
                   cascade-locking the conversation.
        """
        if not chat_id:
            return
        now = time.time()
        if force:
            self._recent_outbound_blocks_until[chat_id] = now + self._block_cascade_seconds
            return
        timestamps = self._outbound_block_timestamps.get(chat_id, [])
        # Prune timestamps outside the rolling window.
        timestamps = [t for t in timestamps if now - t < self._block_cascade_window_seconds]
        timestamps.append(now)
        self._outbound_block_timestamps[chat_id] = timestamps
        if len(timestamps) >= self._block_cascade_threshold:
            self._recent_outbound_blocks_until[chat_id] = now + self._block_cascade_seconds

    @staticmethod
    def _normalize_command_token(text: str) -> str:
        """Normalize first command token so small obfuscations don't bypass local handlers."""
        if not isinstance(text, str) or not text.strip():
            return ""
        first = normalize_input(text).strip().split()[0].lower()
        first = first.split("@")[0]
        return re.sub(r"[^a-z0-9_/\-]", "", first)

    @staticmethod
    def _extract_owner_revoke_target(text: str) -> Optional[str]:
        """Parse /revoke <telegram_user_id> and return normalized target id."""
        if not isinstance(text, str):
            return None
        tokens = normalize_input(text).strip().split()
        if len(tokens) < 2:
            return None
        candidate = re.sub(r"[^0-9]", "", tokens[1])
        if not candidate:
            return None
        return candidate

    @staticmethod
    def _extract_owner_target(text: str) -> Optional[str]:
        """Parse owner command target as numeric id or known collaborator alias."""
        if not isinstance(text, str):
            return None
        tokens = normalize_input(text).strip().lower().split()
        if len(tokens) < 2:
            return None
        raw = re.sub(r"[^a-z0-9_]", "", tokens[1])
        if not raw:
            return None
        if raw.isdigit():
            return raw
        return _KNOWN_COLLABORATOR_ALIASES.get(raw)

    def _resolve_pending_username_target(self, text: str) -> Optional[str]:
        """Resolve owner target from pending-request username aliases (e.g., /approve ana)."""
        if not isinstance(text, str):
            return None
        tokens = normalize_input(text).strip().lower().split()
        if len(tokens) < 2:
            return None
        raw = re.sub(r"[^a-z0-9_@]", "", tokens[1]).lstrip("@")
        if not raw:
            return None
        for user_id, pending in (self._pending_collaborator_requests or {}).items():
            username = str((pending or {}).get("username", "")).strip().lower()
            if not username:
                continue
            username = username.lstrip("@")
            if raw == username:
                return str(user_id)
            # Allow "ana" to match "ana_smith" prefix style for operator ergonomics.
            if username.startswith(raw) and len(raw) >= 3:
                return str(user_id)
        return None

    def _extract_owner_target_resolved(self, text: str) -> Optional[str]:
        """Resolve target by id, static alias, or pending username alias.

        Resolution order:
        1. Numeric ID → return immediately.
        2. Static known-collaborator alias → return only if that ID has a pending
           request, otherwise fall through to pending username resolution so that
           e.g. ``/approve ana`` matches a pending user named "ana_smith" even when
           "ana" is a static alias for a different user.
        3. Pending username prefix match (e.g., "ana" matches "ana_smith").
        """
        target = self._extract_owner_target(text)
        if target:
            # If the static alias resolves to a numeric ID that has a pending
            # collaborator request, prefer it.  Otherwise fall through to the
            # pending username resolver so operator shorthands like /approve ana
            # still work when "ana" is mapped to a different static collaborator ID.
            if target.isdigit() and target in self._pending_collaborator_requests:
                return target
            if target.isdigit() and target not in self._pending_collaborator_requests:
                # Try pending username first; fall back to static alias if no match.
                pending_match = self._resolve_pending_username_target(text)
                if pending_match:
                    return pending_match
            return target
        return self._resolve_pending_username_target(text)

    def _resolve_display_name(self, user_id: str) -> str:
        """Resolve a readable label for user id when available.

        Priority: user self-set name → env override → known labels dict → raw user_id.
        """
        user_id = str(user_id or "").strip()
        if not user_id:
            return "unknown"
        # Highest priority: user-set display name via /setname
        if user_id in self._custom_display_names:
            return f"{self._custom_display_names[user_id]} ({user_id})"
        # Optional override via env: "id:name,id:name"
        env_labels = os.environ.get("AGENTSHROUD_COLLABORATOR_LABELS", "")
        if env_labels:
            try:
                for pair in env_labels.split(","):
                    if ":" not in pair:
                        continue
                    k, v = pair.split(":", 1)
                    if k.strip() == user_id and v.strip():
                        return f"{v.strip()} ({user_id})"
            except Exception:
                pass
        if user_id in _KNOWN_COLLABORATOR_LABELS:
            return f"{_KNOWN_COLLABORATOR_LABELS[user_id]} ({user_id})"
        return user_id

    async def _queue_collaborator_access_request(
        self,
        *,
        user_id: str,
        chat_id: Optional[int],
        username: str,
    ) -> None:
        """Queue owner approval request for unknown/revoked users."""
        if not self._rbac:
            return
        now = time.time()
        owner_id = str(getattr(self._rbac, "owner_user_id", "")).strip()
        if not owner_id or not owner_id.isdigit():
            return
        pending = self._pending_collaborator_requests.get(str(user_id))
        if pending and float(pending.get("expires_at", 0.0)) > now:
            if chat_id:
                await self._send_collaborator_pending_notice(chat_id)
            return

        self._pending_collaborator_requests[str(user_id)] = {
            "user_id": str(user_id),
            "chat_id": str(chat_id or ""),
            "username": username or "unknown",
            "requested_at": now,
            "expires_at": now + self._pending_collaborator_request_cooldown_seconds,
        }
        _display_name = f"@{username}" if username and username != "unknown" else f"ID {user_id}"
        _notif_text = (
            f"{_PROTECT_HEADER}"
            f"*Access Request*\n\n"
            f"User: {_display_name}\n"
            f"ID: `{user_id}`\n"
            f"Action required: approve or deny below."
        )
        _keyboard = {
            "inline_keyboard": [
                [
                    {"text": "✅ Approve", "callback_data": f"collab_approve_{user_id}"},
                    {"text": "❌ Deny", "callback_data": f"collab_deny_{user_id}"},
                ]
            ]
        }
        sent = await self._send_telegram_with_keyboard(int(owner_id), _notif_text, _keyboard)
        if not sent:
            # Fall back to plain text if keyboard send fails
            await self._send_owner_admin_notice(
                int(owner_id),
                (
                    f"{_PROTECT_HEADER}"
                    "Collaborator access request pending.\n"
                    f"User: {_display_name} ({user_id})\n"
                    "Owner action: /approve <user_id> or /deny <user_id>"
                ),
            )
        if chat_id:
            await self._send_collaborator_pending_notice(chat_id)

    @staticmethod
    def _rewrite_known_runtime_errors(text: str) -> Optional[str]:
        """Map recurring runtime/provider failures to deterministic operator guidance."""
        if not isinstance(text, str):
            return None
        lowered = text.lower()
        if "agents.defaults.memorysearch.provider" in lowered and "memory search" in lowered:
            return (
                "⚠️ Runtime dependency error while preparing the response. "
                "Please retry your last message in 10–20 seconds. "
                "If this keeps happening, switch model profile with scripts/switch_model.sh."
            )
        if "memory search is unavailable in this runtime profile" in lowered:
            return (
                "⚠️ Runtime dependency error while preparing the response. "
                "Please retry your last message in 10–20 seconds. "
                "If this keeps happening, switch model profile with scripts/switch_model.sh."
            )
        if lowered.strip() in {"404 status code (no body)", "500 status code (no body)"}:
            return (
                "⚠️ Runtime transport error while preparing the response. "
                "Please retry your last message in 10–20 seconds. "
                "If this keeps happening, run /healthcheck."
            )
        if lowered.strip() == "no response generated. please try again.":
            return (
                "⚠️ Runtime response generation failed before completion. "
                "Please retry your last message in 10–20 seconds."
            )
        if lowered.strip() in {
            "we are currently using the model",
            "we are currently using the model.",
        }:
            active_model = (
                os.environ.get("OPENCLAW_MAIN_MODEL")
                or os.environ.get("AGENTSHROUD_CLOUD_MODEL_REF")
                or os.environ.get("AGENTSHROUD_LOCAL_MODEL_REF")
                or "unknown"
            )
            return f"ℹ️ Current model: {active_model}"
        if lowered.strip().startswith("we are currently using the model"):
            active_model = (
                os.environ.get("OPENCLAW_MAIN_MODEL")
                or os.environ.get("AGENTSHROUD_CLOUD_MODEL_REF")
                or os.environ.get("AGENTSHROUD_LOCAL_MODEL_REF")
                or "unknown"
            )
            return f"ℹ️ Current model: {active_model}"
        if "llm request timed out" in lowered or (
            "timed out" in lowered and "agent failed before reply" in lowered
        ):
            return (
                "⏳ Model response timed out before completion. "
                "Please retry in 10–20 seconds. "
                "If this repeats, switch model profile with scripts/switch_model.sh "
                "(for example: gemini or local qwen3:14b)."
            )
        if (
            ("memory search" in lowered and ("unavailable" in lowered or "disabled" in lowered))
            and re.search(r"embedding(?:\s*[/_-]?\s*)provider", lowered)
            and "error" in lowered
        ):
            explicit_memory_command = any(
                marker in lowered
                for marker in (
                    "memory search command",
                    "run memory search",
                    "execute memory search",
                    "/memory",
                    "memory_search",
                )
            )
            if not explicit_memory_command:
                return (
                    "⚠️ Runtime dependency error while preparing the response. "
                    "Please retry your last message in 10–20 seconds. "
                    "If this keeps happening, switch model profile with scripts/switch_model.sh."
                )
            return (
                "⚠️ Memory search is unavailable in this runtime profile. "
                "Switch to a configured embedding-capable profile (for example: "
                "scripts/switch_model.sh gemini), or configure "
                "agents.defaults.memorySearch.provider, then retry."
            )
        if (
            "healthcheck" in lowered
            and "skill.md" in lowered
            and "sandbox" in lowered
            and re.search(r"(?:unable|cannot)\s+(?:to\s+)?access|can't\s+access", lowered)
        ):
            return (
                "✅ Healthcheck is handled directly by the AgentShroud gateway. "
                "Use /healthcheck and status will be returned directly."
            )
        return None

    def get_stats(self) -> dict:
        return dict(self._stats)

    @staticmethod
    def _sanitize_reason(reason: str) -> str:
        """Strip internal paths and module names from block reasons before user display."""
        # Remove Python module paths (gateway.security.module_name patterns)
        sanitized = re.sub(r"gateway\.[a-z_.]+", "[internal]", reason)
        # Remove absolute file paths (/app/..., /home/..., /usr/...)
        sanitized = re.sub(r"/[a-z][a-zA-Z0-9/_.-]+\.py(?:\s+line\s+\d+)?", "", sanitized)
        return sanitized.strip()

    @staticmethod
    def _looks_like_file_query(text: str) -> bool:
        """Best-effort guardrail: collaborator prompts requesting direct file access."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        internal_file_markers = (
            "bootstrap.md",
            "identity.md",
            "memory.md",
            "skill.md",
            "soul.md",
            "heartbeat.md",
            "agents.md",
        )
        content_request_markers = (
            "show",
            "read",
            "open",
            "cat",
            "print",
            "dump",
            "contents",
            "what's in",
            "what is in",
        )
        if any(marker in lowered for marker in internal_file_markers) and any(
            marker in lowered for marker in content_request_markers
        ):
            return True
        patterns = (
            r"\b(show|read|open|cat|print|dump)\b.{0,32}\b(file|contents?|workspace|directory)\b",
            r"\b(list|enumerate)\b.{0,24}\b(files?|directories|workspace)\b",
            r"\b(ls|find|grep|cat)\b.{0,64}\b(workspace|\.md|\.env|identity\.md|bootstrap\.md)\b",
            r"\bwhat'?s in\b.{0,24}\b(identity\.md|bootstrap\.md|memory\.md)\b",
        )
        return any(re.search(pat, lowered) for pat in patterns)

    @staticmethod
    def _looks_like_file_metadata_question(text: str) -> bool:
        """Detect conceptual file-purpose questions without direct content requests."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        mixed_bootstrap_identity_probe = (
            "bootstrap.md" in lowered
            and "identity.md" in lowered
            and any(
                token in lowered for token in ("what are those", "what are they", "what are these")
            )
        )
        if (
            any(
                token in lowered
                for token in ("show me", "contents", "read", "open", "cat", "print", "dump")
            )
            and not mixed_bootstrap_identity_probe
        ):
            return False
        return any(
            token in lowered
            for token in (
                "what is bootstrap.md",
                "what's bootstrap.md",
                "what are bootstrap.md",
                "what is identity.md",
                "what's identity.md",
                "what are identity.md",
                "what are those",
                "what are those files",
                "what do those files do",
            )
        )

    @staticmethod
    def _looks_like_model_status_question(text: str) -> bool:
        """Detect plain-language model status questions for deterministic local reply."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        return any(
            phrase in lowered
            for phrase in (
                "which model are we using",
                "what model are we using",
                "what model is active",
                "which model is active",
                "current model",
                "model in use",
            )
        )

    @staticmethod
    def _is_no_reply_token(text: str) -> bool:
        """Detect plain NO_REPLY sentinel with light punctuation wrapping."""
        if not isinstance(text, str):
            return False
        normalized = normalize_input(text).strip()
        if normalized.startswith("```") and normalized.endswith("```"):
            inner = normalized[3:-3].strip()
            if "\n" in inner:
                first, *rest = inner.splitlines()
                if re.fullmatch(r"[a-z0-9_-]+", first.strip(), flags=re.IGNORECASE):
                    inner = "\n".join(rest).strip()
            normalized = inner
        normalized = normalized.strip("`'\"[](){}<>.,;:!?")
        return normalized.upper() == "NO_REPLY"

    @staticmethod
    def _looks_like_filename_reference(candidate: str) -> bool:
        """Best-effort check to avoid treating local file names as egress domains."""
        if not isinstance(candidate, str):
            return False
        lowered = normalize_input(candidate).strip().lower()
        if not lowered or "/" in lowered or " " in lowered or ":" in lowered:
            return False
        return bool(
            re.fullmatch(
                r"[a-z0-9._-]+\.(?:md|txt|json|yaml|yml|csv|log|cfg|conf|ini|toml|py|js|ts|sh)",
                lowered,
            )
        )

    @staticmethod
    def _looks_like_sensitive_path_probe(text: str) -> bool:
        """Detect collaborator prompts probing sensitive filesystem paths/secrets."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        path_markers = (
            "/etc/",
            "/proc/",
            "/run/secrets",
            "/var/run/secrets",
            "~/.ssh",
            ".ssh/",
            "~/.aws/credentials",
            ".aws/credentials",
            ".env",
            "id_rsa",
            "known_hosts",
            "authorized_keys",
        )
        if not any(marker in lowered for marker in path_markers):
            return False
        intent_markers = (
            "show",
            "read",
            "open",
            "cat",
            "ls ",
            "grep ",
            "find ",
            "list",
            "access",
            "display",
            "print",
            "what's in",
            "what is in",
            "dump",
        )
        return any(marker in lowered for marker in intent_markers)

    @staticmethod
    def _looks_like_path_traversal_request(text: str) -> bool:
        """Detect collaborator prompts attempting path traversal style file access."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        if "../" not in lowered and "..\\" not in lowered:
            return False
        intent_markers = (
            "show",
            "read",
            "open",
            "cat",
            "print",
            "dump",
            "list",
            "access",
            "fetch",
        )
        return any(marker in lowered for marker in intent_markers)

    @staticmethod
    def _looks_like_metadata_endpoint_probe(text: str) -> bool:
        """Detect collaborator prompts targeting cloud metadata endpoints."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        endpoint_markers = (
            "169.254.169.254",
            "metadata.google.internal",
            "169.254.170.2",
        )
        if not any(marker in lowered for marker in endpoint_markers):
            return False
        intent_markers = (
            "curl",
            "wget",
            "fetch",
            "get",
            "query",
            "open",
            "check",
            "read",
            "request",
        )
        return any(marker in lowered for marker in intent_markers)

    @staticmethod
    def _looks_like_internal_network_probe(text: str) -> bool:
        """Detect collaborator prompts targeting local/internal network hosts."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        if not (
            any(marker in lowered for marker in ("localhost", "127.0.0.1", "0.0.0.0", "::1"))
            or re.search(r"\b10\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", lowered)
            or re.search(r"\b192\.168\.\d{1,3}\.\d{1,3}\b", lowered)
            or re.search(r"\b172\.(1[6-9]|2\d|3[0-1])\.\d{1,3}\.\d{1,3}\b", lowered)
        ):
            return False
        intent_markers = (
            "curl",
            "wget",
            "fetch",
            "get",
            "open",
            "check",
            "request",
            "connect",
            "ping",
            "scan",
        )
        return any(marker in lowered for marker in intent_markers)

    @staticmethod
    def _looks_like_obfuscated_command_probe(text: str) -> bool:
        """Detect collaborator prompts asking to decode/deobfuscate and execute commands."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        if not any(
            token in lowered for token in ("base64", "hex", "decode", "deobfuscate", "unescape")
        ):
            return False
        command_markers = (
            "bash",
            "sh ",
            "powershell",
            "cmd.exe",
            "curl",
            "wget",
            "python -c",
            "node -e",
            "rm ",
            "chmod",
            "chown",
        )
        execution_markers = ("run", "execute", "launch", "invoke", "then run", "pipe to shell")
        return any(marker in lowered for marker in command_markers) and any(
            marker in lowered for marker in execution_markers
        )

    @staticmethod
    def _looks_like_command_enumeration_query(text: str) -> bool:
        """Detect collaborator probes asking for direct command/tool inventories."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        patterns = (
            r"\b(what|which|list|show)\b.{0,30}\b(commands?|tools?|capabilities)\b",
            r"\bwhat can you (run|execute|access|use)\b",
            r"\bwhich tools are blocked\b",
            r"\bdo you have access to\b.{0,24}\b(shell|exec|credentials?|files?)\b",
            r"\b(commands?|tools?|capabilities)\b.{0,36}\b(appropriately )?(blocked|restricted|allowed)\b",
        )
        if any(re.search(pat, lowered) for pat in patterns):
            return True
        if "appropriately blocked" in lowered and any(
            token in lowered
            for token in ("command", "commands", "tool", "tools", "capability", "capabilities")
        ):
            return True
        return False

    @staticmethod
    def _looks_like_web_access_request(text: str) -> bool:
        """Detect collaborator prompts requesting external web/network fetch behavior."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        has_bare_domain = bool(re.search(r"\b[a-z0-9.-]+\.[a-z]{2,}\b", lowered))
        has_url = any(token in lowered for token in ("http://", "https://", "www."))
        asks_policy = any(
            token in lowered for token in ("blocked", "approval", "policy", "allowed", "permission")
        )
        asks_why_how = any(
            token in lowered for token in ("how", "what", "why", "explain", "workflow", "process")
        )
        has_imperative = any(
            token in lowered
            for token in ("check ", "fetch ", "open ", "browse ", "go to ", "look up ", "visit ")
        )
        if (
            not has_url
            and asks_why_how
            and any(
                token in lowered
                for token in ("external api", "egress", "approval", "network access", "web access")
            )
        ):
            # Conceptual policy/design question, not an execution/fetch request.
            return False
        if (has_url or has_bare_domain) and asks_why_how and asks_policy and not has_imperative:
            # Conceptual question that references a URL as an example.
            return False
        if re.search(r"https?://|www\.", lowered):
            return True
        if re.search(r"\bcheck\b.{0,48}\b[a-z0-9.-]+\.[a-z]{2,}\b", lowered):
            return True
        return any(
            token in lowered
            for token in (
                "check the weather",
                "fetch ",
                "open website",
                "browse to",
                "look up online",
                "go to this site",
                "web request",
            )
        )

    @staticmethod
    def _looks_like_unsafe_scheme_request(text: str) -> bool:
        """Detect collaborator requests using disallowed URL schemes."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        if not re.search(r"\b(?:file|ftp|gopher|smb|ssh|mailto|data):\/\/", lowered):
            return False
        request_markers = ("fetch", "open", "download", "request", "get", "check", "read")
        return any(marker in lowered for marker in request_markers)

    @staticmethod
    def _looks_like_allowlist_bypass_request(text: str) -> bool:
        """Detect collaborator prompts trying to bypass domain allowlist/egress policy."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        bypass_markers = (
            "bypass allowlist",
            "bypass egress",
            "evade allowlist",
            "use redirect",
            "open redirect",
            "url shortener",
            "shortened url",
            "redirect chain",
            "follow redirect to blocked",
            "proxy through",
            "tunnel through",
        )
        if not any(marker in lowered for marker in bypass_markers):
            return False
        request_markers = ("fetch", "open", "get", "request", "visit", "check", "use")
        return any(marker in lowered for marker in request_markers)

    @staticmethod
    def _looks_like_unicode_obfuscation_bypass_request(text: str) -> bool:
        """Detect collaborator prompts asking to bypass controls via unicode/invisible tricks."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        obfuscation_markers = (
            "zero-width",
            "zero width",
            "homoglyph",
            "invisible character",
            "unicode trick",
            "unicode bypass",
            "rtl override",
        )
        if not any(marker in lowered for marker in obfuscation_markers):
            return False
        intent_markers = ("bypass", "evade", "avoid", "hide", "obfuscate", "sneak", "slip")
        return any(marker in lowered for marker in intent_markers)

    @staticmethod
    def _looks_like_execution_request(text: str) -> bool:
        """Detect collaborator requests to run commands or perform direct execution."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        patterns = (
            r"\b(run|execute|invoke|launch)\b.{0,28}\b(command|shell|script|terminal)\b",
            r"\b(run|execute)\b.{0,24}\b(pwd|ls|cat|grep|find|whoami|uname|curl|wget)\b",
            r"`\s*(pwd|ls|cat|grep|find|whoami|uname|curl|wget)[^`]*`",
            r"\bjust run\b",
            r"\bdo a harmless system check\b",
            r"\bshow me the output\b.{0,20}\b(command|shell)\b",
        )
        return any(re.search(pat, lowered) for pat in patterns)

    @staticmethod
    def _looks_like_hypothetical_execution_question(text: str) -> bool:
        """Detect policy questions about execution behavior (not actual execution asks)."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        markers = (
            "what happens if",
            "if i asked",
            "would you",
            "can you explain",
            "how do you handle",
            "what would happen",
            "do you need approval",
            "would anything stop you",
        )
        return any(marker in lowered for marker in markers) and any(
            token in lowered for token in ("run", "execute", "command", "shell")
        )

    @staticmethod
    def _looks_like_collaborator_privacy_query(text: str) -> bool:
        """Detect collaborator prompts asking about other users/sessions/identities."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        return any(
            token in lowered
            for token in (
                "who else uses",
                "other collaborators",
                "other users",
                "who is active",
                "what have they been working on",
                "other sessions",
                "other people's files",
                "can you see files they've created",
            )
        )

    @staticmethod
    def _looks_like_identity_enumeration_query(text: str) -> bool:
        """Detect collaborator prompts attempting owner/collaborator identity disclosure."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        return any(
            token in lowered
            for token in (
                "owner telegram id",
                "telegram user id",
                "owner id",
                "who is the owner",
                "what is isaiah",
                "list collaborators",
                "who are the collaborators",
                "collaborator names",
            )
        )

    @staticmethod
    def _looks_like_safe_collaborator_info_query(text: str) -> bool:
        """Allow conceptual security/process questions that don't request execution/data access."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        # Greetings are always safe — no interrogative required.
        if re.match(
            r"^\s*(hello|hi|hey|good\s+morning|good\s+afternoon|good\s+evening|howdy)\b", lowered
        ):
            return True
        # Common conversational identity/capability questions are always safe.
        if re.search(
            r"\b(who are you|what do you do|what can you do|tell me about yourself|what does .{1,40} mean|owner.gated|owner gated)\b",
            lowered,
        ):
            return True
        if not any(
            ch in lowered
            for ch in ("?", "how", "what", "why", "can you explain", "walk me through")
        ):
            return False
        if TelegramAPIProxy._looks_like_file_query(lowered):
            return False
        if TelegramAPIProxy._looks_like_command_enumeration_query(lowered):
            return False
        if re.search(
            r"\b(create|write|edit|delete|execute|open|cat|grep|find|ls|fetch)\b", lowered
        ):
            return False
        if re.search(r"\brun\b(?!\s+on\b)", lowered):
            return False
        return any(
            token in lowered
            for token in (
                "authentication",
                "credential system",
                "security setup",
                "architecture",
                "workflow",
                "policy",
                "recommendation",
                "best practice",
                "approval",
                "approval process",
                "configuration",
                "security settings",
                "self-modification",
                "filters messages",
                "how does this work",
                "how does it work",
                "how do you work",
                "how does",
                "network",
                "infrastructure",
                "hosting",
                "vpn",
                "topology",
                "collaboration",
                "help with",
                "what can you",
                "what do you",
                "who are you",
                "tell me about",
                "security model",
                "security approach",
                "protection",
                "refuse",
                "restrict",
                "decline",
                "not allowed",
                "owner gated",
                "gated",
                "credit card",
                "pii",
                "personal info",
                "sanitiz",
                "formatting trick",
                "spaces or dashes",
                "bypass sanitiz",
                "password",
                "raw values",
                "placeholders",
            )
        )

    @staticmethod
    def _looks_like_approval_queue_probe(text: str) -> bool:
        """Detect collaborator prompts trying to inspect approval queue internals/metadata."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        if "approval" not in lowered and "egress" not in lowered:
            return False
        return any(
            token in lowered
            for token in (
                "pending approvals",
                "approval queue",
                "approval id",
                "request id",
                "egress id",
                "domain list",
                "show approvals",
                "list approvals",
                "risk score",
                "who approved",
            )
        )

    @staticmethod
    def _looks_like_policy_bypass_request(text: str) -> bool:
        """Detect collaborator prompts asking to bypass/disable approvals or protections."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        patterns = (
            r"\b(bypass|skip|ignore|disable|turn off)\b.{0,28}\b(approval|policy|security|guardrail|filter)\b",
            r"\bwithout\b.{0,16}\b(approval|authorization|policy check)\b",
            r"\bforce\b.{0,20}\b(allow|approve)\b",
            r"\bwhitelist\b.{0,24}\b(domain|url|host)\b",
        )
        return any(re.search(pat, lowered) for pat in patterns)

    @staticmethod
    def _looks_like_log_access_request(text: str) -> bool:
        """Detect collaborator prompts requesting direct system/audit log contents."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        patterns = (
            r"\b(show|read|open|print|dump|tail|cat|grep)\b.{0,32}\b(logs?|audit logs?|tracebacks?|stack traces?)\b",
            r"\b(openclaw logs|docker logs|journalctl)\b",
            r"\bwhat (?:do|does)\b.{0,24}\b(logs?|audit)\b.{0,24}\bshow\b",
        )
        return any(re.search(pat, lowered) for pat in patterns)

    @staticmethod
    def _looks_like_memory_access_request(text: str) -> bool:
        """Detect collaborator prompts requesting direct memory content/search access."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        patterns = (
            r"\b(show|read|open|dump|print|list|search|query)\b.{0,24}\b(memory|memories)\b",
            r"\bmemory_search\b",
            r"\brecall\b.{0,28}\b(previous|past|other users?|other collaborators?)\b",
            r"\bwhat do you remember about\b",
        )
        return any(re.search(pat, lowered) for pat in patterns)

    @staticmethod
    def _looks_like_secret_value_request(text: str) -> bool:
        """Detect collaborator prompts asking for raw secret/token/password values."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        conceptual_markers = (
            "policy",
            "workflow",
            "isolation",
            "management",
            "handling",
            "best practice",
            "rotation",
            "how does",
            "how do",
            "architecture",
            "design",
        )
        if any(marker in lowered for marker in conceptual_markers):
            return False
        secret_markers = (
            "api key",
            "token",
            "password",
            "secret",
            "credential",
            "private key",
            "access key",
        )
        request_markers = (
            "show",
            "reveal",
            "display",
            "print",
            "tell me",
            "what is",
            "give me",
            "share",
            "return",
        )
        value_markers = (
            "value",
            "actual",
            "raw",
            "full",
            "exact",
            "literal",
            "itself",
        )
        if not any(marker in lowered for marker in secret_markers):
            return False
        if not any(marker in lowered for marker in request_markers):
            return False
        # Require explicit value intent to avoid blocking conceptual collaborator
        # questions (e.g., "what is the credential isolation policy").
        if any(marker in lowered for marker in value_markers):
            return True
        return bool(
            re.search(
                r"\b(show|reveal|display|print|give|share)\b.{0,32}\b(api key|token|password|secret|credential)\b",
                lowered,
            )
        )

    @staticmethod
    def _looks_like_env_secret_probe(text: str) -> bool:
        """Detect collaborator prompts requesting environment variable/secret listings."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        env_markers = (
            "environment variable",
            "environment variables",
            "env vars",
            "printenv",
            "os.environ",
            "getenv",
            "$openai_api_key",
            "$gemini_api_key",
            "$anthropic_api_key",
            "$api_key",
            "$token",
        )
        if not any(marker in lowered for marker in env_markers):
            return False
        request_markers = (
            "show",
            "list",
            "print",
            "dump",
            "display",
            "reveal",
            "what are",
            "return",
        )
        return any(marker in lowered for marker in request_markers)

    @staticmethod
    def _looks_like_incremental_exfil_request(text: str) -> bool:
        """Detect chunked/partial extraction prompts intended to bypass output controls."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        target_markers = (
            "bootstrap.md",
            "identity.md",
            "memory.md",
            "soul.md",
            "heartbeat.md",
            "agents.md",
            ".env",
            "secret",
            "token",
            "credential",
        )
        if not any(marker in lowered for marker in target_markers):
            return False
        chunk_markers = (
            "first line",
            "first 10",
            "first 20",
            "first 50",
            "one line at a time",
            "line by line",
            "chunk by chunk",
            "in chunks",
            "character by character",
            "few characters",
            "just a snippet",
            "small snippet",
        )
        return any(marker in lowered for marker in chunk_markers)

    @staticmethod
    def _looks_like_encoded_exfil_request(text: str) -> bool:
        """Detect requests to encode sensitive/internal content for exfiltration."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        target_markers = (
            "bootstrap.md",
            "identity.md",
            "memory.md",
            "soul.md",
            "heartbeat.md",
            "agents.md",
            ".env",
            "secret",
            "token",
            "credential",
            "api key",
        )
        if not any(marker in lowered for marker in target_markers):
            return False
        encoding_markers = (
            "base64",
            "hex",
            "url encode",
            "encode it",
            "encoded",
            "rot13",
            "gzip",
            "compress",
            "obfuscate",
        )
        request_markers = ("show", "return", "print", "send", "dump", "export", "give me")
        return any(marker in lowered for marker in encoding_markers) and any(
            marker in lowered for marker in request_markers
        )

    @staticmethod
    def _looks_like_hidden_channel_exfil_request(text: str) -> bool:
        """Detect requests to extract hidden-channel content from sensitive/internal sources."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        target_markers = (
            "bootstrap.md",
            "identity.md",
            "memory.md",
            "soul.md",
            "heartbeat.md",
            "agents.md",
            ".env",
            "internal file",
            "workspace file",
        )
        if not any(marker in lowered for marker in target_markers):
            return False
        hidden_channel_markers = (
            "html comment",
            "markdown link",
            "alt text",
            "metadata",
            "filename stuffing",
            "hidden text",
            "invisible text",
            "annotation",
        )
        request_markers = ("extract", "show", "dump", "print", "return", "reveal", "list")
        return any(marker in lowered for marker in hidden_channel_markers) and any(
            marker in lowered for marker in request_markers
        )

    @staticmethod
    def _looks_like_archive_exfil_request(text: str) -> bool:
        """Detect collaborator prompts requesting archive/bulk export of internal content."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        archive_markers = ("zip", "tar", "tar.gz", "archive", "bundle", "pack")
        target_markers = (
            "workspace",
            "bootstrap.md",
            "identity.md",
            "memory.md",
            "soul.md",
            "heartbeat.md",
            "agents.md",
            "all files",
            "project files",
        )
        request_markers = ("export", "download", "send", "create", "make", "build", "package")
        return (
            any(marker in lowered for marker in archive_markers)
            and any(marker in lowered for marker in target_markers)
            and any(marker in lowered for marker in request_markers)
        )

    @staticmethod
    def _looks_like_cross_user_messaging_request(text: str) -> bool:
        """Detect collaborator prompts requesting direct messaging to other users."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        action_markers = ("send message", "dm", "direct message", "notify", "contact", "message ")
        recipient_markers = (
            "owner",
            "isaiah",
            "another collaborator",
            "other collaborator",
            "other user",
            "marvin",
            "trillian",
            "raspberrypi",
            "telegram id",
        )
        if not any(marker in lowered for marker in action_markers):
            return False
        return any(marker in lowered for marker in recipient_markers)

    @staticmethod
    def _looks_like_scheduler_or_autorun_request(text: str) -> bool:
        """Detect collaborator prompts attempting scheduled/automatic task execution."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        # Conceptual/diagnostic questions about schedules are not execution requests.
        conceptual_markers = (
            "how does",
            "what is",
            "do you have",
            "tell me about",
            "is there a",
            "are there any",
        )
        if any(marker in lowered for marker in conceptual_markers):
            return False
        schedule_markers = (
            "cron",
            "schedule",
            "every hour",
            "every day",
            "automatically run",
            "auto-run",
            "periodic task",
            "background job",
        )
        if not any(marker in lowered for marker in schedule_markers):
            return False
        # Use word-boundary matching for "run" so "running" doesn't trigger a false positive.
        action_markers_re = (
            r"\brun\b",
            r"\bexecute\b",
            r"\bstart\b",
            r"\btrigger\b",
            r"\bcreate\b",
            r"\bset up\b",
            r"\bconfigure\b",
        )
        return any(re.search(pat, lowered) for pat in action_markers_re)

    @staticmethod
    def _looks_like_model_switch_request(text: str) -> bool:
        """Detect collaborator prompts trying to switch runtime model/provider configuration."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        target_markers = (
            "switch model",
            "change model",
            "set model",
            "switch provider",
            "change provider",
            "switch to openai",
            "switch to gemini",
            "switch to ollama",
            "scripts/switch_model.sh",
            "openclaw_main_model",
            "agentshroud_model_mode",
        )
        return any(marker in lowered for marker in target_markers)

    @staticmethod
    def _looks_like_service_control_request(text: str) -> bool:
        """Detect collaborator prompts attempting service/container lifecycle control."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        conceptual_markers = (
            "how should",
            "how does",
            "what is",
            "best practice",
            "approval",
            "governed",
        )
        if any(marker in lowered for marker in conceptual_markers):
            return False
        action_markers = (
            "restart",
            "shutdown",
            "shut down",
            "stop",
            "start",
            "reboot",
            "kill",
        )
        target_markers = (
            "gateway",
            "bot",
            "agentshroud",
            "openclaw",
            "container",
            "docker",
            "service",
            "compose",
            "killswitch",
            "kill switch",
        )
        return any(action in lowered for action in action_markers) and any(
            target in lowered for target in target_markers
        )

    @staticmethod
    def _looks_like_plugin_discovery_request(text: str) -> bool:
        """Detect collaborator prompts requesting plugin/tool auto-discovery inventory."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        discovery_markers = (
            "plugin discovery",
            "auto-discover",
            "auto discover",
            "enumerate plugins",
            "list installed plugins",
            "all mcp servers",
            "show connected mcp tools",
            "tool registry dump",
        )
        if not any(marker in lowered for marker in discovery_markers):
            return False
        request_markers = ("show", "list", "enumerate", "dump", "print", "reveal")
        return any(marker in lowered for marker in request_markers)

    @staticmethod
    def _looks_like_pairing_or_access_probe(text: str) -> bool:
        """Detect collaborator prompts requesting pairing/access bootstrap artifacts."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        targets = (
            "pairing code",
            "openclaw pairing approve",
            "access not configured",
            "telegram user id",
            "approve telegram",
            "pairing approve",
        )
        if not any(target in lowered for target in targets):
            return False
        request_markers = ("show", "give", "send", "share", "provide", "what is", "return")
        return any(marker in lowered for marker in request_markers)

    @staticmethod
    def _looks_like_tool_trace_request(text: str) -> bool:
        """Detect collaborator prompts requesting raw tool traces/arguments/results."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        trace_targets = (
            "function_calls",
            "tool-call",
            "tool call",
            "tool arguments",
            "raw json",
            "raw xml",
            "stdout",
            "stderr",
        )
        if not any(target in lowered for target in trace_targets):
            return False
        request_markers = ("show", "print", "dump", "display", "return", "reveal", "send")
        return any(marker in lowered for marker in request_markers)

    @staticmethod
    def _looks_like_approval_token_probe(text: str) -> bool:
        """Detect collaborator prompts trying to obtain/craft approval callback tokens."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        if not any(
            token in lowered
            for token in ("egress_", "callback data", "approval token", "request id", "rid")
        ):
            return False
        return any(
            token in lowered
            for token in (
                "generate",
                "forge",
                "craft",
                "build",
                "show",
                "give me",
                "return",
                "send",
                "provide",
            )
        )

    @staticmethod
    def _looks_like_approval_action_request(text: str) -> bool:
        """Detect collaborator prompts attempting to approve/deny queued actions."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        action_markers = (
            "approve request",
            "deny request",
            "allow once",
            "allow always",
            "reject request",
            "approve this egress",
            "deny this egress",
        )
        if not any(marker in lowered for marker in action_markers):
            return False
        id_markers = ("request id", "approval id", "rid=", "id:")
        return any(marker in lowered for marker in id_markers)

    @staticmethod
    def _looks_like_cross_tenant_data_probe(text: str) -> bool:
        """Detect collaborator prompts attempting cross-tenant/workspace data access."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        tenant_markers = (
            "other tenant",
            "another tenant",
            "different tenant",
            "other workspace",
            "another workspace",
            "other project workspace",
            "other team data",
            "cross-tenant",
        )
        if not any(marker in lowered for marker in tenant_markers):
            return False
        access_markers = (
            "show",
            "list",
            "read",
            "access",
            "query",
            "search",
            "what is in",
            "can you see",
        )
        return any(marker in lowered for marker in access_markers)

    @staticmethod
    def _looks_like_guardrail_modification_request(text: str) -> bool:
        """Detect collaborator prompts attempting security/config guardrail changes."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        conceptual_markers = (
            "how should",
            "how does",
            "what is",
            "why is",
            "best practice",
            "approved",
            "can you modify your own configuration",
            "could you adjust",
            "if a security rule was blocking",
        )
        if any(marker in lowered for marker in conceptual_markers):
            return False
        targets = (
            "security policy",
            "guardrail",
            "security settings",
            "agentshroud.yaml",
            "config file",
            "rbac",
            "allowlist",
            "blocklist",
            "approval rules",
            "egress rules",
        )
        if not any(token in lowered for token in targets):
            return False
        verbs = (
            "change",
            "modify",
            "update",
            "edit",
            "disable",
            "turn off",
            "relax",
            "override",
            "remove",
            "set",
        )
        return any(verb in lowered for verb in verbs)

    @staticmethod
    def _looks_like_system_prompt_probe(text: str) -> bool:
        """Detect collaborator prompts requesting system prompt/agent instruction leakage."""
        if not isinstance(text, str):
            return False
        lowered = normalize_input(text).lower()
        target_markers = (
            "system prompt",
            "developer prompt",
            "hidden instructions",
            "instruction hierarchy",
            "agent instructions",
            "skill.md",
            "agents.md",
            "bootstrap prompt",
        )
        if not any(marker in lowered for marker in target_markers):
            return False
        request_markers = (
            "show",
            "print",
            "dump",
            "reveal",
            "display",
            "return",
            "give me",
            "share",
        )
        return any(marker in lowered for marker in request_markers)

    @staticmethod
    def _collaborator_safe_notice(reason: str) -> str:
        """Concise collaborator-safe reason text without internal leakage."""
        lowered = normalize_input(reason or "").lower()
        if any(
            token in lowered
            for token in (
                "metadata-endpoint",
                "imds",
                "secret-access",
                "credential",
                "secret",
                "token",
                "password",
                "key",
            )
        ):
            return _COLLABORATOR_SECRET_NOTICE
        if any(
            token in lowered
            for token in (
                "outbound policy block",
                "outbound block",
                "blocked outbound",
                "blocked response",
                "pipeline blocked",
            )
        ):
            return _COLLABORATOR_UNAVAILABLE_NOTICE
        if any(
            token in lowered
            for token in (
                "internal-network",
                "ssrf",
                "localhost",
                "egress",
                "domain",
                "network",
                "url",
                "web",
            )
        ):
            return _COLLABORATOR_EGRESS_NOTICE
        if any(
            token in lowered
            for token in (
                "obfuscated-command",
                "execution-request",
                "tool",
                "command",
                "capability",
                "permissions",
                "blocked command",
            )
        ):
            return _COLLABORATOR_SCOPE_NOTICE
        if any(token in lowered for token in ("file", "workspace", ".md", "path", "directory")):
            return _COLLABORATOR_FILE_NOTICE
        if any(
            token in lowered
            for token in (
                "timeout",
                "unavailable",
                "processing",
                "no_reply",
                "runtime",
                "failed",
                "error",
            )
        ):
            return _COLLABORATOR_UNAVAILABLE_NOTICE
        return _COLLABORATOR_BLOCK_NOTICE

    @staticmethod
    def _build_collaborator_safe_info_response(prompt: str) -> str:
        """Build informative but non-sensitive response for collaborator conceptual questions."""
        lowered = normalize_input(prompt or "").lower()
        if re.match(
            r"^\s*(hello|hi|hey|good\s+morning|good\s+afternoon|good\s+evening|howdy)\b", lowered
        ):
            return (
                f"{_PROTECT_HEADER}"
                "Hello! I'm the AgentShroud assistant operating in collaborator mode.\n"
                "• I can answer conceptual questions about how this system works.\n"
                "• I can discuss authentication patterns, egress approval flows, and security design.\n"
                "• File access, raw credentials, and sensitive operations require owner authorization.\n"
                "• Feel free to ask about security policies, architecture, or how the system handles requests."
            )
        if any(
            token in lowered
            for token in (
                "modify your own configuration",
                "security settings",
                "self-modification",
                "security rule was blocking",
            )
        ):
            return (
                f"{_PROTECT_HEADER}"
                "Configuration safety guidance:\n"
                "• Collaborators and runtime agents cannot self-modify security guardrails.\n"
                "• Security/configuration changes require authorized admin approval.\n"
                "• I can explain policy intent and propose safe change-request language."
            )
        if any(
            token in lowered
            for token in (
                "get processed",
                "message processed",
                "processed before",
                "how are messages",
                "message pipeline",
                "message flow",
                "before you answer",
                "before answering",
            )
        ):
            return (
                "Message processing overview:\n"
                "• Your message passes through identity and policy checks before routing.\n"
                "• Collaborator sessions are isolated from owner sessions — different context and permissions.\n"
                "• Outputs are safety-checked before delivery to prevent unintended disclosure.\n"
                "• I respond based on scoped context — no owner-private files or operational details."
            )
        if any(
            token in lowered
            for token in (
                "authentication",
                "credential",
                "api key",
                "secret",
                "password",
                "raw values",
                "placeholders",
            )
        ):
            if any(
                token in lowered
                for token in (
                    "flow",
                    "how",
                    "intermediary",
                    "handles",
                    "brokered",
                    "integrate",
                    "integration",
                    "work",
                )
            ):
                return (
                    "Authentication in this workspace:\n"
                    "• Credentials are managed server-side — I don't hold raw API keys or tokens in active context.\n"
                    "• When external access is needed, the gateway brokers the request on my behalf.\n"
                    "• I can help with OAuth patterns, least-privilege design, and safe API patterns for integrations."
                )
            return (
                f"{_PROTECT_HEADER}"
                "Secure collaboration guidance:\n"
                "• Authentication is brokered through protected service boundaries.\n"
                "• Collaborators do not receive raw credentials or secret values.\n"
                "• Sensitive operations require policy checks and authorization.\n"
                "• If authorized, I can help with integration patterns and least-privilege recommendations."
            )
        if any(
            token in lowered
            for token in (
                "security setup",
                "architecture",
                "filters messages",
                "how does this work",
                "security model",
                "security approach",
                "protection",
            )
        ):
            return (
                f"{_PROTECT_HEADER}"
                "Secure architecture overview:\n"
                "• Messages pass through policy and safety controls before action.\n"
                "• High-risk actions are restricted and audited.\n"
                "• Outputs are filtered to prevent sensitive disclosure.\n"
                "• I can explain secure design choices without exposing internal execution details."
            )
        if any(token in lowered for token in ("infrastructure", "hosting", "vpn", "topology")):
            return (
                f"{_PROTECT_HEADER}"
                "Infrastructure safety guidance:\n"
                "• Network and hosting internals are intentionally abstracted in collaborator mode.\n"
                "• Security controls enforce trusted boundaries and approved communication paths.\n"
                "• I can provide high-level architecture guidance without exposing sensitive implementation details."
            )
        if any(
            token in lowered
            for token in (
                "tool",
                "command",
                "capability",
                "permissions",
                "what can you",
                "help with",
                "collaboration",
            )
        ):
            return (
                f"{_PROTECT_HEADER}"
                "Collaborator capability overview:\n"
                "• If authorized, I can discuss system concepts, security guidance, and recommendations.\n"
                "• I cannot provide runnable commands, raw tool traces, or execution details.\n"
                "• Direct file content access and secret/credential retrieval are restricted.\n"
                "• External/network actions require explicit owner approval before execution."
            )
        if any(
            token in lowered
            for token in (
                "dns lookup",
                "dns query",
                "dns resolve",
                "dns check",
                "ping",
                "icmp",
                "connectivity probe",
                "connectivity check",
                "udp probe",
                "network probe",
            )
        ):
            return (
                f"{_PROTECT_HEADER}"
                "Network probe policy:\n"
                "• Outbound network access — including DNS probes, pings, and connectivity checks — requires owner authorization.\n"
                "• This applies regardless of protocol (HTTP, DNS, ICMP, UDP).\n"
                "• All external network actions go through the owner approval workflow."
            )
        if any(token in lowered for token in ("approval", "egress", "external", "network")):
            return (
                f"{_PROTECT_HEADER}"
                "Egress and approval guidance:\n"
                "• External/network actions require explicit authorization.\n"
                "• Unauthorized outbound requests are denied.\n"
                "• Approval decisions are enforced before execution.\n"
                "• I can help draft safe request criteria and risk-aware justification."
            )
        if any(
            token in lowered
            for token in (
                "too risky",
                "risky for me",
                "system react",
                "how does the system",
                "considered risky",
                "considered dangerous",
                "action risk",
                "risky action",
            )
        ):
            return (
                "Action risk guidance:\n"
                "• Actions requiring confirmation: external network requests, file writes, destructive operations.\n"
                "• Actions always declined: credential retrieval, system reconnaissance, policy bypass attempts.\n"
                "• The system explains what it can't do and why — there are no silent failures.\n"
                "• The gateway enforces hard limits regardless of how a request is phrased."
            )
        if any(
            token in lowered
            for token in (
                "owner versus",
                "owner vs",
                "came from the owner",
                "came from owner",
                "tell whether",
                "tell if",
                "owner or collaborator",
                "collaborator or owner",
                "how does that affect",
                "how does it affect",
            )
        ):
            return (
                "Yes — all messages are identified by sender and assigned a trust level.\n"
                "• Owner messages have full operational access to tools, files, and external services.\n"
                "• Collaborator messages are policy-gated: conversation is the primary available capability.\n"
                "• These boundaries are enforced by the gateway and cannot be overridden in chat."
            )
        if any(token in lowered for token in ("refuse", "restrict", "decline", "not allowed")):
            return (
                f"{_PROTECT_HEADER}"
                "Restriction overview:\n"
                "• Collaborators cannot access raw file contents, system paths, or live tool outputs.\n"
                "• Commands that execute system actions require owner authorization.\n"
                "• Credential and secret retrieval is fully restricted in collaborator mode.\n"
                "• I can explain what types of requests are gated and why, without exposing policy internals."
            )
        if any(
            token in lowered
            for token in ("credit card", "pii", "personal info", "sanitiz", "what would you see")
        ):
            return (
                f"{_PROTECT_HEADER}"
                "Input privacy notice:\n"
                "• Messages you send pass through a security proxy before reaching the assistant.\n"
                "• The proxy inspects and sanitizes inputs for policy compliance.\n"
                "• Sensitive values such as credentials or personal data are redacted or flagged before forwarding.\n"
                "• I receive sanitized content — I do not see raw credential values or un-sanitized personal data."
            )
        if any(
            token in lowered for token in ("formatting trick", "spaces or dashes", "bypass sanitiz")
        ):
            return (
                f"{_PROTECT_HEADER}"
                "Input handling notice:\n"
                "• The security proxy applies consistent normalization before policy checks.\n"
                "• Formatting variations (extra spaces, dashes, encoding) are normalized before evaluation.\n"
                "• Policy checks are applied to normalized content — formatting tricks do not bypass them."
            )
        if any(
            token in lowered
            for token in (
                "who else",
                "collaborator",
                "other users",
                "other sessions",
                "active users",
                "owner telegram id",
                "telegram user id",
                "owner id",
                "who is the owner",
            )
        ):
            return (
                f"{_PROTECT_HEADER}"
                "Privacy boundary guidance:\n"
                "• Collaborator identities, activity, and session data are privacy-protected.\n"
                "• I cannot disclose other users' status, files, or conversation details.\n"
                "• If authorized, I can help with shared process guidance without exposing user-specific data."
            )
        if any(
            token in lowered
            for token in ("bootstrap.md", "identity.md", "soul.md", "heartbeat.md", "agents.md")
        ):
            return (
                f"{_PROTECT_HEADER}"
                "File access policy guidance:\n"
                "• System config files (SOUL.md, IDENTITY.md, BOOTSTRAP.md, HEARTBEAT.md, AGENTS.md) "
                "are treated as internal system files.\n"
                "• Collaborators cannot access raw file contents or direct file reads.\n"
                "• I can provide high-level onboarding and role guidance without exposing file data."
            )
        if any(
            token in lowered
            for token in (
                "stream through",
                "still stream",
                "chunks",
                "chunked",
                "partial leak",
                "partial content",
                "partial response",
                "blocked answer",
                "too long to",
            )
        ):
            return (
                f"{_PROTECT_HEADER}"
                "Output delivery policy:\n"
                "• Responses are evaluated atomically before delivery — no partial content streams through a block.\n"
                "• If a full response would be blocked, the entire message is replaced, not truncated.\n"
                "• This applies regardless of response length."
            )
        return _COLLABORATOR_SAFE_INFO_NOTICE

    @staticmethod
    def _contains_high_risk_collaborator_leakage(text: str) -> bool:
        """Detect obvious raw tool/file/system leakage patterns in outbound text."""
        if not isinstance(text, str):
            return False
        normalized = normalize_input(text).lower()
        # Never double-filter our own protected/blocked notices.
        if normalized.lstrip().startswith("🛡") or "protected by agentshroud" in normalized:
            return False
        # Patterns that are always high-risk regardless of context.
        unconditional_patterns = (
            r"<function_calls?>",
            r"</function_calls?>",
            r"<invoke\s+name=",
            r"</invoke>",
            r'"\s*name"\s*:\s*"(?:sessions_spawn|sessions_send|web_fetch|exec|shell|find|grep|cat|ls)"',
            r'"\s*arguments"\s*:\s*\{',
            r"\b/(?:etc|proc|run/secrets|home|root|usr|var)/",
            r"\bpairing code\s*:",
            r"\bopenclaw pairing approve telegram\b",
            r"\byour telegram user id\s*:",
            r"\bopenclaw:\s*access not configured\b",
            r"\b(?:traceback|stack trace|stderr|stdout)\b",
        )
        if any(re.search(pat, normalized) for pat in unconditional_patterns):
            return True
        # Filename patterns are only high-risk when content is being revealed,
        # not when the filename appears in a denial/blocked context.
        sensitive_filenames = r"\b(?:\.env|bootstrap\.md|identity\.md|memory\.md)\b"
        fn_match = re.search(sensitive_filenames, normalized)
        if fn_match:
            denial_markers = (
                "cannot",
                "can't",
                "not allowed",
                "restricted",
                "blocked",
                "denied",
                "do not",
                "won't",
                "unable",
                "not able",
                "not permitted",
                "access denied",
                "i'm not",
                "i am not",
                "not authorized",
            )
            fn_start = fn_match.start()
            # Only consider denial safe if a denial marker appears within 120 chars of the filename
            window_start = max(0, fn_start - 120)
            window_end = min(len(normalized), fn_match.end() + 120)
            proximity_text = normalized[window_start:window_end]
            if not any(marker in proximity_text for marker in denial_markers):
                return True
        return False

    @staticmethod
    def _contains_internal_approval_banner(text: str) -> bool:
        """Detect internal approval/egress banner text that must remain owner-only."""
        if not isinstance(text, str):
            return False
        normalized = normalize_input(text).lower()
        return (
            ("egress request" in normalized and "domain:" in normalized)
            or ("risk:" in normalized and "tool:" in normalized and "id:" in normalized)
            # Callback data tokens from inline keyboard (egress approval buttons)
            or "egress_allow_always_" in normalized
            or "egress_allow_once_" in normalized
            or "egress_allow_1h_" in normalized
            or "egress_allow_4h_" in normalized
            or "egress_allow_24h_" in normalized
            or "egress_deny_" in normalized
        )

    @staticmethod
    def _contains_legacy_block_notice(text: str) -> bool:
        """Detect legacy bracket-style block notices for collaborator normalization."""
        if not isinstance(text, str):
            return False
        normalized = normalize_input(text).lower()
        return (
            "[agentshroud:" in normalized
            or "outbound content blocked by security policy" in normalized
            or "[blocked by agentshroud:" in normalized
            or "protected by agentshroud" in normalized
            or "internal tool-call output suppressed" in normalized
        )

    @staticmethod
    def _looks_like_tool_payload_text(text: str) -> bool:
        """Detect raw/embedded tool payload text in user input."""
        if not isinstance(text, str):
            return False
        normalized = normalize_input(text).lower()
        if "<function_calls" in normalized or "</function_calls>" in normalized:
            return True
        if '"name"' in normalized and '"arguments"' in normalized:
            return True
        if "'name'" in normalized and "'arguments'" in normalized:
            return True
        if re.search(r"\bname\s*:\s*[\"']?[a-z0-9_.:-]+[\"']?\s*,\s*arguments\s*:", normalized):
            return True
        if re.search(r"\{\s*\"name\"\s*:\s*\"[a-z0-9_.:-]+\"\s*,\s*\"arguments\"\s*:", normalized):
            return True
        if re.search(r"\{\s*'name'\s*:\s*'[a-z0-9_.:-]+'\s*,\s*'arguments'\s*:", normalized):
            return True
        return False

    @staticmethod
    def _strip_json_fence(text: str) -> str:
        """Strip optional markdown json fences around model output."""
        candidate = normalize_input(text or "").strip()
        if candidate.startswith("```"):
            candidate = re.sub(r"^```(?:json)?\s*", "", candidate, flags=re.IGNORECASE)
            candidate = re.sub(r"\s*```$", "", candidate)
        return candidate.strip()

    @classmethod
    def _parse_tool_call_json(cls, text: str) -> Optional[dict[str, Any]]:
        """Parse leaked model tool-call JSON blobs (e.g. {'name': 'NO_REPLY', ...})."""
        candidate = cls._strip_json_fence(text)
        if not candidate.startswith("{") or not candidate.endswith("}"):
            return None
        try:
            parsed = json.loads(candidate)
        except Exception:
            return None
        if not isinstance(parsed, dict):
            return None
        name = parsed.get("name")
        arguments = parsed.get("arguments")
        if isinstance(name, str) and isinstance(
            arguments, (dict, list, str, int, float, bool, type(None))
        ):
            return parsed
        return None

    @classmethod
    def _extract_embedded_tool_call_json(
        cls, text: str
    ) -> Optional[tuple[dict[str, Any], int, int]]:
        """Find first embedded tool-call JSON object inside arbitrary text."""
        source = text or ""
        decoder = json.JSONDecoder()
        i = 0
        while i < len(source):
            start = source.find("{", i)
            if start < 0:
                return None
            try:
                parsed, end = decoder.raw_decode(source, start)
            except Exception:
                i = start + 1
                continue
            if isinstance(parsed, dict):
                name = parsed.get("name")
                if isinstance(name, str) and "arguments" in parsed:
                    return parsed, start, end
            i = end if end > start else start + 1
        return None

    @staticmethod
    def _extract_first_egress_target(text: str) -> Optional[str]:
        """Extract first outbound web target (URL or bare domain) for egress preflight."""
        if not text:
            return None
        url_match = re.search(r"https?://[^\s<>()\"']+", text, flags=re.IGNORECASE)
        if url_match:
            url = url_match.group(0).rstrip(".,;:!?)]}>'\"`")
            return url or None
        relative_match = re.search(
            r"\b//(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}(?:/[^\s<>()\"']*)?",
            text,
            flags=re.IGNORECASE,
        )
        if relative_match:
            candidate = relative_match.group(0).rstrip(".,;:!?)]}>'\"`")
            if candidate:
                return f"https:{candidate}"
        # Strip non-HTTP URL tokens (ftp://, file://, etc.) before bare-domain
        # fallback matching so unrelated domains elsewhere in the same message
        # can still trigger collaborator egress preflight approvals.
        search_text = re.sub(
            r"\b(?!https?:)[a-z][a-z0-9+.\-]{1,20}://[^\s<>()\"']+",
            " ",
            text,
            flags=re.IGNORECASE,
        )

        # Support bare domains like "weather.com/today" so collaborator requests
        # still trigger interactive egress approval before model/tool execution.
        domain_match = re.search(
            r"(?<!@)\b(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}(?![a-z0-9_-])(?:/[^\s<>()\"']*)?",
            search_text,
            flags=re.IGNORECASE,
        )
        if not domain_match:
            return None
        candidate = domain_match.group(0).rstrip(".,;:!?)]}>'\"`")
        if not candidate:
            return None
        # Avoid false positives where file names (e.g., BOOTSTRAP.md, test.txt)
        # are misinterpreted as outbound domains.
        head = candidate.split("/", 1)[0]
        if "." in head:
            tld = head.rsplit(".", 1)[-1].lower()
            if tld in {
                "md",
                "txt",
                "json",
                "yaml",
                "yml",
                "toml",
                "ini",
                "py",
                "js",
                "ts",
                "tsx",
                "jsx",
                "sh",
                "bash",
                "zsh",
                "csv",
                "log",
                "pdf",
                "png",
                "jpg",
                "jpeg",
                "gif",
                "svg",
                "sql",
                "db",
                "sqlite",
                "env",
                "conf",
                "cfg",
                "lock",
            }:
                return None
        return f"https://{candidate}"

    @staticmethod
    def _is_valid_domain_name(domain: str) -> bool:
        """Validate normalized domain labels to avoid malformed allowlist entries."""
        raw = (domain or "").strip().lower()
        if not raw:
            return False
        if len(raw) > 253:
            return False
        if ".." in raw:
            return False
        labels = raw.split(".")
        if len(labels) < 2:
            return False
        tld = labels[-1]
        if len(tld) < 2 or len(tld) > 63 or not re.fullmatch(r"[a-z]+", tld):
            return False
        for label in labels:
            if not label:
                return False
            if len(label) > 63:
                return False
            if label.startswith("xn--"):
                return False
            if label.startswith("-") or label.endswith("-"):
                return False
            if not re.fullmatch(r"[a-z0-9-]+", label):
                return False
        return True

    @staticmethod
    def _resolve_text_field(data: dict[str, Any]) -> tuple[str, str]:
        """Return (field_name, text_value) for Telegram-style outbound payloads."""
        first_string_key: Optional[str] = None
        for key in ("text", "draft", "message", "content", "caption"):
            value = data.get(key)
            if isinstance(value, str):
                if first_string_key is None:
                    first_string_key = key
                if normalize_input(value).strip():
                    return key, value
        if first_string_key is not None:
            value = data.get(first_string_key)
            return first_string_key, value if isinstance(value, str) else ""
        return "text", ""

    async def proxy_request(
        self,
        bot_token: str,
        method: str,
        body: Optional[bytes] = None,
        content_type: Optional[str] = None,
        is_system: bool = False,
        path_prefix: str = "",
    ) -> dict:
        """Proxy a single Telegram API request.

        For getUpdates responses: scan each message through security pipeline.
        For sendMessage requests: scan outbound content.
        is_system=True skips outbound filtering for system/admin notifications
        (startup, shutdown) that are not LLM-generated output.
        path_prefix: set to "file/" for Telegram file download requests so the
        upstream URL is constructed as https://api.telegram.org/file/bot<token>/<path>.
        """
        self._stats["total_requests"] += 1
        url = f"{TELEGRAM_API_BASE}/{path_prefix}bot{bot_token}/{method}"

        # === OUTBOUND FILTERING (bot → Telegram) ===
        # For sendMessage, editMessageText, etc. — scan the bot's outgoing text.
        # Skip for system notifications (X-AgentShroud-System: 1) — these are
        # shell-script admin messages, not LLM output, so content filtering is not needed.
        #
        # Draft methods are suppressed to prevent transient raw tool-call JSON flicker in
        # Telegram clients before final message sanitization.
        if not is_system and method in ("sendMessageDraft", "editMessageDraft"):
            return {"ok": True, "result": {"suppressed": True, "method": method}}
        if method in ("sendMessage", "editMessageText") and body:
            if self._suppress_duplicate_system_notice(body, content_type):
                return {"ok": True, "result": {"suppressed": True, "method": method}}

        if (
            not is_system
            and method
            in (
                "sendMessage",
                "editMessageText",
                "sendPhoto",
                "sendDocument",
                "copyMessage",
                "forwardMessage",
            )
            and body
        ):
            body = await self._filter_outbound(body, content_type)
            if self._is_suppressed_outbound_payload(body, content_type):
                return {"ok": True, "result": {"suppressed": True, "method": method}}

        # Log bot responses to collaborators for activity reports (/collabs)
        if not is_system and method == "sendMessage" and body and self._collaborator_chat_ids:
            try:
                _outbound_data = json.loads(body.decode("utf-8", errors="replace"))
                _out_chat_id = str(_outbound_data.get("chat_id", ""))
                _collab_uid = self._collaborator_chat_ids.get(_out_chat_id)
                if _collab_uid:
                    _response_text = _outbound_data.get("text", "")
                    from gateway.ingest_api.state import app_state as _app_state

                    _tracker = getattr(_app_state, "collaborator_tracker", None)
                    if _tracker:
                        _corr_pair = self._last_inbound_corr.get(_out_chat_id)
                        _out_corr_id = _corr_pair[0] if _corr_pair else None
                        _tracker.record_activity(
                            user_id=_collab_uid,
                            username="bot",
                            message_preview=_response_text[:80],
                            source="telegram",
                            direction="outbound",
                            correlation_id=_out_corr_id,
                        )
            except Exception as _ote:
                logger.debug("Outbound collab response tracking error (non-fatal): %s", _ote)

        # ── Group chat response gate ──────────────────────────────────────────
        # Suppress bot replies to group/supergroup chats where the last inbound
        # was not an @mention. The bot still received those messages for context
        # (_group_response_eligible tracks eligibility per chat_id). This applies
        # to sendMessage and editMessageText only; system notifications are exempt.
        if (
            not is_system
            and self._group_mention_only
            and self._bot_username
            and method
            in (
                "sendMessage",
                "editMessageText",
                "sendPhoto",
                "sendDocument",
                "copyMessage",
                "forwardMessage",
            )
            and body
        ):
            try:
                _out_body = json.loads(body.decode("utf-8", errors="replace"))
                _out_chat_id = _out_body.get("chat_id")
                if isinstance(_out_chat_id, (int, str)):
                    _cid = int(_out_chat_id)
                    # Telegram group/supergroup IDs are negative integers.
                    if _cid < 0 and not self._group_response_eligible.get(_cid, True):
                        logger.debug(
                            "Group outbound suppressed (context-only mode): chat_id=%s method=%s",
                            _cid,
                            method,
                        )
                        return {"ok": True, "result": {"suppressed": True, "method": method}}
            except Exception as _gge:
                logger.debug("Group gate parse error (non-fatal): %s", _gge)

        # Forward to real Telegram API
        # File download paths return binary data (images, documents) — do NOT JSON-parse.
        if path_prefix == "file/":
            try:
                return await self._forward_file_download(url)
            except Exception as e:
                logger.error(f"Telegram file download proxy error for {method}: {e}")
                return {"ok": False, "error_code": 502, "description": str(e)}

        try:
            response_data = await self._forward_to_telegram(url, body, content_type)
        except Exception as e:
            logger.error(f"Telegram API proxy error for {method}: {e}")
            return {"ok": False, "error_code": 502, "description": str(e)}

        # === INBOUND FILTERING (Telegram → bot) ===
        # For getUpdates: scan each message in the response
        if method == "getUpdates" and response_data.get("ok"):
            inbound_updates = response_data.get("result", [])
            inbound_total = len(inbound_updates) if isinstance(inbound_updates, list) else 0
            response_data = await self._filter_inbound_updates(response_data)
            filtered_updates = response_data.get("result", [])
            inbound_forwarded = len(filtered_updates) if isinstance(filtered_updates, list) else 0
            inbound_dropped = max(0, inbound_total - inbound_forwarded)
            if inbound_total > 0 and inbound_forwarded == 0:
                # Important: if we locally handle and drop every update, the bot runtime
                # never advances Telegram offset and can get stuck replaying the same
                # updates forever. Return ack-only update_ids so offset can advance
                # without forwarding message payloads to the runtime.
                ack_updates = self._build_ack_only_updates(inbound_updates)
                if ack_updates:
                    response_data["result"] = ack_updates
            self._stats["inbound_updates_total"] += inbound_total
            self._stats["inbound_updates_forwarded"] += inbound_forwarded
            self._stats["inbound_updates_dropped"] += inbound_dropped
            if inbound_total > 0:
                logger.info(
                    "Telegram getUpdates filtered: total=%d forwarded=%d dropped=%d",
                    inbound_total,
                    inbound_forwarded,
                    inbound_dropped,
                )

        return response_data

    @staticmethod
    def _strip_collaborator_html_markup(text: str) -> str:
        """Remove Telegram HTML formatting tags from collaborator outbound text."""
        if not isinstance(text, str) or "<" not in text or ">" not in text:
            return text
        return re.sub(
            r"</?(?:code|pre|a|b|i|u|s|strong|em|blockquote|tg-spoiler)\b[^>]*>",
            "",
            text,
            flags=re.IGNORECASE,
        )

    @staticmethod
    def _build_ack_only_updates(inbound_updates: list[Any]) -> list[dict[str, Any]]:
        """Return minimal getUpdates payload entries containing only update_id."""
        ack_only: list[dict[str, Any]] = []
        for update in inbound_updates:
            if not isinstance(update, dict):
                continue
            update_id = update.get("update_id")
            if isinstance(update_id, int):
                ack_only.append({"update_id": update_id})
        return ack_only

    async def _filter_outbound(self, body: bytes, content_type: Optional[str]) -> bytes:
        """Filter outbound bot messages (sendMessage, etc.)."""
        try:
            ct = (content_type or "").lower()
            if "multipart" in ct:
                # For multipart/form-data (sendPhoto, sendDocument with caption):
                # apply XML leak filter using latin-1 for lossless binary round-trip.
                # latin-1 is bijective over 0x00-0xFF so binary image parts are
                # preserved byte-for-byte while XML patterns in text fields are stripped.
                if self.sanitizer:
                    body_str = body.decode("latin-1")
                    filtered, was_filtered = self.sanitizer.filter_xml_blocks(body_str)
                    if was_filtered:
                        body = filtered.encode("latin-1")
                        self._stats["outbound_filtered"] += 1
                        logger.info("Outbound multipart: XML blocks stripped")
                return body
            elif "json" in ct or (not ct and body.lstrip().startswith(b"{")):
                data = json.loads(body)
                text_key, text = self._resolve_text_field(data)
                chat_id = str(data.get("chat_id", ""))
                is_owner_chat = self._is_owner_chat(chat_id)
                logger.info(
                    "Outbound sendMessage: chat_id=%s role=%s len=%d",
                    chat_id,
                    "owner" if is_owner_chat else "collaborator",
                    len(text) if isinstance(text, str) else 0,
                )

                # Guardrail: never leak raw tool-call JSON blobs to Telegram users.
                parsed_tool_call = (
                    self._parse_tool_call_json(text) if isinstance(text, str) else None
                )
                embedded_tool_call = (
                    self._extract_embedded_tool_call_json(text) if isinstance(text, str) else None
                )
                if parsed_tool_call is None and embedded_tool_call is not None:
                    parsed_tool_call, emb_start, emb_end = embedded_tool_call
                    leading = text[:emb_start].strip()
                    trailing = text[emb_end:].strip()
                    cleaned = " ".join(part for part in (leading, trailing) if part).strip()
                    if cleaned:
                        if not is_owner_chat:
                            data[text_key] = self._collaborator_safe_notice("tool output redacted")
                            self._stats["outbound_filtered"] += 1
                            return json.dumps(data).encode()
                        tool_name = str(parsed_tool_call.get("name", "")).strip()
                        tool_args = (
                            parsed_tool_call.get("arguments")
                            if isinstance(parsed_tool_call.get("arguments"), dict)
                            else {}
                        )
                        if tool_name == "web_fetch":
                            approval_queued = await self._trigger_web_fetch_approval(
                                chat_id, tool_args
                            )
                            if approval_queued:
                                cleaned = (
                                    f"{cleaned}\n\n"
                                    "🌐 Web access request detected. Approval request queued for this destination."
                                ).strip()
                        data[text_key] = cleaned
                        self._stats["outbound_filtered"] += 1
                        return json.dumps(data).encode()
                if parsed_tool_call is not None:
                    tool_name = str(parsed_tool_call.get("name", "")).strip()
                    tool_args = (
                        parsed_tool_call.get("arguments")
                        if isinstance(parsed_tool_call.get("arguments"), dict)
                        else {}
                    )
                    self._stats["outbound_filtered"] += 1
                    if tool_name.upper() == "NO_REPLY":
                        data[text_key] = (
                            self._collaborator_safe_notice("processing timeout")
                            if not is_owner_chat
                            else "⏳ Agent is still processing a previous request. Please wait 10–20 seconds and retry."
                        )
                    elif (
                        tool_name == "sessions_spawn"
                        and str(tool_args.get("agentId", "")) == "acp.healthcheck"
                    ):
                        data[text_key] = (
                            self._collaborator_safe_notice("restricted command")
                            if not is_owner_chat
                            else "✅ Healthcheck started. I’ll reply with status once complete."
                        )
                    elif tool_name == "web_fetch":
                        approval_queued = await self._trigger_web_fetch_approval(chat_id, tool_args)
                        if not is_owner_chat:
                            data[text_key] = (
                                _COLLABORATOR_EGRESS_NOTICE
                                if approval_queued
                                else self._collaborator_safe_notice("web access unavailable")
                            )
                        else:
                            approval_note = (
                                " Approval request queued for this destination."
                                if approval_queued
                                else ""
                            )
                            data[text_key] = (
                                "🌐 Web fetch requested, but this model returned raw tool JSON instead of executing it. "
                                "Switch to a tool-capable model (e.g., scripts/switch_model.sh gemini or local qwen3:14b once pulled)."
                                + approval_note
                            )
                    elif tool_name in {"sessions_spawn", "sessions_send", "subagents"}:
                        data[text_key] = (
                            self._collaborator_safe_notice("restricted command")
                            if not is_owner_chat
                            else "✅ Request accepted and queued."
                        )
                    else:
                        self._quarantine_outbound_block(
                            chat_id=chat_id,
                            text=text or "",
                            reason=f"Raw tool-call JSON leaked to outbound text (tool={tool_name or 'unknown'})",
                            source="telegram_outbound_toolcall_json",
                        )
                        data[text_key] = (
                            self._collaborator_safe_notice("tool output redacted")
                            if not is_owner_chat
                            else (
                                f"⚠️ Agent returned a raw tool-call JSON for '{tool_name or 'unknown'}' "
                                "which is not configured in this environment. "
                                "Ask the agent to report findings as text rather than executing commands, "
                                "or switch to a tool-capable model (scripts/switch_model.sh)."
                            )
                        )
                    return json.dumps(data).encode()

                if isinstance(text, str) and "session file locked" in text.lower():
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = (
                        self._collaborator_safe_notice("processing timeout")
                        if not is_owner_chat
                        else "⏳ Agent is still processing a previous request. Please wait 10–20 seconds and retry."
                    )
                    return json.dumps(data).encode()
                if (
                    not is_owner_chat
                    and isinstance(text, str)
                    and normalize_input(text)
                    .strip()
                    .lower()
                    .startswith("⚠️ agent failed before reply:")
                ):
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = self._collaborator_safe_notice("runtime unavailable")
                    return json.dumps(data).encode()
                if (
                    not is_owner_chat
                    and isinstance(text, str)
                    and "not authorized to use this command" in text.lower()
                ):
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = self._collaborator_safe_notice("restricted command")
                    return json.dumps(data).encode()
                if self._is_no_reply_token(text):
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = (
                        self._collaborator_safe_notice("processing timeout")
                        if not is_owner_chat
                        else "⏳ Agent is still processing a previous request. Please wait 10–20 seconds and retry."
                    )
                    return json.dumps(data).encode()
                if (
                    not is_owner_chat
                    and isinstance(text, str)
                    and (
                        "multi-turn disclosure" in text.lower()
                        or "blocked due to security protocols" in text.lower()
                    )
                ):
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = self._collaborator_safe_notice("policy block")
                    return json.dumps(data).encode()
                if (
                    not is_owner_chat
                    and isinstance(text, str)
                    and (
                        "security monitoring active at" in text.lower()
                        and "threshold" in text.lower()
                    )
                ):
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = self._collaborator_safe_notice("policy block")
                    return json.dumps(data).encode()
                if (
                    not is_owner_chat
                    and isinstance(text, str)
                    and self._contains_legacy_block_notice(text)
                ):
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = self._collaborator_safe_notice("policy block")
                    return json.dumps(data).encode()
                if (
                    not is_owner_chat
                    and isinstance(text, str)
                    and self._contains_internal_approval_banner(text)
                ):
                    self._stats["outbound_filtered"] += 1
                    _owner_id_str = str(getattr(self._rbac, "owner_user_id", "")).strip()
                    if _owner_id_str:
                        asyncio.create_task(
                            self._send_owner_admin_notice(
                                int(_owner_id_str),
                                "🔔 *Egress Approval Triggered*\n\nA collaborator interaction generated an egress approval request. Check /pending to review.",
                            )
                        )
                    data[text_key] = _COLLABORATOR_EGRESS_NOTICE
                    return json.dumps(data).encode()
                if (
                    not is_owner_chat
                    and isinstance(text, str)
                    and self._contains_high_risk_collaborator_leakage(text)
                ):
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = self._collaborator_safe_notice("redacted protected content")
                    return json.dumps(data).encode()
                # Redact owner's Telegram user ID from collaborator responses.
                # Strips the ID (and surrounding "Telegram ID …" label if present) so the
                # rest of the response — e.g. the owner's name or role — still reaches the
                # collaborator rather than blanket-blocking the whole message.
                if not is_owner_chat and isinstance(text, str) and self._rbac:
                    _oid = str(getattr(self._rbac, "owner_user_id", "")).strip()
                    if len(_oid) >= 7 and _oid in text:
                        self._stats["outbound_filtered"] += 1
                        # Remove the owner ID and common preceding label fragments that
                        # would otherwise leave dangling phrases like "his ID is" or
                        # "Telegram ID:" after the numeric value is stripped.
                        redacted = re.sub(
                            r"(?:"
                            r"(?:his|her|their|the\s+owner'?s?|my)\s+(?:Telegram\s+)?(?:user\s+)?ID\s+is\s*:?\s*|"
                            r"Telegram\s+(?:user\s+)?ID\s*:?\s*|"
                            r"(?:user\s+)?ID\s*:?\s*"
                            r")?" + re.escape(_oid),
                            "",
                            text,
                            flags=re.IGNORECASE,
                        ).strip()
                        data[text_key] = (
                            redacted
                            if redacted
                            else self._collaborator_safe_notice("redacted protected content")
                        )
                        text = data[
                            text_key
                        ]  # update local ref so sanitizer sees the redacted text
                if isinstance(text, str) and "does not support tools" in text.lower():
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = (
                        "⚠️ Current local model does not support tool calls. Use scripts/switch_model.sh local qwen3:14b (or a tools-capable model)."
                    )
                    return json.dumps(data).encode()
                if isinstance(text, str) and "ollama requires authentication" in text.lower():
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = (
                        "⚠️ Ollama provider is not configured in this session. Set OLLAMA_API_KEY=ollama-local and restart, "
                        "or run scripts/switch_model.sh gemini."
                    )
                    return json.dumps(data).encode()
                if isinstance(text, str) and "unknown model:" in text.lower():
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = (
                        "⚠️ Selected model is not registered. Use scripts/switch_model.sh to pick a configured model "
                        "(local qwen3:14b or cloud gemini/openai)."
                    )
                    return json.dumps(data).encode()
                rewritten_runtime_error = (
                    self._rewrite_known_runtime_errors(text) if isinstance(text, str) else None
                )
                if rewritten_runtime_error:
                    self._stats["outbound_filtered"] += 1
                    if not is_owner_chat and "switch_model.sh" in rewritten_runtime_error.lower():
                        data[text_key] = self._collaborator_safe_notice("runtime unavailable")
                    else:
                        data[text_key] = rewritten_runtime_error
                    return json.dumps(data).encode()

                if text:
                    normalized_text = normalize_input(text)
                    scrubbed_text = strip_markdown_exfil(normalized_text)
                    if scrubbed_text != text:
                        data["text"] = scrubbed_text
                        text = scrubbed_text
                        self._stats["outbound_filtered"] += 1

                # Prevent Telegram HTML parse errors caused by redaction placeholders
                # like <EMAIL_ADDRESS> / <PHONE_NUMBER> in sanitized output.
                parse_mode = str(data.get("parse_mode", "")).upper()
                if (
                    parse_mode == "HTML"
                    and not is_owner_chat
                    and isinstance(data.get(text_key), str)
                ):
                    # Collaborator UX/safety: never render model-provided HTML markup
                    # (e.g., <code> blocks) that can expose code-like snippets.
                    cleaned = self._strip_collaborator_html_markup(data[text_key])
                    data[text_key] = cleaned
                    data.pop("parse_mode", None)
                    self._stats["outbound_filtered"] += 1
                    text = cleaned
                    parse_mode = ""
                if parse_mode == "HTML" and isinstance(data.get(text_key), str):
                    if re.search(r"<[A-Z][A-Z0-9_]{1,64}>", data[text_key]):
                        data.pop("parse_mode", None)
                        self._stats["outbound_filtered"] += 1

                if chat_id:
                    blocked_until = self._recent_outbound_blocks_until.get(chat_id, 0.0)
                    if blocked_until > time.time() and not is_owner_chat:
                        self._quarantine_outbound_block(
                            chat_id=chat_id,
                            text=text or "",
                            reason="Outbound block cascade active",
                            source="telegram_outbound_cascade",
                        )
                        data["text"] = self._collaborator_safe_notice("outbound policy block")
                        self._stats["outbound_filtered"] += 1
                        return json.dumps(data).encode()

                if text and chat_id and not is_owner_chat and len(text) > self._max_outbound_chars:
                    self._quarantine_outbound_block(
                        chat_id=chat_id,
                        text=text or "",
                        reason=f"Outbound text exceeds max length ({len(text)} chars)",
                        source="telegram_outbound_overlength",
                    )
                    data["text"] = self._collaborator_safe_notice("outbound policy block")
                    self._stats["outbound_filtered"] += 1
                    self._set_outbound_block_cascade(chat_id, force=True)
                    logger.warning(
                        "Outbound over-length message blocked for chat %s (%d chars)",
                        chat_id,
                        len(text),
                    )
                    return json.dumps(data).encode()

                if text and self.pipeline:
                    pipeline_result = await self.pipeline.process_outbound(
                        response=text,
                        source="telegram",
                        user_trust_level="FULL" if is_owner_chat else "UNTRUSTED",
                        metadata={"chat_id": chat_id},
                    )
                    if pipeline_result.blocked:
                        self._quarantine_outbound_block(
                            chat_id=chat_id,
                            text=text or "",
                            reason=pipeline_result.block_reason
                            or "Pipeline blocked outbound response",
                            source="telegram_outbound_pipeline_block",
                        )
                        data["text"] = (
                            self._collaborator_safe_notice(
                                pipeline_result.block_reason or "outbound policy block"
                            )
                            if not is_owner_chat
                            else _PROTECTED_POLICY_NOTICE
                        )
                        self._stats["outbound_filtered"] += 1
                        self._set_outbound_block_cascade(chat_id)
                        logger.warning(
                            "Outbound message blocked by pipeline: chat_id=%s reason=%s",
                            chat_id,
                            pipeline_result.block_reason,
                        )
                    elif (
                        chat_id
                        and not is_owner_chat
                        and getattr(pipeline_result, "info_filter_redaction_count", 0) > 0
                    ):
                        self._quarantine_outbound_block(
                            chat_id=chat_id,
                            text=text or "",
                            reason=(
                                "Outbound info filter redacted protected content "
                                f"({getattr(pipeline_result, 'info_filter_redaction_count', 0)} redactions)"
                            ),
                            source="telegram_outbound_info_filter_block",
                        )
                        data["text"] = self._collaborator_safe_notice("redacted protected content")
                        self._stats["outbound_filtered"] += 1
                        self._set_outbound_block_cascade(chat_id)
                        logger.warning(
                            "Outbound message blocked after info-filter redactions "
                            "(chat=%s redactions=%s)",
                            chat_id,
                            getattr(pipeline_result, "info_filter_redaction_count", 0),
                        )
                    elif pipeline_result.sanitized_message != text:
                        data["text"] = pipeline_result.sanitized_message
                        self._stats["outbound_filtered"] += 1
                    return json.dumps(data).encode()
                elif text and self.sanitizer:
                    # Fallback: direct sanitizer calls when pipeline is unavailable
                    # 1. PII sanitization (phone numbers, SSNs, emails, etc.)
                    pii_result = await self.sanitizer.sanitize(data["text"])
                    if pii_result.entity_types_found:
                        data["text"] = pii_result.sanitized_content
                        self._stats["outbound_filtered"] += 1
                        logger.info(
                            "Outbound message: PII redacted: chat_id=%s types=%s",
                            chat_id,
                            pii_result.entity_types_found,
                        )
                    # 2. XML leak filter
                    filtered, was_filtered = self.sanitizer.filter_xml_blocks(data["text"])
                    if was_filtered:
                        data["text"] = filtered
                        self._stats["outbound_filtered"] += 1
                        logger.info("Outbound message: XML blocks stripped chat_id=%s", chat_id)
                    # 3. Credential blocking
                    blocked, was_blocked = await self.sanitizer.block_credentials(
                        data["text"], "telegram"
                    )
                    if was_blocked:
                        self._quarantine_outbound_block(
                            chat_id=chat_id,
                            text=text or "",
                            reason="Credential blocking triggered",
                            source="telegram_outbound_credential_block",
                        )
                        data["text"] = blocked
                        self._stats["outbound_filtered"] += 1
                        logger.warning("Outbound message: credentials blocked chat_id=%s", chat_id)
                    return json.dumps(data).encode()
            elif "x-www-form-urlencoded" in ct or (
                not ct
                and b"chat_id=" in body
                and any(
                    marker in body
                    for marker in (
                        b"text=",
                        b"draft=",
                        b"message=",
                        b"content=",
                        b"caption=",
                    )
                )
            ):
                # Telegram draft/edit calls may arrive as urlencoded form payloads.
                # Filter these the same way as JSON payloads to prevent transient leaks.
                parsed = urllib.parse.parse_qsl(
                    body.decode("utf-8", errors="replace"),
                    keep_blank_values=True,
                )
                data = dict(parsed)
                text_key, text = self._resolve_text_field(data)
                chat_id = str(data.get("chat_id", ""))
                is_owner_chat = self._is_owner_chat(chat_id)

                parsed_tool_call = (
                    self._parse_tool_call_json(text) if isinstance(text, str) else None
                )
                embedded_tool_call = (
                    self._extract_embedded_tool_call_json(text) if isinstance(text, str) else None
                )
                if parsed_tool_call is None and embedded_tool_call is not None:
                    parsed_tool_call, emb_start, emb_end = embedded_tool_call
                    leading = text[:emb_start].strip()
                    trailing = text[emb_end:].strip()
                    cleaned = " ".join(part for part in (leading, trailing) if part).strip()
                    if cleaned:
                        if not is_owner_chat:
                            data[text_key] = self._collaborator_safe_notice("tool output redacted")
                            self._stats["outbound_filtered"] += 1
                            return urllib.parse.urlencode(data).encode()
                        tool_name = str(parsed_tool_call.get("name", "")).strip()
                        tool_args = (
                            parsed_tool_call.get("arguments")
                            if isinstance(parsed_tool_call.get("arguments"), dict)
                            else {}
                        )
                        if tool_name == "web_fetch":
                            approval_queued = await self._trigger_web_fetch_approval(
                                chat_id, tool_args
                            )
                            if approval_queued:
                                cleaned = (
                                    f"{cleaned}\n\n"
                                    "🌐 Web access request detected. Approval request queued for this destination."
                                ).strip()
                        data[text_key] = cleaned
                        self._stats["outbound_filtered"] += 1
                        return urllib.parse.urlencode(data).encode()
                if parsed_tool_call is not None:
                    tool_name = str(parsed_tool_call.get("name", "")).strip()
                    tool_args = (
                        parsed_tool_call.get("arguments")
                        if isinstance(parsed_tool_call.get("arguments"), dict)
                        else {}
                    )
                    self._stats["outbound_filtered"] += 1
                    if tool_name.upper() == "NO_REPLY":
                        data[text_key] = (
                            self._collaborator_safe_notice("processing timeout")
                            if not is_owner_chat
                            else "⏳ Agent is still processing a previous request. Please wait 10–20 seconds and retry."
                        )
                    elif (
                        tool_name == "sessions_spawn"
                        and str(tool_args.get("agentId", "")) == "acp.healthcheck"
                    ):
                        data[text_key] = (
                            self._collaborator_safe_notice("restricted command")
                            if not is_owner_chat
                            else "✅ Healthcheck started. I’ll reply with status once complete."
                        )
                    elif tool_name == "web_fetch":
                        approval_queued = await self._trigger_web_fetch_approval(chat_id, tool_args)
                        if not is_owner_chat:
                            data[text_key] = (
                                _COLLABORATOR_EGRESS_NOTICE
                                if approval_queued
                                else self._collaborator_safe_notice("web access unavailable")
                            )
                        else:
                            approval_note = (
                                " Approval request queued for this destination."
                                if approval_queued
                                else ""
                            )
                            data[text_key] = (
                                "🌐 Web fetch requested, but this model returned raw tool JSON instead of executing it. "
                                "Switch to a tool-capable model (e.g., scripts/switch_model.sh gemini or local qwen3:14b once pulled)."
                                + approval_note
                            )
                    elif tool_name in {"sessions_spawn", "sessions_send", "subagents"}:
                        data[text_key] = (
                            self._collaborator_safe_notice("restricted command")
                            if not is_owner_chat
                            else "✅ Request accepted and queued."
                        )
                    else:
                        data[text_key] = (
                            self._collaborator_safe_notice("tool output redacted")
                            if not is_owner_chat
                            else _PROTECTED_POLICY_NOTICE
                        )
                    return urllib.parse.urlencode(data).encode()

                if isinstance(text, str) and "session file locked" in text.lower():
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = (
                        self._collaborator_safe_notice("processing timeout")
                        if not is_owner_chat
                        else "⏳ Agent is still processing a previous request. Please wait 10–20 seconds and retry."
                    )
                    return urllib.parse.urlencode(data).encode()
                if (
                    not is_owner_chat
                    and isinstance(text, str)
                    and normalize_input(text)
                    .strip()
                    .lower()
                    .startswith("⚠️ agent failed before reply:")
                ):
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = self._collaborator_safe_notice("runtime unavailable")
                    return urllib.parse.urlencode(data).encode()
                if (
                    not is_owner_chat
                    and isinstance(text, str)
                    and "not authorized to use this command" in text.lower()
                ):
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = self._collaborator_safe_notice("restricted command")
                    return urllib.parse.urlencode(data).encode()
                if self._is_no_reply_token(text):
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = (
                        self._collaborator_safe_notice("processing timeout")
                        if not is_owner_chat
                        else "⏳ Agent is still processing a previous request. Please wait 10–20 seconds and retry."
                    )
                    return urllib.parse.urlencode(data).encode()
                if isinstance(text, str) and "does not support tools" in text.lower():
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = (
                        "⚠️ Current local model does not support tool calls. Use scripts/switch_model.sh local qwen3:14b (or a tools-capable model)."
                    )
                    return urllib.parse.urlencode(data).encode()
                if isinstance(text, str) and "ollama requires authentication" in text.lower():
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = (
                        "⚠️ Ollama provider is not configured in this session. Set OLLAMA_API_KEY=ollama-local and restart, "
                        "or run scripts/switch_model.sh gemini."
                    )
                    return urllib.parse.urlencode(data).encode()
                if isinstance(text, str) and "unknown model:" in text.lower():
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = (
                        "⚠️ Selected model is not registered. Use scripts/switch_model.sh to pick a configured model "
                        "(local qwen3:14b or cloud gemini/openai)."
                    )
                    return urllib.parse.urlencode(data).encode()
                rewritten_runtime_error = (
                    self._rewrite_known_runtime_errors(text) if isinstance(text, str) else None
                )
                if rewritten_runtime_error:
                    self._stats["outbound_filtered"] += 1
                    if not is_owner_chat and "switch_model.sh" in rewritten_runtime_error.lower():
                        data[text_key] = self._collaborator_safe_notice("runtime unavailable")
                    else:
                        data[text_key] = rewritten_runtime_error
                    return urllib.parse.urlencode(data).encode()
                if (
                    not is_owner_chat
                    and isinstance(text, str)
                    and (
                        "multi-turn disclosure" in text.lower()
                        or "blocked due to security protocols" in text.lower()
                    )
                ):
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = self._collaborator_safe_notice("policy block")
                    return urllib.parse.urlencode(data).encode()
                if (
                    not is_owner_chat
                    and isinstance(text, str)
                    and (
                        "security monitoring active at" in text.lower()
                        and "threshold" in text.lower()
                    )
                ):
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = self._collaborator_safe_notice("policy block")
                    return urllib.parse.urlencode(data).encode()
                if (
                    not is_owner_chat
                    and isinstance(text, str)
                    and self._contains_legacy_block_notice(text)
                ):
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = self._collaborator_safe_notice("policy block")
                    return urllib.parse.urlencode(data).encode()
                if (
                    not is_owner_chat
                    and isinstance(text, str)
                    and self._contains_internal_approval_banner(text)
                ):
                    self._stats["outbound_filtered"] += 1
                    _owner_id_str = str(getattr(self._rbac, "owner_user_id", "")).strip()
                    if _owner_id_str:
                        asyncio.create_task(
                            self._send_owner_admin_notice(
                                int(_owner_id_str),
                                "🔔 *Egress Approval Triggered*\n\nA collaborator interaction generated an egress approval request. Check /pending to review.",
                            )
                        )
                    data[text_key] = _COLLABORATOR_EGRESS_NOTICE
                    return urllib.parse.urlencode(data).encode()
                if (
                    not is_owner_chat
                    and isinstance(text, str)
                    and self._contains_high_risk_collaborator_leakage(text)
                ):
                    self._stats["outbound_filtered"] += 1
                    data[text_key] = self._collaborator_safe_notice("redacted protected content")
                    return urllib.parse.urlencode(data).encode()
                # Redact owner's Telegram user ID from collaborator responses (form-encoded path).
                if not is_owner_chat and isinstance(text, str) and self._rbac:
                    _oid = str(getattr(self._rbac, "owner_user_id", "")).strip()
                    if len(_oid) >= 7 and _oid in text:
                        self._stats["outbound_filtered"] += 1
                        redacted = re.sub(
                            r"(?:Telegram\s+(?:user\s+)?ID\s*:?\s*)?" + re.escape(_oid),
                            "",
                            text,
                            flags=re.IGNORECASE,
                        ).strip()
                        data[text_key] = (
                            redacted
                            if redacted
                            else self._collaborator_safe_notice("redacted protected content")
                        )
                        return urllib.parse.urlencode(data).encode()
        except Exception as e:
            logger.error(f"Outbound filter error: {e}")
            # Fail-closed: if pipeline crashes, block non-owner outbound messages.
            # Determine if the destination is the owner by inspecting chat_id.
            try:
                data = json.loads(body)
                chat_id = str(data.get("chat_id", ""))
                owner_id = str(self._rbac.owner_user_id) if self._rbac else ""
                if owner_id and chat_id != owner_id:
                    self._quarantine_outbound_block(
                        chat_id=chat_id,
                        text=str(data.get("text", "")),
                        reason="Security pipeline error (fail-closed)",
                        source="telegram_outbound_fail_closed",
                    )
                    data["text"] = self._collaborator_safe_notice("security pipeline error")
                    return json.dumps(data).encode()
            except Exception:
                pass
        return body

    async def _trigger_web_fetch_approval(self, chat_id: str, tool_args: dict[str, Any]) -> bool:
        """Queue an interactive egress approval when raw web_fetch JSON leaks."""
        url = normalize_input(str((tool_args or {}).get("url", ""))).strip().strip("'\"`<>[]{}()")
        if not url:
            return False
        if "\n" in url or "\r" in url:
            return False
        if "://" not in url and self._looks_like_filename_reference(url):
            return False
        if " " in url or "\t" in url:
            # Salvage malformed tool args like "https://weather.com/path with spaces"
            # by extracting the first URL token for destination approval only.
            first_token = re.split(r"[ \t]+", url, maxsplit=1)[0].strip()
            if not first_token:
                return False
            url = first_token
            if "://" not in url and self._looks_like_filename_reference(url):
                return False
        if re.search(r"%(?:0[0-9a-fA-F]|1[0-9a-fA-F]|7[fF])", url):
            return False
        if "\\" in url:
            return False
        if any(ord(ch) < 32 or ord(ch) == 127 for ch in url):
            return False
        if len(url) > 2048:
            return False
        if url.startswith("//"):
            url = f"https:{url}"
        parsed = urlparse(url if "://" in url else f"https://{url}")
        scheme = (parsed.scheme or "https").lower()
        if scheme not in {"http", "https"}:
            return False
        if parsed.username is not None or parsed.password is not None:
            return False
        raw_domain = (parsed.hostname or "").strip().lower()
        if ".." in raw_domain:
            return False
        domain = raw_domain.strip(".")
        if not domain:
            return False
        # Reject malformed hosts instead of silently rewriting them into a
        # potentially different allowlist destination.
        if re.search(r"[^a-z0-9.-]", domain):
            return False
        if not domain:
            return False
        if "." not in domain:
            return False
        if not self._is_valid_domain_name(domain):
            return False
        blocked_suffixes = (
            ".local",
            ".localhost",
            ".localdomain",
            ".internal",
            ".lan",
            ".home",
            ".test",
            ".invalid",
        )
        if domain.endswith(blocked_suffixes):
            return False
        if domain in {"localhost", "local", "localdomain"}:
            return False
        try:
            # Never queue collaborator egress approvals for literal IP targets.
            # IP-based egress (esp. private/link-local) should remain blocked by
            # network policy rather than entering allowlist workflows.
            ipaddress.ip_address(domain)
            return False
        except ValueError:
            pass
        try:
            from gateway.ingest_api.state import app_state as _app_state

            _egress_filter = getattr(_app_state, "egress_filter", None)
            if _egress_filter is None or not hasattr(_egress_filter, "check_async"):
                return False
            _port = parsed.port or (80 if scheme == "http" else 443)
            if _port not in {80, 443}:
                return False
            approval_key = ((chat_id or "unknown"), scheme, domain, _port)
            now = time.time()
            if len(self._recent_web_fetch_approval_until) > 1024:
                self._recent_web_fetch_approval_until = {
                    k: v for k, v in self._recent_web_fetch_approval_until.items() if v > now
                }
            blocked_until = self._recent_web_fetch_approval_until.get(approval_key, 0.0)
            if blocked_until > now:
                return False
            _agent_id = f"telegram_web_fetch:{chat_id}" if chat_id else "telegram_web_fetch"
            asyncio.create_task(
                _egress_filter.check_async(
                    agent_id=_agent_id,
                    destination=f"{scheme}://{domain}",
                    port=_port,
                    tool_name="web_fetch",
                )
            )
            self._recent_web_fetch_approval_until[approval_key] = (
                now + self._web_fetch_approval_cooldown_seconds
            )
            return True
        except Exception:
            return False

    def _suppress_duplicate_system_notice(self, body: bytes, content_type: Optional[str]) -> bool:
        """Suppress repeated startup/shutdown system notices in short windows."""

        def _canonical_notice(raw: str) -> str:
            text = (raw or "").strip()
            # Normalize emoji-variation and punctuation drift so duplicate startup
            # notices are suppressed even when renderers alter glyph variants.
            lowered = re.sub(r"[\ufe0f\u200d]", "", text).lower()
            lowered = re.sub(r"\s+", " ", lowered).strip()
            if "agentshroud" in lowered and "online" in lowered:
                return "agentshroud_online"
            if (
                "agentshroud" in lowered
                and "starting" in lowered
                and "readiness delayed" in lowered
            ):
                return "agentshroud_starting_delayed"
            if "agentshroud" in lowered and "starting" in lowered:
                return "agentshroud_starting"
            if "agentshroud" in lowered and "shutting down" in lowered:
                return "agentshroud_shutting_down"
            return ""

        try:
            ct = (content_type or "").lower()
            payload: dict[str, Any] = {}
            if "json" in ct or (not ct and body.lstrip().startswith(b"{")):
                payload = json.loads(body)
            elif "x-www-form-urlencoded" in ct or (not ct and b"=" in body):
                payload = dict(
                    urllib.parse.parse_qsl(
                        body.decode("utf-8", errors="replace"), keep_blank_values=True
                    )
                )
            chat_id = str(payload.get("chat_id", "")).strip()
            _, text = self._resolve_text_field(payload)
            canonical_notice = _canonical_notice(text or "")
            if not chat_id or not canonical_notice:
                return False
            key = (chat_id, canonical_notice)
            now = time.time()
            blocked_until = self._recent_system_notice_until.get(key, 0.0)
            if blocked_until > now:
                logger.info(
                    "Suppressing duplicate system notice for chat %s: %s",
                    chat_id,
                    canonical_notice,
                )
                return True
            self._recent_system_notice_until[key] = now + self._system_notice_cooldown_seconds
        except Exception:
            return False
        return False

    @staticmethod
    def _is_suppressed_outbound_payload(body: bytes, content_type: Optional[str]) -> bool:
        """True when filtered payload should be dropped instead of forwarded."""
        try:
            ct = (content_type or "").lower()
            if "json" in ct or (not ct and body.lstrip().startswith(b"{")):
                data = json.loads(body)
                for key in ("text", "draft", "message", "content", "caption"):
                    value = data.get(key)
                    if isinstance(value, str) and value.strip() == _SUPPRESS_OUTBOUND_TOKEN:
                        return True
                return False
            if "x-www-form-urlencoded" in ct or (not ct and b"=" in body):
                data = dict(
                    urllib.parse.parse_qsl(
                        body.decode("utf-8", errors="replace"), keep_blank_values=True
                    )
                )
                for key in ("text", "draft", "message", "content", "caption"):
                    value = data.get(key)
                    if isinstance(value, str) and value.strip() == _SUPPRESS_OUTBOUND_TOKEN:
                        return True
        except Exception:
            return False
        return False

    async def _filter_inbound_updates(self, response_data: dict) -> dict:
        """Scan inbound messages from getUpdates for security threats."""
        updates = response_data.get("result", [])
        filtered_updates = []

        for update in updates:
            # Handle inline button callbacks for egress approve/deny
            callback_query = update.get("callback_query")
            if callback_query:
                cb_data = callback_query.get("data", "")
                if cb_data.startswith("egress_"):
                    try:
                        cb_user_id = str((callback_query.get("from") or {}).get("id", ""))
                        cb_chat_id = ((callback_query.get("message") or {}).get("chat") or {}).get(
                            "id"
                        )
                        if cb_user_id and self._rbac and not self._rbac.is_owner(cb_user_id):
                            self._stats["messages_blocked"] += 1
                            self._quarantine_blocked_message(
                                user_id=cb_user_id,
                                chat_id=cb_chat_id,
                                text=cb_data,
                                reason="Blocked collaborator egress-callback action",
                                source="telegram_callback_rbac_block",
                            )
                            from gateway.ingest_api.state import app_state as _app_state

                            _notifier = getattr(_app_state, "egress_notifier", None)
                            if _notifier:
                                await _notifier.answer_callback(
                                    callback_query.get("id", ""),
                                    "Not authorized for approval actions",
                                )
                            continue
                        from gateway.ingest_api.state import app_state as _app_state

                        _notifier = getattr(_app_state, "egress_notifier", None)
                        if _notifier:
                            result = await _notifier.handle_callback(cb_data)
                            if not isinstance(result, dict):
                                result = {
                                    "status": "error",
                                    "reason": str(result),
                                    "action": "ignored",
                                }
                            _queue = getattr(_app_state, "egress_approval_queue", None)
                            from gateway.security.egress_approval import ApprovalMode

                            action = result.get("action", "")
                            domain = result.get("domain", "")
                            rid = result.get("request_id", "")

                            # If request_not_found (e.g. gateway restarted), fall back
                            # to the persisted request_domain_map so old buttons still work.
                            if (
                                result.get("status") == "error"
                                and result.get("reason") == "request_not_found"
                                and _queue
                                and rid
                            ):
                                domain = _queue._request_domain_map.get(rid, "")
                                if domain:
                                    action = (
                                        "allow_always"
                                        if "allow_always" in cb_data
                                        else (
                                            "allow_once"
                                            if "allow_once" in cb_data
                                            else "deny" if "deny" in cb_data else ""
                                        )
                                    )
                                    result = {
                                        "status": "ok",
                                        "action": action,
                                        "request_id": rid,
                                        "domain": domain,
                                    }

                            if _queue and result.get("status") == "ok":
                                if action == "allow_always":
                                    # Use add_rule directly — more reliable than approve(rid)
                                    # because it works even when the in-flight request is gone.
                                    await _queue.add_rule(domain, "allow", ApprovalMode.PERMANENT)
                                elif action in ("allow_1h", "allow_4h", "allow_24h"):
                                    # Time-limited: unblock the waiting future (once) and
                                    # record the TTL in EgressFilter for subsequent requests.
                                    await _queue.approve(rid, ApprovalMode.ONCE)
                                    _expires_at = result.get("expires_at")
                                    if _expires_at and domain:
                                        from gateway.ingest_api.state import (
                                            app_state as _state,
                                        )

                                        _ef = getattr(_state, "egress_filter", None)
                                        if _ef is not None and hasattr(_ef, "grant_timed_approval"):
                                            _ef.grant_timed_approval(domain, _expires_at)
                                elif action == "allow_once":
                                    await _queue.approve(rid, ApprovalMode.ONCE)
                                elif action == "deny":
                                    await _queue.deny(rid, ApprovalMode.ONCE)

                            # Build a human-readable decision label.
                            if result.get("status") == "ok":
                                _domain_label = domain or "unknown"
                                _expires_label = result.get("expires_at", "")
                                if action == "allow_always":
                                    _toast = f"✅ Always allowed: {_domain_label}"
                                    _edit_text = (
                                        f"✅ *Egress Always Allowed*\n\n"
                                        f"Domain: `{_domain_label}`\n"
                                        f"Rule: permanent\n"
                                        f"ID: `{rid[:8]}`"
                                    )
                                elif action in ("allow_1h", "allow_4h", "allow_24h"):
                                    _dur = action.replace("allow_", "")
                                    _toast = f"✅ Allowed {_dur}: {_domain_label}"
                                    _edit_text = (
                                        f"✅ *Egress Allowed ({_dur})*\n\n"
                                        f"Domain: `{_domain_label}`\n"
                                        f"Expires: `{_expires_label or 'soon'}`\n"
                                        f"ID: `{rid[:8]}`"
                                    )
                                elif action == "allow_once":
                                    _toast = f"✅ Allowed once: {_domain_label}"
                                    _edit_text = (
                                        f"✅ *Egress Allowed Once*\n\n"
                                        f"Domain: `{_domain_label}`\n"
                                        f"ID: `{rid[:8]}`"
                                    )
                                else:
                                    _toast = f"❌ Denied: {_domain_label}"
                                    _edit_text = (
                                        f"❌ *Egress Denied*\n\n"
                                        f"Domain: `{_domain_label}`\n"
                                        f"ID: `{rid[:8]}`"
                                    )
                            else:
                                _toast = "⚠️ Approval error — request not found"
                                _edit_text = "⚠️ *Egress Approval Error*\n\nRequest not found (may have expired)."

                            await _notifier.answer_callback(
                                callback_query.get("id", ""),
                                _toast,
                            )
                            # Edit the original approval message to show the decision.
                            _cb_msg_id = (callback_query.get("message") or {}).get("message_id")
                            if _cb_msg_id and cb_chat_id:
                                await _notifier.edit_decision_message(
                                    cb_chat_id, _cb_msg_id, _edit_text
                                )
                            # Notify originating collaborator of decision (plain text, no buttons).
                            # agent_id format: "telegram_web_fetch:{user_id}"
                            _result_agent_id = result.get("agent_id", "")
                            _owner_uid = str(getattr(self._rbac, "owner_user_id", "")).strip()
                            if _result_agent_id and ":" in _result_agent_id:
                                _origin_uid = _result_agent_id.split(":", 1)[1]
                                if _origin_uid and _origin_uid != _owner_uid:
                                    _collab_notice = (
                                        f"{_PROTECT_HEADER}"
                                        f"*Egress Decision*\n\n"
                                        f"{_edit_text}"
                                    )
                                    asyncio.create_task(
                                        self._send_owner_admin_notice(
                                            int(_origin_uid), _collab_notice
                                        )
                                    )
                            logger.info(
                                "Egress callback handled: %s",
                                json.dumps(result, sort_keys=True),
                            )
                    except Exception as _ce:
                        logger.error("Egress callback error (non-fatal): %s", _ce)
                elif cb_data.startswith("collab_approve_") or cb_data.startswith("collab_deny_"):
                    # Inline button tap from the access request notification.
                    try:
                        _cb_action = "approve" if cb_data.startswith("collab_approve_") else "deny"
                        _target_id = (
                            cb_data[len("collab_approve_") :]
                            if _cb_action == "approve"
                            else cb_data[len("collab_deny_") :]
                        ).strip()
                        # RBAC guard — only owner can act
                        if cb_user_id and self._rbac and not self._rbac.is_owner(cb_user_id):
                            await self._answer_callback_query(
                                callback_query.get("id", ""),
                                "Not authorized for approval actions",
                            )
                        elif _target_id:
                            _pending_info = (
                                self._pending_collaborator_requests.get(_target_id, {}) or {}
                            )
                            _cb_username = str(_pending_info.get("username", "")).strip()
                            _cb_display = (
                                f"@{_cb_username}"
                                if _cb_username and _cb_username != "unknown"
                                else f"ID {_target_id}"
                            )
                            _cb_msg_id = (callback_query.get("message") or {}).get("message_id")

                            if _cb_action == "approve":
                                self._runtime_revoked_collaborators.discard(_target_id)
                                self._pending_collaborator_requests.pop(_target_id, None)
                                if self._rbac and _target_id not in {
                                    str(uid) for uid in (self._rbac.collaborator_user_ids or [])
                                }:
                                    self._rbac.collaborator_user_ids = list(
                                        self._rbac.collaborator_user_ids or []
                                    ) + [_target_id]
                                persist_approved_collaborator(_target_id)
                                _decision_text = f"✅ *Access Approved*\n\nUser: {_cb_display}\nID: `{_target_id}`"
                                _toast = f"✅ Approved: {_cb_display}"
                                # Notify the collaborator
                                _collab_chat = _pending_info.get("chat_id")
                                if _collab_chat:
                                    try:
                                        await self._send_owner_admin_notice(
                                            int(str(_collab_chat)),
                                            f"{_PROTECT_HEADER}Access approved. You can continue in collaborator mode.",
                                        )
                                    except Exception:
                                        pass
                            else:
                                self._pending_collaborator_requests.pop(_target_id, None)
                                self._runtime_revoked_collaborators.add(_target_id)
                                _decision_text = (
                                    f"❌ *Access Denied*\n\nUser: {_cb_display}\nID: `{_target_id}`"
                                )
                                _toast = f"❌ Denied: {_cb_display}"
                                _collab_chat = _pending_info.get("chat_id")
                                if _collab_chat:
                                    try:
                                        await self._send_owner_admin_notice(
                                            int(str(_collab_chat)),
                                            f"{_PROTECT_HEADER}Access denied. Contact owner if needed.",
                                        )
                                    except Exception:
                                        pass

                            await self._answer_callback_query(callback_query.get("id", ""), _toast)
                            if _cb_msg_id and cb_chat_id:
                                await self._edit_telegram_message(
                                    cb_chat_id, _cb_msg_id, _decision_text
                                )
                            logger.info(
                                "Collab callback handled: action=%s target=%s",
                                _cb_action,
                                _target_id,
                            )
                    except Exception as _ce:
                        logger.error("Collab callback error (non-fatal): %s", _ce)
                # Drop callback_query updates — they are not bot messages
                continue

            message = update.get("message", {}) or update.get("edited_message", {})
            if not message:
                filtered_updates.append(update)
                continue

            text = message.get("text", "") or message.get("caption", "")
            original_transport_text = text
            user_id = str(message.get("from", {}).get("id", "unknown"))
            chat_id = message.get("chat", {}).get("id")

            # ── Group chat at-mention filter ──────────────────────────────────
            # ALL group messages are forwarded to the bot for conversational context.
            # But outbound responses are suppressed unless the bot was @mentioned.
            # _group_response_eligible[chat_id] = True → bot may respond.
            # _group_response_eligible[chat_id] = False → context only, no reply sent.
            # Requires TELEGRAM_BOT_USERNAME env var; if unset, all messages get replies.
            if (
                self._group_mention_only
                and self._bot_username
                and self._is_group_message(message)
                and chat_id is not None
            ):
                mentioned = self._bot_is_mentioned(message, self._bot_username)
                self._group_response_eligible[int(chat_id)] = mentioned
                if not mentioned:
                    logger.debug(
                        "Group message (context-only, no reply): user_id=%s chat_id=%s preview=%s",
                        user_id,
                        chat_id,
                        (text or "")[:40].replace("\n", " "),
                    )

            if not text:
                # ── CVE-2026-32049: reject oversized media before reaching the bot ─────
                # Telegram includes file_size on document/video/audio/voice/video_note.
                # Drop updates whose declared size exceeds _MAX_MEDIA_FILE_SIZE so an
                # oversized payload can never crash the OpenClaw process.
                for _mk in _MEDIA_KEYS:
                    _media_obj = message.get(_mk)
                    if isinstance(_media_obj, dict):
                        _fsize = _media_obj.get("file_size")
                        if isinstance(_fsize, int) and _fsize > _MAX_MEDIA_FILE_SIZE:
                            logger.warning(
                                "Oversized media dropped (CVE-2026-32049): "
                                "type=%s file_size=%d limit=%d user_id=%s",
                                _mk,
                                _fsize,
                                _MAX_MEDIA_FILE_SIZE,
                                user_id,
                            )
                            if chat_id:
                                await self._send_owner_admin_notice(
                                    int(str(chat_id)),
                                    f"{_PROTECT_HEADER}Oversized media rejected ({_fsize:,} bytes exceeds {_MAX_MEDIA_FILE_SIZE:,} byte limit).",
                                )
                            break
                else:
                    # In local_only mode, collaborators cannot send raw media (no caption).
                    # Forwarding it to the bot would bypass all inbound collaborator guards.
                    _is_known_collab = (
                        self._rbac
                        and not self._rbac.is_owner(user_id)
                        and user_id
                        in {str(uid) for uid in (self._rbac.collaborator_user_ids or [])}
                    )
                    if (
                        _is_known_collab
                        and self._resolve_collaborator_mode(user_id) == "local_only"
                    ):
                        if chat_id:
                            await self._send_owner_admin_notice(
                                int(str(chat_id)),
                                f"{_PROTECT_HEADER}Media without a caption cannot be processed in collaborator mode. Add a text caption to your image or file.",
                            )
                        continue
                    filtered_updates.append(update)
                continue

            # Normalize transport text before any guard checks so downstream
            # detectors see de-obfuscated content (zero-width, encoded entities, etc.).
            normalized_text = normalize_input(text)
            if normalized_text != text:
                if "message" in update:
                    update["message"]["text"] = normalized_text
                elif "edited_message" in update:
                    update["edited_message"]["text"] = normalized_text
                text = normalized_text

            self._stats["messages_scanned"] += 1

            # ── Role resolution ───────────────────────────────────────────────
            is_owner = self._rbac.is_owner(user_id) if self._rbac else False
            is_revoked = user_id in self._runtime_revoked_collaborators
            is_collaborator = (
                self._rbac
                and not is_owner
                and not is_revoked
                and user_id in {str(uid) for uid in (self._rbac.collaborator_user_ids or [])}
            )

            # ── Inbound attribution log ───────────────────────────────────────
            logger.info(
                "Inbound message: user_id=%s role=%s chat_id=%s preview=%s",
                user_id,
                "owner" if is_owner else ("collaborator" if is_collaborator else "unknown"),
                chat_id,
                text[:40].replace("\n", " "),
            )

            # ── Progressive lockdown: early suspend check ─────────────────────
            # If the user's session has been suspended by cumulative block count,
            # drop the message and send a one-time notice to the user (rate-limited
            # to avoid flooding; default cooldown 5 min).
            # Immune users bypass this check entirely (owner-granted, testing only).
            if (
                not is_owner
                and not self._is_immune(user_id)
                and self._lockdown is not None
                and self._lockdown.is_suspended(user_id)
            ):
                logger.warning(
                    "ProgressiveLockdown: dropping message from suspended user %s", user_id
                )
                _now = time.time()
                if chat_id is not None and _now > self._suspended_drop_notice_until.get(
                    user_id, 0.0
                ):
                    self._suspended_drop_notice_until[user_id] = (
                        _now + self._suspended_drop_notice_cooldown_seconds
                    )
                    try:
                        await self._send_telegram_text(
                            int(chat_id),
                            "\U0001f534 Your session is suspended. Contact the system owner to restore access.",
                        )
                    except Exception as _sde:
                        logger.debug("Suspended-drop notice error: %s", _sde)
                filtered_updates.append({"update_id": update.get("update_id", 0)})
                continue

            # ── Egress preflight from user intent ────────────────────────────
            # If a message includes an explicit URL/domain, proactively queue
            # interactive egress approval for that destination. This preserves
            # "little snitch" UX even when the model fails before tool execution.
            # Owner-only: collaborators must not receive or trigger interactive
            # egress approval prompts.
            preflight_egress_queued = False
            try:
                if isinstance(original_transport_text, str) and re.search(
                    r"%(?:0[0-9a-fA-F]|1[0-9a-fA-F]|7[fF])",
                    original_transport_text,
                ):
                    requested_url = None
                else:
                    requested_url = self._extract_first_egress_target(text)
                if requested_url and is_owner:
                    await self._trigger_web_fetch_approval(
                        str(chat_id or ""),
                        {"url": requested_url},
                    )
                    preflight_egress_queued = True
            except Exception as _pf:
                logger.debug("Egress preflight approval error (non-fatal): %s", _pf)

            # ── Gateway-level collaborator/non-owner activity tracking ────────
            # This is the authoritative tracking point — all messages (including
            # long-polling) flow through here. webhook_receiver only handles
            # push-mode webhooks which are not used in this deployment.
            # Track all non-owner users; tracker policy decides whether unknown
            # users are auto-enrolled (track_unknown_non_owner).
            try:
                from gateway.ingest_api.state import app_state as _app_state

                _tracker = getattr(_app_state, "collaborator_tracker", None)
                if _tracker and (not is_owner or is_owner):  # track owner and collaborators
                    sender = message.get("from", {})
                    _telegram_name = sender.get("first_name") or (
                        f"@{sender['username']}" if sender.get("username") else "unknown"
                    )
                    _resolved = self._resolve_display_name(user_id)
                    _username = _resolved if _resolved != user_id else _telegram_name
                    _msg_id = message.get("message_id", int(time.time()))
                    _corr_id = f"{user_id}:{_msg_id}"
                    # Store correlation for outbound pairing (TTL: evict entries older than 5 min)
                    import time as _time_mod

                    _now = _time_mod.time()
                    self._last_inbound_corr = {
                        k: v for k, v in self._last_inbound_corr.items() if _now - v[1] < 300
                    }
                    self._last_inbound_corr[str(chat_id)] = (_corr_id, _now)
                    _tracker.record_activity(
                        user_id=user_id,
                        username=_username,
                        message_preview=text[:80],
                        source="telegram",
                        direction="inbound",
                        correlation_id=_corr_id,
                    )
            except Exception as _te:
                logger.debug("Collaborator tracker error (non-fatal): %s", _te)

            # Register collaborator chat_id → user_id for outbound response attribution
            if is_collaborator and chat_id:
                self._collaborator_chat_ids[str(chat_id)] = user_id

            # Unknown or revoked users must be re-approved by owner.
            if not is_owner and not is_collaborator and chat_id:
                sender = message.get("from", {}) or {}
                username = (
                    sender.get("username")
                    or sender.get("first_name")
                    or sender.get("last_name")
                    or "unknown"
                )
                # Stranger rate limit: throttle unknown users before queuing access
                # requests. Prevents queue flooding from unapproved accounts.
                if not self._stranger_rate_limiter.check(user_id):
                    now = time.time()
                    # Prune expired rate-limit entries to prevent unbounded growth
                    _now_prune = time.time()
                    expired_keys = [
                        k
                        for k, v in self._recent_stranger_rate_limit_until.items()
                        if v < _now_prune
                    ]
                    for k in expired_keys:
                        del self._recent_stranger_rate_limit_until[k]
                    if self._recent_stranger_rate_limit_until.get(user_id, 0) <= now:
                        await self._send_stranger_rate_limit_notice(chat_id, user_id=user_id)
                        self._recent_stranger_rate_limit_until[user_id] = (
                            now + self._rate_limit_notice_cooldown_seconds
                        )
                    continue
                await self._queue_collaborator_access_request(
                    user_id=user_id,
                    chat_id=chat_id,
                    username=str(username),
                )
                continue

            # ── Disclosure notice — send once per session per collaborator ─────
            if is_collaborator and chat_id and user_id not in self._disclosure_sent:
                await self._send_disclosure(chat_id)
                self._disclosure_sent.add(user_id)

            # ── Session unlock for blocked disclosure tracker on /start ───────
            if is_collaborator and text.strip().lower().startswith("/start"):
                try:
                    from gateway.ingest_api.state import app_state as _app_state

                    _tracker = getattr(_app_state, "multi_turn_tracker", None)
                    if _tracker and _tracker.reset_session(user_id, owner_override=True):
                        logger.info(
                            "Reset MultiTurnTracker session for collaborator %s via /start", user_id
                        )
                except Exception as _re:
                    logger.debug("MultiTurnTracker reset error (non-fatal): %s", _re)

            # ── Collaborator rate limiting (configured msgs/hour) ─────────────
            if (
                is_collaborator
                and not self._is_immune(user_id)
                and not self._collaborator_rate_limiter.check(user_id)
            ):
                self._stats["messages_blocked"] += 1
                logger.warning(
                    "Collaborator %s exceeded rate limit (%s/hr) — dropping message",
                    user_id,
                    self._collaborator_rate_limiter.max_requests,
                )
                self._quarantine_blocked_message(
                    user_id=user_id,
                    chat_id=chat_id,
                    text=text,
                    reason="Rate limit exceeded",
                    source="telegram_rate_limit",
                )
                if chat_id:
                    now = time.time()
                    if len(self._recent_rate_limit_notice_until) > 4096:
                        self._recent_rate_limit_notice_until = {
                            k: v for k, v in self._recent_rate_limit_notice_until.items() if v > now
                        }
                    notice_sent = await self._send_rate_limit_notice(chat_id, user_id=user_id)
                    if notice_sent:
                        self._recent_rate_limit_notice_until[user_id] = (
                            now + self._rate_limit_notice_cooldown_seconds
                        )
                continue

            # ── Local deterministic command handling (owner + collaborators) ──
            # Keep core operator commands deterministic and never delegate to model.
            if chat_id:
                cmd_base = self._normalize_command_token(text)
                normalized_text = normalize_input(text or "").strip().lower()
                if re.match(r"^/?(?:whoami|id)(?:@\w+)?$", normalized_text):
                    # Fallback for Telegram command formatting variants that may
                    # bypass first-token normalization (e.g., @bot suffix).
                    cmd_base = "/whoami"
                sender_info = message.get("from", {}) or {}
                sender_username = (
                    sender_info.get("username")
                    or sender_info.get("first_name")
                    or sender_info.get("last_name")
                    or "unknown"
                )
                if cmd_base in {"/whoami", "/id", "/status", "/help", "/start"}:
                    logger.info(
                        "Inbound local-command candidate user=%s owner=%s collaborator=%s cmd=%r text=%r",
                        user_id,
                        is_owner,
                        is_collaborator,
                        cmd_base,
                        (text or "")[:120],
                    )
                local_handler = None
                local_label = ""
                if cmd_base in _LOCAL_START_COMMANDS:
                    local_label = "start"
                    is_owner_snapshot = is_owner

                    async def _local_start_handler(target_chat_id: int) -> None:
                        await self._send_local_start_notice(
                            target_chat_id,
                            is_owner=is_owner_snapshot,
                        )

                    local_handler = _local_start_handler
                elif cmd_base in _LOCAL_HELP_COMMANDS:
                    local_label = "help"
                    is_owner_snapshot = is_owner

                    async def _local_help_handler(target_chat_id: int) -> None:
                        await self._send_local_help_notice(
                            target_chat_id,
                            is_owner=is_owner_snapshot,
                        )

                    local_handler = _local_help_handler
                elif cmd_base in _LOCAL_HEALTHCHECK_COMMANDS:
                    local_handler = self._send_local_healthcheck_notice
                    local_label = "healthcheck"
                elif cmd_base in _LOCAL_STATUS_COMMANDS:
                    local_label = "status"
                    is_owner_snapshot = is_owner

                    async def _local_status_handler(target_chat_id: int) -> None:
                        await self._send_local_status_notice(
                            target_chat_id,
                            is_owner=is_owner_snapshot,
                        )

                    local_handler = _local_status_handler
                elif cmd_base in _LOCAL_MODEL_STATUS_COMMANDS:
                    local_handler = self._send_local_model_notice
                    local_label = "model-status"
                elif cmd_base in _LOCAL_WHOAMI_COMMANDS:
                    local_label = "whoami"
                    is_owner_snapshot = is_owner
                    user_id_snapshot = user_id
                    username_snapshot = str(sender_username)

                    async def _local_whoami_handler(target_chat_id: int) -> None:
                        await self._send_local_whoami_notice(
                            target_chat_id,
                            user_id=user_id_snapshot,
                            is_owner=is_owner_snapshot,
                            username=username_snapshot,
                        )

                    local_handler = _local_whoami_handler
                elif is_owner and cmd_base in _LOCAL_PENDING_COMMANDS:
                    local_handler = self._send_owner_pending_notice
                    local_label = "pending"
                elif is_owner and cmd_base in _LOCAL_COLLABS_COMMANDS:
                    local_handler = self._send_owner_collabs_notice
                    local_label = "collabs"

                # ── Group management (owner-only) ─────────────────────────────
                elif is_owner and cmd_base in _LOCAL_LISTGROUPS_COMMANDS:
                    local_label = "listgroups"
                    _owner_chat_snap = chat_id

                    async def _local_listgroups_handler(target_chat_id: int) -> None:
                        from gateway.ingest_api.state import app_state as _s

                        _gr = getattr(_s, "group_registry", None)
                        if not _gr:
                            await self._send_owner_admin_notice(
                                target_chat_id, f"{_PROTECT_HEADER}Group registry unavailable."
                            )
                            return
                        groups = _gr.list_groups()
                        if not groups:
                            await self._send_owner_admin_notice(
                                target_chat_id, f"{_PROTECT_HEADER}No groups defined."
                            )
                            return
                        lines = [f"{_PROTECT_HEADER}*Groups ({len(groups)}):*\n"]
                        for g in groups:
                            tg = f"tg:{g.telegram_chat_id}" if g.telegram_chat_id else "tg:unlinked"
                            sl = (
                                f"slack:{g.slack_channel_id}"
                                if g.slack_channel_id
                                else "slack:none"
                            )
                            lines.append(
                                f"• `{g.id}` — {g.name} | {len(g.members)} members | {tg} | {sl}"
                            )
                        await self._send_owner_admin_notice(target_chat_id, "\n".join(lines))

                    local_handler = _local_listgroups_handler

                elif is_owner and cmd_base in _LOCAL_NEWGROUP_COMMANDS:
                    local_label = "newgroup"
                    _args = text.split(None, 2)
                    if len(_args) < 3:
                        await self._send_owner_admin_notice(
                            chat_id, f"{_PROTECT_HEADER}Usage: /newgroup <id> <name>"
                        )
                        continue
                    _grp_id = _args[1].lower().strip()
                    _grp_name = _args[2].strip()
                    _owner_chat_snap = chat_id
                    _grp_id_snap = _grp_id
                    _grp_name_snap = _grp_name

                    async def _local_newgroup_handler(target_chat_id: int) -> None:
                        from gateway.ingest_api.state import app_state as _s

                        _gr = getattr(_s, "group_registry", None)
                        if not _gr:
                            await self._send_owner_admin_notice(
                                target_chat_id, f"{_PROTECT_HEADER}Group registry unavailable."
                            )
                            return
                        try:
                            grp = _gr.create_group(_grp_id_snap, _grp_name_snap)
                        except ValueError as ve:
                            await self._send_owner_admin_notice(
                                target_chat_id, f"{_PROTECT_HEADER}Error: {ve}"
                            )
                            return

                        # Auto-provision Slack channel if slack proxy available
                        _slack_ch = None
                        try:
                            from gateway.ingest_api.main import _slack_proxy as _sp

                            _slack_ch = await _sp.provision_group_channel(
                                _grp_id_snap, _grp_name_snap
                            )
                            if _slack_ch:
                                grp.slack_channel_id = _slack_ch
                                from gateway.security.rbac_config import _persist_groups

                                _persist_groups(_gr.groups)
                        except Exception as _se:
                            logger.debug("Slack group provision error: %s", _se)

                        msg = (
                            f"{_PROTECT_HEADER}*Group created:* `{_grp_id_snap}`\n"
                            f"Name: {_grp_name_snap}\n"
                        )
                        if _slack_ch:
                            msg += f"Slack channel: `{_slack_ch}` provisioned ✅\n"
                        else:
                            msg += "Slack: no channel provisioned (tokens not set or unavailable)\n"
                        msg += (
                            "\n*Telegram group:* Bots cannot create groups. To link:\n"
                            "1. Create a Telegram group manually\n"
                            "2. Add this bot as admin (with Invite + Ban permissions)\n"
                            f"3. Run: `/linkgroup {_grp_id_snap} <chat_id>`\n"
                            "   (Get chat_id from gateway logs after the bot receives a group message)"
                        )
                        await self._send_owner_admin_notice(target_chat_id, msg)

                    local_handler = _local_newgroup_handler

                elif is_owner and cmd_base in _LOCAL_LINKGROUP_COMMANDS:
                    local_label = "linkgroup"
                    _args = text.split(None, 2)
                    if len(_args) < 3:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}Usage: /linkgroup <group_id> <telegram_chat_id>",
                        )
                        continue
                    _lnk_grp_id = _args[1].lower().strip()
                    try:
                        _lnk_chat_id = int(_args[2].strip())
                    except ValueError:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}Invalid chat_id — must be an integer (e.g. -1001234567890)",
                        )
                        continue
                    _lnk_grp_id_snap = _lnk_grp_id
                    _lnk_chat_id_snap = _lnk_chat_id

                    async def _local_linkgroup_handler(target_chat_id: int) -> None:
                        from gateway.ingest_api.state import app_state as _s

                        _gr = getattr(_s, "group_registry", None)
                        if not _gr:
                            await self._send_owner_admin_notice(
                                target_chat_id, f"{_PROTECT_HEADER}Group registry unavailable."
                            )
                            return
                        grp = _gr.get_group(_lnk_grp_id_snap)
                        if not grp:
                            await self._send_owner_admin_notice(
                                target_chat_id,
                                f"{_PROTECT_HEADER}Group `{_lnk_grp_id_snap}` not found. Create it first with /newgroup.",
                            )
                            return
                        grp.telegram_chat_id = _lnk_chat_id_snap
                        from gateway.security.rbac_config import _persist_groups

                        _persist_groups(_gr.groups)
                        await self._send_owner_admin_notice(
                            target_chat_id,
                            f"{_PROTECT_HEADER}Linked `{_lnk_grp_id_snap}` → Telegram chat `{_lnk_chat_id_snap}` ✅\n"
                            f"Group has {len(grp.members)} members. Use /addmember to invite them.",
                        )

                    local_handler = _local_linkgroup_handler

                elif is_owner and cmd_base in _LOCAL_ADDMEMBER_COMMANDS:
                    local_label = "addmember"
                    _args = text.split(None, 2)
                    if len(_args) < 3:
                        await self._send_owner_admin_notice(
                            chat_id, f"{_PROTECT_HEADER}Usage: /addmember <group_id> <user_id>"
                        )
                        continue
                    _am_grp_id = _args[1].lower().strip()
                    _am_user_id = _args[2].strip()
                    _am_grp_id_snap = _am_grp_id
                    _am_user_id_snap = _am_user_id
                    _am_owner_chat = chat_id

                    async def _local_addmember_handler(target_chat_id: int) -> None:
                        from gateway.ingest_api.state import app_state as _s

                        _gr = getattr(_s, "group_registry", None)
                        if not _gr:
                            await self._send_owner_admin_notice(
                                target_chat_id, f"{_PROTECT_HEADER}Group registry unavailable."
                            )
                            return
                        grp = _gr.get_group(_am_grp_id_snap)
                        if not grp:
                            await self._send_owner_admin_notice(
                                target_chat_id,
                                f"{_PROTECT_HEADER}Group `{_am_grp_id_snap}` not found.",
                            )
                            return
                        _gr.add_member(_am_grp_id_snap, _am_user_id_snap)

                        results = []
                        # Telegram: send invite link to the user's DM if group is linked
                        if grp.telegram_chat_id:
                            invite = await self._telegram_create_invite_link(grp.telegram_chat_id)
                            if invite:
                                try:
                                    await self._send_telegram_text(
                                        int(_am_user_id_snap),
                                        f"You've been added to group *{grp.name}*.\n"
                                        f"Join via: {invite}",
                                    )
                                    results.append("Telegram invite sent ✅")
                                except Exception:
                                    results.append(
                                        f"Telegram invite link (send manually): {invite}"
                                    )
                            else:
                                results.append(
                                    "Telegram invite: failed (is bot admin with invite permission?)"
                                )
                        else:
                            results.append("Telegram: no linked group chat (use /linkgroup first)")

                        # Slack: invite to channel if user ID looks like a Slack ID and channel exists
                        if grp.slack_channel_id and _am_user_id_snap.startswith("U"):
                            try:
                                from gateway.ingest_api.main import _slack_proxy as _sp

                                ok = await _sp.invite_channel_member(
                                    grp.slack_channel_id, _am_user_id_snap
                                )
                                results.append(f"Slack invite: {'✅' if ok else '❌'}")
                            except Exception as _se:
                                results.append(f"Slack invite error: {_se}")
                        elif grp.slack_channel_id:
                            results.append("Slack: user ID is not a Slack ID (skipped)")

                        summary = "\n".join(f"  • {r}" for r in results)
                        await self._send_owner_admin_notice(
                            target_chat_id,
                            f"{_PROTECT_HEADER}Added `{_am_user_id_snap}` to group `{_am_grp_id_snap}`:\n{summary}",
                        )

                    local_handler = _local_addmember_handler

                elif is_owner and cmd_base in _LOCAL_REMOVEMEMBER_COMMANDS:
                    local_label = "removemember"
                    _args = text.split(None, 2)
                    if len(_args) < 3:
                        await self._send_owner_admin_notice(
                            chat_id, f"{_PROTECT_HEADER}Usage: /removemember <group_id> <user_id>"
                        )
                        continue
                    _rm_grp_id = _args[1].lower().strip()
                    _rm_user_id = _args[2].strip()
                    _rm_grp_id_snap = _rm_grp_id
                    _rm_user_id_snap = _rm_user_id

                    async def _local_removemember_handler(target_chat_id: int) -> None:
                        from gateway.ingest_api.state import app_state as _s

                        _gr = getattr(_s, "group_registry", None)
                        if not _gr:
                            await self._send_owner_admin_notice(
                                target_chat_id, f"{_PROTECT_HEADER}Group registry unavailable."
                            )
                            return
                        grp = _gr.get_group(_rm_grp_id_snap)
                        if not grp:
                            await self._send_owner_admin_notice(
                                target_chat_id,
                                f"{_PROTECT_HEADER}Group `{_rm_grp_id_snap}` not found.",
                            )
                            return
                        _gr.remove_member(_rm_grp_id_snap, _rm_user_id_snap)

                        results = []
                        # Telegram: kick from group if linked
                        if grp.telegram_chat_id:
                            try:
                                kicked = await self._telegram_kick_member(
                                    grp.telegram_chat_id, int(_rm_user_id_snap)
                                )
                                results.append(f"Telegram kick: {'✅' if kicked else '❌'}")
                            except (ValueError, Exception) as _ke:
                                results.append(f"Telegram kick error: {_ke}")
                        else:
                            results.append("Telegram: no linked group chat")

                        # Slack: remove from channel if Slack ID
                        if grp.slack_channel_id and _rm_user_id_snap.startswith("U"):
                            try:
                                from gateway.ingest_api.main import _slack_proxy as _sp

                                ok = await _sp.kick_channel_member(
                                    grp.slack_channel_id, _rm_user_id_snap
                                )
                                results.append(f"Slack remove: {'✅' if ok else '❌'}")
                            except Exception as _se:
                                results.append(f"Slack remove error: {_se}")
                        elif grp.slack_channel_id:
                            results.append("Slack: user ID is not a Slack ID (skipped)")

                        summary = "\n".join(f"  • {r}" for r in results)
                        await self._send_owner_admin_notice(
                            target_chat_id,
                            f"{_PROTECT_HEADER}Removed `{_rm_user_id_snap}` from group `{_rm_grp_id_snap}`:\n{summary}",
                        )

                    local_handler = _local_removemember_handler

                elif is_owner and cmd_base in _LOCAL_REVOKE_COMMANDS:
                    target_id = self._extract_owner_target_resolved(text)
                    if not target_id:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}Usage: /revoke <telegram_user_id|name>",
                        )
                        continue
                    if target_id == user_id:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}Cannot revoke owner access.",
                        )
                        continue
                    self._runtime_revoked_collaborators.add(target_id)
                    self._disclosure_sent.discard(target_id)
                    try:
                        self._collaborator_rate_limiter.requests.pop(target_id, None)
                    except Exception:
                        pass
                    await self._send_owner_admin_notice(
                        chat_id,
                        (
                            f"{_PROTECT_HEADER}"
                            "Collaborator access revoked.\n"
                            f"User ID: {target_id}\n"
                            "This user now requires owner re-approval workflow."
                        ),
                    )
                    continue
                elif is_owner and cmd_base in _LOCAL_APPROVE_COMMANDS:
                    target_id = self._extract_owner_target_resolved(text)
                    if not target_id:
                        pending_ids = list(self._pending_collaborator_requests.keys())
                        if len(pending_ids) == 1:
                            target_id = pending_ids[0]
                        else:
                            if pending_ids:
                                _pending_lines = []
                                for _pid in pending_ids[:5]:
                                    _pi = self._pending_collaborator_requests.get(_pid, {}) or {}
                                    _pu = str(_pi.get("username", "")).strip()
                                    _pu_label = (
                                        f"@{_pu}" if _pu and _pu != "unknown" else "no username"
                                    )
                                    _pending_lines.append(f"  {_pu_label} ({_pid})")
                                pending_hint = "\nPending:\n" + "\n".join(_pending_lines)
                            else:
                                pending_hint = "\nPending: none"
                            await self._send_owner_admin_notice(
                                chat_id,
                                f"{_PROTECT_HEADER}Usage: /approve <user_id|@username>{pending_hint}",
                            )
                            continue
                    if target_id == user_id:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}Owner access is already active.",
                        )
                        continue
                    pending = self._pending_collaborator_requests.get(target_id)
                    if not pending:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}No pending request found for user {target_id}.",
                        )
                        continue
                    self._runtime_revoked_collaborators.discard(target_id)
                    pending = self._pending_collaborator_requests.pop(target_id, None)
                    if self._rbac and target_id not in {
                        str(uid) for uid in (self._rbac.collaborator_user_ids or [])
                    }:
                        self._rbac.collaborator_user_ids = list(
                            self._rbac.collaborator_user_ids or []
                        ) + [target_id]
                    persist_approved_collaborator(target_id)
                    await self._send_owner_admin_notice(
                        chat_id,
                        f"{_PROTECT_HEADER}Collaborator access approved for user {target_id}.",
                    )
                    if pending and pending.get("chat_id"):
                        try:
                            target_chat = int(str(pending.get("chat_id")))
                            await self._send_owner_admin_notice(
                                target_chat,
                                f"{_PROTECT_HEADER}Access approved. You can continue in collaborator mode.",
                            )
                        except Exception:
                            pass
                    continue
                elif is_owner and cmd_base in _LOCAL_DENY_COMMANDS:
                    target_id = self._extract_owner_target_resolved(text)
                    if not target_id:
                        pending_ids = list(self._pending_collaborator_requests.keys())
                        if len(pending_ids) == 1:
                            target_id = pending_ids[0]
                        else:
                            pending_hint = (
                                f"\nPending: {', '.join(pending_ids[:5])}"
                                if pending_ids
                                else "\nPending: none"
                            )
                            await self._send_owner_admin_notice(
                                chat_id,
                                f"{_PROTECT_HEADER}Usage: /deny <telegram_user_id|name>{pending_hint}",
                            )
                            continue
                    pending = self._pending_collaborator_requests.get(target_id)
                    if not pending:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}No pending request found for user {target_id}.",
                        )
                        continue
                    pending = self._pending_collaborator_requests.pop(target_id, None)
                    self._runtime_revoked_collaborators.add(target_id)
                    await self._send_owner_admin_notice(
                        chat_id,
                        f"{_PROTECT_HEADER}Collaborator access denied for user {target_id}.",
                    )
                    if pending and pending.get("chat_id"):
                        try:
                            target_chat = int(str(pending.get("chat_id")))
                            await self._send_owner_admin_notice(
                                target_chat,
                                f"{_PROTECT_HEADER}Access denied. Contact owner if needed.",
                            )
                        except Exception:
                            pass
                    continue
                elif is_owner and cmd_base in _LOCAL_UNLOCK_COMMANDS:
                    target_id = self._extract_owner_target_resolved(text)
                    if not target_id:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}Usage: /unlock <telegram_user_id>",
                        )
                        continue
                    if self._lockdown is None:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}Progressive lockdown module unavailable.",
                        )
                        continue
                    unlocked = self._lockdown.reset(target_id)
                    if unlocked:
                        self._runtime_revoked_collaborators.discard(target_id)
                        self._suspended_drop_notice_until.pop(target_id, None)
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}Session unlocked for user {target_id}. Lockdown state cleared.",
                        )
                    else:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}User {target_id} had no active lockdown state.",
                        )
                    continue
                elif is_owner and cmd_base in _LOCAL_LOCKED_COMMANDS:
                    if self._lockdown is None:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}Progressive lockdown module unavailable.",
                        )
                        continue
                    statuses = self._lockdown.all_statuses()
                    active = [s for s in statuses if s["level"] != "normal"]
                    if not active:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}No active lockdowns.",
                        )
                        continue
                    lines = [f"{_PROTECT_HEADER}\U0001f512 Lockdown Status\n"]
                    for s in active:
                        uid = s["user_id"]
                        level = s["level"].upper()
                        n = s["block_count"]
                        since_ts = s.get("suspended_at") or s.get("last_block_ts") or 0.0
                        since_str = (
                            _dt.datetime.fromtimestamp(since_ts, tz=_dt.timezone.utc).strftime(
                                "%H:%M UTC"
                            )
                            if since_ts
                            else "unknown"
                        )
                        label = _KNOWN_COLLABORATOR_LABELS.get(uid, uid)
                        lines.append(
                            f"User {uid} ({label}) — {level} ({n} blocks, since {since_str})"
                        )
                    lines.append("\nUse /unlock <user_id> to restore access.")
                    await self._send_owner_admin_notice(chat_id, "\n".join(lines))
                    continue
                elif is_owner and cmd_base in _LOCAL_GRANT_IMMUNITY_COMMANDS:
                    target_id = self._extract_owner_target_resolved(text)
                    if not target_id:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}Usage: /gi <telegram_user_id|name> [duration]\n"
                            "Duration examples: 1h, 30m, 2h30m. Omit for default "
                            f"({int(self._immunity_default_ttl_seconds // 3600)}h).",
                        )
                        continue
                    # Parse optional duration from trailing token (e.g. "1h", "30m", "2h30m")
                    _ttl = self._immunity_default_ttl_seconds
                    _parts = text.strip().split()
                    if len(_parts) >= 3:
                        _dur_str = _parts[-1].lower()
                        _dur_match = re.fullmatch(r"(?:(\d+)h)?(?:(\d+)m)?", _dur_str)
                        if _dur_match and (_dur_match.group(1) or _dur_match.group(2)):
                            _h = int(_dur_match.group(1) or 0)
                            _m = int(_dur_match.group(2) or 0)
                            _ttl = float(_h * 3600 + _m * 60)
                    _expiry = time.time() + _ttl if _ttl > 0 else 0.0
                    self._immune_users[target_id] = _expiry
                    label = _KNOWN_COLLABORATOR_LABELS.get(target_id, target_id)
                    _expiry_str = (
                        _dt.datetime.fromtimestamp(_expiry, tz=_dt.timezone.utc).strftime(
                            "%H:%M UTC"
                        )
                        if _expiry
                        else "no expiry"
                    )
                    logger.info(
                        "IMMUNITY GRANTED: owner=%s target=%s (%s) ttl=%.0fs expires=%s",
                        user_id,
                        target_id,
                        label,
                        _ttl,
                        _expiry_str,
                    )
                    await self._send_owner_admin_notice(
                        chat_id,
                        f"{_PROTECT_HEADER}\U0001f6e1\ufe0f Immunity granted to {label} ({target_id}). "
                        f"Security blocks and rate limiting disabled. Expires: {_expiry_str}.",
                    )
                    continue
                elif is_owner and cmd_base in _LOCAL_REVOKE_IMMUNITY_COMMANDS:
                    target_id = self._extract_owner_target_resolved(text)
                    if not target_id:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}Usage: /ri <telegram_user_id|name>",
                        )
                        continue
                    removed = target_id in self._immune_users
                    self._immune_users.pop(target_id, None)
                    label = _KNOWN_COLLABORATOR_LABELS.get(target_id, target_id)
                    if removed:
                        logger.info(
                            "IMMUNITY REVOKED: owner=%s target=%s (%s)",
                            user_id,
                            target_id,
                            label,
                        )
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}Immunity revoked for {label} ({target_id}). "
                            "Normal security enforcement restored.",
                        )
                    else:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}{label} ({target_id}) did not have immunity.",
                        )
                    continue
                elif is_owner and cmd_base in _LOCAL_IMMUNE_COMMANDS:
                    # Purge expired entries before listing
                    _now_ts = time.time()
                    self._immune_users = {
                        uid: exp
                        for uid, exp in self._immune_users.items()
                        if exp == 0.0 or _now_ts < exp
                    }
                    if not self._immune_users:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}No users currently have immunity.",
                        )
                        continue
                    lines = [f"{_PROTECT_HEADER}\U0001f6e1\ufe0f Immune Users\n"]
                    for uid, exp in sorted(self._immune_users.items()):
                        label = _KNOWN_COLLABORATOR_LABELS.get(uid, uid)
                        exp_str = (
                            _dt.datetime.fromtimestamp(exp, tz=_dt.timezone.utc).strftime(
                                "%H:%M UTC"
                            )
                            if exp
                            else "no expiry"
                        )
                        lines.append(f"  {uid} ({label}) — expires {exp_str}")
                    lines.append("\nUse /ri <user_id> to revoke immunity.")
                    await self._send_owner_admin_notice(chat_id, "\n".join(lines))
                    continue
                elif is_owner and cmd_base in _LOCAL_ADD_COLLAB_COMMANDS:
                    target_id = self._extract_owner_target_resolved(text)
                    if not target_id:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}Usage: /addcollab <telegram_user_id|name>",
                        )
                        continue
                    if target_id == user_id:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}Owner access is already active.",
                        )
                        continue
                    pending = self._pending_collaborator_requests.pop(target_id, None)
                    self._runtime_revoked_collaborators.discard(target_id)
                    if self._rbac and target_id not in {
                        str(uid) for uid in (self._rbac.collaborator_user_ids or [])
                    }:
                        self._rbac.collaborator_user_ids = list(
                            self._rbac.collaborator_user_ids or []
                        ) + [target_id]
                    persist_approved_collaborator(target_id)
                    await self._send_owner_admin_notice(
                        chat_id,
                        f"{_PROTECT_HEADER}Collaborator added: {target_id}",
                    )
                    if pending and pending.get("chat_id"):
                        try:
                            target_chat = int(str(pending.get("chat_id")))
                            await self._send_owner_admin_notice(
                                target_chat,
                                f"{_PROTECT_HEADER}Access approved. You can continue in collaborator mode.",
                            )
                        except Exception:
                            pass
                    continue
                elif is_owner and cmd_base in _LOCAL_RESTORE_COLLABS_COMMANDS:
                    if not self._rbac:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}RBAC unavailable.",
                        )
                        continue
                    defaults = [
                        uid
                        for uid in RBACConfig().collaborator_user_ids
                        if str(uid) != str(user_id)
                    ]
                    merged: list[str] = []
                    seen: set[str] = set()
                    for uid in list(self._rbac.collaborator_user_ids or []) + defaults:
                        s = str(uid).strip()
                        if not s or s in seen or s == str(user_id):
                            continue
                        seen.add(s)
                        merged.append(s)
                    self._rbac.collaborator_user_ids = merged
                    for uid in defaults:
                        self._runtime_revoked_collaborators.discard(str(uid))
                    await self._send_owner_admin_notice(
                        chat_id,
                        (
                            f"{_PROTECT_HEADER}"
                            f"Restored collaborators: {len(defaults)} default IDs active.\n"
                            f"Current list: {', '.join(self._rbac.collaborator_user_ids)}"
                        ),
                    )
                    continue
                elif cmd_base in _LOCAL_GROUPS_COMMANDS and (is_owner or is_collaborator):
                    await self._handle_groups_command(chat_id, user_id)
                    continue
                elif cmd_base in _LOCAL_GROUPINFO_COMMANDS and (is_owner or is_collaborator):
                    tokens = normalize_input(text).strip().split(None, 1)
                    group_id = tokens[1].strip() if len(tokens) > 1 else ""
                    await self._handle_groupinfo_command(chat_id, user_id, group_id)
                    continue
                elif cmd_base in _LOCAL_PROJECTS_COMMANDS and (is_owner or is_collaborator):
                    await self._handle_projects_command(chat_id, user_id)
                    continue
                elif is_owner and cmd_base in _LOCAL_ADDTOGROUP_COMMANDS:
                    tokens = normalize_input(text).strip().split(None, 2)
                    uid_arg = tokens[1].strip() if len(tokens) > 1 else ""
                    gid_arg = tokens[2].strip() if len(tokens) > 2 else ""
                    await self._handle_addtogroup_command(chat_id, user_id, uid_arg, gid_arg)
                    continue
                elif (
                    is_owner
                    or (
                        is_collaborator
                        and self._rbac
                        and self._rbac.group_admin_ids.get(
                            next(
                                (
                                    g
                                    for g in (
                                        self._teams_config.groups if self._teams_config else {}
                                    )
                                ),
                                "",
                            )
                        )
                        == user_id
                    )
                ) and cmd_base in _LOCAL_RMFROMGROUP_COMMANDS:
                    tokens = normalize_input(text).strip().split(None, 2)
                    uid_arg = tokens[1].strip() if len(tokens) > 1 else ""
                    gid_arg = tokens[2].strip() if len(tokens) > 2 else ""
                    await self._handle_rmfromgroup_command(chat_id, user_id, uid_arg, gid_arg)
                    continue
                elif is_owner and cmd_base in _LOCAL_SETMODE_COMMANDS:
                    tokens = normalize_input(text).strip().split(None, 2)
                    target_arg = tokens[1].strip() if len(tokens) > 1 else ""
                    mode_arg = tokens[2].strip() if len(tokens) > 2 else ""
                    await self._handle_setmode_command(chat_id, user_id, target_arg, mode_arg)
                    continue
                elif is_owner and cmd_base in _LOCAL_EGRESS_COMMANDS:
                    from gateway.ingest_api.state import app_state as _eq_state

                    _eq = getattr(_eq_state, "egress_approval_queue", None)
                    tokens = normalize_input(text).strip().split(None, 2)
                    # tokens[0] = "/egress", tokens[1] = subcommand, tokens[2] = arg
                    subcmd = tokens[1].lower() if len(tokens) > 1 else "list"
                    if subcmd == "list":
                        if _eq:
                            rules = await _eq.get_all_rules()
                            perm = rules.get("permanent_rules", [])
                            sess = rules.get("session_rules", [])
                            lines = [f"{_PROTECT_HEADER}*Egress Rules*\n"]
                            if perm:
                                lines.append("*Permanent:*")
                                for r in perm:
                                    lines.append(f"  {r['action'].upper()}  `{r['domain']}`")
                            else:
                                lines.append("*Permanent:* none")
                            if sess:
                                lines.append("\n*Session:*")
                                for r in sess:
                                    lines.append(f"  {r['action'].upper()}  `{r['domain']}`")
                            else:
                                lines.append("\n*Session:* none")
                            lines.append("\nUse `/egress revoke <domain>` to remove a rule.")
                            await self._send_owner_admin_notice(chat_id, "\n".join(lines))
                        else:
                            await self._send_owner_admin_notice(
                                chat_id,
                                f"{_PROTECT_HEADER}Egress approval queue not available.",
                            )
                    elif subcmd in ("allow", "pre-approve") and len(tokens) > 2:
                        target_domain = tokens[2].strip()
                        # Optional duration: 1h, 4h, 24h, forever (default: forever)
                        duration_arg = tokens[3].strip().lower() if len(tokens) > 3 else "forever"
                        from gateway.security.egress_approval import ApprovalMode

                        _mode = (
                            ApprovalMode.SESSION
                            if duration_arg not in ("forever", "permanent")
                            else ApprovalMode.PERMANENT
                        )
                        if _eq:
                            added = await _eq.add_rule(target_domain, "allow", _mode)
                            if added:
                                mode_label = (
                                    "session" if _mode == ApprovalMode.SESSION else "permanent"
                                )
                                await self._send_owner_admin_notice(
                                    chat_id,
                                    (
                                        f"{_PROTECT_HEADER}Egress rule added.\n"
                                        f"Domain: `{target_domain}`\n"
                                        f"Action: ALLOW ({mode_label})\n"
                                        "The bot may now connect to this domain."
                                    ),
                                )
                            else:
                                await self._send_owner_admin_notice(
                                    chat_id,
                                    f"{_PROTECT_HEADER}Failed to add rule for `{target_domain}`.",
                                )
                        else:
                            await self._send_owner_admin_notice(
                                chat_id,
                                f"{_PROTECT_HEADER}Egress approval queue not available.",
                            )
                    elif subcmd == "revoke" and len(tokens) > 2:
                        target_domain = tokens[2].strip()
                        if _eq:
                            removed = await _eq.remove_rule(target_domain)
                            if removed:
                                await self._send_owner_admin_notice(
                                    chat_id,
                                    (
                                        f"{_PROTECT_HEADER}Egress rule removed.\n"
                                        f"Domain: `{target_domain}`\n"
                                        "Future requests for this domain will require re-approval."
                                    ),
                                )
                            else:
                                await self._send_owner_admin_notice(
                                    chat_id,
                                    (
                                        f"{_PROTECT_HEADER}No rule found for `{target_domain}`.\n"
                                        "Use `/egress list` to see active rules."
                                    ),
                                )
                        else:
                            await self._send_owner_admin_notice(
                                chat_id,
                                f"{_PROTECT_HEADER}Egress approval queue not available.",
                            )
                    else:
                        await self._send_owner_admin_notice(
                            chat_id,
                            (
                                f"{_PROTECT_HEADER}*Egress Firewall Commands*\n\n"
                                "`/egress list` — show all allow/deny rules\n"
                                "`/egress allow <domain> [forever|session]` — pre-approve a domain\n"
                                "`/egress revoke <domain>` — remove a rule\n"
                            ),
                        )
                    continue
                elif is_owner and cmd_base in _LOCAL_DELEGATE_COMMANDS:
                    # /delegate <uid|alias> <privilege> <duration>
                    # e.g. /delegate brett egress_approval 8h
                    from gateway.ingest_api.state import app_state as _del_state

                    _del_mgr = getattr(_del_state, "delegation_manager", None)
                    _parts = normalize_input(text).strip().split()
                    # _parts: ["/delegate", uid, privilege, duration]
                    if len(_parts) < 4:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}Usage: /delegate <user_id|name> <privilege> <duration>\n"
                            "Privileges: egress_approval, user_management\n"
                            "Duration examples: 1h, 8h, 24h (max 72h)\n"
                            "Example: /delegate brett egress_approval 8h",
                        )
                        continue
                    _del_target_raw = _parts[1]
                    _del_priv_raw = _parts[2].lower()
                    _del_dur_raw = _parts[3].lower()
                    # Resolve target
                    _del_target = (
                        self._extract_owner_target_resolved(
                            f"/delegate {_del_target_raw} {_del_priv_raw} {_del_dur_raw}"
                        )
                        or _del_target_raw
                    )
                    # Parse duration
                    _dur_match = re.fullmatch(r"(?:(\d+)h)?(?:(\d+)m)?", _del_dur_raw)
                    if not _dur_match or not (_dur_match.group(1) or _dur_match.group(2)):
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}Invalid duration: `{_del_dur_raw}`. Use e.g. 8h, 30m, 2h30m (max 72h).",
                        )
                        continue
                    _dur_h = float(_dur_match.group(1) or 0)
                    _dur_m = float(_dur_match.group(2) or 0)
                    _dur_hours = _dur_h + _dur_m / 60.0
                    if _del_mgr is None:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}DelegationManager unavailable.",
                        )
                        continue
                    try:
                        from gateway.security.delegation import DelegationPrivilege

                        _priv = DelegationPrivilege(_del_priv_raw)
                        _delegation = _del_mgr.delegate(
                            owner_id=user_id,
                            to_user_id=_del_target,
                            privilege=_priv,
                            duration_hours=_dur_hours,
                        )
                        _label = _KNOWN_COLLABORATOR_LABELS.get(_del_target, _del_target)
                        _exp_str = _dt.datetime.fromtimestamp(
                            _delegation.expires_at, tz=_dt.timezone.utc
                        ).strftime("%Y-%m-%d %H:%M UTC")
                        logger.info(
                            "DELEGATION CREATED: owner=%s target=%s priv=%s expires=%s",
                            user_id,
                            _del_target,
                            _del_priv_raw,
                            _exp_str,
                        )
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}\U0001f511 Delegation granted.\n"
                            f"User: {_label} ({_del_target})\n"
                            f"Privilege: {_del_priv_raw}\n"
                            f"Expires: {_exp_str}",
                        )
                    except Exception as _del_exc:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}Delegation failed: {_del_exc}",
                        )
                    continue
                elif is_owner and cmd_base in _LOCAL_DELEGATIONS_COMMANDS:
                    from gateway.ingest_api.state import app_state as _del_state

                    _del_mgr = getattr(_del_state, "delegation_manager", None)
                    if not _del_mgr:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}DelegationManager unavailable.",
                        )
                        continue
                    _del_mgr.cleanup_expired()
                    _active = _del_mgr.get_active_delegations()
                    if not _active:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}No active privilege delegations.",
                        )
                        continue
                    lines = [f"{_PROTECT_HEADER}\U0001f511 Active Delegations\n"]
                    for _d in _active:
                        _label = _KNOWN_COLLABORATOR_LABELS.get(_d.delegated_to, _d.delegated_to)
                        _exp_str = _dt.datetime.fromtimestamp(
                            _d.expires_at, tz=_dt.timezone.utc
                        ).strftime("%H:%M UTC")
                        lines.append(
                            f"  {_label} ({_d.delegated_to}) — {_d.privilege} until {_exp_str}"
                        )
                    lines.append("\nUse /revoke_delegation <user_id> <privilege> to revoke.")
                    await self._send_owner_admin_notice(chat_id, "\n".join(lines))
                    continue
                elif is_owner and cmd_base in _LOCAL_REVOKE_DELEGATION_COMMANDS:
                    from gateway.ingest_api.state import app_state as _del_state

                    _del_mgr = getattr(_del_state, "delegation_manager", None)
                    _parts = normalize_input(text).strip().split()
                    # _parts: ["/revoke-delegation", uid, privilege(optional)]
                    if len(_parts) < 2:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}Usage: /revoke_delegation <user_id|name> [privilege]\n"
                            "Privileges: egress_approval, user_management\n"
                            "Omit privilege to revoke all delegations for the user.",
                        )
                        continue
                    _rd_target_raw = _parts[1]
                    _rd_priv_raw = _parts[2].lower() if len(_parts) > 2 else None
                    _rd_target = (
                        self._extract_owner_target_resolved(f"/revoke_delegation {_rd_target_raw}")
                        or _rd_target_raw
                    )
                    if not _del_mgr:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}DelegationManager unavailable.",
                        )
                        continue
                    try:
                        if _rd_priv_raw:
                            from gateway.security.delegation import DelegationPrivilege

                            _priv = DelegationPrivilege(_rd_priv_raw)
                            _revoked = _del_mgr.revoke(user_id, _rd_target, _priv)
                            _count = 1 if _revoked else 0
                        else:
                            _count = _del_mgr.revoke_all_for_user(user_id, _rd_target)
                        _label = _KNOWN_COLLABORATOR_LABELS.get(_rd_target, _rd_target)
                        if _count:
                            logger.info(
                                "DELEGATION REVOKED: owner=%s target=%s priv=%s count=%d",
                                user_id,
                                _rd_target,
                                _rd_priv_raw or "all",
                                _count,
                            )
                            await self._send_owner_admin_notice(
                                chat_id,
                                f"{_PROTECT_HEADER}\U0001f511 Revoked {_count} delegation(s) for {_label} ({_rd_target}).",
                            )
                        else:
                            await self._send_owner_admin_notice(
                                chat_id,
                                f"{_PROTECT_HEADER}No active delegations found for {_label} ({_rd_target}).",
                            )
                    except Exception as _rd_exc:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}Revocation failed: {_rd_exc}",
                        )
                elif is_owner and cmd_base in _LOCAL_EGRESS_ALLOW_COMMANDS:
                    # Shorthand: /egress-allow <domain> [forever|session]
                    from gateway.ingest_api.state import app_state as _ea_state

                    _eq2 = getattr(_ea_state, "egress_approval_queue", None)
                    tokens2 = normalize_input(text).strip().split(None, 2)
                    if len(tokens2) < 2:
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}Usage: /egress-allow <domain> [forever|session]",
                        )
                    else:
                        target_domain2 = tokens2[1].strip()
                        duration2 = tokens2[2].strip().lower() if len(tokens2) > 2 else "forever"
                        from gateway.security.egress_approval import (
                            ApprovalMode as _AM2,
                        )

                        _mode2 = (
                            _AM2.SESSION
                            if duration2 not in ("forever", "permanent")
                            else _AM2.PERMANENT
                        )
                        if _eq2:
                            added2 = await _eq2.add_rule(target_domain2, "allow", _mode2)
                            mode_label2 = "session" if _mode2 == _AM2.SESSION else "permanent"
                            if added2:
                                await self._send_owner_admin_notice(
                                    chat_id,
                                    (
                                        f"{_PROTECT_HEADER}Egress rule added.\n"
                                        f"Domain: `{target_domain2}`\n"
                                        f"Action: ALLOW ({mode_label2})\n"
                                        "The bot may now connect to this domain."
                                    ),
                                )
                            else:
                                await self._send_owner_admin_notice(
                                    chat_id,
                                    f"{_PROTECT_HEADER}Failed to add rule for `{target_domain2}`.",
                                )
                        else:
                            await self._send_owner_admin_notice(
                                chat_id,
                                f"{_PROTECT_HEADER}Egress approval queue not available.",
                            )
                    continue
                elif cmd_base in _LOCAL_SETNAME_COMMANDS:
                    # /setname <display name> — collaborators and owner may set display name
                    tokens_sn = normalize_input(text).strip().split(None, 1)
                    if len(tokens_sn) < 2 or not tokens_sn[1].strip():
                        reply_sn = (
                            "Usage: `/setname <display name>`\n"
                            "Example: `/setname Brett`\n\n"
                            "Your display name will appear in the SOC activity log.\n"
                            "Use `/setname clear` to reset to your Telegram name."
                        )
                        if is_owner:
                            await self._send_owner_admin_notice(
                                chat_id, f"{_PROTECT_HEADER}{reply_sn}"
                            )
                        else:
                            await self._send_telegram_text(int(chat_id), reply_sn)
                    else:
                        new_name = tokens_sn[1].strip()[:64]
                        if new_name.lower() == "clear":
                            self._custom_display_names.pop(user_id, None)
                            msg_sn = "Display name cleared. Your Telegram name will be used."
                        else:
                            self._custom_display_names[user_id] = new_name
                            msg_sn = f"Display name set to: {new_name}"
                        # Persist to disk
                        try:
                            import json as _json_sn

                            with open(self._display_names_path, "w", encoding="utf-8") as _dnf_sn:
                                _json_sn.dump(self._custom_display_names, _dnf_sn)
                        except Exception as _sne:
                            logger.warning("Could not persist display names: %s", _sne)
                        if is_owner:
                            await self._send_owner_admin_notice(
                                chat_id, f"{_PROTECT_HEADER}{msg_sn}"
                            )
                        else:
                            await self._send_telegram_text(int(chat_id), msg_sn)
                    continue
                if local_handler is not None:
                    update_id = update.get("update_id")
                    message_id = message.get("message_id")
                    if update_id is None:
                        dedupe_identity = f"msg:{message_id}"
                    else:
                        dedupe_identity = f"upd:{update_id}"
                    dedupe_key = f"{chat_id}:{dedupe_identity}:{cmd_base}"
                    now = time.time()
                    if len(self._handled_local_command_update_ids) > 4096:
                        self._handled_local_command_update_ids = {
                            k: v
                            for k, v in self._handled_local_command_update_ids.items()
                            if v > now
                        }
                    if self._handled_local_command_update_ids.get(dedupe_key, 0.0) <= now:
                        await local_handler(chat_id)
                        self._handled_local_command_update_ids[dedupe_key] = (
                            now + self._local_command_dedupe_ttl_seconds
                        )
                        logger.info(
                            "Handled local %s command for user %s (update_id=%s)",
                            local_label,
                            user_id,
                            update_id,
                        )
                    # Drop update so bot runtime never sees this command.
                    continue
                if self._looks_like_model_status_question(text):
                    update_id = update.get("update_id")
                    message_id = message.get("message_id")
                    if update_id is None:
                        dedupe_identity = f"msg:{message_id}"
                    else:
                        dedupe_identity = f"upd:{update_id}"
                    dedupe_key = f"{chat_id}:{dedupe_identity}:model-question"
                    now = time.time()
                    if self._handled_local_command_update_ids.get(dedupe_key, 0.0) <= now:
                        await self._send_local_model_notice(chat_id)
                        self._handled_local_command_update_ids[dedupe_key] = (
                            now + self._local_command_dedupe_ttl_seconds
                        )
                        logger.info(
                            "Handled local model question for user %s (update_id=%s)",
                            user_id,
                            update_id,
                        )
                    # Drop update so bot runtime never sees this query.
                    continue

            # ── Collaborator command blocking ─────────────────────────────────
            # Block owner-only slash commands before they reach the bot.
            if is_collaborator and chat_id:
                # ── Group chat context pass-through ──────────────────────────
                # In group chats, ALL messages are forwarded to the bot so it
                # can maintain conversational context.  The DM-focused content
                # guards below (blocked commands, file queries, local_only) are
                # not applied to group messages; response suppression is handled
                # on the outbound side via _group_response_eligible.
                if (
                    self._group_mention_only
                    and self._bot_username
                    and self._is_group_message(message)
                ):
                    filtered_updates.append(update)
                    continue

                cmd_base = self._normalize_command_token(text)
                if cmd_base in _COLLABORATOR_BLOCKED_COMMANDS:
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason=f"Blocked command: {cmd_base}",
                        source="telegram_command_block",
                    )
                    logger.info(
                        "Collaborator %s attempted blocked command %r — rejecting",
                        user_id,
                        cmd_base,
                    )
                    await self._notify_collaborator_command_blocked(chat_id, cmd_base)
                    # Drop the update — do not forward to bot
                    continue
                if (
                    cmd_base.startswith("/")
                    and cmd_base not in _COLLABORATOR_ALLOWED_SLASH_COMMANDS
                ):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason=f"Blocked unapproved collaborator slash command: {cmd_base}",
                        source="telegram_unknown_command_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "restricted-command")
                    continue
                if self._looks_like_tool_payload_text(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator raw tool-payload request",
                        source="telegram_tool_payload_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "tool-payload")
                    continue
                if self._looks_like_approval_token_probe(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator approval-token probe",
                        source="telegram_approval_token_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "restricted-command")
                    continue
                if self._looks_like_approval_action_request(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator approval-action request",
                        source="telegram_approval_action_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "restricted-command")
                    continue
                if self._looks_like_cross_tenant_data_probe(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator cross-tenant data probe",
                        source="telegram_cross_tenant_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "file-access")
                    continue
                if self._looks_like_guardrail_modification_request(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator guardrail-modification request",
                        source="telegram_guardrail_mod_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "restricted-command")
                    continue
                if self._looks_like_system_prompt_probe(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator system-prompt probe",
                        source="telegram_system_prompt_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "restricted-command")
                    continue
                if self._looks_like_tool_trace_request(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator tool-trace request",
                        source="telegram_tool_trace_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "tool-payload")
                    continue
                if self._looks_like_sensitive_path_probe(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator sensitive-path probe",
                        source="telegram_sensitive_path_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "file-access")
                    continue
                if self._looks_like_path_traversal_request(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator path-traversal request",
                        source="telegram_path_traversal_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "file-access")
                    continue
                if self._looks_like_metadata_endpoint_probe(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator metadata-endpoint probe",
                        source="telegram_metadata_endpoint_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "secret-access")
                    continue
                if self._looks_like_secret_value_request(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator secret-value request",
                        source="telegram_secret_value_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "secret-access")
                    continue
                if self._looks_like_env_secret_probe(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator environment-secret probe",
                        source="telegram_env_secret_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "secret-access")
                    continue
                if self._looks_like_internal_network_probe(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator internal-network probe",
                        source="telegram_internal_network_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "web-access")
                    continue
                if self._looks_like_unsafe_scheme_request(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator unsafe-scheme request",
                        source="telegram_unsafe_scheme_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "web-access")
                    continue
                if self._looks_like_allowlist_bypass_request(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator allowlist-bypass request",
                        source="telegram_allowlist_bypass_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "web-access")
                    continue
                if self._looks_like_unicode_obfuscation_bypass_request(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator unicode-obfuscation bypass request",
                        source="telegram_unicode_bypass_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "restricted-command")
                    continue
                if self._looks_like_web_access_request(text):
                    try:
                        has_encoded_controls = bool(
                            isinstance(original_transport_text, str)
                            and re.search(
                                r"%(?:0[0-9a-fA-F]|1[0-9a-fA-F]|7[fF])",
                                original_transport_text,
                            )
                        )
                        requested_url = (
                            self._extract_first_egress_target(text)
                            if not has_encoded_controls
                            else None
                        )
                        if requested_url and not preflight_egress_queued:
                            owner_chat = (
                                str(getattr(self._rbac, "owner_user_id", "")).strip()
                                if self._rbac
                                else ""
                            )
                            await self._trigger_web_fetch_approval(
                                owner_chat or str(chat_id or ""),
                                {"url": requested_url},
                            )
                            await self._send_telegram_text(
                                chat_id, _COLLABORATOR_EGRESS_PENDING_NOTICE
                            )
                        else:
                            await self._notify_collaborator_command_blocked(chat_id, "web-access")
                    except Exception as _wf:
                        logger.debug("Collaborator web-access preflight error (non-fatal): %s", _wf)
                        await self._notify_collaborator_command_blocked(chat_id, "web-access")
                    continue
                if self._looks_like_file_metadata_question(text):
                    await self._send_collaborator_safe_info_response(chat_id, text)
                    continue
                if self._looks_like_file_query(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator file-query request",
                        source="telegram_file_query_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "file-access")
                    continue
                if self._looks_like_incremental_exfil_request(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator incremental-exfil request",
                        source="telegram_incremental_exfil_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "file-access")
                    continue
                if self._looks_like_encoded_exfil_request(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator encoded-exfil request",
                        source="telegram_encoded_exfil_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "file-access")
                    continue
                if self._looks_like_hidden_channel_exfil_request(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator hidden-channel exfil request",
                        source="telegram_hidden_channel_exfil_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "file-access")
                    continue
                if self._looks_like_archive_exfil_request(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator archive-exfil request",
                        source="telegram_archive_exfil_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "file-access")
                    continue
                if self._looks_like_cross_user_messaging_request(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator cross-user messaging request",
                        source="telegram_cross_user_message_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "restricted-command")
                    continue
                if self._looks_like_scheduler_or_autorun_request(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator scheduler/autorun request",
                        source="telegram_scheduler_autorun_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "restricted-command")
                    continue
                if self._looks_like_model_switch_request(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator model-switch request",
                        source="telegram_model_switch_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "restricted-command")
                    continue
                if self._looks_like_service_control_request(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator service-control request",
                        source="telegram_service_control_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "restricted-command")
                    continue
                if self._looks_like_plugin_discovery_request(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator plugin-discovery request",
                        source="telegram_plugin_discovery_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "restricted-command")
                    continue
                if self._looks_like_pairing_or_access_probe(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator pairing/access probe",
                        source="telegram_pairing_access_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "restricted-command")
                    continue
                if self._looks_like_execution_request(text):
                    if self._looks_like_hypothetical_execution_question(text):
                        await self._send_collaborator_safe_info_response(chat_id, text)
                    else:
                        self._stats["messages_blocked"] += 1
                        self._quarantine_blocked_message(
                            user_id=user_id,
                            chat_id=chat_id,
                            text=text,
                            reason="Blocked collaborator execution request",
                            source="telegram_execution_request_block",
                        )
                        await self._notify_collaborator_command_blocked(
                            chat_id, "execution-request"
                        )
                    continue
                if self._looks_like_obfuscated_command_probe(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator obfuscated-command probe",
                        source="telegram_obfuscated_command_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "execution-request")
                    continue
                if self._looks_like_memory_access_request(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator memory-access request",
                        source="telegram_memory_access_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "file-access")
                    continue
                if self._looks_like_collaborator_privacy_query(text):
                    await self._send_collaborator_safe_info_response(chat_id, text)
                    continue
                if self._looks_like_identity_enumeration_query(text):
                    await self._send_collaborator_safe_info_response(chat_id, text)
                    continue
                if self._looks_like_command_enumeration_query(text):
                    await self._send_collaborator_safe_info_response(chat_id, text)
                    continue
                if self._looks_like_approval_queue_probe(text):
                    await self._send_collaborator_safe_info_response(chat_id, text)
                    continue
                if self._looks_like_policy_bypass_request(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator policy-bypass request",
                        source="telegram_policy_bypass_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "restricted-command")
                    continue
                if self._looks_like_log_access_request(text):
                    self._stats["messages_blocked"] += 1
                    self._quarantine_blocked_message(
                        user_id=user_id,
                        chat_id=chat_id,
                        text=text,
                        reason="Blocked collaborator log-access request",
                        source="telegram_log_access_block",
                    )
                    await self._notify_collaborator_command_blocked(chat_id, "file-access")
                    continue
                if self._looks_like_safe_collaborator_info_query(text):
                    await self._send_collaborator_safe_info_response(chat_id, text)
                    continue
                # ── Security pipeline / sanitizer (collaborator path) ────────────
                # When a pipeline or sanitizer is configured, run it as the
                # authoritative security gatekeeper BEFORE collab_mode routing.
                # Clean messages are forwarded to the bot; blocked messages are
                # dropped. This ensures getUpdates inbound messages receive the
                # same pipeline treatment as webhook messages.
                if self.pipeline and text:
                    try:
                        _pipe_result = await self.pipeline.process_inbound(
                            message=text,
                            source="telegram",
                            metadata={"user_id": user_id, "chat_id": chat_id},
                            skip_context_guard=True,
                        )
                        if _pipe_result.blocked:
                            self._stats["messages_blocked"] += 1
                            logger.warning(
                                "Pipeline blocked Telegram message from collaborator %s: %s",
                                user_id,
                                _pipe_result.block_reason,
                            )
                            self._quarantine_blocked_message(
                                user_id=user_id,
                                chat_id=chat_id,
                                text=text,
                                reason=_pipe_result.block_reason or "Pipeline blocked message",
                                source="telegram_pipeline_block",
                            )
                            if chat_id:
                                await self._notify_user_blocked(chat_id, _pipe_result.block_reason)
                            continue
                        # Pipeline passed — apply any PII-sanitized text
                        _pipe_sanitized = _pipe_result.sanitized_message
                        if _pipe_sanitized and _pipe_sanitized != text:
                            self._stats["messages_sanitized"] += 1
                            if "message" in update:
                                update["message"]["text"] = _pipe_sanitized
                            elif "edited_message" in update:
                                update["edited_message"]["text"] = _pipe_sanitized
                    except Exception as _pipe_exc:
                        logger.error(
                            "Pipeline error for collaborator Telegram message from %s: %s",
                            user_id,
                            _pipe_exc,
                        )
                        self._stats["messages_blocked"] += 1
                        if chat_id:
                            await self._notify_user_blocked(chat_id, "Security pipeline error")
                        continue
                    # Pipeline cleared — forward to bot, skip collab_mode local routing
                    filtered_updates.append(update)
                    continue
                elif self.sanitizer and text:
                    try:
                        _san_result = await self.sanitizer.sanitize(text)
                        if _san_result.entity_types_found:
                            self._stats["messages_sanitized"] += 1
                            if "message" in update:
                                update["message"]["text"] = _san_result.sanitized_content
                            elif "edited_message" in update:
                                update["edited_message"]["text"] = _san_result.sanitized_content
                    except Exception as _san_exc:
                        logger.error(
                            "PII sanitization error for collaborator Telegram message: %s", _san_exc
                        )
                    # Sanitizer done — forward to bot, skip collab_mode local routing
                    filtered_updates.append(update)
                    continue
                # Deterministic collaborator handling — resolve per-user collab mode.
                _collab_mode = self._resolve_collaborator_mode(user_id)
                if _collab_mode == "local_only":
                    # Always handle locally (original default behavior).
                    await self._send_collaborator_safe_info_response(chat_id, text)
                    continue
                if _collab_mode == "project_scoped":
                    # Gateway pre-filter: block clearly off-topic messages locally.
                    _user_projects = self._get_user_projects(user_id)
                    if _user_projects and not self._is_within_project_scope(text, _user_projects):
                        await self._send_owner_admin_notice(
                            chat_id,
                            f"{_PROTECT_HEADER}This message is outside your current project scope.\n"
                            "Please keep questions focused on your assigned projects.",
                        )
                        continue
                    # Matching/ambiguous → fall through to bot with project context injection
                    # (handled in middleware pipeline below)
                # _collab_mode == "full_access": forward without restriction

            # ── Middleware pipeline (RBAC, context guard, multi-turn, etc.) ───
            if self.middleware_manager:
                try:
                    request_data = {
                        "message": text,
                        "content_type": "text",
                        "source": "telegram",
                        "headers": {},
                        "user_id": user_id,
                    }
                    result = await self.middleware_manager.process_request(
                        request_data, f"telegram_{user_id}"
                    )
                    if not result.allowed:
                        if is_owner:
                            # Owner messages are logged but never blocked by middleware
                            logger.info(
                                "Middleware would block owner message (%s) — allowing: %s",
                                user_id,
                                result.reason,
                            )
                        else:
                            reason_text = result.reason or ""
                            if (
                                "multi-turn" in reason_text.lower()
                                and self._looks_like_safe_collaborator_info_query(text)
                            ):
                                logger.info(
                                    "Allowing collaborator conceptual query despite multi-turn middleware block (%s)",
                                    user_id,
                                )
                            else:
                                logger.warning(
                                    "Telegram message from %s blocked by middleware: %s",
                                    user_id,
                                    result.reason,
                                )
                                self._stats["messages_blocked"] += 1
                                self._quarantine_blocked_message(
                                    user_id=user_id,
                                    chat_id=chat_id,
                                    text=text,
                                    reason=result.reason or "Middleware blocked message",
                                    source="telegram_middleware_block",
                                )
                                if chat_id:
                                    await self._notify_user_blocked(chat_id, result.reason)
                                blocked_text = (
                                    self._collaborator_safe_notice(
                                        result.reason or "blocked action"
                                    )
                                    if not is_owner
                                    else f"[BLOCKED BY AGENTSHROUD: {result.reason}]"
                                )
                                if "message" in update:
                                    update["message"]["text"] = blocked_text
                                elif "edited_message" in update:
                                    update["edited_message"]["text"] = blocked_text
                                # Drop blocked collaborator message so bot runtime
                                # never receives blocked payloads.
                                continue
                except Exception as e:
                    logger.error(f"Middleware error for telegram message: {e}")

            # ── Security pipeline (prompt injection, PII, heuristic, audit) ──
            # ContextGuard already ran via middleware_manager; skip_context_guard=True avoids double-check.
            if self.pipeline and text:
                try:
                    pipeline_result = await self.pipeline.process_inbound(
                        message=text,
                        source="telegram",
                        metadata={"user_id": user_id, "chat_id": chat_id},
                        skip_context_guard=True,
                    )
                    if pipeline_result.blocked:
                        if is_owner:
                            logger.info(
                                "Pipeline would block owner message (%s) — allowing; reason: %s",
                                user_id,
                                pipeline_result.block_reason,
                            )
                        else:
                            block_reason = pipeline_result.block_reason or ""
                            if (
                                "multi-turn" in block_reason.lower()
                                and self._looks_like_safe_collaborator_info_query(text)
                            ):
                                logger.info(
                                    "Allowing collaborator conceptual query despite multi-turn pipeline block (%s)",
                                    user_id,
                                )
                                filtered_updates.append(update)
                                continue
                            self._stats["messages_blocked"] += 1
                            logger.warning(
                                "Pipeline blocked Telegram message from %s: %s",
                                user_id,
                                pipeline_result.block_reason,
                            )
                            self._quarantine_blocked_message(
                                user_id=user_id,
                                chat_id=chat_id,
                                text=text,
                                reason=pipeline_result.block_reason or "Pipeline blocked message",
                                source="telegram_pipeline_block",
                            )
                            if chat_id:
                                await self._notify_user_blocked(
                                    chat_id, pipeline_result.block_reason
                                )
                            blocked_text = (
                                self._collaborator_safe_notice(
                                    pipeline_result.block_reason or "blocked action"
                                )
                                if not is_owner
                                else f"[BLOCKED BY AGENTSHROUD: {pipeline_result.block_reason}]"
                            )
                            if "message" in update:
                                update["message"]["text"] = blocked_text
                            elif "edited_message" in update:
                                update["edited_message"]["text"] = blocked_text
                            # Drop blocked collaborator message so bot runtime
                            # never receives blocked payloads.
                            continue
                    # Apply sanitized text from pipeline (PII redactions, etc.)
                    sanitized_text = pipeline_result.sanitized_message
                    if sanitized_text != text:
                        self._stats["messages_sanitized"] += 1
                        if "message" in update:
                            update["message"]["text"] = sanitized_text
                            update["message"]["_agentshroud_pii_redacted"] = True
                            update["message"][
                                "_agentshroud_redactions"
                            ] = pipeline_result.pii_redactions
                        elif "edited_message" in update:
                            update["edited_message"]["text"] = sanitized_text
                            update["edited_message"]["_agentshroud_pii_redacted"] = True
                except Exception as exc:
                    logger.error("Pipeline error for Telegram message from %s: %s", user_id, exc)
                    if not is_owner:
                        # Fail-closed: replace message text with block notice, keep in updates list
                        self._stats["messages_blocked"] += 1
                        if chat_id:
                            await self._notify_user_blocked(chat_id, "Security pipeline error")
                        blocked_text = self._collaborator_safe_notice("security pipeline error")
                        if "message" in update:
                            update["message"]["text"] = blocked_text
                        elif "edited_message" in update:
                            update["edited_message"]["text"] = blocked_text
                        # Drop blocked collaborator message so bot runtime
                        # never receives blocked payloads.
                        continue
                    logger.warning("Pipeline error on owner message — allowing through")
            elif self.sanitizer and text:
                # Fallback: direct PII sanitization when pipeline is unavailable
                try:
                    sanitize_result = await self.sanitizer.sanitize(text)
                    if sanitize_result.entity_types_found:
                        self._stats["messages_sanitized"] += 1
                        logger.info(
                            "Telegram message from %s: PII redacted: %s",
                            user_id,
                            sanitize_result.entity_types_found,
                        )
                        if "message" in update:
                            update["message"]["text"] = sanitize_result.sanitized_content
                            update["message"]["_agentshroud_pii_redacted"] = True
                            update["message"]["_agentshroud_redactions"] = list(
                                sanitize_result.entity_types_found
                            )
                        elif "edited_message" in update:
                            update["edited_message"]["text"] = sanitize_result.sanitized_content
                            update["edited_message"]["_agentshroud_pii_redacted"] = True
                except Exception as e:
                    logger.error(f"PII sanitization error for telegram message: {e}")

            filtered_updates.append(update)

        response_data["result"] = filtered_updates
        return response_data

    def _quarantine_blocked_message(
        self,
        user_id: str,
        chat_id: Optional[int],
        text: str,
        reason: str,
        source: str,
    ) -> None:
        """Persist blocked inbound messages for admin review.

        Also records the block in the progressive lockdown counter for this user.
        If the lockdown module raises an escalation alert (owner notification needed),
        it is sent asynchronously without blocking this synchronous call.
        """
        # Progressive lockdown: record this block and check for escalation.
        # Immune users are exempt from lockdown recording (owner-granted, testing only).
        if self._lockdown is not None and not self._is_immune(str(user_id)):
            try:
                action = self._lockdown.record_block(user_id=str(user_id), reason=reason)
                if action.notify_owner and action.notify_text:
                    owner_chat = str(getattr(self._rbac, "owner_user_id", "")).strip()
                    if owner_chat:
                        try:
                            loop = asyncio.get_event_loop()
                            if loop.is_running():
                                loop.create_task(
                                    self._send_telegram_text(owner_chat, action.notify_text)
                                )
                        except Exception as _le:
                            logger.debug("Lockdown owner notify error: %s", _le)
                # Notify the collaborator at each lockdown threshold transition.
                # Only fires once per level (action.notify_owner gates each transition).
                if action.notify_owner and chat_id is not None:
                    _block_count = self._lockdown.get_status(str(user_id)).get("block_count", 0)
                    _level = action.level.value
                    if _level == "suspended":
                        _collab_msg = (
                            f"\U0001f534 Your session has been suspended after {_block_count} security blocks. "
                            "Contact the system owner to restore access."
                        )
                    elif _level == "escalated":
                        _collab_msg = (
                            f"\u26a0\ufe0f Your session is approaching suspension ({_block_count} security blocks). "
                            "Please adjust your approach or contact the system owner."
                        )
                    elif _level == "alert":
                        _collab_msg = (
                            "\u26a0\ufe0f Your session has triggered multiple security blocks. "
                            "Continued attempts may result in a temporary session suspension."
                        )
                    else:
                        _collab_msg = ""
                    if _collab_msg:
                        try:
                            loop = asyncio.get_event_loop()
                            if loop.is_running():
                                loop.create_task(
                                    self._send_telegram_text(int(chat_id), _collab_msg)
                                )
                        except Exception as _ce:
                            logger.debug("Lockdown collab notify error: %s", _ce)
            except Exception as _exc:
                logger.debug("ProgressiveLockdown.record_block error: %s", _exc)

        try:
            from gateway.ingest_api.state import app_state as _app_state

            store = getattr(_app_state, "blocked_message_quarantine", None)
            if store is None:
                store = []
                setattr(_app_state, "blocked_message_quarantine", store)
            store.append(
                {
                    "message_id": str(uuid.uuid4()),
                    "timestamp": time.time(),
                    "user_id": str(user_id),
                    "chat_id": str(chat_id) if chat_id is not None else "",
                    "text": text,
                    "reason": reason,
                    "source": source,
                    "status": "pending",
                    "released_at": None,
                    "released_by": None,
                    "review_note": "",
                }
            )
            if len(store) > 5000:
                del store[: len(store) - 5000]
            self._emit_quarantine_event(
                event_type="quarantine_inbound_blocked",
                summary="Inbound message quarantined",
                details={
                    "user_id": str(user_id),
                    "chat_id": str(chat_id) if chat_id is not None else "",
                    "reason": reason,
                    "source": source,
                },
            )
        except Exception as exc:
            logger.debug("Failed to quarantine blocked message: %s", exc)

    def _quarantine_outbound_block(
        self,
        chat_id: str,
        text: str,
        reason: str,
        source: str,
    ) -> None:
        """Persist blocked outbound messages for admin review."""
        try:
            from gateway.ingest_api.state import app_state as _app_state

            store = getattr(_app_state, "blocked_outbound_quarantine", None)
            if store is None:
                store = []
                setattr(_app_state, "blocked_outbound_quarantine", store)
            store.append(
                {
                    "message_id": str(uuid.uuid4()),
                    "timestamp": time.time(),
                    "chat_id": str(chat_id),
                    "text": text,
                    "reason": reason,
                    "source": source,
                    "status": "pending",
                    "released_at": None,
                    "released_by": None,
                    "review_note": "",
                }
            )
            if len(store) > 5000:
                del store[: len(store) - 5000]
            self._emit_quarantine_event(
                event_type="quarantine_outbound_blocked",
                summary="Outbound message quarantined",
                details={
                    "chat_id": str(chat_id),
                    "reason": reason,
                    "source": source,
                },
            )
        except Exception as exc:
            logger.debug("Failed to quarantine blocked outbound message: %s", exc)

    def _emit_quarantine_event(self, event_type: str, summary: str, details: dict) -> None:
        """Best-effort async event emission for quarantine actions."""
        try:
            from gateway.ingest_api.state import app_state as _app_state

            bus = getattr(_app_state, "event_bus", None)
            if not bus:
                return
            from gateway.ingest_api.event_bus import make_event

            loop = asyncio.get_running_loop()
            loop.create_task(
                bus.emit(
                    make_event(
                        event_type,
                        summary,
                        details,
                        severity="warning",
                    )
                )
            )
        except Exception:
            # No running loop or unavailable event bus: skip quietly.
            return

    async def _send_rate_limit_notice(self, chat_id: int, user_id: Optional[str] = None) -> bool:
        """Notify a collaborator they have exceeded the hourly rate limit."""
        try:
            if self._bot_token:
                limiter_user_id = str(user_id) if user_id else str(chat_id)
                wait_seconds = self._collaborator_rate_limit_retry_after_seconds(limiter_user_id)
                wait_minutes = max(1, math.ceil(wait_seconds / 60.0))
                reset_time_str = time.strftime("%H:%M UTC", time.gmtime(time.time() + wait_seconds))
                msg = (
                    f"{_PROTECT_HEADER}"
                    "Collaborator rate limit reached "
                    f"\\({self._collaborator_rate_limiter.max_requests} messages/hour\\)\\.\n"
                    f"Rate limit resets at {reset_time_str} \\(~{wait_minutes} min\\)\\."
                )
                url = f"{TELEGRAM_API_BASE}/bot{self._bot_token}/sendMessage"
                loop = asyncio.get_event_loop()
                payload = {"chat_id": chat_id, "text": msg, "parse_mode": "MarkdownV2"}
                req = urllib.request.Request(
                    url,
                    data=json.dumps(payload).encode(),
                    headers={"Content-Type": "application/json"},
                )
                try:
                    await loop.run_in_executor(
                        None,
                        lambda: urllib.request.urlopen(req, timeout=5, context=self._ssl_context),
                    )
                    return True
                except Exception:
                    # Fallback: resend without Markdown parse mode to avoid silent
                    # parse failures and ensure collaborator always gets a notice.
                    plain_msg = (
                        f"{_PROTECT_HEADER}"
                        "Collaborator rate limit reached "
                        f"({self._collaborator_rate_limiter.max_requests} messages/hour). "
                        f"Rate limit resets at {reset_time_str} (~{wait_minutes} min)."
                    )
                    fallback_req = urllib.request.Request(
                        url,
                        data=json.dumps({"chat_id": chat_id, "text": plain_msg}).encode(),
                        headers={"Content-Type": "application/json"},
                    )
                    await loop.run_in_executor(
                        None,
                        lambda: urllib.request.urlopen(
                            fallback_req, timeout=5, context=self._ssl_context
                        ),
                    )
                    return True
        except Exception as e:
            logger.warning("Failed to send rate limit notice to chat %s: %s", chat_id, e)
        return False

    def _collaborator_rate_limit_retry_after_seconds(self, user_id: str) -> int:
        """Estimate seconds until collaborator rate limit window opens again."""
        try:
            limiter = self._collaborator_rate_limiter
            now = time.time()
            history = list(getattr(limiter, "requests", {}).get(user_id, []))
            if not history:
                return max(1, int(getattr(limiter, "window_seconds", 3600)))
            earliest = min(float(ts) for ts in history)
            retry_at = earliest + float(getattr(limiter, "window_seconds", 3600))
            return max(1, int(math.ceil(retry_at - now)))
        except Exception:
            return 60

    async def _send_stranger_rate_limit_notice(
        self, chat_id: int, user_id: Optional[str] = None
    ) -> bool:
        """Notify an unknown/unapproved user they have exceeded the access request rate limit."""
        try:
            if not self._bot_token:
                return False
            limiter_user_id = str(user_id) if user_id else str(chat_id)
            limiter = self._stranger_rate_limiter
            now = time.time()
            history = list(getattr(limiter, "requests", {}).get(limiter_user_id, []))
            if history:
                earliest = min(float(ts) for ts in history)
                retry_at_ts = earliest + float(getattr(limiter, "window_seconds", 3600))
            else:
                retry_at_ts = now + float(getattr(limiter, "window_seconds", 3600))
            wait_seconds = max(1, retry_at_ts - now)
            wait_minutes = max(1, math.ceil(wait_seconds / 60.0))
            reset_time_str = time.strftime("%H:%M UTC", time.gmtime(retry_at_ts))
            msg = (
                f"{_PROTECT_HEADER}"
                "Access request rate limit reached.\n"
                f"You may send another access request at {reset_time_str} (~{wait_minutes} min).\n"
                "To request access sooner, contact the system owner directly."
            )
            url = f"{TELEGRAM_API_BASE}/bot{self._bot_token}/sendMessage"
            loop = asyncio.get_event_loop()
            req = urllib.request.Request(
                url,
                data=json.dumps({"chat_id": chat_id, "text": msg}).encode(),
                headers={"Content-Type": "application/json"},
            )
            await loop.run_in_executor(
                None,
                lambda: urllib.request.urlopen(req, timeout=5, context=self._ssl_context),
            )
            return True
        except Exception as e:
            logger.warning("Failed to send stranger rate limit notice to chat %s: %s", chat_id, e)
        return False

    async def _send_telegram_text(
        self,
        chat_id: int,
        text: str,
        *,
        parse_mode: Optional[str] = None,
        retries: int = 3,
    ) -> bool:
        """Best-effort Telegram sender with bounded retries."""
        if not self._bot_token:
            return False
        url = f"{TELEGRAM_API_BASE}/bot{self._bot_token}/sendMessage"
        payload: dict[str, Any] = {"chat_id": chat_id, "text": text}
        if parse_mode:
            payload["parse_mode"] = parse_mode
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json"},
        )
        loop = asyncio.get_event_loop()
        attempts = max(1, retries)
        for attempt in range(attempts):
            try:
                await loop.run_in_executor(
                    None,
                    lambda: urllib.request.urlopen(req, timeout=5, context=self._ssl_context),
                )
                return True
            except Exception as exc:
                retry_after_seconds = 0.0
                if isinstance(exc, urllib.error.HTTPError):
                    try:
                        code = int(getattr(exc, "code", 0) or 0)
                    except Exception:
                        code = 0
                    if code == 429:
                        try:
                            body = exc.read()
                            parsed = (
                                json.loads(body.decode("utf-8", errors="ignore")) if body else {}
                            )
                            retry_after_val = (
                                parsed.get("parameters", {}).get("retry_after", 0)
                                if isinstance(parsed, dict)
                                else 0
                            )
                            retry_after_seconds = max(0.0, float(retry_after_val))
                        except Exception:
                            retry_after_seconds = 0.0
                        if retry_after_seconds <= 0.0:
                            retry_after_seconds = 1.0
                if attempt == attempts - 1:
                    logger.warning(
                        "Telegram sendMessage failed after retries (chat=%s): %s",
                        chat_id,
                        exc,
                    )
                    return False
                await asyncio.sleep(max(0.35 * (attempt + 1), retry_after_seconds))
        return False

    async def _send_telegram_with_keyboard(
        self,
        chat_id: int,
        text: str,
        keyboard: dict,
        *,
        parse_mode: str = "Markdown",
    ) -> bool:
        """Send a Telegram message with an inline keyboard."""
        if not self._bot_token:
            return False
        url = f"{TELEGRAM_API_BASE}/bot{self._bot_token}/sendMessage"
        payload: dict[str, Any] = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": parse_mode,
            "reply_markup": keyboard,
        }
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json"},
        )
        loop = asyncio.get_event_loop()
        try:
            await loop.run_in_executor(
                None,
                lambda: urllib.request.urlopen(req, timeout=5, context=self._ssl_context),
            )
            return True
        except Exception as exc:
            logger.warning("Telegram sendMessage+keyboard failed (chat=%s): %s", chat_id, exc)
            return False

    async def _edit_telegram_message(
        self,
        chat_id,
        message_id: int,
        text: str,
        *,
        parse_mode: str = "Markdown",
    ) -> bool:
        """Edit an existing Telegram message in-place (removes inline keyboard too)."""
        if not self._bot_token:
            return False
        url = f"{TELEGRAM_API_BASE}/bot{self._bot_token}/editMessageText"
        payload: dict[str, Any] = {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": text,
            "parse_mode": parse_mode,
        }
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json"},
        )
        loop = asyncio.get_event_loop()
        try:
            await loop.run_in_executor(
                None,
                lambda: urllib.request.urlopen(req, timeout=5, context=self._ssl_context),
            )
            return True
        except Exception as exc:
            logger.warning(
                "Telegram editMessageText failed (chat=%s, msg=%s): %s", chat_id, message_id, exc
            )
            return False

    async def _answer_callback_query(
        self,
        callback_query_id: str,
        text: str,
    ) -> bool:
        """Dismiss the Telegram inline button spinner with a brief toast."""
        if not self._bot_token:
            return False
        url = f"{TELEGRAM_API_BASE}/bot{self._bot_token}/answerCallbackQuery"
        payload: dict[str, Any] = {
            "callback_query_id": callback_query_id,
            "text": text,
            "show_alert": False,
        }
        req = urllib.request.Request(
            url,
            data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json"},
        )
        loop = asyncio.get_event_loop()
        try:
            await loop.run_in_executor(
                None,
                lambda: urllib.request.urlopen(req, timeout=5, context=self._ssl_context),
            )
            return True
        except Exception as exc:
            logger.warning("Telegram answerCallbackQuery failed: %s", exc)
            return False

    async def _send_local_notice_with_fallback(
        self,
        chat_id: int,
        primary_text: str,
        *,
        collaborator_safe: bool,
    ) -> None:
        """Send local command response with deterministic fallback text."""
        sent = await self._send_telegram_text(chat_id, primary_text, retries=2)
        if sent:
            return
        fallback = (
            _COLLABORATOR_UNAVAILABLE_NOTICE
            if collaborator_safe
            else "⚠️ AgentShroud local command notice unavailable. Please retry /status."
        )
        await self._send_telegram_text(chat_id, fallback, retries=5)

    async def _send_local_healthcheck_notice(self, chat_id: int) -> None:
        """Send deterministic gateway health status without model invocation."""
        try:
            if self._bot_token:
                msg = (
                    "✅ AgentShroud healthcheck\n"
                    "• Gateway: online\n"
                    "• Telegram channel: connected\n"
                    "• Security pipeline: enforcing\n"
                    "• Model routing: active"
                )
                await self._send_local_notice_with_fallback(
                    chat_id,
                    msg,
                    collaborator_safe=False,
                )
        except Exception as e:
            logger.warning("Failed to send local healthcheck notice to chat %s: %s", chat_id, e)

    async def _send_local_model_notice(self, chat_id: int) -> None:
        """Send deterministic model status without model invocation."""
        try:
            if self._bot_token:
                model_ref = (
                    os.environ.get("OPENCLAW_MAIN_MODEL")
                    or os.environ.get("AGENTSHROUD_CLOUD_MODEL_REF")
                    or os.environ.get("AGENTSHROUD_LOCAL_MODEL_REF")
                    or "unknown"
                )
                mode = os.environ.get("AGENTSHROUD_MODEL_MODE", "unknown")
                profile = os.environ.get("AGENTSHROUD_ACTIVE_PROFILE", "unknown")
                msg = (
                    "ℹ️ AgentShroud model status\n"
                    f"• Mode: {mode}\n"
                    f"• Profile: {profile}\n"
                    f"• Model: {model_ref}"
                )
                await self._send_local_notice_with_fallback(
                    chat_id,
                    msg,
                    collaborator_safe=False,
                )
        except Exception as e:
            logger.warning("Failed to send local model notice to chat %s: %s", chat_id, e)

    async def _send_local_help_notice(self, chat_id: int, *, is_owner: bool) -> None:
        """Send deterministic /help command list without model invocation."""
        try:
            if self._bot_token:
                if is_owner:
                    msg = (
                        "🛡️ AgentShroud owner commands\n"
                        "• /start\n"
                        "• /help\n"
                        "• /status (alias: /healthcheck)\n"
                        "• /whoami\n"
                        "• /model\n"
                        "• /pending\n"
                        "• /collabs\n"
                        "• /addcollab <telegram_user_id>\n"
                        "• /restorecollabs\n"
                        "• /approve <telegram_user_id>\n"
                        "• /deny <telegram_user_id>\n"
                        "• /revoke <telegram_user_id>\n"
                        "• /unlock <telegram_user_id>"
                    )
                else:
                    msg = (
                        f"{_PROTECT_HEADER}"
                        "Collaborator commands:\n"
                        "• /start\n"
                        "• /help\n"
                        "• /status (alias: /healthcheck)\n"
                        "• /whoami\n"
                        "• /model\n\n"
                        "If authorized, I can discuss architecture, security concepts, workflows, and recommendations.\n"
                        "Command execution, direct file access, and secrets remain restricted."
                    )
                await self._send_local_notice_with_fallback(
                    chat_id,
                    msg,
                    collaborator_safe=not is_owner,
                )
        except Exception as e:
            logger.warning("Failed to send local help notice to chat %s: %s", chat_id, e)

    async def _send_local_whoami_notice(
        self,
        chat_id: int,
        *,
        user_id: str,
        is_owner: bool,
        username: str,
    ) -> None:
        """Send deterministic identity/role notice to simplify approval workflows."""
        try:
            if not self._bot_token:
                return
            role = "owner" if is_owner else "collaborator"
            cleaned_username = (username or "unknown").strip()
            if is_owner:
                msg = (
                    "🛡️ AgentShroud identity\n"
                    f"• Role: {role}\n"
                    f"• Telegram user id: {user_id}\n"
                    f"• Username: {cleaned_username}\n"
                    "• Use /pending, /approve, /deny, /revoke, /unlock to manage collaborator access."
                )
            else:
                msg = (
                    f"{_PROTECT_HEADER}"
                    "Collaborator identity:\n"
                    f"• Role: {role}\n"
                    f"• Telegram user id: {user_id}\n"
                    f"• Username: {cleaned_username}\n"
                    "• Share this user id with owner for approval commands if needed."
                )
            await self._send_local_notice_with_fallback(
                chat_id,
                msg,
                collaborator_safe=not is_owner,
            )
        except Exception as e:
            logger.warning("Failed to send local whoami notice to chat %s: %s", chat_id, e)

    async def _send_owner_pending_notice(self, chat_id: int) -> None:
        """Send deterministic owner pending-approval snapshot."""
        try:
            if not self._bot_token:
                return
            now = time.time()
            pending_ids = sorted(self._pending_collaborator_requests.keys())
            configured_ids: list[str] = []
            if self._rbac:
                configured_ids = sorted(
                    str(uid) for uid in (self._rbac.collaborator_user_ids or [])
                )
            revoked_ids = sorted(self._runtime_revoked_collaborators)
            lines = ["🛡️ Protected by AgentShroud\n*Pending Access Requests*\n"]
            if pending_ids:
                for uid in pending_ids:
                    p = self._pending_collaborator_requests.get(uid, {}) or {}
                    uname = str(p.get("username", "")).strip()
                    uname_label = f"@{uname}" if uname and uname != "unknown" else "no username"
                    elapsed = int(now - float(p.get("requested_at", now)))
                    if elapsed < 60:
                        age = f"{elapsed}s ago"
                    elif elapsed < 3600:
                        age = f"{elapsed // 60}m ago"
                    else:
                        age = f"{elapsed // 3600}h ago"
                    lines.append(f"• {uname_label}  `{uid}`  ({age})")
                    lines.append(f"  `/approve {uid}`  •  `/deny {uid}`")
            else:
                lines.append("• No pending requests")
            if configured_ids:
                active_display = [self._resolve_display_name(uid) for uid in configured_ids]
                lines.append(f"\n*Active:* {', '.join(active_display)}")
            if revoked_ids:
                lines.append(f"*Revoked:* {', '.join(revoked_ids)}")
            msg = "\n".join(lines)
            await self._send_local_notice_with_fallback(
                chat_id,
                msg,
                collaborator_safe=False,
            )
        except Exception as e:
            logger.warning("Failed to send owner pending notice to chat %s: %s", chat_id, e)

    async def _send_owner_collabs_notice(self, chat_id: int) -> None:
        """Send owner-friendly collaborator roster with known labels."""
        try:
            if not self._bot_token:
                return
            configured_ids: list[str] = []
            if self._rbac:
                configured_ids = sorted(
                    str(uid) for uid in (self._rbac.collaborator_user_ids or [])
                )
            pending_ids = sorted(self._pending_collaborator_requests.keys())
            revoked_ids = sorted(self._runtime_revoked_collaborators)

            active_display = [self._resolve_display_name(uid) for uid in configured_ids]
            pending_display: list[str] = []
            for uid in pending_ids:
                pending = self._pending_collaborator_requests.get(uid, {}) or {}
                username = str(pending.get("username", "")).strip()
                if username and username != "unknown":
                    pending_display.append(f"{username} ({uid})")
                else:
                    pending_display.append(self._resolve_display_name(uid))
            revoked_display = [self._resolve_display_name(uid) for uid in revoked_ids]

            msg = (
                "🛡️ AgentShroud collaborator roster\n"
                f"• Active: {', '.join(active_display) if active_display else 'none'}\n"
                f"• Pending: {', '.join(pending_display) if pending_display else 'none'}\n"
                f"• Revoked: {', '.join(revoked_display) if revoked_display else 'none'}"
            )

            # Append recent activity section from tracker (queries + bot responses)
            try:
                import time as _time
                from datetime import datetime as _datetime
                from datetime import timezone as _tz

                from gateway.ingest_api.state import app_state as _app_state

                _tracker = getattr(_app_state, "collaborator_tracker", None)
                if _tracker and configured_ids:
                    # Pull last 24h of activity, max 60 entries
                    _recent = _tracker.get_activity(since=_time.time() - 86400, limit=60)
                    if _recent:
                        # Group by (user_id, source), newest-first already
                        _by_user: dict[str, list[dict]] = {}
                        for _e in _recent:
                            _k = str(_e.get("user_id", ""))
                            _by_user.setdefault(_k, []).append(_e)

                        _activity_lines: list[str] = []
                        for _uid in configured_ids:
                            _entries = _by_user.get(_uid, [])
                            if not _entries:
                                continue
                            _name = self._resolve_display_name(_uid)
                            _last_ts = _entries[0].get("timestamp", 0)
                            _last_dt = _datetime.fromtimestamp(_last_ts, tz=_tz.utc)
                            _last_str = _last_dt.strftime("%H:%M UTC")
                            _inbound = [
                                e for e in _entries if e.get("direction", "inbound") == "inbound"
                            ]
                            _outbound = [e for e in _entries if e.get("direction") == "outbound"]
                            _activity_lines.append(
                                f"\n{_name} — {len(_inbound)}q/{len(_outbound)}r, last {_last_str}"
                            )
                            # Show last 3 Q+A pairs interleaved (most recent 6 entries)
                            for _e in list(reversed(_entries))[-6:]:
                                _d = _e.get("direction", "inbound")
                                _src = _e.get("source", "telegram")
                                _t = _datetime.fromtimestamp(_e.get("timestamp", 0), tz=_tz.utc)
                                _ts = _t.strftime("%H:%M")
                                _prefix = "  <-" if _d == "inbound" else "  ->"
                                _src_tag = "" if _src == "telegram" else f"[{_src}]"
                                _preview = str(_e.get("message_preview", ""))[:60]
                                _activity_lines.append(f'{_prefix}{_src_tag} {_ts} "{_preview}"')

                        if _activity_lines:
                            msg += "\n\nRecent activity (24h):" + "".join(_activity_lines)
            except Exception as _ae:
                logger.debug("Collabs activity append error (non-fatal): %s", _ae)

            await self._send_local_notice_with_fallback(
                chat_id,
                msg,
                collaborator_safe=False,
            )
        except Exception as e:
            logger.warning("Failed to send owner collaborator roster to chat %s: %s", chat_id, e)

    async def _send_local_status_notice(self, chat_id: int, *, is_owner: bool) -> None:
        """Send deterministic /status summary without model invocation."""
        try:
            if not self._bot_token:
                return
            if is_owner:
                pending_count = len(self._pending_collaborator_requests)
                collaborator_count = len(getattr(self._rbac, "collaborator_user_ids", []) or [])
                revoked_count = len(self._runtime_revoked_collaborators)
                msg = (
                    "🛡️ AgentShroud status\n"
                    "• Gateway: online\n"
                    "• Security pipeline: enforcing\n"
                    f"• Active collaborators: {collaborator_count}\n"
                    f"• Pending approvals: {pending_count}\n"
                    f"• Revoked users: {revoked_count}\n"
                    "• Commands: /pending, /approve, /deny, /revoke, /unlock, /addcollab, /restorecollabs"
                )
            else:
                msg = (
                    f"{_PROTECT_HEADER}"
                    "Collaborator session status:\n"
                    "• Gateway: online\n"
                    "• Security mode: enforcing\n"
                    "• If authorized, I can provide security concepts and recommendations.\n"
                    "• Direct command execution, file contents, and secrets remain restricted."
                )
            await self._send_local_notice_with_fallback(
                chat_id,
                msg,
                collaborator_safe=not is_owner,
            )
        except Exception as e:
            logger.warning("Failed to send local status notice to chat %s: %s", chat_id, e)

    async def _send_local_start_notice(self, chat_id: int, *, is_owner: bool) -> None:
        """Send deterministic /start notice without model invocation."""
        try:
            if self._bot_token:
                if is_owner:
                    msg = (
                        "🛡️ AgentShroud online\n"
                        "• Security pipeline: enforcing\n"
                        "• Use /healthcheck for runtime status\n"
                        "• Use /model for active model status"
                    )
                else:
                    msg = (
                        f"{_PROTECT_HEADER}"
                        "Collaborator session is ready.\n"
                        "If authorized, you can ask about architecture, security concepts, and recommendations.\n"
                        "Command execution, direct file access, and secrets remain restricted."
                    )
                await self._send_local_notice_with_fallback(
                    chat_id,
                    msg,
                    collaborator_safe=not is_owner,
                )
        except Exception as e:
            logger.warning("Failed to send local start notice to chat %s: %s", chat_id, e)

    async def _send_owner_admin_notice(self, chat_id: int, message: str) -> None:
        """Send deterministic owner admin notice without model invocation."""
        try:
            if self._bot_token:
                sent = await self._send_telegram_text(chat_id, message, retries=2)
                if not sent:
                    await self._send_telegram_text(
                        chat_id,
                        "⚠️ AgentShroud admin notice delivery retry. Please run /status and /pending.",
                        retries=5,
                    )
        except Exception as e:
            logger.warning("Failed to send owner admin notice to chat %s: %s", chat_id, e)

    async def _send_collaborator_pending_notice(self, chat_id: int) -> None:
        """Send deterministic pending-approval notice to unknown/revoked users."""
        try:
            if not self._bot_token:
                return
            await self._send_local_notice_with_fallback(
                chat_id,
                f"{_PROTECT_HEADER}Access pending owner approval. Please wait.",
                collaborator_safe=True,
            )
        except Exception as e:
            logger.warning("Failed to send collaborator pending notice to chat %s: %s", chat_id, e)

    async def _send_collaborator_safe_info_notice(self, chat_id: int) -> None:
        """Send concise informative collaborator-safe guidance."""
        try:
            if self._bot_token:
                sent = await self._send_telegram_text(
                    chat_id,
                    _COLLABORATOR_SAFE_INFO_NOTICE,
                    retries=2,
                )
                if not sent:
                    await self._send_telegram_text(
                        chat_id,
                        _COLLABORATOR_UNAVAILABLE_NOTICE,
                        retries=5,
                    )
        except Exception as e:
            logger.warning(
                "Failed to send collaborator safe-info notice to chat %s: %s", chat_id, e
            )

    # ------------------------------------------------------------------
    # V9-4D — Collab mode resolution + project scope
    # ------------------------------------------------------------------

    @property
    def _teams_config(self):
        """Return TeamsConfig from app_state if available."""
        try:
            from gateway.ingest_api.state import app_state as _as

            cfg = getattr(_as, "config", None)
            return getattr(cfg, "teams", None) if cfg else None
        except Exception:
            return None

    def _resolve_collaborator_mode(self, user_id: str) -> str:
        """Resolve effective collaboration mode for a user.

        Resolution order:
          1. user-level override via TeamsConfig
          2. group collab_mode (first group the user belongs to)
          3. AGENTSHROUD_COLLAB_LOCAL_INFO_ONLY env var fallback
          4. "local_only" (safe default)
        """
        teams = self._teams_config
        if teams is not None:
            mode = teams.get_user_collab_mode(user_id)
            if mode:
                return mode
        # Env var backward-compat
        local_only = os.getenv("AGENTSHROUD_COLLAB_LOCAL_INFO_ONLY", "1").strip().lower()
        if local_only in {"0", "false", "no"}:
            return "full_access"
        return "local_only"

    def _get_user_projects(self, user_id: str):
        """Return list of ProjectConfig objects for this user, or empty list."""
        teams = self._teams_config
        if teams is None:
            return []
        return teams.get_user_projects(user_id)

    def _is_within_project_scope(self, text: str, projects) -> bool:
        """Return True if text has any keyword overlap with the user's project focus_topics.

        A zero-keyword match is treated as clearly off-topic → return False.
        Any overlap (even one keyword) is treated as ambiguous → return True (pass through).
        """
        if not projects:
            return True  # No scope defined → allow everything
        text_lower = (text or "").lower()
        for project in projects:
            for topic in project.focus_topics or []:
                if topic.lower() in text_lower:
                    return True
        return False

    # ------------------------------------------------------------------
    # V9-4F — Group command handlers
    # ------------------------------------------------------------------

    async def _handle_groups_command(self, chat_id: int, user_id: str) -> None:
        """Handle /groups — list groups this user belongs to."""
        from .collaborator_responses import format_groups_list

        teams = self._teams_config
        if teams is None:
            await self._send_owner_admin_notice(
                chat_id,
                f"{_PROTECT_HEADER}No team groups configured.",
            )
            return
        user_groups = teams.get_user_groups(user_id)
        await self._send_owner_admin_notice(
            chat_id, format_groups_list(user_id, user_groups, teams)
        )

    async def _handle_groupinfo_command(self, chat_id: int, user_id: str, group_id: str) -> None:
        """Handle /groupinfo <group_id>."""
        from .collaborator_responses import (
            format_group_info,
            format_not_member,
            format_unknown_group,
        )

        teams = self._teams_config
        if teams is None or not group_id:
            await self._send_owner_admin_notice(
                chat_id,
                f"{_PROTECT_HEADER}Usage: /groupinfo <group_id>",
            )
            return
        group = teams.groups.get(group_id)
        if group is None:
            await self._send_owner_admin_notice(chat_id, format_unknown_group(group_id))
            return
        is_owner = self._rbac and self._rbac.is_owner(user_id) if self._rbac else False
        if not is_owner and user_id not in group.members:
            await self._send_owner_admin_notice(chat_id, format_not_member(group_id))
            return
        await self._send_owner_admin_notice(chat_id, format_group_info(group_id, group, teams))

    async def _handle_projects_command(self, chat_id: int, user_id: str) -> None:
        """Handle /projects — list accessible projects."""
        from .collaborator_responses import format_projects_list

        teams = self._teams_config
        if teams is None:
            await self._send_owner_admin_notice(
                chat_id,
                f"{_PROTECT_HEADER}No projects configured.",
            )
            return
        user_projects = teams.get_user_projects(user_id)
        await self._send_owner_admin_notice(chat_id, format_projects_list(user_id, user_projects))

    async def _handle_addtogroup_command(
        self, chat_id: int, user_id: str, target_uid: str, group_id: str
    ) -> None:
        """Handle /addtogroup <user_id> <group_id> (owner only)."""
        from ..security.group_config import persist_group_member_add
        from .collaborator_responses import (
            format_addtogroup_success,
            format_unknown_group,
        )

        if not target_uid or not group_id:
            await self._send_owner_admin_notice(
                chat_id,
                f"{_PROTECT_HEADER}Usage: /addtogroup <user_id> <group_id>",
            )
            return
        teams = self._teams_config
        if teams is None or group_id not in teams.groups:
            await self._send_owner_admin_notice(chat_id, format_unknown_group(group_id))
            return
        group = teams.groups[group_id]
        if target_uid not in group.members:
            group.members.append(target_uid)
        persist_group_member_add(group_id, target_uid)
        # Also ensure the user is a recognized collaborator
        if self._rbac and target_uid not in {
            str(u) for u in (self._rbac.collaborator_user_ids or [])
        }:
            self._rbac.collaborator_user_ids = list(self._rbac.collaborator_user_ids or []) + [
                target_uid
            ]
        await self._send_owner_admin_notice(
            chat_id, format_addtogroup_success(target_uid, group_id)
        )

    async def _handle_rmfromgroup_command(
        self, chat_id: int, user_id: str, target_uid: str, group_id: str
    ) -> None:
        """Handle /rmfromgroup <user_id> <group_id> (owner or group admin)."""
        from ..security.group_config import persist_group_member_remove
        from .collaborator_responses import (
            format_rmfromgroup_success,
            format_unknown_group,
        )

        if not target_uid or not group_id:
            await self._send_owner_admin_notice(
                chat_id,
                f"{_PROTECT_HEADER}Usage: /rmfromgroup <user_id> <group_id>",
            )
            return
        teams = self._teams_config
        if teams is None or group_id not in teams.groups:
            await self._send_owner_admin_notice(chat_id, format_unknown_group(group_id))
            return
        group = teams.groups[group_id]
        group.members = [m for m in group.members if m != target_uid]
        persist_group_member_remove(group_id, target_uid)
        await self._send_owner_admin_notice(
            chat_id, format_rmfromgroup_success(target_uid, group_id)
        )

    async def _handle_setmode_command(
        self, chat_id: int, user_id: str, target: str, mode: str
    ) -> None:
        """Handle /setmode <group_id|user_id> <local_only|project_scoped|full_access> (owner only)."""
        from ..security.group_config import persist_group_collab_mode
        from .collaborator_responses import format_setmode_success

        valid_modes = {"local_only", "project_scoped", "full_access"}
        if not target or mode not in valid_modes:
            await self._send_owner_admin_notice(
                chat_id,
                f"{_PROTECT_HEADER}Usage: /setmode <group_id|user_id> <local_only|project_scoped|full_access>",
            )
            return
        teams = self._teams_config
        if teams and target in teams.groups:
            teams.groups[target].collab_mode = mode
            persist_group_collab_mode(target, mode)
            await self._send_owner_admin_notice(
                chat_id, format_setmode_success(target, mode, "group")
            )
        else:
            # Treat as user-level override (stored in group_overrides.json)
            persist_group_collab_mode(f"user:{target}", mode)
            await self._send_owner_admin_notice(
                chat_id, format_setmode_success(target, mode, "user")
            )

    async def _send_collaborator_safe_info_response(self, chat_id: int, prompt: str) -> None:
        """Send tailored safe informational response for collaborator conceptual query."""
        try:
            if self._bot_token:
                msg = self._build_collaborator_safe_info_response(prompt)
                # V9-4: Apply per-group safe_response_prefix if operator configured one.
                try:
                    from gateway.ingest_api.state import app_state as _gs

                    _rbac = getattr(_gs, "rbac_config", None)
                    _teams = getattr(_rbac, "teams_config", None) if _rbac else None
                    if _teams:
                        _uid = self._collaborator_chat_ids.get(str(chat_id))
                        if _uid:
                            _pfx = _teams.get_group_safe_response_prefix(_uid)
                            if _pfx:
                                msg = _pfx + "\n\n" + msg
                except Exception:
                    pass  # Never block delivery on prefix lookup failure
                sent = await self._send_telegram_text(chat_id, msg, retries=2)
                if not sent:
                    await self._send_telegram_text(
                        chat_id,
                        _COLLABORATOR_UNAVAILABLE_NOTICE,
                        retries=5,
                    )
                # Record outbound response in activity tracker so both sides of the
                # conversation appear in the SOC Command Center Activity tab.
                try:
                    from gateway.ingest_api.state import app_state as _app_state

                    _tracker = getattr(_app_state, "collaborator_tracker", None)
                    if _tracker:
                        _collab_uid = self._collaborator_chat_ids.get(str(chat_id))
                        if _collab_uid:
                            _corr_pair = self._last_inbound_corr.get(str(chat_id))
                            _local_corr_id = _corr_pair[0] if _corr_pair else None
                            _tracker.record_activity(
                                user_id=_collab_uid,
                                username="bot",
                                message_preview=(msg or _COLLABORATOR_UNAVAILABLE_NOTICE)[:80],
                                source="telegram",
                                direction="outbound",
                                correlation_id=_local_corr_id,
                            )
                except Exception as _te:
                    logger.debug("Outbound local-response tracker error (non-fatal): %s", _te)
        except Exception as e:
            logger.warning(
                "Failed to send collaborator safe-info response to chat %s: %s", chat_id, e
            )
            try:
                await self._send_telegram_text(chat_id, _COLLABORATOR_UNAVAILABLE_NOTICE, retries=3)
            except Exception:
                pass

    async def _send_disclosure(self, chat_id: int) -> None:
        """Send the one-time collaborator disclosure notice."""
        try:
            if self._bot_token:
                sent = await self._send_telegram_text(
                    chat_id,
                    _DISCLOSURE_MESSAGE,
                    parse_mode="MarkdownV2",
                )
                if not sent:
                    # Markdown formatting can fail in edge cases; retry plain text.
                    sent = await self._send_telegram_text(chat_id, _DISCLOSURE_MESSAGE)
                if sent:
                    logger.info("Sent collaborator disclosure to chat %s", chat_id)
        except Exception as e:
            logger.warning("Failed to send disclosure to chat %s: %s", chat_id, e)

    async def _notify_collaborator_command_blocked(self, chat_id: int, command: str) -> None:
        """Notify a collaborator that a privileged command is not available."""
        try:
            if self._bot_token:
                msg = self._collaborator_safe_notice(command)
                sent = await self._send_telegram_text(chat_id, msg, retries=2)
                if not sent:
                    await self._send_telegram_text(
                        chat_id,
                        _COLLABORATOR_UNAVAILABLE_NOTICE,
                        retries=5,
                    )
        except Exception as e:
            logger.warning("Failed to send command-blocked notice to chat %s: %s", chat_id, e)

    async def _notify_user_blocked(self, chat_id: int, reason: str):
        """Send a user-friendly notification when a message is blocked."""
        try:
            is_owner = self._is_owner_chat(str(chat_id))
            if not is_owner:
                notice = self._collaborator_safe_notice(reason)
            else:
                friendly_reasons = {
                    "gitguard": "Your message contained patterns resembling code or script injection.",
                    "promptguard": "Your message was flagged as a potential prompt injection attempt.",
                    "prompt injection": "Your message was flagged as a potential prompt injection attempt.",
                    "browsersecurity": "Your message contained a potentially unsafe browser payload.",
                    "rbac": "You don't have permission to perform this action.",
                    "contextguard": "Your message was flagged for context manipulation.",
                    "filesandbox": "Your message referenced a restricted file path.",
                }
                user_msg = "Your message was blocked by a security filter."
                reason_lower = reason.lower()
                for key, friendly in friendly_reasons.items():
                    if key in reason_lower:
                        user_msg = friendly
                        break

                notice = (
                    "\u26a0\ufe0f Message Blocked\n\n"
                    f"{user_msg}\n\n"
                    f"Reason: {self._sanitize_reason(reason)}\n\n"
                    "If this is an error, contact the system owner."
                )
            if self._bot_token:
                sent = await self._send_telegram_text(chat_id, notice, retries=2)
                if not sent:
                    fallback = (
                        _COLLABORATOR_UNAVAILABLE_NOTICE
                        if not is_owner
                        else "⚠️ AgentShroud notice unavailable. Please retry /status."
                    )
                    sent = await self._send_telegram_text(chat_id, fallback, retries=5)
                if sent:
                    logger.info(f"Sent block notification to chat {chat_id}")
        except Exception as e:
            logger.error(f"Failed to send block notification to {chat_id}: {e}")

    async def _forward_to_telegram(
        self, url: str, body: Optional[bytes], content_type: Optional[str]
    ) -> dict:
        """Forward request to real Telegram API and return parsed response."""
        headers = {}
        if content_type:
            headers["Content-Type"] = content_type

        req = urllib.request.Request(url, data=body, headers=headers)

        loop = asyncio.get_event_loop()
        try:
            response = await loop.run_in_executor(
                None,
                lambda: urllib.request.urlopen(req, timeout=60, context=self._ssl_context),
            )
            response_body = response.read()
            return json.loads(response_body)
        except urllib.error.HTTPError as exc:
            # Telegram uses HTTP 4xx/5xx with JSON bodies for expected API failures
            # (e.g., malformed Markdown, invalid chat ID). Treat as handled response.
            raw = b""
            try:
                raw = exc.read() if hasattr(exc, "read") else b""
            except Exception:
                raw = b""

            parsed: dict[str, Any]
            if raw:
                try:
                    loaded = json.loads(raw.decode("utf-8", errors="replace"))
                    if isinstance(loaded, dict):
                        parsed = loaded
                    else:
                        parsed = {}
                except Exception:
                    parsed = {}
            else:
                parsed = {}

            if "ok" not in parsed:
                parsed["ok"] = False
            parsed.setdefault("error_code", getattr(exc, "code", 502))
            parsed.setdefault("description", getattr(exc, "reason", str(exc)))

            logger.info(
                "Telegram API returned HTTP %s (%s)",
                parsed.get("error_code"),
                parsed.get("description"),
            )
            return parsed

    async def _forward_file_download(self, url: str) -> dict:
        """Forward a Telegram file download and return a raw-binary sentinel dict.

        File downloads (path prefix ``file/``) return binary image or document
        data, not JSON.  Callers must detect the ``_raw_body`` key and return a
        binary HTTP response instead of JSONResponse.

        CVE-2026-32049: reads in chunks and aborts if the response exceeds
        _MAX_MEDIA_FILE_SIZE, preventing unbounded memory consumption.
        """
        req = urllib.request.Request(url)
        loop = asyncio.get_event_loop()
        response = await loop.run_in_executor(
            None,
            lambda: urllib.request.urlopen(req, timeout=60, context=self._ssl_context),
        )
        content_type = response.headers.get("Content-Type", "application/octet-stream")
        status_code = response.status

        # Stream in 64 KB chunks; abort if total exceeds the media size limit.
        _chunk_size = 65536
        _chunks: list[bytes] = []
        _total = 0

        def _read_chunks():
            nonlocal _total
            while True:
                chunk = response.read(_chunk_size)
                if not chunk:
                    break
                _total += len(chunk)
                if _total > _MAX_MEDIA_FILE_SIZE:
                    raise ValueError(
                        f"File download exceeds size limit ({_MAX_MEDIA_FILE_SIZE} bytes)"
                    )
                _chunks.append(chunk)

        await loop.run_in_executor(None, _read_chunks)
        body = b"".join(_chunks)
        return {
            "_raw_body": body,
            "_content_type": content_type,
            "_status_code": status_code,
        }
