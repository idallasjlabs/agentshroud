---
type: community
cohesion: 0.16
members: 25
---

# voice_task

**Cohesion:** 0.16 - loosely connected
**Members:** 25 nodes

## Members
- [[_deliver_utterance()]] - code - firmware/voice-terminal/main/app_main.c
- [[_on_event()]] - code - firmware/voice-terminal/main/ws_client.c
- [[esp_err_t_1]] - code - firmware/voice-terminal/main/ws_client.c
- [[esp_event_base_t]] - code - firmware/voice-terminal/main/ws_client.c
- [[rlog_task()]] - code - firmware/voice-terminal/main/app_main.c
- [[voice_task()]] - code - firmware/voice-terminal/main/app_main.c
- [[wakeword_agent_index()]] - code - firmware/voice-terminal/main/wakeword.c
- [[wakeword_agent_switch_ack()]] - code - firmware/voice-terminal/main/wakeword.c
- [[wakeword_agent_switch_pending()]] - code - firmware/voice-terminal/main/wakeword.c
- [[wakeword_feed_bytes()]] - code - firmware/voice-terminal/main/wakeword.c
- [[ws_client.c]] - code - firmware/voice-terminal/main/ws_client.c
- [[ws_client_connected()]] - code - firmware/voice-terminal/main/ws_client.c
- [[ws_client_create()]] - code - firmware/voice-terminal/main/ws_client.c
- [[ws_client_destroy()]] - code - firmware/voice-terminal/main/ws_client.c
- [[ws_client_handle_t]] - code - firmware/voice-terminal/main/ws_client.c
- [[ws_client_send_end()]] - code - firmware/voice-terminal/main/ws_client.c
- [[ws_client_send_keepalive()]] - code - firmware/voice-terminal/main/ws_client.c
- [[ws_client_send_listen()]] - code - firmware/voice-terminal/main/ws_client.c
- [[ws_client_send_listen_resume()]] - code - firmware/voice-terminal/main/ws_client.c
- [[ws_client_send_log()]] - code - firmware/voice-terminal/main/ws_client.c
- [[ws_client_send_pcm()]] - code - firmware/voice-terminal/main/ws_client.c
- [[ws_client_send_stop()]] - code - firmware/voice-terminal/main/ws_client.c
- [[ws_ctrl_cb_t]] - code - firmware/voice-terminal/main/ws_client.c
- [[ws_pcm_cb_t]] - code - firmware/voice-terminal/main/ws_client.c
- [[ws_state_cb_t]] - code - firmware/voice-terminal/main/ws_client.c

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/voice_task
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_app_main.c]]
- 8 edges to [[_COMMUNITY_test_ptt_state.c]]
- 6 edges to [[_COMMUNITY_wakeword.c]]
- 5 edges to [[_COMMUNITY_test_playback_state.c]]

## Top bridge nodes
- [[voice_task()]] - degree 25, connects to 4 communities
- [[_deliver_utterance()]] - degree 10, connects to 2 communities
- [[rlog_task()]] - degree 4, connects to 2 communities
- [[ws_client.c]] - degree 12, connects to 1 community
- [[ws_client_create()]] - degree 7, connects to 1 community
