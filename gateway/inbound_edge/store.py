# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Gateway-side state for the Inbound MCP Edge (SCRUM-210).

Holds OAuth clients, one-time enrollment codes, pending authorisations,
authorisation codes, refresh-token families, every issued access-token ``jti``,
and the revocation/kill list. It lives in the gateway's data directory — never in
the internet-facing edge container, which holds no state.

Every bearer secret (enrollment code, authorisation code, refresh token, client
secret) is stored only as a SHA-256 hash, so a copy of this database cannot be
replayed. Grants are single use: authorisation codes are deleted when taken, and
re-presenting a rotated refresh token revokes its whole family (RFC 9700 §4.14).

IEC 62443 alignment: FR1 (Identification and Authentication Control), FR2 (Use
Control) — revocation and kill take effect on the next request.
"""

import hashlib
import json
import logging
import secrets
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

import aiosqlite

logger = logging.getLogger("agentshroud.inbound_edge.store")

KILL_SCOPES = ("vendor", "client", "jti")

_SCHEMA = """
CREATE TABLE IF NOT EXISTS clients (
    client_id TEXT PRIMARY KEY,
    vendor TEXT NOT NULL,
    secret_hash TEXT,
    info TEXT NOT NULL,
    created_at REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS enrollments (
    code_hash TEXT PRIMARY KEY,
    vendor TEXT NOT NULL,
    expires_at REAL NOT NULL,
    used_at REAL
);
CREATE TABLE IF NOT EXISTS pending_authorizations (
    request_hash TEXT PRIMARY KEY,
    client_id TEXT NOT NULL,
    vendor TEXT NOT NULL,
    params TEXT NOT NULL,
    expires_at REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS auth_codes (
    code_hash TEXT PRIMARY KEY,
    client_id TEXT NOT NULL,
    vendor TEXT NOT NULL,
    data TEXT NOT NULL,
    expires_at REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS refresh_tokens (
    token_hash TEXT PRIMARY KEY,
    client_id TEXT NOT NULL,
    vendor TEXT NOT NULL,
    family TEXT NOT NULL,
    data TEXT NOT NULL,
    expires_at REAL NOT NULL,
    used INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS revoked_families (family TEXT PRIMARY KEY, revoked_at REAL NOT NULL);
CREATE TABLE IF NOT EXISTS issued_jtis (
    jti TEXT PRIMARY KEY,
    client_id TEXT NOT NULL,
    vendor TEXT NOT NULL,
    expires_at REAL NOT NULL
);
CREATE TABLE IF NOT EXISTS kills (
    scope TEXT NOT NULL,
    value TEXT NOT NULL,
    reason TEXT NOT NULL,
    created_at REAL NOT NULL,
    PRIMARY KEY (scope, value)
);
"""


def _h(secret: str) -> str:
    return hashlib.sha256(secret.encode()).hexdigest()


class EdgeStore:
    """Async SQLite store. One instance per gateway process."""

    def __init__(self, db_path: Path | str, clock=time.time):
        self._path = str(db_path)
        self._clock = clock
        self._db: Optional[aiosqlite.Connection] = None

    async def init(self) -> None:
        self._db = await aiosqlite.connect(self._path, isolation_level=None)
        await self._db.execute("PRAGMA journal_mode=WAL")
        await self._db.executescript(_SCHEMA)

    async def close(self) -> None:
        if self._db is not None:
            await self._db.close()
            self._db = None

    @property
    def db(self) -> aiosqlite.Connection:
        if self._db is None:
            raise RuntimeError("EdgeStore not initialised")
        return self._db

    async def _one(self, sql: str, args: tuple) -> Optional[tuple]:
        async with self.db.execute(sql, args) as cur:
            return await cur.fetchone()

    # ── clients ──────────────────────────────────────────────────────────
    async def add_client(
        self, client_id: str, vendor: str, info: Dict[str, Any], secret: Optional[str]
    ) -> None:
        await self.db.execute(
            "INSERT INTO clients(client_id, vendor, secret_hash, info, created_at) "
            "VALUES (?,?,?,?,?)",
            (client_id, vendor, _h(secret) if secret else None, json.dumps(info), self._clock()),
        )

    async def get_client(self, client_id: str) -> Optional[Dict[str, Any]]:
        row = await self._one("SELECT vendor, info FROM clients WHERE client_id=?", (client_id,))
        if row is None:
            return None
        return {"client_id": client_id, "vendor": row[0], "info": json.loads(row[1])}

    async def list_clients(self) -> List[Dict[str, Any]]:
        async with self.db.execute(
            "SELECT client_id, vendor, created_at FROM clients ORDER BY created_at"
        ) as cur:
            return [{"client_id": r[0], "vendor": r[1], "created_at": r[2]} async for r in cur]

    # ── enrollment ───────────────────────────────────────────────────────
    async def open_enrollment(self, vendor: str, ttl_s: int = 600) -> str:
        """Mint a one-time code the owner types on the consent page. Returned once."""
        code = secrets.token_urlsafe(9)
        await self.db.execute(
            "INSERT INTO enrollments(code_hash, vendor, expires_at) VALUES (?,?,?)",
            (_h(code), vendor, self._clock() + ttl_s),
        )
        return code

    async def consume_enrollment(self, code: str, vendor: str) -> Optional[bool]:
        """True exactly once for an unexpired code bound to ``vendor``; else None."""
        cur = await self.db.execute(
            "UPDATE enrollments SET used_at=? WHERE code_hash=? AND vendor=? "
            "AND used_at IS NULL AND expires_at>?",
            (self._clock(), _h(code), vendor, self._clock()),
        )
        return True if cur.rowcount == 1 else None

    async def enrollment_window_vendor(self) -> Optional[str]:
        """The vendor with an open (unused, unexpired) enrollment, if exactly one."""
        async with self.db.execute(
            "SELECT DISTINCT vendor FROM enrollments WHERE used_at IS NULL AND expires_at>?",
            (self._clock(),),
        ) as cur:
            vendors = [r[0] async for r in cur]
        return vendors[0] if len(vendors) == 1 else None

    # ── pending authorisations (between /authorize and owner consent) ────
    async def put_pending(
        self, request_id: str, client_id: str, vendor: str, params: Dict[str, Any], ttl_s: int
    ) -> None:
        await self.db.execute(
            "INSERT INTO pending_authorizations VALUES (?,?,?,?,?)",
            (_h(request_id), client_id, vendor, json.dumps(params), self._clock() + ttl_s),
        )

    async def peek_pending(self, request_id: str) -> Optional[Dict[str, Any]]:
        row = await self._one(
            "SELECT client_id, vendor, params FROM pending_authorizations "
            "WHERE request_hash=? AND expires_at>?",
            (_h(request_id), self._clock()),
        )
        if row is None:
            return None
        return {"client_id": row[0], "vendor": row[1], "params": json.loads(row[2])}

    async def take_pending(self, request_id: str) -> Optional[Dict[str, Any]]:
        found = await self.peek_pending(request_id)
        cur = await self.db.execute(
            "DELETE FROM pending_authorizations WHERE request_hash=?", (_h(request_id),)
        )
        return found if cur.rowcount == 1 else None

    # ── authorisation codes ──────────────────────────────────────────────
    async def put_code(
        self, code: str, client_id: str, vendor: str, data: Dict[str, Any], expires_at: float
    ) -> None:
        await self.db.execute(
            "INSERT INTO auth_codes VALUES (?,?,?,?,?)",
            (_h(code), client_id, vendor, json.dumps(data), expires_at),
        )

    async def peek_code(self, code: str) -> Optional[Dict[str, Any]]:
        row = await self._one(
            "SELECT client_id, vendor, data FROM auth_codes WHERE code_hash=? AND expires_at>?",
            (_h(code), self._clock()),
        )
        if row is None:
            return None
        return {"client_id": row[0], "vendor": row[1], "data": json.loads(row[2])}

    async def take_code(self, code: str) -> Optional[Dict[str, Any]]:
        """Return and delete an unexpired code. A second call returns None."""
        found = await self.peek_code(code)
        cur = await self.db.execute("DELETE FROM auth_codes WHERE code_hash=?", (_h(code),))
        return found if cur.rowcount == 1 else None

    # ── refresh tokens ───────────────────────────────────────────────────
    async def put_refresh(
        self,
        token: str,
        client_id: str,
        vendor: str,
        family: str,
        expires_at: float,
        data: Dict[str, Any],
    ) -> None:
        await self.db.execute(
            "INSERT INTO refresh_tokens(token_hash, client_id, vendor, family, data, expires_at) "
            "VALUES (?,?,?,?,?,?)",
            (_h(token), client_id, vendor, family, json.dumps(data), expires_at),
        )

    async def peek_refresh(self, token: str) -> Optional[Dict[str, Any]]:
        row = await self._one(
            "SELECT r.client_id, r.vendor, r.family, r.data, r.used FROM refresh_tokens r "
            "WHERE r.token_hash=? AND r.expires_at>? AND r.family NOT IN "
            "(SELECT family FROM revoked_families)",
            (_h(token), self._clock()),
        )
        if row is None or row[4]:
            return None
        return {"client_id": row[0], "vendor": row[1], "family": row[2], "data": json.loads(row[3])}

    async def rotate_refresh(self, token: str) -> Optional[Dict[str, Any]]:
        """Consume a refresh token. Reuse of a consumed token revokes its family."""
        row = await self._one(
            "SELECT family, used FROM refresh_tokens WHERE token_hash=?", (_h(token),)
        )
        if row is None:
            return None
        family, used = row
        if used:
            await self.db.execute(
                "INSERT OR IGNORE INTO revoked_families VALUES (?,?)", (family, self._clock())
            )
            logger.warning("refresh token reuse detected — family revoked")
            return None
        found = await self.peek_refresh(token)
        if found is None:
            return None
        cur = await self.db.execute(
            "UPDATE refresh_tokens SET used=1 WHERE token_hash=? AND used=0", (_h(token),)
        )
        return found if cur.rowcount == 1 else None

    # ── issued access tokens ─────────────────────────────────────────────
    async def record_jti(self, jti: str, client_id: str, vendor: str, expires_at: float) -> None:
        await self.db.execute(
            "INSERT INTO issued_jtis VALUES (?,?,?,?)", (jti, client_id, vendor, expires_at)
        )

    async def jti_issued(self, jti: str, client_id: str, vendor: str) -> bool:
        row = await self._one(
            "SELECT 1 FROM issued_jtis WHERE jti=? AND client_id=? AND vendor=?",
            (jti, client_id, vendor),
        )
        return row is not None

    # ── kill / revocation ────────────────────────────────────────────────
    async def kill(self, scope: str, value: str, reason: str) -> None:
        if scope not in KILL_SCOPES:
            raise ValueError(f"kill scope must be one of {KILL_SCOPES}")
        await self.db.execute(
            "INSERT OR REPLACE INTO kills VALUES (?,?,?,?)", (scope, value, reason, self._clock())
        )

    async def unkill(self, scope: str, value: str) -> None:
        await self.db.execute("DELETE FROM kills WHERE scope=? AND value=?", (scope, value))

    async def killed_reason(self, vendor: str, client_id: str, jti: str) -> Optional[str]:
        row = await self._one(
            "SELECT scope, reason FROM kills WHERE (scope='vendor' AND value=?) "
            "OR (scope='client' AND value=?) OR (scope='jti' AND value=?) LIMIT 1",
            (vendor, client_id, jti),
        )
        return None if row is None else f"{row[0]} revoked: {row[1]}"

    async def list_kills(self) -> List[Dict[str, Any]]:
        async with self.db.execute(
            "SELECT scope, value, reason, created_at FROM kills ORDER BY created_at"
        ) as cur:
            return [
                {"scope": r[0], "value": r[1], "reason": r[2], "created_at": r[3]}
                async for r in cur
            ]

    async def purge_expired(self) -> None:
        now = self._clock()
        for table, col in (
            ("enrollments", "expires_at"),
            ("pending_authorizations", "expires_at"),
            ("auth_codes", "expires_at"),
            ("issued_jtis", "expires_at"),
            ("refresh_tokens", "expires_at"),
        ):
            await self.db.execute(
                f"DELETE FROM {table} WHERE {col}<?", (now - 86400,)
            )  # nosec B608
