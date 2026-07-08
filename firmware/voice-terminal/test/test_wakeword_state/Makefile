# Host-native Makefile for wakeword PTT state machine tests.
# Compiles wakeword.c against stub headers (no ESP-IDF, no FreeRTOS, no hardware).
#
# Usage:
#   make          # build + run
#   make build    # build only
#   make clean    # remove build artefacts

CC      = cc
TARGET  = test_ptt_state
MAIN_SRC = ../../main/wakeword.c

# -DHAVE_ESP_SR=0          : disable AFE/WakeNet (no esp-sr headers available on host)
# -I stubs                 : provide FreeRTOS, ESP-IDF, BSP stub headers
# -I ../../main            : wakeword.h, audio.h
# -Wno-unused-function     : _btn_* callbacks are registered via function pointers;
#                            the compiler cannot see the call site in host builds
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

$(TARGET): $(MAIN_SRC) test_ptt_state.c
	$(CC) $(CFLAGS) $^ -o $@

run: $(TARGET)
	@echo ""
	./$(TARGET)
	@echo ""

clean:
	rm -f $(TARGET)
