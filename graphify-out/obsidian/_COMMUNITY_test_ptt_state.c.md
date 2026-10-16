---
type: community
cohesion: 0.17
members: 26
---

# test_ptt_state.c

**Cohesion:** 0.17 - loosely connected
**Members:** 26 nodes

## Members
- [[_send_status_beacon()]] - code - firmware/voice-terminal/main/app_main.c
- [[audio.h stub (wakeword PTT test)]] - code - firmware/voice-terminal/test/test_wakeword_state/stubs/audio.h
- [[bspesp-bsp.h stub (wakeword PTT test)]] - code - firmware/voice-terminal/test/test_wakeword_state/stubs/bsp/esp-bsp.h
- [[do_tap()]] - code - firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c
- [[esp_err.h stub (wakeword PTT test)]] - code - firmware/voice-terminal/test/test_wakeword_state/stubs/esp_err.h
- [[esp_log.h stub (wakeword PTT test)]] - code - firmware/voice-terminal/test/test_wakeword_state/stubs/esp_log.h
- [[freertosFreeRTOS.h stub (wakeword PTT test)]] - code - firmware/voice-terminal/test/test_wakeword_state/stubs/freertos/FreeRTOS.h
- [[freertostask.h stub (wakeword PTT test)]] - code - firmware/voice-terminal/test/test_wakeword_state/stubs/freertos/task.h
- [[iot_button.h stub (wakeword PTT test)]] - code - firmware/voice-terminal/test/test_wakeword_state/stubs/iot_button.h
- [[main()_16]] - code - firmware/voice-terminal/test/test_wakeword_state/test_ptt_state.c
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
- [[wakeword_ptt_finish()]] - code - firmware/voice-terminal/main/wakeword.c
- [[wakeword_push_frame()]] - code - firmware/voice-terminal/main/wakeword.c
- [[wakeword_tick()]] - code - firmware/voice-terminal/main/wakeword.c
- [[wakeword_triggered()]] - code - firmware/voice-terminal/main/wakeword.c
- [[ws_client_handle_t]] - code - firmware/voice-terminal/main/app_main.c

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/test_ptt_statec
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_wakeword.c]]
- 8 edges to [[_COMMUNITY_voice_task]]
- 5 edges to [[_COMMUNITY_test_playback_state.c]]
- 1 edge to [[_COMMUNITY_app_main.c]]

## Top bridge nodes
- [[wakeword_triggered()]] - degree 15, connects to 3 communities
- [[wakeword_clear()]] - degree 9, connects to 3 communities
- [[wakeword_ended()]] - degree 9, connects to 2 communities
- [[wakeword_ptt_finish()]] - degree 6, connects to 2 communities
- [[_send_status_beacon()]] - degree 5, connects to 2 communities
