---
source_file: "gateway/security/context_guard.py"
type: "code"
community: "Session Manager & PII/Context Guard"
location: "L128"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Session_Manager__PII/Context_Guard
---

# .analyze_message()

## Connections
- [[dot-_detect_hidden_instructions()]] - `calls` [EXTRACTED]
- [[dot-_detect_instruction_injection()]] - `calls` [EXTRACTED]
- [[dot-_detect_rapid_context_growth()]] - `calls` [EXTRACTED]
- [[dot-_detect_repetition_attacks()]] - `calls` [EXTRACTED]
- [[dot-should_block_message()]] - `calls` [EXTRACTED]
- [[Analyze a message for context poisoning attempts.          Args             ses]] - `rationale_for` [EXTRACTED]
- [[ContextAttack]] - `references` [EXTRACTED]
- [[ContextGuard]] - `method` [EXTRACTED]
- [[SessionContext]] - `calls` [EXTRACTED]
- [[check_message()]] - `calls` [EXTRACTED]
- [[deque]] - `calls` [INFERRED]
- [[normalize_input()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Session_Manager__PII/Context_Guard