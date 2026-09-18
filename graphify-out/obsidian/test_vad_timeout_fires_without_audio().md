---
source_file: "firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c"
type: "code"
community: "test_ptt_state.c"
location: "L128"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/test_ptt_statec
---

# test_vad_timeout_fires_without_audio()

## Connections
- [[do_tap()]] - `calls` [EXTRACTED]
- [[main()_21]] - `calls` [EXTRACTED]
- [[test_ptt_state.c]] - `contains` [EXTRACTED]
- [[wakeword_clear()]] - `calls` [INFERRED]
- [[wakeword_ended()]] - `calls` [INFERRED]
- [[wakeword_tick]] - `calls` [INFERRED]
- [[wakeword_triggered()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/test_ptt_statec