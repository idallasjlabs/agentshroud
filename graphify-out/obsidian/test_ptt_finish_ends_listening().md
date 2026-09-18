---
source_file: "firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c"
type: "code"
community: "test_ptt_state.c"
location: "L81"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/test_ptt_statec
---

# test_ptt_finish_ends_listening()

## Connections
- [[do_tap()]] - `calls` [EXTRACTED]
- [[main()_21]] - `calls` [EXTRACTED]
- [[test_ptt_state.c]] - `contains` [EXTRACTED]
- [[wakeword_clear()]] - `calls` [INFERRED]
- [[wakeword_ended()]] - `calls` [INFERRED]
- [[wakeword_ptt_finish]] - `calls` [INFERRED]
- [[wakeword_triggered()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/test_ptt_statec