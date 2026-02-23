# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Dashboard — Proxy Status Display.

Shows real-time status of the security proxy pipeline including:
- Proxy mode (active/sidecar/unprotected)
- Last message proxied
- PII sanitization stats
- Audit chain integrity
- Direct access blocked status
- Canary status
"""
from __future__ import annotations


import time
from dataclasses import dataclass


@dataclass
class ProxyStatusReport:
    """Complete proxy status report for the dashboard."""

    mode: str  # "proxy", "sidecar", "unprotected"
    mode_icon: str
    last_message_proxied_ago: float  # seconds
    pii_sanitized_today: int
    audit_chain_entries: int
    audit_chain_valid: bool
    direct_access_blocked: bool
    direct_access_last_tested: float  # seconds ago
    canary_passed: bool
    canary_last_run: float  # seconds ago
    uptime_seconds: float

    def to_display(self) -> dict[str, str]:
        """Return human-readable dashboard strings."""
        if self.mode == "proxy":
            mode_str = "Proxy mode: ACTIVE \u2705"
        elif self.mode == "sidecar":
            mode_str = "Sidecar mode: ACTIVE \u26a0\ufe0f"
        else:
            mode_str = "UNPROTECTED \u274c"

        last_msg = (
            f"{self.last_message_proxied_ago:.0f}s ago"
            if self.last_message_proxied_ago > 0
            else "never"
        )
        chain_str = (
            f"VERIFIED \u2705 ({self.audit_chain_entries} entries)"
            if self.audit_chain_valid
            else "BROKEN \u274c"
        )
        direct_str = (
            f"\u2705 (last tested: {self.direct_access_last_tested:.0f}s ago)"
            if self.direct_access_blocked
            else "\u274c EXPOSED"
        )
        canary_str = (
            f"PASSED \u2705 (last run: {self.canary_last_run:.0f}s ago)"
            if self.canary_passed
            else "FAILED \u274c"
        )

        return {
            "proxy_mode": mode_str,
            "last_proxied": f"Last message proxied: {last_msg}",
            "pii_today": f"PII items sanitized today: {self.pii_sanitized_today}",
            "audit_chain": f"Audit chain integrity: {chain_str}",
            "direct_access": f"Direct access blocked: {direct_str}",
            "canary": f"Canary status: {canary_str}",
        }


class ProxyDashboard:
    """Collects status from all security components and generates reports."""

    def __init__(self):
        self._mode: str = "unprotected"
        self._started_at: float = time.time()
        self._last_message_time: float = 0
        self._pii_today: int = 0
        self._pii_reset_day: int = 0
        self._audit_entries: int = 0
        self._audit_valid: bool = False
        self._direct_blocked: bool = False
        self._direct_tested_at: float = 0
        self._canary_passed: bool = False
        self._canary_run_at: float = 0

    def set_mode(self, mode: str):
        self._mode = mode

    def record_message_proxied(self):
        self._last_message_time = time.time()

    def record_pii_redaction(self, count: int = 1):
        import datetime

        today = datetime.date.today().day
        if today != self._pii_reset_day:
            self._pii_today = 0
            self._pii_reset_day = today
        self._pii_today += count

    def update_audit_status(self, entries: int, valid: bool):
        self._audit_entries = entries
        self._audit_valid = valid

    def update_direct_access(self, blocked: bool):
        self._direct_blocked = blocked
        self._direct_tested_at = time.time()

    def update_canary(self, passed: bool):
        self._canary_passed = passed
        self._canary_run_at = time.time()

    def get_report(self) -> ProxyStatusReport:
        now = time.time()
        return ProxyStatusReport(
            mode=self._mode,
            mode_icon={
                "proxy": "\u2705",
                "sidecar": "\u26a0\ufe0f",
                "unprotected": "\u274c",
            }.get(self._mode, "\u2753"),
            last_message_proxied_ago=(
                (now - self._last_message_time) if self._last_message_time else -1
            ),
            pii_sanitized_today=self._pii_today,
            audit_chain_entries=self._audit_entries,
            audit_chain_valid=self._audit_valid,
            direct_access_blocked=self._direct_blocked,
            direct_access_last_tested=(
                (now - self._direct_tested_at) if self._direct_tested_at else -1
            ),
            canary_passed=self._canary_passed,
            canary_last_run=(now - self._canary_run_at) if self._canary_run_at else -1,
            uptime_seconds=now - self._started_at,
        )

    def get_display(self) -> dict[str, str]:
        return self.get_report().to_display()
