# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for configuration loading"""

from __future__ import annotations

import pytest

from gateway.ingest_api.config import load_config


def test_load_config():
    """Test loading configuration from agentshroud.yaml.

    Skipped in CI where agentshroud.yaml is not present (config lives on the
    deployment host, not in the repo).  Run locally against a real config.
    """
    try:
        config = load_config()
    except FileNotFoundError:
        pytest.skip("agentshroud.yaml not found — skipped in CI")

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
    try:
        config = load_config()
    except FileNotFoundError:
        pytest.skip("agentshroud.yaml not found — skipped in CI")

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
