#include <string.h>
#include "wifi_credentials.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/event_groups.h"
#include "esp_log.h"
#include "esp_wifi.h"
#include "esp_event.h"
#include "nvs_flash.h"
#include "bsp/esp-bsp.h"
#include "lvgl.h"

static const char *TAG = "vt";

/* ── WiFi ─────────────────────────────────────────────────────────────── */

#define WIFI_CONNECTED_BIT BIT0
#define WIFI_FAIL_BIT      BIT1

static EventGroupHandle_t s_wifi_eg;
static int                s_retry = 0;
static char               s_ip[20];

typedef struct { const char *ssid; const char *pass; } wifi_net_t;
static const wifi_net_t NETWORKS[] = {
    { CONFIG_VT_WIFI_SSID,   CONFIG_VT_WIFI_PASSWORD   },
    { CONFIG_VT_WIFI_SSID_2, CONFIG_VT_WIFI_PASSWORD_2 },
};
#define NETWORK_COUNT (sizeof(NETWORKS) / sizeof(NETWORKS[0]))
static int s_net_idx = 0;

/* ── LVGL UI ──────────────────────────────────────────────────────────── */

typedef enum {
    UI_WIFI_CONNECTING,
    UI_WIFI_CONNECTED,
    UI_READY,
} ui_state_t;

static lv_obj_t  *s_label      = NULL;
static lv_obj_t  *s_sub_label  = NULL;
static ui_state_t s_ui_state   = UI_WIFI_CONNECTING;

static void ui_update(ui_state_t state, const char *detail)
{
    if (!s_label) return;
    bsp_display_lock(0);
    s_ui_state = state;
    switch (state) {
        case UI_WIFI_CONNECTING:
            lv_label_set_text(s_label, "Connecting to WiFi...");
            lv_label_set_text(s_sub_label, detail ? detail : "");
            break;
        case UI_WIFI_CONNECTED:
            lv_label_set_text(s_label, "WiFi connected");
            lv_label_set_text(s_sub_label, detail ? detail : "");
            break;
        case UI_READY:
            lv_label_set_text(s_label, "Hermes online");
            lv_label_set_text(s_sub_label, "Say \"hey buddy\"");
            break;
    }
    bsp_display_unlock();
}

static void ui_init(void)
{
    bsp_display_cfg_t cfg = {
        .lvgl_port_cfg = ESP_LVGL_PORT_INIT_CONFIG(),
        .buffer_size   = BSP_LCD_H_RES * BSP_LCD_V_RES / 4,
    };
    bsp_display_start_with_config(&cfg);
    bsp_display_backlight_on();

    bsp_display_lock(0);

    lv_obj_t *scr = lv_scr_act();
    lv_obj_set_style_bg_color(scr, lv_color_hex(0x1a1a2e), LV_PART_MAIN);

    s_label = lv_label_create(scr);
    lv_obj_set_style_text_color(s_label, lv_color_hex(0xeaeaea), LV_PART_MAIN);
    lv_obj_set_style_text_font(s_label, &lv_font_montserrat_28, LV_PART_MAIN);
    lv_obj_align(s_label, LV_ALIGN_CENTER, 0, -28);
    lv_label_set_text(s_label, "Starting...");

    s_sub_label = lv_label_create(scr);
    lv_obj_set_style_text_color(s_sub_label, lv_color_hex(0x888888), LV_PART_MAIN);
    lv_obj_set_style_text_font(s_sub_label, &lv_font_montserrat_28, LV_PART_MAIN);
    lv_obj_align(s_sub_label, LV_ALIGN_CENTER, 0, 28);
    lv_label_set_text(s_sub_label, "");

    bsp_display_unlock();
}

/* ── WiFi event handler ───────────────────────────────────────────────── */

