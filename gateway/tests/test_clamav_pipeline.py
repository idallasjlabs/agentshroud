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
import os
import shutil
import socket
import subprocess
import tempfile
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from gateway.proxy.pipeline import PipelineAction, SecurityPipeline
from gateway.security import clamav_scanner
from gateway.security.clamav_scanner import scan_bytes

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


async def _timeout_wait_for(coro, timeout):
    """Test replacement for asyncio.wait_for — raises TimeoutError.

    Closes the un-awaited coroutine first, otherwise its garbage collection
    emits 'coroutine was never awaited' in whatever test runs next.
    """
    coro.close()
    raise asyncio.TimeoutError()


@pytest.mark.asyncio
async def test_scan_bytes_timeout():
    mock_proc = AsyncMock()
    with patch("asyncio.create_subprocess_exec", return_value=mock_proc):
        with patch("asyncio.wait_for", new=_timeout_wait_for):
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


# ---------------------------------------------------------------------------
# clamd detection — 2026-10-18 gateway OOM: callers probed a socket path that
# never exists, so every scan loaded a second ~1 GB DB via clamscan.
# ---------------------------------------------------------------------------


@pytest.fixture
def clamd_sock_path():
    # Short dir: AF_UNIX paths are capped at ~104 bytes on macOS.
    d = tempfile.mkdtemp(prefix="cd", dir="/tmp")
    yield os.path.join(d, "clamd.ctl")
    shutil.rmtree(d, ignore_errors=True)


def test_clamd_socket_constant_matches_both_images_clamd_conf():
    want = f"LocalSocket {clamav_scanner.CLAMD_SOCKET}"
    assert want in Path("gateway/Dockerfile").read_text(encoding="utf-8")
    assert want in Path("docker/bots/openclaw/Dockerfile").read_text(encoding="utf-8")


# CVE-2026-20213..20216 (2026-10-22): trixie ships clamav 1.4.3; the fix,
# 1.4.6+dfsg-1~deb13u1, is only in trixie-proposed-updates. Both images take
# ClamAV (and nothing else) from there until it reaches a point release.
_IMAGES_WITH_CLAMAV = ("gateway/Dockerfile", "docker/bots/openclaw/Dockerfile")


@pytest.mark.parametrize("dockerfile", _IMAGES_WITH_CLAMAV)
def test_clamav_comes_from_proposed_updates_and_nothing_else_does(dockerfile):
    text = Path(dockerfile).read_text(encoding="utf-8")
    assert "Suites: trixie-proposed-updates" in text
    # Every other package stays on stable: proposed-updates defaults to priority 1.
    assert "Package: *\\nPin: release a=trixie-proposed-updates\\nPin-Priority: 1\\n" in text
    assert (
        "Package: clamav* clamdscan libclamav*\\nPin: release a=trixie-proposed-updates\\n"
        "Pin-Priority: 990\\n"
    ) in text


# GHSA-6q48-6c7w-9gw2 (CRITICAL, 2026-10-20): the python:3.13-slim base ships
# pip 26.2.1, whose vendored certifi (2026.06.17) bundles the compromised emSign
# roots. pip 26.2.2 vendors certifi 2026.10.19.
def test_gateway_upgrades_pip_past_the_vendored_certifi_advisory():
    assert '"pip>=26.2.2"' in Path("gateway/Dockerfile").read_text(encoding="utf-8")


# The 2026-03-27 `Trusted: yes` workaround (apt 2.6 arm64/bookworm gpgv bug)
# turned off repo signature checks. OpenClaw removed it on trixie 2026-09-24;
# the gateway kept it. An image that installs unverified packages is a
# supply-chain exposure.
@pytest.mark.parametrize("dockerfile", _IMAGES_WITH_CLAMAV)
def test_apt_repo_signatures_are_verified(dockerfile):
    code = "\n".join(
        line
        for line in Path(dockerfile).read_text(encoding="utf-8").splitlines()
        if not line.lstrip().startswith("#")
    )
    assert "Trusted: yes" not in code
    assert "trusted=yes" not in code


def test_clamd_available_true_when_daemon_listening(clamd_sock_path):
    srv = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    srv.bind(clamd_sock_path)
    srv.listen(1)
    try:
        assert clamav_scanner.clamd_available(clamd_sock_path) is True
    finally:
        srv.close()


def test_clamd_available_false_for_stale_socket_left_by_killed_daemon(clamd_sock_path):
    srv = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    srv.bind(clamd_sock_path)
    srv.close()  # daemon gone, socket file remains (what an OOM kill leaves)
    assert os.path.exists(clamd_sock_path)
    assert clamav_scanner.clamd_available(clamd_sock_path) is False


def test_clamd_available_false_when_socket_missing(clamd_sock_path):
    assert clamav_scanner.clamd_available(clamd_sock_path) is False


def test_preferred_scan_binary_uses_daemon_when_listening(clamd_sock_path):
    srv = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    srv.bind(clamd_sock_path)
    srv.listen(1)
    try:
        with patch.object(clamav_scanner.shutil, "which", return_value="/usr/bin/clamdscan"):
            assert clamav_scanner.preferred_scan_binary(clamd_sock_path) == "clamdscan"
        with patch.object(clamav_scanner.shutil, "which", return_value=None):
            assert clamav_scanner.preferred_scan_binary(clamd_sock_path) == "clamscan"
    finally:
        srv.close()


def test_preferred_scan_binary_falls_back_when_daemon_dead(clamd_sock_path):
    with patch.object(clamav_scanner.shutil, "which", return_value="/usr/bin/clamdscan"):
        assert clamav_scanner.preferred_scan_binary(clamd_sock_path) == "clamscan"


def _run_capture(**kwargs):
    seen = {}

    def fake_run(cmd, **_kw):
        seen["cmd"] = cmd
        return subprocess.CompletedProcess(cmd, 0, stdout="", stderr="")

    with patch.object(clamav_scanner.subprocess, "run", side_effect=fake_run):
        result = clamav_scanner.run_clamscan(target="/app", **kwargs)
    return seen["cmd"], result


def test_run_clamscan_clamdscan_command_has_no_clamscan_only_flags():
    cmd, result = _run_capture(clamscan_bin="clamdscan", exclude_patterns=["x"])
    assert cmd == ["clamdscan", "--no-summary", "--fdpass", "/app"]
    assert result["infected_count"] == 0


def test_run_clamscan_clamscan_command_unchanged():
    cmd, _ = _run_capture(clamscan_bin="clamscan", exclude_patterns=["x"])
    assert cmd == ["clamscan", "--no-summary", "-r", "--exclude", "x", "/app"]
