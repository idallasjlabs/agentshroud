# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for ClamAV inline pipeline integration.

Covers:
  - scan_bytes() happy path: clean data
  - scan_bytes() malware detected: returns infected_count > 0
  - scan_bytes() error paths: binary not found, timeout
  - SecurityPipeline Step 2.5: base64 payload with malware → BLOCK
  - SecurityPipeline Step 2.5: clean base64 payload → FORWARD
  - SecurityPipeline Step 2.5: no clamav_scanner configured → skipped (no error)
  - SecurityPipeline Step 2.5: clamav_scanner error → fail-open (FORWARD + CRITICAL log)
"""

from __future__ import annotations

import asyncio
import base64
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from gateway.proxy.pipeline import PipelineAction, SecurityPipeline
from gateway.security.clamav_scanner import parse_clamscan_output, scan_bytes

# ---------------------------------------------------------------------------
# scan_bytes unit tests
# ---------------------------------------------------------------------------


@pytest.mark.asyncio
async def test_scan_bytes_empty_input():
    result = await scan_bytes(b"")
    assert result["infected_count"] == 0
    assert result["scanned_bytes"] == 0
    assert result["error"] is None


@pytest.mark.asyncio
async def test_scan_bytes_binary_not_found():
    with patch(
        "asyncio.create_subprocess_exec", side_effect=FileNotFoundError("clamdscan not found")
    ):
        result = await scan_bytes(b"hello world" * 50)
    assert result["infected_count"] == 0
    assert result["error"] == "binary_not_found"


@pytest.mark.asyncio
async def test_scan_bytes_timeout():
    mock_proc = AsyncMock()
    with patch("asyncio.create_subprocess_exec", return_value=mock_proc):
        with patch("asyncio.wait_for", side_effect=asyncio.TimeoutError()):
            result = await scan_bytes(b"x" * 500, timeout=1)
    assert result["infected_count"] == 0
    assert result["error"] == "timeout"


async def _instant_wait_for(coro, timeout):
    """Test replacement for asyncio.wait_for — awaits coroutine directly."""
    return await coro


@pytest.mark.asyncio
async def test_scan_bytes_clean():
    mock_proc = AsyncMock()
    mock_proc.returncode = 0
    mock_proc.communicate = AsyncMock(return_value=(b"/tmp/file: OK\n", b""))

    with patch("asyncio.create_subprocess_exec", return_value=mock_proc):
        with patch("asyncio.wait_for", new=_instant_wait_for):
            result = await scan_bytes(b"safe data " * 100)
    assert result["infected_count"] == 0
    assert result["error"] is None
    assert result["scanned_bytes"] > 0


@pytest.mark.asyncio
async def test_scan_bytes_infected():
    eicar_output = b"stream: Eicar-Test-Signature FOUND\n"
    mock_proc = AsyncMock()
    mock_proc.returncode = 1
    mock_proc.communicate = AsyncMock(return_value=(eicar_output, b""))

    with patch("asyncio.create_subprocess_exec", return_value=mock_proc):
        with patch("asyncio.wait_for", new=_instant_wait_for):
            result = await scan_bytes(b"X5O!P%@AP[4" * 10)
    assert result["infected_count"] == 1
    assert result["infected_files"][0]["signature"] == "Eicar-Test-Signature"


# ---------------------------------------------------------------------------
# Pipeline integration tests
# ---------------------------------------------------------------------------


def _make_pipeline(clamav_fn=None):
    """Build a minimal SecurityPipeline with passthrough PII + optional clamav."""
    pii = MagicMock()

    async def _passthrough(text):
        return MagicMock(sanitized_content=text, entity_types_found=[], redactions=[])

    pii.sanitize = _passthrough
    pii.filter_xml_blocks = MagicMock(return_value=("", False))
    return SecurityPipeline(pii_sanitizer=pii, clamav_scanner=clamav_fn)


def _b64_payload(content: bytes) -> str:
    """Wrap bytes in a long-enough base64 chunk to trigger the scan (>= 64 groups of 4)."""
    # Pad to ensure ≥ 256 decoded bytes for the chunk check
    padded = content + b"\x00" * max(0, 256 - len(content))
    return base64.b64encode(padded).decode()


@pytest.mark.asyncio
async def test_pipeline_clamav_clean_payload():
    """Clean base64 payload → FORWARD."""
    clamav_fn = AsyncMock(return_value={"infected_count": 0, "infected_files": [], "error": None})
    pipeline = _make_pipeline(clamav_fn)
    payload = _b64_payload(b"clean data " * 30)
    result = await pipeline.process_inbound(f"check this: {payload}", agent_id="agent1")
    assert result.action == PipelineAction.FORWARD
    assert not result.blocked


@pytest.mark.asyncio
async def test_pipeline_clamav_malware_blocked():
    """Malware-infected base64 payload → BLOCK with signature in block_reason."""
    clamav_fn = AsyncMock(
        return_value={
            "infected_count": 1,
            "infected_files": [{"file": "stream", "signature": "Eicar-Test-Signature"}],
            "error": None,
        }
    )
    pipeline = _make_pipeline(clamav_fn)
    payload = _b64_payload(b"EICAR" * 60)
    result = await pipeline.process_inbound(f"run this: {payload}", agent_id="agent1")
    assert result.action == PipelineAction.BLOCK
    assert result.blocked
    assert "Eicar-Test-Signature" in result.block_reason


@pytest.mark.asyncio
async def test_pipeline_clamav_not_configured():
    """No clamav_scanner configured → step skipped, no error."""
    pipeline = _make_pipeline(clamav_fn=None)
    result = await pipeline.process_inbound("hello world", agent_id="agent1")
    assert result.action == PipelineAction.FORWARD


@pytest.mark.asyncio
async def test_pipeline_clamav_error_fail_open(caplog):
    """ClamAV scan_bytes returns error → fail-open: CRITICAL log, FORWARD."""
    clamav_fn = AsyncMock(
        return_value={
            "infected_count": 0,
            "error": "binary_not_found",
        }
    )
    pipeline = _make_pipeline(clamav_fn)
    payload = _b64_payload(b"data " * 60)
    import logging

    with caplog.at_level(logging.CRITICAL, logger="agentshroud.proxy.pipeline"):
        result = await pipeline.process_inbound(f"scan this: {payload}", agent_id="agent1")
    assert result.action == PipelineAction.FORWARD
    assert any("binary_not_found" in r.message for r in caplog.records)


@pytest.mark.asyncio
async def test_pipeline_short_base64_not_scanned():
    """Short base64 (<64 groups of 4) skips ClamAV scan."""
    clamav_fn = AsyncMock(
        return_value={
            "infected_count": 1,
            "infected_files": [{"file": "x", "signature": "Test"}],
            "error": None,
        }
    )
    pipeline = _make_pipeline(clamav_fn)
    # Short base64 (< 256 bytes decoded) — should NOT trigger scan
    short_b64 = base64.b64encode(b"short " * 5).decode()
    result = await pipeline.process_inbound(f"val: {short_b64}", agent_id="agent1")
    # clamav_fn should NOT have been called (message too short)
    clamav_fn.assert_not_called()
    assert result.action == PipelineAction.FORWARD
