# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""MFAGuard — second factor for high-risk owner operations.

SCRUM-93 · IEC 62443 FR1 (Identification & Authentication Control, SL2).

A compromised owner channel (Telegram/iOS/browser) can, by itself, authorize a
destructive action once the owner identity is trusted. FR1 requires a *second*
independent authenticator for such operations. This module verifies a
time-based one-time password (RFC 6238 TOTP) as that second factor before an
owner-approved high-risk action is committed.

Design constraints (No Security Theater):
  * Config-gated, DEFAULT OFF — existing deployments are unchanged until an
    operator sets ``AGENTSHROUD_MFA_ENABLED`` and provisions a secret.
  * FAIL-CLOSED — when enabled, a high-risk action with a missing / invalid /
    expired / replayed factor is DENIED.
  * CONSTANT-TIME — code comparison uses ``hmac.compare_digest`` to avoid
    timing side channels (CWE-208).
  * REPLAY-RESISTANT — each accepted (counter, code) pair is recorded; the same
    code cannot be reused within its validity window.
  * NO NEW DEPENDENCY — implemented on the Python standard library
    (``hmac`` / ``hashlib`` / ``base64`` / ``struct``); ``pyotp`` is not required.
  * NO HARDCODED SECRET — the shared secret is read from an env var or a
    Docker-secret file, never committed.

