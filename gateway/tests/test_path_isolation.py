# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

"""Tests for path isolation functionality."""

import os
import pytest
import tempfile
import shutil
from pathlib import Path
from unittest.mock import patch, MagicMock

from gateway.security.path_isolation import (
    PathIsolationManager,
    PathIsolationConfig,
    PathRewriteResult,
)


class TestPathIsolationConfig:
    """Test path isolation configuration."""
    
    def test_default_config(self):
        """Test default configuration values."""
        config = PathIsolationConfig()
        
        assert config.base_temp_dir == "/tmp/agentshroud"
        assert config.cleanup_on_session_end is True
        assert "/tmp" in config.isolated_paths
        assert "/var/tmp" in config.isolated_paths
        assert config.max_abandoned_age_hours == 24
        assert config.block_base_directory_access is True
    
    def test_custom_config(self):
        """Test custom configuration values."""
        config = PathIsolationConfig(
            base_temp_dir="/custom/agentshroud",
            cleanup_on_session_end=False,
            isolated_paths=["/tmp", "/custom/temp"],
            max_abandoned_age_hours=48,
            block_base_directory_access=False
        )
        
        assert config.base_temp_dir == "/custom/agentshroud"
        assert config.cleanup_on_session_end is False
        assert config.isolated_paths == ["/tmp", "/custom/temp"]
        assert config.max_abandoned_age_hours == 48
        assert config.block_base_directory_access is False


