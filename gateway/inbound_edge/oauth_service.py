# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""OAuth 2.1 authorisation server for the Inbound MCP Edge (SCRUM-210).

The MCP SDK in the edge container serves the standard endpoints (RFC 8414 and
RFC 9728 metadata, ``/authorize``, ``/token``, ``/register``, ``/revoke``) and does
PKCE S256 and client authentication itself. Every decision those handlers delegate
to a provider lands here, in the gateway, behind ``/edge/v1/rpc``.

Owner consent is the security-critical step. A vendor's OAuth flow sends the
owner's browser to a public URL, so that page must not take a password. Instead the
owner first runs ``asb edge enroll --vendor <id>`` from the tailnet, which opens a
ten-minute enrollment window and prints a one-time code; the consent page accepts
only that code, three attempts per authorisation request. Dynamic client
registration (RFC 7591, deprecated in MCP 2026-07-28 but still what Claude, Poke and
Gemini use) is accepted only while a window is open, only for an enabled vendor
whose profile allows it, and only for redirect URIs on that vendor's allowlist.

IEC 62443 alignment: FR1 (SR 1.1, 1.2 identification and authentication of
software processes), FR2 (SR 2.1 authorisation enforcement).
"""

import logging
import secrets
import time
from typing import Any, Awaitable, Callable, Dict, List, Optional
from urllib.parse import urlencode, urlparse

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

from gateway.inbound_edge.edge_jwt import TokenRejected, TokenService
from gateway.inbound_edge.profiles import VendorProfile
from gateway.inbound_edge.store import EdgeStore

logger = logging.getLogger("agentshroud.inbound_edge.oauth")

AUTH_CODE_TTL_S = 300
PENDING_TTL_S = 600
REFRESH_TTL_S = 30 * 86400
MAX_CONSENT_ATTEMPTS = 3

Notify = Callable[[str], Awaitable[None]]


class OAuthFailure(Exception):
    """Maps onto an RFC 6749 / 7591 error code at the HTTP layer."""

    def __init__(self, error: str, description: str):
        super().__init__(description)
        self.error = error
        self.description = description


def derive_seal_key(signing_key_pem: bytes) -> bytes:
    """AES-256 key for sealing client secrets, derived from the gateway-only signing key."""
    return HKDF(
        algorithm=hashes.SHA256(), length=32, salt=None, info=b"agentshroud-edge-client-seal"
    ).derive(signing_key_pem)


class EdgeOAuthService:
    def __init__(
        self,
        store: EdgeStore,
        tokens: TokenService,
        profiles: Dict[str, VendorProfile],
        issuer: str,
        resource: str,
        notify: Optional[Notify] = None,
        clock: Callable[[], float] = time.time,
    ):
        self.store = store
        self.tokens = tokens
        self.profiles = profiles
        self.issuer = issuer.rstrip("/")
        self.resource = resource
        self._notify = notify
        self._clock = clock
        self._attempts: Dict[str, int] = {}

    # ── helpers ────────────────────────────────────────────────────────
    def _profile(self, vendor: str) -> VendorProfile:
        profile = self.profiles.get(vendor)
        if profile is None or not profile.enabled or not profile.oauth:
            raise OAuthFailure("unauthorized_client", f"vendor {vendor} is disabled")
        return profile

    async def _vendor_of(self, client_id: str) -> str:
        client = await self.store.get_client(client_id)
        if client is None:
            raise OAuthFailure("invalid_client", "unknown client")
        return client["vendor"]

    async def _say(self, text: str) -> None:
        if self._notify is not None:
            try:
                await self._notify(text)
            except Exception as exc:
                logger.error("edge oauth owner notification failed: %s", exc)

    async def _issue(
        self, client_id: str, vendor: str, scopes: List[str], family: Optional[str] = None
    ) -> Dict[str, Any]:
        killed = await self.store.killed_reason(vendor, client_id, "-")
        if killed:
            raise OAuthFailure("invalid_grant", killed)
        access, _, exp = await self.tokens.mint_access(client_id, vendor, scopes)
        refresh = secrets.token_urlsafe(32)
        await self.store.put_refresh(
            refresh,
            client_id,
            vendor,
            family or secrets.token_hex(16),
            self._clock() + REFRESH_TTL_S,
            {"scopes": scopes},
        )
        return {
            "access_token": access,
            "token_type": "Bearer",
            "expires_in": exp - int(self._clock()),
            "scope": " ".join(scopes) or None,
            "refresh_token": refresh,
        }

    # ── clients ────────────────────────────────────────────────────────
    async def get_client(self, client_id: str) -> Optional[Dict[str, Any]]:
        client = await self.store.get_client(client_id)
        if client is None:
            return None
        info = dict(client["info"])
        info["client_secret"] = client["secret"]
        info["vendor"] = client["vendor"]
        return info

    async def register_client(self, info: Dict[str, Any]) -> None:
        vendor = await self.store.enrollment_window_vendor()
        if vendor is None:
            raise OAuthFailure(
                "invalid_client_metadata",
                "registration is closed: open an enrollment window with `asb edge enroll`",
            )
        profile = self._profile(vendor)
        if not profile.dynamic_registration:
            raise OAuthFailure(
                "invalid_client_metadata", f"dynamic registration is off for {vendor}"
            )
        uris = [str(u) for u in (info.get("redirect_uris") or [])]
        if not uris or any(u not in profile.redirect_uris for u in uris):
            raise OAuthFailure(
                "invalid_redirect_uri", f"redirect URI not on the {vendor} allowlist"
            )
        secret = info.get("client_secret")
        stored = {k: v for k, v in info.items() if k != "client_secret"}
        await self.store.add_client(info["client_id"], vendor, stored, secret)
        logger.info("edge client registered for vendor %s", vendor)

    # ── authorize + consent ────────────────────────────────────────────
    async def authorize(self, client_id: str, params: Dict[str, Any]) -> str:
        vendor = await self._vendor_of(client_id)
        self._profile(vendor)
        resource = params.get("resource")
        if resource not in (None, self.resource):
            raise OAuthFailure("invalid_target", "token requested for a different resource")
        request_id = secrets.token_urlsafe(24)
        await self.store.put_pending(request_id, client_id, vendor, params, PENDING_TTL_S)
        return f"{self.issuer}/oauth/consent?{urlencode({'req': request_id})}"

    async def consent_view(self, request_id: str) -> Optional[Dict[str, Any]]:
        pending = await self.store.peek_pending(request_id)
        if pending is None:
            return None
        profile = self.profiles.get(pending["vendor"])
        return {
            "vendor": pending["vendor"],
            "vendor_display": profile.display_name if profile else pending["vendor"],
            "redirect_host": urlparse(pending["params"]["redirect_uri"]).hostname,
            "scopes": pending["params"].get("scopes") or [],
        }

    async def consent_submit(self, request_id: str, enrollment_code: str) -> str:
        pending = await self.store.peek_pending(request_id)
        attempts = self._attempts.get(request_id, 0)
        if pending is None or attempts >= MAX_CONSENT_ATTEMPTS:
            await self.store.take_pending(request_id)
            raise OAuthFailure("access_denied", "authorisation request expired")
        vendor = pending["vendor"]
        self._profile(vendor)
        if not await self.store.consume_enrollment(enrollment_code.strip(), vendor):
            self._attempts[request_id] = attempts + 1
            raise OAuthFailure("access_denied", "wrong or expired enrollment code")
        taken = await self.store.take_pending(request_id)
        if taken is None:
            raise OAuthFailure("access_denied", "authorisation request expired")
        self._attempts.pop(request_id, None)
        params = taken["params"]
        code = secrets.token_urlsafe(32)
        await self.store.put_code(
            code,
            taken["client_id"],
            vendor,
            {
                "scopes": params.get("scopes") or [],
                "code_challenge": params["code_challenge"],
                "redirect_uri": params["redirect_uri"],
                "redirect_uri_provided_explicitly": params["redirect_uri_provided_explicitly"],
                "resource": params.get("resource"),
                "expires_at": self._clock() + AUTH_CODE_TTL_S,
            },
            self._clock() + AUTH_CODE_TTL_S,
        )
        await self._say(
            f"AgentShroud: {self.profiles[vendor].display_name} linked to the Inbound Edge "
            f"(client {taken['client_id'][:8]}…). If this was not you: asb edge kill --vendor {vendor}"
        )
        query = {"code": code}
        if params.get("state"):
            query["state"] = params["state"]
        sep = "&" if "?" in params["redirect_uri"] else "?"
        return f"{params['redirect_uri']}{sep}{urlencode(query)}"

    # ── codes and tokens ───────────────────────────────────────────────
    async def load_authorization_code(self, client_id: str, code: str) -> Optional[Dict[str, Any]]:
        found = await self.store.peek_code(code)
        if found is None or found["client_id"] != client_id:
            return None
        return {"code": code, "client_id": client_id, **found["data"]}

    async def exchange_authorization_code(self, client_id: str, code: str) -> Dict[str, Any]:
        found = await self.store.take_code(code)
        if found is None or found["client_id"] != client_id:
            raise OAuthFailure("invalid_grant", "authorisation code invalid or used")
        return await self._issue(client_id, found["vendor"], list(found["data"]["scopes"]))

    async def load_refresh_token(self, client_id: str, token: str) -> Optional[Dict[str, Any]]:
        found = await self.store.peek_refresh(token)
        if found is None or found["client_id"] != client_id:
            return None
        return {"token": token, "client_id": client_id, "scopes": found["data"]["scopes"]}

    async def exchange_refresh_token(
        self, client_id: str, token: str, scopes: List[str]
    ) -> Dict[str, Any]:
        found = await self.store.rotate_refresh(token)
        if found is None or found["client_id"] != client_id:
            raise OAuthFailure("invalid_grant", "refresh token invalid, used or revoked")
        granted = list(found["data"]["scopes"])
        if scopes and not set(scopes) <= set(granted):
            raise OAuthFailure("invalid_scope", "scope widening is not allowed")
        killed = await self.store.killed_reason(found["vendor"], client_id, "-")
        if killed:
            raise OAuthFailure("invalid_grant", killed)
        return await self._issue(client_id, found["vendor"], scopes or granted, found["family"])

    async def load_access_token(self, token: str) -> Optional[Dict[str, Any]]:
        try:
            principal = await self.tokens.verify_access(token)
        except TokenRejected:
            return None
        return {
            "token": token,
            "client_id": principal.client_id,
            "scopes": list(principal.scopes),
            "expires_at": principal.expires_at,
            "resource": self.resource,
            "subject": f"{principal.vendor}:{principal.client_id}",
        }

    async def revoke_token(self, token: str) -> None:
        if token.count(".") == 2:
            try:
                principal = await self.tokens.verify_access(token)
            except TokenRejected:
                return
            await self.store.kill("jti", principal.jti, "revoked by client")
            return
        await self.store.revoke_refresh_family(token)
