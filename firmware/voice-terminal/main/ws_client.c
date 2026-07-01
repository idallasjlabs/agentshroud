#include "ws_client.h"
#include <string.h>
#include <stdlib.h>
#include "cJSON.h"
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
    void          *user_ctx;
    SemaphoreHandle_t mutex;
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
        break;

    case WEBSOCKET_EVENT_DISCONNECTED:
        ESP_LOGW(TAG, "WebSocket disconnected — HTTP:%d tls_err:0x%x tls_stack:0x%x sock_errno:%d",
                 data ? data->error_handle.esp_ws_handshake_status_code : -1,
                 data ? data->error_handle.esp_tls_last_esp_err        : -1,
                 data ? data->error_handle.esp_tls_stack_err            : -1,
                 data ? data->error_handle.esp_transport_sock_errno     : -1);
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
        if (c->state_cb) c->state_cb(WS_VG_STATE_DISCONNECTED, c->user_ctx);
        break;

    case WEBSOCKET_EVENT_CLOSED:
        ESP_LOGW(TAG, "WebSocket closed — code:%d",
                 data ? data->error_handle.esp_ws_handshake_status_code : -1);
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
        .reconnect_timeout_ms = 5000,
        /* 8 s — gives TLS enough headroom for DERP relay latency spikes while
         * staying safely under the 10 s task WDT timeout. 15 s was too close
         * to the old 5 s WDT and triggered it on every retry cycle. */
        .network_timeout_ms   = 8000,
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
        /* Pin websocket_task to CPU 0 so TLS bignum cannot starve IDLE1 (CPU 1).
         * task_core_id_set MUST be true — the client ignores task_core_id and
         * uses tskNO_AFFINITY when task_core_id_set is false (default for a
         * zero-initialised struct, even if task_core_id is explicitly set to 0). */
        .task_core_id_set     = true,
        .task_core_id         = 0,
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
    if (!esp_websocket_client_is_connected(c->wsc)) return ESP_ERR_INVALID_STATE;
    int sent = esp_websocket_client_send_bin(c->wsc, (const char *)buf,
                                             (int)len, pdMS_TO_TICKS(1000));
    return (sent >= 0) ? ESP_OK : ESP_FAIL;
}

esp_err_t ws_client_send_listen(ws_client_handle_t c)
{
    if (!c) return ESP_ERR_INVALID_ARG;
    if (!esp_websocket_client_is_connected(c->wsc)) return ESP_ERR_INVALID_STATE;
    const char *msg = "LISTEN";
    int sent = esp_websocket_client_send_text(c->wsc, msg, strlen(msg),
                                              pdMS_TO_TICKS(1000));
    return (sent >= 0) ? ESP_OK : ESP_FAIL;
}

esp_err_t ws_client_send_end(ws_client_handle_t c)
{
    if (!c) return ESP_ERR_INVALID_ARG;
    if (!esp_websocket_client_is_connected(c->wsc)) return ESP_ERR_INVALID_STATE;
    const char *msg = "END";
    int sent = esp_websocket_client_send_text(c->wsc, msg, strlen(msg),
                                              pdMS_TO_TICKS(1000));
    return (sent >= 0) ? ESP_OK : ESP_FAIL;
}

bool ws_client_connected(ws_client_handle_t c)
{
    if (!c) return false;
    return esp_websocket_client_is_connected(c->wsc);
}

void ws_client_destroy(ws_client_handle_t c)
{
    if (!c) return;
    esp_websocket_client_stop(c->wsc);
    esp_websocket_client_destroy(c->wsc);
    if (c->mutex) vSemaphoreDelete(c->mutex);
    free(c);
}