class TestPathIsolationManager:
    """Test path isolation manager."""
    
    @pytest.fixture
    def temp_dir(self):
        """Create temporary directory for testing."""
        temp_dir = tempfile.mkdtemp()
        yield temp_dir
        shutil.rmtree(temp_dir, ignore_errors=True)
    
    @pytest.fixture
    def config(self, temp_dir):
        """Create test configuration."""
        return PathIsolationConfig(
            base_temp_dir=os.path.join(temp_dir, "agentshroud"),
            isolated_paths=["/tmp", "/var/tmp"]
        )
    
    @pytest.fixture
    def manager(self, config):
        """Create path isolation manager for testing."""
        return PathIsolationManager(config)
    
    def test_initialization(self, manager, temp_dir):
        """Test manager initialization."""
        assert isinstance(manager.config, PathIsolationConfig)
        assert len(manager._active_users) == 0
        assert len(manager._user_session_times) == 0
        
        # Base directory should be created
        base_dir = os.path.join(temp_dir, "agentshroud")
        assert os.path.exists(base_dir)
    
    def test_user_id_sanitization(self, manager):
        """Test user ID sanitization."""
        # Valid IDs should pass through
        assert manager._sanitize_user_id("user123") == "user123"
        assert manager._sanitize_user_id("test-user_1") == "test-user_1"
        
        # Invalid characters should be removed
        assert manager._sanitize_user_id("user../hack") == "userhack"
        assert manager._sanitize_user_id("../../../etc/passwd") == "etcpasswd"
        
        # Empty or dot-only IDs should be replaced
        sanitized_empty = manager._sanitize_user_id("")
        assert sanitized_empty.startswith("user_")
        
        sanitized_dots = manager._sanitize_user_id("...")
        assert sanitized_dots.startswith("user_")
    
    def test_register_user_session(self, manager, temp_dir):
        """Test user session registration."""
        user_id = "test_user"
        manager.register_user_session(user_id)
        
        # User should be registered
        assert user_id in manager._active_users
        assert user_id in manager._user_session_times
        
        # User directory should be created
        user_dir = os.path.join(temp_dir, "agentshroud", "test_user")
        assert os.path.exists(user_dir)
        
        # Directory should have restrictive permissions
        stat_info = os.stat(user_dir)
        assert oct(stat_info.st_mode)[-3:] == "700"
    
    def test_end_user_session(self, manager, temp_dir):
        """Test ending user session."""
        user_id = "test_user"
        manager.register_user_session(user_id)
        
        # Verify user is registered
        assert user_id in manager._active_users
        user_dir = os.path.join(temp_dir, "agentshroud", "test_user")
        assert os.path.exists(user_dir)
        
        # End session
        manager.end_user_session(user_id)
        
        # User should be removed from active lists
        assert user_id not in manager._active_users
        assert user_id not in manager._user_session_times
        
        # Directory should be cleaned up (if cleanup enabled)
        assert not os.path.exists(user_dir)
    
    def test_path_rewriting_temp_files(self, manager):
        """Test path rewriting for /tmp files."""
        user_id = "test_user"
        manager.register_user_session(user_id)
        
        # Test /tmp path rewriting
        result = manager.rewrite_path("/tmp/test.txt", user_id)
        
        assert result.was_rewritten is True
        assert result.blocked is False
        assert result.original_path == "/tmp/test.txt"
        assert "agentshroud/test_user/test.txt" in result.rewritten_path
    
    def test_path_rewriting_nested_paths(self, manager):
        """Test path rewriting for nested /tmp paths."""
        user_id = "test_user"
        manager.register_user_session(user_id)
        
        # Test nested path
        result = manager.rewrite_path("/tmp/subdir/file.txt", user_id)
        
        assert result.was_rewritten is True
        assert "agentshroud/test_user/subdir/file.txt" in result.rewritten_path
    
    def test_path_rewriting_no_rewrite_needed(self, manager):
        """Test paths that don't need rewriting."""
        user_id = "test_user"
        
        # Test non-isolated path
        result = manager.rewrite_path("/home/user/file.txt", user_id)
        
        assert result.was_rewritten is False
        assert result.blocked is False
        assert result.rewritten_path == "/home/user/file.txt"
    
    def test_block_base_directory_access(self, manager):
        """Test blocking direct access to base agentshroud directory."""
        user_id = "test_user"
        
        result = manager.rewrite_path(manager.config.base_temp_dir, user_id)
        
        assert result.blocked is True
        assert result.was_rewritten is False
        assert "Direct access to AgentShroud base temp directory blocked" in result.reason
    
    def test_block_cross_user_access(self, manager):
        """Test blocking cross-user namespace access."""
        user1 = "user1"
        user2 = "user2"
        
        manager.register_user_session(user1)
        manager.register_user_session(user2)
        
        # User1 tries to access User2's namespace
        user2_path = manager.get_user_temp_path(user2, "secret.txt")
        result = manager.rewrite_path(user2_path, user1)
        
        assert result.blocked is True
        assert "Cross-user access blocked" in result.reason
    
    def test_allow_own_namespace_access(self, manager):
        """Test allowing access to own namespace."""
        user_id = "test_user"
        manager.register_user_session(user_id)
        
        # User accesses their own namespace
        own_path = manager.get_user_temp_path(user_id, "file.txt")
        result = manager.rewrite_path(own_path, user_id)
        
        assert result.blocked is False
        assert result.was_rewritten is False  # Already in correct namespace
    
    def test_already_isolated_paths_not_rewritten(self, manager):
        """Test that already isolated paths are not double-rewritten."""
        user_id = "test_user"
        manager.register_user_session(user_id)
        
        # Path already in manager's namespace (use actual base dir)
        user_dir = manager._get_user_temp_dir(user_id)
        already_isolated = f"{user_dir}/file.txt"
        result = manager.rewrite_path(already_isolated, user_id)
        
        assert result.was_rewritten is False
        assert result.blocked is False
    
    @patch('time.time')
    def test_cleanup_abandoned_directories(self, mock_time, manager, temp_dir):
        """Test cleanup of abandoned user directories."""
        # Set up old directory
        old_user_dir = os.path.join(temp_dir, "agentshroud", "old_user")
        os.makedirs(old_user_dir, exist_ok=True)
        
        # Make directory appear old
        old_time = 1000000000  # Very old timestamp
        current_time = old_time + (manager.config.max_abandoned_age_hours * 3600) + 1
        
        mock_time.return_value = current_time
        
        # Set directory modification time to old time
        os.utime(old_user_dir, (old_time, old_time))
        
        # Run cleanup
        manager.cleanup_abandoned_directories()
        
        # Directory should be removed
        assert not os.path.exists(old_user_dir)
    
    @patch('time.time')
    def test_dont_cleanup_active_user_directories(self, mock_time, manager, temp_dir):
        """Test that active user directories are not cleaned up."""
        user_id = "active_user"
        manager.register_user_session(user_id)
        
        user_dir = manager.get_user_temp_path(user_id)
        
        # Make directory appear old
        old_time = 1000000000
        current_time = old_time + (manager.config.max_abandoned_age_hours * 3600) + 1
        mock_time.return_value = current_time
        
        os.utime(user_dir, (old_time, old_time))
        
        # Run cleanup
        manager.cleanup_abandoned_directories()
        
        # Active user directory should NOT be removed
        assert os.path.exists(user_dir)
    
    def test_get_user_temp_path(self, manager):
        """Test getting user temp path."""
        user_id = "test_user"
        
        # Without relative path
        path = manager.get_user_temp_path(user_id)
        expected = manager._get_user_temp_dir(user_id)
        assert path == expected
        
        # With relative path
        rel_path = "subdir/file.txt"
        path = manager.get_user_temp_path(user_id, rel_path)
        expected = os.path.join(manager._get_user_temp_dir(user_id), rel_path)
        assert path == expected
    
    def test_get_active_users(self, manager):
        """Test getting active users."""
        assert len(manager.get_active_users()) == 0
        
        manager.register_user_session("user1")
        manager.register_user_session("user2")
        
        active_users = manager.get_active_users()
        assert len(active_users) == 2
        assert "user1" in active_users
        assert "user2" in active_users
        
        manager.end_user_session("user1")
        active_users = manager.get_active_users()
        assert len(active_users) == 1
        assert "user2" in active_users
    
    def test_get_stats(self, manager):
        """Test getting statistics."""
        stats = manager.get_stats()
        
        assert "active_users" in stats
        assert "base_temp_dir" in stats
        assert "cleanup_enabled" in stats
        assert "user_session_times" in stats
        
        assert stats["active_users"] == 0
        assert stats["base_temp_dir"] == manager.config.base_temp_dir
        assert stats["cleanup_enabled"] == manager.config.cleanup_on_session_end
        
        # Register a user and check stats update
        manager.register_user_session("test_user")
        updated_stats = manager.get_stats()
        assert updated_stats["active_users"] == 1
        assert "test_user" in updated_stats["user_session_times"]


class TestPathRewriteResult:
    """Test PathRewriteResult dataclass."""
    
    def test_basic_result(self):
        """Test basic result creation."""
        result = PathRewriteResult(
            original_path="/tmp/test.txt",
            rewritten_path="/tmp/agentshroud/user/test.txt",
            was_rewritten=True
        )
        
        assert result.original_path == "/tmp/test.txt"
        assert result.rewritten_path == "/tmp/agentshroud/user/test.txt"
        assert result.was_rewritten is True
        assert result.blocked is False
        assert result.reason == ""
    
    def test_blocked_result(self):
        """Test blocked result creation."""
        result = PathRewriteResult(
            original_path="/tmp/agentshroud/other_user/secret.txt",
            rewritten_path="/tmp/agentshroud/other_user/secret.txt",
            was_rewritten=False,
            blocked=True,
            reason="Cross-user access blocked"
        )
        
        assert result.blocked is True
        assert result.reason == "Cross-user access blocked"


if __name__ == "__main__":
    pytest.main([__file__])