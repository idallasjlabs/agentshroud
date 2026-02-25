# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Memory Lifecycle Manager - R-19 Implementation

Manages memory file retention policies, archival, and content security.
Prevents memory poisoning through PII scanning and injection detection.
"""

import logging
import re
import shutil
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple, Any
from dataclasses import dataclass, asdict
from enum import Enum

from gateway.security.memory_config import MemorySecurityConfig, MemoryLifecycleConfig


logger = logging.getLogger(__name__)


class ContentThreatType(Enum):
    """Types of content threats detected in memory files."""
    PII_DETECTED = 'pii_detected'
    PROMPT_INJECTION = 'prompt_injection'
    MALICIOUS_CODE = 'malicious_code'
    EXCESSIVE_SIZE = 'excessive_size'


@dataclass 
class ContentThreat:
    """Detected threat in memory file content."""
    threat_type: ContentThreatType
    file_path: str
    line_number: Optional[int] = None
    matched_pattern: Optional[str] = None
    severity: str = 'MEDIUM'
    details: Optional[str] = None
    timestamp: float = None
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = time.time()


@dataclass
class RetentionAction:
    """Action taken during retention policy enforcement."""
    action_type: str  # 'archived', 'deleted', 'truncated'
    file_path: str
    original_size: int
    final_size: int = 0
    archive_path: Optional[str] = None
    timestamp: float = None
    reason: str = ''
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = time.time()


class MemoryLifecycleManager:
    """Manages memory file lifecycle and content security."""
    
    def __init__(self, config: MemoryLifecycleConfig, base_directory: Path):
        self.config = config
        self.base_directory = base_directory
        self.archive_directory = base_directory / self.config.archive_directory
        
        # Pattern compilation for efficiency
        self._compiled_injection_patterns = [
            re.compile(pattern, re.IGNORECASE | re.MULTILINE) 
            for pattern in self.config.injection_patterns
        ]
        
        # PII patterns (basic regex patterns for common PII types)
        self._pii_patterns = {
            'US_SSN': re.compile(r'\b\d{3}-\d{2}-\d{4}\b|\b\d{9}\b'),
            'CREDIT_CARD': re.compile(r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b'),
            'PHONE_NUMBER': re.compile(r'\b\d{3}[\s.-]?\d{3}[\s.-]?\d{4}\b'),
            'EMAIL_ADDRESS': re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'),
            'US_PASSPORT': re.compile(r'\b[A-Za-z]{1,2}\d{6,8}\b'),
            'US_DRIVER_LICENSE': re.compile(r'\b[A-Za-z]\d{7,8}\b|\b\d{8,9}\b')
        }
        
        # Threat tracking
        self.detected_threats: List[ContentThreat] = []
        self.retention_actions: List[RetentionAction] = []
        
        # Ensure archive directory exists
        self.archive_directory.mkdir(parents=True, exist_ok=True)
    
    def scan_content_for_threats(self, content: str, file_path: str) -> List[ContentThreat]:
        """Scan memory file content for security threats."""
        threats = []
        
        if not self.config.enabled:
            return threats
        
        lines = content.split('\n')
        
        # PII scanning
        if self.config.pii_scanning_enabled:
            for entity_type in self.config.pii_entities:
                if entity_type in self._pii_patterns:
                    pattern = self._pii_patterns[entity_type]
                    for line_num, line in enumerate(lines, 1):
                        matches = pattern.findall(line)
                        for match in matches:
                            threat = ContentThreat(
                                threat_type=ContentThreatType.PII_DETECTED,
                                file_path=file_path,
                                line_number=line_num,
                                matched_pattern=entity_type,
                                severity='HIGH',
                                details=f'Found {entity_type}: {match[:10]}...'
                            )
                            threats.append(threat)
        
        # Prompt injection scanning
        if self.config.injection_scanning_enabled:
            for pattern in self._compiled_injection_patterns:
                for line_num, line in enumerate(lines, 1):
                    match = pattern.search(line)
                    if match:
                        threat = ContentThreat(
                            threat_type=ContentThreatType.PROMPT_INJECTION,
                            file_path=file_path,
                            line_number=line_num,
                            matched_pattern=match.group(0),
                            severity='CRITICAL',
                            details=f'Potential prompt injection: {match.group(0)[:50]}...'
                        )
                        threats.append(threat)
        
        # Size check
        if len(content.encode('utf-8')) > self.config.memory_md_max_size and file_path.endswith('MEMORY.md'):
            threat = ContentThreat(
                threat_type=ContentThreatType.EXCESSIVE_SIZE,
                file_path=file_path,
                severity='MEDIUM',
                details=f'File exceeds maximum size: {len(content)} bytes > {self.config.memory_md_max_size} bytes'
            )
            threats.append(threat)
        
        return threats
    
    def sanitize_content(self, content: str, file_path: str) -> Tuple[str, List[ContentThreat]]:
        """Sanitize content by removing/redacting threats."""
        threats = self.scan_content_for_threats(content, file_path)
        sanitized_content = content
        
        for threat in threats:
            if threat.threat_type == ContentThreatType.PII_DETECTED:
                # Redact PII
                if threat.matched_pattern and threat.matched_pattern in self._pii_patterns:
                    pattern = self._pii_patterns[threat.matched_pattern]
                    sanitized_content = pattern.sub('[REDACTED-PII]', sanitized_content)
            
            elif threat.threat_type == ContentThreatType.PROMPT_INJECTION:
                # Remove injection attempts
                if threat.matched_pattern:
                    sanitized_content = sanitized_content.replace(
                        threat.matched_pattern, 
                        '[REMOVED-INJECTION-ATTEMPT]'
                    )
        
        return sanitized_content, threats
    
    def validate_memory_write(self, content: str, file_path: Path) -> Tuple[bool, List[ContentThreat]]:
        """Validate content before writing to memory file."""
        path_str = str(file_path.relative_to(self.base_directory))
        threats = self.scan_content_for_threats(content, path_str)
        
        # Log threats
        for threat in threats:
            self.detected_threats.append(threat)
            if threat.severity == 'CRITICAL':
                logger.critical(f"SECURITY THREAT: {threat.threat_type.value} in {path_str}: {threat.details}")
            elif threat.severity == 'HIGH':
                logger.error(f"HIGH RISK: {threat.threat_type.value} in {path_str}: {threat.details}")
            else:
                logger.warning(f"RISK: {threat.threat_type.value} in {path_str}: {threat.details}")
        
        # Determine if write should be blocked
        critical_threats = [t for t in threats if t.severity == 'CRITICAL']
        
        return len(critical_threats) == 0, threats
    
    def archive_file(self, file_path: Path, reason: str = '') -> Optional[Path]:
        """Archive a file to the archive directory."""
        try:
            if not file_path.exists():
                return None
            
            # Create archive path with timestamp
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            archive_name = f'{file_path.stem}_{timestamp}{file_path.suffix}'
            archive_path = self.archive_directory / archive_name
            
            # Ensure archive directory structure
            archive_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Copy file to archive
            shutil.copy2(file_path, archive_path)
            
            original_size = file_path.stat().st_size
            
            # Record the action
            action = RetentionAction(
                action_type='archived',
                file_path=str(file_path.relative_to(self.base_directory)),
                original_size=original_size,
                archive_path=str(archive_path.relative_to(self.base_directory)),
                reason=reason
            )
            self.retention_actions.append(action)
            
            logger.info(f"Archived {file_path} to {archive_path} ({reason})")
            return archive_path
            
        except Exception as e:
            logger.error(f"Failed to archive {file_path}: {e}")
            return None
    
    def enforce_daily_notes_retention(self):
        """Enforce retention policy for daily notes."""
        if not self.config.enabled:
            return
        
        memory_dir = self.base_directory / 'memory'
        if not memory_dir.exists():
            return
        
        cutoff_date = datetime.now() - timedelta(days=self.config.daily_notes_retention_days)
        cutoff_timestamp = cutoff_date.timestamp()
        
        # Find old daily note files
        for file_path in memory_dir.glob('*.md'):
            # Skip non-daily-note files
            if not re.match(r'\d{4}-\d{2}-\d{2}\.md', file_path.name):
                continue
            
            try:
                stat = file_path.stat()
                if stat.st_mtime < cutoff_timestamp:
                    archive_path = self.archive_file(
                        file_path, 
                        f'retention_policy_daily_notes_{self.config.daily_notes_retention_days}d'
                    )
                    if archive_path:
                        file_path.unlink()  # Delete original
            except Exception as e:
                logger.error(f"Failed to process daily note {file_path}: {e}")
    
    def enforce_memory_md_size_limit(self):
        """Enforce size limit for MEMORY.md file."""
        if not self.config.enabled:
            return
        
        memory_md_path = self.base_directory / 'MEMORY.md'
        if not memory_md_path.exists():
            return
        
        try:
            current_size = memory_md_path.stat().st_size
            if current_size > self.config.memory_md_max_size:
                logger.warning(f"MEMORY.md exceeds size limit: {current_size} > {self.config.memory_md_max_size}")
                
                # Archive current version
                archive_path = self.archive_file(
                    memory_md_path,
                    f'size_limit_exceeded_{current_size}bytes'
                )
                
                if archive_path:
                    # Truncate to size limit
                    with open(memory_md_path, 'r+', encoding='utf-8') as f:
                        content = f.read()
                        # Try to truncate at a reasonable boundary (paragraph break)
                        truncated = content[:self.config.memory_md_max_size]
                        last_double_newline = truncated.rfind('\n\n')
                        if last_double_newline > self.config.memory_md_max_size // 2:
                            truncated = truncated[:last_double_newline + 2]
                        
                        truncated += '\n\n[TRUNCATED - Full content archived due to size limit]\n'
                        
                        f.seek(0)
                        f.write(truncated)
                        f.truncate()
                    
                    action = RetentionAction(
                        action_type='truncated',
                        file_path='MEMORY.md',
                        original_size=current_size,
                        final_size=len(truncated.encode('utf-8')),
                        archive_path=str(archive_path.relative_to(self.base_directory)),
                        reason=f'size_limit_{self.config.memory_md_max_size}bytes'
                    )
                    self.retention_actions.append(action)
                    
                    logger.info(f"Truncated MEMORY.md from {current_size} to {action.final_size} bytes")
        
        except Exception as e:
            logger.error(f"Failed to enforce MEMORY.md size limit: {e}")
    
    def run_lifecycle_maintenance(self):
        """Run all lifecycle maintenance tasks."""
        if not self.config.enabled:
            logger.debug("Memory lifecycle management disabled")
            return
        
        logger.debug("Running memory lifecycle maintenance")
        
        try:
            self.enforce_daily_notes_retention()
            self.enforce_memory_md_size_limit()
            self._cleanup_old_threats()
            self._cleanup_old_actions()
        except Exception as e:
            logger.error(f"Error during lifecycle maintenance: {e}")
        
        logger.debug("Completed memory lifecycle maintenance")
    
    def _cleanup_old_threats(self, days: int = 30):
        """Clean up old threat records."""
        cutoff_time = time.time() - (days * 24 * 3600)
        original_count = len(self.detected_threats)
        self.detected_threats = [
            threat for threat in self.detected_threats
            if threat.timestamp > cutoff_time
        ]
        if len(self.detected_threats) < original_count:
            logger.debug(f"Cleaned up {original_count - len(self.detected_threats)} old threat records")
    
    def _cleanup_old_actions(self, days: int = 30):
        """Clean up old retention action records."""
        cutoff_time = time.time() - (days * 24 * 3600)
        original_count = len(self.retention_actions)
        self.retention_actions = [
            action for action in self.retention_actions
            if action.timestamp > cutoff_time
        ]
        if len(self.retention_actions) < original_count:
            logger.debug(f"Cleaned up {original_count - len(self.retention_actions)} old retention action records")
    
    def get_recent_threats(self, hours: int = 24) -> List[ContentThreat]:
        """Get threats detected in the last N hours."""
        cutoff_time = time.time() - (hours * 3600)
        return [threat for threat in self.detected_threats if threat.timestamp > cutoff_time]
    
    def get_recent_actions(self, hours: int = 24) -> List[RetentionAction]:
        """Get retention actions taken in the last N hours."""
        cutoff_time = time.time() - (hours * 3600)
        return [action for action in self.retention_actions if action.timestamp > cutoff_time]
    
    def get_lifecycle_status(self) -> Dict[str, Any]:
        """Get current lifecycle management status."""
        recent_threats = self.get_recent_threats()
        recent_actions = self.get_recent_actions()
        critical_threats = [t for t in recent_threats if t.severity == 'CRITICAL']
        
        return {
            'enabled': self.config.enabled,
            'pii_scanning_enabled': self.config.pii_scanning_enabled,
            'injection_scanning_enabled': self.config.injection_scanning_enabled,
            'daily_notes_retention_days': self.config.daily_notes_retention_days,
            'memory_md_max_size': self.config.memory_md_max_size,
            'recent_threats_24h': len(recent_threats),
            'critical_threats_24h': len(critical_threats),
            'recent_actions_24h': len(recent_actions),
            'archive_directory': str(self.archive_directory)
        }
