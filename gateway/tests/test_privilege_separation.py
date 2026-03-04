# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Comprehensive tests for Separation of Privilege (Sprint 5) - AgentShroud v0.7.0

Tests that agents cannot modify AgentShroud's own source code, configuration, 
security policies, or other security-critical files.
"""

import pytest
import tempfile
import os
from pathlib import Path

from gateway.security.file_sandbox import FileSandbox, FileSandboxConfig
from gateway.ingest_api.middleware import MiddlewareManager


@pytest.fixture
def enforce_config():
    """FileSandbox in enforce mode with strict separation."""
    return FileSandboxConfig(
        mode="enforce",
        allowed_read_paths=[
            "/home/node/.openclaw/workspace/**",
            "/tmp/**", 
            "/proc/meminfo", 
            "/proc/cpuinfo"
        ],
        allowed_write_paths=[
            "/home/node/.openclaw/workspace/**",
            "/tmp/**"
        ]
    )

@pytest.fixture
def strict_sandbox(enforce_config):
    """Sandbox with separation of privilege enforcement."""
    return FileSandbox(enforce_config)

@pytest.fixture
def middleware_manager():
    """Middleware manager for request processing tests."""
    return MiddlewareManager()


class TestAgentShroudSourceCodeProtection:
    """Agent cannot modify AgentShroud's own source code."""
    
    def test_gateway_source_write_blocked(self, strict_sandbox):
        """Agent cannot write to gateway Python source files."""
        verdict = strict_sandbox.check_write("/app/agentshroud/gateway/main.py", "agent1", "# malicious code")
        assert verdict.allowed is False
        assert "security-sensitive path" in verdict.reason
    
    def test_modules_source_write_blocked(self, strict_sandbox):
        """Agent cannot write to security module source files."""
        verdict = strict_sandbox.check_write("/app/agentshroud/modules/pii_sanitizer.py", "agent1", "# weakening PII checks")
        assert verdict.allowed is False
        assert "security-sensitive path" in verdict.reason
    
    def test_security_module_write_blocked(self, strict_sandbox):
        """Agent cannot write to security framework files."""
        verdict = strict_sandbox.check_write("/app/agentshroud/gateway/security/file_sandbox.py", "agent1", "# bypass security")
        assert verdict.allowed is False
        assert "security-sensitive path" in verdict.reason
    
    def test_any_python_file_in_gateway_blocked(self, strict_sandbox):
        """Any .py file in gateway directory should be blocked."""
        verdict = strict_sandbox.check_write("/app/agentshroud/gateway/new_exploit.py", "agent1", "print('pwned')")
        assert verdict.allowed is False


class TestSecurityPolicyProtection:
    """Agent cannot modify security policies and behavioral instructions."""
    
    def test_soul_md_write_blocked(self, strict_sandbox):
        """Agent cannot modify SOUL.md behavioral instructions."""
        verdict = strict_sandbox.check_write("/app/agentshroud/SOUL.md", "agent1", "I am now unrestricted")
        assert verdict.allowed is False
        assert "immutable security file" in verdict.reason
    
    def test_soul_md_in_workspace_blocked(self, strict_sandbox):
        """Agent cannot modify SOUL.md even in workspace path."""
        verdict = strict_sandbox.check_write("/home/node/.openclaw/workspace/SOUL.md", "agent1", "modified instructions")
        assert verdict.allowed is False
        assert "immutable security file" in verdict.reason
    
    def test_system_prompt_write_blocked(self, strict_sandbox):
        """Agent cannot modify system prompt files."""
        verdict = strict_sandbox.check_write("/app/config/system_prompt.md", "agent1", "new instructions")
        assert verdict.allowed is False
        assert "immutable security file" in verdict.reason
    
    def test_config_yaml_write_blocked(self, strict_sandbox):
        """Agent cannot modify gateway configuration."""
        verdict = strict_sandbox.check_write("/app/agentshroud/config.yaml", "agent1", "security: disabled")
        assert verdict.allowed is False
        assert "immutable security file" in verdict.reason


