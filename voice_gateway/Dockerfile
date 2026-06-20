# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud Voice Gateway — STT + TTS bridge for ESP32-S3-BOX-3
FROM python:3.13-slim

LABEL maintainer="Isaiah Dallas Jefferson, Jr. <idallasj@gmail.com>"
LABEL org.agentshroud.component="voice-gateway"

# Non-root user (UID 1001) for least-privilege operation
RUN useradd -m -u 1001 -s /sbin/nologin vg

WORKDIR /app

# System deps: Piper needs libsndfile; faster-whisper needs ffmpeg for audio decoding
RUN apt-get update -qq && \
    apt-get install -y --no-install-recommends \
        ffmpeg \
        libsndfile1 \
        curl \
    && rm -rf /var/lib/apt/lists/*

# Install Piper TTS binary — supports linux/amd64 and linux/arm64 (marvin is arm64)
ARG PIPER_VERSION=2023.11.14-2
ARG TARGETARCH
RUN case "${TARGETARCH}" in \
        arm64|aarch64) PIPER_ARCH="aarch64" ;; \
        *)             PIPER_ARCH="x86_64"  ;; \
    esac && \
    curl -fsSL \
        "https://github.com/rhasspy/piper/releases/download/${PIPER_VERSION}/piper_linux_${PIPER_ARCH}.tar.gz" \
        | tar -xz -C /usr/local/bin --strip-components=1 piper/piper && \
    chmod +x /usr/local/bin/piper

# Download Piper voice model
RUN mkdir -p /opt/piper && \
    curl -fsSL "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx" \
        -o /opt/piper/en_US-lessac-medium.onnx && \
    curl -fsSL "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx.json" \
        -o /opt/piper/en_US-lessac-medium.onnx.json

COPY voice_gateway/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY voice_gateway/ /app/voice_gateway/

ENV PIPER_BIN=/usr/local/bin/piper
ENV PIPER_MODEL=/opt/piper/en_US-lessac-medium.onnx
ENV VG_HOST=0.0.0.0
ENV VG_PORT=8765

USER vg
EXPOSE 8765

HEALTHCHECK --interval=30s --timeout=5s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:8765/health || exit 1

CMD ["python", "-m", "voice_gateway"]
