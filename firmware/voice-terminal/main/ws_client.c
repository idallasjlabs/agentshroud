#include "ws_client.h"
#include <string.h>
#include <stdlib.h>
#include "cJSON.h"
#include "remote_log.h"   /* vt_remote_log only ENQUEUES — safe from ws task */
#include "esp_log.h"
#include "esp_websocket_client.h"
#include "esp_crt_bundle.h"
#include "freertos/FreeRTOS.h"
#include "freertos/semphr.h"

static const char *TAG = "ws_client";

struct ws_client {
    esp_websocket_client_handle_t wsc;
    ws_state_cb_t  state_cb;
    ws_pcm_cb_t    pcm_cb;
    ws_ctrl_cb_t   ctrl_cb;
    void          *user_ctx;
    SemaphoreHandle_t mutex;
    /* Lock-free connection flag, maintained from CONNECTED/DISCONNECTED/ERROR/
     * CLOSED events.  ws_client_connected() reads this instead of calling
     * esp_websocket_client_is_connected(), which takes the client's internal
     * lock with portMAX_DELAY — an unbounded wait that deadlocked voice_task
     * and the LVGL task whenever websocket_task held the lock while running
     * a slow event callback (the "freeze after first LISTEN" bug). */
    volatile bool connected;
};

/* ── Internal event handler ─────────────────────────────────────────────── */

