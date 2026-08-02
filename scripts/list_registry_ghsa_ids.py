#!/usr/bin/env python3
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Print every ghsa_id in the CVE registry, one per line.

Exists so the daily CVE triage job can diff the registry's known GHSA ids
against a fresh GitHub Security Advisories API pull without constructing an
inline extraction one-liner (grep pipes, python3 -c with regex/comprehension
metacharacters) — the gateway's shell-metacharacter guard rejects those with
HTTP 403 "Shell metacharacter injection detected."

Usage:
    python3 scripts/list_registry_ghsa_ids.py
    python3 scripts/list_registry_ghsa_ids.py | sort > /tmp/registry-ghsa-ids.txt
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from gateway.security.agent_cve_registry import (  # noqa: E402
    AGENT_CVE_REGISTRY,
    HERMES_CVE_REGISTRY,
)


def main() -> None:
    for registry in (AGENT_CVE_REGISTRY, HERMES_CVE_REGISTRY):
        for entry in registry:
            ghsa_id = entry.get("ghsa_id")
            if ghsa_id is not None:
                print(ghsa_id)


if __name__ == "__main__":
    main()
