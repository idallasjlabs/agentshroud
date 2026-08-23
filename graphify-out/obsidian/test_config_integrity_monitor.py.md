---
source_file: "gateway/tests/test_config_integrity_monitor.py"
type: "code"
community: "Config Integrity Monitor"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Config_Integrity_Monitor
---

# test_config_integrity_monitor.py

## Connections
- [[ConfigIntegrityMonitor]] - `imports` [EXTRACTED]
- [[_write_openclaw()]] - `contains` [EXTRACTED]
- [[dirs()]] - `contains` [EXTRACTED]
- [[test_added_file_is_detected()]] - `contains` [EXTRACTED]
- [[test_baseline_advances_only_when_clean()]] - `contains` [EXTRACTED]
- [[test_first_boot_establishes_baseline_without_alerts()]] - `contains` [EXTRACTED]
- [[test_format_alert_text_handles_missing_hashes()]] - `contains` [EXTRACTED]
- [[test_format_alert_text_includes_event_and_hash_prefixes()]] - `contains` [EXTRACTED]
- [[test_hash_file_is_stable_and_content_sensitive()]] - `contains` [EXTRACTED]
- [[test_hash_file_returns_none_for_missing()]] - `contains` [EXTRACTED]
- [[test_load_baseline_missing_file_returns_empty()]] - `contains` [EXTRACTED]
- [[test_load_baseline_tolerates_corrupt_json()]] - `contains` [EXTRACTED]
- [[test_modified_file_is_detected()]] - `contains` [EXTRACTED]
- [[test_removed_file_is_detected()]] - `contains` [EXTRACTED]
- [[test_reset_baseline_accepts_current_state()]] - `contains` [EXTRACTED]
- [[test_tamper_baseline_is_not_advanced_so_alert_refires()]] - `contains` [EXTRACTED]
- [[test_unchanged_second_run_reports_no_changes()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Config_Integrity_Monitor