# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Container image signature verification using cosign.

Verifies that the running container images were signed by the CI pipeline
using keyless OIDC (Sigstore).  Runs at gateway startup as a background task.

Fail mode: if cosign binary is not found or verification fails, log a WARNING
(not CRITICAL) — dev environments use unsigned local builds.  Only in production
environments with AGENTSHROUD_IMAGE_VERIFICATION_ENFORCE=1 does failure block startup.
"""

import asyncio
import logging
import shutil
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

# Environment variable to set the expected OIDC issuer (default: GitHub Actions)
_DEFAULT_OIDC_ISSUER = "https://token.actions.githubusercontent.com"
# Regexp matching any GitHub Actions identity in the repository
_DEFAULT_IDENTITY_REGEXP = r"https://github\.com/.*/\.github/workflows/.*"


async def verify_image(
    image_ref: str,
    certificate_oidc_issuer: str = _DEFAULT_OIDC_ISSUER,
    certificate_identity_regexp: str = _DEFAULT_IDENTITY_REGEXP,
    timeout: int = 30,
) -> dict:
    """Verify an image signature using cosign keyless OIDC verification.

    Args:
        image_ref: Docker image reference (registry/repo:tag or digest).
        certificate_oidc_issuer: Expected OIDC issuer URL.
        certificate_identity_regexp: Regexp matching the expected signing identity.
        timeout: Verification timeout in seconds.

    Returns:
        Dict with keys: image_ref, verified (bool), error (str|None), timestamp.
    """
    result = {
        "image_ref": image_ref,
        "verified": False,
        "error": None,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    cosign_path = shutil.which("cosign")
    if not cosign_path:
        result["error"] = "cosign binary not found — skipping signature verification"
        logger.warning("image_verifier: %s", result["error"])
        return result

    cmd = [
        cosign_path,
        "verify",
        "--certificate-oidc-issuer", certificate_oidc_issuer,
        "--certificate-identity-regexp", certificate_identity_regexp,
        image_ref,
    ]

    try:
        proc = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=timeout)
        if proc.returncode == 0:
            result["verified"] = True
            logger.info("image_verifier: %s verified OK", image_ref)
        else:
            err_text = stderr.decode("utf-8", errors="replace").strip()
            result["error"] = f"cosign verify failed (rc={proc.returncode}): {err_text[:200]}"
            logger.warning("image_verifier: %s — %s", image_ref, result["error"])
    except asyncio.TimeoutError:
        result["error"] = f"cosign verify timed out after {timeout}s"
        logger.warning("image_verifier: %s — %s", image_ref, result["error"])
    except Exception as exc:
        result["error"] = str(exc)
        logger.warning("image_verifier: %s — unexpected error: %s", image_ref, exc)

    return result


async def verify_images(image_refs: list[str], **kwargs) -> dict[str, dict]:
    """Verify multiple image signatures concurrently.

    Returns:
        Dict mapping image_ref → verification result dict.
    """
    tasks = [verify_image(ref, **kwargs) for ref in image_refs]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    out: dict[str, dict] = {}
    for ref, res in zip(image_refs, results):
        if isinstance(res, Exception):
            out[ref] = {
                "image_ref": ref,
                "verified": False,
                "error": str(res),
                "timestamp": datetime.now(timezone.utc).isoformat(),
            }
        else:
            out[ref] = res
    return out
