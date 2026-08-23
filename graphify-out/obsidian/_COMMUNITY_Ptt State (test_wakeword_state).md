---
type: community
cohesion: 0.19
members: 23
---

# Ptt State (test_wakeword_state)

**Cohesion:** 0.19 - loosely connected
**Members:** 23 nodes

## Members
- [[audio.h stub (wakeword PTT test)]] - code - firmware/voice-terminal/test/test_wakeword_state/stubs/audio.h
- [[bspesp-bsp.h stub (wakeword PTT test)]] - code - firmware/voice-terminal/test/test_wakeword_state/stubs/bsp/esp-bsp.h
- [[do_tap()]] - code - firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c
- [[esp_err.h stub (wakeword PTT test)]] - code - firmware/voice-terminal/test/test_wakeword_state/stubs/esp_err.h
- [[esp_log.h stub (wakeword PTT test)]] - code - firmware/voice-terminal/test/test_wakeword_state/stubs/esp_log.h
- [[freertosFreeRTOS.h stub (wakeword PTT test)]] - code - firmware/voice-terminal/test/test_wakeword_state/stubs/freertos/FreeRTOS.h
- [[freertostask.h stub (wakeword PTT test)]] - code - firmware/voice-terminal/test/test_wakeword_state/stubs/freertos/task.h
- [[iot_button.h stub (wakeword PTT test)]] - code - firmware/voice-terminal/test/test_wakeword_state/stubs/iot_button.h
- [[main()_9]] - code - firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c
- [[test_clear_allows_fresh_tap()]] - code - firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c
- [[test_ptt_finish_ends_listening()]] - code - firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c
- [[test_ptt_finish_noop_when_idle()]] - code - firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c
- [[test_ptt_state.c]] - code - firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c
- [[test_push_frame_suppressed_while_triggered()]] - code - firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c
- [[test_tap_in_idle_starts_listen()]] - code - firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c
- [[test_vad_timeout_fires_without_audio()]] - code - firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c
- [[vt_agent_count()_2]] - code - firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c
- [[vt_remote_log()_2]] - code - firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c
- [[wakeword_clear()]] - code - firmware/voice-terminal/main/wakeword.c
- [[wakeword_ended()]] - code - firmware/voice-terminal/main/wakeword.c
- [[wakeword_ptt_finish()]] - code - firmware/voice-terminal/main/wakeword.c
- [[wakeword_push_frame()]] - code - firmware/voice-terminal/main/wakeword.c
- [[wakeword_tick()]] - code - firmware/voice-terminal/main/wakeword.c

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Ptt_State_test_wakeword_state
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_Wakeword (main)]]
- 7 edges to [[_COMMUNITY_Playback State (test_playback_state)]]
- 5 edges to [[_COMMUNITY_Ws Client (main)]]
- 1 edge to [[_COMMUNITY_Main (src)]]

## Top bridge nodes
- [[wakeword_clear()]] - degree 9, connects to 3 communities
- [[wakeword_ended()]] - degree 8, connects to 2 communities
- [[wakeword_ptt_finish()]] - degree 6, connects to 2 communities
- [[wakeword_push_frame()]] - degree 3, connects to 2 communities
- [[wakeword_tick()]] - degree 3, connects to 2 communities