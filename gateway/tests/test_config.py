"""Tests for configuration loading"""

import pytest
from pathlib import Path

from gateway.ingest_api.config import load_config


def test_load_config():
    """Test loading configuration from secureclaw.yaml"""
    # This should find ../secureclaw.yaml from the tests directory
    config = load_config()

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


def test_entity_type_mapping():
    """Test PII entity type mapping"""
    from gateway.ingest_api.config import _entity_type_mapping

    assert _entity_type_mapping("SSN") == "US_SSN"
    assert _entity_type_mapping("CREDIT_CARD") == "CREDIT_CARD"
    assert _entity_type_mapping("STREET_ADDRESS") == "LOCATION"
    assert _entity_type_mapping("UNKNOWN") == "UNKNOWN"  # Passthrough
