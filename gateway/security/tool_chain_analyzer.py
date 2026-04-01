# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Tool Chain Analysis for AgentShroud Gateway

Analyzes sequences of tool calls to detect potentially dangerous patterns
that could indicate data exfiltration or security bypass attempts.

This module tracks tool call chains per session and identifies suspicious
patterns like read_file → web_fetch or credential access → outbound tools.
"""
from __future__ import annotations

import logging
import re
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Pattern, Tuple

logger = logging.getLogger("agentshroud.security.tool_chain_analyzer")


# C34: Parameter injection patterns (compiled once at module load)
_PARAM_INJECTION_PATTERNS: list[tuple[re.Pattern, str]] = [
    (re.compile(r'[;&|`$()]{1,}.*(?:rm\b|cat\b|wget\b|curl\b|chmod\b)|(?:^|\s)[;&|`]'), "shell_metacharacter"),
    (re.compile(r"(?:'\s*OR\s*'?1'?\s*=\s*'?1|UNION\s+(?:ALL\s+)?SELECT|DROP\s+TABLE|INSERT\s+INTO\s+\w+\s+VALUES)", re.IGNORECASE), "sql_injection"),
    (re.compile(r'(?:\.\.[\\/]){1,}'), "path_traversal"),
    (re.compile(r'\{\{[^}]*\}\}|\$\{[^}]*\}'), "template_injection"),
]

# C37: Reversibility scores for known tool names (1.0 = fully reversible)
_REVERSIBILITY_MAP: dict[str, float] = {
    "read_file": 1.0, "read": 1.0, "glob": 1.0, "grep": 1.0, "search": 1.0,
    "write_file": 0.7, "write": 0.7, "edit": 0.7, "create_file": 0.7,
    "delete_file": 0.1, "delete": 0.1, "remove": 0.1,
    "execute_command": 0.2, "exec": 0.2, "run": 0.2, "bash": 0.2,
    "send_message": 0.3, "message": 0.3, "tts": 0.3,
    "web_fetch": 0.9, "browser": 0.9, "web_search": 0.95,
    "modify_config": 0.3, "config_write": 0.3, "gateway_config": 0.3,
    "admin_action": 0.1, "kill_session": 0.1,
}


class RiskLevel(str, Enum):
    """Risk levels for tool call chains."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ChainAction(str, Enum):
    """Actions to take on suspicious chains."""
    ALLOW = "allow"
    WARN = "warn" 
    BLOCK = "block"
    REQUIRE_APPROVAL = "require_approval"


# C34: Parameter scan result
@dataclass
class ParamScanResult:
    """Result of scanning tool parameters for injection patterns."""
    safe: bool
    violations: List[str]
    sanitized_params: Dict[str, Any]


# C37: Reversibility score for a tool call
@dataclass
class ReversibilityScore:
    """How reversible an action is (1.0 = fully reversible, 0.0 = irreversible)."""
    score: float
    tool_name: str
    action: str
    reasoning: str


@dataclass
class ToolCall:
    """Represents a single tool call."""
    tool_name: str
    parameters: Dict[str, Any]
    timestamp: float
    session_id: str
    call_id: str = ""
    

@dataclass
class ChainPattern:
    """Definition of a suspicious tool call pattern."""
    name: str
    source_pattern: Pattern[str]
    sink_pattern: Pattern[str]
    risk_level: RiskLevel
    action: ChainAction
    description: str
    max_chain_length: int = 10
    max_time_window: float = 300.0  # 5 minutes


@dataclass
class ChainMatch:
    """A detected suspicious chain."""
    pattern: ChainPattern
    source_calls: List[ToolCall]
    sink_calls: List[ToolCall]
    risk_score: float
    detected_at: float
    session_id: str


@dataclass
class SessionChainContext:
    """Tool call chain context for a session."""
    session_id: str
    tool_calls: List[ToolCall] = field(default_factory=list)
    detected_chains: List[ChainMatch] = field(default_factory=list)
    blocked_calls: int = 0
    approval_required_calls: int = 0
    last_activity: float = field(default_factory=time.time)


