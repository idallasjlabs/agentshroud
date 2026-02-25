# Multi-stage Dockerfile for AgentShroud Gateway
# Stage 1: Builder - Install dependencies and spaCy model
# Stage 2: Runtime - Non-root user, minimal image

# === Builder Stage ===
FROM python:3.13-slim AS builder

WORKDIR /build

# Install system dependencies for building Python packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY gateway/requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# === Runtime Stage ===
FROM python:3.13-slim

WORKDIR /app

# Install OpenSCAP for compliance scanning (Debian Trixie = libopenscap33)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libopenscap33 \
    openscap-scanner \
    && rm -rf /var/lib/apt/lists/*

# ClamAV for malware scanning
RUN apt-get update && apt-get install -y --no-install-recommends \
    clamav clamav-daemon clamav-freshclam clamdscan \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir -p /var/lib/clamav \n    && freshclam --quiet 2>/dev/null || echo "freshclam: virus DB download deferred to runtime"

# Install 1Password CLI for op-proxy credential broker
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates gpg \
    && curl -sS https://downloads.1password.com/linux/keys/1password.asc \
        | gpg --dearmor --output /usr/share/keyrings/1password-archive-keyring.gpg \
    && arch=$(dpkg --print-architecture) \
    && echo "deb [arch=${arch} signed-by=/usr/share/keyrings/1password-archive-keyring.gpg] https://downloads.1password.com/linux/debian/${arch} stable main" \
        > /etc/apt/sources.list.d/1password.list \
    && apt-get update && apt-get install -y --no-install-recommends 1password-cli \
    && rm -rf /var/lib/apt/lists/*

# Trivy vulnerability scanner (ARM64 compatible)
RUN curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin

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
LABEL org.opencontainers.image.version="0.7.0"
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
RUN python3 -m spacy download en_core_web_sm || echo "spaCy model download failed — will use regex fallback"

# Copy repo root files needed by tests
COPY README.md /app/README.md
COPY SECURITY.md /app/SECURITY.md
COPY CONTRIBUTING.md /app/CONTRIBUTING.md
COPY examples/ /app/examples/
COPY docker/docker-compose.yml /app/docker/docker-compose.yml
COPY pytest.ini /app/pytest.ini
COPY docker/scripts/killswitch.sh /app/docker/scripts/killswitch.sh

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
