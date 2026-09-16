---
source_file: ".claude/settings.json"
type: "code"
community: "Community 304"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Community_304
---

# .claude/settings.json (hook + permission wiring)

## Connections
- [[auto_format_python.sh (PostToolUse hook)]] - `references` [EXTRACTED]
- [[block_credential_read.sh (PreToolUse hook)]] - `shares_data_with` [INFERRED]
- [[block_credential_write.sh (PreToolUse hook)]] - `references` [EXTRACTED]
- [[block_main_commits.sh (PreToolUse hook)]] - `references` [EXTRACTED]
- [[remind_proposal_review.sh (PostToolUse hook)]] - `references` [EXTRACTED]
- [[require_impact_analysis.sh (PreToolUse hook, referenced)]] - `references` [EXTRACTED]
- [[run_targeted_tests.sh (PostToolUse hook)]] - `references` [EXTRACTED]
- [[warn_dangerous_bash.sh (PreToolUse hook)]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Community_304