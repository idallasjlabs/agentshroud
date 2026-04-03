# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Middleware Manager - P1 Security Hardening
Orchestrates security modules for request processing.
Now includes per-user session isolation enforcement.
"""

import logging
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

from gateway.security.agent_isolation import AgentRegistry
from gateway.security.alert_dispatcher import AlertDispatcher
from gateway.security.approval_hardening import (
    ApprovalHardening,
    ApprovalHardeningConfig,
)
from gateway.security.audit_export import AuditExportConfig, AuditExporter
from gateway.security.browser_security import BrowserSecurityGuard
from gateway.security.consent_framework import ConsentFramework
from gateway.security.context_guard import ContextGuard
from gateway.security.credential_injector import (
    CredentialInjector,
    CredentialInjectorConfig,
)
from gateway.security.dns_filter import DNSFilter, DNSFilterConfig
from gateway.security.drift_detector import DriftDetector
from gateway.security.egress_monitor import EgressMonitor, EgressMonitorConfig
from gateway.security.env_guard import EnvironmentGuard
from gateway.security.file_sandbox import FileSandbox, FileSandboxConfig
from gateway.security.git_guard import GitGuard
from gateway.security.input_normalizer import normalize_input
from gateway.security.key_rotation import KeyRotationManager
from gateway.security.killswitch_monitor import KillSwitchMonitor
from gateway.security.log_sanitizer import LogSanitizer
from gateway.security.memory_config import MemorySecurityConfig
from gateway.security.memory_integrity import MemoryIntegrityMonitor
from gateway.security.memory_lifecycle import MemoryLifecycleManager
from gateway.security.metadata_guard import MetadataGuard
from gateway.security.multi_turn_tracker import MultiTurnTracker
from gateway.security.network_validator import NetworkValidator
from gateway.security.oauth_security import OAuthSecurityValidator
from gateway.security.output_canary import OutputCanary
from gateway.security.path_isolation import PathIsolationConfig, PathIsolationManager
from gateway.security.rbac import Action, RBACManager, Resource, ToolTier
from gateway.security.rbac_config import RBACConfig
from gateway.security.resource_guard import ResourceGuard
from gateway.security.session_manager import UserSessionManager
from gateway.security.session_security import SessionManager
from gateway.security.subagent_monitor import SubagentMonitor, SubagentMonitorConfig
from gateway.security.token_validation import TokenValidator
from gateway.security.tool_chain_analyzer import ToolChainAnalyzer
from gateway.security.tool_result_injection import ToolResultInjectionScanner
from gateway.security.tool_result_sanitizer import (
    ToolResultPIIConfig,
    ToolResultSanitizer,
)
from gateway.security.tool_result_sanitizer_enhanced import (
    ToolResultSanitizer as EnhancedToolResultSanitizer,
)
from gateway.security.tool_result_sanitizer_enhanced import (
    ToolResultSanitizerConfig as EnhancedSanitizerConfig,
)
from gateway.security.xml_leak_filter import XMLLeakFilter

logger = logging.getLogger(__name__)


@dataclass
class MiddlewareResult:
    """Result from middleware processing."""

    allowed: bool
    reason: Optional[str] = None
    modified_request: Optional[Dict[str, Any]] = None


# Owner detection: delegates to RBAC config (single source of truth).
# Middleware resolves owner status dynamically — no hardcoded user IDs here.
# See gateway/security/rbac_config.py for owner_user_id configuration.


class MiddlewareManager:
    """Manages the P1 security middleware modules."""

    def __init__(self):
        """Initialize all security modules."""
        self.original_request_data = None  # Track original request
        # Resolved from the default BotConfig in set_config(); kept as fallback here.
        self.bot_workspace_path: str = "/home/node/.openclaw/workspace"

        # Initialize RBAC system
        try:
            self.rbac_config = RBACConfig()
            self.rbac_manager = RBACManager(self.rbac_config)
            logger.info("RBAC system initialized")
        except Exception as e:
            logger.error(f"Failed to initialize RBAC system: {e}")
            self.rbac_manager = None
        # Initialize session manager for per-user isolation
        try:
            base_workspace = Path("/tmp/agentshroud/workspace")
            base_workspace.mkdir(parents=True, exist_ok=True)
            from gateway.security.rbac_config import RBACConfig as _RBACConfig

            owner_user_id = _RBACConfig().owner_user_id
            self.user_session_manager = UserSessionManager(
                base_workspace=base_workspace, owner_user_id=owner_user_id
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
            self.token_validator = TokenValidator(
                expected_audience="agentshroud-gateway", expected_issuer="agentshroud"
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
            config = SubagentMonitorConfig()
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
        # Memory Security Components
        try:
            base_workspace = Path("/tmp/agentshroud/workspace")
            base_workspace.mkdir(parents=True, exist_ok=True)
            self.memory_config = MemorySecurityConfig.from_env()
            self.memory_config.base_directory = base_workspace
            self.memory_integrity_monitor = MemoryIntegrityMonitor(
                self.memory_config.integrity, base_workspace
            )
            self.memory_lifecycle_manager = MemoryLifecycleManager(
                self.memory_config.lifecycle, base_workspace
            )
            logger.info("Memory security components initialized")
        except Exception as e:
            logger.error(f"Failed to initialize memory security: {e}")
            self.memory_config = None
            self.memory_integrity_monitor = None
            self.memory_lifecycle_manager = None
        # Tool result injection scanner
        try:
            self.tool_injection_scanner = ToolResultInjectionScanner()
            logger.info("ToolResultInjectionScanner initialized")
        except Exception as e:
            logger.error(f"Failed to initialize ToolResultInjectionScanner: {e}")
            self.tool_injection_scanner = None

        # XML leak filter
        try:
            self.xml_leak_filter = XMLLeakFilter()
            logger.info("XMLLeakFilter initialized")
        except Exception as e:
            logger.error(f"Failed to initialize XMLLeakFilter: {e}")
            self.xml_leak_filter = None

        # === NEWLY WIRED MODULES (v0.8.0) ===

        # Alert Dispatcher
        try:
            self.alert_dispatcher = AlertDispatcher(
                alert_log=Path("/tmp/agentshroud/alerts/security.log")
            )
            logger.info("AlertDispatcher initialized")
        except Exception as e:
            logger.error(f"Failed to initialize AlertDispatcher: {e}")
            self.alert_dispatcher = None

        # Approval Hardening
        try:
            self.approval_hardening = ApprovalHardening(ApprovalHardeningConfig())
            logger.info("ApprovalHardening initialized")
        except Exception as e:
            logger.error(f"Failed to initialize ApprovalHardening: {e}")
            self.approval_hardening = None

        # Browser Security Guard
        try:
            self.browser_security = BrowserSecurityGuard()
            logger.info("BrowserSecurityGuard initialized")
        except Exception as e:
            logger.error(f"Failed to initialize BrowserSecurityGuard: {e}")
            self.browser_security = None

        # Credential Injector
        try:
            self.credential_injector = CredentialInjector()
            logger.info("CredentialInjector initialized")
        except Exception as e:
            logger.error(f"Failed to initialize CredentialInjector: {e}")
            self.credential_injector = None

        # DNS Filter
        try:
            self.dns_filter = DNSFilter(DNSFilterConfig())
            logger.info("DNSFilter initialized")
        except Exception as e:
            logger.error(f"Failed to initialize DNSFilter: {e}")
            self.dns_filter = None

        # Drift Detector
        try:
            self.drift_detector = DriftDetector()
            logger.info("DriftDetector initialized")
        except Exception as e:
            logger.error(f"Failed to initialize DriftDetector: {e}")
            self.drift_detector = None

        # Egress Monitor
        try:
            self.egress_monitor = EgressMonitor(EgressMonitorConfig())
            logger.info("EgressMonitor initialized")
        except Exception as e:
            logger.error(f"Failed to initialize EgressMonitor: {e}")
            self.egress_monitor = None

        # Key Rotation Manager
        try:
            self.key_rotation = KeyRotationManager()
            logger.info("KeyRotationManager initialized")
        except Exception as e:
            logger.error(f"Failed to initialize KeyRotationManager: {e}")
            self.key_rotation = None

        # Kill Switch Monitor
        try:
            self.killswitch_monitor = KillSwitchMonitor()
            logger.info("KillSwitchMonitor initialized")
        except Exception as e:
            logger.error(f"Failed to initialize KillSwitchMonitor: {e}")
            self.killswitch_monitor = None

        # Multi-Turn Tracker
        try:
            self.multi_turn_tracker = MultiTurnTracker()
            logger.info("MultiTurnTracker initialized")
        except Exception as e:
            logger.error(f"Failed to initialize MultiTurnTracker: {e}")
            self.multi_turn_tracker = None

        # Network Validator
        try:
            self.network_validator = NetworkValidator()
            logger.info("NetworkValidator initialized")
        except Exception as e:
            logger.error(f"Failed to initialize NetworkValidator: {e}")
            self.network_validator = None

        # OAuth Security Validator
        try:
            self.oauth_security = OAuthSecurityValidator(
                allowed_redirect_uris=["https://agentshroud.ai/callback"]
            )
            logger.info("OAuthSecurityValidator initialized")
        except Exception as e:
            logger.error(f"Failed to initialize OAuthSecurityValidator: {e}")
            self.oauth_security = None

        # Output Canary
        try:
            self.output_canary = OutputCanary()
            logger.info("OutputCanary initialized")
        except Exception as e:
            logger.error(f"Failed to initialize OutputCanary: {e}")
            self.output_canary = None

        # Path Isolation Manager
        try:
            self.path_isolation = PathIsolationManager(PathIsolationConfig())
            logger.info("PathIsolationManager initialized")
        except Exception as e:
            logger.error(f"Failed to initialize PathIsolationManager: {e}")
            self.path_isolation = None

        # Tool Chain Analyzer
        try:
            self.tool_chain_analyzer = ToolChainAnalyzer()
            logger.info("ToolChainAnalyzer initialized")
        except Exception as e:
            logger.error(f"Failed to initialize ToolChainAnalyzer: {e}")
            self.tool_chain_analyzer = None

        # Enhanced Tool Result Sanitizer
        try:
            self.enhanced_tool_sanitizer = EnhancedToolResultSanitizer(EnhancedSanitizerConfig())
            logger.info("EnhancedToolResultSanitizer initialized")
        except Exception as e:
            logger.error(f"Failed to initialize EnhancedToolResultSanitizer: {e}")
            self.enhanced_tool_sanitizer = None

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
                return MiddlewareResult(allowed=False, reason="No user identification found")

            # RBAC Check - Check basic permissions first
            rbac_result = self._check_rbac_permissions(request_data, user_id)
            if not rbac_result.allowed:
                return rbac_result

            # Session Isolation Enforcement - This is the new critical security check
            isolation_result = self._enforce_session_isolation(request_data, user_id)
            if not isolation_result.allowed:
                return isolation_result

            # Apply session isolation modifications to the request
            if isolation_result.modified_request:
                request_data = isolation_result.modified_request

            # Memory Security - Validate memory file operations
            message = request_data.get("message", "")
            if isinstance(message, dict):
                message = str(message)
            message = normalize_input(message)
            if message != request_data.get("message", ""):
                request_data["message"] = message

            # Register expected writes to memory files to prevent false integrity alerts
            if self.memory_integrity_monitor and (
                "write" in message.lower() or "edit" in message.lower()
            ):
                import re

                memory_patterns = [
                    r"(?:write|edit).*?(?:MEMORY\.md|memory/.*\.md|HEARTBEAT\.md|TOOLS\.md)",
                ]
                for pattern in memory_patterns:
                    if re.search(pattern, message, re.IGNORECASE):
                        # Extract file path and register expected write
                        path_match = re.search(r"(?:write|edit)\s+(\S+\\.md)", message)
                        if path_match:
                            self.memory_integrity_monitor.register_expected_write(
                                path_match.group(1)
                            )
                            logger.debug(f"Registered expected write for {path_match.group(1)}")

            # 0.8. Multi-Turn Tracker — cumulative cross-turn disclosure risk
            if self.multi_turn_tracker:
                try:
                    # Owner exemption: track but never block the owner
                    from gateway.security.rbac_config import RBACConfig

                    _is_owner = RBACConfig().is_owner(user_id)

                    message_content_mt = request_data.get("message", "")
                    if isinstance(message_content_mt, dict):
                        message_content_mt = str(message_content_mt)
                    mt_session_id = session_id or user_id or "unknown"
                    mt_ctx = self.multi_turn_tracker.track_message(
                        mt_session_id, message_content_mt
                    )
                    if mt_ctx.blocked:
                        if _is_owner:
                            logger.info(
                                f"MultiTurnTracker: owner session {mt_session_id} would be blocked "
                                f"(score={mt_ctx.total_score:.2f}) - EXEMPTED"
                            )
                        else:
                            logger.warning(
                                f"MultiTurnTracker blocked session {mt_session_id}: "
                                f"score={mt_ctx.total_score:.2f}, events={len(mt_ctx.events)}"
                            )
                            return MiddlewareResult(
                                allowed=False,
                                reason="Multi-turn disclosure risk threshold exceeded",
                            )
                except Exception as e:
                    logger.error(f"MultiTurnTracker error: {e}")
                    return MiddlewareResult(
                        allowed=False, reason=f"MultiTurnTracker error: {str(e)}"
                    )

            # 0.9. Tool Chain Analyzer — block suspicious tool call sequences (tool calls only)
            if self.tool_chain_analyzer and self._is_tool_call_request(request_data):
                try:
                    tc_session_id = session_id or user_id or "unknown"
                    for tc in request_data.get("tool_calls", []):
                        tool_name = tc.get("name", "unknown")
                        tool_params = tc.get("input", {})
                        call_id = tc.get("id", "")
                        allow, chain_match = self.tool_chain_analyzer.analyze_tool_call(
                            tc_session_id, tool_name, tool_params, call_id
                        )
                        if not allow:
                            reason = (
                                f"Suspicious tool chain detected: {chain_match.chain_name}"
                                if chain_match
                                else "Suspicious tool chain detected"
                            )
                            logger.warning(
                                f"ToolChainAnalyzer blocked {tool_name} for user {user_id}: {reason}"
                            )
                            return MiddlewareResult(allowed=False, reason=reason)
                except Exception as e:
                    logger.error(f"ToolChainAnalyzer error: {e}")
                    return MiddlewareResult(
                        allowed=False, reason=f"ToolChainAnalyzer error: {str(e)}"
                    )

            # 1. Context Guard - Check for prompt injection and manipulation
            if self.context_guard and self._is_owner(user_id):
                logger.info(f"ContextGuard bypassed for owner user {user_id}")
            elif self.context_guard:
                try:
                    message_content = request_data.get("message", "")
                    if isinstance(message_content, dict):
                        message_content = str(message_content)

                    attacks = self.context_guard.analyze_message(
                        session_id or "unknown", message_content
                    )
                    if attacks:
                        for attack in attacks:
                            # repetition_attack fires on legitimate structured output (nc output,
                            # status checks, etc.) — log it but never block on it.
                            # Only block on instruction_injection, which is the real threat.
                            if attack.attack_type == "repetition_attack":
                                logger.info(
                                    f"Context repetition noted (not blocking): {attack.description}"
                                )
                                continue
                            if attack.severity in ["critical", "high"]:
                                logger.warning(f"Context attack detected: {attack.description}")
                                return MiddlewareResult(
                                    allowed=False,
                                    reason=f"Context attack detected: {attack.attack_type}",
                                )
                except Exception as e:
                    logger.error(f"ContextGuard processing error: {e}")
                    return MiddlewareResult(allowed=False, reason=f"ContextGuard error: {str(e)}")

            # 2. Metadata Guard - Sanitize headers and metadata
            if self.metadata_guard:
                try:
                    headers = request_data.get("headers", {})
                    if headers:
                        sanitized_headers = self.metadata_guard.sanitize_headers(headers)
                        if sanitized_headers != headers:
                            # Modify the request data with sanitized headers
                            request_data = request_data.copy()
                            request_data["headers"] = sanitized_headers
                except Exception as e:
                    logger.error(f"MetadataGuard processing error: {e}")

            # 3. Environment Guard - Check for environment variable access
            # Only run env_guard if content looks like a shell command.
            # Raw Telegram chat messages (natural language questions) should
            # never be treated as command execution attempts.
            _COMMAND_INDICATORS = (
                "/proc/",
                "printenv",
                "$ENV{",
                "${",
                "$(",
                "`",
                "| grep",
                "| awk",
                "| sed",
                ">/dev/",
            )

            if self.env_guard:
                try:
                    message_content = request_data.get("message", "")
                    if isinstance(message_content, dict):
                        message_content = str(message_content)

                    if any(indicator in message_content for indicator in _COMMAND_INDICATORS):
                        if not self.env_guard.check_command_execution(
                            message_content, session_id or "unknown"
                        ):
                            logger.warning("Unauthorized command execution detected")
                            return MiddlewareResult(
                                allowed=False, reason="Unauthorized command execution detected"
                            )
                except Exception as e:
                    logger.error(f"EnvGuard processing error: {e}")
                    return MiddlewareResult(allowed=False, reason=f"EnvGuard error: {str(e)}")

            # 3.5. Browser Security Guard — social engineering detection
            if self.browser_security:
                try:
                    bs_message = request_data.get("message", "")
                    if isinstance(bs_message, dict):
                        bs_message = str(bs_message)
                    assessment = self.browser_security.analyze_content(bs_message)
                    # ThreatLevel enum: NONE=0, LOW=1, MEDIUM=2, HIGH=3, CRITICAL=4
                    if assessment.threat_level.value >= 3:  # HIGH or CRITICAL
                        logger.warning(
                            f"BrowserSecurityGuard: {assessment.threat_level.name} threat for user {user_id}: "
                            f"{assessment.threats}"
                        )
                        return MiddlewareResult(
                            allowed=False,
                            reason=f"Browser security threat detected: {', '.join(assessment.threats)}",
                        )
                except Exception as e:
                    logger.error(f"BrowserSecurityGuard error: {e}")
                    return MiddlewareResult(
                        allowed=False, reason=f"BrowserSecurityGuard error: {str(e)}"
                    )

            # 4. Git Guard - Scan message content for malicious git/supply-chain patterns
            if self.git_guard and self._is_owner(user_id):
                logger.info(f"GitGuard bypassed for owner user {user_id}")
            elif self.git_guard:
                try:
                    message_content = request_data.get("message", "")
                    if isinstance(message_content, dict):
                        message_content = str(message_content)
                    findings = self.git_guard.scan_content(message_content)
                    for finding in findings:
                        if finding.threat_level.value in ("critical", "high"):
                            logger.warning(
                                f"GitGuard blocked {finding.threat_level.value} finding "
                                f"for user {user_id}: {finding.description}"
                            )
                            return MiddlewareResult(
                                allowed=False,
                                reason=f"GitGuard: {finding.description}",
                            )
                except Exception as e:
                    logger.error(f"GitGuard processing error: {e}")
                    return MiddlewareResult(allowed=False, reason=f"GitGuard error: {str(e)}")

            # 5. File Sandbox - Validate file operations (now session-aware).
            # ONLY runs for actual tool calls — plain chat messages that mention
            # file-like words (e.g. "check config.yaml") must NOT be blocked.
            if self._is_owner(user_id):
                logger.debug(f"FileSandbox bypassed for owner user {user_id}")
            elif (
                self.file_sandbox
                and self.user_session_manager
                and self._is_tool_call_request(request_data)
            ):
                try:
                    # Check if request contains file operations
                    message_content = request_data.get("message", "")
                    if isinstance(message_content, dict):
                        message_content = str(message_content)

                    # Extract file paths from message
                    file_paths = self._extract_file_paths(message_content)

                    # Also extract paths from tool_calls inputs
                    for tc in request_data.get("tool_calls", []):
                        tc_input = tc.get("input", {})
                        for v in tc_input.values():
                            if isinstance(v, str) and ("/" in v or "\\" in v):
                                file_paths.append(v)

                    # Check if user is trying to access files outside their workspace
                    user_workspace = self.user_session_manager.get_user_workspace_path(user_id)

                    for file_path in file_paths:
                        if not self._is_path_allowed_for_user(file_path, user_workspace, user_id):
                            if user_id == self.user_session_manager.owner_user_id:
                                logger.info(
                                    f"Owner {user_id} accessed path outside workspace (audited): {file_path}"
                                )
                            else:
                                logger.warning(
                                    f"User {user_id} attempted to access unauthorized path: {file_path}"
                                )
                                return MiddlewareResult(
                                    allowed=False,
                                    reason=f"Unauthorized file access: {file_path} - cannot access other users' data",
                                )

                except Exception as e:
                    logger.error(f"FileSandbox processing error: {e}")
                    return MiddlewareResult(allowed=False, reason=f"FileSandbox error: {str(e)}")

            # 5.5. Path Isolation Manager — enforce per-user path isolation for tool calls
            if self.path_isolation and self._is_tool_call_request(request_data):
                try:
                    for tc in request_data.get("tool_calls", []):
                        tc_input = tc.get("input", {})
                        for v in tc_input.values():
                            if isinstance(v, str) and ("/" in v or "\\" in v):
                                rewrite = self.path_isolation.rewrite_path(v, user_id)
                                if rewrite.blocked:
                                    logger.warning(
                                        f"PathIsolationManager blocked path {v} for user {user_id}: "
                                        f"{rewrite.reason}"
                                    )
                                    return MiddlewareResult(
                                        allowed=False,
                                        reason=f"Path isolation violation: {rewrite.reason}",
                                    )
                except Exception as e:
                    logger.error(f"PathIsolationManager error: {e}")
                    return MiddlewareResult(
                        allowed=False, reason=f"PathIsolationManager error: {str(e)}"
                    )

            # 6. Session Send Security - Check for cross-session messaging attempts
            cross_session_result = self._check_cross_session_access(request_data, user_id)
            if not cross_session_result.allowed:
                return cross_session_result

            # All checks passed
            modified_request = request_data if request_data != self.original_request_data else None
            return MiddlewareResult(allowed=True, modified_request=modified_request)

        except Exception as e:
            logger.error(f"Middleware processing error: {e}")
            # Fail closed - deny on error
            return MiddlewareResult(allowed=False, reason=f"Middleware processing error: {str(e)}")

    def _check_rbac_permissions(
        self, request_data: Dict[str, Any], user_id: str
    ) -> MiddlewareResult:
        """Check RBAC permissions for the request."""
        if not self.rbac_manager:
            logger.warning("RBAC manager not available - proceeding without RBAC")
            return MiddlewareResult(allowed=True)

        try:
            message_content = request_data.get("message", "")
            if isinstance(message_content, dict):
                message_content = str(message_content)

            # Determine what the user is trying to do
            action, resource, tool_tier = self._analyze_request_for_rbac(
                message_content, request_data
            )

            # Check basic permission
            if action and resource:
                context = {"tool_tier": tool_tier} if tool_tier else None
                permission = self.rbac_manager.check_permission(user_id, action, resource, context)

                if not permission.allowed:
                    if permission.requires_approval:
                        logger.info(f"User {user_id} action requires approval: {permission.reason}")
                        return MiddlewareResult(
                            allowed=False, reason=f"Action requires approval: {permission.reason}"
                        )
                    else:
                        logger.warning(f"RBAC denied user {user_id}: {permission.reason}")
                        return MiddlewareResult(
                            allowed=False, reason=f"Access denied: {permission.reason}"
                        )

            # Check tool tier permissions specifically
            if tool_tier:
                tool_permission = self.rbac_manager.check_tool_permission(user_id, tool_tier)
                if not tool_permission.allowed:
                    if tool_permission.requires_approval:
                        logger.info(
                            f"User {user_id} tool usage requires approval: {tool_permission.reason}"
                        )
                        return MiddlewareResult(
                            allowed=False,
                            reason=f"Tool usage requires approval: {tool_permission.reason}",
                        )
                    else:
                        logger.warning(
                            f"RBAC denied tool usage for user {user_id}: {tool_permission.reason}"
                        )
                        return MiddlewareResult(
                            allowed=False, reason=f"Tool access denied: {tool_permission.reason}"
                        )

            # Log successful RBAC check for auditing
            user_role = self.rbac_manager.get_user_role(user_id)
            logger.debug(f"RBAC check passed for user {user_id} (role: {user_role.value})")

            return MiddlewareResult(allowed=True)

        except Exception as e:
            logger.error(f"RBAC check error: {e}")
            return MiddlewareResult(allowed=False, reason=f"RBAC check error: {str(e)}")

    def _analyze_request_for_rbac(
        self, message_content: str, request_data: Dict[str, Any]
    ) -> Tuple[Optional[Action], Optional[Resource], Optional[ToolTier]]:
        """Analyze request to determine RBAC action, resource, and tool tier."""
        message_lower = message_content.lower()

        # Determine action based on message content
        action = None
        resource = None
        tool_tier = None

        # Check for file operations — use word boundaries to avoid substring false positives
        # (e.g. "rm" inside "terms", "perform", "information")
        file_patterns = [
            r"\b(?:read|cat|view|open|ls|dir)\b",
            r"\b(?:write|edit|create|save|modify)\b",
            r"\b(?:delete|remove|rm|trash)\b",
            r"\b(?:execute|run|exec)\b",
        ]

        if any(re.search(pattern, message_lower) for pattern in file_patterns[:1]):
            action = Action.READ
            resource = Resource.FILES
        elif any(re.search(pattern, message_lower) for pattern in file_patterns[1:2]):
            action = Action.WRITE
            resource = Resource.FILES
        elif any(re.search(pattern, message_lower) for pattern in file_patterns[2:3]):
            action = Action.DELETE
            resource = Resource.FILES
        elif any(re.search(pattern, message_lower) for pattern in file_patterns[3:4]):
            action = Action.EXECUTE
            resource = Resource.TOOLS

        # Determine tool tier based on operation type
        critical_tools = ["ssh", "sudo", "rm -rf", "format", "delete database", "drop table"]
        high_tools = ["git push", "deploy", "install", "update system", "network config"]
        medium_tools = ["exec", "run", "command", "script"]
        low_tools = ["read", "list", "show", "get", "fetch"]

        if any(tool in message_lower for tool in critical_tools):
            tool_tier = ToolTier.CRITICAL
        elif any(tool in message_lower for tool in high_tools):
            tool_tier = ToolTier.HIGH
        elif any(tool in message_lower for tool in medium_tools):
            tool_tier = ToolTier.MEDIUM
        elif any(tool in message_lower for tool in low_tools):
            tool_tier = ToolTier.LOW

        # If we couldn't determine the action from content, default based on common patterns
        if not action:
            if "?" in message_content or any(
                word in message_lower for word in ["what", "how", "show", "list"]
            ):
                action = Action.READ
                resource = Resource.SYSTEM
                tool_tier = ToolTier.LOW
            else:
                action = Action.TOOL_USE
                resource = Resource.TOOLS
                tool_tier = ToolTier.MEDIUM  # Default to medium for unknown operations

        return action, resource, tool_tier

    def get_rbac_manager(self) -> Optional[RBACManager]:
        """Get the RBAC manager for external access."""
        return self.rbac_manager

    def get_multi_turn_tracker(self):
        return self.multi_turn_tracker

    def get_output_canary(self):
        return self.output_canary

    def get_tool_chain_analyzer(self):
        return self.tool_chain_analyzer

    def get_dns_filter(self):
        return self.dns_filter

    def get_alert_dispatcher(self):
        return self.alert_dispatcher

    def get_killswitch_monitor(self):
        return self.killswitch_monitor

    def get_drift_detector(self):
        return self.drift_detector

    def get_network_validator(self):
        return self.network_validator

    def get_enhanced_tool_sanitizer(self):
        return self.enhanced_tool_sanitizer

    def _extract_user_id(self, request_data: Dict[str, Any]) -> Optional[str]:
        """Extract user ID from request data."""
        # Check session context first
        session_context = request_data.get("session_context", {})
        if session_context and "user_id" in session_context:
            return session_context["user_id"]

        # Check metadata
        metadata = request_data.get("metadata", {})
        if metadata and "user_id" in metadata:
            return metadata["user_id"]

        # Check direct user_id field
        if "user_id" in request_data:
            return request_data["user_id"]

        return None

    def _enforce_session_isolation(
        self, request_data: Dict[str, Any], user_id: str
    ) -> MiddlewareResult:
        """Enforce per-user session isolation rules."""
        if not self.user_session_manager:
            logger.error("UserSessionManager not initialized - session isolation fail-closed")
            return MiddlewareResult(
                allowed=False, reason="Session isolation unavailable - request denied"
            )

        try:
            # Ensure user session exists
            session = self.user_session_manager.get_or_create_session(user_id)

            # Inject session context into request if not already present
            if "session_context" not in request_data:
                session_context = self.user_session_manager.get_session_context(user_id)
                session_prompt = self.user_session_manager.get_session_prompt_addition(user_id)

                modified_request = request_data.copy()
                modified_request["session_context"] = session_context
                modified_request["session_context"]["isolation_prompt"] = session_prompt

                logger.info(f"Injected session context for user {user_id}")

                return MiddlewareResult(allowed=True, modified_request=modified_request)

            return MiddlewareResult(allowed=True)

        except Exception as e:
            logger.error(f"Session isolation enforcement error: {e}")
            return MiddlewareResult(allowed=False, reason=f"Session isolation error: {str(e)}")

    def _is_owner(self, user_id: str) -> bool:
        """Check if user_id is the system owner via RBAC config (single source of truth)."""
        if hasattr(self, "rbac_manager") and self.rbac_manager:
            return self.rbac_manager.config.is_owner(user_id)
        # Fallback: check RBACConfig defaults if no manager is initialized yet
        from gateway.security.rbac_config import RBACConfig

        return RBACConfig().is_owner(user_id)

    def _extract_file_paths(self, message: str) -> list[str]:
        """Extract potential file paths from message content."""
        # More comprehensive file path patterns
        patterns = [
            r"/[a-zA-Z0-9_./\-]+",  # Unix-style absolute paths
            r"[a-zA-Z0-9_./\-]+/[a-zA-Z0-9_./\-]+",  # Relative paths with slashes
            # Only match files with explicit path prefix (./  ../  ~/) to avoid
            # false positives on bare words like "config.yaml" in conversation.
            r"(?:\.{1,2}/|~/)[a-zA-Z0-9_./\-]+\.(?:txt|md|py|js|json|yaml|yml|conf|cfg|log|csv|xml)",
        ]

        paths = []
        for pattern in patterns:
            matches = re.findall(pattern, message)
            paths.extend(matches)

        # Also look for common file operation commands
        file_commands = [
            r"(?:read|write|open|cat|ls|dir|rm|delete|mv|move|cp|copy)\s+([^\s]+)",
            r"(?:edit|vim|nano|emacs)\s+([^\s]+)",
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

        # Owner bypass — owner identity has access to all paths
        if (
            self.user_session_manager.owner_user_id
            and user_id == self.user_session_manager.owner_user_id
        ):
            return True

        try:
            # Convert to absolute paths for comparison
            file_path_abs = str(Path(file_path).resolve())
            user_workspace_abs = str(Path(user_workspace).resolve())

            # Normalize macOS /private prefix
            for prefix in ["/private"]:
                if file_path_abs.startswith(prefix) and not user_workspace_abs.startswith(prefix):
                    file_path_abs = file_path_abs[len(prefix) :]
                elif user_workspace_abs.startswith(prefix) and not file_path_abs.startswith(prefix):
                    user_workspace_abs = user_workspace_abs[len(prefix) :]

            # Allow access to user's own workspace
            if file_path_abs.startswith(user_workspace_abs):
                return True

            # Allow access to shared resources (read-only)
            shared_path = str(Path(self.bot_workspace_path + "/shared").resolve())
            if file_path_abs.startswith(shared_path):
                return True

            # Allow access to common system paths (read-only)
            allowed_system_paths = ["/tmp", "/proc/meminfo", "/proc/cpuinfo", "/etc/os-release"]

            for allowed_path in allowed_system_paths:
                try:
                    allowed_path_abs = str(Path(allowed_path).resolve())
                    if file_path_abs.startswith(allowed_path_abs):
                        return True
                except Exception:
                    continue

            # Explicitly check and deny access to other users' workspaces
            _users_dir = self.bot_workspace_path + "/users"
            users_base = (
                str(Path(_users_dir).resolve()) if Path(_users_dir).exists() else "/workspace/users"
            )
            if file_path_abs.startswith(users_base) and not file_path_abs.startswith(
                user_workspace_abs
            ):
                logger.warning(f"User {user_id} attempted cross-session access to: {file_path}")
                return False

            # For temporary directories in tests, check if it's another user's directory
            if "/users/" in file_path_abs:
                # Extract the user part from the path
                parts = file_path_abs.split("/users/")
                if len(parts) > 1:
                    other_user_part = parts[1].split("/")[0]  # Get the user ID part
                    if other_user_part != user_id:
                        logger.warning(
                            f"User {user_id} attempted cross-session access to user {other_user_part}: {file_path}"
                        )
                        return False

            # Default deny — paths not explicitly allowed are blocked
            return False

        except Exception as e:
            logger.error(f"Error checking path permissions for {file_path}: {e}")
            # Fail secure - deny access on error
            return False

    def _check_cross_session_access(
        self, request_data: Dict[str, Any], user_id: str
    ) -> MiddlewareResult:
        """Check for unauthorized cross-session access attempts.

        **Implementation note:** This is a lightweight string-based heuristic.
        It scans the serialised ``message`` field of the request payload for
        regex patterns that resemble cross-session commands (e.g. ``session_send``,
        ``send to session``, ``access user <id>``).  It does *not* parse or
        execute the message — it only checks whether the text matches known
        command patterns.

        False-positive risk: legitimate messages that coincidentally contain
        phrases like "access user settings" may trigger the pattern.  The
        owner is always allowed through; non-owner requests are blocked with an
        explanation.  If a false positive is reported, tighten the regex or add
        an allowlist of safe phrases here.
        """
        message_content = request_data.get("message", "")
        if isinstance(message_content, dict):
            message_content = str(message_content)

        # Check for sessions_send or similar cross-session commands
        cross_session_patterns = [
            r"sessions?_send",
            r"send.*to.*session",
            r"message.*other.*user",
            r"access.*user.*\d+",
        ]

        for pattern in cross_session_patterns:
            if re.search(pattern, message_content, re.IGNORECASE):
                if self.user_session_manager:
                    # Check if user is owner/admin
                    if (
                        self.user_session_manager.owner_user_id
                        and user_id == self.user_session_manager.owner_user_id
                    ):
                        logger.info(f"Owner {user_id} attempting cross-session access - allowed")
                        return MiddlewareResult(allowed=True)

                logger.warning(f"User {user_id} attempted cross-session access")
                return MiddlewareResult(
                    allowed=False,
                    reason="Cross-session access denied - use approval queue for inter-user communication",
                )

        return MiddlewareResult(allowed=True)

    def _is_tool_call_request(self, request_data: Dict[str, Any]) -> bool:
        """Return True only when the request contains actual tool calls or tool results.

        Plain chat messages that happen to mention file-like words (e.g. "check
        config.yaml") must NOT trigger file-path extraction and sandbox checks.
        Only requests that carry tool_calls / tool_results keys with non-empty
        lists, or whose ``type`` field is ``"tool_call"``, are considered tool
        operations.
        """
        if request_data.get("type") == "tool_call":
            return True
        if request_data.get("tool_calls"):  # non-empty list
            return True
        if request_data.get("tool_results"):  # non-empty list
            return True
        return False

    def scan_tool_result(self, tool_name: str, result_content: str) -> Optional[str]:
        """
        Scan tool result for injection attempts and return sanitized content.

        Args:
            tool_name: Name of the tool that produced the result
            result_content: The content returned by the tool

        Returns:
            Sanitized content, or None if result should be blocked entirely
        """
        if not self.tool_injection_scanner:
            logger.warning(
                "ToolResultInjectionScanner not available - tool result passed through unsanitized"
            )
            return result_content

        try:
            scan_result = self.tool_injection_scanner.scan_tool_result(tool_name, result_content)

            # Log the scan result
            if scan_result.patterns:
                logger.warning(
                    f"Tool result injection detected in {tool_name}: "
                    f"severity={scan_result.severity.value}, "
                    f"action={scan_result.action.value}, "
                    f"patterns={scan_result.patterns}"
                )

            # Handle based on severity
            if scan_result.action.value == "strip":
                # HIGH severity - content filtered
                logger.error(
                    f"HIGH severity injection detected in {tool_name} result - content filtered. "
                    f"Patterns: {scan_result.patterns}"
                )
                return scan_result.sanitized_content

            elif scan_result.action.value == "warn":
                # MEDIUM severity - warning added
                logger.warning(
                    f"MEDIUM severity injection detected in {tool_name} result - warning added. "
                    f"Patterns: {scan_result.patterns}"
                )
                return scan_result.sanitized_content

            else:
                # LOW severity - log only
                if scan_result.patterns:
                    logger.info(
                        f"LOW severity patterns detected in {tool_name} result: {scan_result.patterns}"
                    )
                return result_content

        except Exception as e:
            logger.error(f"Error scanning tool result from {tool_name}: {e}")
            # Fail open for tool results to avoid breaking functionality
            return result_content

    def filter_outbound_response(self, response_content: str) -> str:
        """
        Filter outbound response to remove sensitive XML and path information.

        Args:
            response_content: The response content to filter

        Returns:
            Filtered response content
        """
        if not self.xml_leak_filter:
            logger.warning("XMLLeakFilter not available - response passed through unfiltered")
            return response_content

        try:
            filter_result = self.xml_leak_filter.filter_response(response_content)

            if filter_result.filter_applied:
                logger.info(
                    f"XML/path information filtered from response. "
                    f"Removed: {len(filter_result.removed_items)} items"
                )
                logger.debug(f"Filtered items: {filter_result.removed_items}")

            return filter_result.filtered_content

        except Exception as e:
            logger.error(f"Error filtering outbound response: {e}")
            # Fail open to avoid breaking responses
            return response_content

    def get_log_sanitizer(self) -> Optional[LogSanitizer]:
        """Get the log sanitizer for integration with logging system."""
        return self.log_sanitizer

    def set_config(self, config):
        """Set configuration and initialize tool result sanitizer"""
        # Resolve workspace path from the default bot config.
        try:
            bots = getattr(config, "bots", {})
            default_bot = next(
                (b for b in bots.values() if b.default),
                next(iter(bots.values()), None),
            )
            if default_bot:
                self.bot_workspace_path = default_bot.workspace_path
        except Exception:
            pass  # Keep fallback value set in __init__

        try:
            from .config import PIIConfig

            tool_result_config_dict = getattr(config, "tool_result_pii", {})
            if tool_result_config_dict:
                # Create default PIIConfig from the general PII config
                default_config = getattr(config, "pii", PIIConfig())

                # Create ToolResultPIIConfig
                tool_config = ToolResultPIIConfig(
                    enabled=tool_result_config_dict.get("enabled", True),
                    default_config=default_config,
                    tool_overrides=tool_result_config_dict.get("tool_overrides", {}),
                )

                self.tool_result_sanitizer = ToolResultSanitizer(tool_config)
                logger.info("Tool result PII sanitizer configured successfully")
            else:
                logger.warning("No tool_result_pii configuration found")
        except Exception as e:
            logger.error(f"Failed to configure tool result sanitizer: {e}")
            self.tool_result_sanitizer = None

    async def process_tool_result(
        self, tool_name: str, tool_result: Any, session_id: Optional[str] = None
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
            logger.warning(
                "Tool result sanitizer not configured - allowing result through unsanitized"
            )
            return tool_result, False

        try:
            sanitized_result, redaction_result = (
                await self.tool_result_sanitizer.sanitize_tool_result(
                    tool_name=tool_name, tool_result=tool_result, session_id=session_id
                )
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

    async def close(self) -> None:
        """Shutdown middleware background tasks cleanly."""
        try:
            if self.resource_guard:
                await self.resource_guard.stop()
        except Exception as exc:
            logger.warning("MiddlewareManager.close(): ResourceGuard stop failed: %s", exc)
