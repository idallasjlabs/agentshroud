# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Documentation Verification Tests — ensure docs match reality."""

from __future__ import annotations

import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent.parent


def _read_file(relative_path: str) -> str | None:
    path = REPO_ROOT / relative_path
    if not path.exists():
        return None
    return path.read_text()


class TestReadmeAccuracy:
    """Verify README.md claims match actual implementation."""

    @pytest.fixture
    def readme(self):
        return _read_file("README.md")

    def test_claims_68_security_modules(self, readme):
        assert "68 security modules" in readme

    def test_security_modules_listed(self, readme):
        """This representative sample of modules mentioned in README should exist as code."""
        expected_modules = [
            "PII Sanitizer",
            "Approval Queue",
            "Audit Ledger",
            "Prompt Guard",
            "Egress Filter",
            "Trust Manager",
            "Drift Detector",
            "Encrypted Store",
            "SSH Proxy",
            "Kill Switch",
            "Isolation Verifier",
            "Dashboard",
        ]
        for module in expected_modules:
            assert module in readme, f"README should mention '{module}'"

    def test_python_version_claim(self, readme):
        """README claims Python 3.9+."""
        assert "3.9" in readme or "python" in readme.lower()

    def test_mentions_mit_license(self, readme):
        assert "MIT" in readme

    def test_architecture_diagram_present(self, readme):
        assert "AGENTSHROUD GATEWAY" in readme

    def test_quickstart_section_present(self, readme):
        assert "Quickstart" in readme or "quickstart" in readme


class TestReadmeModulesMatchCode:
    """Verify each module listed in README has actual implementation."""

    MODULE_FILES = {
        "PII Sanitizer": "gateway/ingest_api/sanitizer.py",
        "Approval Queue": "gateway/approval_queue/queue.py",
        "Audit Ledger": "gateway/ingest_api/ledger.py",
        "Prompt Guard": "gateway/security/prompt_guard.py",
        "Egress Filter": "gateway/security/egress_filter.py",
        "Trust Manager": "gateway/security/trust_manager.py",
        "Drift Detector": "gateway/security/drift_detector.py",
        "Encrypted Store": "gateway/security/encrypted_store.py",
        "SSH Proxy": "gateway/ssh_proxy/proxy.py",
        "Isolation Verifier": "gateway/security/agent_isolation.py",
    }

    @pytest.mark.parametrize("module_name,file_path", MODULE_FILES.items())
    def test_module_has_implementation(self, module_name, file_path):
        path = REPO_ROOT / file_path
        assert path.exists(), f"Module '{module_name}' missing implementation at {file_path}"
        content = path.read_text()
        assert len(content) > 100, f"Module '{module_name}' at {file_path} appears to be a stub"


class TestSecurityMdAccuracy:
    """Verify SECURITY.md content."""

    @pytest.fixture
    def security_md(self):
        return _read_file("SECURITY.md")

    def test_has_supported_versions(self, security_md):
        assert "Supported Versions" in security_md

    def test_has_security_contact(self, security_md):
        assert "security" in security_md.lower()
        # Should have some contact method
        assert (
            "email" in security_md.lower()
            or "advisories" in security_md.lower()
            or "@" in security_md
        )

    def test_has_disclosure_policy(self, security_md):
        assert "Disclosure" in security_md or "disclosure" in security_md

    def test_lists_security_features(self, security_md):
        assert "PII Sanitizer" in security_md
        # SECURITY.md uses "PromptGuard" (no space) — accept both spellings
        assert "PromptGuard" in security_md or "Prompt Guard" in security_md
        assert (
            "Kill Switch" in security_md
            or "KillSwitch" in security_md
            or "kill switch" in security_md.lower()
        )

    def test_version_table_present(self, security_md):
        # Should have version support table with current or recent versions
        assert any(v in security_md for v in ("1.0", "0.9", "0.8", "0.7", "0.6"))


class TestContributingMdAccuracy:
    """Verify CONTRIBUTING.md references are correct."""

    @pytest.fixture
    def contributing(self):
        return _read_file("CONTRIBUTING.md")

    def test_mentions_pytest(self, contributing):
        assert "pytest" in contributing

    def test_mentions_test_directory(self, contributing):
        assert "gateway/tests" in contributing

    def test_pytest_command_syntax(self, contributing):
        """The test command in CONTRIBUTING.md should be valid."""
        assert "pytest gateway/tests/" in contributing

    def test_mentions_python_311(self, contributing):
        assert "3.9" in contributing or "python3" in contributing.lower()

    def test_mentions_coverage_requirement(self, contributing):
        assert "coverage" in contributing.lower() or "cov" in contributing.lower()

    def test_branch_naming_convention(self, contributing):
        assert "feature/" in contributing


