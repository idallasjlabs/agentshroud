---
type: community
cohesion: 0.10
members: 32
---

# app_main.c

**Cohesion:** 0.10 - loosely connected
**Members:** 32 nodes

## Members
- [[_apply_agent_cb]] - code - firmware/voice-terminal/main/ui_face.c
- [[_apply_state_cb]] - code - firmware/voice-terminal/main/ui_face.c
- [[_build_ws_url]] - code - firmware/voice-terminal/main/app_main.c
- [[_find_canvas]] - code - firmware/voice-terminal/main/ui_face.c
- [[_lvgl_flush_wait_yield()]] - code - firmware/voice-terminal/main/app_main.c
- [[_on_tts_pcm]] - code - firmware/voice-terminal/main/app_main.c
- [[_on_vg_state]] - code - firmware/voice-terminal/main/app_main.c
- [[_on_ws_ctrl]] - code - firmware/voice-terminal/main/app_main.c
- [[_report_and_place_canvas]] - code - firmware/voice-terminal/main/ui_face.c
- [[_state_to_emotion]] - code - firmware/voice-terminal/main/ui_face.c
- [[app_main]] - code - firmware/voice-terminal/main/app_main.c
- [[app_main.c]] - code - firmware/voice-terminal/main/app_main.c
- [[esp_err_t_3]] - code
- [[esp_event_base_t]] - code
- [[face_emotion_t]] - code
- [[lv_display_t]] - code
- [[lv_obj_t]] - code
- [[tts_task]] - code - firmware/voice-terminal/main/app_main.c
- [[ui_face.c]] - code - firmware/voice-terminal/main/ui_face.c
- [[ui_face_init]] - code - firmware/voice-terminal/main/ui_face.c
- [[ui_face_set_agent]] - code - firmware/voice-terminal/main/ui_face.c
- [[ui_face_set_state]] - code - firmware/voice-terminal/main/ui_face.c
- [[ui_init (WiFi status labels)]] - code - firmware/voice-terminal/main/app_main.c
- [[ui_state_t]] - code
- [[ui_update()]] - code - firmware/voice-terminal/main/app_main.c
- [[wakeword_init]] - code - firmware/voice-terminal/main/wakeword.c
- [[wakeword_tts_stop_requested()]] - code - firmware/voice-terminal/main/wakeword.c
- [[wifi_event_handler]] - code - firmware/voice-terminal/main/app_main.c
- [[wifi_init]] - code - firmware/voice-terminal/main/app_main.c
- [[ws_client.h]] - code - firmware/voice-terminal/main/ws_client.h
- [[ws_vg_state_t]] - code
- [[ws_vg_state_t_1]] - code

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/app_mainc
SORT file.name ASC
```

## Connections to other communities
- 11 edges to [[_COMMUNITY_wakeword.c]]
- 10 edges to [[_COMMUNITY_voice_task]]
- 4 edges to [[_COMMUNITY_test_playback_state.c]]
- 2 edges to [[_COMMUNITY_test_ptt_state.c]]

## Top bridge nodes
- [[wakeword_tts_stop_requested()]] - degree 6, connects to 3 communities
- [[app_main.c]] - degree 20, connects to 2 communities
- [[_on_vg_state]] - degree 6, connects to 2 communities
- [[tts_task]] - degree 6, connects to 2 communities
- [[ui_face.c]] - degree 13, connects to 1 community