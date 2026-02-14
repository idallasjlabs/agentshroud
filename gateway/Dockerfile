# Multi-stage Dockerfile for SecureClaw Gateway
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
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Download spaCy model (this will fail gracefully, fallback to regex works)
RUN /install/bin/python -m spacy download en_core_web_lg || echo "spaCy model download failed, will use regex fallback"

# === Runtime Stage ===
FROM python:3.13-slim

WORKDIR /app

# Create non-root user
RUN useradd --create-home --shell /bin/bash --uid 1000 secureclaw

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy application code
COPY . /app/gateway/

# Create data directory and set ownership
RUN mkdir -p /app/gateway/data && \
    chown -R secureclaw:secureclaw /app

# Switch to non-root user
USER secureclaw

# Expose gateway port
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/status').read()" || exit 1

# Set Python path to include parent directory
ENV PYTHONPATH=/app

# Run gateway
CMD ["uvicorn", "gateway.ingest_api.main:app", "--host", "127.0.0.1", "--port", "8080"]
