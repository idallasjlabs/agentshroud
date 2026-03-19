# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Session Manager - Per-User Session Isolation

Implements per-user session isolation to prevent data leakage between users.
Each user gets an isolated workspace, memory file, and conversation history.

References:
    - docs/redteam/03-session-isolation.md - Security requirements
"""
from __future__ import annotations

import json
import logging
import os
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Any

logger = logging.getLogger(__name__)


@dataclass 
class ConversationMessage:
    """A single message in a conversation."""
    role: str  # "user" or "assistant"
    content: str
    timestamp: str
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class UserSession:
    """Represents an isolated session for a user."""
    user_id: str
    workspace_dir: Path
    memory_file: Path
    conversation_history: List[ConversationMessage] = field(default_factory=list)
    trust_level: str = "UNTRUSTED"
    created_at: Optional[str] = None
    last_active: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert session to dictionary for serialization."""
        return {
            "user_id": self.user_id,
            "workspace_dir": str(self.workspace_dir),
            "memory_file": str(self.memory_file),
            "conversation_history": [
                {
                    "role": msg.role,
                    "content": msg.content,
                    "timestamp": msg.timestamp,
                    "metadata": msg.metadata
                }
                for msg in self.conversation_history
            ],
            "trust_level": self.trust_level,
            "created_at": self.created_at,
            "last_active": self.last_active,
            "metadata": self.metadata
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "UserSession":
        """Create session from dictionary."""
        history = [
            ConversationMessage(
                role=msg["role"],
                content=msg["content"],
                timestamp=msg["timestamp"],
                metadata=msg.get("metadata", {})
            )
            for msg in data.get("conversation_history", [])
        ]
        
        return cls(
            user_id=data["user_id"],
            workspace_dir=Path(data["workspace_dir"]),
            memory_file=Path(data["memory_file"]),
            conversation_history=history,
            trust_level=data.get("trust_level", "UNTRUSTED"),
            created_at=data.get("created_at"),
            last_active=data.get("last_active"),
            metadata=data.get("metadata", {})
        )


class UserSessionManager:
    """Manages per-user session isolation."""
    
    def __init__(self, base_workspace: Path, owner_user_id: Optional[str] = None):
        """Initialize session manager.
        
        Args:
            base_workspace: Base directory for user workspaces
            owner_user_id: User ID of the owner/admin who can view all sessions
        """
        self.base_workspace = Path(base_workspace)
        self.owner_user_id = owner_user_id
        self.sessions: Dict[str, UserSession] = {}
        self.session_metadata_file = self.base_workspace / "session_registry.json"
        
        # Ensure base directories exist
        self.base_workspace.mkdir(parents=True, exist_ok=True)
        (self.base_workspace / "users").mkdir(exist_ok=True)
        (self.base_workspace / "shared").mkdir(exist_ok=True)
        
        # Load existing sessions
        self._load_sessions()

    def _load_sessions(self):
        """Load existing sessions from metadata file."""
        if self.session_metadata_file.exists():
            try:
                with open(self.session_metadata_file, "r") as f:
                    sessions_data = json.load(f)
                    
                for user_id, session_data in sessions_data.items():
                    self.sessions[user_id] = UserSession.from_dict(session_data)
                    
                logger.info(f"Loaded {len(self.sessions)} user sessions")
            except Exception as e:
                logger.error(f"Failed to load sessions: {e}")

    def _save_sessions(self):
        """Save current sessions to metadata file."""
        try:
            sessions_data = {
                user_id: session.to_dict() 
                for user_id, session in self.sessions.items()
            }
            
            with open(self.session_metadata_file, "w") as f:
                json.dump(sessions_data, f, indent=2)
                
        except Exception as e:
            logger.error(f"Failed to save sessions: {e}")

    @staticmethod
    def _validate_user_id(user_id: str) -> str:
        """Validate and sanitize user_id to prevent path traversal.
        
        Only allows alphanumeric characters, underscores, and hyphens.
        Raises ValueError for invalid user IDs.
        """
        import re
        if not user_id or not re.match(r'^[a-zA-Z0-9_-]+$', user_id):
            raise ValueError(f"Invalid user_id: must be alphanumeric, got {user_id!r}")
        if len(user_id) > 64:
            raise ValueError(f"Invalid user_id: too long ({len(user_id)} chars)")
        return user_id

    def get_or_create_session(self, user_id: str) -> UserSession:
        """Get existing session or create a new one for the user."""
        user_id = self._validate_user_id(user_id)
        if user_id not in self.sessions:
            session_dir = self.base_workspace / "users" / user_id
            # Verify resolved path is within base_workspace (defense in depth)
            resolved = session_dir.resolve()
            base_resolved = self.base_workspace.resolve()
            if not str(resolved).startswith(str(base_resolved)):
                raise ValueError(f"Path traversal detected for user_id: {user_id!r}")
            session_dir.mkdir(parents=True, exist_ok=True)
            
            workspace_dir = session_dir / "workspace"
            memory_file = session_dir / "MEMORY.md"
            logs_dir = session_dir / "logs"
            
            # Create directories
            workspace_dir.mkdir(exist_ok=True)
            logs_dir.mkdir(exist_ok=True)
            
            # Create initial memory file
            if not memory_file.exists():
                memory_content = f"""# Session Memory for User {user_id}

This is your personal memory space. Information stored here is private to your session.

## Created
{datetime.now(timezone.utc).isoformat()}

## Notes
- This memory is isolated from other users
- Your conversations and files are private to your session
- Cross-user data sharing requires explicit consent

"""
                memory_file.write_text(memory_content)
            
            # Create session object
            session = UserSession(
                user_id=user_id,
                workspace_dir=workspace_dir,
                memory_file=memory_file,
                trust_level="UNTRUSTED",
                created_at=datetime.now(timezone.utc).isoformat(),
            )
            
            self.sessions[user_id] = session
            self._save_sessions()
            
            logger.info(f"Created new session for user {user_id}")
            
        # Update last active timestamp
        session = self.sessions[user_id]
        session.last_active = datetime.now(timezone.utc).isoformat()
        
        return session

    def add_conversation_message(
        self, 
        user_id: str, 
        role: str, 
        content: str, 
        metadata: Optional[Dict[str, Any]] = None
    ):
        """Add a message to the user's conversation history."""
        session = self.get_or_create_session(user_id)
        
        message = ConversationMessage(
            role=role,
            content=content,
            timestamp=datetime.now(timezone.utc).isoformat(),
            metadata=metadata or {}
        )
        
        session.conversation_history.append(message)
        
        # Limit conversation history size (keep last 1000 messages)
        if len(session.conversation_history) > 1000:
            session.conversation_history = session.conversation_history[-1000:]
        
        self._save_sessions()

    def get_session_context(self, user_id: str) -> Dict[str, Any]:
        """Get session context for injection into agent request."""
        session = self.get_or_create_session(user_id)
        
        # Read current memory content
        memory_content = ""
        if session.memory_file.exists():
            try:
                memory_content = session.memory_file.read_text()
            except Exception as e:
                logger.error(f"Failed to read memory file for user {user_id}: {e}")
        
        return {
            "user_id": user_id,
            "workspace_path": str(session.workspace_dir),
            "memory_path": str(session.memory_file),
            "memory_content": memory_content,
            "trust_level": session.trust_level,
            "conversation_history": [
                {"role": msg.role, "content": msg.content, "timestamp": msg.timestamp}
                for msg in session.conversation_history[-10:]  # Last 10 messages for context
            ]
        }

    def get_session_prompt_addition(self, user_id: str) -> str:
        """Get session-specific prompt addition for the agent."""
        session = self.get_or_create_session(user_id)
        
        return f"""
SESSION CONTEXT:
You are currently in an isolated session with user {user_id}.
Your workspace is at {session.workspace_dir}
Your memory file is at {session.memory_file}
User trust level: {session.trust_level}

CRITICAL ISOLATION RULES:
- Do NOT access, read, reference, or disclose information from other users' sessions
- Each user's data is confidential to that user only
- If asked about other users' conversations or data, respond: "I cannot access other users' session data"
- Only work within this user's workspace directory: {session.workspace_dir}
- Only read/write this user's memory file: {session.memory_file}
- Cross-user data sharing requires explicit consent mechanism (not yet implemented)

USER SESSION TRUST LEVEL: {session.trust_level}
"""

    def can_user_access_session(self, requesting_user_id: str, target_user_id: str) -> bool:
        """Check if a user can access another user's session."""
        # Owner/admin can access all sessions
        if self.owner_user_id and requesting_user_id == self.owner_user_id:
            return True
        
        # Users can only access their own sessions
        return requesting_user_id == target_user_id

    def list_sessions_for_user(self, requesting_user_id: str) -> List[str]:
        """List sessions that the requesting user is allowed to see."""
        if self.owner_user_id and requesting_user_id == self.owner_user_id:
            # Owner can see all sessions
            return list(self.sessions.keys())
        else:
            # Regular users can only see their own session
            return [requesting_user_id] if requesting_user_id in self.sessions else []

    def get_user_workspace_path(self, user_id: str) -> str:
        """Get the workspace path for a user."""
        session = self.get_or_create_session(user_id)
        return str(session.workspace_dir)

    def update_user_trust_level(self, user_id: str, trust_level: str):
        """Update the trust level for a user."""
        session = self.get_or_create_session(user_id)
        session.trust_level = trust_level
        self._save_sessions()
        logger.info(f"Updated trust level for user {user_id} to {trust_level}")

    def cleanup_old_sessions(self, days_inactive: int = 90):
        """Clean up sessions that haven't been active for the specified number of days."""
        import time
        cutoff_timestamp = time.time() - (days_inactive * 24 * 60 * 60)
        
        sessions_to_remove = []
        for user_id, session in self.sessions.items():
            if session.last_active:
                try:
                    last_active = datetime.fromisoformat(session.last_active.replace("Z", "+00:00"))
                    if last_active.timestamp() < cutoff_timestamp:
                        sessions_to_remove.append(user_id)
                except Exception as e:
                    logger.error(f"Error parsing last_active for user {user_id}: {e}")
        
        for user_id in sessions_to_remove:
            logger.info(f"Cleaning up inactive session for user {user_id}")
            del self.sessions[user_id]
            
        if sessions_to_remove:
            self._save_sessions()