static void _on_event(void *handler_args, esp_event_base_t base,
                      int32_t event_id, void *event_data)
{
    struct ws_client *c     = (struct ws_client *)handler_args;
    esp_websocket_event_data_t *data = (esp_websocket_event_data_t *)event_data;

    switch (event_id) {

    case WEBSOCKET_EVENT_CONNECTED:
        ESP_LOGI(TAG, "WebSocket connected");
        c->connected = true;
        /* Queued — flushed by rlog_task now that we're connected.  Any
         * disconnect-reason lines queued while offline flush right before
         * this one, giving the gateway log the full drop/recover story. */
        vt_remote_log("ws CONNECTED");
        /* Reset the UI to IDLE on (re)connect — the server only sends states
         * on transitions, so without this the face stays on "Reconnecting…"
         * until the next utterance even though the link is back. */
        if (c->state_cb) c->state_cb(WS_VG_STATE_IDLE, c->user_ctx);
        break;

    case WEBSOCKET_EVENT_DISCONNECTED:
        ESP_LOGW(TAG, "WebSocket disconnected — HTTP:%d tls_err:0x%x tls_stack:0x%x sock_errno:%d",
                 data ? data->error_handle.esp_ws_handshake_status_code : -1,
                 data ? data->error_handle.esp_tls_last_esp_err        : -1,
                 data ? data->error_handle.esp_tls_stack_err            : -1,
                 data ? data->error_handle.esp_transport_sock_errno     : -1);
        c->connected = false;
        /* Enqueue the reason NOW; it is delivered after the next reconnect.
         * This is the only remote visibility into why the link dropped. */
        vt_remote_log("ws DISCONNECTED http=%d tls=0x%x stack=0x%x errno=%d",
                      data ? data->error_handle.esp_ws_handshake_status_code : -1,
                      data ? (unsigned)data->error_handle.esp_tls_last_esp_err : 0u,
                      data ? (unsigned)data->error_handle.esp_tls_stack_err    : 0u,
                      data ? data->error_handle.esp_transport_sock_errno       : -1);
        if (c->state_cb) c->state_cb(WS_VG_STATE_DISCONNECTED, c->user_ctx);
        break;

    case WEBSOCKET_EVENT_DATA:
        if (!data) break;

        if (data->op_code == 0x02) {
            /* Binary frame → TTS PCM */
            if (c->pcm_cb && data->data_ptr && data->data_len > 0) {
                c->pcm_cb((const uint8_t *)data->data_ptr,
                          (size_t)data->data_len,
                          c->user_ctx);
            }
        } else if (data->op_code == 0x01) {
            /* Text frame — either JSON state or "END" marker */
            if (!data->data_ptr || data->data_len <= 0) break;

            char buf[64] = {0};
            size_t copy_len = (size_t)data->data_len < sizeof(buf) - 1
                              ? (size_t)data->data_len : sizeof(buf) - 1;
            memcpy(buf, data->data_ptr, copy_len);
            buf[copy_len] = '\0';

            if (strcmp(buf, "END") == 0) {
                /* TTS stream complete — return to idle */
                if (c->state_cb) c->state_cb(WS_VG_STATE_IDLE, c->user_ctx);
                break;
            }

            cJSON *root = cJSON_ParseWithLength(buf, copy_len);
            if (!root) break;
            /* Control frames: {"cmd":"set_volume","value":80} — server-side
             * intercepts of spoken commands (no agent round-trip). */
            cJSON *cmd_item = cJSON_GetObjectItem(root, "cmd");
            if (cJSON_IsString(cmd_item)) {
                cJSON *val_item = cJSON_GetObjectItem(root, "value");
                int val = cJSON_IsNumber(val_item) ? (int)val_item->valuedouble : 0;
                if (c->ctrl_cb) c->ctrl_cb(cmd_item->valuestring, val, c->user_ctx);
                cJSON_Delete(root);
                break;
            }
            cJSON *state_item = cJSON_GetObjectItem(root, "state");
            if (cJSON_IsString(state_item)) {
                const char *s = state_item->valuestring;
                ws_vg_state_t st = WS_VG_STATE_UNKNOWN;
                if      (strcmp(s, "idle")      == 0) st = WS_VG_STATE_IDLE;
                else if (strcmp(s, "listening") == 0) st = WS_VG_STATE_LISTENING;
                else if (strcmp(s, "thinking")  == 0) st = WS_VG_STATE_THINKING;
                else if (strcmp(s, "speaking")  == 0) st = WS_VG_STATE_SPEAKING;
                if (c->state_cb) c->state_cb(st, c->user_ctx);
            }
            cJSON_Delete(root);
        }
        break;

    case WEBSOCKET_EVENT_ERROR:
        ESP_LOGE(TAG, "WebSocket error — HTTP:%d tls_err:0x%x tls_stack:0x%x sock_errno:%d",
                 data ? data->error_handle.esp_ws_handshake_status_code : -1,
                 data ? data->error_handle.esp_tls_last_esp_err        : -1,
                 data ? data->error_handle.esp_tls_stack_err            : -1,
                 data ? data->error_handle.esp_transport_sock_errno     : -1);
        c->connected = false;
        vt_remote_log("ws ERROR http=%d tls=0x%x stack=0x%x errno=%d",
                      data ? data->error_handle.esp_ws_handshake_status_code : -1,
                      data ? (unsigned)data->error_handle.esp_tls_last_esp_err : 0u,
                      data ? (unsigned)data->error_handle.esp_tls_stack_err    : 0u,
                      data ? data->error_handle.esp_transport_sock_errno       : -1);
        if (c->state_cb) c->state_cb(WS_VG_STATE_DISCONNECTED, c->user_ctx);
        break;

    case WEBSOCKET_EVENT_CLOSED:
        ESP_LOGW(TAG, "WebSocket closed — code:%d",
                 data ? data->error_handle.esp_ws_handshake_status_code : -1);
        c->connected = false;
        if (c->state_cb) c->state_cb(WS_VG_STATE_DISCONNECTED, c->user_ctx);
        break;

    default:
        break;
    }
}

/* ── Public API ──────────────────────────────────────────────────────────── */

