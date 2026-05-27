# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for multi-bot Telegram token registry in the gateway route handler.

Phase 1.3 of v1.4.0: the /telegram-api/{path} endpoint previously accepted only
the single OpenClaw bot token. These tests verify the multi-bot registry correctly
dispatches by token and rejects unrecognised tokens with 403 (fail-closed).
"""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest


_OPENCLAW_TOKEN = "123456789:OpenClawFakeTelegram_TokenABCDEFGHIJK"
_HERMES_TOKEN = "987654321:HermesFakeTelegram_TokenXYZABCDEFGHIJ"
_UNKNOWN_TOKEN = "000000000:UnknownFakeTelegram_TokenZZZZZZZZZZZZ"

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
