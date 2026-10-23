---
source_file: "firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c"
type: "code"
community: "test_security_toolchain.py (2)"
location: "L151"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/test_security_toolchainpy_2
---

# test_ptt_finish_noop_when_idle()

## Connections
- [[main()_16]] - `calls` [EXTRACTED]
- [[test_ptt_state.c]] - `contains` [EXTRACTED]
- [[wakeword_clear()]] - `calls` [INFERRED]
- [[wakeword_ended()]] - `calls` [INFERRED]
- [[wakeword_ptt_finish()]] - `calls` [INFERRED]
- [[wakeword_triggered()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/test_security_toolchainpy_2
