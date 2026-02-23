# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tests for the canary verification system."""
from __future__ import annotations


import pytest

from gateway.security.canary import (
    CANARY_EMAIL,
    CANARY_MESSAGE,
    CANARY_SSN,
    run_canary,
)
from gateway.proxy.pipeline import SecurityPipeline
from gateway.proxy.forwarder import ForwarderConfig, HTTPForwarder
from gateway.security.prompt_guard import PromptGuard
from gateway.security.trust_manager import TrustManager
from gateway.ingest_api.sanitizer import PIISanitizer
from gateway.ingest_api.config import PIIConfig


@pytest.fixture
def canary_pipeline():
    pii_config = PIIConfig(
        engine="regex",
        entities=["US_SSN", "CREDIT_CARD", "PHONE_NUMBER", "EMAIL_ADDRESS"],
        enabled=True,
    )
    sanitizer = PIISanitizer(pii_config)
    prompt_guard = PromptGuard()
    trust_manager = TrustManager(db_path=":memory:")
    trust_manager.register_agent("canary")

    return SecurityPipeline(
        prompt_guard=prompt_guard,
        pii_sanitizer=sanitizer,
        trust_manager=trust_manager,
    )


@pytest.fixture
def healthy_forwarder():
    f = HTTPForwarder(ForwarderConfig())
    f.set_response_handler(lambda p, b: (200, '{"status": "ok"}'))
    return f


@pytest.fixture
def unhealthy_forwarder():
    f = HTTPForwarder(ForwarderConfig(max_retries=0))
    f.set_response_handler(lambda p, b: (500, "Internal Server Error"))
    return f


@pytest.mark.asyncio
async def test_canary_passes_with_pipeline(canary_pipeline):
    """Canary should pass when pipeline is properly configured."""
    result = await run_canary(pipeline=canary_pipeline)
    assert result.verified is True
    assert result.checks["pii"] is True
    assert result.checks["audit"] is True
    assert result.checks["chain"] is True
    assert result.checks["proxy"] is True  # No forwarder = test mode = pass
    assert result.timestamp
    assert result.duration_ms >= 0


@pytest.mark.asyncio
async def test_canary_verifies_pii_stripping(canary_pipeline):
    """Canary should detect that fake PII was stripped."""
    result = await run_canary(pipeline=canary_pipeline)
    assert result.checks["pii"] is True
    pii_detail = next(c for c in result.check_details if c.name == "pii")
    assert (
        "stripped" in pii_detail.details.lower()
        or "redaction" in pii_detail.details.lower()
    )


@pytest.mark.asyncio
async def test_canary_verifies_audit_chain(canary_pipeline):
    """Canary should verify audit chain integrity."""
    result = await run_canary(pipeline=canary_pipeline)
    assert result.checks["chain"] is True
    chain_detail = next(c for c in result.check_details if c.name == "chain")
    assert "valid" in chain_detail.details.lower()


@pytest.mark.asyncio
async def test_canary_with_healthy_forwarder(canary_pipeline, healthy_forwarder):
    """Canary should pass proxy check with healthy forwarder."""
    result = await run_canary(pipeline=canary_pipeline, forwarder=healthy_forwarder)
    assert result.checks["proxy"] is True


@pytest.mark.asyncio
async def test_canary_with_unhealthy_forwarder(canary_pipeline, unhealthy_forwarder):
    """Canary should fail proxy check with unhealthy forwarder."""
    result = await run_canary(pipeline=canary_pipeline, forwarder=unhealthy_forwarder)
    assert result.checks["proxy"] is False
    assert result.verified is False


@pytest.mark.asyncio
async def test_canary_fails_without_pipeline():
    """Canary should fail when no pipeline configured."""
    result = await run_canary(pipeline=None)
    assert result.verified is False
    assert result.checks["pii"] is False
    assert result.checks["audit"] is False
    assert result.checks["chain"] is False


@pytest.mark.asyncio
async def test_canary_result_serialization(canary_pipeline):
    """Canary result should serialize to dict properly."""
    result = await run_canary(pipeline=canary_pipeline)
    d = result.to_dict()
    assert isinstance(d, dict)
    assert "verified" in d
    assert "checks" in d
    assert "check_details" in d
    assert isinstance(d["check_details"], list)
    assert len(d["check_details"]) == 4


@pytest.mark.asyncio
async def test_canary_message_contains_fake_pii():
    """Verify canary message contains the expected fake PII."""
    assert CANARY_SSN in CANARY_MESSAGE
    assert CANARY_EMAIL in CANARY_MESSAGE
