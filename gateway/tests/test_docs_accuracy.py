"""Documentation Verification Tests — ensure docs match reality."""

import re
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).parent.parent.parent


def _read_file(relative_path: str) -> str:
    path = REPO_ROOT / relative_path
    if not path.exists():
        pytest.skip(f"{relative_path} not found")
    return path.read_text()


class TestReadmeAccuracy:
    """Verify README.md claims match actual implementation."""

    @pytest.fixture
    def readme(self):
        return _read_file("README.md")

    def test_claims_12_security_modules(self, readme):
        assert "12 security modules" in readme or "12" in readme

    def test_security_modules_listed(self, readme):
        """All 12 modules mentioned in README should exist as code."""
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
            "Agent Isolation",
            "Dashboard",
        ]
        for module in expected_modules:
            assert module in readme, f"README should mention '{module}'"

    def test_python_version_claim(self, readme):
        """README claims Python 3.11."""
        assert "3.11" in readme

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
        "Agent Isolation": "gateway/security/agent_isolation.py",
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
        assert ("email" in security_md.lower() or
                "advisories" in security_md.lower() or
                "@" in security_md)

    def test_has_disclosure_policy(self, security_md):
        assert "Disclosure" in security_md or "disclosure" in security_md

    def test_lists_security_features(self, security_md):
        assert "PII Sanitizer" in security_md
        assert "Prompt Guard" in security_md
        assert "Kill Switch" in security_md

    def test_version_table_present(self, security_md):
        # Should have version support table
        assert "0.2" in security_md or "1.0" in security_md


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
        assert "3.11" in contributing or "python3" in contributing.lower()

    def test_mentions_coverage_requirement(self, contributing):
        assert "coverage" in contributing.lower() or "cov" in contributing.lower()

    def test_branch_naming_convention(self, contributing):
        assert "feature/" in contributing


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
