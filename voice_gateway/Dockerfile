# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud Voice Gateway — STT + TTS bridge for ESP32-S3-BOX-3
# Base image pinned to SHA256 digest for supply-chain integrity (SCRUM-100).
# Update with: docker pull python:3.12-slim && docker inspect --format='{{index .RepoDigests 0}}' python:3.12-slim
# SCRUM-101: digest refreshed 2026-07-14 to latest patched python:3.12-slim.
FROM python:3.12-slim@sha256:c3d81d25b3154142b0b42eb1e61300024426268edeb5b5a26dd7ddf64d9daf28

LABEL maintainer="Isaiah Dallas Jefferson, Jr. <idallasj@gmail.com>"
LABEL org.agentshroud.component="voice-gateway"

# Non-root user (UID 1001) for least-privilege operation
RUN useradd -m -u 1001 -s /sbin/nologin vg

WORKDIR /app

# System deps: kokoro needs espeak-ng for phonemization; faster-whisper needs ffmpeg
RUN apt-get update -qq && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        ffmpeg \
        libsndfile1 \
        espeak-ng \
        curl \
    && rm -rf /var/lib/apt/lists/*

COPY voice_gateway/requirements.txt .
# --retries/--timeout: the multi-GB wheel downloads (torch chain) die on
# transient network faults from this host (PyPI read timeout + SSL record
# failure, two of three consecutive build failures on 2026-08-30); per-package
# retries let a blip cost seconds instead of the whole build.
RUN pip install --no-cache-dir --retries 10 --timeout 60 -r requirements.txt

# Pre-bake the Kokoro TTS model weights so runtime needs ZERO egress.
# voice-gateway runs on agentshroud-isolated; HF_HUB_OFFLINE=1 blocks all
# outbound at runtime.  We download here at build time while internet is available.
ENV HF_HOME=/opt/hf-cache
RUN python -c "from kokoro import KPipeline; pipe = KPipeline(lang_code='a'); pipe.load_voice('af_heart'); pipe.load_voice('af_bella')" && \
    chmod -R a+rX /opt/hf-cache

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

ENV KOKORO_VOICE=af_heart
ENV KOKORO_SPEED=1.0
ENV VG_HOST=0.0.0.0
ENV VG_PORT=8765

USER vg
EXPOSE 8765

HEALTHCHECK --interval=30s --timeout=5s --start-period=60s --retries=3 \
    CMD curl -f http://localhost:8765/health || exit 1

CMD ["python", "-m", "voice_gateway"]