class TestManageModulesEndpointAccuracy:
    """Verify /manage/modules enumerates every module MiddlewareManager wires.

    MiddlewareManager.ALL_MODULE_ATTRS is the single source of truth for which
    P1 module attributes exist on the class; both the live status endpoint and
    README's P1 tier count must be derived from — not merely consistent with —
    this list, or the three drift silently the way they did before.
    """

    def test_all_module_attrs_exist_after_init(self):
        from gateway.ingest_api.middleware import MiddlewareManager

        mm = MiddlewareManager()
        assert len(MiddlewareManager.ALL_MODULE_ATTRS) >= 30
        for name in MiddlewareManager.ALL_MODULE_ATTRS:
            assert hasattr(mm, name), f"MiddlewareManager has no attribute '{name}'"

    def test_manage_modules_endpoint_uses_the_same_registry(self):
        """The endpoint's P1 section must be generated from ALL_MODULE_ATTRS,
        not a separately hand-maintained name list that can drift from it."""
        import inspect

        from gateway.ingest_api import main as main_module

        source = inspect.getsource(main_module.list_security_modules)
        assert "ALL_MODULE_ATTRS" in source

    def test_readme_p1_count_matches_middleware_manager(self):
        from gateway.ingest_api.middleware import MiddlewareManager

        readme = _read_file("README.md")
        real_count = len(MiddlewareManager.ALL_MODULE_ATTRS)
        assert f"P1 — Middleware**: {real_count} modules wired" in readme, (
            f"README's P1 tier count is stale: MiddlewareManager wires " f"{real_count} modules"
        )

    @pytest.mark.asyncio
    async def test_endpoint_reports_no_key_collisions_and_high_total(self, monkeypatch):
        """Execute the real endpoint against a fully-populated app_state and
        verify it enumerates a total close to the "68 security modules" public
        claim, with no tier silently overwriting another tier's entry for the
        same module name (the bug that made the old hardcoded P1/P2 lists
        under-report ~37 total instead of anywhere near 68)."""
        from types import SimpleNamespace

        from gateway.ingest_api import main as main_module
        from gateway.ingest_api.middleware import MiddlewareManager

        fake = SimpleNamespace()
        fake.sanitizer = SimpleNamespace(mode="enforce")
        for name in (
            "approval_queue",
            "pipeline",
            "prompt_guard",
            "trust_manager",
            "egress_filter",
            "prompt_protection",
            "heuristic_classifier",
            "network_validator",
            "alert_dispatcher",
            "killswitch_monitor",
            "drift_detector",
            "encrypted_store",
            "key_vault",
            "health_report",
            "canary_runner",
            "clamav_scanner",
            "trivy_scanner",
            "falco_monitor",
            "wazuh_client",
            "config_integrity",
            "cron_state_monitor",
            "collaborator_tracker",
            "memory_integrity",
            "memory_lifecycle",
            "egress_approval_queue",
            "outbound_filter",
            "tool_acl_enforcer",
            "privacy_enforcer",
            "delegation_manager",
            "report_store",
            "audit_store",
        ):
            setattr(fake, name, object())
        fake.openscap_available = True
        fake.middleware_manager = MiddlewareManager()

        monkeypatch.setattr(main_module, "app_state", fake)

        result = await main_module.list_security_modules(auth=None)

        assert result["total"] == len(result["modules"]), "duplicate keys collapsed silently"
        statuses = {m["status"] for m in result["modules"].values()}
        assert statuses <= {"active", "loaded", "unavailable", "degraded"}
        assert result["total"] >= 60, (
            f"endpoint only enumerates {result['total']} modules — still far "
            f"short of the public '68 security modules' claim"
        )


class TestTestCountAccuracy:
    """Verify test count claims in README/docs are reasonable."""

    def test_actual_test_count_meets_minimum(self):
        """We should have at least 350 tests (README says 351+)."""
        # Count test functions across all test files
        tests_dir = REPO_ROOT / "gateway" / "tests"
        test_count = 0
        for test_file in tests_dir.glob("test_*.py"):
            content = test_file.read_text()
            # Count def test_ and async def test_ functions
            test_count += len(re.findall(r"^\s*(?:async\s+)?def\s+test_", content, re.MULTILINE))
            # Count parametrize decorators (each adds tests)
            test_count += len(re.findall(r"@pytest\.mark\.parametrize", content))

        assert test_count >= 350, f"Expected 350+ test functions, found {test_count}"
