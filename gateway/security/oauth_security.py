"""OAuth Security Module - Prevents confused deputy attacks on MCP OAuth proxy flows.

Implements per-client consent validation, PKCE enforcement, state parameter
validation, redirect URI strict matching, and consent cookie binding.

References:
    - Wang et al. 2026 (arXiv:2602.08412) - MCP OAuth confused deputy attacks
"""
import hashlib
import hmac
import json
import secrets
import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set
from urllib.parse import urlparse
import posixpath


class OAuthError(Exception):
    pass

class ConfusedDeputyError(OAuthError):
    pass

class PKCEViolation(OAuthError):
    pass

class RedirectMismatch(OAuthError):
    pass


@dataclass
class OAuthRequest:
    client_id: str
    redirect_uri: str
    state: str
    code_challenge: Optional[str] = None
    code_challenge_method: Optional[str] = None


class OAuthSecurityValidator:
    _COOKIE_SECRET = secrets.token_bytes(32)

    def __init__(self, allowed_redirect_uris: List[str], require_pkce: bool = True):
        self.allowed_redirect_uris = set(allowed_redirect_uris)
        self.require_pkce = require_pkce
        self.require_s256 = False
        self._known_shared_ids: Set[str] = set()
        self._used_states: Dict[str, float] = {}
        self._max_states = 100000

    def register_known_shared_ids(self, ids: List[str]):
        self._known_shared_ids.update(ids)

    def validate_request(self, req: OAuthRequest) -> bool:
        if not req.client_id:
            raise OAuthError("Empty client_id")
        if req.client_id in self._known_shared_ids:
            raise ConfusedDeputyError(f"Shared/static client_id rejected: {req.client_id}")
        if not req.state or len(req.state) < 8:
            raise OAuthError("State parameter missing or too short (min 8 chars)")
        self.validate_redirect_uri(req.redirect_uri)
        if self.require_pkce:
            if not req.code_challenge:
                raise PKCEViolation("PKCE code_challenge required")
            if self.require_s256 and req.code_challenge_method != "S256":
                raise PKCEViolation("S256 code_challenge_method required")
        return True

    def validate_redirect_uri(self, uri: str) -> bool:
        parsed = urlparse(uri)
        # Normalize path to catch traversal
        normalized = parsed._replace(path=posixpath.normpath(parsed.path) if parsed.path else parsed.path)
        normalized_uri = normalized.geturl()
        # Block non-localhost HTTP
        if parsed.scheme == "http" and parsed.hostname not in ("localhost", "127.0.0.1", "::1"):
            raise RedirectMismatch(f"Non-localhost HTTP redirect rejected: {uri}")
        if normalized_uri not in self.allowed_redirect_uris and uri not in self.allowed_redirect_uris:
            raise RedirectMismatch(f"Redirect URI not in allowed list: {uri}")
        return True

    def record_state_used(self, state: str):
        self._used_states[state] = time.time()
        # Evict oldest entries if over limit
        if len(self._used_states) > self._max_states:
            oldest = sorted(self._used_states, key=self._used_states.get)[:len(self._used_states) - self._max_states]
            for k in oldest:
                del self._used_states[k]

    def check_state_reuse(self, state: str):
        if state in self._used_states:
            raise OAuthError(f"State replay detected: {state}")

    def verify_pkce(self, verifier: str, challenge: str, method: str) -> bool:
        import base64
        if method == "S256":
            computed = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).rstrip(b"=").decode()
            return hmac.compare_digest(computed, challenge)
        elif method == "plain":
            return hmac.compare_digest(verifier, challenge)
        return False

    def create_consent_cookie(self, client_id: str, scopes: List[str], user_id: str) -> str:
        payload = json.dumps({"c": client_id, "s": sorted(scopes), "u": user_id, "t": time.time()})
        sig = hmac.new(self._COOKIE_SECRET, payload.encode(), hashlib.sha256).hexdigest()
        import base64
        encoded = base64.urlsafe_b64encode(payload.encode()).decode()
        return f"{encoded}.{sig}"

    def validate_consent_cookie(self, cookie: str, client_id: str, scopes: List[str], user_id: str) -> bool:
        try:
            import base64
            encoded, sig = cookie.rsplit(".", 1)
            payload = base64.urlsafe_b64decode(encoded.encode()).decode()
            expected_sig = hmac.new(self._COOKIE_SECRET, payload.encode(), hashlib.sha256).hexdigest()
            if not hmac.compare_digest(sig, expected_sig):
                return False
            data = json.loads(payload)
            return data["c"] == client_id and sorted(data["s"]) == sorted(scopes) and data["u"] == user_id
        except Exception:
            return False
