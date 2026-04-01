# AgentShroud Deployment Architecture

## Overview

AgentShroud supports flexible deployment patterns optimized for different operational requirements and container runtime environments. The system provides two primary deployment modes: **Proxy Mode** for maximum security isolation and **Sidecar Mode** for performance-critical scenarios requiring minimal latency.

## Deployment Modes

### Proxy Mode (Recommended)

Proxy mode implements complete network isolation with AgentShroud as the sole gateway to OpenClaw agents:

```
┌─────────────────────────────────────────────────────────────────────┐
│                        Docker Host Environment                      │
│                                                                     │
│  ┌─ External Network (agentshroud_external) ─────────────────────┐   │
│  │                                                              │   │
│  │    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │   │
│  │    │   Ingress   │    │  Dashboard  │    │  Metrics    │     │   │
│  │    │   Nginx     │◄──►│   WebApp    │◄──►│ Collector   │     │   │
│  │    │ :80/:443    │    │   :3000     │    │   :9090     │     │   │
│  │    └─────┬───────┘    └─────────────┘    └─────────────┘     │   │
│  └──────────┼───────────────────────────────────────────────────┘   │
│             │                                                       │
│  ┌─ Management Network (agentshroud_mgmt) ─────────┐                 │
│  │          │                                     │                 │
│  │    ┌─────▼───────┐    ┌─────────────┐          │                 │
│  │    │ AgentShroud  │    │   SQLite    │          │                 │
│  │    │  Gateway    │◄──►│  Database   │          │                 │
│  │    │   :8080     │    │  (Volume)   │          │                 │
│  │    └─────┬───────┘    └─────────────┘          │                 │
│  └──────────┼─────────────────────────────────────┘                 │
│             │                                                       │
│  ┌─ Internal Network (agentshroud_internal) ───────┐                 │
│  │          │                                     │                 │
│  │    ┌─────▼───────┐    ┌─────────────┐          │                 │
│  │    │ OpenClaw    │    │  Memory/    │          │                 │
│  │    │   Agent     │◄──►│  Skills     │          │                 │
│  │    │ (Isolated)  │    │  Storage    │          │                 │
│  │    └─────────────┘    └─────────────┘          │                 │
│  └─────────────────────────────────────────────────┘                 │
└─────────────────────────────────────────────────────────────────────┘
```

### Sidecar Mode (Performance Optimized)

Sidecar mode co-locates AgentShroud with OpenClaw for reduced latency while maintaining security controls:

```
┌─────────────────────────────────────────────────────────────────────┐
│                        Docker Host Environment                      │
│                                                                     │
│  ┌─ Shared Network (agentshroud_shared) ──────────────────────────┐   │
│  │                                                             │   │
│  │  ┌─────────────┐                    ┌─────────────┐         │   │
│  │  │  External   │                    │ AgentShroud  │         │   │
│  │  │  Traffic    │───── Traffic ────►│  Gateway    │         │   │
│  │  │   :80/443   │      Flow         │   :8080     │         │   │
│  │  └─────────────┘                    └──────┬──────┘         │   │
│  │                                            │                │   │
│  │                   Local Network            │                │   │
│  │                   Communication            │                │   │
│  │                        │                   │                │   │
│  │  ┌─────────────┐       │            ┌─────▼───────┐         │   │
│  │  │ OpenClaw    │◄──────┴────────────┤ OpenClaw    │         │   │
│  │  │ Agent Core  │    Shared Memory    │ Agent Sidecar│        │   │
│  │  │             │    Communication    │ (AgentShroud)│         │   │
│  │  └─────────────┘                    └─────────────┘         │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

## Multi-Runtime Support

### Docker Runtime

Standard Docker deployment using docker-compose:

```yaml
# docker-compose.yml
version: '3.8'

services:
  agentshroud-gateway:
    image: agentshroud/gateway:latest
    container_name: agentshroud-gateway
    networks:
      - agentshroud_external
      - agentshroud_internal
    ports:
      - "${AGENTSHROUD_PORT:-8080}:8080"
    volumes:
      - agentshroud_config:/app/config
      - agentshroud_audit:/app/audit
      - /var/run/docker.sock:/var/run/docker.sock:ro
    environment:
      - AGENTSHROUD_MODE=proxy
      - OPENCLAW_INTERNAL_URL=http://openclaw:8000
      - DATABASE_URL=sqlite:///app/data/audit.db
    depends_on:
      - openclaw-agent
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  openclaw-agent:
    image: openclaw/agent:latest
    container_name: openclaw-agent
    networks:
      - agentshroud_internal
    volumes:
      - openclaw_workspace:/workspace
      - openclaw_memory:/app/memory
    environment:
      - OPENCLAW_WORKSPACE=/workspace
      - OPENCLAW_SECURITY_MODE=transparent
    restart: unless-stopped

