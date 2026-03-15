# AgentShroud Container - Powered by OpenClaw
# Goal: Full OpenClaw features (agents, skills, MCP) with bot identity
# Base: Node.js 22 (required by OpenClaw)
# OpenClaw source: https://github.com/openclaw/openclaw

# M8: Base image pinned to SHA256 digest for supply chain integrity
# Update with: docker pull node:22-bookworm-slim && docker inspect --format='{{index .RepoDigests 0}}' node:22-bookworm-slim
FROM node:22-bookworm-slim@sha256:5373f1906319b3a1f291da5d102f4ce5c77ccbe29eb637f072b6c7b70443fc36
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        openssh-client \
        netcat-openbsd \
        git \
        curl \
        ca-certificates \
        unzip \
        libopenscap25 \
        openscap-scanner \
        gosu \
        gnupg \
        clamav clamav-daemon clamav-freshclam \
    && apt-get clean && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

# Trivy vulnerability scanner — pinned version with checksum verification (M7 fix)
ARG TRIVY_VERSION=0.69.3
# R2-M1: Download Trivy with checksum verification for supply chain integrity
RUN DPKG_ARCH=$(dpkg --print-architecture) && \
    case "$DPKG_ARCH" in \
      arm64) TRIVY_ARCH="ARM64" ;; \
      amd64) TRIVY_ARCH="64bit" ;; \
      armhf) TRIVY_ARCH="ARM" ;; \
      *) TRIVY_ARCH="$DPKG_ARCH" ;; \
    esac &&     curl -sSfL -o "/tmp/trivy_${TRIVY_VERSION}_Linux-${TRIVY_ARCH}.deb"         "https://github.com/aquasecurity/trivy/releases/download/v${TRIVY_VERSION}/trivy_${TRIVY_VERSION}_Linux-${TRIVY_ARCH}.deb" &&     curl -sSfL -o /tmp/trivy_checksums.txt         "https://github.com/aquasecurity/trivy/releases/download/v${TRIVY_VERSION}/trivy_${TRIVY_VERSION}_checksums.txt" &&     cd /tmp && grep "trivy_${TRIVY_VERSION}_Linux-${TRIVY_ARCH}.deb" trivy_checksums.txt | sha256sum -c - &&     dpkg -i "/tmp/trivy_${TRIVY_VERSION}_Linux-${TRIVY_ARCH}.deb" &&     rm "/tmp/trivy_${TRIVY_VERSION}_Linux-${TRIVY_ARCH}.deb" /tmp/trivy_checksums.txt

# ClamAV DB directory
RUN mkdir -p /var/lib/clamav

# Install bun via npm (avoids curl|bash supply chain risk)
# M8: Pin bun to specific version for reproducible builds
RUN npm install -g bun@1.2.4

# Enable pnpm (OpenClaw uses pnpm for package management)
RUN corepack enable

# Set working directory
WORKDIR /app

# Install OpenClaw from npm registry (pinned version for reproducible builds)
RUN npm install -g openclaw@2026.3.8
# SECURITY: Route LLM API through AgentShroud gateway
COPY docker/scripts/patch-anthropic-sdk.sh /tmp/patch-anthropic-sdk.sh
RUN sh /tmp/patch-anthropic-sdk.sh && rm /tmp/patch-anthropic-sdk.sh

# Install Playwright for browser automation (browser-fetch skill)
RUN npm install -g playwright@1.50.1 && \
    npx playwright install --with-deps chromium

