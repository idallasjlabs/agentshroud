# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Inbound MCP Edge — stolen or forged tokens (threat T4, SCRUM-210)."""

import base64
import json
import time

import jwt
import pytest
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

from gateway.inbound_edge.edge_jwt import (
    TokenRejected,
    TokenService,
    generate_signing_key_pem,
    verify_signature_only,
)
from gateway.inbound_edge.store import EdgeStore

ISSUER = "https://edge.example.ts.net:8443"
RESOURCE = "https://edge.example.ts.net:8443/mcp"


class Clock:
    def __init__(self, now: float):
        self.now = now

    def __call__(self) -> float:
        return self.now


@pytest.fixture
async def store(tmp_path):
    s = EdgeStore(tmp_path / "edge.db")
    await s.init()
    yield s
    await s.close()


@pytest.fixture
def clock():
    return Clock(time.time())


@pytest.fixture
def svc(store, clock):
    return TokenService(store, generate_signing_key_pem(), ISSUER, RESOURCE, clock=clock)


async def _token(svc, vendor="claude-duet", client="c1"):
    token, jti, _ = await svc.mint_access(client_id=client, vendor=vendor, scopes=["mcp"])
    return token, jti


def _forge(svc, **overrides):
    """Sign arbitrary claims with the real key (as if minted outside the issuer)."""
    now = int(time.time())
    claims = {
        "iss": ISSUER,
        "aud": RESOURCE,
        "sub": "claude-duet:c1",
        "client_id": "c1",
        "vendor": "claude-duet",
        "jti": "forged-jti",
        "iat": now,
        "nbf": now,
        "exp": now + 600,
        "scope": "mcp",
    }
    claims.update(overrides)
    return jwt.encode(claims, svc._private_key, algorithm="ES256")


class TestValidToken:
    async def test_minted_token_verifies(self, svc):
        token, jti = await _token(svc)
        principal = await svc.verify_access(token)
        assert principal.vendor == "claude-duet"
        assert principal.client_id == "c1"
        assert principal.jti == jti
        assert principal.principal_id == "edge:claude-duet:c1"

    async def test_edge_can_check_signature_with_public_key_only(self, svc):
        token, _ = await _token(svc)
        claims = verify_signature_only(token, svc.public_key_pem, ISSUER, RESOURCE)
        assert claims["vendor"] == "claude-duet"

    async def test_lifetime_is_15_minutes(self, svc, clock):
        _, _, exp = await svc.mint_access(client_id="c1", vendor="claude-duet", scopes=["mcp"])
        assert exp - int(clock.now) == 900


class TestRejected:
    async def test_expired(self, svc, clock):
        clock.now -= 3600
        token, _ = await _token(svc)
        with pytest.raises(TokenRejected, match="expired"):
            await svc.verify_access(token)

    async def test_wrong_audience(self, store, clock):
        other = TokenService(store, generate_signing_key_pem(), ISSUER, RESOURCE + "x", clock=clock)
        token, _ = await _token(other)
        mine = TokenService(store, other._private_key_pem, ISSUER, RESOURCE, clock=clock)
        with pytest.raises(TokenRejected, match="audience"):
            await mine.verify_access(token)

    async def test_wrong_issuer(self, svc):
        with pytest.raises(TokenRejected, match="issuer"):
            await svc.verify_access(_forge(svc, iss="https://evil.example"))

    async def test_unsigned_alg_none(self, svc):
        token = jwt.encode(
            {"iss": ISSUER, "aud": RESOURCE, "jti": "x", "exp": int(time.time()) + 60},
            key=None,
            algorithm="none",
        )
        with pytest.raises(TokenRejected):
            await svc.verify_access(token)

    async def test_hs256_signed_with_public_key(self, svc):
        """Algorithm confusion: HMAC 'signed' with the published public key."""
        header = base64.urlsafe_b64encode(json.dumps({"alg": "HS256"}).encode()).rstrip(b"=")
        body = base64.urlsafe_b64encode(
            json.dumps({"iss": ISSUER, "aud": RESOURCE, "jti": "x"}).encode()
        ).rstrip(b"=")
        import hashlib
        import hmac

        sig = hmac.new(svc.public_key_pem, header + b"." + body, hashlib.sha256).digest()
        token = (header + b"." + body + b"." + base64.urlsafe_b64encode(sig).rstrip(b"=")).decode()
        with pytest.raises(TokenRejected):
            await svc.verify_access(token)
        with pytest.raises(TokenRejected):
            verify_signature_only(token, svc.public_key_pem, ISSUER, RESOURCE)

    async def test_signed_by_another_key(self, svc, store, clock):
        attacker = TokenService(store, generate_signing_key_pem(), ISSUER, RESOURCE, clock=clock)
        token, _ = await _token(attacker)
        with pytest.raises(TokenRejected, match="signature"):
            await svc.verify_access(token)

    async def test_tampered_payload(self, svc):
        token, _ = await _token(svc)
        head, body, sig = token.split(".")
        claims = json.loads(base64.urlsafe_b64decode(body + "=="))
        claims["vendor"] = "poke"
        body2 = base64.urlsafe_b64encode(json.dumps(claims).encode()).rstrip(b"=").decode()
        with pytest.raises(TokenRejected, match="signature"):
            await svc.verify_access(f"{head}.{body2}.{sig}")

    async def test_jti_never_issued_is_rejected(self, svc):
        """A correctly signed token the issuer has no record of (e.g. from another
        environment's key copy, or a restored backup) is not honoured."""
        with pytest.raises(TokenRejected, match="unknown jti"):
            await svc.verify_access(_forge(svc))

    async def test_missing_required_claims(self, svc):
        for claim in ("jti", "exp", "iat", "client_id", "vendor"):
            token = _forge(svc)
            claims = jwt.decode(token, options={"verify_signature": False})
            claims.pop(claim)
            bad = jwt.encode(claims, svc._private_key, algorithm="ES256")
            with pytest.raises(TokenRejected):
                await svc.verify_access(bad)

    async def test_issued_in_the_future(self, svc):
        future = int(time.time()) + 3600
        with pytest.raises(TokenRejected, match="iat"):
            await svc.verify_access(_forge(svc, iat=future, nbf=future - 3600))

    async def test_lifetime_longer_than_policy(self, svc):
        now = int(time.time())
        with pytest.raises(TokenRejected, match="lifetime"):
            await svc.verify_access(_forge(svc, iat=now, exp=now + 86400))

    async def test_sub_must_match_vendor_and_client(self, svc, store):
        await store.record_jti("forged-jti", "c1", "claude-duet", int(time.time()) + 600)
        with pytest.raises(TokenRejected, match="sub"):
            await svc.verify_access(_forge(svc, sub="poke:c1"))

    async def test_es256_with_wrong_curve_key_rejected(self, svc):
        p384 = ec.generate_private_key(ec.SECP384R1())
        pem = p384.private_bytes(
            serialization.Encoding.PEM,
            serialization.PrivateFormat.PKCS8,
            serialization.NoEncryption(),
        )
        with pytest.raises(ValueError, match="P-256"):
            TokenService(svc._store, pem, ISSUER, RESOURCE)


