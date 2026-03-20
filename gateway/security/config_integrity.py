# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Config Integrity Monitor — detects tampering with bot configuration files.

Hashes openclaw.json and other security-critical workspace files at gateway
startup. On each subsequent startup (or on-demand check), compares against the
stored baseline and alerts the owner via Telegram if anything changed unexpectedly.

Why this matters: the bot's config volume (agentshroud-config) is writable by the
bot container. A compromised bot could edit openclaw.json directly, silently
weakening tool restrictions or agent bindings without a container rebuild. The
gateway mounts this volume read-only and acts as an independent audit observer.
"""
from __future__ import annotations

import hashlib
import json
import logging
import time
from pathlib import Path
from typing import Dict, Optional

logger = logging.getLogger("agentshroud.security.config_integrity")

# Files to monitor, relative to the bot config mount point (/data/bot-config)
_MONITORED_FILES = [
    "openclaw.json",
]


class ConfigIntegrityMonitor:
    """Computes and verifies SHA256 hashes of monitored bot config files.

    At gateway startup:
      1. Compute hashes of all monitored files
      2. Compare against the last known baseline stored in gateway-data
      3. If changed → log warning + return alert info for Telegram notification
      4. Store new baseline

    Args:
        bot_config_dir: Path to the bot config volume mount (read-only in gateway).
            Typically /data/bot-config.
        baseline_path: Where to persist baseline hashes (gateway-data volume).
            Typically /app/data/config-integrity-baseline.json.
    """

    def __init__(
        self,
        bot_config_dir: Path,
        baseline_path: Path,
    ) -> None:
        self.bot_config_dir = bot_config_dir
        self.baseline_path = baseline_path

    def _hash_file(self, path: Path) -> Optional[str]:
        """Return hex SHA256 of a file, or None if the file does not exist."""
        try:
            h = hashlib.sha256(path.read_bytes())
            return h.hexdigest()
        except (FileNotFoundError, OSError):
            return None

    def _load_baseline(self) -> Dict[str, Optional[str]]:
        """Load the last known baseline from disk. Returns empty dict if not found."""
        try:
            data = json.loads(self.baseline_path.read_text(encoding="utf-8"))
            return data.get("hashes", {})
        except (FileNotFoundError, OSError, json.JSONDecodeError):
            return {}

    def _save_baseline(self, hashes: Dict[str, Optional[str]]) -> None:
        """Persist the current hashes as the new baseline."""
        try:
            self.baseline_path.parent.mkdir(parents=True, exist_ok=True)
            payload = {
                "updated_at": time.time(),
                "hashes": hashes,
            }
            self.baseline_path.write_text(
                json.dumps(payload, indent=2), encoding="utf-8"
            )
        except OSError as exc:
            logger.warning("ConfigIntegrityMonitor: could not save baseline: %s", exc)

    def check(self) -> list[dict]:
        """Compare current file hashes against baseline.

        Returns a list of change records — empty means everything matches.
        Each record: {"file": str, "previous": str|None, "current": str|None, "event": str}
        event values: "modified", "added", "removed"
        """
        baseline = self._load_baseline()
        current: Dict[str, Optional[str]] = {}
        changes: list[dict] = []

        for rel_path in _MONITORED_FILES:
            abs_path = self.bot_config_dir / rel_path
            current[rel_path] = self._hash_file(abs_path)

        for rel_path in _MONITORED_FILES:
            prev = baseline.get(rel_path)
            curr = current.get(rel_path)

            if prev is None and curr is not None:
                event = "added"
            elif prev is not None and curr is None:
                event = "removed"
            elif prev != curr:
                event = "modified"
            else:
                continue  # unchanged

            changes.append({
                "file": rel_path,
                "previous": prev,
                "current": curr,
                "event": event,
            })
            logger.warning(
                "ConfigIntegrityMonitor: %s → %s (was %s, now %s)",
                rel_path, event,
                (prev or "MISSING")[:12] + "..." if prev else "MISSING",
                (curr or "MISSING")[:12] + "..." if curr else "MISSING",
            )

        # Only advance the baseline when no changes are detected.  If tampering is
        # found, preserve the prior baseline so the alert re-fires on the next restart
        # until the owner explicitly acknowledges the deviation.
        if not changes:
            self._save_baseline(current)

        return changes

    def reset_baseline(self) -> None:
        """Accept current file hashes as the new baseline (owner-acknowledged rebuild)."""
        current: Dict[str, Optional[str]] = {}
        for rel_path in _MONITORED_FILES:
            abs_path = self.bot_config_dir / rel_path
            current[rel_path] = self._hash_file(abs_path)
        self._save_baseline(current)
        logger.info(
            "ConfigIntegrityMonitor: baseline reset by owner (%d file(s))", len(current)
        )

    def format_alert_text(self, changes: list[dict]) -> str:
        """Format Telegram alert text for detected config changes."""
        lines = ["⚠️ *Config Integrity Alert*\n"]
        for c in changes:
            prev_short = (c["previous"] or "MISSING")[:8]
            curr_short = (c["current"] or "MISSING")[:8]
            lines.append(
                f"• `{c['file']}` {c['event'].upper()}\n"
                f"  Before: `{prev_short}...`\n"
                f"  After:  `{curr_short}...`"
            )
        lines.append(
            "\nBot config may have been modified without a rebuild. "
            "Inspect `openclaw.json` on the agentshroud-config volume."
        )
        return "\n".join(lines)
