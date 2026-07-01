// Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
#include "ota.h"
#include <string.h>
#include "esp_log.h"
#include "esp_http_client.h"
#include "esp_crt_bundle.h"
#include "esp_ota_ops.h"
#include "nvs.h"
#include "esp_system.h"

static const char *TAG = "vt_ota";
static char s_etag_buf[128];

static esp_err_t _http_event_handler(esp_http_client_event_t *evt)
{
    if (evt->event_id == HTTP_EVENT_ON_HEADER &&
        strcasecmp(evt->header_key, "ETag") == 0) {
        strncpy(s_etag_buf, evt->header_value, sizeof(s_etag_buf) - 1);
        s_etag_buf[sizeof(s_etag_buf) - 1] = '\0';
    }
    return ESP_OK;
}

/* wss://host/path → https://host  (ws:// → http://) */
static void _ws_to_https_base(const char *ws_url, char *out, size_t out_len)
{
    const char *scheme;
    const char *host_start;
    if (strncmp(ws_url, "wss://", 6) == 0) {
        scheme = "https://";
        host_start = ws_url + 6;
    } else if (strncmp(ws_url, "ws://", 5) == 0) {
        scheme = "http://";
        host_start = ws_url + 5;
    } else {
        strncpy(out, ws_url, out_len - 1);
        out[out_len - 1] = '\0';
        return;
    }
    const char *path = strchr(host_start, '/');
    int host_len = path ? (int)(path - host_start) : (int)strlen(host_start);
    snprintf(out, out_len, "%s%.*s", scheme, host_len, host_start);
}

static bool _nvs_get_etag(char *out, size_t len)
{
    nvs_handle_t h;
    if (nvs_open("ota_state", NVS_READONLY, &h) != ESP_OK) return false;
    size_t get_len = len;
    bool ok = (nvs_get_str(h, "etag", out, &get_len) == ESP_OK);
    nvs_close(h);
    return ok;
}

static void _nvs_set_etag(const char *etag)
{
    nvs_handle_t h;
    if (nvs_open("ota_state", NVS_READWRITE, &h) != ESP_OK) return;
    nvs_set_str(h, "etag", etag);
    nvs_commit(h);
    nvs_close(h);
}

esp_err_t ota_check(const char *ws_url, const char *token)
{
    char base[256];
    _ws_to_https_base(ws_url, base, sizeof(base));

    char url[384];
    snprintf(url, sizeof(url), "%s/firmware/bin?token=%s", base, token);

    /* HEAD: retrieve ETag from gateway ──────────────────────────────────── */
    s_etag_buf[0] = '\0';
    esp_http_client_config_t cfg = {
        .url               = url,
        .method            = HTTP_METHOD_HEAD,
        .timeout_ms        = 10000,
        .crt_bundle_attach = esp_crt_bundle_attach,
        .event_handler     = _http_event_handler,
    };
    esp_http_client_handle_t client = esp_http_client_init(&cfg);
    if (!client) {
        ESP_LOGW(TAG, "OTA: failed to init HTTP client");
        return ESP_OK;
    }
    esp_err_t err = esp_http_client_perform(client);
    int status = esp_http_client_get_status_code(client);
    esp_http_client_cleanup(client);

    if (err != ESP_OK || status != 200) {
        ESP_LOGW(TAG, "OTA HEAD failed: err=%d http=%d", err, status);
        return ESP_OK;
    }
    if (s_etag_buf[0] == '\0') {
        ESP_LOGW(TAG, "OTA HEAD: no ETag in response");
        return ESP_OK;
    }
    ESP_LOGI(TAG, "Remote ETag: %s", s_etag_buf);

    /* Compare with stored ETag ──────────────────────────────────────────── */
    char stored[128] = {0};
    if (_nvs_get_etag(stored, sizeof(stored)) &&
        strcmp(stored, s_etag_buf) == 0) {
        ESP_LOGI(TAG, "Firmware current");
        return ESP_OK;
    }
    ESP_LOGI(TAG, "ETag mismatch — starting OTA download");

    /* GET: stream binary into the inactive OTA partition ────────────────── */
    const esp_partition_t *update_part = esp_ota_get_next_update_partition(NULL);
    if (!update_part) {
        ESP_LOGE(TAG, "OTA: no update partition — check partitions.csv has ota_1");
        return ESP_OK;
    }

    esp_ota_handle_t ota_handle = 0;
    err = esp_ota_begin(update_part, OTA_WITH_SEQUENTIAL_WRITES, &ota_handle);
    if (err != ESP_OK) {
        ESP_LOGE(TAG, "esp_ota_begin: %s", esp_err_to_name(err));
        return ESP_OK;
    }

    esp_http_client_config_t get_cfg = {
        .url               = url,
        .method            = HTTP_METHOD_GET,
        .timeout_ms        = 120000,
        .crt_bundle_attach = esp_crt_bundle_attach,
        .buffer_size       = 4096,
    };
    client = esp_http_client_init(&get_cfg);
    if (!client) {
        ESP_LOGE(TAG, "OTA: failed to init GET client");
        esp_ota_abort(ota_handle);
        return ESP_OK;
    }

    err = esp_http_client_open(client, 0);
    if (err != ESP_OK) {
        ESP_LOGE(TAG, "OTA HTTP open: %s", esp_err_to_name(err));
        esp_http_client_cleanup(client);
        esp_ota_abort(ota_handle);
        return ESP_OK;
    }
    esp_http_client_fetch_headers(client);
    status = esp_http_client_get_status_code(client);
    if (status != 200) {
        ESP_LOGE(TAG, "OTA GET returned HTTP %d", status);
        esp_http_client_close(client);
        esp_http_client_cleanup(client);
        esp_ota_abort(ota_handle);
        return ESP_OK;
    }

    char *buf = malloc(4096);
    if (!buf) {
        ESP_LOGE(TAG, "OTA: out of memory for download buffer");
        esp_http_client_close(client);
        esp_http_client_cleanup(client);
        esp_ota_abort(ota_handle);
        return ESP_OK;
    }
    int total = 0;
    int rd;
    bool ok = true;
    while ((rd = esp_http_client_read(client, buf, 4096)) > 0) {
        if (esp_ota_write(ota_handle, buf, rd) != ESP_OK) {
            ESP_LOGE(TAG, "esp_ota_write failed at byte %d", total);
            ok = false;
            break;
        }
        total += rd;
    }
    esp_http_client_close(client);
    esp_http_client_cleanup(client);
    free(buf);

    if (!ok || total == 0) {
        ESP_LOGE(TAG, "OTA download incomplete (%d bytes)", total);
        esp_ota_abort(ota_handle);
        return ESP_OK;
    }
    ESP_LOGI(TAG, "Downloaded %d bytes", total);

    err = esp_ota_end(ota_handle);
    if (err != ESP_OK) {
        ESP_LOGE(TAG, "esp_ota_end: %s", esp_err_to_name(err));
        return ESP_OK;
    }
    err = esp_ota_set_boot_partition(update_part);
    if (err != ESP_OK) {
        ESP_LOGE(TAG, "esp_ota_set_boot_partition: %s", esp_err_to_name(err));
        return ESP_OK;
    }

    _nvs_set_etag(s_etag_buf);
    ESP_LOGI(TAG, "OTA complete — rebooting into new firmware");
    esp_restart();
    return ESP_OK;  /* unreachable */
}
