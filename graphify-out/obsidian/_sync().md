---
source_file: "gateway/tests/test_sync_cve_registry_ghsa.py"
type: "code"
community: "Community 55"
location: "L41"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_55
---

# _sync()

## Connections
- [[._run()_2]] - `calls` [EXTRACTED]
- [[.registry()]] - `calls` [EXTRACTED]
- [[.test_403_without_token_still_raises()]] - `calls` [EXTRACTED]
- [[.test_agent_var_resolved_from_registry_dict()]] - `calls` [EXTRACTED]
- [[.test_append_on_unlocatable_list_exits_nonzero()]] - `calls` [EXTRACTED]
- [[.test_append_targets_correct_agent_list()]] - `calls` [EXTRACTED]
- [[.test_cvss_none_when_absent()]] - `calls` [EXTRACTED]
- [[.test_dedup_by_cve_id()]] - `calls` [EXTRACTED]
- [[.test_dedup_by_ghsa_id()]] - `calls` [EXTRACTED]
- [[.test_dry_run_reports_count_and_writes_nothing()]] - `calls` [EXTRACTED]
- [[.test_dry_run_writes_nothing()]] - `calls` [EXTRACTED]
- [[.test_duplicate_within_same_feed_page_registered_once()]] - `calls` [EXTRACTED]
- [[.test_edit_that_does_not_add_n_entries_is_rejected()]] - `calls` [EXTRACTED]
- [[.test_empty_input_is_a_no_op()]] - `calls` [EXTRACTED]
- [[.test_entry_to_py_handles_none_cvss()]] - `calls` [EXTRACTED]
- [[.test_entry_to_py_roundtrips()]] - `calls` [EXTRACTED]
- [[.test_every_agent_list_accepts_an_append()]] - `calls` [EXTRACTED]
- [[.test_feed_fetch_failure_is_not_reported_as_zero_new()]] - `calls` [EXTRACTED]
- [[.test_fetch_paginates_via_link_cursor()]] - `calls` [EXTRACTED]
- [[.test_hermes_snapshot_zero_new()]] - `calls` [EXTRACTED]
- [[.test_id_numbering_continues_from_max()]] - `calls` [EXTRACTED]
- [[.test_idempotent_on_rerun()]] - `calls` [EXTRACTED]
- [[.test_insert_adds_exactly_n_entries_and_still_parses()]] - `calls` [EXTRACTED]
- [[.test_known_cves_matched_by_cve_id_not_id()]] - `calls` [EXTRACTED]
- [[.test_live_registry_is_idempotent_no_new_backlog()]] - `calls` [EXTRACTED]
- [[.test_main_exits_nonzero_when_an_agent_fails()]] - `calls` [EXTRACTED]
- [[.test_missing_variable_raises()]] - `calls` [EXTRACTED]
- [[.test_never_fabricates_ids_skips_advisory_without_ghsa()]] - `calls` [EXTRACTED]
- [[.test_new_advisory_becomes_under_review()]] - `calls` [EXTRACTED]
- [[.test_non_list_value_raises()]] - `calls` [EXTRACTED]
- [[.test_nvd_layout_failure_exits_nonzero()]] - `calls` [EXTRACTED]
- [[.test_openclaw_advisory_does_not_touch_hermes_registry()]] - `calls` [EXTRACTED]
- [[.test_openclaw_and_hermes_lists_each_get_their_own_entry()]] - `calls` [EXTRACTED]
- [[.test_openclaw_snapshot_registers_backlog_as_under_review()]] - `calls` [EXTRACTED]
- [[.test_other_http_errors_are_not_retried()]] - `calls` [EXTRACTED]
- [[.test_per_agent_prefix_applied()]] - `calls` [EXTRACTED]
- [[.test_persistent_failure_exits_non_zero()]] - `calls` [EXTRACTED]
- [[.test_string_literals_match_black_quote_preference()]] - `calls` [EXTRACTED]
- [[.test_token_refused_retries_public_endpoint_without_token()]] - `calls` [EXTRACTED]
- [[.test_transient_read_timeout_is_retried()]] - `calls` [EXTRACTED]
- [[test_sync_cve_registry_ghsa.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_55