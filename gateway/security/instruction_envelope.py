# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Signed Instruction Envelopes — C46

Wraps instructions and tool results in HMAC-SHA256 signed envelopes so the
pipeline can verify they haven't been tampered with in transit.

Key sourcing (in priority order):
  1. ``AGENTSHROUD_ENVELOPE_SIGNING_KEY`` environment variable
  2. Session-scoped random 32-byte key (rotated on restart)
"""
from __future__ import annotations

import hashlib
import hmac
import logging
import os
import secrets
import time
import uuid
from dataclasses import dataclass

logger = logging.getLogger("agentshroud.security.instruction_envelope")


@dataclass
class InstructionEnvelope:
    """A signed instruction or tool result."""
    instruction_id: str   # UUID
    content: str
    issuer: str           # e.g. "system", "tool:read_file", "owner"
    timestamp: float
    signature: str        # hex HMAC-SHA256
    algorithm: str = "hmac-sha256"


class EnvelopeSigner:
    """Signs and verifies InstructionEnvelopes.

    Usage::

        signer = EnvelopeSigner()
        env = signer.sign("Do X", issuer="system")
        assert signer.verify(env)
    """

    def __init__(self, key: bytes | None = None) -> None:
        if key is not None:
            self._key = key
        else:
            env_key = os.environ.get("AGENTSHROUD_ENVELOPE_SIGNING_KEY", "")
            self._key = env_key.encode() if env_key else secrets.token_bytes(32)

    # ── Signing ──────────────────────────────────────────────────────────────

    def sign(self, content: str, issuer: str = "system") -> InstructionEnvelope:
        """Return a signed envelope for content."""
        instruction_id = str(uuid.uuid4())
        ts = time.time()
        sig = self._compute_signature(instruction_id, content, issuer, ts)
        return InstructionEnvelope(
            instruction_id=instruction_id,
            content=content,
            issuer=issuer,
            timestamp=ts,
            signature=sig,
            algorithm="hmac-sha256",
        )

    def verify(self, envelope: InstructionEnvelope) -> bool:
        """Return True if the envelope's signature is valid."""
        expected = self._compute_signature(
            envelope.instruction_id,
            envelope.content,
            envelope.issuer,
            envelope.timestamp,
        )
        return hmac.compare_digest(expected, envelope.signature)

    def wrap_system_prompt(self, prompt: str) -> InstructionEnvelope:
        """Convenience: sign a system prompt as issuer='system'."""
        return self.sign(prompt, issuer="system")

    def wrap_tool_result(self, result: str, tool_name: str) -> InstructionEnvelope:
        """Convenience: sign a tool result as issuer='tool:<tool_name>'."""
        return self.sign(result, issuer=f"tool:{tool_name}")

    # ── Internal ─────────────────────────────────────────────────────────────

    def _compute_signature(
        self, instruction_id: str, content: str, issuer: str, timestamp: float
    ) -> str:
        payload = f"{instruction_id}:{issuer}:{timestamp:.6f}:{content}"
        h = hmac.new(self._key, payload.encode("utf-8"), hashlib.sha256)
        return h.hexdigest()
