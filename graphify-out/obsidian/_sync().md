---
source_file: "gateway/tests/test_sync_cve_registry_ghsa.py"
type: "code"
community: "Community 53"
location: "L41"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_53
---

# _sync()

## Connections
- [[.test_append_targets_correct_agent_marker()]] - `calls` [EXTRACTED]
- [[.test_cvss_none_when_absent()]] - `calls` [EXTRACTED]
- [[.test_dedup_by_cve_id()]] - `calls` [EXTRACTED]
- [[.test_dedup_by_ghsa_id()]] - `calls` [EXTRACTED]
- [[.test_dry_run_writes_nothing()]] - `calls` [EXTRACTED]
- [[.test_duplicate_within_same_feed_page_registered_once()]] - `calls` [EXTRACTED]
- [[.test_entry_to_py_handles_none_cvss()]] - `calls` [EXTRACTED]
- [[.test_entry_to_py_roundtrips()]] - `calls` [EXTRACTED]
- [[.test_fetch_paginates_via_link_cursor()]] - `calls` [EXTRACTED]
- [[.test_hermes_snapshot_zero_new()]] - `calls` [EXTRACTED]
- [[.test_id_numbering_continues_from_max()]] - `calls` [EXTRACTED]
- [[.test_idempotent_on_rerun()]] - `calls` [EXTRACTED]
- [[.test_live_registry_is_idempotent_no_new_backlog()]] - `calls` [EXTRACTED]
- [[.test_never_fabricates_ids_skips_advisory_without_ghsa()]] - `calls` [EXTRACTED]
- [[.test_new_advisory_becomes_under_review()]] - `calls` [EXTRACTED]
- [[.test_openclaw_advisory_does_not_touch_hermes_registry()]] - `calls` [EXTRACTED]
- [[.test_openclaw_snapshot_registers_backlog_as_under_review()]] - `calls` [EXTRACTED]
- [[.test_per_agent_prefix_applied()]] - `calls` [EXTRACTED]
- [[test_sync_cve_registry_ghsa.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_53