---
source_file: "firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c"
type: "code"
community: "A2AGovernanceProxy"
location: "L101"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/A2AGovernanceProxy
---

# test_clear_allows_fresh_tap()

## Connections
- [[do_tap()]] - `calls` [EXTRACTED]
- [[main()_10]] - `calls` [EXTRACTED]
- [[test_ptt_state.c]] - `contains` [EXTRACTED]
- [[wakeword_clear()]] - `calls` [INFERRED]
- [[wakeword_ended()]] - `calls` [INFERRED]
- [[wakeword_ptt_finish()]] - `calls` [INFERRED]
- [[wakeword_triggered()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/A2AGovernanceProxy