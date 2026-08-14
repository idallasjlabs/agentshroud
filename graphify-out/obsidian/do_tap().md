---
source_file: "firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c"
type: "code"
community: "Gateway Test Suite"
location: "L58"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Test_Suite
---

# do_tap()

## Connections
- [[test_clear_allows_fresh_tap()]] - `calls` [EXTRACTED]
- [[test_ptt_finish_ends_listening()]] - `calls` [EXTRACTED]
- [[test_ptt_state.c]] - `contains` [EXTRACTED]
- [[test_push_frame_suppressed_while_triggered()]] - `calls` [EXTRACTED]
- [[test_tap_in_idle_starts_listen()]] - `calls` [EXTRACTED]
- [[test_vad_timeout_fires_without_audio()]] - `calls` [EXTRACTED]
- [[wakeword_ptt_press()]] - `calls` [INFERRED]
- [[wakeword_ptt_release()]] - `calls` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Test_Suite