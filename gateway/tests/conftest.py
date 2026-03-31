# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Shared test fixtures for AgentShroud Gateway tests"""


import sys
import tempfile
from pathlib import Path

import pytest

# Allow bare `from security.xxx` and `from ingest_api.xxx` imports in test files
# that were written relative to the gateway/ package root.
_gateway_root = str(Path(__file__).parent.parent)
if _gateway_root not in sys.path:
    sys.path.insert(0, _gateway_root)

# Pre-register gateway sub-packages under their bare names so that relative
# imports inside those packages resolve correctly (avoids "attempted relative
# import beyond top-level package" errors when loaded as top-level).
import importlib as _importlib

_ALIAS_MAP = [
    ("security", "gateway.security"),
    ("proxy", "gateway.proxy"),
    ("ingest_api", "gateway.ingest_api"),
    # Sub-modules accessed directly by test_security_audit_advanced.py
    ("ingest_api.sanitizer", "gateway.ingest_api.sanitizer"),
    ("ingest_api.config", "gateway.ingest_api.config"),
    ("ingest_api.models", "gateway.ingest_api.models"),
]
for _alias, _full in _ALIAS_MAP:
    if _alias not in sys.modules:
        try:
            _mod = _importlib.import_module(_full)
            sys.modules[_alias] = _mod
        except Exception:
            pass
import pytest_asyncio
from fastapi.testclient import TestClient

from gateway.ingest_api.config import (
    ApprovalQueueConfig,
    GatewayConfig,
    LedgerConfig,
    PIIConfig,
    RouterConfig,
)
from gateway.ingest_api.ledger import DataLedger
from gateway.ingest_api.main import app, app_state
from gateway.ingest_api.sanitizer import PIISanitizer


@pytest.fixture
def test_config() -> GatewayConfig:
    """Create a test configuration

    Uses regex fallback for PII (no spaCy model required).
    Uses in-memory SQLite for ledger.
    Sets a known auth token for testing.
    """
    return GatewayConfig(
        bind="127.0.0.1",
        port=8080,
        auth_method="shared_secret",
        auth_token="test-token-12345",
        ledger=LedgerConfig(
            backend="sqlite",
            path=Path(":memory:"),  # In-memory database
            retention_days=90,
        ),
        router=RouterConfig(
            enabled=True,
            default_target="test-agent",
            targets={},
        ),
        pii=PIIConfig(
            engine="regex",  # Force regex mode (no spaCy)
            entities=["US_SSN", "CREDIT_CARD", "PHONE_NUMBER", "EMAIL_ADDRESS"],
            enabled=True,
        ),
        approval_queue=ApprovalQueueConfig(
            enabled=True,
            actions=["email_sending", "file_deletion"],
            timeout_seconds=3600,
            db_path=str(Path(tempfile.mkdtemp()) / "test_approvals.db"),
        ),
        log_level="WARNING",  # Reduce test noise
    )


@pytest_asyncio.fixture
async def test_ledger(test_config: GatewayConfig):
    """Create an initialized in-memory ledger for testing

    Yields the ledger, then closes it.
    """
    # Use a temporary file instead of :memory: for proper async testing
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as tmp:
        tmp_path = Path(tmp.name)

    config = LedgerConfig(
        backend="sqlite",
        path=tmp_path,
        retention_days=90,
    )

    ledger = DataLedger(config)
    await ledger.initialize()

    yield ledger

    await ledger.close()
    tmp_path.unlink()  # Clean up


@pytest.fixture
def auth_headers() -> dict[str, str]:
    """Return Authorization headers with test token"""
    return {"Authorization": "Bearer test-token-12345"}


@pytest.fixture
def test_client(test_config: GatewayConfig):
    """Create a FastAPI TestClient with test configuration

    Note: This doesn't initialize the full application state.
    Use integration tests for full endpoint testing.
    """
    app_state.config = test_config

    with TestClient(app) as client:
        yield client


@pytest.fixture
def sanitizer(test_config: GatewayConfig) -> PIISanitizer:
    """Create a PIISanitizer instance for testing"""
    return PIISanitizer(test_config.pii)


# Note: Removed custom event_loop fixture to use pytest-asyncio's built-in
# This eliminates deprecation warnings and uses the recommended approach
