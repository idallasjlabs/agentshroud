---
source_file: "firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c"
type: "code"
community: "Ptt State (test_wakeword_state)"
location: "L151"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Ptt_State_test_wakeword_state
---

# test_ptt_finish_noop_when_idle()

## Connections
- [[main()_9]] - `calls` [EXTRACTED]
- [[test_ptt_state.c]] - `contains` [EXTRACTED]
- [[wakeword_clear()]] - `calls` [INFERRED]
- [[wakeword_ended()]] - `calls` [INFERRED]
- [[wakeword_ptt_finish()]] - `calls` [INFERRED]
- [[wakeword_triggered()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/Ptt_State_test_wakeword_state