---
title: oauth_security.py
type: module
file_path: gateway/security/oauth_security.py
tags: [security, oauth, pkce, confused-deputy, mcp, authorization]
related: [[token_validation.py]], [[session_security.py]], [[consent_framework.py]]
status: documented
---

# oauth_security.py

## Purpose
Prevents confused deputy attacks on MCP (Model Context Protocol) OAuth proxy flows by enforcing per-client consent validation, PKCE (Proof Key for Code Exchange), state parameter integrity, strict redirect URI matching, and cryptographically signed consent cookies.

## Threat Model
Addresses the confused deputy attack class documented in Wang et al. 2026 (arXiv:2602.08412), where a malicious MCP server proxies OAuth authorization requests using a shared or static `client_id` to obtain tokens on behalf of another client. Additional mitigations target redirect URI hijacking, state replay attacks, and authorization code interception via non-PKCE flows.

## Responsibilities
- Validate OAuth authorization requests for empty or shared/static `client_id` values
- Enforce minimum entropy requirements on `state` parameters (8+ characters)
- Validate redirect URIs strictly against an allowlist; normalize paths to prevent traversal
- Block non-localhost HTTP redirect URIs
- Require and verify PKCE `code_challenge` / `code_challenge_method` on all requests
- Detect and reject state parameter replay attacks
- Create and validate HMAC-signed consent cookies binding client, scopes, and user identity

## Key Classes / Functions

| Name | Type | Description |
|------|------|-------------|
| `OAuthSecurityValidator` | Class | Core validator; enforces all OAuth security controls |
| `OAuthRequest` | Dataclass | Represents an inbound OAuth authorization request |
| `OAuthError` | Exception | Base exception for all OAuth validation failures |
| `ConfusedDeputyError` | Exception | Raised when a shared/static `client_id` is detected |
| `PKCEViolation` | Exception | Raised when PKCE requirements are not met |
| `RedirectMismatch` | Exception | Raised when the redirect URI fails allowlist validation |

## Function Details

### OAuthSecurityValidator.__init__(allowed_redirect_uris, require_pkce)
**Purpose:** Initializes the validator with an allowlist of permitted redirect URIs and PKCE enforcement flag. Generates a random 32-byte session secret for consent cookie signing.
**Parameters:** `allowed_redirect_uris` (list[str]), `require_pkce` (bool, default `True`)

### OAuthSecurityValidator.validate_request(req)
**Purpose:** Orchestrates full request validation: checks `client_id` is non-empty and not in the known shared-ID set, verifies state entropy, validates redirect URI, and enforces PKCE if required.
**Parameters:** `req` — `OAuthRequest`
**Returns:** `True` on success; raises `OAuthError` subclass on failure

### OAuthSecurityValidator.validate_redirect_uri(uri)
**Purpose:** Normalizes the URI path (to block `../` traversal), rejects non-localhost HTTP schemes, and verifies the URI (or its normalized form) exists in the configured allowlist.
**Parameters:** `uri` (str)
**Returns:** `True`; raises `RedirectMismatch` on failure

### OAuthSecurityValidator.register_known_shared_ids(ids)
**Purpose:** Adds known shared/static `client_id` values to the rejection set. Any request using one of these IDs will raise `ConfusedDeputyError`.
**Parameters:** `ids` (list[str])

### OAuthSecurityValidator.record_state_used(state) / check_state_reuse(state)
**Purpose:** Maintains an in-memory set of used state values. `check_state_reuse` raises `OAuthError` if the state has been seen before. The state map is bounded at 100,000 entries with LRU eviction.
**Parameters:** `state` (str)

### OAuthSecurityValidator.verify_pkce(verifier, challenge, method)
**Purpose:** Verifies the PKCE code verifier against the stored challenge using S256 (SHA-256 + base64url) or plain method. Uses `hmac.compare_digest` to prevent timing attacks.
**Parameters:** `verifier` (str), `challenge` (str), `method` (str)
**Returns:** `bool`

### OAuthSecurityValidator.create_consent_cookie(client_id, scopes, user_id)
**Purpose:** Serializes client identity, sorted scopes, user identity, and timestamp as JSON; HMAC-signs the payload with the session secret; returns `base64(payload).signature`.
**Parameters:** `client_id`, `scopes` (list[str]), `user_id` (str)
**Returns:** Signed cookie string

### OAuthSecurityValidator.validate_consent_cookie(cookie, client_id, scopes, user_id)
**Purpose:** Verifies the HMAC signature and confirms the cookie's client, scope set, and user identity match the expected values. Returns `False` on any validation failure without raising.
**Parameters:** `cookie` (str), `client_id`, `scopes`, `user_id`
**Returns:** `bool`

## Configuration / Environment Variables
- `allowed_redirect_uris` — passed at construction; no environment override currently
- `require_pkce` — defaults to `True`; should remain `True` in production
- `_COOKIE_SECRET` — 32 bytes of `secrets.token_bytes(32)`, generated per process; not persisted

## Related
- [[token_validation.py]]
- [[session_security.py]]
- [[consent_framework.py]]
