---
source_file: "gateway/security/config_integrity.py"
type: "code"
community: "Community 214"
location: "L33"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_214
---

# ConfigIntegrityMonitor

## Connections
- [[.__init__()_63]] - `method` [EXTRACTED]
- [[._hash_file()]] - `method` [EXTRACTED]
- [[._load_baseline()]] - `method` [EXTRACTED]
- [[._save_baseline()]] - `method` [EXTRACTED]
- [[.check()_2]] - `method` [EXTRACTED]
- [[.format_alert_text()]] - `method` [EXTRACTED]
- [[.reset_baseline()]] - `method` [EXTRACTED]
- [[Computes and verifies SHA256 hashes of monitored bot config files.      At gatew]] - `rationale_for` [EXTRACTED]
- [[config_integrity.py]] - `contains` [EXTRACTED]
- [[lifespan()_1]] - `calls` [EXTRACTED]
- [[lifespan.py]] - `imports` [EXTRACTED]
- [[test_added_file_is_detected()]] - `calls` [EXTRACTED]
- [[test_baseline_advances_only_when_clean()]] - `calls` [EXTRACTED]
- [[test_config_integrity_monitor.py]] - `imports` [EXTRACTED]
- [[test_first_boot_establishes_baseline_without_alerts()]] - `calls` [EXTRACTED]
- [[test_format_alert_text_handles_missing_hashes()]] - `calls` [EXTRACTED]
- [[test_format_alert_text_includes_event_and_hash_prefixes()]] - `calls` [EXTRACTED]
- [[test_hash_file_is_stable_and_content_sensitive()]] - `calls` [EXTRACTED]
- [[test_hash_file_returns_none_for_missing()]] - `calls` [EXTRACTED]
- [[test_load_baseline_missing_file_returns_empty()]] - `calls` [EXTRACTED]
- [[test_load_baseline_tolerates_corrupt_json()]] - `calls` [EXTRACTED]
- [[test_modified_file_is_detected()]] - `calls` [EXTRACTED]
- [[test_removed_file_is_detected()]] - `calls` [EXTRACTED]
- [[test_reset_baseline_accepts_current_state()]] - `calls` [EXTRACTED]
- [[test_tamper_baseline_is_not_advanced_so_alert_refires()]] - `calls` [EXTRACTED]
- [[test_unchanged_second_run_reports_no_changes()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_214