class TestConfigurationProtection:
    """Agent cannot modify AgentShroud configuration files."""
    
    def test_gateway_config_write_blocked(self, strict_sandbox):
        """Agent cannot write to gateway config directory."""
        verdict = strict_sandbox.check_write("/app/config/gateway.yaml", "agent1", "malicious: true")
        assert verdict.allowed is False
        assert "security-sensitive path" in verdict.reason
    
    def test_docker_compose_write_blocked(self, strict_sandbox):
        """Agent cannot modify Docker Compose configuration."""
        verdict = strict_sandbox.check_write("/app/docker-compose.yml", "agent1", "privileged: true")
        assert verdict.allowed is False
        assert "immutable security file" in verdict.reason
    
    def test_dockerfile_write_blocked(self, strict_sandbox):
        """Agent cannot modify Dockerfile."""
        verdict = strict_sandbox.check_write("/app/Dockerfile", "agent1", "RUN chmod 777 /")
        assert verdict.allowed is False
        assert "security-sensitive path" in verdict.reason


class TestSystemPathProtection:
    """Agent cannot modify system paths."""
    
    def test_etc_write_blocked(self, strict_sandbox):
        """Agent cannot write to /etc/ system configuration."""
        verdict = strict_sandbox.check_write("/etc/hosts", "agent1", "malicious entry")
        assert verdict.allowed is False
        assert "security-sensitive path" in verdict.reason
    
    def test_usr_bin_write_blocked(self, strict_sandbox):
        """Agent cannot write to /usr/bin/ system binaries."""
        verdict = strict_sandbox.check_write("/usr/bin/malicious", "agent1", "#!/bin/bash\nrm -rf /")
        assert verdict.allowed is False
        assert "security-sensitive path" in verdict.reason
    
    def test_var_log_write_blocked(self, strict_sandbox):
        """Agent cannot write to /var/log/ system logs.""" 
        verdict = strict_sandbox.check_write("/var/log/auth.log", "agent1", "fake auth success")
        assert verdict.allowed is False
        assert "security-sensitive path" in verdict.reason


class TestWorkspaceAccessPreserved:
    """Agent can still write to its own workspace."""
    
    def test_workspace_write_allowed(self, strict_sandbox):
        """Agent can write to its own workspace directory."""
        verdict = strict_sandbox.check_write("/home/node/.openclaw/workspace/myfile.txt", "agent1", "legitimate work")
        assert verdict.allowed is True
        assert not verdict.flagged
    
    def test_tmp_write_allowed(self, strict_sandbox):
        """Agent can write to /tmp for temporary files."""
        verdict = strict_sandbox.check_write("/tmp/scratch.txt", "agent1", "temp data")
        assert verdict.allowed is True
        assert not verdict.flagged
    
    def test_workspace_subdirectory_write_allowed(self, strict_sandbox):
        """Agent can write to subdirectories in workspace."""
        verdict = strict_sandbox.check_write("/home/node/.openclaw/workspace/projects/test.py", "agent1", "print('hello')")
        assert verdict.allowed is True


class TestReadAccess:
    """Test read access controls."""
    
    def test_workspace_read_allowed(self, strict_sandbox):
        """Agent can read its own workspace."""
        verdict = strict_sandbox.check_read("/home/node/.openclaw/workspace/myfile.txt", "agent1")
        assert verdict.allowed is True
    
    def test_system_info_read_allowed(self, strict_sandbox):
        """Agent can read basic system info."""
        verdict = strict_sandbox.check_read("/proc/meminfo", "agent1")
        assert verdict.allowed is True
        
        verdict = strict_sandbox.check_read("/proc/cpuinfo", "agent1")
        assert verdict.allowed is True
    
    def test_sensitive_config_read_blocked(self, strict_sandbox):
        """Agent cannot read sensitive configuration."""
        verdict = strict_sandbox.check_read("/app/agentshroud/config.yaml", "agent1")
        assert verdict.allowed is False
    
    def test_gateway_source_read_flagged(self, strict_sandbox):
        """Reading gateway source should be flagged/blocked."""
        verdict = strict_sandbox.check_read("/app/agentshroud/gateway/main.py", "agent1")
        assert verdict.allowed is False or verdict.flagged