# SECURITY: Route Telegram API through AgentShroud gateway
# NOTE: placed after Playwright to preserve the expensive Playwright cache layer
COPY docker/scripts/patch-telegram-sdk.sh /tmp/patch-telegram-sdk.sh
RUN sh /tmp/patch-telegram-sdk.sh && rm /tmp/patch-telegram-sdk.sh
# Install 1Password CLI for secure secret management (multi-arch)
# R2-H1: GPG signature verification for supply chain integrity
RUN curl -sS https://downloads.1password.com/linux/keys/1password.asc | \
    gpg --dearmor --output /usr/share/keyrings/1password-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/1password-archive-keyring.gpg] https://downloads.1password.com/linux/debian/$(dpkg --print-architecture) stable main" | \
    tee /etc/apt/sources.list.d/1password.list && \
    apt-get update && apt-get install -y --no-install-recommends 1password-cli \
    && rm -rf /var/lib/apt/lists/*
# Create directories for AgentShroud configuration and workspace
# Create directories for AgentShroud configuration and workspace
# Note: OpenClaw CLI expects ~/.openclaw, so we symlink it to ~/.agentshroud
RUN mkdir -p /home/node/.agentshroud && \
    ln -s /home/node/.agentshroud /home/node/.openclaw && \
    mkdir -p /home/node/agentshroud/workspace && \
    mkdir -p /home/node/.ssh && \
    chown -R node:node /home/node

# Copy SCAP content for compliance scanning
RUN mkdir -p /usr/share/xml/scap/ssg/content
COPY docker/scap-content/ssg-debian12-ds.xml /usr/share/xml/scap/ssg/content/

# Copy startup and utility scripts
COPY docker/scripts/security-entrypoint.sh /usr/local/bin/security-entrypoint.sh
COPY docker/scripts/security-scheduler.sh /usr/local/bin/security-scheduler.sh
COPY docker/scripts/security-scan.sh /usr/local/bin/security-scan.sh
COPY docker/scripts/security-report.sh /usr/local/bin/security-report.sh
COPY docker/scripts/op-auth-common.sh /usr/local/bin/op-auth-common.sh
COPY docker/scripts/start-agentshroud.sh /usr/local/bin/start-agentshroud.sh
COPY docker/scripts/op-wrapper.sh /usr/local/bin/op-wrapper.sh
COPY docker/scripts/get-credential.sh /usr/local/bin/get-credential
COPY docker/scripts/1password-skill.sh /usr/local/bin/1password-skill
COPY docker/scripts/entrypoint-agentshroud.sh /usr/local/bin/entrypoint-agentshroud.sh
COPY docker/scripts/init-openclaw-config.sh /usr/local/bin/init-openclaw-config.sh
COPY docker/scripts/mcp-proxy-wrapper.js /usr/local/bin/mcp-proxy-wrapper.js
COPY docker/scripts/container-net-diag.sh /app/scripts/container-net-diag.sh

# Bake in OpenClaw config defaults (cron jobs, agent patches)
# Applied to the volume on every startup by init-openclaw-config.sh
COPY docker/config/openclaw/ /app/config-defaults/openclaw/

# Bake in collaborator workspace defaults (anti-hallucination rules, public info)
# Applied to the collaborator workspace on every startup by init-openclaw-config.sh
COPY docker/bots/openclaw/workspace/collaborator-workspace/ /app/config-defaults/openclaw/collaborator-workspace/

# Bake in SSH allowlist config (approved hosts, key-only auth)
# Applied to /home/node/.ssh/config on every startup by init-openclaw-config.sh
COPY docker/config/ssh/ /app/config-defaults/ssh/

# Bake in Claude Code config (agents, skills, hooks, ORCHESTRATOR.md)
# Applied to workspace/.claude/ on every startup by init-openclaw-config.sh
COPY .claude/ /app/config-defaults/claude/

RUN chmod +x /usr/local/bin/security-entrypoint.sh \
    /usr/local/bin/security-scheduler.sh \
    /usr/local/bin/security-scan.sh \
    /usr/local/bin/security-report.sh \
    /usr/local/bin/op-auth-common.sh \
    /usr/local/bin/start-agentshroud.sh \
    /usr/local/bin/op-wrapper.sh \
    /usr/local/bin/get-credential \
    /usr/local/bin/1password-skill \
    /usr/local/bin/entrypoint-agentshroud.sh \
    /usr/local/bin/init-openclaw-config.sh \
    /usr/local/bin/mcp-proxy-wrapper.js

# Copy documentation
COPY docker/bot-capabilities.md /app/bot-capabilities.md
COPY docker/SYSTEM-INSTRUCTIONS-SECURITY.md /app/SYSTEM-INSTRUCTIONS-SECURITY.md

# OCI Image labels
LABEL org.opencontainers.image.title="AgentShroud Bot"
LABEL org.opencontainers.image.description="AgentShroud platform for agentshroud bot"
LABEL org.opencontainers.image.vendor="AgentShroud"
LABEL org.opencontainers.image.version="0.8.0"
LABEL org.opencontainers.image.source="https://github.com/idallasj/agentshroud"

# SECURITY (M2): Remove unnecessary interpreter entrypoints from PATH.
# Avoid purging essential base packages to keep image builds warning-free.
RUN rm -f /usr/bin/perl /usr/bin/perl5* 2>/dev/null || true

# Strip setuid/setgid bits — CIS Docker Benchmark 4.8 (R2-H2 fix)
RUN find / -perm /6000 -type f -exec chmod a-s {} + 2>/dev/null || true

# Switch to non-root user (node user has UID 1000)
USER node
ENV HOME=/home/node
WORKDIR /home/node

# Expose AgentShroud gateway port
EXPOSE 18789

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
    CMD curl -sf http://localhost:18789/ -o /dev/null || exit 1

# Start AgentShroud gateway via wrapper script
CMD ["/usr/local/bin/start-agentshroud.sh"]