ws_client_handle_t ws_client_create(const char *url,
                                    ws_state_cb_t state_cb,
                                    ws_pcm_cb_t   pcm_cb,
                                    void         *user_ctx)
{
    struct ws_client *c = calloc(1, sizeof(*c));
    if (!c) return NULL;

    c->state_cb  = state_cb;
    c->pcm_cb    = pcm_cb;
    c->user_ctx  = user_ctx;
    c->mutex     = xSemaphoreCreateMutex();

    esp_websocket_client_config_t cfg = {
        .uri                  = url,
        /* 1.5 s (was 5 s): on the drop-happy hotspot every delivery retry
         * paid the full wait before reconnecting — with uplink resume the
         * retries are cheap, so start them fast. */
        .reconnect_timeout_ms = 1500,
        /* 5 s — headroom for TLS/DERP latency spikes, but short enough that a
         * write to a dying socket can't monopolise the tx lock for long (the
         * old 8 s made each doomed PCM write starve every other sender). */
        .network_timeout_ms   = 5000,
        /* Buffer large enough for one TTS chunk (4 KB PCM). */
        .buffer_size          = 8192,
        /* WS-level PING disabled (0 = off).  Tailscale Funnel / DERP relay does
         * not reliably relay WebSocket control frames (PING/PONG) — the relay
         * drops the PONG, pingpong_timeout_sec fires, and the ESP disconnects
         * after ~40 s of idle.  Application-level heartbeat ({"heartbeat":1}
         * text frame every 4 s from the server) keeps the relay and hotspot
         * NAT alive without control frames. */
        .ping_interval_sec    = 0,
        .pingpong_timeout_sec = 0,
        /* TLS: attach the ESP-IDF CA bundle (includes ISRG Root X1 / Let's Encrypt).
         * Required for wss:// connections to Tailscale Funnel. No-op for ws://. */
        .crt_bundle_attach    = esp_crt_bundle_attach,
        /* Pin websocket_task to CPU 1 alongside voice_task.
         * task_core_id_set MUST be true — the client ignores task_core_id and
         * uses tskNO_AFFINITY when task_core_id_set is false. */
        .task_core_id_set     = true,
        .task_core_id         = 1,
        /* Priority below voice_task (5) so PSRAM canvas fills in the ws event
         * callback (face_set_emotion → lv_canvas_fill_bg) cannot preempt audio
         * capture.  Default is 10, which is above voice_task and would starve it. */
        .task_prio            = 4,
    };

    c->wsc = esp_websocket_client_init(&cfg);
    if (!c->wsc) {
        ESP_LOGE(TAG, "esp_websocket_client_init failed");
        free(c);
        return NULL;
    }

    esp_websocket_register_events(c->wsc, WEBSOCKET_EVENT_ANY,
                                  _on_event, (void *)c);
    esp_err_t ret = esp_websocket_client_start(c->wsc);
    if (ret != ESP_OK) {
        ESP_LOGE(TAG, "esp_websocket_client_start failed: %s",
                 esp_err_to_name(ret));
        esp_websocket_client_destroy(c->wsc);
        free(c);
        return NULL;
    }

    ESP_LOGI(TAG, "WebSocket connecting to %s", url);
    return c;
}

esp_err_t ws_client_send_pcm(ws_client_handle_t c, const uint8_t *buf, size_t len)
{
    if (!c || !buf || len == 0) return ESP_ERR_INVALID_ARG;
    if (!c->connected) return ESP_ERR_INVALID_STATE;   /* lock-free flag — see ws_client_connected() */
    /* 4 s: hotspot radio wake-up stalls the socket for over a second at burst
     * start; with 1 s the write timed out, the client closed the connection,
     * and the whole delivery attempt was spent (live trace 2026-07-04:
     * attempts died at 4-151 KB into 256 KB).  Only the store-and-forward
     * delivery path calls this, so a longer wait blocks nothing critical. */
    int sent = esp_websocket_client_send_bin(c->wsc, (const char *)buf,
                                             (int)len, pdMS_TO_TICKS(4000));
    return (sent >= 0) ? ESP_OK : ESP_FAIL;
}

esp_err_t ws_client_send_listen(ws_client_handle_t c)
{
    if (!c) return ESP_ERR_INVALID_ARG;
    if (!c->connected) return ESP_ERR_INVALID_STATE;   /* lock-free flag — see ws_client_connected() */
    const char *msg = "LISTEN";
    int sent = esp_websocket_client_send_text(c->wsc, msg, strlen(msg),
                                              pdMS_TO_TICKS(1000));
    return (sent >= 0) ? ESP_OK : ESP_FAIL;
}

