# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""
Collaborator daily greeting — fires on the first inbound Telegram message
from any collaborator (or the owner) after a 24-hour quiet period.

Sends the AgentShroud logo photo + a per-(bot, user) personalised caption
with a random tagline drawn from branding/taglines.json.

Dispatched fire-and-forget via asyncio.create_task from telegram_proxy.py
so it never blocks the proxy hot-path (<0.5 ms baseline unaffected).
All I/O wrapped in try/except — must never raise.
"""
from __future__ import annotations

import json
import logging
import os
import random
import time
from pathlib import Path
from typing import Any

import httpx

logger = logging.getLogger("agentshroud.proxy.collaborator_greeter")

_DEFAULT_TAGLINE = "Your agent can do anything— except get away with it."
_CAPTION_MAX = 1024  # Telegram sendPhoto caption limit


class CollaboratorGreeter:
    """Sends a branded greeting photo to each (bot, user) pair once per 24 h."""

    def __init__(
        self,
        state_path: str,
        taglines_path: str,
        logo_path: str,
        gateway_telegram_base: str = "http://127.0.0.1:8080/telegram-api",
        cooldown_seconds: int = 86400,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        self._state_path = state_path
        self._logo_path = logo_path
        self._gateway_base = gateway_telegram_base.rstrip("/")
        self._cooldown = cooldown_seconds
        self._taglines = self._load_taglines(taglines_path)
        self._state: dict[str, float] = self._load_state(state_path)
        self._http_client = http_client  # injected in tests; created lazily otherwise
        self._own_client: httpx.AsyncClient | None = None

    def _get_client(self) -> httpx.AsyncClient:
        if self._http_client is not None:
            return self._http_client
        if self._own_client is None:
            self._own_client = httpx.AsyncClient()
        return self._own_client

    # ── public ────────────────────────────────────────────────────────────────

    async def maybe_greet(
        self,
        *,
        bot_token: str,
        bot_id: str,
        user_id: str,
        first_name: str | None,
    ) -> bool:
        """Greet user if cooldown has expired. Returns True when greeting was sent."""
        try:
            key = f"{bot_id}:{user_id}"
            now = time.time()
            last = self._state.get(key, 0.0)
            if now - last < self._cooldown:
                return False

            tagline = random.choice(self._taglines)
            name = first_name or "there"
            raw_caption = f"Hello, {name} — AgentShroud at your service.\n\n{tagline}"
            caption = raw_caption[:_CAPTION_MAX]

            url = f"{self._gateway_base}/bot{bot_token}/sendPhoto"
            logo = Path(self._logo_path)
            if not logo.exists():
                logger.warning("Greeter logo not found at %s — skipping", self._logo_path)
                return False

            files = {
                "photo": (logo.name, logo.read_bytes(), "image/png"),
                "chat_id": (None, user_id),
                "caption": (None, caption),
            }
            resp = await self._get_client().post(
                url,
                files=files,  # type: ignore[arg-type]
                headers={"X-AgentShroud-System": "1"},
                timeout=15.0,
            )
            if resp.status_code == 200:
                self._state[key] = now
                self._persist_state()
                logger.info("Greeter: sent greeting to %s via bot=%s", user_id, bot_id)
                return True
            logger.warning(
                "Greeter sendPhoto failed: %s %s", resp.status_code, resp.text[:200]
            )
            return False
        except Exception as exc:
            logger.warning("Greeter.maybe_greet error: %s", exc)
            return False

    # ── helpers ───────────────────────────────────────────────────────────────

    @staticmethod
    def _load_taglines(path: str) -> list[str]:
        try:
            raw = Path(path).read_text(encoding="utf-8")
            data = json.loads(raw)
            if isinstance(data, list) and data:
                return [str(t) for t in data if t]
        except Exception as exc:
            logger.warning("Greeter: could not load taglines from %s (%s) — using default", path, exc)
        return [_DEFAULT_TAGLINE]

    @staticmethod
    def _load_state(path: str) -> dict[str, float]:
        try:
            raw = Path(path).read_text(encoding="utf-8")
            data = json.loads(raw)
            if isinstance(data, dict):
                return {k: float(v) for k, v in data.items()}
        except FileNotFoundError:
            pass
        except Exception as exc:
            logger.warning("Greeter: state file %s corrupt (%s) — starting fresh", path, exc)
            try:
                Path(path).write_text("{}", encoding="utf-8")
            except Exception:
                pass
        return {}

    def _persist_state(self) -> None:
        try:
            tmp = self._state_path + ".tmp"
            Path(tmp).write_text(json.dumps(self._state), encoding="utf-8")
            os.replace(tmp, self._state_path)
        except Exception as exc:
            logger.warning("Greeter: failed to persist state: %s", exc)
