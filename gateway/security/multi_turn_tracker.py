# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Multi-Turn Context Tracker for AgentShroud Gateway

Tracks cumulative information disclosure across multiple conversation turns
to detect slow data extraction attacks. Maintains per-session scoring and
implements threshold-based alerting and blocking.

This module detects patterns like sequential extraction ("first digit is...",
"second digit is...") and repeated sensitive queries with different phrasing.
"""
from __future__ import annotations

import logging
import re
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Set

logger = logging.getLogger("agentshroud.security.multi_turn_tracker")


class DisclosureCategory(str, Enum):
    """Categories of information that contribute to disclosure scoring."""
    PII_FRAGMENT = "pii_fragment"
    INFRASTRUCTURE = "infrastructure"  
    TOOL_NAME = "tool_name"
    CREDENTIAL_INFO = "credential_info"
    SYSTEM_INFO = "system_info"
    FILE_REFERENCE = "file_reference"
    USER_CONTEXT = "user_context"


class AlertLevel(str, Enum):
    """Alert severity levels."""
    WARN = "warn"
    ALERT = "alert" 
    BLOCK = "block"


@dataclass
class DisclosureEvent:
    """A single disclosure event in a session."""
    category: DisclosureCategory
    content: str
    score_impact: float
    timestamp: float
    turn_number: int
    pattern_matched: str = ""


@dataclass
class SessionContext:
    """Context tracking for a single session."""
    session_id: str
    total_score: float = 0.0
    events: List[DisclosureEvent] = field(default_factory=list)
    turn_count: int = 0
    first_seen: float = field(default_factory=time.time)
    last_activity: float = field(default_factory=time.time)
    blocked: bool = False
    owner_notified: bool = False
    repeated_queries: Dict[str, int] = field(default_factory=dict)
    sequential_extractions: List[str] = field(default_factory=list)


@dataclass
class ThresholdConfig:
    """Configuration for alert thresholds."""
    warn_threshold: float = 50.0
    alert_threshold: float = 100.0
    block_threshold: float = 200.0
    max_session_duration: float = 3600.0  # 1 hour
    sequential_extraction_limit: int = 3


class MultiTurnTracker:
    """Main multi-turn disclosure tracking engine.
    
    Maintains session state and scores cumulative disclosure risk
    across conversation turns. Implements threshold-based alerting
    and can block sessions that exceed risk limits.
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initialize the multi-turn tracker.
        
        Args:
            config: Configuration dictionary with threshold settings
        """
        self.config = config or {}
        self.thresholds = ThresholdConfig(**self.config.get("thresholds", {}))
        self.enabled = self.config.get("enabled", True)
        
        # In-memory session storage
        self.sessions: Dict[str, SessionContext] = {}
        
        # Pattern compilation
        self._compile_detection_patterns()
        
        # Alert callbacks
        self.alert_callbacks: List[callable] = []
        
    def _compile_detection_patterns(self) -> None:
        """Compile regex patterns for detecting disclosure categories."""
        
        # PII fragment patterns
        self.pii_patterns = [
            re.compile(r'\b(first|second|third|fourth|fifth)\s+(digit|character|letter)', re.IGNORECASE),
            re.compile(r'\b(starts with|ends with|contains)\s+[a-zA-Z0-9]', re.IGNORECASE),
            re.compile(r'\b(email|phone|address|name|birthday)\s+(is|contains)', re.IGNORECASE),
        ]
        
        # Infrastructure patterns  
        self.infrastructure_patterns = [
            re.compile(r'\b(hostname|server|database|redis|postgres)', re.IGNORECASE),
            re.compile(r'\b(docker|kubernetes|k8s|container)', re.IGNORECASE),
            re.compile(r'\b(port|endpoint|url|domain)', re.IGNORECASE),
        ]
        
        # Tool name patterns
        self.tool_patterns = [
            re.compile(r'\b(read|write|edit|exec|process|browser|canvas|message|tts)\b', re.IGNORECASE),
            re.compile(r'\btool\s+(name|list|inventory)', re.IGNORECASE),
            re.compile(r'\bfunction\s+(call|invoke)', re.IGNORECASE),
        ]
        
        # Credential info patterns
        self.credential_patterns = [
            re.compile(r'\b(password|token|key|secret|credential)', re.IGNORECASE),
            re.compile(r'\b(vault|keychain|1password)', re.IGNORECASE),
            re.compile(r'/run/secrets/', re.IGNORECASE),
        ]
        
        # System info patterns
        self.system_patterns = [
            re.compile(r'\b(system prompt|instructions|rules)', re.IGNORECASE),
            re.compile(r'\b(SOUL\.md|AGENTS\.md|configuration)', re.IGNORECASE),
            re.compile(r'\b(model|claude|anthropic)', re.IGNORECASE),
        ]
        
        # File reference patterns
        self.file_patterns = [
            re.compile(r'\b\w+\.(md|txt|json|yaml|py|js)\b', re.IGNORECASE),
            re.compile(r'\b(memory|config|logs)/', re.IGNORECASE),
        ]
        
        # Sequential extraction patterns
        self.sequential_patterns = [
            re.compile(r'\b(first|1st|initial)\b', re.IGNORECASE),
            re.compile(r'\b(second|2nd|next)\b', re.IGNORECASE), 
            re.compile(r'\b(third|3rd|then)\b', re.IGNORECASE),
            re.compile(r'\b(fourth|4th|after)\b', re.IGNORECASE),
            re.compile(r'\b(last|final|end)\b', re.IGNORECASE),
        ]
        
    def track_message(self, session_id: str, message: str, response: str = "") -> SessionContext:
        """Track a message and response pair for disclosure analysis.
        
        Args:
            session_id: Unique session identifier
            message: User's input message
            response: Agent's response (optional)
            
        Returns:
            Updated session context
        """
        if not self.enabled:
            return self.sessions.get(session_id, SessionContext(session_id=session_id))
            
        # Get or create session context
        if session_id not in self.sessions:
            self.sessions[session_id] = SessionContext(session_id=session_id)
            
        session = self.sessions[session_id]
        session.turn_count += 1
        session.last_activity = time.time()
        
        # Check if session is blocked
        if session.blocked:
            logger.warning(f"Blocked session {session_id} attempted new message")
            return session
            
        # Clean old sessions periodically
        self._cleanup_old_sessions()
        
        # Analyze user message for disclosure attempts
        self._analyze_user_message(session, message)
        
        # Analyze agent response for leaks
        if response:
            self._analyze_agent_response(session, response)
            
        # Check thresholds and take action
        self._check_thresholds(session)
        
        return session
        
    def _analyze_user_message(self, session: SessionContext, message: str) -> None:
        """Analyze user message for disclosure patterns."""
        
        # Check for repeated queries (rephrasing detection)
        normalized_message = self._normalize_query(message)
        if normalized_message in session.repeated_queries:
            session.repeated_queries[normalized_message] += 1
            if session.repeated_queries[normalized_message] >= 3:
                self._add_disclosure_event(
                    session,
                    DisclosureCategory.SYSTEM_INFO,
                    f"Repeated query attempt #{session.repeated_queries[normalized_message]}",
                    15.0,
                    "repeated_query"
                )
        else:
            session.repeated_queries[normalized_message] = 1
            
        # Check for sequential extraction patterns
        sequential_matches = []
        for pattern in self.sequential_patterns:
            if pattern.search(message):
                sequential_matches.append(pattern.pattern)
                
        if sequential_matches:
            session.sequential_extractions.extend(sequential_matches)
            if len(session.sequential_extractions) >= self.thresholds.sequential_extraction_limit:
                self._add_disclosure_event(
                    session,
                    DisclosureCategory.PII_FRAGMENT,
                    "Sequential extraction detected",
                    25.0,
                    "sequential_extraction"
                )
                
        # Score based on pattern categories
        self._score_message_patterns(session, message)
        
    def _analyze_agent_response(self, session: SessionContext, response: str) -> None:
        """Analyze agent response for potential information leaks."""
        
        # Score response patterns that might indicate leaks
        self._score_response_patterns(session, response)
        
    def _score_message_patterns(self, session: SessionContext, message: str) -> None:
        """Score message based on disclosure patterns."""
        
        pattern_categories = [
            (self.pii_patterns, DisclosureCategory.PII_FRAGMENT, 10.0),
            (self.infrastructure_patterns, DisclosureCategory.INFRASTRUCTURE, 15.0),
            (self.tool_patterns, DisclosureCategory.TOOL_NAME, 8.0),
            (self.credential_patterns, DisclosureCategory.CREDENTIAL_INFO, 25.0),
            (self.system_patterns, DisclosureCategory.SYSTEM_INFO, 20.0),
            (self.file_patterns, DisclosureCategory.FILE_REFERENCE, 12.0),
        ]
        
        for patterns, category, base_score in pattern_categories:
            for pattern in patterns:
                matches = pattern.findall(message)
                for match in matches:
                    self._add_disclosure_event(
                        session,
                        category,
                        str(match)[:100],  # Truncate for storage
                        base_score,
                        pattern.pattern[:50]
                    )
                    
    def _score_response_patterns(self, session: SessionContext, response: str) -> None:
        """Score agent response for potential leaks."""
        
        # Look for signs that sensitive info was disclosed
        leak_indicators = [
            re.compile(r'\[.*REDACTED.*\]', re.IGNORECASE),
            re.compile(r'I cannot (share|reveal|disclose)', re.IGNORECASE),
            re.compile(r'(sensitive|confidential|internal)', re.IGNORECASE),
        ]
        
        for pattern in leak_indicators:
            if pattern.search(response):
                self._add_disclosure_event(
                    session,
                    DisclosureCategory.SYSTEM_INFO,
                    "Potential leak detected in response",
                    5.0,
                    "response_analysis"
                )
                
    def _normalize_query(self, message: str) -> str:
        """Normalize query for repeated query detection."""
        # Remove common variations and normalize
        normalized = re.sub(r'\b(what|how|can you|could you|please)\b', '', message.lower())
        normalized = re.sub(r'[^a-z0-9\s]', '', normalized)
        normalized = re.sub(r'\s+', ' ', normalized).strip()
        return normalized[:100]  # Truncate
        
    def _add_disclosure_event(
        self, 
        session: SessionContext, 
        category: DisclosureCategory,
        content: str,
        score_impact: float,
        pattern: str
    ) -> None:
        """Add a disclosure event to the session."""
        
        event = DisclosureEvent(
            category=category,
            content=content,
            score_impact=score_impact,
            timestamp=time.time(),
            turn_number=session.turn_count,
            pattern_matched=pattern
        )
        
        session.events.append(event)
        session.total_score += score_impact
        
        logger.info(f"Session {session.session_id}: +{score_impact} points for {category.value} (total: {session.total_score})")
        
    def _check_thresholds(self, session: SessionContext) -> None:
        """Check session score against thresholds and take action."""
        
        score = session.total_score
        
        if score >= self.thresholds.block_threshold:
            if not session.blocked:
                session.blocked = True
                self._trigger_alert(session, AlertLevel.BLOCK)
                logger.error(f"Session {session.session_id} BLOCKED - score: {score}")
                
        elif score >= self.thresholds.alert_threshold:
            if not session.owner_notified:
                session.owner_notified = True
                self._trigger_alert(session, AlertLevel.ALERT)
                logger.warning(f"Session {session.session_id} ALERT - score: {score}")
                
        elif score >= self.thresholds.warn_threshold:
            self._trigger_alert(session, AlertLevel.WARN)
            logger.info(f"Session {session.session_id} WARNING - score: {score}")
            
    def _trigger_alert(self, session: SessionContext, level: AlertLevel) -> None:
        """Trigger alert callbacks."""
        for callback in self.alert_callbacks:
            try:
                callback(session, level)
            except Exception as e:
                logger.error(f"Alert callback failed: {e}")
                
    def _cleanup_old_sessions(self) -> None:
        """Remove old sessions to prevent memory bloat."""
        cutoff = time.time() - self.thresholds.max_session_duration
        
        expired_sessions = [
            sid for sid, session in self.sessions.items()
            if session.last_activity < cutoff
        ]
        
        for sid in expired_sessions:
            del self.sessions[sid]
            logger.debug(f"Cleaned up expired session: {sid}")
            
    def reset_session(self, session_id: str, owner_override: bool = False) -> bool:
        """Reset session score after owner review.
        
        Args:
            session_id: Session to reset
            owner_override: Whether this is an owner-authorized reset
            
        Returns:
            True if reset was successful
        """
        if session_id not in self.sessions:
            return False
            
        session = self.sessions[session_id]
        
        if owner_override:
            session.total_score = 0.0
            session.blocked = False
            session.owner_notified = False
            session.events.clear()
            session.repeated_queries.clear()
            session.sequential_extractions.clear()
            
            logger.info(f"Session {session_id} reset by owner override")
            return True
            
        return False
        
    def get_session_stats(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Get statistics for a session."""
        if session_id not in self.sessions:
            return None
            
        session = self.sessions[session_id]
        
        category_counts = {}
        for event in session.events:
            category_counts[event.category.value] = category_counts.get(event.category.value, 0) + 1
            
        return {
            "session_id": session_id,
            "total_score": session.total_score,
            "turn_count": session.turn_count,
            "event_count": len(session.events),
            "blocked": session.blocked,
            "owner_notified": session.owner_notified,
            "category_breakdown": category_counts,
            "repeated_query_count": len(session.repeated_queries),
            "sequential_extraction_count": len(session.sequential_extractions),
            "session_duration": time.time() - session.first_seen,
        }
        
    def get_global_stats(self) -> Dict[str, Any]:
        """Get global tracking statistics."""
        total_sessions = len(self.sessions)
        blocked_sessions = sum(1 for s in self.sessions.values() if s.blocked)
        total_events = sum(len(s.events) for s in self.sessions.values())
        
        return {
            "enabled": self.enabled,
            "total_sessions": total_sessions,
            "blocked_sessions": blocked_sessions,
            "total_events": total_events,
            "thresholds": {
                "warn": self.thresholds.warn_threshold,
                "alert": self.thresholds.alert_threshold,
                "block": self.thresholds.block_threshold,
            }
        }
        
    def add_alert_callback(self, callback: callable) -> None:
        """Add a callback function for alerts."""
        self.alert_callbacks.append(callback)

    # ── C30: Response Consistency Scoring ─────────────────────────────────────

    def score_response_consistency(
        self, session_id: str, response: str, query: str
    ) -> "ConsistencyScore":
        """Compute a heuristic consistency score between query and response.

        Returns ConsistencyScore with score 0.0–1.0 (higher = more consistent).
        Anomalies below 0.4 trigger an audit warning.
        """
        from dataclasses import dataclass as _dc

        factors: List[str] = []
        anomalies: List[str] = []
        score = 1.0

        # Unsolicited tool call in response — likely injection artefact
        if re.search(
            r'<(?:function_calls?|tool_calls?|invoke)\b', response, re.IGNORECASE
        ):
            score -= 0.3
            anomalies.append("unsolicited_tool_call")

        # Length ratio anomaly — response vastly longer than query unprompted
        if query and len(response) > len(query) * 25:
            score -= 0.2
            anomalies.append("length_ratio_anomaly")

        # Topic scope: key content words in query absent from response
        query_words = set(re.findall(r'\b\w{5,}\b', query.lower()))
        resp_words = set(re.findall(r'\b\w{5,}\b', response.lower()))
        if query_words and len(query_words & resp_words) / len(query_words) < 0.1:
            score -= 0.2
            anomalies.append("topic_scope_mismatch")

        score = max(0.0, round(score, 2))

        if score < 0.4 and self.enabled:
            logger.warning(
                "Low response consistency score %.2f for session %s: %s",
                score, session_id, anomalies,
            )

        return ConsistencyScore(score=score, factors=factors, anomalies=anomalies)


@dataclass
class ConsistencyScore:
    """Heuristic consistency score between a query and its response."""
    score: float
    factors: List[str]
    anomalies: List[str]