class TestRevocationAndKill:
    async def test_revoked_jti(self, svc, store):
        token, jti = await _token(svc)
        await store.kill("jti", jti, "test")
        with pytest.raises(TokenRejected, match="revoked"):
            await svc.verify_access(token)

    async def test_killed_client(self, svc, store):
        token, _ = await _token(svc, client="c9")
        await store.kill("client", "c9", "test")
        with pytest.raises(TokenRejected, match="revoked"):
            await svc.verify_access(token)

    async def test_killed_vendor_blocks_all_its_tokens(self, svc, store):
        t1, _ = await _token(svc, client="a")
        t2, _ = await _token(svc, client="b")
        other, _ = await _token(svc, vendor="poke", client="z")
        await store.kill("vendor", "claude-duet", "test")
        for t in (t1, t2):
            with pytest.raises(TokenRejected, match="revoked"):
                await svc.verify_access(t)
        assert (await svc.verify_access(other)).vendor == "poke"

    async def test_kill_takes_effect_within_one_second(self, svc, store):
        token, _ = await _token(svc)
        await svc.verify_access(token)
        start = time.monotonic()
        await store.kill("vendor", "claude-duet", "killswitch")
        with pytest.raises(TokenRejected):
            await svc.verify_access(token)
        assert time.monotonic() - start < 1.0

    async def test_unkill_restores(self, svc, store):
        token, _ = await _token(svc)
        await store.kill("vendor", "claude-duet", "test")
        await store.unkill("vendor", "claude-duet")
        assert (await svc.verify_access(token)).vendor == "claude-duet"

    async def test_bad_kill_scope_rejected(self, store):
        with pytest.raises(ValueError):
            await store.kill("everything", "x", "test")


class TestSingleUseGrants:
    async def test_auth_code_is_single_use(self, store):
        await store.put_code("code-1", "c1", "claude-duet", {"k": 1}, time.time() + 60)
        assert await store.take_code("code-1") == {
            "client_id": "c1",
            "vendor": "claude-duet",
            "data": {"k": 1},
        }
        assert await store.take_code("code-1") is None

    async def test_expired_auth_code(self, store):
        await store.put_code("code-2", "c1", "claude-duet", {}, time.time() - 1)
        assert await store.take_code("code-2") is None

    async def test_refresh_rotation_and_reuse_revokes_family(self, store):
        exp = time.time() + 3600
        await store.put_refresh("r1", "c1", "claude-duet", "fam", exp, {})
        assert (await store.rotate_refresh("r1"))["family"] == "fam"
        await store.put_refresh("r2", "c1", "claude-duet", "fam", exp, {})
        # Replaying the already-rotated r1 is theft: the whole family dies.
        assert await store.rotate_refresh("r1") is None
        assert await store.rotate_refresh("r2") is None

    async def test_secrets_are_stored_hashed(self, store, tmp_path):
        await store.put_code("plain-code-xyz", "c1", "v", {}, time.time() + 60)
        await store.put_refresh("plain-refresh-xyz", "c1", "v", "f", time.time() + 60, {})
        raw = (tmp_path / "edge.db").read_bytes()
        assert b"plain-code-xyz" not in raw
        assert b"plain-refresh-xyz" not in raw


class TestEnrollment:
    async def test_enrollment_code_single_use_and_vendor_bound(self, store):
        code = await store.open_enrollment("claude-duet", ttl_s=600)
        assert len(code) >= 8
        assert await store.consume_enrollment(code, "poke") is None
        assert await store.consume_enrollment(code, "claude-duet") is True
        assert await store.consume_enrollment(code, "claude-duet") is None

    async def test_enrollment_expires(self, store):
        code = await store.open_enrollment("claude-duet", ttl_s=-1)
        assert await store.consume_enrollment(code, "claude-duet") is None

    async def test_open_window_names_vendor(self, store):
        assert await store.enrollment_window_vendor() is None
        await store.open_enrollment("poke", ttl_s=600)
        assert await store.enrollment_window_vendor() == "poke"
