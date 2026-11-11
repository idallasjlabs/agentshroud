# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Inbound MCP Edge — OAuth 2.1 authorisation server (threat T4, SCRUM-210)."""

import base64
import hashlib
import secrets
from urllib.parse import parse_qs, urlparse

import pytest

from gateway.inbound_edge import profiles as p
from gateway.inbound_edge.edge_jwt import TokenService, generate_signing_key_pem
from gateway.inbound_edge.oauth_service import EdgeOAuthService, OAuthFailure, derive_seal_key
from gateway.inbound_edge.store import EdgeStore

ISSUER = "https://edge.example.ts.net:8443"
RESOURCE = ISSUER + "/mcp"
CALLBACK = "https://claude.ai/api/mcp/auth_callback"


def _profile(**kw):
    base = dict(
        vendor="claude-duet",
        display_name="Claude Duet",
        enabled=True,
        mode="enforce",
        oauth=True,
        dynamic_registration=True,
        redirect_uris=(CALLBACK,),
        static_bearer=False,
        tools={"lab_search": "read"},
        per_client_per_minute=30,
        per_vendor_per_minute=60,
        max_concurrency=4,
        daily_calls=500,
        daily_delegations=20,
        dlp_mode="redact",
        dlp_min_confidence=0.9,
        max_response_bytes=1_048_576,
    )
    base.update(kw)
    return p.VendorProfile(**base)


@pytest.fixture
async def svc(tmp_path):
    key = generate_signing_key_pem()
    store = EdgeStore(tmp_path / "edge.db", seal_key=derive_seal_key(key))
    await store.init()
    notes = []

    async def notify(text):
        notes.append(text)

    service = EdgeOAuthService(
        store=store,
        tokens=TokenService(store, key, ISSUER, RESOURCE),
        profiles={"claude-duet": _profile(), "poke": _profile(vendor="poke", redirect_uris=())},
        issuer=ISSUER,
        resource=RESOURCE,
        notify=notify,
    )
    service.notes = notes
    yield service
    await store.close()


def _client_info(client_id="cid-1", redirect=CALLBACK, method="client_secret_post"):
    info = {
        "client_id": client_id,
        "client_name": "Claude",
        "redirect_uris": [redirect],
        "grant_types": ["authorization_code", "refresh_token"],
        "response_types": ["code"],
        "token_endpoint_auth_method": method,
    }
    if method != "none":
        info["client_secret"] = secrets.token_hex(32)
    return info


def _pkce():
    verifier = secrets.token_urlsafe(48)
    challenge = (
        base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).rstrip(b"=").decode()
    )
    return verifier, challenge


async def _linked(svc, resource=RESOURCE):
    code = await svc.store.open_enrollment("claude-duet", ttl_s=600)
    info = _client_info()
    await svc.register_client(info)
    _, challenge = _pkce()
    redirect = await svc.authorize(
        info["client_id"],
        {
            "state": "st-1",
            "scopes": ["mcp"],
            "code_challenge": challenge,
            "redirect_uri": CALLBACK,
            "redirect_uri_provided_explicitly": True,
            "resource": resource,
        },
    )
    req = parse_qs(urlparse(redirect).query)["req"][0]
    back = await svc.consent_submit(req, code)
    auth_code = parse_qs(urlparse(back).query)["code"][0]
    return info, auth_code, back


class TestRegistration:
    async def test_requires_open_enrollment_window(self, svc):
        with pytest.raises(OAuthFailure, match="enrollment"):
            await svc.register_client(_client_info())

    async def test_redirect_must_be_allowlisted(self, svc):
        await svc.store.open_enrollment("claude-duet", ttl_s=600)
        with pytest.raises(OAuthFailure) as exc:
            await svc.register_client(_client_info(redirect="https://evil.example/cb"))
        assert exc.value.error == "invalid_redirect_uri"

    async def test_vendor_without_redirects_cannot_register(self, svc):
        await svc.store.open_enrollment("poke", ttl_s=600)
        with pytest.raises(OAuthFailure):
            await svc.register_client(_client_info())

    async def test_disabled_vendor_cannot_register(self, svc):
        svc.profiles["claude-duet"] = _profile(enabled=False)
        await svc.store.open_enrollment("claude-duet", ttl_s=600)
        with pytest.raises(OAuthFailure, match="disabled"):
            await svc.register_client(_client_info())

    async def test_dcr_off_in_profile(self, svc):
        svc.profiles["claude-duet"] = _profile(dynamic_registration=False)
        await svc.store.open_enrollment("claude-duet", ttl_s=600)
        with pytest.raises(OAuthFailure, match="registration"):
            await svc.register_client(_client_info())

    async def test_client_secret_is_sealed_at_rest(self, svc, tmp_path):
        await svc.store.open_enrollment("claude-duet", ttl_s=600)
        info = _client_info()
        await svc.register_client(info)
        assert info["client_secret"].encode() not in (tmp_path / "edge.db").read_bytes()
        got = await svc.get_client(info["client_id"])
        assert got["client_secret"] == info["client_secret"]
        assert got["vendor"] == "claude-duet"


