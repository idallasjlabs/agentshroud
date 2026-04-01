# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Memory Integrity Monitor - R-18 Implementation

Protects against memory poisoning attacks by monitoring file integrity using SHA-256 hashes.
Detects unauthorized modifications to critical memory files and tracks modification sources.
"""

import hashlib
import json
import logging
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Optional, Set, Tuple, Any
from enum import Enum
from dataclasses import dataclass, asdict

from gateway.security.memory_config import MemorySecurityConfig, MemoryIntegrityConfig


logger = logging.getLogger(__name__)


class ModificationSource(Enum):
    """Source of a file modification."""
    AGENT = 'agent'
    HUMAN = 'human'  
    UNKNOWN = 'unknown'
    SYSTEM = 'system'


@dataclass
class FileIntegrityRecord:
    """Record of a file's integrity state."""
    file_path: str
    hash_sha256: str
    size: int
    last_modified: float
    last_check: float
    modification_source: ModificationSource
    is_protected: bool = False
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for JSON serialization."""
        result = asdict(self)
        result['modification_source'] = self.modification_source.value
        return result
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'FileIntegrityRecord':
        """Create from dictionary for JSON deserialization."""
        data['modification_source'] = ModificationSource(data['modification_source'])
        return cls(**data)


class MemoryIntegrityMonitor:
    """Monitors integrity of critical memory files."""
    
    def __init__(self, config: MemoryIntegrityConfig, base_directory: Path):
        self.config = config
        self.base_directory = base_directory
        self.integrity_db_path = base_directory / '.agentshroud' / 'memory_integrity.json'
        self.write_window_db_path = base_directory / '.agentshroud' / 'write_windows.json'
        
        # In-memory tracking
        self.file_records: Dict[str, FileIntegrityRecord] = {}
        self.active_write_windows: Dict[str, float] = {}  # file -> end_time
        self.modification_alerts: List[Dict[str, Any]] = []
        
        # Ensure directories exist
        self.integrity_db_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Load existing data
        self._load_integrity_database()
        self._load_write_windows()
        
    def _compute_file_hash(self, file_path: Path) -> Optional[str]:
        """Compute SHA-256 hash of a file."""
        try:
            if not file_path.exists():
                return None
                
            hasher = hashlib.sha256()
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(8192), b''):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except Exception as e:
            logger.error(f"Failed to compute hash for {file_path}: {e}")
            return None
    
    def _load_integrity_database(self):
        """Load integrity database from disk."""
        try:
            if self.integrity_db_path.exists():
                with open(self.integrity_db_path, 'r') as f:
                    data = json.load(f)
                    for path, record_data in data.get('records', {}).items():
                        self.file_records[path] = FileIntegrityRecord.from_dict(record_data)
                        
                    self.modification_alerts = data.get('alerts', [])
        except Exception as e:
            logger.error(f"Failed to load integrity database: {e}")
    
    def _save_integrity_database(self):
        """Save integrity database to disk."""
        try:
            data = {
                'records': {path: record.to_dict() for path, record in self.file_records.items()},
                'alerts': self.modification_alerts,
                'last_updated': time.time()
            }
            with open(self.integrity_db_path, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save integrity database: {e}")
    
    def _load_write_windows(self):
        """Load active write windows from disk."""
        try:
            if self.write_window_db_path.exists():
                with open(self.write_window_db_path, 'r') as f:
                    data = json.load(f)
                    current_time = time.time()
                    # Only load windows that haven't expired
                    self.active_write_windows = {
                        path: end_time for path, end_time in data.items()
                        if end_time > current_time
                    }
        except Exception as e:
            logger.error(f"Failed to load write windows: {e}")
    
    def _save_write_windows(self):
        """Save active write windows to disk."""
        try:
            with open(self.write_window_db_path, 'w') as f:
                json.dump(self.active_write_windows, f, indent=2)
        except Exception as e:
            logger.error(f"Failed to save write windows: {e}")
    
    def register_expected_write(self, file_path: str, source: ModificationSource = ModificationSource.AGENT):
        """Register an expected write to a file to prevent false alerts."""
        end_time = time.time() + self.config.write_grace_period
        self.active_write_windows[file_path] = end_time
        self._save_write_windows()
        logger.debug(f"Registered expected write for {file_path} from {source.value}")
    
    def _is_in_write_window(self, file_path: str) -> bool:
        """Check if a file is currently in a write grace window."""
        current_time = time.time()
        end_time = self.active_write_windows.get(file_path)
        
        if end_time and end_time > current_time:
            return True
            
        # Clean up expired windows
        if end_time and end_time <= current_time:
            del self.active_write_windows[file_path]
            self._save_write_windows()
            
        return False
    
    def _detect_modification_source(self, file_path: Path) -> ModificationSource:
        """Attempt to detect the source of a file modification.

        Detection strategy (in priority order):
        1. Explicit write windows registered by the agent — highest confidence.
        2. Inode change time (ctime) vs modification time (mtime): if ctime is
           very recent but mtime is older, a metadata-only change (e.g. chmod)
           was made externally — classify as HUMAN.
        3. mtime within the last 5 seconds — likely in-flight agent write.
        4. Fallback to UNKNOWN.
        """
        # Priority 1: Explicit write window registered by agent
        if self._is_in_write_window(str(file_path)):
            return ModificationSource.AGENT

        try:
            stat = file_path.stat()
            now = time.time()

            # Priority 2: ctime much newer than mtime → external metadata change
            if hasattr(stat, "st_ctime"):
                ctime_age = now - stat.st_ctime
                mtime_age = now - stat.st_mtime
                if ctime_age < 5 and mtime_age > 60:
                    # Metadata changed recently but content is old → human/system action
                    return ModificationSource.HUMAN

            # Priority 3: Very recent mtime — likely in-flight agent write
            if now - stat.st_mtime < 5:
                return ModificationSource.AGENT

            return ModificationSource.UNKNOWN

        except Exception:
            return ModificationSource.UNKNOWN
    
    def scan_file(self, file_path: Path) -> Optional[FileIntegrityRecord]:
        """Scan a single file for integrity changes."""
        try:
            if not file_path.exists():
                # File was deleted
                path_str = str(file_path.relative_to(self.base_directory))
                if path_str in self.file_records:
                    logger.warning(f"Monitored file deleted: {path_str}")
                    del self.file_records[path_str]
                    self._save_integrity_database()
                return None
            
            path_str = str(file_path.relative_to(self.base_directory))
            current_hash = self._compute_file_hash(file_path)
            if not current_hash:
                return None
                
            stat = file_path.stat()
            current_time = time.time()
            is_protected = file_path.name in self.config.protected_files
            
            existing_record = self.file_records.get(path_str)
            
            if existing_record:
                # Check for modifications
                if existing_record.hash_sha256 != current_hash:
                    source = self._detect_modification_source(file_path)
                    
                    # Alert on unauthorized modifications
                    if is_protected and source != ModificationSource.HUMAN:
                        alert = {
                            'timestamp': current_time,
                            'file_path': path_str,
                            'alert_type': 'protected_file_modified',
                            'old_hash': existing_record.hash_sha256,
                            'new_hash': current_hash,
                            'suspected_source': source.value,
                            'severity': 'HIGH'
                        }
                        self.modification_alerts.append(alert)
                        logger.critical(f"SECURITY ALERT: Protected file {path_str} was modified by {source.value}")
                    
                    elif not self._is_in_write_window(path_str):
                        alert = {
                            'timestamp': current_time,
                            'file_path': path_str,
                            'alert_type': 'unexpected_modification',
                            'old_hash': existing_record.hash_sha256,
                            'new_hash': current_hash,
                            'suspected_source': source.value,
                            'severity': 'MEDIUM' if is_protected else 'LOW'
                        }
                        self.modification_alerts.append(alert)
                        logger.warning(f"Unexpected modification to {path_str} by {source.value}")
                    
                    # Update record
                    record = FileIntegrityRecord(
                        file_path=path_str,
                        hash_sha256=current_hash,
                        size=stat.st_size,
                        last_modified=stat.st_mtime,
                        last_check=current_time,
                        modification_source=source,
                        is_protected=is_protected
                    )
                else:
                    # No changes, just update check time
                    record = existing_record
                    record.last_check = current_time
            else:
                # New file
                source = self._detect_modification_source(file_path)
                record = FileIntegrityRecord(
                    file_path=path_str,
                    hash_sha256=current_hash,
                    size=stat.st_size,
                    last_modified=stat.st_mtime,
                    last_check=current_time,
                    modification_source=source,
                    is_protected=is_protected
                )
                logger.info(f"Started monitoring new file: {path_str}")
            
            self.file_records[path_str] = record
            return record
            
        except Exception as e:
            logger.error(f"Failed to scan file {file_path}: {e}")
            return None
    
    def scan_all_monitored_files(self):
        """Scan all configured monitored files and directories."""
        if not self.config.enabled:
            return
            
        logger.debug("Starting memory integrity scan")
        
        # Scan individual monitored files
        for filename in self.config.monitored_files:
            file_path = self.base_directory / filename
            self.scan_file(file_path)
        
        # Scan protected files
        for filename in self.config.protected_files:
            file_path = self.base_directory / filename
            self.scan_file(file_path)
        
        # Scan monitored directories
        for dirname in self.config.monitored_directories:
            dir_path = self.base_directory / dirname
            if dir_path.exists() and dir_path.is_dir():
                for file_path in dir_path.rglob('*.md'):
                    self.scan_file(file_path)
        
        self._save_integrity_database()
        logger.debug("Completed memory integrity scan")
    
    def get_recent_alerts(self, hours: int = 24) -> List[Dict[str, Any]]:
        """Get alerts from the last N hours."""
        cutoff_time = time.time() - (hours * 3600)
        return [alert for alert in self.modification_alerts if alert['timestamp'] > cutoff_time]
    
    def clear_old_alerts(self, days: int = 7):
        """Clear alerts older than N days."""
        cutoff_time = time.time() - (days * 24 * 3600)
        original_count = len(self.modification_alerts)
        self.modification_alerts = [
            alert for alert in self.modification_alerts 
            if alert['timestamp'] > cutoff_time
        ]
        cleared_count = original_count - len(self.modification_alerts)
        if cleared_count > 0:
            logger.info(f"Cleared {cleared_count} old integrity alerts")
            self._save_integrity_database()
    
    def get_integrity_status(self) -> Dict[str, Any]:
        """Get current integrity monitoring status."""
        recent_alerts = self.get_recent_alerts()
        high_severity_alerts = [a for a in recent_alerts if a.get('severity') == 'HIGH']
        
        return {
            'enabled': self.config.enabled,
            'monitored_files': len(self.file_records),
            'recent_alerts_24h': len(recent_alerts),
            'high_severity_alerts_24h': len(high_severity_alerts),
            'active_write_windows': len(self.active_write_windows),
            'last_scan': max([r.last_check for r in self.file_records.values()], default=0)
        }
