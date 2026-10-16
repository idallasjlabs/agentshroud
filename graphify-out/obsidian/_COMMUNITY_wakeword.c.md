---
type: community
cohesion: 0.11
members: 29
---

# wakeword.c

**Cohesion:** 0.11 - loosely connected
**Members:** 29 nodes

## Members
- [[_agent_btn_pressed()]] - code - firmware/voice-terminal/main/wakeword.c
- [[_apply_agent_cb()]] - code - firmware/voice-terminal/main/ui_face.c
- [[_apply_state_cb()]] - code - firmware/voice-terminal/main/ui_face.c
- [[_btn_pressed()]] - code - firmware/voice-terminal/main/wakeword.c
- [[_btn_released()]] - code - firmware/voice-terminal/main/wakeword.c
- [[_find_canvas()]] - code - firmware/voice-terminal/main/ui_face.c
- [[_ptt_end()]] - code - firmware/voice-terminal/main/wakeword.c
- [[_ptt_start()]] - code - firmware/voice-terminal/main/wakeword.c
- [[_report_and_place_canvas()]] - code - firmware/voice-terminal/main/ui_face.c
- [[_state_to_emotion()]] - code - firmware/voice-terminal/main/ui_face.c
- [[_touch_pressed()]] - code - firmware/voice-terminal/main/ui_face.c
- [[_touch_start_only()]] - code - firmware/voice-terminal/main/ui_face.c
- [[esp_err_t_6]] - code - firmware/voice-terminal/main/wakeword.c
- [[face_animation_pause()]] - code - firmware/voice-terminal/components/lvgl_kawaii_face/lvgl_kawaii_face.c
- [[face_emotion_t_1]] - code - firmware/voice-terminal/main/ui_face.c
- [[lv_event_t]] - code - firmware/voice-terminal/main/ui_face.c
- [[lv_obj_t_1]] - code - firmware/voice-terminal/main/ui_face.c
- [[remote_log.h]] - code - firmware/voice-terminal/main/remote_log.h
- [[ui_face.c]] - code - firmware/voice-terminal/main/ui_face.c
- [[ui_face_init()]] - code - firmware/voice-terminal/main/ui_face.c
- [[ui_face_set_state()]] - code - firmware/voice-terminal/main/ui_face.c
- [[wakeword.c]] - code - firmware/voice-terminal/main/wakeword.c
- [[wakeword_deinit()]] - code - firmware/voice-terminal/main/wakeword.c
- [[wakeword_init()]] - code - firmware/voice-terminal/main/wakeword.c
- [[wakeword_next_agent()]] - code - firmware/voice-terminal/main/wakeword.c
- [[wakeword_ptt_press()]] - code - firmware/voice-terminal/main/wakeword.c
- [[wakeword_ptt_release()]] - code - firmware/voice-terminal/main/wakeword.c
- [[wakeword_tts_stop_request()]] - code - firmware/voice-terminal/main/wakeword.c
- [[ws_vg_state_t_1]] - code - firmware/voice-terminal/main/ui_face.c

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/wakewordc
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_test_ptt_state.c]]
- 7 edges to [[_COMMUNITY_test_playback_state.c]]
- 6 edges to [[_COMMUNITY_voice_task]]
- 5 edges to [[_COMMUNITY_lvgl_kawaii_face.c]]
- 5 edges to [[_COMMUNITY_app_main.c]]

## Top bridge nodes
- [[wakeword.c]] - degree 26, connects to 3 communities
- [[ui_face_set_state()]] - degree 6, connects to 3 communities
- [[_touch_pressed()]] - degree 10, connects to 2 communities
- [[wakeword_ptt_press()]] - degree 6, connects to 2 communities
- [[ui_face_init()]] - degree 5, connects to 2 communities
