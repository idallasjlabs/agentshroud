"""
API Key Isolation — keys live only in the gateway, never in agent containers.

Keys are stored in memory (encrypted at rest in production), scoped per-agent,
injected transparently on proxied requests, and redacted from all output.
"""

import logging
import re
import time
from dataclasses import dataclass, field
from typing import Optional

logger = logging.getLogger(__name__)


@dataclass
class KeyVaultConfig:
    redact_in_logs: bool = True
    detect_leaks: bool = True


@dataclass
class KeyEntry:
    name: str
    value: str
    scopes: list[str]  # agent IDs or ["*"] for all
    created_at: float = field(default_factory=time.time)
    rotated_at: Optional[float] = None


@dataclass
class KeyScope:
    key_name: str
    agent_ids: list[str]


@dataclass
class KeyAuditEvent:
    timestamp: float
    key_name: str
    agent_id: str
    action: str  # "accessed", "access_denied", "rotated", "deleted", "leak_detected"
    details: str = ""


@dataclass
class LeakScanResult:
    leak_detected: bool
    leaked_key_names: list[str] = field(default_factory=list)


# Common API key patterns for generic detection
GENERIC_KEY_PATTERNS = [
    re.compile(r"\bsk-proj-[a-zA-Z0-9]{20,}\b"),
    re.compile(r"\bsk-[a-zA-Z0-9]{20,}\b"),
    re.compile(r"\bghp_[a-zA-Z0-9]{20,}\b"),
    re.compile(r"\bgho_[a-zA-Z0-9]{20,}\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bxoxb-[a-zA-Z0-9-]+\b"),
]


class KeyVault:
    def __init__(self, config: KeyVaultConfig):
        self.config = config
        self._keys: dict[str, KeyEntry] = {}
        self._old_values: list[str] = []  # for redacting rotated keys
        self._audit: list[KeyAuditEvent] = []

    def store_key(self, name: str, value: str, scopes: Optional[list[str]] = None):
        self._keys[name] = KeyEntry(name=name, value=value, scopes=scopes or ["*"])
        logger.info("Key stored: %s (scopes: %s)", name, scopes)

    def get_key(self, name: str, agent_id: str) -> Optional[str]:
        entry = self._keys.get(name)
        if entry is None:
            return None
        if not self._agent_in_scope(agent_id, entry.scopes):
            self._log_audit(name, agent_id, "access_denied", f"agent not in scope")
            return None
        self._log_audit(name, agent_id, "accessed")
        return entry.value

    def list_keys(self, agent_id: str) -> dict[str, dict]:
        result = {}
        for name, entry in self._keys.items():
            if self._agent_in_scope(agent_id, entry.scopes):
                result[name] = {
                    "scopes": entry.scopes,
                    "created_at": entry.created_at,
                    "rotated_at": entry.rotated_at,
                }
        return result

    def delete_key(self, name: str):
        entry = self._keys.pop(name, None)
        if entry:
            self._old_values.append(entry.value)
            self._log_audit(name, "", "deleted")

    def rotate_key(self, name: str, new_value: str):
        if name not in self._keys:
            raise KeyError(f"Key {name} not found")
        entry = self._keys[name]
        self._old_values.append(entry.value)
        entry.value = new_value
        entry.rotated_at = time.time()
        self._log_audit(name, "", "rotated")

    def redact(self, text: str) -> str:
        for entry in self._keys.values():
            if entry.value in text:
                text = text.replace(entry.value, "[REDACTED]")
        for old in self._old_values:
            if old in text:
                text = text.replace(old, "[REDACTED]")
        return text

    def get_audit_log(self) -> list[KeyAuditEvent]:
        return list(self._audit)

    def _agent_in_scope(self, agent_id: str, scopes: list[str]) -> bool:
        return "*" in scopes or agent_id in scopes

    def _log_audit(self, key_name: str, agent_id: str, action: str, details: str = ""):
        self._audit.append(KeyAuditEvent(
            timestamp=time.time(), key_name=key_name,
            agent_id=agent_id, action=action, details=details,
        ))


class KeyInjector:
    def __init__(self, vault: KeyVault):
        self.vault = vault

    def inject_for_request(self, url: str, headers: dict,
                           agent_id: str, key_name: str) -> dict:
        key = self.vault.get_key(key_name, agent_id)
        result = dict(headers)
        if key:
            result["Authorization"] = f"Bearer {key}"
        return result


class KeyLeakDetector:
    def __init__(self, vault: KeyVault):
        self.vault = vault

    def scan_outbound(self, text: str) -> LeakScanResult:
        leaked = []
        # Check stored keys
        for name, entry in self.vault._keys.items():
            if entry.value in text:
                leaked.append(name)
                self.vault._log_audit(name, "", "leak_detected", "key found in outbound content")

        # Check generic patterns
        if not leaked:
            for pattern in GENERIC_KEY_PATTERNS:
                if pattern.search(text):
                    leaked.append("unknown_key_pattern")
                    self.vault._log_audit("unknown", "", "leak_detected", "generic key pattern in outbound")
                    break

        return LeakScanResult(leak_detected=len(leaked) > 0, leaked_key_names=leaked)
