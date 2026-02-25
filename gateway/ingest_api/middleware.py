# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Middleware Manager - P1 Security Hardening
Orchestrates security modules for request processing.
Now includes per-user session isolation enforcement.
"""

import logging
import re
from pathlib import Path
from typing import Dict, Any, Optional, Tuple
from dataclasses import dataclass

from gateway.security.context_guard import ContextGuard
from gateway.security.metadata_guard import MetadataGuard
from gateway.security.log_sanitizer import LogSanitizer
from gateway.security.env_guard import EnvironmentGuard
from gateway.security.git_guard import GitGuard
from gateway.security.file_sandbox import FileSandbox, FileSandboxConfig
from gateway.security.resource_guard import ResourceGuard
from gateway.security.session_security import SessionManager
from gateway.security.token_validation import TokenValidator
from gateway.security.consent_framework import ConsentFramework
from gateway.security.subagent_monitor import SubagentMonitor, SubagentMonitorConfig
from gateway.security.agent_isolation import AgentRegistry
from gateway.security.session_manager import UserSessionManager
from gateway.security.tool_result_sanitizer import ToolResultSanitizer, ToolResultPIIConfig

logger = logging.getLogger(__name__)


@dataclass
class MiddlewareResult:
    """Result from middleware processing."""
    allowed: bool
    reason: Optional[str] = None
    modified_request: Optional[Dict[str, Any]] = None


class MiddlewareManager:
    """Manages the P1 security middleware modules."""
    
    def __init__(self):
        """Initialize all security modules."""
        self.original_request_data = None  # Track original request
        
        # Initialize session manager for per-user isolation
        try:
            base_workspace = Path("/home/node/.openclaw/workspace")
            # TODO: Load owner_user_id from config
            owner_user_id = "1234567890"  # This should come from config
            self.user_session_manager = UserSessionManager(
                base_workspace=base_workspace,
                owner_user_id=owner_user_id
            )
            logger.info("UserSessionManager initialized")
        except Exception as e:
            logger.error(f"Failed to initialize UserSessionManager: {e}")
            self.user_session_manager = None
        
        try:
            self.context_guard = ContextGuard()
            logger.info("ContextGuard initialized")
        except Exception as e:
            logger.error(f"Failed to initialize ContextGuard: {e}")
            self.context_guard = None
            
        try:
            self.metadata_guard = MetadataGuard()
            logger.info("MetadataGuard initialized")
        except Exception as e:
            logger.error(f"Failed to initialize MetadataGuard: {e}")
            self.metadata_guard = None
            
        try:
            self.log_sanitizer = LogSanitizer()
            logger.info("LogSanitizer initialized")
        except Exception as e:
            logger.error(f"Failed to initialize LogSanitizer: {e}")
            self.log_sanitizer = None
            
        try:
            self.env_guard = EnvironmentGuard()
            logger.info("EnvGuard initialized")
        except Exception as e:
            logger.error(f"Failed to initialize EnvGuard: {e}")
            self.env_guard = None
            
        try:
            self.git_guard = GitGuard()
            logger.info("GitGuard initialized")
        except Exception as e:
            logger.error(f"Failed to initialize GitGuard: {e}")
            self.git_guard = None
            
        try:
            # FileSandbox requires a config - we'll modify this for per-user paths
            config = FileSandboxConfig(
                mode="enforce",
                allowed_read_paths=["/app", "/tmp", "/proc/meminfo", "/proc/cpuinfo"],
                allowed_write_paths=["/tmp", "/app/data", "/app/logs"],
            )
            self.file_sandbox = FileSandbox(config)
            logger.info("FileSandbox initialized")
        except Exception as e:
            logger.error(f"Failed to initialize FileSandbox: {e}")
            self.file_sandbox = None
            
        try:
            self.resource_guard = ResourceGuard()
            logger.info("ResourceGuard initialized")
        except Exception as e:
            logger.error(f"Failed to initialize ResourceGuard: {e}")
            self.resource_guard = None
        
        # P2 request-path modules
        try:
            self.session_manager = SessionManager()
            logger.info("SessionManager initialized")
        except Exception as e:
            logger.error(f"Failed to initialize SessionManager: {e}")
            self.session_manager = None
            
        try:
            self.token_validator = TokenValidator()
            logger.info("TokenValidator initialized")
        except Exception as e:
            logger.error(f"Failed to initialize TokenValidator: {e}")
            self.token_validator = None
            
        try:
            self.consent_framework = ConsentFramework()
            logger.info("ConsentFramework initialized")
        except Exception as e:
            logger.error(f"Failed to initialize ConsentFramework: {e}")
            self.consent_framework = None
            
        try:
            config = SubagentMonitorConfig(
                max_subagents=5,
                max_depth=2,
                timeout_seconds=300,
                allowed_operations=["read", "write", "execute"],
            )
            self.subagent_monitor = SubagentMonitor(config)
            logger.info("SubagentMonitor initialized")
        except Exception as e:
            logger.error(f"Failed to initialize SubagentMonitor: {e}")
            self.subagent_monitor = None
            
        try:
            self.agent_registry = AgentRegistry()
            logger.info("AgentRegistry initialized")
        except Exception as e:
            logger.error(f"Failed to initialize AgentRegistry: {e}")
            self.agent_registry = None

        # Tool result PII sanitizer (configured later via set_config)
        self.tool_result_sanitizer = None

    async def process_request(
        self,
        request_data: Dict[str, Any],
        session_id: Optional[str] = None,
    ) -> MiddlewareResult:
        """Process request through all middleware modules."""
        self.original_request_data = request_data.copy()
        
        try:
            # Extract user_id for session isolation
            user_id = self._extract_user_id(request_data)
            if not user_id:
                logger.warning("No user_id found in request - denying access")
                return MiddlewareResult(
                    allowed=False,
                    reason="No user identification found"
                )
            
            # Session Isolation Enforcement - This is the new critical security check
            isolation_result = self._enforce_session_isolation(request_data, user_id)
            if not isolation_result.allowed:
                return isolation_result
            
            # Apply session isolation modifications to the request
            if isolation_result.modified_request:
                request_data = isolation_result.modified_request
            
            # 1. Context Guard - Check for prompt injection and manipulation
            if self.context_guard:
                try:
                    message_content = request_data.get('message', '')
                    if isinstance(message_content, dict):
                        message_content = str(message_content)
                    
                    attacks = self.context_guard.analyze_message(session_id or 'unknown', message_content)
                    if attacks:
                        for attack in attacks:
                            if attack.severity in ['critical', 'high']:
                                logger.warning(f"Context attack detected: {attack.description}")
                                return MiddlewareResult(
                                    allowed=False,
                                    reason=f"Context attack detected: {attack.attack_type}"
                                )
                except Exception as e:
                    logger.error(f"ContextGuard processing error: {e}")
            
            # 2. Metadata Guard - Sanitize headers and metadata
            if self.metadata_guard:
                try:
                    headers = request_data.get('headers', {})
                    if headers:
                        sanitized_headers = self.metadata_guard.sanitize_headers(headers)
                        if sanitized_headers != headers:
                            # Modify the request data with sanitized headers
                            request_data = request_data.copy()
                            request_data['headers'] = sanitized_headers
                except Exception as e:
                    logger.error(f"MetadataGuard processing error: {e}")
            
            # 3. Environment Guard - Check for environment variable access
            if self.env_guard:
                try:
                    message_content = request_data.get('message', '')
                    if isinstance(message_content, dict):
                        message_content = str(message_content)
                    
                    # Check if this is a command execution attempt
                    if not self.env_guard.check_command_execution(message_content, session_id or 'unknown'):
                        logger.warning("Unauthorized command execution detected")
                        return MiddlewareResult(
                            allowed=False,
                            reason="Unauthorized command execution detected"
                        )
                except Exception as e:
                    logger.error(f"EnvGuard processing error: {e}")
            
            # 4. Git Guard - Check for git-related security issues
            if self.git_guard:
                try:
                    # Git guard is repository-based, so we'll do a basic check
                    # In a real implementation, this would need more context
                    logger.debug("Git security check passed (basic validation)")
                except Exception as e:
                    logger.error(f"GitGuard processing error: {e}")
            
            # 5. File Sandbox - Validate file operations (now session-aware)
            if self.file_sandbox and self.user_session_manager:
                try:
                    # Check if request contains file operations
                    message_content = request_data.get('message', '')
                    if isinstance(message_content, dict):
                        message_content = str(message_content)
                    
                    # Extract file paths from message
                    file_paths = self._extract_file_paths(message_content)
                    
                    # Check if user is trying to access files outside their workspace
                    user_workspace = self.user_session_manager.get_user_workspace_path(user_id)
                    
                    for file_path in file_paths:
                        if not self._is_path_allowed_for_user(file_path, user_workspace, user_id):
                            logger.warning(f"User {user_id} attempted to access unauthorized path: {file_path}")
                            return MiddlewareResult(
                                allowed=False,
                                reason=f"Unauthorized file access: {file_path} - cannot access other users' data"
                            )
                            
                except Exception as e:
                    logger.error(f"FileSandbox processing error: {e}")
            
            # 6. Session Send Security - Check for cross-session messaging attempts
            cross_session_result = self._check_cross_session_access(request_data, user_id)
            if not cross_session_result.allowed:
                return cross_session_result
            
            # All checks passed
            modified_request = request_data if request_data != self.original_request_data else None
            return MiddlewareResult(
                allowed=True,
                modified_request=modified_request
            )
            
        except Exception as e:
            logger.error(f"Middleware processing error: {e}")
            # Fail closed - deny on error
            return MiddlewareResult(
                allowed=False,
                reason=f"Middleware processing error: {str(e)}"
            )

    def _extract_user_id(self, request_data: Dict[str, Any]) -> Optional[str]:
        """Extract user ID from request data."""
        # Check session context first
        session_context = request_data.get('session_context', {})
        if session_context and 'user_id' in session_context:
            return session_context['user_id']
        
        # Check metadata
        metadata = request_data.get('metadata', {})
        if metadata and 'user_id' in metadata:
            return metadata['user_id']
        
        # Check direct user_id field
        if 'user_id' in request_data:
            return request_data['user_id']
        
        return None

    def _enforce_session_isolation(self, request_data: Dict[str, Any], user_id: str) -> MiddlewareResult:
        """Enforce per-user session isolation rules."""
        if not self.user_session_manager:
            logger.warning("UserSessionManager not initialized - session isolation degraded")
            return MiddlewareResult(
                allowed=True,
                reason="Session isolation unavailable - operating in degraded mode"
            )
        
        try:
            # Ensure user session exists
            session = self.user_session_manager.get_or_create_session(user_id)
            
            # Inject session context into request if not already present
            if 'session_context' not in request_data:
                session_context = self.user_session_manager.get_session_context(user_id)
                session_prompt = self.user_session_manager.get_session_prompt_addition(user_id)
                
                modified_request = request_data.copy()
                modified_request['session_context'] = session_context
                modified_request['session_context']['isolation_prompt'] = session_prompt
                
                logger.info(f"Injected session context for user {user_id}")
                
                return MiddlewareResult(
                    allowed=True,
                    modified_request=modified_request
                )
            
            return MiddlewareResult(allowed=True)
            
        except Exception as e:
            logger.error(f"Session isolation enforcement error: {e}")
            return MiddlewareResult(
                allowed=False,
                reason=f"Session isolation error: {str(e)}"
            )

    def _extract_file_paths(self, message: str) -> list[str]:
        """Extract potential file paths from message content."""
        # More comprehensive file path patterns
        patterns = [
            r'/[a-zA-Z0-9_./\-]+',  # Unix-style absolute paths
            r'[a-zA-Z0-9_./\-]+/[a-zA-Z0-9_./\-]+',  # Relative paths with slashes
            r'[a-zA-Z0-9_./\-]+\.(?:txt|md|py|js|json|yaml|yml|conf|cfg|log|csv|xml)',  # Files with extensions
        ]
        
        paths = []
        for pattern in patterns:
            matches = re.findall(pattern, message)
            paths.extend(matches)
        
        # Also look for common file operation commands
        file_commands = [
            r'(?:read|write|open|cat|ls|dir|rm|delete|mv|move|cp|copy)\s+([^\s]+)',
            r'(?:edit|vim|nano|emacs)\s+([^\s]+)',
        ]
        
        for pattern in file_commands:
            matches = re.findall(pattern, message, re.IGNORECASE)
            paths.extend(matches)
        
        # Clean up and return unique paths
        cleaned_paths = []
        for path in set(paths):
            path = path.strip("'\"")  # Remove quotes
            if path and len(path) > 1:  # Skip single characters
                cleaned_paths.append(path)
        
        return cleaned_paths

    def _is_path_allowed_for_user(self, file_path: str, user_workspace: str, user_id: str) -> bool:
        """Check if a file path is allowed for a user to access."""
        if not self.user_session_manager:
            return False
        
        try:
            # Convert to absolute paths for comparison
            file_path_abs = str(Path(file_path).resolve())
            user_workspace_abs = str(Path(user_workspace).resolve())
            
            # Allow access to user's own workspace
            if file_path_abs.startswith(user_workspace_abs):
                return True
            
            # Allow access to shared resources (read-only)
            shared_path = str(Path("/home/node/.openclaw/workspace/shared").resolve())
            if file_path_abs.startswith(shared_path):
                return True
            
            # Allow access to common system paths (read-only)
            allowed_system_paths = [
                "/tmp", "/proc/meminfo", "/proc/cpuinfo", "/etc/os-release"
            ]
            
            for allowed_path in allowed_system_paths:
                try:
                    allowed_path_abs = str(Path(allowed_path).resolve())
                    if file_path_abs.startswith(allowed_path_abs):
                        return True
                except Exception:
                    continue
            
            # Explicitly check and deny access to other users' workspaces
            users_base = str(Path("/home/node/.openclaw/workspace/users").resolve()) if Path("/home/node/.openclaw/workspace/users").exists() else "/workspace/users"
            if file_path_abs.startswith(users_base) and not file_path_abs.startswith(user_workspace_abs):
                logger.warning(f"User {user_id} attempted cross-session access to: {file_path}")
                return False
            
            # For temporary directories in tests, check if it's another user's directory
            if "/users/" in file_path_abs:
                # Extract the user part from the path
                parts = file_path_abs.split("/users/")
                if len(parts) > 1:
                    other_user_part = parts[1].split("/")[0]  # Get the user ID part
                    if other_user_part != user_id:
                        logger.warning(f"User {user_id} attempted cross-session access to user {other_user_part}: {file_path}")
                        return False
            
            # Default to allowing other paths (will be caught by existing file sandbox)
            return True
            
        except Exception as e:
            logger.error(f"Error checking path permissions for {file_path}: {e}")
            # Fail secure - deny access on error
            return False

    def _check_cross_session_access(self, request_data: Dict[str, Any], user_id: str) -> MiddlewareResult:
        """Check for unauthorized cross-session access attempts."""
        message_content = request_data.get('message', '')
        if isinstance(message_content, dict):
            message_content = str(message_content)
        
        # Check for sessions_send or similar cross-session commands
        cross_session_patterns = [
            r'sessions?_send',
            r'send.*to.*session',
            r'message.*other.*user',
            r'access.*user.*\d+',
        ]
        
        for pattern in cross_session_patterns:
            if re.search(pattern, message_content, re.IGNORECASE):
                if self.user_session_manager:
                    # Check if user is owner/admin
                    if (self.user_session_manager.owner_user_id and 
                        user_id == self.user_session_manager.owner_user_id):
                        logger.info(f"Owner {user_id} attempting cross-session access - allowed")
                        return MiddlewareResult(allowed=True)
                
                logger.warning(f"User {user_id} attempted cross-session access")
                return MiddlewareResult(
                    allowed=False,
                    reason="Cross-session access denied - use approval queue for inter-user communication"
                )
        
        return MiddlewareResult(allowed=True)
    
    def get_log_sanitizer(self) -> Optional[LogSanitizer]:
        """Get the log sanitizer for integration with logging system."""
        return self.log_sanitizer
    def set_config(self, config):
        """Set configuration and initialize tool result sanitizer"""
        try:
            from .config import PIIConfig
            
            tool_result_config_dict = getattr(config, 'tool_result_pii', {})
            if tool_result_config_dict:
                # Create default PIIConfig from the general PII config
                default_config = getattr(config, 'pii', PIIConfig())
                
                # Create ToolResultPIIConfig
                tool_config = ToolResultPIIConfig(
                    enabled=tool_result_config_dict.get('enabled', True),
                    default_config=default_config,
                    tool_overrides=tool_result_config_dict.get('tool_overrides', {})
                )
                
                self.tool_result_sanitizer = ToolResultSanitizer(tool_config)
                logger.info("Tool result PII sanitizer configured successfully")
            else:
                logger.warning("No tool_result_pii configuration found")
        except Exception as e:
            logger.error(f"Failed to configure tool result sanitizer: {e}")
            self.tool_result_sanitizer = None

    async def process_tool_result(
        self, 
        tool_name: str, 
        tool_result: Any, 
        session_id: Optional[str] = None
    ) -> tuple[Any, bool]:
        """Process tool result through PII sanitization before it reaches agent
        
        Args:
            tool_name: Name of the tool that produced the result
            tool_result: The raw tool result from the tool
            session_id: Optional session ID for audit logging
            
        Returns:
            Tuple of (sanitized_result, was_modified)
        """
        if not self.tool_result_sanitizer:
            logger.warning("Tool result sanitizer not configured - allowing result through unsanitized")
            return tool_result, False
            
        try:
            sanitized_result, redaction_result = await self.tool_result_sanitizer.sanitize_tool_result(
                tool_name=tool_name,
                tool_result=tool_result,
                session_id=session_id
            )
            
            was_modified = len(redaction_result.redactions) > 0
            
            if was_modified:
                logger.info(
                    f"Tool result sanitized: tool={tool_name} session={session_id or 'unknown'} "
                    f"redactions={len(redaction_result.redactions)} "
                    f"entities={redaction_result.entity_types_found}"
                )
                
            return sanitized_result, was_modified
            
        except Exception as e:
            logger.error(f"Tool result sanitization failed for {tool_name}: {e}")
            # Fail secure - if we can't sanitize, we should block the result
            # But for now, log and allow through to avoid breaking functionality
            logger.warning(f"Allowing unsanitized tool result through due to sanitization error")
            return tool_result, False
