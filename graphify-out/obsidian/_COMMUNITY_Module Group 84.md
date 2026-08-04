---
type: community
cohesion: 0.06
members: 47
---

# Module Group 84

**Cohesion:** 0.06 - loosely connected
**Members:** 47 nodes

## Members
- [[AGENT_CVE_REGISTRY must be the exact same object as _OPENCLAW_CVE_REGISTRY.]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[Any_26]] - code - gateway/security/agent_cve_registry.py
- [[CVE-2026-22171 is the first manually curated OpenClaw entry; verify it exists.]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[Calling with no args must produce the same result as bot_id='openclaw'.]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[HERMES_CVE_REGISTRY public alias must be non-empty and match private list.]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[Hermes registry must contain exactly the 7 CVEs specified in M1.]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[Public AGENT_CVE_REGISTRY alias still exposes the OpenClaw list.]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[Return a summary of the CVE registry for the specified agent.      Args]] - rationale - gateway/security/agent_cve_registry.py
- [[WRAPPED_AGENT must remain 'OpenClaw' for downstream consumers.]] - rationale - gateway/tests/test_agent_cve_registry.py
- [[get_agent_cve_summary()]] - code - gateway/security/agent_cve_registry.py
- [[test_agent_cve_registries_contains_both()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_agent_cve_registries_objects_match_lists()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_agent_cve_registry.py]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_agent_cve_registry_alias_is_openclaw_list()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_agent_cve_registry_alias_nonempty()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_default_summary_equals_openclaw_summary()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_default_summary_wrapped_agent_openclaw()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_empty_bot_id_raises_key_error()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_7112_and_7113_gateway_auth_gate()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_7396_fully_mitigated()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_7397_fully_mitigated_with_upstream_fix()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_9367_high_severity_fully_mitigated()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_all_cves_have_required_fields()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_all_cvss_are_numeric()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_all_defense_layers_are_lists()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_all_required_ids_present()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_all_severities_valid()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_all_statuses_valid()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_by_severity_totals_match()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_by_status_totals_match()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_cve_registry_public_alias()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_summary_count_is_seven()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_summary_count_matches_registry()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_summary_cves_is_hermes_list()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_summary_keys()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_hermes_summary_wrapped_agent_is_hermes()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_openclaw_all_cves_have_required_fields()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_openclaw_all_severities_valid()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_openclaw_all_statuses_valid()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_openclaw_by_severity_totals_match()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_openclaw_by_status_totals_match()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_openclaw_cve_22171_present()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_openclaw_summary_count_matches_registry()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_openclaw_summary_cves_is_openclaw_list()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_openclaw_summary_keys()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_unknown_bot_id_raises_key_error()]] - code - gateway/tests/test_agent_cve_registry.py
- [[test_wrapped_agent_constant_unchanged()]] - code - gateway/tests/test_agent_cve_registry.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_84
SORT file.name ASC
```

## Connections to other communities
- 6 edges to [[_COMMUNITY_Module Group 251]]
- 1 edge to [[_COMMUNITY_SOC Router & Correlation]]
- 1 edge to [[_COMMUNITY_SOC Bots & CVE Management]]

## Top bridge nodes
- [[get_agent_cve_summary()]] - degree 25, connects to 3 communities
- [[test_agent_cve_registry.py]] - degree 40, connects to 1 community
