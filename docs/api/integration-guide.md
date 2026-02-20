# Integration Guide
## AgentShroud v0.9.0

### Overview

This guide provides comprehensive instructions for integrating AgentShroud with various systems and platforms. AgentShroud is designed as a transparent security proxy that can be integrated with minimal configuration changes to existing AI agent infrastructure.

---

## OpenClaw Integration (Primary Target)

AgentShroud is purpose-built for OpenClaw AI agents, providing seamless integration with transparent proxy functionality.

### Architecture Overview

```
[User] → [AgentShroud Proxy] → [OpenClaw Agent] → [External Services]
                ↓
        [Security Modules] → [Audit System]
```

### Configuration

**1. Docker Compose Integration**

Add AgentShroud to your existing OpenClaw deployment:

```yaml
version: '3.8'
services:
  agentshroud:
    image: agentshroud:0.9.0
    ports:
      - "8443:8443"
    environment:
      - OPENCLAW_UPSTREAM=http://openclaw:3000
      - SECURITY_LEVEL=enforce
      - AUDIT_ENABLED=true
    volumes:
      - ./config:/app/config
      - agentshroud-data:/app/data
    networks:
      - openclaw-net

  openclaw:
    image: openclaw:latest
    environment:
      - PROXY_MODE=true
      - PROXY_ENDPOINT=http://agentshroud:8080
    networks:
      - openclaw-net
    depends_on:
      - agentshroud

volumes:
  agentshroud-data:

networks:
  openclaw-net:
    driver: bridge
```

**2. Environment Configuration**

```bash
# AgentShroud Configuration
export AGENTSHROUD_MODE=proxy
export AGENTSHROUD_UPSTREAM=http://localhost:3000
export AGENTSHROUD_PORT=8443
export AGENTSHROUD_LOG_LEVEL=info

# OpenClaw Integration
export OPENCLAW_PROXY_ENABLED=true
export OPENCLAW_PROXY_URL=http://localhost:8443
export OPENCLAW_SECURITY_TOKEN=$(cat /run/secrets/security_token)
```

**3. Transparent Proxy Mode**

For zero-configuration deployment, enable transparent proxy mode:

```json
{
  "proxy": {
    "mode": "transparent",
    "upstream": {
      "host": "openclaw",
      "port": 3000,
      "protocol": "http"
    },
    "intercept": {
      "inbound": true,
      "outbound": true,
      "mcp_calls": true
    }
  },
  "security": {
    "pii_protection": true,
    "prompt_injection_defense": true,
    "audit_all_requests": true
  }
}
```

**4. Agent Configuration**

Update OpenClaw agent configuration:

```javascript
// openclaw-config.js
module.exports = {
  security: {
    proxy: {
      enabled: true,
      endpoint: 'http://localhost:8443',
      token: process.env.OPENCLAW_SECURITY_TOKEN
    }
  },
  audit: {
    enabled: true,
    endpoint: 'http://localhost:8443/api/v1/audit'
  }
};
```

### Integration Testing

Verify integration with health check:

```bash
curl -X GET http://localhost:8443/api/v1/health \
  -H "Authorization: Bearer $SECURITY_TOKEN"
```

Expected response indicates successful integration:

```json
{
  "status": "healthy",
  "upstream": {
    "openclaw": "connected",
    "response_time_ms": 12
  },
  "security_modules": "active"
}
```

---

## Generic AI Agent Integration

AgentShroud can protect any AI agent system through HTTP proxy mode.

### HTTP Proxy Mode

**1. Agent Configuration**

Configure your AI agent to route traffic through AgentShroud:

```python
# Python Agent Example
import requests

class SecureAgent:
    def __init__(self):
        self.proxy_url = "http://localhost:8443"
        self.agent_id = "my-ai-agent-001"
        self.session = requests.Session()
        self.session.headers.update({
            'X-Agent-ID': self.agent_id,
            'Authorization': f'Bearer {os.getenv("AGENTSHROUD_TOKEN")}'
        })

    def send_message(self, message):
        response = self.session.post(
            f"{self.proxy_url}/api/v1/ingest",
            json={
                'agent_id': self.agent_id,
                'message': message,
                'timestamp': datetime.now().isoformat()
            }
        )
        return response.json()
```

**2. Node.js Integration**

```javascript
// Node.js Agent Example
const axios = require('axios');

class SecureAIAgent {
  constructor(agentId, proxyUrl = 'http://localhost:8443') {
    this.agentId = agentId;
    this.proxyUrl = proxyUrl;
    this.client = axios.create({
      baseURL: proxyUrl,
      headers: {
        'X-Agent-ID': agentId,
        'Authorization': `Bearer ${process.env.AGENTSHROUD_TOKEN}`
      }
    });
  }

  async processMessage(message) {
    try {
      const response = await this.client.post('/api/v1/ingest', {
        agent_id: this.agentId,
        message: message,
        timestamp: new Date().toISOString()
      });
      return response.data;
    } catch (error) {
      console.error('Security proxy error:', error.response?.data);
      throw error;
    }
  }
}
```

