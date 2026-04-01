# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Output Canary System for AgentShroud Gateway

Detects prompt leakage by injecting unique invisible canary tokens into system
prompts and scanning outbound responses for their presence. When a canary is
detected in a response, it indicates that the system prompt was leaked.

Features:
- UUID-based unique canary generation per session
- Invisible canary injection using zero-width characters and Unicode markers
- Response scanning for canary detection
- Incident logging and alerting
- Session status tracking
"""
from __future__ import annotations

import logging
import re
import time
import uuid
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set

logger = logging.getLogger("agentshroud.security.output_canary")


@dataclass
class CanaryResult:
    """Result of checking a response for canary presence."""
    canary_detected: bool
    session_id: str
    canary_id: str
    matches_found: List[str] = field(default_factory=list)
    match_positions: List[tuple] = field(default_factory=list)  # (start, end) positions
    detection_method: str = ""
    risk_level: str = "low"  # low, medium, high
    incident_id: Optional[str] = None
    timestamp: float = field(default_factory=time.time)


@dataclass
class CanaryConfig:
    """Configuration for the Output Canary System."""
    canary_length: int = 32  # Length of the base UUID portion
    use_zero_width_chars: bool = True
    use_unicode_tags: bool = True
    use_comment_markers: bool = True
    log_incidents: bool = True
    block_on_detection: bool = True
    max_canaries_per_session: int = 1


class OutputCanary:
    """Main Output Canary System for detecting prompt leakage.
    
    This system generates unique canary tokens for each session and embeds
    them invisibly into system prompts. If these canaries appear in outbound
    responses, it indicates that the system prompt has been leaked.
    """
    
    def __init__(self, config: Optional[CanaryConfig] = None):
        """Initialize the Output Canary System.
        
        Args:
            config: Optional configuration. Uses defaults if not provided.
        """
        self.config = config or CanaryConfig()
        self._session_canaries: Dict[str, Dict[str, Any]] = {}
        self._canary_cache: Set[str] = set()
        
        # Zero-width characters for invisible injection
        self._zero_width_chars = {
            'zwsp': '\u200B',  # Zero Width Space
            'zwnj': '\u200C',  # Zero Width Non-Joiner
            'zwj': '\u200D',   # Zero Width Joiner
            'ltr': '\u202D',   # Left-to-Right Override
            'rtl': '\u202E',   # Right-to-Left Override
            'pdf': '\u202C',   # Pop Directional Formatting
        }
        
        # Unicode tag characters (invisible)
        self._tag_chars = [chr(i) for i in range(0xE0020, 0xE007F)]
        
        logger.info("Output Canary System initialized")
    
    def generate_canary(self, session_id: str) -> str:
        """Generate and store a canary for this session.
        
        Args:
            session_id: Unique session identifier
            
        Returns:
            The canary string to embed in system prompt
            
        Raises:
            ValueError: If session already has max canaries
        """
        if session_id in self._session_canaries:
            if len(self._session_canaries[session_id]) >= self.config.max_canaries_per_session:
                raise ValueError(f"Session {session_id} already has maximum canaries")
        
        # Generate base canary using UUID
        base_canary = str(uuid.uuid4()).replace('-', '')[:self.config.canary_length]
        canary_id = f"canary-{int(time.time())}-{len(self._session_canaries.get(session_id, {}))}"
        
        # Create invisible canary variants
        invisible_canary = self._create_invisible_canary(base_canary, canary_id)
        
        # Store canary data
        if session_id not in self._session_canaries:
            self._session_canaries[session_id] = {}
            
        canary_data = {
            'canary_id': canary_id,
            'base_canary': base_canary,
            'invisible_canary': invisible_canary,
            'created_at': time.time(),
            'detection_patterns': self._create_detection_patterns(base_canary),
        }
        
        self._session_canaries[session_id][canary_id] = canary_data
        self._canary_cache.add(base_canary)
        
        logger.info(f"Generated canary {canary_id} for session {session_id}")
        return invisible_canary
    
    def _create_invisible_canary(self, base_canary: str, canary_id: str) -> str:
        """Create an invisible version of the canary using various techniques.
        
        Args:
            base_canary: Base canary string
            canary_id: Canary identifier
            
        Returns:
            Invisible canary string
        """
        invisible_parts = []
        
        if self.config.use_zero_width_chars:
            # Embed using zero-width characters
            zw_canary = ''
            for i, char in enumerate(base_canary):
                zw_canary += char
                if i < len(base_canary) - 1:  # Don't add after last char
                    zw_char = list(self._zero_width_chars.values())[i % len(self._zero_width_chars)]
                    zw_canary += zw_char
            invisible_parts.append(zw_canary)
        
        if self.config.use_unicode_tags:
            # Embed using Unicode tag characters
            tag_canary = base_canary
            for i, tag_char in enumerate(self._tag_chars[:len(base_canary)]):
                tag_canary += tag_char
            invisible_parts.append(tag_canary)
        
        if self.config.use_comment_markers:
            # Embed using comment-style markers (less invisible but effective)
            comment_canary = f"<!-- {canary_id}: {base_canary} -->"
            invisible_parts.append(comment_canary)
        
        # Combine all invisible techniques
        return ''.join(invisible_parts) if invisible_parts else base_canary
    
    def _create_detection_patterns(self, base_canary: str) -> List[re.Pattern]:
        """Create regex patterns to detect the canary in responses.
        
        Args:
            base_canary: Base canary string to create patterns for
            
        Returns:
            List of compiled regex patterns
        """
        patterns = []
        
        # Exact match
        patterns.append(re.compile(re.escape(base_canary), re.IGNORECASE))
        
        # Match with zero-width characters inserted
        zw_pattern = re.escape(base_canary[0])
        for char in base_canary[1:]:
            zw_pattern += r'[\u200B\u200C\u200D\u202D\u202E\u202C]*' + re.escape(char)
        patterns.append(re.compile(zw_pattern, re.IGNORECASE))
        
        # Match with potential encoding/escaping
        encoded_pattern = re.escape(base_canary).replace(r'\ ', r'[\ \s]*')
        patterns.append(re.compile(encoded_pattern, re.IGNORECASE))
        
        # Partial matches (at least 8 consecutive chars for long canaries)
        if len(base_canary) >= 12:
            for i in range(len(base_canary) - 8):
                partial = base_canary[i:i+8]
                patterns.append(re.compile(re.escape(partial), re.IGNORECASE))
        
        return patterns
    
    def check_response(self, session_id: str, response_text: str) -> CanaryResult:
        """Check if response contains the session's canary (prompt leakage detected).
        
        Args:
            session_id: Session identifier to check canaries for
            response_text: Response text to scan for canaries
            
        Returns:
            CanaryResult with detection status and details
        """
        # If no canaries for this session, return safe result
        if session_id not in self._session_canaries:
            return CanaryResult(
                canary_detected=False,
                session_id=session_id,
                canary_id="none",
                risk_level="low"
            )
        
        # Check each canary for this session
        for canary_id, canary_data in self._session_canaries[session_id].items():
            result = self._scan_for_canary(session_id, canary_id, canary_data, response_text)
            if result.canary_detected:
                return result
        
        # No canaries detected
        return CanaryResult(
            canary_detected=False,
            session_id=session_id,
            canary_id="none",
            risk_level="low"
        )
    
    def _scan_for_canary(self, session_id: str, canary_id: str, canary_data: Dict[str, Any], 
                        response_text: str) -> CanaryResult:
        """Scan response text for a specific canary.
        
        Args:
            session_id: Session identifier
            canary_id: Canary identifier
            canary_data: Canary data dictionary
            response_text: Text to scan
            
        Returns:
            CanaryResult with detection details
        """
        matches_found = []
        match_positions = []
        detection_method = ""
        risk_level = "low"
        
        # Check against all detection patterns
        for i, pattern in enumerate(canary_data['detection_patterns']):
            matches = list(pattern.finditer(response_text))
            if matches:
                matches_found.extend([match.group() for match in matches])
                match_positions.extend([(match.start(), match.end()) for match in matches])
                
                if i == 0:  # Exact match
                    detection_method = "exact_match"
                    risk_level = "high"
                elif i == 1:  # Zero-width character match
                    detection_method = "zero_width_match"
                    risk_level = "high"
                elif i == 2:  # Encoded match
                    detection_method = "encoded_match"
                    risk_level = "medium"
                else:  # Partial match
                    detection_method = "partial_match"
                    risk_level = "medium"
                break
        
        canary_detected = len(matches_found) > 0
        incident_id = None
        
        if canary_detected:
            incident_id = f"canary-leak-{session_id}-{canary_id}-{int(time.time())}"
            
            if self.config.log_incidents:
                logger.warning(
                    f"CANARY DETECTED: Possible prompt leakage in session {session_id}. "
                    f"Canary: {canary_id}, Method: {detection_method}, "
                    f"Matches: {len(matches_found)}, Risk: {risk_level}, "
                    f"Incident: {incident_id}"
                )
            
            # Mark canary as compromised
            canary_data['compromised'] = True
            canary_data['compromised_at'] = time.time()
        
        return CanaryResult(
            canary_detected=canary_detected,
            session_id=session_id,
            canary_id=canary_id,
            matches_found=matches_found,
            match_positions=match_positions,
            detection_method=detection_method,
            risk_level=risk_level,
            incident_id=incident_id
        )
    
    def get_status(self, session_id: str) -> Dict[str, Any]:
        """Return canary status for dashboard.
        
        Args:
            session_id: Session identifier
            
        Returns:
            Dictionary with canary status information
        """
        if session_id not in self._session_canaries:
            return {
                'session_id': session_id,
                'status': 'red',  # No canary = not protected
                'canary_count': 0,
                'active_canaries': 0,
                'compromised_canaries': 0,
                'last_generated': None,
                'protection_level': 'none'
            }
        
        canaries = self._session_canaries[session_id]
        active_count = sum(1 for c in canaries.values() if not c.get('compromised', False))
        compromised_count = sum(1 for c in canaries.values() if c.get('compromised', False))
        
        # Determine status
        if compromised_count > 0:
            status = 'red'  # Compromised
            protection_level = 'compromised'
        elif active_count > 0:
            status = 'green'  # Active protection
            protection_level = 'protected'
        else:
            status = 'yellow'  # No active canaries
            protection_level = 'expired'
        
        # Get last generation time
        last_generated = None
        if canaries:
            last_generated = max(c.get('created_at', 0) for c in canaries.values())
        
        return {
            'session_id': session_id,
            'status': status,
            'canary_count': len(canaries),
            'active_canaries': active_count,
            'compromised_canaries': compromised_count,
            'last_generated': last_generated,
            'protection_level': protection_level
        }
    
    def cleanup_expired_canaries(self, max_age_seconds: float = 3600) -> int:
        """Clean up old canaries to prevent memory leaks.
        
        Args:
            max_age_seconds: Maximum age of canaries to keep
            
        Returns:
            Number of canaries cleaned up
        """
        current_time = time.time()
        cleaned_count = 0
        
        sessions_to_remove = []
        for session_id, canaries in self._session_canaries.items():
            canaries_to_remove = []
            
            for canary_id, canary_data in canaries.items():
                if current_time - canary_data.get('created_at', 0) > max_age_seconds:
                    canaries_to_remove.append(canary_id)
                    self._canary_cache.discard(canary_data.get('base_canary', ''))
                    cleaned_count += 1
            
            for canary_id in canaries_to_remove:
                del canaries[canary_id]
            
            if not canaries:
                sessions_to_remove.append(session_id)
        
        for session_id in sessions_to_remove:
            del self._session_canaries[session_id]
        
        if cleaned_count > 0:
            logger.info(f"Cleaned up {cleaned_count} expired canaries")
        
        return cleaned_count