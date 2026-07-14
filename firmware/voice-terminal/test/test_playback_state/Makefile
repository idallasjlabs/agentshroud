# Host-native Makefile for the TTS playback END-gate + state-machine tests.
# Compiles wakeword.c (for the real tts_playing / triggered flag functions)
# against stub headers and links the pure playback_logic.h helpers.
# No ESP-IDF, no FreeRTOS, no LVGL, no hardware.
#
# Usage:
#   make          # build + run
#   make build    # build only
#   make clean    # remove build artefacts

CC      = cc
TARGET  = test_playback_state
MAIN_SRC = ../../main/wakeword.c

# -DHAVE_ESP_SR=0          : disable AFE/WakeNet (no esp-sr headers on host)
# -I stubs                 : FreeRTOS, ESP-IDF, BSP stub headers
# -I ../../main            : wakeword.h, playback_logic.h
# -Wno-unused-function     : _btn_* callbacks registered via function pointers
CFLAGS  = \
    -std=c11 \
    -DHAVE_ESP_SR=0 \
    -I stubs \
    -I ../../main \
    -Wall \
    -Wno-unused-function \
    -Wno-unused-variable

.PHONY: all build run clean

all: build run

build: $(TARGET)

$(TARGET): $(MAIN_SRC) test_playback_state.c
	$(CC) $(CFLAGS) $^ -o $@

run: $(TARGET)
	@echo ""
	./$(TARGET)
	@echo ""

clean:
	rm -f $(TARGET)
