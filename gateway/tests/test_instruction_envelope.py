# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Tests for EnvelopeSigner (C46 — Signed Instruction Envelopes)."""

from __future__ import annotations

import pytest

from gateway.security.instruction_envelope import EnvelopeSigner, InstructionEnvelope


@pytest.fixture
def signer():
    # Use a fixed key for deterministic tests
    return EnvelopeSigner(key=b"test-key-32-bytes-long-padding-x")


class TestEnvelopeSigner:
    def test_sign_and_verify_roundtrip(self, signer):
        """sign() + verify() should return True for unmodified content."""
        env = signer.sign("Do X and report back", issuer="system")
        assert isinstance(env, InstructionEnvelope)
        assert env.algorithm == "hmac-sha256"
        assert signer.verify(env)

    def test_tampered_content_fails(self, signer):
        """Modifying content after signing should fail verification."""
        env = signer.sign("Original instruction", issuer="system")
        env.content = "INJECTED instruction"
        assert not signer.verify(env)

    def test_tampered_signature_fails(self, signer):
        """Modifying the signature directly should fail verification."""
        env = signer.sign("Some instruction", issuer="owner")
        env.signature = "0" * 64
        assert not signer.verify(env)

    def test_envelope_wraps_system_prompt(self, signer):
        """wrap_system_prompt() sets issuer='system' and passes verification."""
        prompt = "You are a secure assistant."
        env = signer.wrap_system_prompt(prompt)
        assert env.issuer == "system"
        assert env.content == prompt
        assert signer.verify(env)

    def test_envelope_wraps_tool_result(self, signer):
        """wrap_tool_result() sets issuer='tool:<name>' and passes verification."""
        result = '{"status": "ok", "data": "value"}'
        env = signer.wrap_tool_result(result, tool_name="read_file")
        assert env.issuer == "tool:read_file"
        assert env.content == result
        assert signer.verify(env)

    def test_different_signers_same_key_verify(self):
        """Two signers sharing the same key can cross-verify envelopes."""
        key = b"shared-secret-key-32-bytes-paddd"
        signer_a = EnvelopeSigner(key=key)
        signer_b = EnvelopeSigner(key=key)
        env = signer_a.sign("Important directive", issuer="system")
        assert signer_b.verify(env)

    def test_different_keys_fail_verification(self):
        """Envelopes signed with one key should not verify with a different key."""
        signer_a = EnvelopeSigner(key=b"key-a-32-bytes-long-for-testing!")
        signer_b = EnvelopeSigner(key=b"key-b-32-bytes-long-for-testing!")
        env = signer_a.sign("Directive", issuer="system")
        assert not signer_b.verify(env)
