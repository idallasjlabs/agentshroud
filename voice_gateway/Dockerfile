# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud Voice Gateway — STT + TTS bridge for ESP32-S3-BOX-3
FROM python:3.13-slim

LABEL maintainer="Isaiah Dallas Jefferson, Jr. <idallasj@gmail.com>"
LABEL org.agentshroud.component="voice-gateway"

# Non-root user (UID 1001) for least-privilege operation
RUN useradd -m -u 1001 -s /sbin/nologin vg

WORKDIR /app

# System deps: Piper needs libsndfile + libespeak-ng1; faster-whisper needs ffmpeg
RUN apt-get update -qq && \
    apt-get install -y --no-install-recommends \
        ffmpeg \
        libsndfile1 \
        libespeak-ng1 \
        curl \
    && rm -rf /var/lib/apt/lists/*

# Install Piper TTS binary + bundled shared libs.
# The piper release tarball contains libpiper_phonemize.so.1 and libonnxruntime.so.1.14.1
# alongside the binary — these MUST be extracted or piper exits 127 at runtime.
# We extract everything into /opt/piper-bin, then symlink the executable so
# LD_LIBRARY_PATH=/opt/piper-bin makes the bundled libs visible.
ARG PIPER_VERSION=2023.11.14-2
ARG TARGETARCH
RUN case "${TARGETARCH}" in \
        arm64|aarch64) PIPER_ARCH="aarch64" ;; \
        *)             PIPER_ARCH="x86_64"  ;; \
    esac && \
    mkdir -p /opt/piper-bin && \
    curl -fsSL \
        "https://github.com/rhasspy/piper/releases/download/${PIPER_VERSION}/piper_linux_${PIPER_ARCH}.tar.gz" \
        | tar -xz -C /opt/piper-bin --strip-components=1 && \
    chmod +x /opt/piper-bin/piper && \
    ln -sf /opt/piper-bin/piper /usr/local/bin/piper
ENV LD_LIBRARY_PATH=/opt/piper-bin

# Download Piper voice model
RUN mkdir -p /opt/piper && \
    curl -fsSL "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx" \
        -o /opt/piper/en_US-lessac-medium.onnx && \
    curl -fsSL "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_US/lessac/medium/en_US-lessac-medium.onnx.json" \
        -o /opt/piper/en_US-lessac-medium.onnx.json

COPY voice_gateway/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-bake the faster-whisper STT model so runtime needs ZERO egress.
# voice-gateway runs on agentshroud-isolated; all outbound is blocked by the
# gateway egress proxy (default-deny enforce mode, huggingface.co not allowlisted).
# Mirrors the Piper voice-model bake above — build time has full internet.
ARG WHISPER_MODEL_SIZE=small.en
ENV WHISPER_MODEL_DIR=/opt/whisper/${WHISPER_MODEL_SIZE}
RUN python -c "from faster_whisper import download_model; \
    download_model('${WHISPER_MODEL_SIZE}', output_dir='/opt/whisper/${WHISPER_MODEL_SIZE}')" && \
    chmod -R a+rX /opt/whisper
# Belt-and-suspenders: never reach out to HF at runtime even for metadata checks.
ENV HF_HUB_OFFLINE=1

COPY voice_gateway/ /app/voice_gateway/

ENV PIPER_BIN=/opt/piper-bin/piper
ENV PIPER_MODEL=/opt/piper/en_US-lessac-medium.onnx
ENV VG_HOST=0.0.0.0
ENV VG_PORT=8765

USER vg
EXPOSE 8765

HEALTHCHECK --interval=30s --timeout=5s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:8765/health || exit 1

CMD ["python", "-m", "voice_gateway"]
