---
type: community
cohesion: 0.03
members: 138
---

# MemoryIntegrityMonitor

**Cohesion:** 0.03 - loosely connected
**Members:** 138 nodes

## Members
- [[dot-__init__()_66]] - code - gateway/security/memory_integrity.py
- [[dot-__init__()_67]] - code - gateway/security/memory_lifecycle.py
- [[dot-__post_init__()_3]] - code - gateway/security/memory_lifecycle.py
- [[dot-__post_init__()_4]] - code - gateway/security/memory_lifecycle.py
- [[dot-_cleanup_old_actions()]] - code - gateway/security/memory_lifecycle.py
- [[dot-_cleanup_old_threats()]] - code - gateway/security/memory_lifecycle.py
- [[dot-_compute_file_hash()]] - code - gateway/security/memory_integrity.py
- [[dot-_detect_modification_source()]] - code - gateway/security/memory_integrity.py
- [[dot-_is_in_write_window()]] - code - gateway/security/memory_integrity.py
- [[dot-_load_integrity_database()]] - code - gateway/security/memory_integrity.py
- [[dot-_load_write_windows()]] - code - gateway/security/memory_integrity.py
- [[dot-_save_integrity_database()]] - code - gateway/security/memory_integrity.py
- [[dot-_save_write_windows()]] - code - gateway/security/memory_integrity.py
- [[dot-archive_file()]] - code - gateway/security/memory_lifecycle.py
- [[dot-clear_old_alerts()]] - code - gateway/security/memory_integrity.py
- [[dot-enforce_daily_notes_retention()]] - code - gateway/security/memory_lifecycle.py
- [[dot-enforce_memory_md_size_limit()]] - code - gateway/security/memory_lifecycle.py
- [[dot-from_dict()_2]] - code - gateway/security/memory_integrity.py
- [[dot-get_integrity_status()]] - code - gateway/security/memory_integrity.py
- [[dot-get_lifecycle_status()]] - code - gateway/security/memory_lifecycle.py
- [[dot-get_recent_actions()]] - code - gateway/security/memory_lifecycle.py
- [[dot-get_recent_alerts()]] - code - gateway/security/memory_integrity.py
- [[dot-get_recent_threats()]] - code - gateway/security/memory_lifecycle.py
- [[dot-register_expected_write()]] - code - gateway/security/memory_integrity.py
- [[dot-run_lifecycle_maintenance()]] - code - gateway/security/memory_lifecycle.py
- [[dot-sanitize_content()]] - code - gateway/security/memory_lifecycle.py
- [[dot-scan_all_monitored_files()]] - code - gateway/security/memory_integrity.py
- [[dot-scan_content_for_threats()]] - code - gateway/security/memory_lifecycle.py
- [[dot-scan_file()]] - code - gateway/security/memory_integrity.py
- [[dot-setup_method()_6]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-setup_method()_7]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-setup_method()_8]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-teardown_method()_2]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-teardown_method()_3]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-teardown_method()_4]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_config_from_env()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_content_sanitization()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_daily_notes_retention()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_default_config()_2]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_expected_write_window()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_file_monitoring_new_file()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_hash_computation()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_integrated_memory_protection()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_integrity_database_persistence()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_lifecycle_maintenance()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_memory_md_size_limit()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_memory_write_validation()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_pii_detection()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_prompt_injection_detection()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_status_reporting()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_tampering_detection()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-test_threat_cleanup()]] - code - gateway/tests/test_memory_lifecycle.py
- [[dot-to_dict()_4]] - code - gateway/security/memory_integrity.py
- [[dot-validate_memory_write()]] - code - gateway/security/memory_lifecycle.py
- [[Action taken during retention policy enforcement.]] - rationale - gateway/security/memory_lifecycle.py
- [[Any_19]] - code - gateway/security/memory_integrity.py
- [[Any_20]] - code - gateway/security/memory_lifecycle.py
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
- [[MemoryIntegrityConfig]] - code - gateway/security/memory_integrity.py
- [[MemoryIntegrityConfig_1]] - code - gateway/security/memory_config.py
- [[MemoryIntegrityMonitor]] - code - gateway/security/memory_integrity.py
- [[MemoryLifecycleConfig]] - code - gateway/security/memory_lifecycle.py
- [[MemoryLifecycleConfig_1]] - code - gateway/security/memory_config.py
- [[MemoryLifecycleManager]] - code - gateway/security/memory_lifecycle.py
- [[ModificationSource]] - code - gateway/security/memory_integrity.py
- [[Monitors integrity of critical memory files.]] - rationale - gateway/security/memory_integrity.py
- [[Path_16]] - code - gateway/security/memory_integrity.py
- [[Path_17]] - code - gateway/security/memory_lifecycle.py
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
- [[Test default configuration values.]] - rationale - gateway/tests/test_memory_lifecycle.py
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
TABLE source_file, type FROM #community/MemoryIntegrityMonitor
SORT file.name ASC
```

## Connections to other communities
- 27 edges to [[_COMMUNITY_Any]]
- 4 edges to [[_COMMUNITY_MiddlewareManager]]
- 4 edges to [[_COMMUNITY_Enum]]
- 1 edge to [[_COMMUNITY_Skill MCP Doctor (MCPM-DOCTOR)]]

## Top bridge nodes
- [[MemoryIntegrityMonitor]] - degree 39, connects to 2 communities
- [[MemoryLifecycleManager]] - degree 37, connects to 2 communities
- [[memory_lifecycle.py]] - degree 7, connects to 2 communities
- [[TestMemoryLifecycleManager]] - degree 20, connects to 1 community
- [[TestMemoryIntegrityMonitor]] - degree 17, connects to 1 community
