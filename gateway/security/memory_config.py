# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Memory Security Configuration - Memory Lifecycle Management

Centralized configuration for memory file integrity monitoring and lifecycle policies.
Protects against memory poisoning attacks and manages retention policies.
"""

import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Set


@dataclass
class MemoryIntegrityConfig:
    """Configuration for memory file integrity monitoring."""
    
    # Files that should never change without human authorization
    protected_files: Set[str] = field(default_factory=lambda: {
        'SOUL.md',
        'AGENTS.md',
        'BRAND.md',
        'USER.md'
    })
    
    # Memory files to monitor for integrity
    monitored_files: Set[str] = field(default_factory=lambda: {
        'MEMORY.md',
        'HEARTBEAT.md',
        'TOOLS.md'
    })
    
    # Directories to monitor for daily notes
    monitored_directories: Set[str] = field(default_factory=lambda: {
        'memory'
    })
    
    # How often to check integrity (seconds)
    check_interval: int = 300  # 5 minutes
    
    # Grace period after expected writes (seconds)
    write_grace_period: int = 60  # 1 minute
    
    # Enable integrity checking
    enabled: bool = True


@dataclass 
class MemoryLifecycleConfig:
    """Configuration for memory lifecycle management."""
    
    # Retention policy for daily notes (days)
    daily_notes_retention_days: int = 90
    
    # Maximum size for MEMORY.md (bytes)
    memory_md_max_size: int = 100 * 1024  # 100KB
    
    # Archive directory for old memory files
    archive_directory: str = 'memory/archive'
    
    # PII entities to scan for in memory files
    pii_entities: Set[str] = field(default_factory=lambda: {
        'US_SSN',
        'CREDIT_CARD', 
        'PHONE_NUMBER',
        'EMAIL_ADDRESS',
        'US_PASSPORT',
        'US_DRIVER_LICENSE'
    })
    
    # Dangerous patterns that indicate prompt injection
    injection_patterns: List[str] = field(default_factory=lambda: [
        r'ignore.*instructions',
        r'ignore\s+previous\s+instructions',
        r'you\s+are\s+now\s+a\s+different\s+assistant',
        r'forget\s+everything\s+above',
        r'system\s*:\s*new\s+directive',
        r'<\s*system\s*>.*?override',
        r'jailbreak\s+mode',
        r'developer\s+mode\s+enabled'
    ])
    
    # Enable lifecycle management
    enabled: bool = True
    
    # Enable PII scanning 
    pii_scanning_enabled: bool = True
    
    # Enable injection scanning
    injection_scanning_enabled: bool = True


@dataclass
class MemorySecurityConfig:
    """Combined memory security configuration."""
    
    integrity: MemoryIntegrityConfig = field(default_factory=MemoryIntegrityConfig)
    lifecycle: MemoryLifecycleConfig = field(default_factory=MemoryLifecycleConfig)
    
    # Base directory for memory files (relative to workspace)
    base_directory: Path = field(default_factory=lambda: Path('.'))
    
    @classmethod
    def from_env(cls) -> 'MemorySecurityConfig':
        """Create configuration from environment variables."""
        config = cls()
        
        # Override from environment
        if retention_days := os.getenv('AGENTSHROUD_MEMORY_RETENTION_DAYS'):
            config.lifecycle.daily_notes_retention_days = int(retention_days)
            
        if max_size := os.getenv('AGENTSHROUD_MEMORY_MAX_SIZE'):
            config.lifecycle.memory_md_max_size = int(max_size)
            
        if check_interval := os.getenv('AGENTSHROUD_MEMORY_CHECK_INTERVAL'):
            config.integrity.check_interval = int(check_interval)
            
        if base_dir := os.getenv('AGENTSHROUD_WORKSPACE_DIR'):
            config.base_directory = Path(base_dir)
            
        # Enable/disable flags
        config.integrity.enabled = os.getenv('AGENTSHROUD_MEMORY_INTEGRITY_ENABLED', 'true').lower() == 'true'
        config.lifecycle.enabled = os.getenv('AGENTSHROUD_MEMORY_LIFECYCLE_ENABLED', 'true').lower() == 'true'
        config.lifecycle.pii_scanning_enabled = os.getenv('AGENTSHROUD_MEMORY_PII_SCAN_ENABLED', 'true').lower() == 'true'
        config.lifecycle.injection_scanning_enabled = os.getenv('AGENTSHROUD_MEMORY_INJECTION_SCAN_ENABLED', 'true').lower() == 'true'
        
        return config
