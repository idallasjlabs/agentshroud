---
source_file: "gateway/tests/test_round2_hardening.py"
type: "code"
community: "PII Sanitizer & Resource Guard"
location: "L13"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/PII_Sanitizer__Resource_Guard
---

# TestResourceGuardFailClosed

## Connections
- [[.test_check_cpu_limit_returns_false_on_exception()]] - `method` [EXTRACTED]
- [[.test_check_disk_write_limit_returns_false_on_exception()]] - `method` [EXTRACTED]
- [[.test_check_memory_limit_returns_false_on_exception()]] - `method` [EXTRACTED]
- [[EgressFilterConfig]] - `uses` [INFERRED]
- [[EnvironmentGuard]] - `uses` [INFERRED]
- [[FileSandboxConfig]] - `uses` [INFERRED]
- [[GitGuard]] - `uses` [INFERRED]
- [[ResourceGuard]] - `uses` [INFERRED]
- [[TelegramAPIProxy]] - `uses` [INFERRED]
- [[Verify resource check methods return False (deny) on exception.]] - `rationale_for` [EXTRACTED]
- [[test_round2_hardening.py]] - `contains` [EXTRACTED]

#graphify/code #graphify/INFERRED #community/PII_Sanitizer__Resource_Guard