networks:
  agentshroud_external:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/24
          gateway: 172.20.0.1
  agentshroud_internal:
    driver: bridge
    internal: true
    ipam:
      config:
        - subnet: 172.21.0.0/24
          gateway: 172.21.0.1

volumes:
  agentshroud_config:
    driver: local
  agentshroud_audit:
    driver: local
  openclaw_workspace:
    driver: local
  openclaw_memory:
    driver: local
```

### Podman Support

Podman deployment with rootless containers and systemd integration:

```yaml
# podman-compose.yml
version: '3.8'

services:
  agentshroud-gateway:
    image: agentshroud/gateway:latest
    container_name: agentshroud-gateway
    security_opt:
      - label=type:container_runtime_t
    networks:
      - agentshroud_external
      - agentshroud_internal
    ports:
      - "${AGENTSHROUD_PORT:-8080}:8080"
    volumes:
      - agentshroud_config:/app/config:Z
      - agentshroud_audit:/app/audit:Z
      - /run/user/${UID}/podman/podman.sock:/var/run/docker.sock:ro
    environment:
      - CONTAINER_RUNTIME=podman
      - AGENTSHROUD_MODE=proxy
    user: "${UID}:${GID}"
    userns_mode: keep-id
    restart: unless-stopped

networks:
  agentshroud_external:
    driver: bridge
  agentshroud_internal:
    driver: bridge
    internal: true
```

### Apple Containers (macOS)

Native macOS deployment using Apple's container runtime:

```yaml
# docker-compose.darwin.yml
version: '3.8'

services:
  agentshroud-gateway:
    platform: linux/arm64
    image: agentshroud/gateway:arm64
    ports:
      - "${AGENTSHROUD_PORT:-8080}:8080"
    networks:
      - agentshroud_external
      - agentshroud_internal
    volumes:
      - type: bind
        source: /Users/Shared/AgentShroud/config
        target: /app/config
      - type: bind
        source: /Users/Shared/AgentShroud/audit
        target: /app/audit
    environment:
      - CONTAINER_RUNTIME=apple
      - MACOS_KEYCHAIN_INTEGRATION=enabled
    extra_hosts:
      - "host.docker.internal:host-gateway"
```

## Network Topology

### Three-Network Architecture

AgentShroud implements a three-tier network model for maximum security:

```
Internet
   │
   ▼
┌─────────────────────────────────────────────┐
│          External Network                   │
│        (agentshroud_external)                │
│    ┌─────────────┐    ┌─────────────┐       │
│    │   Ingress   │    │  Dashboard  │       │
│    │   Proxy     │    │    Web      │       │ ◄── DMZ Zone
│    │ (Public IP) │    │  Interface  │       │
│    └─────┬───────┘    └─────────────┘       │
└──────────┼─────────────────────────────────────┘
           │
    ┌──────▼──────┐
    │  AgentShroud │
    │   Gateway   │ ◄── Security Enforcement Point
    │ (Dual-Homed)│
    └──────┬──────┘
           │
┌──────────▼─────────────────────────────────────┐
│         Management Network                     │
│        (agentshroud_mgmt)                       │
│  ┌─────────────┐    ┌─────────────┐            │ ◄── Control Plane
│  │  Security   │    │   Audit     │            │
│  │  Modules    │    │  Database   │            │
│  └─────┬───────┘    └─────────────┘            │
└────────┼──────────────────────────────────────────┘
         │
┌────────▼──────────────────────────────────────┐
│         Internal Network                      │
│       (agentshroud_internal)                   │
│  ┌─────────────┐    ┌─────────────┐           │ ◄── Protected Zone
│  │  OpenClaw   │    │   Memory    │           │
│  │   Agent     │    │   Storage   │           │
│  └─────────────┘    └─────────────┘           │
└─────────────────────────────────────────────────┘
```

### DNS Routing Configuration

AgentShroud provides intelligent DNS routing for service discovery:

```
┌─────────────────────────────────────────────────────────────┐
│                    DNS Resolution Flow                      │
│                                                             │
│  External Domain          AgentShroud DNS         Internal   │
│  Resolution               Filter & Router        Services   │
│                                                             │
│  api.example.com ────────► DNS Filter ─────────► Gateway   │
│                           │                     Service    │
│  *.openclaw.local ───────►│ Block/Allow ──────► OpenClaw   │
│                           │ Lists              Agent       │
│  malicious.domain ───────►│                                │
│                           ▼                               │
│                        [BLOCKED]                          │
│                                                           │
│  Internal DNS Mapping:                                    │
│  • gateway.agentshroud.local    → 172.20.0.2              │
│  • agent.agentshroud.local      → 172.21.0.2              │
│  • dashboard.agentshroud.local  → 172.20.0.3              │
│  • audit.agentshroud.local      → 172.21.0.3              │
└─────────────────────────────────────────────────────────────┘
```

## Port Mappings and Auto-Detection

### Default Port Allocation

```
Component               Default Port    Auto-Detect Range
─────────────────────────────────────────────────────────
AgentShroud Gateway      8080           8080-8089
Dashboard Web UI        3000           3000-3009
OpenClaw Agent         8000           8000-8009
SSH Proxy              2222           2222-2229
MCP Proxy              8888           8888-8897
Prometheus Metrics     9090           9090-9099
Health Check           9999           9999-9999
```

### Multi-Instance Support

AgentShroud automatically detects port conflicts and assigns available ports:

```python
# Port Auto-Detection Algorithm
def find_available_port(base_port: int, instance_id: int) -> int:
    """
    Auto-detect available ports for multi-instance deployments
    """
    candidate_port = base_port + instance_id
    max_attempts = 10
    
    for attempt in range(max_attempts):
        port = candidate_port + attempt
        if is_port_available(port):
            return port
    
    raise PortExhaustionError(f"No available ports in range {base_port}-{base_port + max_attempts}")

