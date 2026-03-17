# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""SCL authentication and authorization helpers.

Supports three auth methods for the /soc/v1/ API:
  - Bearer token (CLI, direct API)
  - HTTP-only session cookie (web dashboard)
  - Telegram/Slack platform identity (chat bot — implicit)

RBAC is enforced via check_permission() on every SCL handler.
"""
from __future__ import annotations

import hashlib
import hmac
import logging
import os
import secrets
import time
from typing import Optional

from fastapi import Cookie, Depends, Header, HTTPException, Request, status

from ..security.rbac import Action, Resource, RBACManager
from ..security.rbac_config import RBACConfig, Role

logger = logging.getLogger("agentshroud.soc.auth")

# WS tokens: short-lived, single-use, 5-minute TTL
_WS_TOKEN_TTL = 300  # seconds
_ws_tokens: dict[str, tuple[str, float]] = {}  # token → (user_id, issued_at)


def _get_rbac_manager() -> RBACManager:
    return RBACManager(RBACConfig())


def _verify_bearer(token: str, config_token: str) -> bool:
    """Constant-time comparison against the gateway shared secret."""
    if not token or not config_token:
        return False
    return hmac.compare_digest(token.encode(), config_token.encode())


def _get_config_token() -> str:
    """Read the gateway auth token from env/secret."""
    token = os.environ.get("AGENTSHROUD_GATEWAY_PASSWORD", "")
    if not token:
        token = os.environ.get("OPENCLAW_GATEWAY_PASSWORD", "")
    if not token:
        secret_file = os.environ.get("GATEWAY_AUTH_TOKEN_FILE", "")
        if secret_file:
            try:
                with open(secret_file) as f:
                    token = f.read().strip()
            except OSError:
                pass
    return token


def issue_ws_token(user_id: str) -> str:
    """Issue a short-lived, single-use WebSocket token for a user."""
    token = secrets.token_hex(32)
    _ws_tokens[token] = (user_id, time.time())
    # Prune expired tokens
    now = time.time()
    expired = [t for t, (_, ts) in _ws_tokens.items() if now - ts > _WS_TOKEN_TTL]
    for t in expired:
        _ws_tokens.pop(t, None)
    return token


def redeem_ws_token(token: str) -> Optional[str]:
    """Consume a WS token and return the user_id, or None if invalid/expired."""
    entry = _ws_tokens.pop(token, None)
    if entry is None:
        return None
    user_id, issued_at = entry
    if time.time() - issued_at > _WS_TOKEN_TTL:
        return None
    return user_id


# ---------------------------------------------------------------------------
# FastAPI dependency: resolve caller identity + enforce RBAC
# ---------------------------------------------------------------------------

class SCLCaller:
    """Resolved identity of the SCL caller, including role and user_id."""

    def __init__(self, user_id: str, role: Role, rbac: RBACManager):
        self.user_id = user_id
        self.role = role
        self._rbac = rbac

    def require(self, action: Action, resource: Resource) -> None:
        """Raise 403 if the caller lacks the required permission."""
        result = self._rbac.check_permission(self.user_id, action, resource)
        if not result.allowed:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={"error": True, "code": "PERMISSION_DENIED", "message": result.reason or "Forbidden"},
            )

    def is_owner(self) -> bool:
        return self._rbac.config.is_owner(self.user_id)

    def is_group_admin(self, group_id: str) -> bool:
        """Check group admin status via TeamsConfig if available."""
        teams = getattr(self._rbac.config, "_teams_config", None)
        if teams is None:
            return False
        return teams.is_group_admin(self.user_id, group_id)


def _resolve_caller(
    authorization: Optional[str] = Header(default=None),
    x_soc_token: Optional[str] = Header(default=None),
    soc_session: Optional[str] = Cookie(default=None),
) -> SCLCaller:
    """FastAPI dependency: resolve Bearer/cookie token → user_id → role."""
    config_token = _get_config_token()
    token = None

    # Bearer: Authorization: Bearer <token>
    if authorization and authorization.startswith("Bearer "):
        token = authorization[7:].strip()
    elif x_soc_token:
        token = x_soc_token.strip()
    elif soc_session:
        token = soc_session.strip()

    if token and _verify_bearer(token, config_token):
        # Gateway shared-secret bearer = owner
        rbac = _get_rbac_manager()
        owner_id = rbac.config.owner_user_id
        return SCLCaller(user_id=owner_id, role=Role.OWNER, rbac=rbac)

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={"error": True, "code": "UNAUTHORIZED", "message": "Valid bearer token required"},
        headers={"WWW-Authenticate": "Bearer"},
    )


def get_caller(caller: SCLCaller = Depends(_resolve_caller)) -> SCLCaller:
    """Public FastAPI dependency injected by SCL route handlers."""
    return caller
