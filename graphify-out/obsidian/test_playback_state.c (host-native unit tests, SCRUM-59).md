---
source_file: "firmware/voice-terminal/test/test_playback_state/test_playback_state.c"
type: "code"
community: "Playback State (test_playback_state)"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Playback_State_test_playback_state
---

# test_playback_state.c (host-native unit tests, SCRUM-59)

## Connections
- [[delivery_resume_offset()]] - `calls` [EXTRACTED]
- [[delivery_track_sent_ok()]] - `calls` [EXTRACTED]
- [[playback_logic.h (pure END-gateresume math, extracted for host testing)]] - `references` [EXTRACTED]
- [[stubsaudio.h (host-test stub replacing audio.h constants)]] - `references` [EXTRACTED]
- [[wakeword.c (PTT + WakeNet trigger)]] - `references` [EXTRACTED]
- [[wakeword_ptt_press()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Playback_State_test_playback_state