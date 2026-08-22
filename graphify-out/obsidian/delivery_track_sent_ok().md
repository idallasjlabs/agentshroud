---
source_file: "firmware/voice-terminal/main/playback_logic.h"
type: "code"
community: "Playback State (test_playback_state)"
location: "L96"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Playback_State_test_playback_state
---

# delivery_track_sent_ok()

## Connections
- [[_deliver_utterance()]] - `calls` [EXTRACTED]
- [[playback_logic.h]] - `contains` [EXTRACTED]
- [[test_playback_state.c (host-native unit tests, SCRUM-59)]] - `calls` [EXTRACTED]
- [[test_track_sent_ok_is_monotonic()]] - `calls` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/Playback_State_test_playback_state