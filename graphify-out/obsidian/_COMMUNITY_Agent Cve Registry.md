---
type: community
cohesion: 0.05
members: 62
---

# Agent Cve Registry

**Cohesion:** 0.05 - loosely connected
**Members:** 62 nodes

## Members
- [[7 app-level entries + 7 dependency-chain entries added 2026-07-31 after a     re]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[A real CVE always came from a GHSA advisory, so cve_id implies ghsa_id.]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[Any_30]] - code - gateway/security/agent_cve_registry.py
- [[CRITICAL GUARD no entry `id` may look like a real CVE id.      This is the load]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[Every `id` must be a zero-padded ASH-OCLAW-NNN  ASH-HERMES-NNN ref.]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[Hermes has no NATIVE GHSA advisory feed (nousresearchhermes-agent publishes]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[Return a summary of the advisory registry for the specified agent.      Counts a]] - rationale - gateway/security/agent_cve_registry.py
- [[Synthetic ids are unique and numbered 1..N in list order for each agent.]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[The first curated OpenClaw entry (Feishu media download) survives migration.]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[The migration produced a real (non-zero) verified GHSA match set.]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[_all_entries()]] - code - gateway/tests/test_agent_cve_registry.py
- [[_hermes_by_title()]] - code - gateway/tests/test_agent_cve_registry.py
- [[cve_id must be either None or a real-looking CVE id — never junk.]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[get_agent_cve_summary()]] - code - gateway/security/agent_cve_registry.py
- [[ghsacvepending counts must be internally consistent and honest.]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[ghsa_id must be either None or a real-looking GHSA id.]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[test_agent_cve_registries_contains_both()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_agent_cve_registries_objects_match_lists()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_agent_cve_registry.py]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_agent_cve_registry_alias_is_openclaw_list()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_agent_cve_registry_alias_nonempty()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_ash_ids_are_unique_and_stable_order()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_cve_id_field_only_holds_real_looking_cve_ids()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_default_summary_equals_openclaw_summary()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_default_summary_wrapped_agent_openclaw()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_empty_bot_id_raises_key_error()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_entry_with_cve_id_also_has_ghsa_id()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_every_entry_id_is_synthetic_ash_ref()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_ghsa_id_field_only_holds_real_looking_ghsa_ids()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_all_cves_have_required_fields()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_all_cvss_are_numeric()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_all_defense_layers_are_lists()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_all_required_titles_present()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_all_severities_valid()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_all_statuses_valid()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_auth_entries_use_gateway_auth_gate()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_by_severity_totals_match()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_by_status_totals_match()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_command_injection_high_severity()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_cve_registry_public_alias()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_summary_count_is_fourteen()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_summary_count_matches_registry()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_summary_cves_is_hermes_list()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_summary_keys()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_summary_wrapped_agent_is_hermes()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_symlink_entry_upstream_fix()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_verified_ids_are_never_fabricated()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_wechat_adapter_fully_mitigated()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_no_entry_id_looks_like_a_cve()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_openclaw_all_cves_have_required_fields()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_openclaw_all_severities_valid()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_openclaw_all_statuses_valid()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_openclaw_by_severity_totals_match()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_openclaw_by_status_totals_match()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_openclaw_first_entry_is_feishu_media_download()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_openclaw_has_some_confident_ghsa_matches()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_openclaw_match_counts_are_consistent()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_openclaw_summary_count_matches_registry()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_openclaw_summary_cves_is_openclaw_list()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_openclaw_summary_keys()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_unknown_bot_id_raises_key_error()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_wrapped_agent_constant_unchanged()]] - code - gateway/tests/test_agent_cve_registry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Agent_Cve_Registry
SORT file.name ASC
```

## Connections to other communities
- 7 edges to [[_COMMUNITY_Generate Cve Page (scripts)]]
- 1 edge to [[_COMMUNITY_SOC Router (Collaborator Mgmt)]]
- 1 edge to [[_COMMUNITY_Soc Bots]]

## Top bridge nodes
- [[get_agent_cve_summary()]] - degree 27, connects to 3 communities
- [[test_agent_cve_registry.py]] - degree 52, connects to 1 community