---
source_file: "gateway/tests/test_clamav_pipeline.py"
type: "code"
community: "Community 220"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_220
---

# test_clamav_pipeline.py

## Connections
- [[PipelineAction]] - `imports` [EXTRACTED]
- [[SecurityPipeline]] - `imports` [EXTRACTED]
- [[_b64_payload()]] - `contains` [EXTRACTED]
- [[_instant_wait_for()]] - `contains` [EXTRACTED]
- [[_make_pipeline()]] - `contains` [EXTRACTED]
- [[_run_capture()]] - `contains` [EXTRACTED]
- [[_timeout_wait_for()]] - `contains` [EXTRACTED]
- [[clamav_scanner.py]] - `imports_from` [EXTRACTED]
- [[clamd_sock_path()]] - `contains` [EXTRACTED]
- [[scan_bytes()]] - `imports` [EXTRACTED]
- [[test_apt_repo_signatures_are_verified()]] - `contains` [EXTRACTED]
- [[test_clamav_comes_from_proposed_updates_and_nothing_else_does()]] - `contains` [EXTRACTED]
- [[test_clamd_available_false_for_stale_socket_left_by_killed_daemon()]] - `contains` [EXTRACTED]
- [[test_clamd_available_false_when_socket_missing()]] - `contains` [EXTRACTED]
- [[test_clamd_available_true_when_daemon_listening()]] - `contains` [EXTRACTED]
- [[test_clamd_socket_constant_matches_both_images_clamd_conf()]] - `contains` [EXTRACTED]
- [[test_gateway_upgrades_pip_past_the_vendored_certifi_advisory()]] - `contains` [EXTRACTED]
- [[test_pipeline_clamav_clean_payload()]] - `contains` [EXTRACTED]
- [[test_pipeline_clamav_error_fail_open()]] - `contains` [EXTRACTED]
- [[test_pipeline_clamav_malware_blocked()]] - `contains` [EXTRACTED]
- [[test_pipeline_clamav_not_configured()]] - `contains` [EXTRACTED]
- [[test_pipeline_short_base64_not_scanned()]] - `contains` [EXTRACTED]
- [[test_preferred_scan_binary_falls_back_when_daemon_dead()]] - `contains` [EXTRACTED]
- [[test_preferred_scan_binary_uses_daemon_when_listening()]] - `contains` [EXTRACTED]
- [[test_run_clamscan_clamdscan_command_has_no_clamscan_only_flags()]] - `contains` [EXTRACTED]
- [[test_run_clamscan_clamscan_command_unchanged()]] - `contains` [EXTRACTED]
- [[test_scan_bytes_binary_not_found()]] - `contains` [EXTRACTED]
- [[test_scan_bytes_clean()]] - `contains` [EXTRACTED]
- [[test_scan_bytes_empty_input()]] - `contains` [EXTRACTED]
- [[test_scan_bytes_infected()]] - `contains` [EXTRACTED]
- [[test_scan_bytes_timeout()]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_220