Wiring: ``gateway/approval_queue/queue.py::ApprovalQueue.decide`` calls
``MFAGuard.verify`` at the owner-authorization chokepoint. See tests in
``gateway/tests/test_mfa_guard.py`` and the approval-decide integration tests.
"""

from __future__ import annotations

import base64
import binascii
import hashlib
import hmac
import logging
import os
import struct
import time
from dataclasses import dataclass
from typing import Optional, Set

logger = logging.getLogger("agentshroud.security.mfa_guard")


# ---------------------------------------------------------------------------
# High-risk action types that require a second factor when MFA is enabled.
# Mirrors the approval-queue categories (CLAUDE.md §7 hard constraint #7) plus
# destructive admin operations.
# ---------------------------------------------------------------------------
DEFAULT_HIGH_RISK_ACTIONS: frozenset[str] = frozenset(
    {
        "email_sending",
        "imessage_sending",
        "file_deletion",
        "external_api_calls",
        "skill_installation",
        # Destructive admin operations
        "config_override",
        "key_rotation",
        "killswitch",
        "agent_delete",
    }
)


@dataclass(frozen=True)
class MFAResult:
    """Outcome of an MFA verification.

    Attributes:
        allowed: True if the action may proceed (either MFA not required, or a
            valid second factor was presented).
        required: True if the action type is high-risk and MFA is enabled.
        reason: Human-readable explanation (safe to log; never contains the code).
    """

    allowed: bool
    required: bool
    reason: str


class MFAGuard:
    """Verify a TOTP second factor for high-risk operations (fail-closed).

    Args:
        secret_b32: Base32-encoded shared TOTP secret (RFC 4648). Empty string
            means "no secret configured" — when ``enabled`` is True this makes
            every high-risk verification fail closed.
        enabled: Master switch. When False, ``verify`` always allows (behavior
            unchanged for existing deployments).
        step: TOTP time step in seconds (RFC 6238 default 30).
        digits: Number of code digits (default 6).
        window: Number of adjacent time steps to accept on each side for clock
            skew (default 1 → accepts previous / current / next step).
        high_risk_actions: Optional override of the action-type set that
            requires a second factor. Defaults to ``DEFAULT_HIGH_RISK_ACTIONS``.
    """

    def __init__(
        self,
        secret_b32: str,
        enabled: bool = False,
        step: int = 30,
        digits: int = 6,
        window: int = 1,
        high_risk_actions: Optional[Set[str]] = None,
    ) -> None:
        self.enabled = bool(enabled)
        self._step = max(1, int(step))
        self._digits = max(6, int(digits))
        self._window = max(0, int(window))
        self._high_risk = frozenset(
            a.lower().strip()
            for a in (
                high_risk_actions if high_risk_actions is not None else DEFAULT_HIGH_RISK_ACTIONS
            )
        )
        self._key = self._decode_secret(secret_b32)
        # Replay tracking: set of (counter, code) pairs already accepted.
        self._used: Set[tuple[int, str]] = set()

    # ------------------------------------------------------------------
    # Construction from environment / secret file
    # ------------------------------------------------------------------

    @classmethod
    def from_env(cls) -> "MFAGuard":
        """Build an MFAGuard from environment variables / Docker secret file.

        Recognized configuration (all optional; default = disabled):
          * ``AGENTSHROUD_MFA_ENABLED`` — "true"/"1"/"yes"/"on" to enable.
          * ``AGENTSHROUD_MFA_SECRET`` — base32 TOTP secret (inline).
          * ``AGENTSHROUD_MFA_SECRET_FILE`` — path to a file containing the
            base32 secret (preferred; Docker-secret friendly). Takes precedence
            over the inline value when readable.
          * ``AGENTSHROUD_MFA_WINDOW`` — clock-skew window (int, default 1).
        """
        enabled = _truthy(os.environ.get("AGENTSHROUD_MFA_ENABLED", ""))

        secret = os.environ.get("AGENTSHROUD_MFA_SECRET", "").strip()
        secret_file = os.environ.get("AGENTSHROUD_MFA_SECRET_FILE", "").strip()
        if secret_file:
            try:
                with open(secret_file, encoding="utf-8") as fh:
                    file_secret = fh.read().strip()
                if file_secret:
                    secret = file_secret
                    logger.info("MFAGuard: loaded TOTP secret from secret file")
            except OSError as exc:
                logger.warning("MFAGuard: could not read AGENTSHROUD_MFA_SECRET_FILE: %s", exc)

        try:
            window = int(os.environ.get("AGENTSHROUD_MFA_WINDOW", "1"))
        except ValueError:
            window = 1

        if enabled and not secret:
            logger.warning(
                "MFAGuard: AGENTSHROUD_MFA_ENABLED is set but no secret is configured — "
                "high-risk operations will FAIL CLOSED until AGENTSHROUD_MFA_SECRET(_FILE) is set."
            )

        return cls(secret_b32=secret, enabled=enabled, window=window)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def is_required(self, action_type: str) -> bool:
        """Return True if ``action_type`` requires a second factor right now."""
        return self.enabled and (action_type or "").lower().strip() in self._high_risk

    def verify(
        self,
        action_type: str,
        code: Optional[str],
        now: Optional[int] = None,
    ) -> MFAResult:
        """Verify the second factor for a high-risk action.

        Args:
            action_type: The action being authorized (e.g. ``email_sending``).
            code: The TOTP code presented by the owner, or None if absent.
            now: Unix timestamp to evaluate against (defaults to real time).
                Injectable for deterministic tests — never sleeps.

        Returns:
            MFAResult. ``allowed`` is False (fail-closed) whenever MFA is
            required and the presented factor is missing, malformed, out of
            window, replayed, or the guard has no secret configured.
        """
        if not self.is_required(action_type):
            return MFAResult(allowed=True, required=False, reason="mfa not required for action")

        if not self._key:
            logger.error("MFAGuard: enabled but no secret configured — denying high-risk action")
            return MFAResult(
                allowed=False,
                required=True,
                reason="mfa required but secret not configured (fail-closed)",
            )

        if code is None or not str(code).strip():
            return MFAResult(allowed=False, required=True, reason="mfa code missing")

        candidate = str(code).strip()
        if not candidate.isdigit() or len(candidate) != self._digits:
            return MFAResult(allowed=False, required=True, reason="mfa code invalid format")

        at = int(time.time()) if now is None else int(now)
        counter = at // self._step

        for drift in range(-self._window, self._window + 1):
            expected_counter = counter + drift
            if expected_counter < 0:
                continue
            expected = self._totp_for_counter(expected_counter)
            # Constant-time comparison (CWE-208).
            if hmac.compare_digest(expected, candidate):
                key = (expected_counter, candidate)
                if key in self._used:
                    logger.warning("MFAGuard: replayed code rejected for action=%s", action_type)
                    return MFAResult(
                        allowed=False, required=True, reason="mfa code replay rejected"
                    )
                self._used.add(key)
                self._prune_used(counter)
                return MFAResult(allowed=True, required=True, reason="mfa verified")

        logger.warning("MFAGuard: invalid code for action=%s", action_type)
        return MFAResult(allowed=False, required=True, reason="mfa code invalid")

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------

    @staticmethod
    def _decode_secret(secret_b32: str) -> bytes:
        """Decode a base32 secret; return b"" on empty/invalid input."""
        s = (secret_b32 or "").strip().replace(" ", "").upper()
        if not s:
            return b""
        # Pad to a multiple of 8 for base32.
        s += "=" * ((8 - len(s) % 8) % 8)
        try:
            return base64.b32decode(s, casefold=True)
        except (binascii.Error, ValueError):
            logger.error("MFAGuard: TOTP secret is not valid base32 — treating as unconfigured")
            return b""

    def _totp_for_counter(self, counter: int) -> str:
        """Compute the RFC 6238 TOTP value for a specific time-step counter."""
        msg = struct.pack(">Q", counter)
        digest = hmac.new(self._key, msg, hashlib.sha1).digest()
        offset = digest[-1] & 0x0F
        binary = struct.unpack(">I", digest[offset : offset + 4])[0] & 0x7FFFFFFF
        return str(binary % (10**self._digits)).zfill(self._digits)

    def _prune_used(self, current_counter: int) -> None:
        """Drop replay records older than the accepted window (bounded memory)."""
        floor = current_counter - self._window - 1
        stale = [pair for pair in self._used if pair[0] < floor]
        for pair in stale:
            self._used.discard(pair)


def _truthy(value: str) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes", "on"}
