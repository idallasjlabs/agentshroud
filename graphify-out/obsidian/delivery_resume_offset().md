---
source_file: "firmware/voice-terminal/main/playback_logic.h"
type: "code"
community: "test_playback_state.c"
location: "L75"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/test_playback_statec
---

# delivery_resume_offset()

## Connections
- [[playback_logic.h]] - `contains` [EXTRACTED]
- [[test_playback_state.c (host-native unit tests, SCRUM-59)]] - `calls` [EXTRACTED]
- [[test_resume_offset_first_attempt_is_zero()]] - `calls` [INFERRED]
- [[test_resume_offset_rewinds_8kb()]] - `calls` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/test_playback_statec