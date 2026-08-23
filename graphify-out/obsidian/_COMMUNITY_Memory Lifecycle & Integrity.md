---
type: community
cohesion: 0.03
members: 138
---

# Memory Lifecycle & Integrity

**Cohesion:** 0.03 - loosely connected
**Members:** 138 nodes

## Members
- [[.__init__()_95]] - code - gateway/security/memory_integrity.py
- [[.__init__()_96]] - code - gateway/security/memory_lifecycle.py
- [[.__post_init__()_6]] - code - gateway/security/memory_lifecycle.py
- [[.__post_init__()_7]] - code - gateway/security/memory_lifecycle.py
- [[._cleanup_old_actions()]] - code - gateway/security/memory_lifecycle.py
- [[._cleanup_old_threats()]] - code - gateway/security/memory_lifecycle.py
- [[._compute_file_hash()]] - code - gateway/security/memory_integrity.py
- [[._detect_modification_source()]] - code - gateway/security/memory_integrity.py
- [[._is_in_write_window()]] - code - gateway/security/memory_integrity.py
- [[._load_integrity_database()]] - code - gateway/security/memory_integrity.py
- [[._load_write_windows()]] - code - gateway/security/memory_integrity.py
- [[._save_integrity_database()]] - code - gateway/security/memory_integrity.py
- [[._save_write_windows()]] - code - gateway/security/memory_integrity.py
- [[.archive_file()]] - code - gateway/security/memory_lifecycle.py
- [[.clear_old_alerts()]] - code - gateway/security/memory_integrity.py
- [[.enforce_daily_notes_retention()]] - code - gateway/security/memory_lifecycle.py
- [[.enforce_memory_md_size_limit()]] - code - gateway/security/memory_lifecycle.py
- [[.from_dict()_8]] - code - gateway/security/memory_integrity.py
- [[.get_integrity_status()]] - code - gateway/security/memory_integrity.py
- [[.get_lifecycle_status()]] - code - gateway/security/memory_lifecycle.py
- [[.get_recent_actions()]] - code - gateway/security/memory_lifecycle.py
- [[.get_recent_alerts()]] - code - gateway/security/memory_integrity.py
- [[.get_recent_threats()]] - code - gateway/security/memory_lifecycle.py
- [[.register_expected_write()]] - code - gateway/security/memory_integrity.py
- [[.run_lifecycle_maintenance()]] - code - gateway/security/memory_lifecycle.py
- [[.sanitize_content()]] - code - gateway/security/memory_lifecycle.py
- [[.scan_all_monitored_files()]] - code - gateway/security/memory_integrity.py
- [[.scan_content_for_threats()]] - code - gateway/security/memory_lifecycle.py
- [[.scan_file()]] - code - gateway/security/memory_integrity.py
- [[.setup_method()_9]] - code - gateway/tests/test_memory_lifecycle.py
- [[.setup_method()_10]] - code - gateway/tests/test_memory_lifecycle.py
- [[.setup_method()_11]] - code - gateway/tests/test_memory_lifecycle.py
- [[.teardown_method()_1]] - code - gateway/tests/test_memory_lifecycle.py
- [[.teardown_method()_2]] - code - gateway/tests/test_memory_lifecycle.py
- [[.teardown_method()_3]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_config_from_env()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_content_sanitization()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_daily_notes_retention()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_default_config()_4]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_expected_write_window()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_file_monitoring_new_file()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_hash_computation()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_integrated_memory_protection()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_integrity_database_persistence()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_lifecycle_maintenance()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_memory_md_size_limit()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_memory_write_validation()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_pii_detection()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_prompt_injection_detection()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_status_reporting()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_tampering_detection()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.test_threat_cleanup()]] - code - gateway/tests/test_memory_lifecycle.py
- [[.to_dict()_11]] - code - gateway/security/memory_integrity.py
- [[.validate_memory_write()]] - code - gateway/security/memory_lifecycle.py
- [[Action taken during retention policy enforcement.]] - rationale - gateway/security/memory_lifecycle.py
- [[Any_48]] - code - gateway/security/memory_integrity.py
- [[Any_49]] - code - gateway/security/memory_lifecycle.py
- [[Archive a file to the archive directory.]] - rationale - gateway/security/memory_lifecycle.py
- [[Attempt to detect the source of a file modification.          Detection strategy]] - rationale - gateway/security/memory_integrity.py
- [[Check if a file is currently in a write grace window.]] - rationale - gateway/security/memory_integrity.py
- [[Clean up integration test environment.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Clean up old retention action records.]] - rationale - gateway/security/memory_lifecycle.py
- [[Clean up old threat records.]] - rationale - gateway/security/memory_lifecycle.py
- [[Clean up test environment.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Clear alerts older than N days.]] - rationale - gateway/security/memory_integrity.py
- [[Compute SHA-256 hash of a file.]] - rationale - gateway/security/memory_integrity.py
- [[Configuration for memory file integrity monitoring.]] - rationale - gateway/security/memory_config.py
- [[Configuration for memory lifecycle management.]] - rationale - gateway/security/memory_config.py
- [[ContentThreat]] - code - gateway/security/memory_lifecycle.py
- [[ContentThreatType]] - code - gateway/security/memory_lifecycle.py
- [[Convert to dictionary for JSON serialization.]] - rationale - gateway/security/memory_integrity.py
- [[Create from dictionary for JSON deserialization.]] - rationale - gateway/security/memory_integrity.py
- [[Detected threat in memory file content.]] - rationale - gateway/security/memory_lifecycle.py
- [[Enforce retention policy for daily notes.]] - rationale - gateway/security/memory_lifecycle.py
- [[Enforce size limit for MEMORY.md file.]] - rationale - gateway/security/memory_lifecycle.py
- [[FileIntegrityRecord]] - code - gateway/security/memory_integrity.py
- [[Get alerts from the last N hours.]] - rationale - gateway/security/memory_integrity.py
- [[Get current integrity monitoring status.]] - rationale - gateway/security/memory_integrity.py
- [[Get current lifecycle management status.]] - rationale - gateway/security/memory_lifecycle.py
- [[Get retention actions taken in the last N hours.]] - rationale - gateway/security/memory_lifecycle.py
- [[Get threats detected in the last N hours.]] - rationale - gateway/security/memory_lifecycle.py
- [[Load active write windows from disk.]] - rationale - gateway/security/memory_integrity.py
- [[Load integrity database from disk.]] - rationale - gateway/security/memory_integrity.py
- [[Manages memory file lifecycle and content security.]] - rationale - gateway/security/memory_lifecycle.py
- [[MemoryIntegrityConfig_1]] - code - gateway/security/memory_integrity.py
- [[MemoryIntegrityConfig]] - code - gateway/security/memory_config.py
- [[MemoryIntegrityMonitor]] - code - gateway/security/memory_integrity.py
- [[MemoryLifecycleConfig_1]] - code - gateway/security/memory_lifecycle.py
- [[MemoryLifecycleConfig]] - code - gateway/security/memory_config.py
- [[MemoryLifecycleManager]] - code - gateway/security/memory_lifecycle.py
- [[ModificationSource]] - code - gateway/security/memory_integrity.py
- [[Monitors integrity of critical memory files.]] - rationale - gateway/security/memory_integrity.py
- [[Path_15]] - code - gateway/security/memory_integrity.py
- [[Path_16]] - code - gateway/security/memory_lifecycle.py
- [[Record of a file's integrity state.]] - rationale - gateway/security/memory_integrity.py
- [[Register an expected write to a file to prevent false alerts.]] - rationale - gateway/security/memory_integrity.py
- [[RetentionAction]] - code - gateway/security/memory_lifecycle.py
- [[Run all lifecycle maintenance tasks.]] - rationale - gateway/security/memory_lifecycle.py
- [[Sanitize content by removingredacting threats.]] - rationale - gateway/security/memory_lifecycle.py
- [[Save active write windows to disk.]] - rationale - gateway/security/memory_integrity.py
- [[Save integrity database to disk.]] - rationale - gateway/security/memory_integrity.py
- [[Scan a single file for integrity changes.]] - rationale - gateway/security/memory_integrity.py
- [[Scan all configured monitored files and directories.]] - rationale - gateway/security/memory_integrity.py
- [[Scan memory file content for security threats.]] - rationale - gateway/security/memory_lifecycle.py
- [[Set up integration test environment.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Set up test environment.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Source of a file modification.]] - rationale - gateway/security/memory_integrity.py
- [[Test MEMORY.md size limit enforcement.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test PII detection in memory content.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test cleanup of old threat records.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test complete lifecycle maintenance run.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test complete memory protection workflow.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test configuration from environment variables.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test content sanitization removes threats.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test default configuration values._3]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test detection of unauthorized modifications.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test file hash computation.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test integration of memory security components.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test integrity database saves and loads correctly.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test memory integrity configuration.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test memory integrity monitoring.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test memory lifecycle management.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test monitoring a new file.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test prompt injection detection.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test retention policy for daily notes.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test status reporting from both components.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test validation before writing to memory files.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[Test write grace window prevents false alerts.]] - rationale - gateway/tests/test_memory_lifecycle.py
- [[TestMemoryIntegrityConfig]] - code - gateway/tests/test_memory_lifecycle.py
- [[TestMemoryIntegrityMonitor]] - code - gateway/tests/test_memory_lifecycle.py
- [[TestMemoryLifecycleManager]] - code - gateway/tests/test_memory_lifecycle.py
- [[TestMemorySecurityIntegration]] - code - gateway/tests/test_memory_lifecycle.py
- [[Types of content threats detected in memory files.]] - rationale - gateway/security/memory_lifecycle.py
- [[Validate content before writing to memory file.]] - rationale - gateway/security/memory_lifecycle.py
- [[memory_config.py]] - code - gateway/security/memory_config.py
- [[memory_integrity.py]] - code - gateway/security/memory_integrity.py
- [[memory_lifecycle.py]] - code - gateway/security/memory_lifecycle.py
- [[test_memory_lifecycle.py]] - code - gateway/tests/test_memory_lifecycle.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Memory_Lifecycle__Integrity
SORT file.name ASC
```

## Connections to other communities
- 31 edges to [[_COMMUNITY_RBAC & Ingest Middleware]]
- 8 edges to [[_COMMUNITY_Security Audit & Watchtower Tests]]
- 5 edges to [[_COMMUNITY_Tool Chain & CVE Triage]]
- 1 edge to [[_COMMUNITY_Manifest (skills)]]

## Top bridge nodes
- [[MemoryIntegrityMonitor]] - degree 41, connects to 2 communities
- [[MemoryLifecycleManager]] - degree 39, connects to 2 communities
- [[memory_lifecycle.py]] - degree 7, connects to 2 communities
- [[TestMemoryLifecycleManager]] - degree 20, connects to 1 community
- [[MemoryIntegrityConfig]] - degree 18, connects to 1 community