class TestAuthorizeAndConsent:
    async def test_full_flow_issues_working_tokens(self, svc):
        info, code, back = await _linked(svc)
        assert back.startswith(CALLBACK) and "state=st-1" in back
        loaded = await svc.load_authorization_code(info["client_id"], code)
        assert loaded["redirect_uri"] == CALLBACK
        tok = await svc.exchange_authorization_code(info["client_id"], code)
        principal = await svc.tokens.verify_access(tok["access_token"])
        assert principal.vendor == "claude-duet" and tok["expires_in"] == 900
        assert tok["refresh_token"]
        assert any("linked" in n.lower() for n in svc.notes)

    async def test_code_is_single_use(self, svc):
        info, code, _ = await _linked(svc)
        await svc.exchange_authorization_code(info["client_id"], code)
        with pytest.raises(OAuthFailure):
            await svc.exchange_authorization_code(info["client_id"], code)

    async def test_code_bound_to_client(self, svc):
        info, code, _ = await _linked(svc)
        assert await svc.load_authorization_code("other-client", code) is None

    async def test_wrong_enrollment_code_and_attempt_limit(self, svc):
        await svc.store.open_enrollment("claude-duet", ttl_s=600)
        info = _client_info()
        await svc.register_client(info)
        _, challenge = _pkce()
        redirect = await svc.authorize(
            info["client_id"],
            {
                "state": "s",
                "scopes": [],
                "code_challenge": challenge,
                "redirect_uri": CALLBACK,
                "redirect_uri_provided_explicitly": True,
                "resource": RESOURCE,
            },
        )
        req = parse_qs(urlparse(redirect).query)["req"][0]
        for _ in range(3):
            with pytest.raises(OAuthFailure, match="enrollment code"):
                await svc.consent_submit(req, "wrong-code")
        with pytest.raises(OAuthFailure, match="expired"):
            await svc.consent_submit(req, "wrong-code")

    async def test_consent_view_shows_vendor_not_client_supplied_text(self, svc):
        await svc.store.open_enrollment("claude-duet", ttl_s=600)
        info = _client_info()
        info["client_name"] = "Totally Legit <script>"
        await svc.register_client(info)
        _, challenge = _pkce()
        redirect = await svc.authorize(
            info["client_id"],
            {
                "state": None,
                "scopes": [],
                "code_challenge": challenge,
                "redirect_uri": CALLBACK,
                "redirect_uri_provided_explicitly": True,
                "resource": RESOURCE,
            },
        )
        req = parse_qs(urlparse(redirect).query)["req"][0]
        view = await svc.consent_view(req)
        assert view["vendor_display"] == "Claude Duet"
        assert view["redirect_host"] == "claude.ai"

    async def test_foreign_resource_rejected(self, svc):
        await svc.store.open_enrollment("claude-duet", ttl_s=600)
        info = _client_info()
        await svc.register_client(info)
        with pytest.raises(OAuthFailure) as exc:
            await svc.authorize(
                info["client_id"],
                {
                    "state": None,
                    "scopes": [],
                    "code_challenge": "x" * 43,
                    "redirect_uri": CALLBACK,
                    "redirect_uri_provided_explicitly": True,
                    "resource": "https://elsewhere.example/mcp",
                },
            )
        assert exc.value.error == "invalid_target"


class TestRefreshAndRevoke:
    async def test_refresh_rotates_and_reuse_kills_family(self, svc):
        info, code, _ = await _linked(svc)
        tok = await svc.exchange_authorization_code(info["client_id"], code)
        r1 = tok["refresh_token"]
        assert await svc.load_refresh_token(info["client_id"], r1) is not None
        tok2 = await svc.exchange_refresh_token(info["client_id"], r1, [])
        assert tok2["refresh_token"] != r1
        with pytest.raises(OAuthFailure):
            await svc.exchange_refresh_token(info["client_id"], r1, [])
        # family revoked: the rotated token is dead too
        with pytest.raises(OAuthFailure):
            await svc.exchange_refresh_token(info["client_id"], tok2["refresh_token"], [])

    async def test_revoke_access_token(self, svc):
        info, code, _ = await _linked(svc)
        tok = await svc.exchange_authorization_code(info["client_id"], code)
        await svc.revoke_token(tok["access_token"])
        assert await svc.load_access_token(tok["access_token"]) is None

    async def test_revoke_refresh_token(self, svc):
        info, code, _ = await _linked(svc)
        tok = await svc.exchange_authorization_code(info["client_id"], code)
        await svc.revoke_token(tok["refresh_token"])
        with pytest.raises(OAuthFailure):
            await svc.exchange_refresh_token(info["client_id"], tok["refresh_token"], [])

    async def test_killed_vendor_cannot_refresh(self, svc):
        info, code, _ = await _linked(svc)
        tok = await svc.exchange_authorization_code(info["client_id"], code)
        await svc.store.kill("vendor", "claude-duet", "owner")
        with pytest.raises(OAuthFailure, match="revoked"):
            await svc.exchange_refresh_token(info["client_id"], tok["refresh_token"], [])
