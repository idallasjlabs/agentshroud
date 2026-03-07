# NanoBot (HKUDS) — Python agent template for AgentShroud encapsulation.
#
# This Dockerfile is a starting template. Adapt it to the specific NanoBot
# package and entry point once the bot is integrated.
#
# Required env vars set by AgentShroud (gateway's docker-compose.yml):
#   ANTHROPIC_BASE_URL           http://gateway:8080
#   HTTP_PROXY / HTTPS_PROXY     http://gateway:8181
#   AGENTSHROUD_GATEWAY_PASSWORD gateway auth token
#   AGENTSHROUD_BOT_ID           nanobot
#   AGENTSHROUD_WORKSPACE        /app/workspace

FROM python:3.12-slim

# Security hardening
RUN groupadd -r botuser && useradd -r -g botuser botuser

WORKDIR /app

# Install bot dependencies (replace with actual NanoBot requirements)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

RUN mkdir -p /app/workspace /app/config && \
    chown -R botuser:botuser /app

USER botuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health').read()"

CMD ["/app/start.sh"]
