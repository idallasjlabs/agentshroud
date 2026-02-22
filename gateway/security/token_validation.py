# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Token Validation Module - Validates MCP token claims before passthrough.

Validates audience, issuer, scope, and expiry claims. Logs all validation
decisions to an audit ledger.

References:
    - Naik et al. 2026 (arXiv:2602.13477) - Token passthrough vulnerabilities
    - Maloyan & Namiot 2026 (arXiv:2601.17548) - MCP security analysis
"""
import base64
import json
import sqlite3
import time
from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any


class TokenError(Exception):
    pass

class AudienceMismatch(TokenError):
    pass

class IssuerMismatch(TokenError):
    pass

class ScopeViolation(TokenError):
    pass

class TokenExpiredError(TokenError):
    pass


@dataclass
class TokenValidationResult:
    valid: bool
    claims: Dict[str, Any] = field(default_factory=dict)


class TokenValidator:
    def __init__(self, expected_audience: str, expected_issuer: str, audit_log_path: str = ":memory:"):
        self.expected_audience = expected_audience
        self.expected_issuer = expected_issuer
        self._db = sqlite3.connect(audit_log_path)
        self._db.execute("""CREATE TABLE IF NOT EXISTS audit_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp REAL, decision TEXT, reason TEXT, claims TEXT
        )""")
        self._db.commit()

    def _decode_token(self, token: str) -> Dict[str, Any]:
        if not token:
            raise TokenError("Empty token")
        parts = token.split(".")
        if len(parts) != 3:
            raise TokenError("Invalid token format (expected 3 parts)")
        try:
            payload = parts[1]
            # Add padding
            payload += "=" * (4 - len(payload) % 4)
            decoded = base64.urlsafe_b64decode(payload)
            return json.loads(decoded)
        except Exception as e:
            raise TokenError(f"Failed to decode token: {e}")

    def _log(self, decision: str, reason: str, claims: Dict):
        self._db.execute("INSERT INTO audit_log (timestamp, decision, reason, claims) VALUES (?, ?, ?, ?)",
                         (time.time(), decision, reason, json.dumps(claims, default=str)))
        self._db.commit()

    def validate(self, token: str, required_scopes: Optional[List[str]] = None) -> TokenValidationResult:
        try:
            claims = self._decode_token(token)
        except TokenError:
            self._log("rejected", "malformed token", {})
            raise

        # Audience
        aud = claims.get("aud")
        if aud is None:
            self._log("rejected", "missing audience", claims)
            raise AudienceMismatch("Missing audience claim")
        if isinstance(aud, list):
            if self.expected_audience not in aud:
                self._log("rejected", "audience mismatch", claims)
                raise AudienceMismatch(f"Expected audience {self.expected_audience} not in {aud}")
        elif aud != self.expected_audience:
            self._log("rejected", "audience mismatch", claims)
            raise AudienceMismatch(f"Expected {self.expected_audience}, got {aud}")

        # Issuer
        iss = claims.get("iss")
        if iss is None:
            self._log("rejected", "missing issuer", claims)
            raise IssuerMismatch("Missing issuer claim")
        if iss != self.expected_issuer:
            self._log("rejected", "issuer mismatch", claims)
            raise IssuerMismatch(f"Expected {self.expected_issuer}, got {iss}")

        # Expiry
        exp = claims.get("exp")
        if exp is None:
            self._log("rejected", "missing expiry", claims)
            raise TokenError("Missing exp claim")
        if time.time() > exp:
            self._log("rejected", "token expired", claims)
            raise TokenExpiredError("Token has expired")

        # Scopes
        if required_scopes:
            scope_str = claims.get("scope")
            if scope_str is None:
                self._log("rejected", "missing scope", claims)
                raise ScopeViolation("Token has no scope claim but scopes required")
            granted = set(scope_str.split())
            required = set(required_scopes)
            if not required.issubset(granted):
                missing = required - granted
                self._log("rejected", f"scope violation: missing {missing}", claims)
                raise ScopeViolation(f"Missing scopes: {missing}")

        self._log("approved", "all checks passed", claims)
        return TokenValidationResult(valid=True, claims=claims)

    def get_audit_log(self) -> List[Dict]:
        cursor = self._db.execute("SELECT timestamp, decision, reason, claims FROM audit_log ORDER BY id")
        return [{"timestamp": r[0], "decision": r[1], "reason": r[2], "claims": json.loads(r[3])} for r in cursor]
