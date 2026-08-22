---
source_file: "gateway/tests/test_mfa_guard.py"
type: "code"
community: "Mfa Guard"
location: "L34"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Mfa_Guard
---

# _ref_totp()

## Connections
- [[test_decide_mfa_enabled_replayed_code_denied()]] - `calls` [EXTRACTED]
- [[test_decide_mfa_enabled_valid_code_approves()]] - `calls` [EXTRACTED]
- [[test_enhanced_decide_valid_code_approves()]] - `calls` [EXTRACTED]
- [[test_enhanced_tool_call_critical_allowed_with_mfa()]] - `calls` [EXTRACTED]
- [[test_enhanced_tool_call_high_allowed_with_mfa()]] - `calls` [EXTRACTED]
- [[test_expired_window_code_denies()]] - `calls` [EXTRACTED]
- [[test_from_env_reads_secret_and_flag()]] - `calls` [EXTRACTED]
- [[test_from_env_reads_secret_file()]] - `calls` [EXTRACTED]
- [[test_from_env_unreadable_secret_file()]] - `calls` [EXTRACTED]
- [[test_mfa_guard.py]] - `contains` [EXTRACTED]
- [[test_prune_used_drops_stale_entries()]] - `calls` [EXTRACTED]
- [[test_real_time_default_now()]] - `calls` [EXTRACTED]
- [[test_replayed_code_denies()]] - `calls` [EXTRACTED]
- [[test_uses_constant_time_compare()]] - `calls` [EXTRACTED]
- [[test_valid_totp_allows_high_risk()]] - `calls` [EXTRACTED]
- [[test_valid_totp_prev_window_allowed()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Mfa_Guard