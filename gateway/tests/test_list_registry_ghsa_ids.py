# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Tests for scripts/list_registry_ghsa_ids.py.

Exists so the daily CVE triage job can diff the registry against a fresh
GitHub Security Advisories pull without an inline extraction one-liner (the
gateway's shell-metacharacter guard rejects grep pipes / python3 -c regex
comprehensions with HTTP 403).
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from unittest.mock import patch

REPO_ROOT = Path(__file__).resolve().parent.parent.parent

_MOD_NAME = "scripts._list_registry_ghsa_ids"
_MOD_PATH = REPO_ROOT / "scripts" / "list_registry_ghsa_ids.py"

if _MOD_NAME not in sys.modules:
    _spec = importlib.util.spec_from_file_location(_MOD_NAME, _MOD_PATH)
    assert _spec is not None
    _mod = importlib.util.module_from_spec(_spec)
    sys.modules[_MOD_NAME] = _mod
    _spec.loader.exec_module(_mod)  # type: ignore[union-attr]


def _script():
    return sys.modules[_MOD_NAME]


class TestListRegistryGhsaIds:
    def test_prints_every_ghsa_id_one_per_line(self, capsys):
        agent_registry = [
            {"ghsa_id": "GHSA-aaaa-bbbb-cccc"},
            {"ghsa_id": "GHSA-dddd-eeee-ffff"},
        ]
        hermes_registry = [{"ghsa_id": "GHSA-gggg-hhhh-iiii"}]

        with (
            patch.object(_script(), "AGENT_CVE_REGISTRY", agent_registry),
            patch.object(_script(), "HERMES_CVE_REGISTRY", hermes_registry),
        ):
            _script().main()

        out = capsys.readouterr().out.splitlines()
        assert out == [
            "GHSA-aaaa-bbbb-cccc",
            "GHSA-dddd-eeee-ffff",
            "GHSA-gggg-hhhh-iiii",
        ]

    def test_skips_none_ghsa_id_entries(self, capsys):
        agent_registry = [
            {"ghsa_id": "GHSA-aaaa-bbbb-cccc"},
            {"ghsa_id": None},
        ]
        hermes_registry = [{"ghsa_id": None}]

        with (
            patch.object(_script(), "AGENT_CVE_REGISTRY", agent_registry),
            patch.object(_script(), "HERMES_CVE_REGISTRY", hermes_registry),
        ):
            _script().main()

        out = capsys.readouterr().out.splitlines()
        assert out == ["GHSA-aaaa-bbbb-cccc"]

    def test_empty_registries_print_nothing(self, capsys):
        with (
            patch.object(_script(), "AGENT_CVE_REGISTRY", []),
            patch.object(_script(), "HERMES_CVE_REGISTRY", []),
        ):
            _script().main()

        assert capsys.readouterr().out == ""

    def test_against_the_real_registry(self, capsys):
        """Smoke test against the actual committed registry — every real
        ghsa_id currently in gateway/security/agent_cve_registry.py must be
        importable and printable with no crash."""
        from gateway.security.agent_cve_registry import (
            AGENT_CVE_REGISTRY,
            HERMES_CVE_REGISTRY,
        )

        _script().main()
        out = capsys.readouterr().out.splitlines()

        expected_count = sum(
            1
            for registry in (AGENT_CVE_REGISTRY, HERMES_CVE_REGISTRY)
            for entry in registry
            if entry.get("ghsa_id") is not None
        )
        assert len(out) == expected_count
        assert all(line.startswith("GHSA-") for line in out)
