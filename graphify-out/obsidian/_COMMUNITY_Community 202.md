---
type: community
members: 34
---

# Community 202

**Members:** 34 nodes

## Members
- [[.__init__()_63]] - code - gateway/security/config_integrity.py
- [[._hash_file()]] - code - gateway/security/config_integrity.py
- [[._load_baseline()]] - code - gateway/security/config_integrity.py
- [[._save_baseline()]] - code - gateway/security/config_integrity.py
- [[.check()_2]] - code - gateway/security/config_integrity.py
- [[.format_alert_text()]] - code - gateway/security/config_integrity.py
- [[.reset_baseline()]] - code - gateway/security/config_integrity.py
- [[Accept current file hashes as the new baseline (owner-acknowledged rebuild).]] - rationale - gateway/security/config_integrity.py
- [[Compare current file hashes against baseline.          Returns a list of change]] - rationale - gateway/security/config_integrity.py
- [[Computes and verifies SHA256 hashes of monitored bot config files.      At gatew]] - rationale - gateway/security/config_integrity.py
- [[ConfigIntegrityMonitor]] - code - gateway/security/config_integrity.py
- [[Format Telegram alert text for detected config changes.]] - rationale - gateway/security/config_integrity.py
- [[Load the last known baseline from disk. Returns empty dict if not found.]] - rationale - gateway/security/config_integrity.py
- [[Path_10]] - code - gateway/security/config_integrity.py
- [[Persist the current hashes as the new baseline.]] - rationale - gateway/security/config_integrity.py
- [[Return (bot_config_dir, baseline_path) rooted in an isolated tmp dir.]] - rationale - gateway/tests/test_config_integrity_monitor.py
- [[Return hex SHA256 of a file, or None if the file does not exist.]] - rationale - gateway/security/config_integrity.py
- [[_write_openclaw()]] - code - gateway/tests/test_config_integrity_monitor.py
- [[dirs()]] - code - gateway/tests/test_config_integrity_monitor.py
- [[test_added_file_is_detected()]] - code - gateway/tests/test_config_integrity_monitor.py
- [[test_baseline_advances_only_when_clean()]] - code - gateway/tests/test_config_integrity_monitor.py
- [[test_config_integrity_monitor.py]] - code - gateway/tests/test_config_integrity_monitor.py
- [[test_first_boot_establishes_baseline_without_alerts()]] - code - gateway/tests/test_config_integrity_monitor.py
- [[test_format_alert_text_handles_missing_hashes()]] - code - gateway/tests/test_config_integrity_monitor.py
- [[test_format_alert_text_includes_event_and_hash_prefixes()]] - code - gateway/tests/test_config_integrity_monitor.py
- [[test_hash_file_is_stable_and_content_sensitive()]] - code - gateway/tests/test_config_integrity_monitor.py
- [[test_hash_file_returns_none_for_missing()]] - code - gateway/tests/test_config_integrity_monitor.py
- [[test_load_baseline_missing_file_returns_empty()]] - code - gateway/tests/test_config_integrity_monitor.py
- [[test_load_baseline_tolerates_corrupt_json()]] - code - gateway/tests/test_config_integrity_monitor.py
- [[test_modified_file_is_detected()]] - code - gateway/tests/test_config_integrity_monitor.py
- [[test_removed_file_is_detected()]] - code - gateway/tests/test_config_integrity_monitor.py
- [[test_reset_baseline_accepts_current_state()]] - code - gateway/tests/test_config_integrity_monitor.py
- [[test_tamper_baseline_is_not_advanced_so_alert_refires()]] - code - gateway/tests/test_config_integrity_monitor.py
- [[test_unchanged_second_run_reports_no_changes()]] - code - gateway/tests/test_config_integrity_monitor.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_202
SORT file.name ASC
```

## Connections to other communities
- 2 edges to [[_COMMUNITY_Community 6]]
- 1 edge to [[_COMMUNITY_Community 799]]

## Top bridge nodes
- [[ConfigIntegrityMonitor]] - degree 26, connects to 2 communities