# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Access tokens for the Inbound MCP Edge (SCRUM-210, threat T4).

Tokens are ES256 JWTs, 15 minutes long, audience-bound to the edge's MCP resource
URL (RFC 8707), each with a unique ``jti``. The P-256 signing key exists only in
the gateway (Docker secret ``edge_signing_key``). The internet-facing edge holds the
public key and may pre-screen signatures with :func:`verify_signature_only`; the
authoritative decision is :meth:`TokenService.verify_access` in the gateway, which
additionally requires that the issuer recorded the ``jti`` and that no
vendor/client/jti kill applies — so a kill takes effect on the very next request.

``alg`` is pinned to ES256: ``none`` and HMAC algorithm-confusion tokens fail.

The existing ``gateway/security/token_validation.py`` is deliberately not reused: it
decodes payloads without verifying signatures (discovery finding F9).

IEC 62443 alignment: FR1 (Identification and Authentication Control).
"""

import logging
import secrets
import time
from dataclasses import dataclass
from typing import Any, Dict, List, Tuple

import jwt
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec

from gateway.inbound_edge.store import EdgeStore

logger = logging.getLogger("agentshroud.inbound_edge.tokens")

ALGORITHM = "ES256"
ACCESS_TTL_S = 900
CLOCK_SKEW_S = 30
_REQUIRED = ["iss", "aud", "sub", "exp", "iat", "nbf", "jti", "client_id", "vendor"]


class TokenRejected(Exception):
    """The presented token must not be honoured. ``str(exc)`` is safe to audit."""


@dataclass(frozen=True)
class EdgePrincipal:
    vendor: str
    client_id: str
    jti: str
    scopes: Tuple[str, ...]
    expires_at: int

    @property
    def principal_id(self) -> str:
        """Namespaced identity used by every downstream module. Never an owner ID."""
        return f"edge:{self.vendor}:{self.client_id}"


def generate_signing_key_pem() -> bytes:
    key = ec.generate_private_key(ec.SECP256R1())
    return key.private_bytes(
        serialization.Encoding.PEM,
        serialization.PrivateFormat.PKCS8,
        serialization.NoEncryption(),
    )


def _decode(token: str, key: Any, issuer: str, audience: str) -> Dict[str, Any]:
    try:
        header = jwt.get_unverified_header(token)
    except jwt.InvalidTokenError as exc:
        raise TokenRejected(f"malformed token: {exc}") from exc
    if header.get("alg") != ALGORITHM:
        raise TokenRejected(f"algorithm {header.get('alg')!r} not accepted")
    try:
        return jwt.decode(
            token,
            key,
            algorithms=[ALGORITHM],
            audience=audience,
            issuer=issuer,
            leeway=CLOCK_SKEW_S,
            options={"require": _REQUIRED},
        )
    except jwt.ExpiredSignatureError as exc:
        raise TokenRejected("token expired") from exc
    except jwt.InvalidAudienceError as exc:
        raise TokenRejected("wrong audience") from exc
    except jwt.InvalidIssuerError as exc:
        raise TokenRejected("wrong issuer") from exc
    except jwt.InvalidSignatureError as exc:
        raise TokenRejected("bad signature") from exc
    except jwt.MissingRequiredClaimError as exc:
        raise TokenRejected(f"missing claim: {exc.claim}") from exc
    except jwt.InvalidTokenError as exc:
        raise TokenRejected(f"invalid token: {exc}") from exc


def verify_signature_only(
    token: str, public_key_pem: bytes, issuer: str, audience: str
) -> Dict[str, Any]:
    """Edge-side pre-screen: signature, alg, iss, aud, exp. No revocation check."""
    key = serialization.load_pem_public_key(public_key_pem)
    return _decode(token, key, issuer, audience)


class TokenService:
    """Mint and authoritatively verify edge access tokens (gateway only)."""

    def __init__(
        self,
        store: EdgeStore,
        private_key_pem: bytes,
        issuer: str,
        resource: str,
        clock=time.time,
        ttl_s: int = ACCESS_TTL_S,
    ):
        key = serialization.load_pem_private_key(private_key_pem, password=None)
        if not isinstance(key, ec.EllipticCurvePrivateKey) or key.curve.name != "secp256r1":
            raise ValueError("edge signing key must be an EC P-256 private key")
        self._store = store
        self._private_key = key
        self._private_key_pem = private_key_pem
        self.public_key_pem = key.public_key().public_bytes(
            serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo
        )
        self.issuer = issuer
        self.resource = resource
        self._clock = clock
        self.ttl_s = ttl_s

    async def mint_access(
        self, client_id: str, vendor: str, scopes: List[str]
    ) -> Tuple[str, str, int]:
        now = int(self._clock())
        jti = secrets.token_urlsafe(24)
        exp = now + self.ttl_s
        claims = {
            "iss": self.issuer,
            "aud": self.resource,
            "sub": f"{vendor}:{client_id}",
            "client_id": client_id,
            "vendor": vendor,
            "jti": jti,
            "iat": now,
            "nbf": now,
            "exp": exp,
            "scope": " ".join(scopes),
        }
        await self._store.record_jti(jti, client_id, vendor, exp)
        return jwt.encode(claims, self._private_key, algorithm=ALGORITHM), jti, exp

    async def verify_access(self, token: str) -> EdgePrincipal:
        claims = _decode(token, self._private_key.public_key(), self.issuer, self.resource)
        now = self._clock()
        iat, exp = int(claims["iat"]), int(claims["exp"])
        if iat > now + CLOCK_SKEW_S:
            raise TokenRejected("iat in the future")
        if exp - iat > self.ttl_s:
            raise TokenRejected("token lifetime exceeds policy")
        vendor, client_id, jti = str(claims["vendor"]), str(claims["client_id"]), str(claims["jti"])
        if claims["sub"] != f"{vendor}:{client_id}":
            raise TokenRejected("sub does not match vendor/client")
        if not await self._store.jti_issued(jti, client_id, vendor):
            raise TokenRejected("unknown jti")
        killed = await self._store.killed_reason(vendor, client_id, jti)
        if killed:
            raise TokenRejected(killed)
        return EdgePrincipal(
            vendor=vendor,
            client_id=client_id,
            jti=jti,
            scopes=tuple(str(claims.get("scope", "")).split()),
            expires_at=exp,
        )