class ToolChainAnalyzer:
    """Main tool chain analysis engine.
    
    Tracks sequences of tool calls and identifies potentially dangerous
    patterns that could indicate data exfiltration or security bypasses.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initialize the tool chain analyzer.
        
        Args:
            config: Configuration dictionary with chain patterns and settings
        """
        self.config = config or {}
        self.enabled = self.config.get("enabled", True)
        self.max_session_duration = self.config.get("max_session_duration", 3600.0)
        
        # Session storage
        self.sessions: Dict[str, SessionChainContext] = {}
        
        # Load built-in patterns
        self._load_default_patterns()
        
        # Load custom patterns from config
        self._load_custom_patterns()
        
        # Alert callbacks
        self.alert_callbacks: List[callable] = []
        
    def _load_default_patterns(self) -> None:
        """Load default suspicious chain patterns."""
        
        self.patterns: List[ChainPattern] = [
            # Credential access to outbound (check first - most specific)
            ChainPattern(
                name="credential_to_outbound",
                source_pattern=re.compile(r'\bread.*(/run/secrets|/etc/passwd|credential|secret|key)', re.IGNORECASE),
                sink_pattern=re.compile(r'\b(web_fetch|browser|message|tts)\b', re.IGNORECASE),
                risk_level=RiskLevel.CRITICAL,
                action=ChainAction.BLOCK,
                description="Credential access followed by outbound communication",
                max_chain_length=2,
                max_time_window=30.0
            ),
            
            # Configuration file access chains
            ChainPattern(
                name="config_file_to_outbound",
                source_pattern=re.compile(r'\bread.*(config|env|\.yaml|\.json|\.conf)', re.IGNORECASE),
                sink_pattern=re.compile(r'\b(web_fetch|browser|message)\b', re.IGNORECASE),
                risk_level=RiskLevel.HIGH,
                action=ChainAction.REQUIRE_APPROVAL,
                description="Configuration file access followed by outbound communication",
                max_chain_length=2,
                max_time_window=45.0
            ),
            
            # Exec to network
            ChainPattern(
                name="exec_to_network",
                source_pattern=re.compile(r'\bexec\b', re.IGNORECASE),
                sink_pattern=re.compile(r'\b(web_fetch|browser|message)\b', re.IGNORECASE),
                risk_level=RiskLevel.HIGH,
                action=ChainAction.REQUIRE_APPROVAL,
                description="Command execution followed by network communication",
                max_chain_length=3,
                max_time_window=60.0
            ),
            
            # Data exfiltration via messaging (check before HTTP to prioritize message blocking)
            ChainPattern(
                name="read_to_message_exfil",
                source_pattern=re.compile(r'\bread\b', re.IGNORECASE),
                sink_pattern=re.compile(r'\bmessage\b', re.IGNORECASE),
                risk_level=RiskLevel.CRITICAL,
                action=ChainAction.REQUIRE_APPROVAL,
                description="File read followed by message sending",
                max_chain_length=3,
                max_time_window=60.0
            ),
            
            # Data exfiltration via HTTP (more general, check later)
            ChainPattern(
                name="read_to_http_exfil",
                source_pattern=re.compile(r'\bread\b', re.IGNORECASE),
                sink_pattern=re.compile(r'\b(web_fetch|browser)\b', re.IGNORECASE),
                risk_level=RiskLevel.HIGH,
                action=ChainAction.REQUIRE_APPROVAL,
                description="File read followed by HTTP outbound tool",
                max_chain_length=5,
                max_time_window=120.0
            ),
            
            # Rapid file enumeration
            ChainPattern(
                name="rapid_file_enumeration",
                source_pattern=re.compile(r'\bread\b', re.IGNORECASE),
                sink_pattern=re.compile(r'\bread\b', re.IGNORECASE),
                risk_level=RiskLevel.MEDIUM,
                action=ChainAction.WARN,
                description="Rapid succession of file read operations",
                max_chain_length=8,
                max_time_window=30.0
            ),
            
            # Exec to network
            ChainPattern(
                name="exec_to_network",
                source_pattern=re.compile(r'\bexec\b', re.IGNORECASE),
                sink_pattern=re.compile(r'\b(web_fetch|browser|message)\b', re.IGNORECASE),
                risk_level=RiskLevel.HIGH,
                action=ChainAction.REQUIRE_APPROVAL,
                description="Command execution followed by network communication",
                max_chain_length=3,
                max_time_window=60.0
            ),
            
            # Configuration file access chains
            ChainPattern(
                name="config_file_to_outbound",
                source_pattern=re.compile(r'\bread.*(config|env|secret|key)', re.IGNORECASE),
                sink_pattern=re.compile(r'\b(web_fetch|browser|message)\b', re.IGNORECASE),
                risk_level=RiskLevel.HIGH,
                action=ChainAction.REQUIRE_APPROVAL,
                description="Configuration file access followed by outbound communication",
                max_chain_length=2,
                max_time_window=45.0
            )
        ]
        
        logger.info(f"Loaded {len(self.patterns)} default chain patterns")
        
    def _load_custom_patterns(self) -> None:
        """Load custom patterns from configuration."""
        custom_patterns = self.config.get("custom_patterns", [])
        
        for pattern_config in custom_patterns:
            try:
                pattern = ChainPattern(
                    name=pattern_config["name"],
                    source_pattern=re.compile(pattern_config["source_pattern"], re.IGNORECASE),
                    sink_pattern=re.compile(pattern_config["sink_pattern"], re.IGNORECASE),
                    risk_level=RiskLevel(pattern_config.get("risk_level", "medium")),
                    action=ChainAction(pattern_config.get("action", "warn")),
                    description=pattern_config.get("description", ""),
                    max_chain_length=pattern_config.get("max_chain_length", 10),
                    max_time_window=pattern_config.get("max_time_window", 300.0)
                )
                self.patterns.append(pattern)
            except Exception as e:
                logger.error(f"Failed to load custom pattern {pattern_config.get('name')}: {e}")
                
        logger.info(f"Total patterns loaded: {len(self.patterns)}")
        
    def analyze_tool_call(
        self, 
        session_id: str, 
        tool_name: str, 
        parameters: Dict[str, Any],
        call_id: str = ""
    ) -> Tuple[bool, Optional[ChainMatch]]:
        """Analyze a tool call for suspicious chain patterns.
        
        Args:
            session_id: Session identifier
            tool_name: Name of the tool being called
            parameters: Tool parameters
            call_id: Unique identifier for this call
            
        Returns:
            Tuple of (should_allow, detected_chain_match)
        """
        if not self.enabled:
            return True, None
            
        # Get or create session context
        if session_id not in self.sessions:
            self.sessions[session_id] = SessionChainContext(session_id=session_id)
            
        session = self.sessions[session_id]
        session.last_activity = time.time()
        
        # Create tool call record
        tool_call = ToolCall(
            tool_name=tool_name,
            parameters=parameters,
            timestamp=time.time(),
            session_id=session_id,
            call_id=call_id
        )
        
        # Add to session history
        session.tool_calls.append(tool_call)
        
        # Clean up old sessions periodically
        self._cleanup_old_sessions()
        
        # Analyze for chain patterns
        chain_match = self._detect_chain_patterns(session, tool_call)
        
        if chain_match:
            session.detected_chains.append(chain_match)
            self._trigger_alert(chain_match)
            
            # Determine action
            if chain_match.pattern.action == ChainAction.BLOCK:
                session.blocked_calls += 1
                logger.error(f"BLOCKING tool call {tool_name} in session {session_id} due to pattern: {chain_match.pattern.name}")
                return False, chain_match
                
            elif chain_match.pattern.action == ChainAction.REQUIRE_APPROVAL:
                session.approval_required_calls += 1
                logger.warning(f"APPROVAL REQUIRED for tool call {tool_name} in session {session_id} due to pattern: {chain_match.pattern.name}")
                # Note: This requires external approval system integration
                return False, chain_match
                
            elif chain_match.pattern.action == ChainAction.WARN:
                logger.warning(f"Suspicious tool call pattern detected: {chain_match.pattern.name} in session {session_id}")
                
        return True, chain_match
        
    def _detect_chain_patterns(self, session: SessionChainContext, current_call: ToolCall) -> Optional[ChainMatch]:
        """Detect if current call completes a suspicious pattern."""
        
        for pattern in self.patterns:
            # Check if current call matches sink pattern
            if not pattern.sink_pattern.search(current_call.tool_name):
                continue
                
            # Look for source calls within time window
            cutoff_time = current_call.timestamp - pattern.max_time_window
            recent_calls = [
                call for call in session.tool_calls
                if call.timestamp >= cutoff_time and call != current_call
            ]
            
            # Limit chain length
            recent_calls = recent_calls[-pattern.max_chain_length:]
            
            # Find source calls matching pattern
            source_calls = []
            for call in recent_calls:
                if self._matches_source_pattern(pattern, call):
                    source_calls.append(call)
            
            if source_calls:
                # Calculate risk score based on pattern and timing
                risk_score = self._calculate_risk_score(pattern, source_calls, [current_call])
                
                return ChainMatch(
                    pattern=pattern,
                    source_calls=source_calls,
                    sink_calls=[current_call],
                    risk_score=risk_score,
                    detected_at=time.time(),
                    session_id=session.session_id
                )
                
        return None
        
    def _matches_source_pattern(self, pattern: ChainPattern, call: ToolCall) -> bool:
        """Check if a call matches the source pattern, including parameter analysis."""
        # Check tool name first
        if not pattern.source_pattern.search(call.tool_name):
            return False
            
        # For credential patterns, check file paths in parameters  
        if "credential" in pattern.name:
            file_path = call.parameters.get("file_path", "")
            if file_path and ("/run/secrets" in file_path or "/etc/passwd" in file_path or "secret" in file_path.lower() or "credential" in file_path.lower() or "key" in file_path.lower()):
                return True
            return False
            
        # For config patterns, check config file extensions
        if "config" in pattern.name:
            file_path = call.parameters.get("file_path", "")
            if file_path and (file_path.endswith((".yaml", ".json", ".conf", ".cfg")) or "config" in file_path.lower()):
                return True
            return False
            
        # Default: just match the tool name
        return True
        
    def _calculate_risk_score(
        self, 
        pattern: ChainPattern, 
        source_calls: List[ToolCall], 
        sink_calls: List[ToolCall]
    ) -> float:
        """Calculate risk score for a detected chain."""
        
        base_score = {
            RiskLevel.LOW: 10.0,
            RiskLevel.MEDIUM: 25.0,
            RiskLevel.HIGH: 50.0,
            RiskLevel.CRITICAL: 100.0
        }[pattern.risk_level]
        
        # Adjust for number of source calls
        source_multiplier = min(len(source_calls) * 0.5, 2.0)
        
        # Adjust for timing (faster = more suspicious)
        if source_calls and sink_calls:
            time_diff = sink_calls[-1].timestamp - source_calls[0].timestamp
            timing_multiplier = max(0.5, 2.0 - (time_diff / pattern.max_time_window))
        else:
            timing_multiplier = 1.0
            
        return base_score * source_multiplier * timing_multiplier
        
    def _trigger_alert(self, chain_match: ChainMatch) -> None:
        """Trigger alert callbacks for a detected chain."""
        for callback in self.alert_callbacks:
            try:
                callback(chain_match)
            except Exception as e:
                logger.error(f"Chain alert callback failed: {e}")
                
    def _cleanup_old_sessions(self) -> None:
        """Remove old sessions to prevent memory bloat."""
        cutoff = time.time() - self.max_session_duration
        
        expired_sessions = [
            sid for sid, session in self.sessions.items()
            if session.last_activity < cutoff
        ]
        
        for sid in expired_sessions:
            del self.sessions[sid]
            logger.debug(f"Cleaned up expired session: {sid}")
            
    def approve_pending_call(self, session_id: str, call_id: str, approver: str = "owner") -> bool:
        """Approve a pending tool call that required approval.
        
        Args:
            session_id: Session containing the call
            call_id: Identifier of the call to approve
            approver: Who approved the call
            
        Returns:
            True if approval was successful
        """
        # In a real implementation, this would interface with an approval queue
        # For now, we just log the approval and return True
        logger.info(f"Tool call {call_id} approved by {approver} for session {session_id}")
        return True
        
    def get_session_stats(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Get statistics for a session."""
        if session_id not in self.sessions:
            return None
            
        session = self.sessions[session_id]
        
        # Count tools by type
        tool_counts = {}
        for call in session.tool_calls:
            tool_counts[call.tool_name] = tool_counts.get(call.tool_name, 0) + 1
            
        # Count patterns by type
        pattern_counts = {}
        for chain in session.detected_chains:
            pattern_counts[chain.pattern.name] = pattern_counts.get(chain.pattern.name, 0) + 1
            
        return {
            "session_id": session_id,
            "total_calls": len(session.tool_calls),
            "detected_chains": len(session.detected_chains),
            "blocked_calls": session.blocked_calls,
            "approval_required_calls": session.approval_required_calls,
            "tool_counts": tool_counts,
            "pattern_counts": pattern_counts,
            "session_duration": time.time() - (session.tool_calls[0].timestamp if session.tool_calls else time.time())
        }
        
    def get_global_stats(self) -> Dict[str, Any]:
        """Get global analyzer statistics."""
        total_sessions = len(self.sessions)
        total_calls = sum(len(s.tool_calls) for s in self.sessions.values())
        total_chains = sum(len(s.detected_chains) for s in self.sessions.values())
        total_blocked = sum(s.blocked_calls for s in self.sessions.values())
        
        return {
            "enabled": self.enabled,
            "total_sessions": total_sessions,
            "total_calls": total_calls,
            "detected_chains": total_chains,
            "blocked_calls": total_blocked,
            "loaded_patterns": len(self.patterns),
            "pattern_names": [p.name for p in self.patterns]
        }
        
    def add_alert_callback(self, callback: callable) -> None:
        """Add a callback function for chain detection alerts."""
        self.alert_callbacks.append(callback)
        
    def add_pattern(self, pattern: ChainPattern) -> None:
        """Add a new chain pattern at runtime."""
        self.patterns.append(pattern)
        logger.info(f"Added new pattern: {pattern.name}")

    # ── C34: Parameter Sanitization ──────────────────────────────────────────

    def sanitize_tool_params(self, tool_name: str, params: Dict[str, Any]) -> ParamScanResult:
        """Scan tool parameters for injection payloads and return sanitized copy."""
        violations: List[str] = []
        sanitized: Dict[str, Any] = {}

        for key, value in params.items():
            val_str = str(value)
            clean = val_str
            for pattern, injection_type in _PARAM_INJECTION_PATTERNS:
                if pattern.search(val_str):
                    violations.append(f"{key}:{injection_type}")
                    clean = pattern.sub("", clean)
            sanitized[key] = clean

        return ParamScanResult(
            safe=len(violations) == 0,
            violations=violations,
            sanitized_params=sanitized,
        )

    # ── C37: Reversibility Scoring ───────────────────────────────────────────

    def score_reversibility(self, tool_name: str, params: Dict[str, Any]) -> ReversibilityScore:
        """Return a reversibility score for the given tool call (1.0 = safe, 0.1 = irreversible)."""
        tool_lower = tool_name.lower().strip()
        score = _REVERSIBILITY_MAP.get(tool_lower, 0.2)
        reasoning = (
            "mapped from built-in reversibility table"
            if tool_lower in _REVERSIBILITY_MAP
            else "unknown tool — defaulting to low reversibility (0.2)"
        )
        return ReversibilityScore(
            score=score,
            tool_name=tool_name,
            action=tool_lower,
            reasoning=reasoning,
        )