# Environment Variable Substitution
AGENTSHROUD_GATEWAY_PORT=${AGENTSHROUD_PORT_BASE:-8080}
AGENTSHROUD_INSTANCE_ID=${AGENTSHROUD_INSTANCE:-0}
```

## Volume Mounts and Secrets Management

### Persistent Storage Architecture

```
Host Filesystem                    Container Mount Points
───────────────                   ─────────────────────
/opt/agentshroud/
├── config/
│   ├── gateway.yaml         ───► /app/config/gateway.yaml
│   ├── security.yaml        ───► /app/config/security.yaml
│   └── trust-policies.yaml  ───► /app/config/trust-policies.yaml
├── data/
│   ├── audit.db            ───► /app/data/audit.db
│   ├── approval-queue.db   ───► /app/data/approval-queue.db
│   └── trust-scores.json   ───► /app/data/trust-scores.json
├── logs/
│   ├── gateway.log         ───► /app/logs/gateway.log
│   ├── security.log        ───► /app/logs/security.log
│   └── audit.log           ───► /app/logs/audit.log
└── secrets/
    ├── tls-certificates/   ───► /app/certs/
    ├── api-keys.env        ───► /run/secrets/api-keys
    └── signing-key.pem     ───► /run/secrets/signing-key
```

### Secrets Management Integration

AgentShroud supports multiple secrets management backends:

#### Docker Secrets
```yaml
secrets:
  api_keys:
    file: ./secrets/api-keys.env
  tls_cert:
    external: true
    external_name: agentshroud_tls_cert
  signing_key:
    external: true
    external_name: agentshroud_signing_key

services:
  agentshroud-gateway:
    secrets:
      - source: api_keys
        target: /run/secrets/api-keys
        uid: '1000'
        gid: '1000'
        mode: 0400
```

#### HashiCorp Vault Integration
```yaml
environment:
  - VAULT_ADDR=https://vault.example.com
  - VAULT_ROLE=agentshroud-gateway
  - VAULT_AUTH_METHOD=kubernetes
  - VAULT_SECRET_PATH=secret/agentshroud/production
```

#### Cloud Provider Secrets
```yaml
# AWS Secrets Manager
environment:
  - AWS_REGION=us-west-2
  - AWS_SECRETS_MANAGER_ARN=arn:aws:secretsmanager:us-west-2:123456789:secret:agentshroud-prod

# Azure Key Vault
environment:
  - AZURE_KEYVAULT_URL=https://agentshroud.vault.azure.net/
  - AZURE_CLIENT_ID=${AZURE_CLIENT_ID}
  - AZURE_TENANT_ID=${AZURE_TENANT_ID}
```

## Zero-Configuration Deployment

AgentShroud achieves "docker-compose up = fully secured" through intelligent defaults and auto-configuration:

```bash
# Complete deployment in three commands
git clone https://github.com/idallasjlabs/agentshroud.git
cd agentshroud/deployments/agentshroud
docker-compose up -d

# Automatic configuration includes:
# - Network isolation setup
# - Security module initialization
# - Default security policies
# - Audit trail initialization
# - Trust level baseline establishment
# - Health monitoring activation
```

### Deployment Validation

Automated deployment validation ensures security posture:

```bash
#!/bin/bash
# deployment-validator.sh

echo "🔍 Validating AgentShroud deployment..."

# Network isolation check
docker network inspect agentshroud_internal | jq '.Internal' | grep -q true || {
    echo "❌ Internal network not properly isolated"
    exit 1
}

# Security module health check
curl -sf http://localhost:8080/health/security || {
    echo "❌ Security modules not responding"
    exit 1
}

# Audit system verification
curl -sf http://localhost:8080/audit/chain/verify || {
    echo "❌ Audit hash chain invalid"
    exit 1
}

echo "✅ AgentShroud deployment validated successfully"
```

This deployment architecture ensures AgentShroud provides robust security controls while maintaining operational simplicity and supporting diverse container runtime environments.