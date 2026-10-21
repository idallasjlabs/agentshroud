---
type: community
members: 33
---

# AgentShroud v0.7.0 Enforcement Audit Results

**Members:** 33 nodes

## Members
- [[1Password bootstrap credentials never auto-resolved]] - rationale - docker/setup-secrets.sh
- [[Credential backend cascade (Keychain → secret-tool → 1Password → file)]] - rationale - docker/setup-secrets.sh
- [[S6 setup-secrets.sh read_secret_masked routes display output to devtty]] - concept - tests/startup_smoke/test_bot_boot_static.sh
- [[SECRET_DEFS]] - code - docker/setup-secrets.sh
- [[SS13SS14 behavioural test of write_secret_file]] - concept - tests/startup_smoke/test_setup_secrets.sh
- [[Static assertions SS1-SS12 on setup-secrets.sh]] - concept - tests/startup_smoke/test_setup_secrets.sh
- [[check]] - code - tests/startup_smoke/test_setup_secrets.sh
- [[cmd_dump_op_refs]] - code - docker/setup-secrets.sh
- [[cmd_extract]] - code - docker/setup-secrets.sh
- [[cmd_help]] - code - docker/setup-secrets.sh
- [[cmd_interactive]] - code - docker/setup-secrets.sh
- [[cmd_migrate]] - code - docker/setup-secrets.sh
- [[cmd_store]] - code - docker/setup-secrets.sh
- [[detect_backend]] - code - docker/setup-secrets.sh
- [[ensure_keychain]] - code - docker/setup-secrets.sh
- [[generate_gateway_password]] - code - docker/setup-secrets.sh
- [[get_secret]] - code - docker/setup-secrets.sh
- [[has]] - code - tests/startup_smoke/test_setup_secrets.sh
- [[has_in_section]] - code - tests/startup_smoke/test_setup_secrets.sh
- [[keychain_get]] - code - docker/setup-secrets.sh
- [[keychain_store]] - code - docker/setup-secrets.sh
- [[normalize_secret]] - code - docker/setup-secrets.sh
- [[op_get]] - code - docker/setup-secrets.sh
- [[op_ref_for]] - code - docker/setup-secrets.sh
- [[read_secret_masked]] - code - docker/setup-secrets.sh
- [[read_secret_plain]] - code - docker/setup-secrets.sh
- [[secret_matches_bot_filter]] - code - docker/setup-secrets.sh
- [[setup-secrets.sh]] - code - docker/setup-secrets.sh
- [[setup-secrets.sh script]] - code - docker/setup-secrets.sh
- [[store_secret]] - code - docker/setup-secrets.sh
- [[test_setup_secrets.sh]] - code - tests/startup_smoke/test_setup_secrets.sh
- [[test_setup_secrets.sh script]] - code - tests/startup_smoke/test_setup_secrets.sh
- [[write_secret_file]] - code - docker/setup-secrets.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentShroud_v070_Enforcement_Audit_Results
SORT file.name ASC
```

## Connections to other communities
- 1 edge to [[_COMMUNITY_export-bot-conversations.py]]
- 1 edge to [[_COMMUNITY_telegram_api_proxy (telegram-api{path})]]

## Top bridge nodes
- [[op_ref_for]] - degree 5, connects to 2 communities
