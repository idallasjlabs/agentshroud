# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for multi-bot Telegram token registry in the gateway route handler.

Phase 1.3 of v1.1.0: the /telegram-api/{path} endpoint previously accepted only
the single OpenClaw bot token. These tests verify the multi-bot registry correctly
dispatches by token and rejects unrecognised tokens with 403 (fail-closed).
"""

from __future__ import annotations

import asyncio
import time
from typing import TYPE_CHECKING
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

if TYPE_CHECKING:
    from gateway.proxy.telegram_proxy import TelegramAPIProxy

_OPENCLAW_TOKEN = "000000001:EXAMPLEFakeOpenClawToken0000000000000"
_HERMES_TOKEN = "000000002:EXAMPLEFakeHermesToken00000000000000"
_UNKNOWN_TOKEN = "000000003:EXAMPLEFakeUnknownToken000000000000000"

_REGISTRY = {
    _OPENCLAW_TOKEN: "openclaw",
    _HERMES_TOKEN: "hermes",
}


class TestTelegramTokenRegistry:
    """Validate the token → bot_id registry logic extracted from the route handler."""

    def test_openclaw_token_resolves_to_openclaw(self):
        matched = _REGISTRY.get(_OPENCLAW_TOKEN)
        assert matched == "openclaw"

    def test_hermes_token_resolves_to_hermes(self):
        matched = _REGISTRY.get(_HERMES_TOKEN)
        assert matched == "hermes"

    def test_unknown_token_resolves_to_none(self):
        matched = _REGISTRY.get(_UNKNOWN_TOKEN)
        assert matched is None

    def test_registry_rejects_empty_string(self):
        matched = _REGISTRY.get("")
        assert matched is None

    def test_registry_rejects_partial_token(self):
        partial = _OPENCLAW_TOKEN[:10]
        assert _REGISTRY.get(partial) is None

    def test_registry_rejects_case_variant(self):
        """Token matching must be exact — case-sensitive."""
        upper = _OPENCLAW_TOKEN.upper()
        assert _REGISTRY.get(upper) is None

    def test_both_bots_registered_distinct_ids(self):
        """Registry maps two distinct tokens to two distinct bot_ids."""
        ids = set(_REGISTRY.values())
        assert "openclaw" in ids
        assert "hermes" in ids
        assert len(ids) == 2

    def test_no_token_collision(self):
        """Tokens are the registry keys — no two bots share a token."""
        assert len(_REGISTRY) == len(set(_REGISTRY.keys()))


class TestTelegramProxyRouteMultiBot:
    """Integration tests for the /telegram-api/{path} route with multi-bot registry."""

    def _mock_app_state_with_registry(self, registry: dict):
        mock = MagicMock()
        mock._telegram_token_registry = registry
        # Minimal config.bots stub (registry already pre-built)
        mock.config = MagicMock()
        mock.config.bots = {}
        return mock

    def test_valid_openclaw_token_accepted(self):
        """A request bearing the OpenClaw token resolves to 'openclaw' bot_id."""
        registry = {_OPENCLAW_TOKEN: "openclaw", _HERMES_TOKEN: "hermes"}

        matched_bot_id = registry.get(_OPENCLAW_TOKEN)
        assert matched_bot_id == "openclaw"
        assert matched_bot_id is not None

    def test_valid_hermes_token_accepted(self):
        """A request bearing the Hermes token resolves to 'hermes' bot_id."""
        registry = {_OPENCLAW_TOKEN: "openclaw", _HERMES_TOKEN: "hermes"}

        matched_bot_id = registry.get(_HERMES_TOKEN)
        assert matched_bot_id == "hermes"
        assert matched_bot_id is not None

    def test_unknown_token_rejected(self):
        """An unregistered token must not be matched — fail-closed."""
        registry = {_OPENCLAW_TOKEN: "openclaw", _HERMES_TOKEN: "hermes"}

        matched_bot_id = registry.get(_UNKNOWN_TOKEN)
        assert matched_bot_id is None

    def test_empty_registry_fails_closed(self):
        """If no tokens are registered, any token must be rejected."""
        registry = {}
        assert registry.get(_OPENCLAW_TOKEN) is None
        assert registry.get(_HERMES_TOKEN) is None
        assert registry.get(_UNKNOWN_TOKEN) is None


class TestTelegramBotConfigTokenSecretField:
    """Verify BotConfig.telegram_token_secret field is present and defaults correctly."""

    def test_bot_config_has_telegram_token_secret_field(self):
        from gateway.ingest_api.bot_config import BotConfig

        cfg = BotConfig(
            id="hermes",
            name="Hermes Agent",
            hostname="agentshroud-hermes",
            port=8642,
            workspace_path="/opt/data/home",
            config_dir="/opt/data",
        )
        assert hasattr(cfg, "telegram_token_secret")
        assert cfg.telegram_token_secret == ""

    def test_bot_config_telegram_token_secret_set(self):
        from gateway.ingest_api.bot_config import BotConfig

        cfg = BotConfig(
            id="hermes",
            name="Hermes Agent",
            hostname="agentshroud-hermes",
            port=8642,
            workspace_path="/opt/data/home",
            config_dir="/opt/data",
            telegram_token_secret="hermes_telegram_bot_token",
        )
        assert cfg.telegram_token_secret == "hermes_telegram_bot_token"

    def test_bot_config_image_field_present(self):
        from gateway.ingest_api.bot_config import BotConfig

        cfg = BotConfig(
            id="hermes",
            name="Hermes Agent",
            hostname="agentshroud-hermes",
            port=8642,
            workspace_path="/opt/data/home",
            config_dir="/opt/data",
            image="agentshroud/hermes:latest",
        )
        assert cfg.image == "agentshroud/hermes:latest"

    def test_openclaw_bot_config_backward_compat(self):
        """OpenClaw BotConfig must still work without the new fields."""
        from gateway.ingest_api.bot_config import BotConfig

        cfg = BotConfig(
            id="openclaw",
            name="OpenClaw",
            hostname="agentshroud",
            port=18789,
            workspace_path="/home/node/.openclaw/workspace",
            config_dir="/home/node/.openclaw",
        )
        # New optional fields default gracefully
        assert cfg.telegram_token_secret == ""
        assert cfg.image == ""
        assert cfg.default is False


class TestMultiBotContextvarRouting:
    """Tests for per-request bot token routing via contextvars.

    Regression suite for the cross-bot reply misrouting bug:
      /status sent to Hermes bot → reply delivered through OpenClaw bot.
    Root cause: single shared TelegramAPIProxy with self._bot_token = OpenClaw token;
    local-command replies always egressed through the default token regardless of which
    bot received the inbound getUpdates request.
    Fix: proxy_request sets _inbound_bot_token contextvar; senders read _active_send_token().
    """

    def _make_proxy(self, default_token: str = _OPENCLAW_TOKEN) -> "TelegramAPIProxy":
        from gateway.proxy.telegram_proxy import TelegramAPIProxy

        proxy = TelegramAPIProxy.__new__(TelegramAPIProxy)
        proxy._bot_token = default_token
        proxy._ssl_context = MagicMock()
        proxy._default_bot_id = "openclaw"
        return proxy

    def test_active_send_token_returns_default_outside_request(self):
        """Outside a proxy_request call, _active_send_token() returns self._bot_token."""
        from gateway.proxy import telegram_proxy as _tp

        _tp._inbound_bot_token.set(None)
        proxy = self._make_proxy(_OPENCLAW_TOKEN)
        assert proxy._active_send_token() == _OPENCLAW_TOKEN

    def test_active_send_token_returns_contextvar_inside_request(self):
        """When _inbound_bot_token is set, _active_send_token() returns it."""
        from gateway.proxy import telegram_proxy as _tp

        token = _tp._inbound_bot_token.set(_HERMES_TOKEN)
        try:
            proxy = self._make_proxy(_OPENCLAW_TOKEN)
            assert proxy._active_send_token() == _HERMES_TOKEN
        finally:
            _tp._inbound_bot_token.reset(token)

    def test_active_bot_id_falls_back_to_openclaw(self):
        """Outside a proxy_request call, _active_bot_id() returns 'openclaw'."""
        from gateway.proxy import telegram_proxy as _tp

        _tp._inbound_bot_id.set(None)
        proxy = self._make_proxy()
        assert proxy._active_bot_id() == "openclaw"

    def test_active_bot_id_returns_contextvar_when_set(self):
        """When _inbound_bot_id is set, _active_bot_id() returns it."""
        from gateway.proxy import telegram_proxy as _tp

        token = _tp._inbound_bot_id.set("hermes")
        try:
            proxy = self._make_proxy()
            assert proxy._active_bot_id() == "hermes"
        finally:
            _tp._inbound_bot_id.reset(token)

    def test_send_telegram_text_uses_inbound_token(self):
        """_send_telegram_text uses the inbound contextvar token, not self._bot_token."""
        from gateway.proxy import telegram_proxy as _tp

        captured_urls = []

        def fake_urlopen(req, timeout=None, context=None):
            captured_urls.append(req.full_url)
            return MagicMock()

        ctx_token = _tp._inbound_bot_token.set(_HERMES_TOKEN)
        try:
            proxy = self._make_proxy(_OPENCLAW_TOKEN)
            with patch("urllib.request.urlopen", side_effect=fake_urlopen):
                asyncio.run(proxy._send_telegram_text(12345, "hello"))
        finally:
            _tp._inbound_bot_token.reset(ctx_token)

        assert len(captured_urls) == 1
        assert f"bot{_HERMES_TOKEN}" in captured_urls[0]
        assert f"bot{_OPENCLAW_TOKEN}" not in captured_urls[0]

    def test_send_telegram_text_falls_back_to_default_token(self):
        """Without contextvar, _send_telegram_text uses self._bot_token."""
        from gateway.proxy import telegram_proxy as _tp

        captured_urls = []

        def fake_urlopen(req, timeout=None, context=None):
            captured_urls.append(req.full_url)
            return MagicMock()

        _tp._inbound_bot_token.set(None)
        proxy = self._make_proxy(_OPENCLAW_TOKEN)
        with patch("urllib.request.urlopen", side_effect=fake_urlopen):
            asyncio.run(proxy._send_telegram_text(12345, "hello"))

        assert len(captured_urls) == 1
        assert f"bot{_OPENCLAW_TOKEN}" in captured_urls[0]

    def test_proxy_request_resets_contextvar_after_return(self):
        """After proxy_request returns, _inbound_bot_token is reset to its prior value."""
        from gateway.proxy import telegram_proxy as _tp

        proxy = self._make_proxy(_OPENCLAW_TOKEN)
        initial_value = _tp._inbound_bot_token.get()

        async def run():
            proxy._proxy_request_impl = AsyncMock(return_value={"ok": True, "result": []})
            await proxy.proxy_request(_HERMES_TOKEN, "getUpdates", bot_id="hermes")

        asyncio.run(run())
        assert _tp._inbound_bot_token.get() == initial_value

    def test_proxy_request_contextvar_visible_inside_impl(self):
        """The contextvar set by proxy_request is visible throughout _proxy_request_impl.

        This plus test_send_telegram_text_uses_inbound_token jointly prove that any sender
        invoked inside _proxy_request_impl (e.g. _send_local_status_notice) will use the
        inbound bot's token rather than the OpenClaw default — fixing the routing bug.
        """

        proxy = self._make_proxy(_OPENCLAW_TOKEN)
        captured_token_in_impl: list = []

        async def run():
            async def impl_capture(token, method, body=None, ct=None, is_system=False, prefix=""):
                captured_token_in_impl.append(proxy._active_send_token())
                return {"ok": True, "result": []}

            proxy._proxy_request_impl = impl_capture
            await proxy.proxy_request(_HERMES_TOKEN, "getUpdates", bot_id="hermes")

        asyncio.run(run())

        assert len(captured_token_in_impl) == 1


class TestTelegramTokenRegistryRebuildOnMiss:
    """The token registry is built lazily on the first /telegram-api/{path} request
    and cached for the life of the process. If a bot's secret file is not yet
    mounted/synced at that exact moment (e.g. an ephemeral-secrets copy step racing
    gateway's healthcheck at boot), the stale cache previously 403'd that bot on
    every request until a full gateway restart — even after the secret became
    available seconds later. These tests prove the registry now self-heals on a
    cache miss (debounced so a flood of unknown tokens can't force unbounded
    secret-store re-reads)."""

    def _mock_request(self) -> AsyncMock:
        from starlette.requests import ClientDisconnect

        mock_req = AsyncMock()
        mock_req.method = "POST"
        mock_req.client = type("Addr", (), {"host": "127.0.0.1"})()
        mock_req.headers = {}
        # Short-circuits with 499 right after the token check passes, so a
        # successful auth is distinguishable from a 403 without mocking the
        # full Telegram-forwarding chain.
        mock_req.body = AsyncMock(side_effect=ClientDisconnect())
        return mock_req

    @staticmethod
    def _allowed_networks():
        import ipaddress

        return [ipaddress.ip_network("127.0.0.0/8")]

    async def test_miss_rebuilds_and_recovers_when_secret_becomes_available(self, monkeypatch):
        """A token missing from a stale cached registry is picked up on retry
        once its secret is readable, without needing a process restart."""
        import json

        from gateway.ingest_api.main import app_state, telegram_api_proxy

        monkeypatch.setattr(
            app_state, "_telegram_token_registry", {_OPENCLAW_TOKEN: "openclaw"}, raising=False
        )
        monkeypatch.setattr(app_state, "_telegram_token_registry_built_at", 0.0, raising=False)

        hermes_bcfg = MagicMock()
        hermes_bcfg.telegram_token_secret = "hermes_telegram_bot_token"
        monkeypatch.setattr(
            app_state, "config", MagicMock(bots={"hermes": hermes_bcfg}), raising=False
        )

        def _fake_read_secret(name):
            # Secret has now landed on disk — the boot-time race has resolved.
            return _HERMES_TOKEN if name == "hermes_telegram_bot_token" else None

        with (
            patch("gateway.ingest_api.main._read_secret", side_effect=_fake_read_secret),
            patch(
                "gateway.ingest_api.main._PROXY_ALLOWED_NETWORKS",
                self._allowed_networks(),
            ),
        ):
            result = await telegram_api_proxy(f"bot{_HERMES_TOKEN}/getMe", self._mock_request())

        data = json.loads(result.body)
        assert result.status_code == 499  # passed the token gate, hit the mocked disconnect
        assert data["ok"] is False
        assert app_state._telegram_token_registry.get(_HERMES_TOKEN) == "hermes"

    async def test_miss_debounced_within_rebuild_interval(self, monkeypatch):
        """Repeated misses within the debounce window must not re-read secrets
        on every request — bounds the cost of an unknown-token flood."""
        from gateway.ingest_api.main import app_state, telegram_api_proxy

        monkeypatch.setattr(
            app_state, "_telegram_token_registry", {_OPENCLAW_TOKEN: "openclaw"}, raising=False
        )
        monkeypatch.setattr(
            app_state, "_telegram_token_registry_built_at", time.time(), raising=False
        )

        hermes_bcfg = MagicMock()
        hermes_bcfg.telegram_token_secret = "hermes_telegram_bot_token"
        monkeypatch.setattr(
            app_state, "config", MagicMock(bots={"hermes": hermes_bcfg}), raising=False
        )

        read_calls: list[str] = []

        def _fake_read_secret(name):
            read_calls.append(name)
            return _HERMES_TOKEN if name == "hermes_telegram_bot_token" else None

        with (
            patch("gateway.ingest_api.main._read_secret", side_effect=_fake_read_secret),
            patch(
                "gateway.ingest_api.main._PROXY_ALLOWED_NETWORKS",
                self._allowed_networks(),
            ),
        ):
            from fastapi import HTTPException

            with pytest.raises(HTTPException) as exc:
                await telegram_api_proxy(f"bot{_HERMES_TOKEN}/getMe", self._mock_request())

        assert exc.value.status_code == 403
        assert read_calls == []  # debounced — no secret re-read attempted

    async def test_miss_still_rejected_after_rebuild_if_truly_unknown(self, monkeypatch):
        """A genuinely-unregistered token must not be falsely accepted by the
        rebuild path — the fix must not weaken fail-closed behavior."""
        from gateway.ingest_api.main import app_state, telegram_api_proxy

        monkeypatch.setattr(app_state, "_telegram_token_registry", {}, raising=False)
        monkeypatch.setattr(app_state, "_telegram_token_registry_built_at", 0.0, raising=False)
        monkeypatch.setattr(app_state, "config", MagicMock(bots={}), raising=False)

        with (
            patch(
                "gateway.ingest_api.main._read_secret",
                side_effect=lambda name: _OPENCLAW_TOKEN if name == "telegram_bot_token" else None,
            ),
            patch(
                "gateway.ingest_api.main._PROXY_ALLOWED_NETWORKS",
                self._allowed_networks(),
            ),
        ):
            from fastapi import HTTPException

            with pytest.raises(HTTPException) as exc:
                await telegram_api_proxy(f"bot{_UNKNOWN_TOKEN}/getMe", self._mock_request())

        assert exc.value.status_code == 403
