# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for gateway/security/image_verifier.py.

Covers:
  - verify_image: cosign binary not found → error, not verified
  - verify_image: cosign succeeds → verified=True
  - verify_image: cosign fails (bad signature) → verified=False, error set
  - verify_image: timeout → verified=False, error="timeout"
  - verify_images: multiple images, mixed results
"""
from __future__ import annotations

import asyncio
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from gateway.security.image_verifier import verify_image, verify_images


async def _instant_wait_for(coro, timeout):
    """Test replacement for asyncio.wait_for — awaits coroutine directly."""
    return await coro


@pytest.mark.asyncio
async def test_cosign_not_found():
    with patch("shutil.which", return_value=None):
        result = await verify_image("ghcr.io/example/app:latest")
    assert result["verified"] is False
    assert "not found" in result["error"]
    assert result["image_ref"] == "ghcr.io/example/app:latest"
    assert result["timestamp"]


@pytest.mark.asyncio
async def test_cosign_success():
    mock_proc = AsyncMock()
    mock_proc.returncode = 0
    mock_proc.communicate = AsyncMock(return_value=(b'[{"critical": {}}]', b""))

    with patch("shutil.which", return_value="/usr/local/bin/cosign"):
        with patch("asyncio.create_subprocess_exec", return_value=mock_proc):
            with patch("asyncio.wait_for", new=_instant_wait_for):
                result = await verify_image("ghcr.io/example/app:sha256-abc")

    assert result["verified"] is True
    assert result["error"] is None


@pytest.mark.asyncio
async def test_cosign_fails_bad_signature():
    mock_proc = AsyncMock()
    mock_proc.returncode = 1
    mock_proc.communicate = AsyncMock(return_value=(b"", b"Error: no matching signatures\n"))

    with patch("shutil.which", return_value="/usr/local/bin/cosign"):
        with patch("asyncio.create_subprocess_exec", return_value=mock_proc):
            with patch("asyncio.wait_for", new=_instant_wait_for):
                result = await verify_image("ghcr.io/example/app:sha256-bad")

    assert result["verified"] is False
    assert "no matching signatures" in result["error"]


@pytest.mark.asyncio
async def test_cosign_timeout():
    with patch("shutil.which", return_value="/usr/local/bin/cosign"):
        with patch("asyncio.create_subprocess_exec"):
            with patch("asyncio.wait_for", side_effect=asyncio.TimeoutError()):
                result = await verify_image("ghcr.io/example/app:latest", timeout=5)

    assert result["verified"] is False
    assert "timed out" in result["error"]


@pytest.mark.asyncio
async def test_verify_images_mixed():
    """verify_images: one succeeds, one fails → results keyed by ref."""

    async def _mock_verify(ref, **kwargs):
        if "good" in ref:
            return {"image_ref": ref, "verified": True, "error": None, "timestamp": "t"}
        return {"image_ref": ref, "verified": False, "error": "no sig", "timestamp": "t"}

    with patch("gateway.security.image_verifier.verify_image", side_effect=_mock_verify):
        results = await verify_images(["ghcr.io/good:1", "ghcr.io/bad:1"])

    assert results["ghcr.io/good:1"]["verified"] is True
    assert results["ghcr.io/bad:1"]["verified"] is False
    assert results["ghcr.io/bad:1"]["error"] == "no sig"


@pytest.mark.asyncio
async def test_verify_images_exception_handled():
    """verify_images: exception from one task is caught, others continue."""

    async def _mock_verify(ref, **kwargs):
        if "boom" in ref:
            raise RuntimeError("unexpected")
        return {"image_ref": ref, "verified": True, "error": None, "timestamp": "t"}

    with patch("gateway.security.image_verifier.verify_image", side_effect=_mock_verify):
        results = await verify_images(["ghcr.io/ok:1", "ghcr.io/boom:1"])

    assert results["ghcr.io/ok:1"]["verified"] is True
    assert results["ghcr.io/boom:1"]["verified"] is False
    assert "unexpected" in results["ghcr.io/boom:1"]["error"]