esp_err_t ws_client_send_listen_resume(ws_client_handle_t c, size_t offset)
{
    if (!c) return ESP_ERR_INVALID_ARG;
    if (!c->connected) return ESP_ERR_INVALID_STATE;   /* lock-free flag — see ws_client_connected() */
    char msg[32];
    int  n = snprintf(msg, sizeof(msg), "LISTEN %u", (unsigned)offset);
    int sent = esp_websocket_client_send_text(c->wsc, msg, n,
                                              pdMS_TO_TICKS(1000));
    return (sent >= 0) ? ESP_OK : ESP_FAIL;
}

esp_err_t ws_client_send_end(ws_client_handle_t c)
{
    if (!c) return ESP_ERR_INVALID_ARG;
    if (!c->connected) return ESP_ERR_INVALID_STATE;   /* lock-free flag — see ws_client_connected() */
    const char *msg = "END";
    int sent = esp_websocket_client_send_text(c->wsc, msg, strlen(msg),
                                              pdMS_TO_TICKS(1000));
    return (sent >= 0) ? ESP_OK : ESP_FAIL;
}

esp_err_t ws_client_send_stop(ws_client_handle_t c)
{
    if (!c) return ESP_ERR_INVALID_ARG;
    if (!c->connected) return ESP_ERR_INVALID_STATE;   /* lock-free flag — see ws_client_connected() */
    const char *msg = "STOP";
    int sent = esp_websocket_client_send_text(c->wsc, msg, strlen(msg),
                                              pdMS_TO_TICKS(1000));
    return (sent >= 0) ? ESP_OK : ESP_FAIL;
}

esp_err_t ws_client_send_keepalive(ws_client_handle_t c)
{
    if (!c) return ESP_ERR_INVALID_ARG;
    if (!c->connected) return ESP_OK;   /* lock-free flag — see ws_client_connected() */
    const char *msg = "{\"ping\":1}";
    int sent = esp_websocket_client_send_text(c->wsc, msg, strlen(msg),
                                              pdMS_TO_TICKS(1000));
    return (sent >= 0) ? ESP_OK : ESP_FAIL;
}

esp_err_t ws_client_send_log(ws_client_handle_t c, const char *msg)
{
    if (!c || !msg) return ESP_ERR_INVALID_ARG;
    if (!c->connected) return ESP_OK;  /* best effort; lock-free flag */

    /* Build {"log":"<msg>"} with JSON-hostile chars replaced.  Diagnostic
     * strings are ASCII we control, so stripping quotes/backslashes/control
     * chars is sufficient — no full escaper needed. */
    char frame[224];
    size_t pos = 0;
    const char *prefix = "{\"log\":\"";
    for (const char *p = prefix; *p; p++) frame[pos++] = *p;
    for (const char *p = msg; *p && pos < sizeof(frame) - 3; p++) {
        unsigned char ch = (unsigned char)*p;
        frame[pos++] = (ch == '"' || ch == '\\' || ch < 0x20) ? ' ' : (char)ch;
    }
    frame[pos++] = '"';
    frame[pos++] = '}';
    frame[pos]   = '\0';

    /* Bounded timeout: only rlog_task calls this (never LVGL/voice_task
     * directly), so 500 ms is safe and wins more lock races against the
     * streaming PCM writes than the original 200 ms did. */
    int sent = esp_websocket_client_send_text(c->wsc, frame, (int)pos,
                                              pdMS_TO_TICKS(500));
    return (sent >= 0) ? ESP_OK : ESP_FAIL;
}

void ws_client_set_ctrl_cb(ws_client_handle_t c, ws_ctrl_cb_t cb)
{
    if (c) c->ctrl_cb = cb;
}

bool ws_client_connected(ws_client_handle_t c)
{
    if (!c) return false;
    /* LOCK-FREE — do NOT call esp_websocket_client_is_connected() here.
     * That API takes the client's internal recursive mutex with portMAX_DELAY;
     * while websocket_task holds the same mutex during receive+dispatch (which
     * runs our event callbacks), any caller wedges unboundedly.  This exact
     * interaction froze voice_task and the LVGL task after the first LISTEN. */
    return c->connected;
}

void ws_client_destroy(ws_client_handle_t c)
{
    if (!c) return;
    esp_websocket_client_stop(c->wsc);
    esp_websocket_client_destroy(c->wsc);
    if (c->mutex) vSemaphoreDelete(c->mutex);
    free(c);
}
