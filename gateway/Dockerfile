# Multi-stage Dockerfile for AgentShroud Gateway
# Stage 1: Builder - Install dependencies and spaCy model
# Stage 2: Runtime - Non-root user, minimal image

# === Builder Stage ===
# M8: Base image pinned to SHA256 digest for supply chain integrity
FROM python:3.13-slim@sha256:3de9a8d7aedbb7984dc18f2dff178a7850f16c1ae7c34ba9d7ecc23d0755e35f AS builder

WORKDIR /build
ENV PIP_ROOT_USER_ACTION=ignore
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies for building Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY gateway/requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# === Runtime Stage ===
FROM python:3.13-slim@sha256:3de9a8d7aedbb7984dc18f2dff178a7850f16c1ae7c34ba9d7ecc23d0755e35f

WORKDIR /app
ENV PIP_ROOT_USER_ACTION=ignore
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies: OpenSCAP (compliance), SSH client, ClamAV (malware scanning), 1Password CLI
RUN apt-get update && apt-get install -y --no-install-recommends \
    libopenscap33 \
    openscap-scanner \
    openssh-client \
    clamav clamav-daemon clamav-freshclam clamdscan \
    curl ca-certificates gpg \
    && mkdir -p /var/lib/clamav \
    && (freshclam --quiet 2>/dev/null || echo "freshclam: virus DB download deferred to runtime") \
    && curl -sS https://downloads.1password.com/linux/keys/1password.asc \
        | gpg --dearmor --output /usr/share/keyrings/1password-archive-keyring.gpg \
    && arch=$(dpkg --print-architecture) \
    && echo "deb [arch=${arch} signed-by=/usr/share/keyrings/1password-archive-keyring.gpg] https://downloads.1password.com/linux/debian/${arch} stable main" \
        > /etc/apt/sources.list.d/1password.list \
    && apt-get update && apt-get install -y --no-install-recommends 1password-cli \
    && rm -rf /var/lib/apt/lists/*

# Syft SBOM generator — pinned version
ARG SYFT_VERSION=1.18.1
RUN DPKG_ARCH=$(dpkg --print-architecture) && \
    case "$DPKG_ARCH" in \
      arm64) SYFT_ARCH="arm64" ;; \
      amd64) SYFT_ARCH="amd64" ;; \
      armhf) SYFT_ARCH="arm" ;; \
      *) SYFT_ARCH="$DPKG_ARCH" ;; \
    esac && \
    curl -sSfL -o "/tmp/syft_${SYFT_VERSION}_linux_${SYFT_ARCH}.deb" \
        "https://github.com/anchore/syft/releases/download/v${SYFT_VERSION}/syft_${SYFT_VERSION}_linux_${SYFT_ARCH}.deb" && \
    dpkg -i "/tmp/syft_${SYFT_VERSION}_linux_${SYFT_ARCH}.deb" && \
    rm "/tmp/syft_${SYFT_VERSION}_linux_${SYFT_ARCH}.deb"

# Docker CLI — for container scanning via mounted Docker socket (no daemon)
ARG DOCKER_CLI_VERSION=27.3.1
RUN DPKG_ARCH=$(dpkg --print-architecture) && \
    curl -sSfL -o "/tmp/docker-${DOCKER_CLI_VERSION}.tgz" \
        "https://download.docker.com/linux/static/stable/${DPKG_ARCH}/docker-${DOCKER_CLI_VERSION}.tgz" && \
    tar xzf "/tmp/docker-${DOCKER_CLI_VERSION}.tgz" --strip-components=1 -C /usr/local/bin/ docker/docker && \
    rm "/tmp/docker-${DOCKER_CLI_VERSION}.tgz"

# Trivy vulnerability scanner — pinned version (M7 fix)
ARG TRIVY_VERSION=0.69.3
# R2-M1: Download Trivy with checksum verification for supply chain integrity
RUN DPKG_ARCH=$(dpkg --print-architecture) && \
    case "$DPKG_ARCH" in \
      arm64) TRIVY_ARCH="ARM64" ;; \
      amd64) TRIVY_ARCH="64bit" ;; \
      armhf) TRIVY_ARCH="ARM" ;; \
      *) TRIVY_ARCH="$DPKG_ARCH" ;; \
    esac && \
    curl -sSfL -o "/tmp/trivy_${TRIVY_VERSION}_Linux-${TRIVY_ARCH}.deb" \
        "https://github.com/aquasecurity/trivy/releases/download/v${TRIVY_VERSION}/trivy_${TRIVY_VERSION}_Linux-${TRIVY_ARCH}.deb" && \
    curl -sSfL -o /tmp/trivy_checksums.txt \
        "https://github.com/aquasecurity/trivy/releases/download/v${TRIVY_VERSION}/trivy_${TRIVY_VERSION}_checksums.txt" && \
    cd /tmp && grep "trivy_${TRIVY_VERSION}_Linux-${TRIVY_ARCH}.deb" trivy_checksums.txt | sha256sum -c - && \
    dpkg -i "/tmp/trivy_${TRIVY_VERSION}_Linux-${TRIVY_ARCH}.deb" && \
    rm "/tmp/trivy_${TRIVY_VERSION}_Linux-${TRIVY_ARCH}.deb" /tmp/trivy_checksums.txt

# Create non-root user
RUN useradd --create-home --shell /bin/bash --uid 1000 agentshroud

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy application code
COPY gateway/ /app/gateway/

# Create data directory (volume will be mounted here) and set ownership
RUN mkdir -p /app/data && \
    chown -R agentshroud:agentshroud /app

# Copy SCAP content for compliance scanning (from parent context)
RUN mkdir -p /usr/share/xml/scap/ssg/content
COPY docker/scap-content/ssg-debian12-ds.xml /usr/share/xml/scap/ssg/content/

# OCI Image labels
LABEL org.opencontainers.image.title="AgentShroud Gateway"
LABEL org.opencontainers.image.description="PII sanitization proxy for AgentShroud"
LABEL org.opencontainers.image.vendor="AgentShroud"
LABEL org.opencontainers.image.version="0.9.0"
LABEL org.opencontainers.image.source="https://github.com/idallasj/agentshroud"

# Prevent Python bytecode generation (read-only filesystem compatibility)
ENV PYTHONDONTWRITEBYTECODE=1
# Redirect op CLI config to tmpfs mount (read-only root filesystem)
ENV XDG_CONFIG_HOME=/tmp

# Copy security scripts
COPY docker/scripts/security-entrypoint.sh /usr/local/bin/security-entrypoint.sh
COPY docker/scripts/security-scheduler.sh /usr/local/bin/security-scheduler.sh
COPY docker/scripts/security-scan.sh /usr/local/bin/security-scan.sh
COPY docker/scripts/security-report.sh /usr/local/bin/security-report.sh
RUN chmod +x /usr/local/bin/security-*.sh

# Create security log directory
RUN mkdir -p /var/log/security && chown agentshroud:agentshroud /var/log/security

# Download spaCy NLP model for PII detection (560MB, cached in Docker layer)
RUN python3 -m spacy download en_core_web_sm >/tmp/spacy-download.log 2>&1 \
    || echo "spaCy model download skipped (offline) — regex fallback enabled"

# Copy repo root files needed by tests
COPY README.md /app/README.md
COPY SECURITY.md /app/SECURITY.md
COPY CONTRIBUTING.md /app/CONTRIBUTING.md
# SDL config files for Secure Development scorer (Domain 11)
COPY .semgrep.yml /app/.semgrep.yml
COPY .pre-commit-config.yaml /app/.pre-commit-config.yaml
COPY gitleaks.toml /app/gitleaks.toml
COPY examples/ /app/examples/
COPY docker/docker-compose.yml /app/docker/docker-compose.yml
COPY pytest.ini /app/pytest.ini
COPY docker/scripts/killswitch.sh /app/docker/scripts/killswitch.sh
COPY docker/scripts/start-agentshroud.sh /app/docker/scripts/start-agentshroud.sh
COPY docker/scripts/init-openclaw-config.sh /app/docker/scripts/init-openclaw-config.sh
COPY docker/config/openclaw/apply-patches.js /app/docker/config/openclaw/apply-patches.js
COPY docker/Dockerfile.agentshroud /app/docker/Dockerfile.agentshroud
COPY docker/bots/openclaw/Dockerfile /app/docker/bots/openclaw/Dockerfile
COPY docker/bots/openclaw/start.sh /app/docker/bots/openclaw/start.sh
COPY scripts/start-control-center /app/scripts/start-control-center
COPY scripts/chat-console /app/scripts/chat-console
COPY scripts/switch_model.sh /app/scripts/switch_model.sh

# Switch to non-root user
# Strip setuid/setgid bits — CIS Docker Benchmark 4.8
RUN find / -perm /6000 -type f -exec chmod a-s {} + 2>/dev/null || true

USER agentshroud

# Expose gateway port
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/status').read()" || exit 1

# Set Python path to include parent directory
ENV PYTHONPATH=/app

# Run gateway (bind to 0.0.0.0 for Docker port mapping to work)
# Security: docker-compose maps only to host 127.0.0.1
CMD ["uvicorn", "gateway.ingest_api.main:app", "--host", "0.0.0.0", "--port", "8080"]
