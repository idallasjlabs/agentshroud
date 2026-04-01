# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Owner-Away Privilege Delegation (v0.9.0 Tranche 1)

Owner can delegate specific privileges to trusted collaborators for a bounded
time window. Delegation auto-revokes on expiry. All changes are logged and
persisted on the config volume so they survive gateway restarts.

Delegatable privileges:
  - egress_approval  : Can approve/deny pending egress requests
  - user_management  : Can add/remove members from groups they belong to

Usage:
  mgr = DelegationManager()
  d   = mgr.delegate(owner_id="123", to_user_id="456",
                     privilege=DelegationPrivilege.EGRESS_APPROVAL,
                     duration_hours=4)
  mgr.is_delegated("456", DelegationPrivilege.EGRESS_APPROVAL)  # True
"""
from __future__ import annotations

import fcntl
import json
import logging
import os
import time
import uuid
from dataclasses import asdict, dataclass, field
from enum import Enum
from pathlib import Path
from typing import Dict, List, Optional

logger = logging.getLogger("agentshroud.security.delegation")

_DATA_DIR = Path(os.environ.get("AGENTSHROUD_DATA_DIR", "/app/data"))
_DELEGATIONS_FILE = _DATA_DIR / "delegations.json"


# ---------------------------------------------------------------------------
# Domain types
# ---------------------------------------------------------------------------

class DelegationPrivilege(str, Enum):
    """Subset of privileges that can be delegated by the owner."""
    EGRESS_APPROVAL = "egress_approval"
    USER_MANAGEMENT = "user_management"


class DelegationError(ValueError):
    """Raised when a delegation operation is invalid."""


@dataclass
class Delegation:
    """A single time-bounded privilege delegation record."""
    id: str
    delegated_by: str       # owner user_id
    delegated_to: str       # target user_id
    privilege: str          # DelegationPrivilege value (str for easy JSON round-trip)
    expires_at: float       # Unix timestamp
    created_at: float = field(default_factory=time.time)

    @property
    def is_active(self) -> bool:
        return time.time() < self.expires_at

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict) -> "Delegation":
        return cls(
            id=data["id"],
            delegated_by=data["delegated_by"],
            delegated_to=data["delegated_to"],
            privilege=data["privilege"],
            expires_at=data["expires_at"],
            created_at=data.get("created_at", 0.0),
        )


# ---------------------------------------------------------------------------
# Manager
# ---------------------------------------------------------------------------

class DelegationManager:
    """Manages owner-away privilege delegations.

    Thread-safe via file locking for persistence; in-process dict for fast
    read path (is_delegated is called on every inbound message).
    """

    # Max hours any single delegation can span
    MAX_DURATION_HOURS: int = 72

    def __init__(self, owner_user_id: str = "", persist: bool = True):
        self._owner_user_id = owner_user_id
        self._persist = persist
        # {delegation_id: Delegation}
        self._delegations: Dict[str, Delegation] = {}
        if persist:
            self._load()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def delegate(
        self,
        owner_id: str,
        to_user_id: str,
        privilege: DelegationPrivilege,
        duration_hours: float,
    ) -> Delegation:
        """Create a time-bounded delegation.

        Args:
            owner_id: Must match configured owner_user_id.
            to_user_id: User receiving the delegated privilege.
            privilege: Which privilege to delegate.
            duration_hours: TTL in hours (max 72).

        Returns:
            The new Delegation record.

        Raises:
            DelegationError: If caller is not owner, duration is invalid, or
                             target is the owner (self-delegation unnecessary).
        """
        self._require_owner(owner_id)

        if to_user_id == owner_id:
            raise DelegationError("Owner cannot delegate to themselves")

        if not isinstance(privilege, DelegationPrivilege):
            raise DelegationError(f"Invalid privilege: {privilege!r}")

        if not (0 < duration_hours <= self.MAX_DURATION_HOURS):
            raise DelegationError(
                f"duration_hours must be between 0 and {self.MAX_DURATION_HOURS}, "
                f"got {duration_hours}"
            )

        # Revoke any existing active delegation for the same user+privilege
        # before creating a new one (idempotent re-delegation).
        self._revoke_by_user_privilege(to_user_id, privilege, caller_is_owner=True)

        d = Delegation(
            id=str(uuid.uuid4()),
            delegated_by=owner_id,
            delegated_to=to_user_id,
            privilege=privilege.value,
            expires_at=time.time() + duration_hours * 3600,
        )
        self._delegations[d.id] = d
        self._save()

        logger.info(
            "Delegation created: %s → %s priv=%s ttl=%.1fh id=%s",
            owner_id, to_user_id, privilege.value, duration_hours, d.id,
        )
        return d

    def revoke(self, owner_id: str, to_user_id: str, privilege: DelegationPrivilege) -> bool:
        """Revoke an active delegation.

        Returns True if a matching active delegation was found and removed.
        """
        self._require_owner(owner_id)
        return self._revoke_by_user_privilege(to_user_id, privilege, caller_is_owner=True)

    def revoke_all_for_user(self, owner_id: str, to_user_id: str) -> int:
        """Revoke all delegations for a specific user. Returns count removed."""
        self._require_owner(owner_id)
        ids_to_remove = [
            did for did, d in self._delegations.items()
            if d.delegated_to == to_user_id and d.is_active
        ]
        for did in ids_to_remove:
            del self._delegations[did]
            logger.info("Delegation revoked: id=%s user=%s (bulk revoke)", did, to_user_id)
        if ids_to_remove:
            self._save()
        return len(ids_to_remove)

    def is_delegated(self, user_id: str, privilege: DelegationPrivilege) -> bool:
        """Return True if the user currently holds the delegated privilege."""
        self._cleanup_expired()
        priv_val = privilege.value if isinstance(privilege, DelegationPrivilege) else privilege
        return any(
            d.delegated_to == user_id and d.privilege == priv_val and d.is_active
            for d in self._delegations.values()
        )

    def get_active_delegations(self) -> List[Delegation]:
        """Return all currently active (non-expired) delegations."""
        self._cleanup_expired()
        return [d for d in self._delegations.values() if d.is_active]

    def get_delegations_for_user(self, user_id: str) -> List[Delegation]:
        """Return all active delegations held by a specific user."""
        self._cleanup_expired()
        return [
            d for d in self._delegations.values()
            if d.delegated_to == user_id and d.is_active
        ]

    def cleanup_expired(self) -> int:
        """Remove expired delegations, persist result. Returns count removed."""
        expired = [did for did, d in self._delegations.items() if not d.is_active]
        for did in expired:
            d = self._delegations.pop(did)
            logger.debug("Delegation expired and pruned: id=%s user=%s priv=%s", did, d.delegated_to, d.privilege)
        if expired:
            self._save()
        return len(expired)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _require_owner(self, user_id: str) -> None:
        if self._owner_user_id and user_id != self._owner_user_id:
            raise DelegationError(f"Only the owner can manage delegations, got user_id={user_id!r}")

    def _revoke_by_user_privilege(
        self, to_user_id: str, privilege: DelegationPrivilege, *, caller_is_owner: bool
    ) -> bool:
        priv_val = privilege.value if isinstance(privilege, DelegationPrivilege) else privilege
        matches = [
            did for did, d in self._delegations.items()
            if d.delegated_to == to_user_id and d.privilege == priv_val and d.is_active
        ]
        for did in matches:
            del self._delegations[did]
            logger.info("Delegation revoked: id=%s user=%s priv=%s", did, to_user_id, priv_val)
        if matches:
            self._save()
        return bool(matches)

    def _cleanup_expired(self) -> None:
        expired = [did for did, d in self._delegations.items() if not d.is_active]
        for did in expired:
            self._delegations.pop(did, None)

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def _load(self) -> None:
        try:
            if _DELEGATIONS_FILE.exists():
                raw = json.loads(_DELEGATIONS_FILE.read_text(encoding="utf-8"))
                for item in raw.get("delegations", []):
                    try:
                        d = Delegation.from_dict(item)
                        if d.is_active:  # skip already-expired on load
                            self._delegations[d.id] = d
                    except Exception as exc:
                        logger.warning("Skipping malformed delegation record: %s", exc)
                logger.info("Loaded %d active delegations", len(self._delegations))
        except Exception as exc:
            logger.warning("Could not load delegations.json: %s", exc)

    def _save(self) -> None:
        if not self._persist:
            return
        _DATA_DIR.mkdir(parents=True, exist_ok=True)
        lock_path = _DELEGATIONS_FILE.with_suffix(".lock")
        try:
            with open(lock_path, "w") as lf:
                fcntl.flock(lf, fcntl.LOCK_EX)
                try:
                    payload = {"delegations": [d.to_dict() for d in self._delegations.values()]}
                    _DELEGATIONS_FILE.write_text(json.dumps(payload, indent=2), encoding="utf-8")
                finally:
                    fcntl.flock(lf, fcntl.LOCK_UN)
        except Exception as exc:
            logger.warning("Could not persist delegations.json: %s", exc)
