# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.

"""
Path Isolation Manager — Prevent cross-session data leakage via shared filesystem paths.

Provides per-user namespacing for temporary directories and intercepts file operations
to rewrite paths to isolated user-specific locations. Prevents users from accessing
each other's temporary files and data.
"""

import logging
import os
import shutil
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Optional, Set

logger = logging.getLogger(__name__)


@dataclass
class PathIsolationConfig:
    """Configuration for path isolation system."""

    # Base directory for user namespaces
    base_temp_dir: str = "/tmp/agentshroud"

    # Whether to clean up user temp dirs on session end
    cleanup_on_session_end: bool = True

    # Paths that should be isolated per user (will be rewritten)
    isolated_paths: list[str] = field(
        default_factory=lambda: [
            "/tmp",
            "/var/tmp",
        ]
    )

    # Maximum age for cleanup of abandoned user directories (hours)
    max_abandoned_age_hours: int = 24

    # Whether to block access to the base temp directory listing
    block_base_directory_access: bool = True


@dataclass
class PathRewriteResult:
    """Result of path rewriting operation."""

    original_path: str
    rewritten_path: str
    was_rewritten: bool
    blocked: bool = False
    reason: str = ""


class PathIsolationManager:
    """Manages per-user path isolation for temporary files and directories."""

    def __init__(self, config: PathIsolationConfig):
        self.config = config
        self._active_users: Set[str] = set()
        self._user_session_times: Dict[str, float] = {}

        # Ensure base directory exists
        self._ensure_base_directory()

    def _ensure_base_directory(self) -> None:
        """Create base agentshroud temp directory if it doesn't exist."""
        try:
            os.makedirs(self.config.base_temp_dir, mode=0o755, exist_ok=True)
            logger.debug(f"Ensured base temp directory exists: {self.config.base_temp_dir}")
        except Exception as e:
            logger.error(f"Failed to create base temp directory {self.config.base_temp_dir}: {e}")

    def register_user_session(self, user_id: str) -> None:
        """Register a new user session and create their isolated directory."""
        self._active_users.add(user_id)
        self._user_session_times[user_id] = time.time()

        user_temp_dir = self._get_user_temp_dir(user_id)
        try:
            os.makedirs(user_temp_dir, mode=0o700, exist_ok=True)
            logger.info(f"Created isolated temp directory for user {user_id}: {user_temp_dir}")
        except Exception as e:
            logger.error(f"Failed to create user temp directory {user_temp_dir}: {e}")

    def end_user_session(self, user_id: str) -> None:
        """End a user session and optionally clean up their isolated directory."""
        if user_id in self._active_users:
            self._active_users.remove(user_id)

        if user_id in self._user_session_times:
            del self._user_session_times[user_id]

        if self.config.cleanup_on_session_end:
            self._cleanup_user_directory(user_id)

    def _get_user_temp_dir(self, user_id: str) -> str:
        """Get the isolated temp directory path for a user."""
        # Sanitize user_id to prevent path traversal
        safe_user_id = self._sanitize_user_id(user_id)
        return os.path.join(self.config.base_temp_dir, safe_user_id)

    def _sanitize_user_id(self, user_id: str) -> str:
        """Sanitize user ID to prevent path traversal attacks."""
        # Remove any path separators and dangerous characters
        sanitized = "".join(c for c in user_id if c.isalnum() or c in "-_")
        # Ensure it's not empty or just dots
        if not sanitized or sanitized.startswith("."):
            sanitized = f"user_{abs(hash(user_id))}"
        return sanitized

    def rewrite_path(self, path: str, user_id: str) -> PathRewriteResult:
        """
        Rewrite a path to isolate it to the user's namespace.

        Args:
            path: Original file path
            user_id: User identifier for isolation

        Returns:
            PathRewriteResult with rewrite information
        """
        original_path = os.path.abspath(path)

        # Check if trying to access the base agentshroud directory directly
        if self._is_base_directory_access(original_path):
            return PathRewriteResult(
                original_path=path,
                rewritten_path=original_path,
                was_rewritten=False,
                blocked=True,
                reason="Direct access to AgentShroud base temp directory blocked",
            )

        # Check if trying to access another user's namespace
        cross_user_access = self._check_cross_user_access(original_path, user_id)
        if cross_user_access:
            return PathRewriteResult(
                original_path=path,
                rewritten_path=original_path,
                was_rewritten=False,
                blocked=True,
                reason=f"Cross-user access blocked: {cross_user_access}",
            )

        # Check if path needs rewriting
        rewritten_path = self._apply_path_rewriting(original_path, user_id)
        was_rewritten = rewritten_path != original_path

        if was_rewritten:
            # Ensure the user's directory exists
            self._ensure_user_directory(user_id)

        return PathRewriteResult(
            original_path=path, rewritten_path=rewritten_path, was_rewritten=was_rewritten
        )

    def _is_base_directory_access(self, path: str) -> bool:
        """Check if path is trying to access the base AgentShroud directory."""
        if not self.config.block_base_directory_access:
            return False

        return os.path.abspath(path) == os.path.abspath(self.config.base_temp_dir)

    def _check_cross_user_access(self, path: str, current_user_id: str) -> Optional[str]:
        """
        Check if path is trying to access another user's isolated namespace.

        Returns:
            None if access is allowed, error message if blocked
        """
        abs_path = os.path.abspath(path)
        base_temp_abs = os.path.abspath(self.config.base_temp_dir)

        # If path is not under agentshroud temp dir, no cross-user concern
        if not abs_path.startswith(base_temp_abs + os.sep):
            return None

        # Extract the user directory being accessed
        relative_path = os.path.relpath(abs_path, base_temp_abs)
        accessed_user_id = relative_path.split(os.sep)[0]
        current_safe_user_id = self._sanitize_user_id(current_user_id)

        # Allow access to own directory
        if accessed_user_id == current_safe_user_id:
            return None

        return f"attempting to access user '{accessed_user_id}' namespace"

    def _apply_path_rewriting(self, path: str, user_id: str) -> str:
        """Apply path rewriting rules to isolate paths per user."""
        abs_path = os.path.abspath(path)

        for isolated_path in self.config.isolated_paths:
            isolated_abs = os.path.abspath(isolated_path)

            # Check if path is under this isolated directory
            if abs_path.startswith(isolated_abs):
                # Calculate relative path from the isolated directory
                try:
                    relative_path = os.path.relpath(abs_path, isolated_abs)
                    # Check if path is already in the user's namespace
                    user_temp_dir = self._get_user_temp_dir(user_id)
                    if abs_path.startswith(user_temp_dir + os.sep) or abs_path == user_temp_dir:
                        return abs_path

                    # Rewrite to user's isolated directory
                    user_temp_dir = self._get_user_temp_dir(user_id)
                    rewritten_path = os.path.join(user_temp_dir, relative_path)
                    return rewritten_path
                except ValueError:
                    # Path is not actually under isolated_path, continue
                    continue

        # No rewriting needed
        return path

    def _ensure_user_directory(self, user_id: str) -> None:
        """Ensure user's isolated directory exists."""
        user_temp_dir = self._get_user_temp_dir(user_id)
        try:
            os.makedirs(user_temp_dir, mode=0o700, exist_ok=True)
        except Exception as e:
            logger.error(f"Failed to create user directory {user_temp_dir}: {e}")

    def _cleanup_user_directory(self, user_id: str) -> None:
        """Clean up a user's isolated directory."""
        user_temp_dir = self._get_user_temp_dir(user_id)
        try:
            if os.path.exists(user_temp_dir):
                shutil.rmtree(user_temp_dir)
                logger.info(f"Cleaned up user temp directory: {user_temp_dir}")
        except Exception as e:
            logger.error(f"Failed to cleanup user temp directory {user_temp_dir}: {e}")

    def cleanup_abandoned_directories(self) -> None:
        """Clean up abandoned user directories based on max age."""
        if not os.path.exists(self.config.base_temp_dir):
            return

        max_age_seconds = self.config.max_abandoned_age_hours * 3600
        current_time = time.time()

        try:
            for user_dir in os.listdir(self.config.base_temp_dir):
                user_path = os.path.join(self.config.base_temp_dir, user_dir)
                if not os.path.isdir(user_path):
                    continue

                # Check if user is still active
                if user_dir in [self._sanitize_user_id(uid) for uid in self._active_users]:
                    continue

                # Check directory age
                try:
                    stat_info = os.stat(user_path)
                    dir_age = current_time - stat_info.st_mtime

                    if dir_age > max_age_seconds:
                        shutil.rmtree(user_path)
                        logger.info(f"Cleaned up abandoned user directory: {user_path}")
                except Exception as e:
                    logger.error(f"Error checking/cleaning directory {user_path}: {e}")

        except Exception as e:
            logger.error(f"Error during abandoned directory cleanup: {e}")

    def get_user_temp_path(self, user_id: str, relative_path: str = "") -> str:
        """Get a path within the user's isolated temp directory."""
        user_temp_dir = self._get_user_temp_dir(user_id)
        if relative_path:
            return os.path.join(user_temp_dir, relative_path)
        return user_temp_dir

    def get_active_users(self) -> Set[str]:
        """Get set of currently active users."""
        return self._active_users.copy()

    def get_stats(self) -> Dict[str, any]:
        """Get statistics about path isolation manager."""
        return {
            "active_users": len(self._active_users),
            "base_temp_dir": self.config.base_temp_dir,
            "cleanup_enabled": self.config.cleanup_on_session_end,
            "user_session_times": self._user_session_times.copy(),
        }
