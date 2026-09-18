---
type: community
cohesion: 0.23
members: 21
---

# test_ptt_state.c

**Cohesion:** 0.23 - loosely connected
**Members:** 21 nodes

## Members
- [[audio.h stub (wakeword PTT test)]] - code - firmware/voice-terminal/test/test_wakeword_state/stubs/audio.h
- [[bspesp-bsp.h stub (wakeword PTT test)]] - code - firmware/voice-terminal/test/test_wakeword_state/stubs/bsp/esp-bsp.h
- [[do_tap()]] - code - firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c
- [[esp_err.h stub (wakeword PTT test)]] - code - firmware/voice-terminal/test/test_wakeword_state/stubs/esp_err.h
- [[esp_log.h stub (wakeword PTT test)]] - code - firmware/voice-terminal/test/test_wakeword_state/stubs/esp_log.h
- [[freertosFreeRTOS.h stub (wakeword PTT test)]] - code - firmware/voice-terminal/test/test_wakeword_state/stubs/freertos/FreeRTOS.h
- [[freertostask.h stub (wakeword PTT test)]] - code - firmware/voice-terminal/test/test_wakeword_state/stubs/freertos/task.h
- [[iot_button.h stub (wakeword PTT test)]] - code - firmware/voice-terminal/test/test_wakeword_state/stubs/iot_button.h
- [[main()_21]] - code - firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c
- [[test_clear_allows_fresh_tap()]] - code - firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c
- [[test_ptt_finish_ends_listening()]] - code - firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c
- [[test_ptt_finish_noop_when_idle()]] - code - firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c
- [[test_ptt_state.c]] - code - firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c
- [[test_push_frame_suppressed_while_triggered()]] - code - firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c
- [[test_tap_in_idle_starts_listen()]] - code - firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c
- [[test_vad_timeout_fires_without_audio()]] - code - firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c
- [[vt_agent_count()_1]] - code - firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c
- [[vt_remote_log()_1]] - code - firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c
- [[wakeword_clear()]] - code - firmware/voice-terminal/main/wakeword.c
- [[wakeword_ended()]] - code - firmware/voice-terminal/main/wakeword.c
- [[wakeword_triggered()]] - code - firmware/voice-terminal/main/wakeword.c

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_ptt_statec
SORT file.name ASC
```

## Connections to other communities
- 13 edges to [[_COMMUNITY_wakeword.c]]
- 4 edges to [[_COMMUNITY_voice_task]]
- 4 edges to [[_COMMUNITY_test_playback_state.c]]
- 2 edges to [[_COMMUNITY_app_main.c]]

## Top bridge nodes
- [[wakeword_triggered()]] - degree 16, connects to 4 communities
- [[wakeword_clear()]] - degree 9, connects to 3 communities
- [[wakeword_ended()]] - degree 9, connects to 2 communities
- [[do_tap()]] - degree 8, connects to 1 community
- [[test_clear_allows_fresh_tap()]] - degree 7, connects to 1 community