**3. REST API Integration**

Direct REST API integration for non-HTTP agents:

```bash
# Message Processing
curl -X POST http://localhost:8443/api/v1/ingest \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $TOKEN" \
  -H "X-Agent-ID: my-agent-001" \
  -d '{
    "agent_id": "my-agent-001",
    "message": "User input message",
    "session_id": "session-123",
    "metadata": {
      "user_id": "user-456",
      "trust_level": 3
    }
  }'
```

---

## MCP Server Integration

Secure Model Context Protocol communications through AgentShroud MCP proxy.

### MCP Proxy Configuration

**1. MCP Server Setup**

Configure MCP servers to connect through AgentShroud:

```json
{
  "mcp": {
    "proxy": {
      "enabled": true,
      "port": 8444,
      "upstream_servers": [
        {
          "name": "filesystem",
          "endpoint": "http://mcp-filesystem:3001",
          "permissions": ["read", "write"],
          "trust_required": 5
        },
        {
          "name": "web_search",
          "endpoint": "http://mcp-search:3002", 
          "permissions": ["search"],
          "trust_required": 2
        }
      ]
    },
    "security": {
      "validate_parameters": true,
      "log_all_calls": true,
      "approval_required": ["filesystem.write", "system.exec"]
    }
  }
}
```

**2. Agent MCP Configuration**

Update agent MCP client configuration:

```javascript
// MCP Client Configuration
const mcpClient = new MCPClient({
  transport: {
    type: 'http',
    url: 'http://localhost:8444',
    headers: {
      'Authorization': `Bearer ${process.env.AGENTSHROUD_TOKEN}`,
      'X-Agent-ID': 'my-agent-001'
    }
  },
  security: {
    proxy_enabled: true,
    audit_calls: true
  }
});
```

**3. Tool Permission Policies**

Define tool-specific security policies:

```yaml
# mcp-policies.yml
policies:
  filesystem:
    read:
      trust_level: 2
      paths_allowed:
        - "/app/data/*"
        - "/tmp/*"
      paths_denied:
        - "/etc/*"
        - "/home/*"
    write:
      trust_level: 5
      approval_required: true
      max_file_size: "10MB"

  web_search:
    search:
      trust_level: 1
      rate_limit: "100/hour"
      domains_blocked:
        - "*.onion"
        - "malicious-site.com"
```

---

## Monitoring System Integration

Integrate AgentShroud with monitoring and alerting systems.

### Webhook Alerts

**1. Webhook Configuration**

Configure security alerts to external monitoring:

```json
{
  "webhooks": {
    "security_alerts": {
      "url": "https://monitoring.company.com/webhooks/security",
      "method": "POST",
      "headers": {
        "Authorization": "Bearer webhook-token",
        "Content-Type": "application/json"
      },
      "events": ["security_violation", "kill_switch", "pii_detected"],
      "severity_filter": ["medium", "high", "critical"]
    },
    "approval_requests": {
      "url": "https://ops.company.com/api/approvals",
      "events": ["approval_required"],
      "template": "slack"
    }
  }
}
```

**2. Webhook Payload Format**

Security alert webhook payload:

```json
{
  "event_type": "security_violation",
  "timestamp": "2026-02-19T11:16:00Z",
  "severity": "high",
  "agent_id": "agent-12345",
  "violation": {
    "type": "prompt_injection",
    "confidence": 0.95,
    "blocked": true,
    "details": "System prompt override attempt detected"
  },
  "context": {
    "session_id": "session-abcde",
    "user_id": "user-67890",
    "message_hash": "sha256-hash-value"
  },
  "response_required": false
}
```

### Prometheus Metrics

**1. Metrics Endpoint**

Configure Prometheus to scrape AgentShroud metrics:

```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'agentshroud'
    static_configs:
      - targets: ['localhost:8443']
    metrics_path: '/metrics'
    scrape_interval: 30s
    scrape_timeout: 10s
```

**2. Available Metrics**

AgentShroud exposes comprehensive security metrics:

```
# Security metrics
agentshroud_requests_total{agent_id, status}
agentshroud_security_violations_total{type, severity}
agentshroud_pii_detections_total{type}
agentshroud_prompt_injections_blocked_total
agentshroud_processing_duration_seconds{module}

# System metrics
agentshroud_active_agents
agentshroud_memory_usage_bytes
agentshroud_cpu_usage_percent
agentshroud_audit_entries_total
```

**3. Grafana Dashboard**

Import AgentShroud Grafana dashboard:

```json
{
  "dashboard": {
    "title": "AgentShroud Security Dashboard",
    "panels": [
      {
        "title": "Security Violations",
        "type": "stat",
        "targets": [
          {
            "expr": "sum(rate(agentshroud_security_violations_total[5m]))",
            "legendFormat": "Violations/sec"
          }
        ]
      }
    ]
  }
}
```

---

