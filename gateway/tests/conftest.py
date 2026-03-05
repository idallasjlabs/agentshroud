# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Shared test fixtures for AgentShroud Gateway tests"""


import tempfile
from pathlib import Path

import pytest
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
