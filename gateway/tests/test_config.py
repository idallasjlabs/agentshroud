# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for configuration loading"""

from __future__ import annotations

from pathlib import Path

from gateway.ingest_api.config import load_config

REPO_ROOT = Path(__file__).resolve().parents[2]


def _load_config():
    """Load the real agentshroud.yaml when present (deployment host), else the
    committed agentshroud.yaml.example (CI), so these tests always execute."""
    try:
        return load_config()
    except FileNotFoundError:
        return load_config(REPO_ROOT / "agentshroud.yaml.example")


def test_load_config():
    """Test loading configuration from agentshroud.yaml (or the committed example)."""
    config = _load_config()

    assert config is not None
    assert config.bind == "127.0.0.1"
    assert config.port == 8080
    assert config.pii.enabled is True
    assert "US_SSN" in config.pii.entities or "EMAIL_ADDRESS" in config.pii.entities
    assert config.ledger.retention_days == 90


def test_config_defaults():
    """Test that configuration has sensible defaults"""
    from gateway.ingest_api.config import GatewayConfig

    config = GatewayConfig()

    assert config.bind == "127.0.0.1"
    assert config.port == 8080
    assert config.log_level == "INFO"


def test_load_config_has_bots():
    """Test that load_config() populates bots — from YAML or backward-compat default."""
    config = _load_config()

    assert config.bots, "bots dict must not be empty"
    default_bots = [b for b in config.bots.values() if b.default]
    assert len(default_bots) == 1, "exactly one bot must be marked default"
    default_bot = default_bots[0]
    assert default_bot.hostname, "default bot must have a hostname"
    assert default_bot.port > 0, "default bot must have a port"
    # Router default_url must point at the default bot
    assert str(default_bot.port) in config.router.default_url
    assert default_bot.hostname in config.router.default_url


def test_bot_config_base_url():
    """BotConfig.base_url computes http://{hostname}:{port}."""
    from gateway.ingest_api.bot_config import BotConfig

    bot = BotConfig(
        id="test",
        name="Test Bot",
        hostname="mybot",
        port=9000,
        workspace_path="/app/workspace",
        config_dir="/app/config",
    )
    assert bot.base_url == "http://mybot:9000"


def test_bot_config_resolved_container_name_defaults_to_agentshroud_id():
    """No explicit container_name — derives 'agentshroud-{id}' (openclaw's case)."""
    from gateway.ingest_api.bot_config import BotConfig

    bot = BotConfig(
        id="openclaw",
        name="OpenClaw",
        hostname="agentshroud",
        port=18789,
        workspace_path="/app/workspace",
        config_dir="/app/config",
    )
    assert bot.resolved_container_name == "agentshroud-openclaw"


def test_bot_config_resolved_container_name_uses_explicit_override():
    """Explicit container_name wins over the 'agentshroud-{id}' convention —
    regression guard for the real bug: hermes's container was renamed to
    'agentshroud-hermes-v2' but the dashboard's Services page kept computing
    'agentshroud-hermes', so docker inspect always found nothing and Hermes
    was reported stopped/unknown despite running healthy."""
    from gateway.ingest_api.bot_config import BotConfig

    bot = BotConfig(
        id="hermes",
        name="Hermes Agent",
        hostname="agentshroud-hermes-v2",
        container_name="agentshroud-hermes-v2",
        port=8642,
        workspace_path="/opt/data/home",
        config_dir="/opt/data",
    )
    assert bot.resolved_container_name == "agentshroud-hermes-v2"


def test_bot_service_names_uses_resolved_container_name():
    """_bot_service_names() must use each bot's real container name, not a
    hardcoded 'agentshroud-{bot_id}' guess that breaks on rename."""
    from gateway.web.api import _bot_service_names

    names = _bot_service_names()
    assert "agentshroud-openclaw" in names
    assert "agentshroud-hermes-v2" in names
    assert "agentshroud-hermes" not in names


def test_router_config_accepts_docker_service_hostname():
    """RouterConfig should accept single-label Docker service hostnames."""
    from gateway.ingest_api.config import RouterConfig

    # Single-label name (no dot) — Docker service hostname
    cfg = RouterConfig(default_url="http://agentshroud:18789")
    assert cfg.default_url == "http://agentshroud:18789"

    cfg2 = RouterConfig(default_url="http://nanobot:8000")
    assert cfg2.default_url == "http://nanobot:8000"


def test_entity_type_mapping():
    """Test PII entity type mapping"""
    from gateway.ingest_api.config import _entity_type_mapping

    assert _entity_type_mapping("SSN") == "US_SSN"
    assert _entity_type_mapping("CREDIT_CARD") == "CREDIT_CARD"
    assert _entity_type_mapping("STREET_ADDRESS") == "LOCATION"
    assert _entity_type_mapping("UNKNOWN") == "UNKNOWN"  # Passthrough


def test_load_config_registers_hermes():
    """When agentshroud.yaml declares hermes:, load_config() populates it in bots."""
    config = _load_config()

    assert "hermes" in config.bots, "hermes must be declared in agentshroud.yaml bots: section"
    hermes = config.bots["hermes"]
    assert hermes.port == 8642, "Hermes gateway API port must be 8642"
    assert hermes.default is False, "Hermes must NOT be the default bot (OpenClaw is)"
    # Renamed 2026-07-18 (see docker-compose.yml) — was "agentshroud-hermes".
    assert hermes.hostname == "agentshroud-hermes-v2"
    assert hermes.resolved_container_name == "agentshroud-hermes-v2"
    assert hermes.chat_path == "/v1/chat/completions"
    assert hermes.telegram_token_secret == "hermes_telegram_bot_token"
    assert "api.telegram.org" in hermes.egress_domains


def test_router_config_accepts_hermes_hostname():
    """RouterConfig must accept the Hermes Docker service hostname."""
    from gateway.ingest_api.config import RouterConfig

    cfg = RouterConfig(default_url="http://agentshroud-hermes:8642")
    assert cfg.default_url == "http://agentshroud-hermes:8642"
