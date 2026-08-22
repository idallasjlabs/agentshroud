---
source_file: "firmware/voice-terminal/main/playback_logic.h"
type: "code"
community: "Playback State (test_playback_state)"
location: "L75"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Playback_State_test_playback_state
---

# delivery_resume_offset()

## Connections
- [[_deliver_utterance()]] - `calls` [EXTRACTED]
- [[playback_logic.h]] - `contains` [EXTRACTED]
- [[test_playback_state.c (host-native unit tests, SCRUM-59)]] - `calls` [EXTRACTED]
- [[test_resume_offset_first_attempt_is_zero()]] - `calls` [INFERRED]
- [[test_resume_offset_rewinds_8kb()]] - `calls` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Playback_State_test_playback_state