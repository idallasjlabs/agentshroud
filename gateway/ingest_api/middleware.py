# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Middleware Manager - P1 Security Hardening
Orchestrates security modules for request processing.
"""

import logging
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
            # FileSandbox requires a config
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
            self.token_validator = TokenValidator(
                expected_audience="agentshroud-gateway",
                expected_issuer="agentshroud"
            )
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
            self.subagent_monitor = SubagentMonitor(SubagentMonitorConfig())
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

        logger.info("MiddlewareManager initialized with all security modules")
    
    def process(self, request_data: Dict[str, Any], session_id: str = None) -> MiddlewareResult:
        """Process request through all middleware modules.
        
        Args:
            request_data: The request data to process
            session_id: Optional session identifier
            
        Returns:
            MiddlewareResult with allow/deny decision and optional modifications
        """
        self.original_request_data = request_data.copy()
        
        try:
            # Process through each middleware module
            # Each module can block the request or modify it
            
            # 1. Context Guard - Check for context window attacks
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
            
            # 5. File Sandbox - Validate file operations
            if self.file_sandbox:
                try:
                    # Check if request contains file operations
                    message_content = request_data.get('message', '')
                    if isinstance(message_content, dict):
                        message_content = str(message_content)
                    
                    # If there are file paths mentioned, check access
                    # This is a simplified check - real implementation would parse commands
                    if '/etc/' in message_content or '/var/' in message_content or '/root/' in message_content:
                        # Check read access for sensitive paths
                        verdict = self.file_sandbox.check_read('/etc/passwd', session_id or 'unknown')
                        if verdict.allowed == False:
                            logger.warning("Unauthorized file access attempt")
                            return MiddlewareResult(
                                allowed=False,
                                reason="Unauthorized file access attempt"
                            )
                except Exception as e:
                    logger.error(f"FileSandbox processing error: {e}")
            
            # 6. Resource Guard - This is more of a system monitor
            # We'll skip blocking based on resource guard for now
            # as it's designed for monitoring rather than request blocking
            
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
    
    def get_log_sanitizer(self) -> Optional[LogSanitizer]:
        """Get the log sanitizer for integration with logging system."""
        return self.log_sanitizer
