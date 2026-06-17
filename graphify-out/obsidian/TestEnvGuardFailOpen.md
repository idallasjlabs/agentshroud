---
source_file: "gateway/tests/test_round2_hardening.py"
type: "code"
community: "Environment Guard & Leak Detection"
location: "L107"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Environment_Guard__Leak_Detection
---

# TestEnvGuardFailOpen

## Connections
- [[.test_natural_language_question_is_allowed()]] - `method` [EXTRACTED]
- [[.test_unparseable_text_is_allowed()]] - `method` [EXTRACTED]
- [[EgressFilterConfig]] - `uses` [INFERRED]
- [[EnvironmentGuard]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[GitGuard]] - `uses` [INFERRED]
- [[ResourceGuard]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[test_round2_hardening.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/Environment_Guard__Leak_Detection