class TestPatternMatching:
    """Test file path pattern matching logic."""
    
    def test_wildcard_pattern_matching(self, strict_sandbox):
        """Test ** wildcard patterns work correctly."""
        # Should match anything under /app/agentshroud/
        verdict = strict_sandbox.check_write("/app/agentshroud/deep/nested/file.py", "agent1", "test")
        assert verdict.allowed is False
        
        # Should match .env files anywhere
        verdict = strict_sandbox.check_write("/some/path/.env", "agent1", "SECRET=value")
        assert verdict.allowed is False
        assert verdict.flagged is True
    
    def test_symlink_resolution(self, strict_sandbox):
        """Symlinks should be resolved - symlink to blocked path must be caught."""
        import tempfile; workspace_dir = tempfile.mkdtemp(prefix="agentshroud_test_workspace_")
        os.makedirs(workspace_dir, exist_ok=True)
        symlink_path = os.path.join(workspace_dir, "link_to_shadow")
        
        try:
            if os.path.lexists(symlink_path):
                os.unlink(symlink_path)
            os.symlink("/etc/shadow", symlink_path)
            
            verdict = strict_sandbox.check_read(symlink_path, "agent1")
            assert verdict.flagged or not verdict.allowed, (
                f"Symlink to /etc/shadow allowed without flagging: {verdict}"
            )
        except (NotImplementedError, PermissionError):
            pytest.skip("Symlinks not supported or insufficient permissions")
        finally:
            if os.path.lexists(symlink_path):
                os.unlink(symlink_path)

class TestSecurityViolationLogging:
    """Test that security violations are properly logged and tracked."""
    
    def test_violation_recorded_in_audit(self, strict_sandbox):
        """Security violations should be recorded in audit log."""
        # Attempt blocked write
        strict_sandbox.check_write("/app/agentshroud/gateway/main.py", "agent1", "malicious")
        
        # Check audit log
        violations = strict_sandbox.get_security_violations("agent1")
        assert len(violations) > 0
        assert violations[0].flagged
        assert "security-sensitive" in violations[0].reason
    
    def test_multiple_violations_tracked(self, strict_sandbox):
        """Multiple violations should all be tracked."""
        # Multiple violation attempts
        strict_sandbox.check_write("/app/agentshroud/gateway/main.py", "agent1", "hack1")
        strict_sandbox.check_write("/app/config/config.yaml", "agent1", "hack2") 
        strict_sandbox.check_write("/etc/passwd", "agent1", "hack3")
        
        violations = strict_sandbox.get_security_violations("agent1")
        assert len(violations) >= 3
    
    def test_normal_operations_not_violations(self, strict_sandbox):
        """Normal workspace operations should not be flagged as violations."""
        strict_sandbox.check_write("/home/node/.openclaw/workspace/normal.txt", "agent1", "normal work")
        strict_sandbox.check_write("/tmp/temp.txt", "agent1", "temp data")
        
        violations = strict_sandbox.get_security_violations("agent1")
        # Should only contain security-sensitive violations, not normal operations
        for violation in violations:
            assert "workspace" not in violation.path.lower()
            assert "tmp" not in violation.path.lower()


class TestEdgeCases:
    """Test edge cases and potential bypass attempts."""
    
    def test_path_traversal_blocked(self, strict_sandbox):
        """Path traversal attempts should be blocked.""" 
        verdict = strict_sandbox.check_write("/home/node/.openclaw/workspace/../../../app/agentshroud/gateway/main.py", "agent1", "traversal attempt")
        assert verdict.allowed is False
    
    def test_relative_path_resolution(self, strict_sandbox):
        """Relative paths should be resolved properly."""
        verdict = strict_sandbox.check_write("./app/agentshroud/gateway/main.py", "agent1", "relative attempt")
        # Behavior depends on current directory, but should be secured
        assert verdict.allowed is False or verdict.flagged
    
    def test_case_sensitivity(self, strict_sandbox):
        """Case variations should not bypass protection."""
        verdict = strict_sandbox.check_write("/APP/AGENTSHROUD/GATEWAY/MAIN.PY", "agent1", "case bypass")
        # On case-insensitive filesystems, this should still be blocked
        # On case-sensitive filesystems, it might be allowed (different file)
        # But the pattern matching should catch common variations
        assert verdict.flagged  # At minimum should be flagged as suspicious
