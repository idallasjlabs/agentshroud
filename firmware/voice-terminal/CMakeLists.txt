cmake_minimum_required(VERSION 3.16)

include($ENV{IDF_PATH}/tools/cmake/project.cmake)
project(voice_terminal)

# Patch esp-box-3 BSP for IDF v5.3+ i2c API compatibility.
# ESP_LCD_TOUCH_IO_I2C_*_CONFIG() macros set scl_speed_hz, which the legacy
# i2c LCD driver rejects in IDF >= 5.3 with ESP_ERR_INVALID_ARG.
# This runs after the component manager fetches the BSP on first build.
set(_BSP_SRC "${CMAKE_CURRENT_SOURCE_DIR}/managed_components/espressif__esp-box-3/esp-box-3.c")
if(EXISTS "${_BSP_SRC}")
    file(READ "${_BSP_SRC}" _bsp)
    if(_bsp MATCHES "ESP_RETURN_ON_ERROR.esp_lcd_new_panel_io_i2c" AND NOT _bsp MATCHES "scl_speed_hz = 0")
        string(REPLACE
            "    ESP_RETURN_ON_ERROR(esp_lcd_new_panel_io_i2c((esp_lcd_i2c_bus_handle_t)BSP_I2C_NUM"
            "    tp_io_config.scl_speed_hz = 0; /* IDF v5.3+ rejects non-zero value in legacy driver */\n    ESP_RETURN_ON_ERROR(esp_lcd_new_panel_io_i2c((esp_lcd_i2c_bus_handle_t)BSP_I2C_NUM"
            _bsp_patched "${_bsp}")
        file(WRITE "${_BSP_SRC}" "${_bsp_patched}")
        message(STATUS "voice_terminal: applied IDF v5.4 scl_speed_hz patch to esp-box-3 BSP")
    endif()
endif()
