idf_component_register(
    SRCS
        "app_main.c"
        "audio.c"
        "wakeword.c"
        "ws_client.c"
        "ui_face.c"
    INCLUDE_DIRS "."
    PRIV_REQUIRES
        esp_wifi
        esp_event
        nvs_flash
        esp_codec_dev
        esp_websocket_client
        json
        button
        esp-sr
)