static void wifi_event_handler(void *arg, esp_event_base_t base,
                               int32_t id, void *data)
{
    if (base == WIFI_EVENT && id == WIFI_EVENT_STA_START) {
        esp_wifi_connect();

    } else if (base == WIFI_EVENT && id == WIFI_EVENT_STA_DISCONNECTED) {
        wifi_event_sta_disconnected_t *ev = (wifi_event_sta_disconnected_t *)data;
        s_retry++;
        ESP_LOGW(TAG, "WiFi disconnected from '%s' reason=%d (attempt %d/%d)",
                 NETWORKS[s_net_idx].ssid, ev->reason, s_retry, CONFIG_VT_WIFI_MAX_RETRY);

        if (s_retry >= CONFIG_VT_WIFI_MAX_RETRY) {
            /* Try next network in the list; skip blank SSIDs */
            s_retry = 0;
            s_net_idx = (s_net_idx + 1) % NETWORK_COUNT;
            if (strlen(NETWORKS[s_net_idx].ssid) == 0) {
                s_net_idx = 0;
            }
            ESP_LOGI(TAG, "Switching to network '%s'", NETWORKS[s_net_idx].ssid);

            wifi_config_t cfg = {};
            strlcpy((char *)cfg.sta.ssid,     NETWORKS[s_net_idx].ssid, 32);
            strlcpy((char *)cfg.sta.password, NETWORKS[s_net_idx].pass, 64);
            esp_wifi_set_config(WIFI_IF_STA, &cfg);
            ui_update(UI_WIFI_CONNECTING, NETWORKS[s_net_idx].ssid);
        }
        esp_wifi_connect();

    } else if (base == IP_EVENT && id == IP_EVENT_STA_GOT_IP) {
        ip_event_got_ip_t *ev = (ip_event_got_ip_t *)data;
        snprintf(s_ip, sizeof(s_ip), IPSTR, IP2STR(&ev->ip_info.ip));
        ESP_LOGI(TAG, "Got IP: %s", s_ip);
        s_retry = 0;
        xEventGroupSetBits(s_wifi_eg, WIFI_CONNECTED_BIT);
        ui_update(UI_WIFI_CONNECTED, s_ip);
    }
}

static void wifi_init(void)
{
    s_wifi_eg = xEventGroupCreate();
    esp_netif_create_default_wifi_sta();

    wifi_init_config_t init = WIFI_INIT_CONFIG_DEFAULT();
    ESP_ERROR_CHECK(esp_wifi_init(&init));

    ESP_ERROR_CHECK(esp_event_handler_instance_register(
        WIFI_EVENT, ESP_EVENT_ANY_ID, &wifi_event_handler, NULL, NULL));
    ESP_ERROR_CHECK(esp_event_handler_instance_register(
        IP_EVENT, IP_EVENT_STA_GOT_IP, &wifi_event_handler, NULL, NULL));

    wifi_config_t cfg = {};
    strlcpy((char *)cfg.sta.ssid,     NETWORKS[0].ssid, 32);
    strlcpy((char *)cfg.sta.password, NETWORKS[0].pass, 64);
    cfg.sta.threshold.authmode = WIFI_AUTH_OPEN;

    ESP_ERROR_CHECK(esp_wifi_set_mode(WIFI_MODE_STA));
    ESP_ERROR_CHECK(esp_wifi_set_config(WIFI_IF_STA, &cfg));
    ESP_ERROR_CHECK(esp_wifi_start());

    ESP_LOGI(TAG, "Connecting to '%s'...", NETWORKS[0].ssid);
    ui_update(UI_WIFI_CONNECTING, NETWORKS[0].ssid);
}

/* ── app_main ─────────────────────────────────────────────────────────── */

void app_main(void)
{
    ESP_LOGI(TAG, "Voice terminal starting");

    /* NVS — required by WiFi */
    esp_err_t err = nvs_flash_init();
    if (err == ESP_ERR_NVS_NO_FREE_PAGES || err == ESP_ERR_NVS_NEW_VERSION_FOUND) {
        ESP_ERROR_CHECK(nvs_flash_erase());
        err = nvs_flash_init();
    }
    ESP_ERROR_CHECK(err);

    /* Log PSRAM (confirmed by sdkconfig; init is automatic) */
    ESP_LOGI(TAG, "PSRAM: %u KB available",
             (unsigned)(heap_caps_get_total_size(MALLOC_CAP_SPIRAM) / 1024));

    /* Display + touch */
    ui_init();
    ESP_LOGI(TAG, "Display initialised");

    /* WiFi */
    ESP_ERROR_CHECK(esp_netif_init());
    ESP_ERROR_CHECK(esp_event_loop_create_default());
    wifi_init();

    /* Wait for first connection, then show ready screen */
    xEventGroupWaitBits(s_wifi_eg, WIFI_CONNECTED_BIT, pdFALSE, pdTRUE,
                        portMAX_DELAY);

    /* Brief pause so user can read the IP */
    vTaskDelay(pdMS_TO_TICKS(2000));
    ui_update(UI_READY, NULL);
    ESP_LOGI(TAG, "Ready. Tunnel and voice streaming in next phase.");

    /* Reconnect loop — WiFi event handler already retries; this just idles */
    while (1) {
        vTaskDelay(pdMS_TO_TICKS(10000));
    }
}
