---
type: community
members: 30
---

# test_playback_state.c

**Members:** 30 nodes

## Members
- [[_on_vg_state()]] - code - firmware/voice-terminal/main/app_main.c
- [[delivery_resume_offset()]] - code - firmware/voice-terminal/main/playback_logic.h
- [[delivery_track_sent_ok()]] - code - firmware/voice-terminal/main/playback_logic.h
- [[face_set_state()]] - code - firmware/voice-terminal/test/test_playback_state/test_playback_state.c
- [[face_state_t]] - code
- [[main()_28]] - code - firmware/voice-terminal/test/test_playback_state/test_playback_state.c
- [[playback_gate_should_open()]] - code - firmware/voice-terminal/main/playback_logic.h
- [[playback_logic.h]] - code - firmware/voice-terminal/main/playback_logic.h
- [[playback_step()]] - code - firmware/voice-terminal/test/test_playback_state/test_playback_state.c
- [[reset_all()]] - code - firmware/voice-terminal/test/test_playback_state/test_playback_state.c
- [[test_drain_clears_playing_and_returns_idle()]] - code - firmware/voice-terminal/test/test_playback_state/test_playback_state.c
- [[test_drain_keeps_face_off_idle_when_retriggered()]] - code - firmware/voice-terminal/test/test_playback_state/test_playback_state.c
- [[test_gate_open_sets_speaking_and_tts_playing()]] - code - firmware/voice-terminal/test/test_playback_state/test_playback_state.c
- [[test_gate_opens_on_20s_age()]] - code - firmware/voice-terminal/test/test_playback_state/test_playback_state.c
- [[test_gate_opens_on_768kb_cap()]] - code - firmware/voice-terminal/test/test_playback_state/test_playback_state.c
- [[test_gate_opens_on_reply_complete()]] - code - firmware/voice-terminal/test/test_playback_state/test_playback_state.c
- [[test_gate_stays_closed_before_any_cap()]] - code - firmware/voice-terminal/test/test_playback_state/test_playback_state.c
- [[test_gate_stays_closed_leaves_state_idle()]] - code - firmware/voice-terminal/test/test_playback_state/test_playback_state.c
- [[test_playback_state.c]] - code - firmware/voice-terminal/test/test_playback_state/test_playback_state.c
- [[test_resume_offset_first_attempt_is_zero()]] - code - firmware/voice-terminal/test/test_playback_state/test_playback_state.c
- [[test_resume_offset_rewinds_8kb()]] - code - firmware/voice-terminal/test/test_playback_state/test_playback_state.c
- [[test_track_sent_ok_is_monotonic()]] - code - firmware/voice-terminal/test/test_playback_state/test_playback_state.c
- [[tts_task()]] - code - firmware/voice-terminal/main/app_main.c
- [[vt_agent_count()_2]] - code - firmware/voice-terminal/test/test_playback_state/test_playback_state.c
- [[vt_remote_log()_2]] - code - firmware/voice-terminal/test/test_playback_state/test_playback_state.c
- [[wakeword_set_tts_playing()]] - code - firmware/voice-terminal/main/wakeword.c
- [[wakeword_tts_playing()]] - code - firmware/voice-terminal/main/wakeword.c
- [[wakeword_tts_stop_clear()]] - code - firmware/voice-terminal/main/wakeword.c
- [[wakeword_tts_stop_requested()]] - code - firmware/voice-terminal/main/wakeword.c
- [[ws_vg_state_t_1]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_playback_statec
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_wakeword.c]]
- 8 edges to [[_COMMUNITY_app_main.c]]
- 3 edges to [[_COMMUNITY_ws_client.c]]
- 1 edge to [[_COMMUNITY_main.rs]]

## Top bridge nodes
- [[tts_task()]] - degree 9, connects to 2 communities
- [[wakeword_tts_playing()]] - degree 8, connects to 2 communities
- [[_on_vg_state()]] - degree 6, connects to 2 communities
- [[wakeword_tts_stop_requested()]] - degree 6, connects to 2 communities
- [[test_playback_state.c]] - degree 19, connects to 1 community
