---
source_file: "firmware/voice-terminal/main/app_main.c"
type: "code"
community: "Ws Client (main)"
location: "L688"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Ws_Client_main
---

# voice_task()

## Connections
- [[_build_ws_url()]] - `calls` [EXTRACTED]
- [[_deliver_utterance()]] - `calls` [EXTRACTED]
- [[_send_status_beacon()]] - `calls` [EXTRACTED]
- [[app_main.c]] - `contains` [EXTRACTED]
- [[audio_capture_frame()]] - `calls` [EXTRACTED]
- [[ui_face_set_agent()]] - `calls` [EXTRACTED]
- [[ui_face_set_state()]] - `calls` [EXTRACTED]
- [[vt_remote_log()]] - `calls` [EXTRACTED]
- [[wakeword_agent_index()]] - `calls` [INFERRED]
- [[wakeword_agent_switch_ack()]] - `calls` [INFERRED]
- [[wakeword_agent_switch_pending()]] - `calls` [INFERRED]
- [[wakeword_clear()]] - `calls` [INFERRED]
- [[wakeword_ended()]] - `calls` [INFERRED]
- [[wakeword_feed_bytes()]] - `calls` [INFERRED]
- [[wakeword_next_agent()]] - `calls` [AMBIGUOUS]
- [[wakeword_ptt_finish()]] - `calls` [INFERRED]
- [[wakeword_push_frame()]] - `calls` [INFERRED]
- [[wakeword_push_frame() — AFE feed + VAD endpointing]] - `calls` [EXTRACTED]
- [[wakeword_tick()]] - `calls` [INFERRED]
- [[wakeword_triggered()]] - `calls` [INFERRED]
- [[wakeword_tts_playing()]] - `calls` [INFERRED]
- [[wakeword_tts_stop_requested()]] - `calls` [INFERRED]
- [[ws_client_connected()]] - `calls` [INFERRED]
- [[ws_client_create()]] - `calls` [INFERRED]
- [[ws_client_create() — registers callbacks + starts client]] - `calls` [EXTRACTED]
- [[ws_client_destroy()]] - `calls` [INFERRED]
- [[ws_client_send_keepalive()]] - `calls` [INFERRED]
- [[ws_client_send_stop()]] - `calls` [INFERRED]
- [[ws_client_set_ctrl_cb()]] - `calls` [INFERRED]

#graphify/code #graphify/INFERRED #community/Ws_Client_main