## 1Password Integration

Secure credential management with 1Password service accounts.

### Service Account Setup

**1. 1Password Configuration**

Create service account with limited vault access:

```bash
# Create service account
op service-account create "AgentShroud Bot" \
  --vault "AgentShroud Bot Credentials" \
  --permissions read

# Generate service account token
export OP_SERVICE_ACCOUNT_TOKEN="<service-account-token>"
```

**2. Vault Structure**

Organize credentials in dedicated vault:

```
AgentShroud Bot Credentials/
├── API Keys/
│   ├── Brave Search API
│   ├── Threat Intelligence Feed
│   └── Monitoring Webhooks
├── Database/
│   ├── Audit Database Credentials
│   └── Session Store Credentials
└── Certificates/
    ├── TLS Certificate
    └── JWT Signing Key
```

**3. Integration Configuration**

```json
{
  "credentials": {
    "provider": "1password",
    "service_account": {
      "token_file": "/run/secrets/1password_service_account",
      "vault": "AgentShroud Bot Credentials"
    },
    "items": {
      "brave_api_key": "Brave Search API",
      "threat_feed_token": "Threat Intelligence Feed",
      "webhook_token": "Monitoring Webhooks"
    },
    "refresh_interval": "1h"
  }
}
```

**4. Runtime Credential Access**

```javascript
// Runtime credential retrieval
const { exec } = require('child_process');
const util = require('util');
const execPromise = util.promisify(exec);

class CredentialManager {
  async getApiKey(itemName) {
    try {
      const { stdout } = await execPromise(
        `op item get "${itemName}" --vault "AgentShroud Bot Credentials" --fields api_key --reveal`
      );
      return stdout.trim();
    } catch (error) {
      throw new Error(`Failed to retrieve credential: ${error.message}`);
    }
  }
}
```

---

## CI/CD Pipeline Integration

Integrate AgentShroud security testing into development workflows.

### GitHub Actions Integration

**1. Security Testing Workflow**

```yaml
# .github/workflows/security-test.yml
name: AgentShroud Security Testing

on:
  pull_request:
    branches: [ main ]
  push:
    branches: [ main ]

jobs:
  security-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Start AgentShroud
        run: |
          docker run -d --name agentshroud \
            -p 8443:8443 \
            -e SECURITY_LEVEL=enforce \
            -e TEST_MODE=true \
            agentshroud:latest
          
          # Wait for startup
          timeout 60 bash -c 'until curl -f http://localhost:8443/health; do sleep 5; done'

      - name: Run Security Tests
        run: |
          npm test -- --testNamePattern="security"
          
      - name: Security Scan
        run: |
          docker run --rm --network host \
            -v $(pwd):/workspace \
            agentshroud/security-scanner:latest \
            --target http://localhost:8443 \
            --config /workspace/.security-scan.yml

      - name: Collect Audit Logs
        if: always()
        run: |
          curl -H "Authorization: Bearer ${{ secrets.TEST_TOKEN }}" \
            http://localhost:8443/api/v1/audit > audit-logs.json
            
      - name: Upload Test Results
        uses: actions/upload-artifact@v3
        if: always()
        with:
          name: security-test-results
          path: |
            audit-logs.json
            test-results.xml
```

**2. Deployment Pipeline**

```yaml
# .github/workflows/deploy.yml
name: Deploy with AgentShroud

on:
  release:
    types: [ created ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy AgentShroud
        run: |
          # Deploy AgentShroud first
          kubectl apply -f k8s/agentshroud/
          kubectl wait --for=condition=ready pod -l app=agentshroud
          
          # Deploy application behind AgentShroud
          kubectl apply -f k8s/app/
          
      - name: Verify Security Integration
        run: |
          # Test security endpoints
          kubectl port-forward svc/agentshroud 8443:8443 &
          sleep 10
          
          curl -f http://localhost:8443/health
          curl -f http://localhost:8443/api/v1/version
```

### Docker Security Scanning

**1. Container Security**

```dockerfile
# Multi-stage build for security
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM node:18-alpine AS runtime
RUN addgroup -g 1001 -S agentshroud && \
    adduser -S agentshroud -u 1001

WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY --chown=agentshroud:agentshroud . .

# Security hardening
RUN chmod -R 755 /app && \
    chown -R agentshroud:agentshroud /app

USER agentshroud
EXPOSE 8443

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8443/health || exit 1

CMD ["node", "server.js"]
```

**2. Security Scanning Integration**

```yaml
# docker-compose.security.yml
version: '3.8'
services:
  security-scanner:
    image: aquasec/trivy:latest
    command: |
      sh -c "
        trivy image --exit-code 0 --severity LOW,MEDIUM agentshroud:latest
        trivy image --exit-code 1 --severity HIGH,CRITICAL agentshroud:latest
      "
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    depends_on:
      - agentshroud
```

This integration guide provides comprehensive instructions for deploying AgentShroud across various environments and systems while maintaining security best practices and operational efficiency.