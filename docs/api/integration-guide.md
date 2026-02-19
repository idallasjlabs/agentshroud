# Integration Guide
## SecureClaw v0.9.0

### Overview

This guide provides comprehensive instructions for integrating SecureClaw with various systems and platforms. SecureClaw is designed as a transparent security proxy that can be integrated with minimal configuration changes to existing AI agent infrastructure.

---

## OpenClaw Integration (Primary Target)

SecureClaw is purpose-built for OpenClaw AI agents, providing seamless integration with transparent proxy functionality.

### Architecture Overview

```
[User] → [SecureClaw Proxy] → [OpenClaw Agent] → [External Services]
                ↓
        [Security Modules] → [Audit System]
```

### Configuration

**1. Docker Compose Integration**

Add SecureClaw to your existing OpenClaw deployment:

```yaml
version: '3.8'
services:
  secureclaw:
    image: secureclaw:0.9.0
    ports:
      - "8443:8443"
    environment:
      - OPENCLAW_UPSTREAM=http://openclaw:3000
      - SECURITY_LEVEL=enforce
      - AUDIT_ENABLED=true
    volumes:
      - ./config:/app/config
      - secureclaw-data:/app/data
    networks:
      - openclaw-net

  openclaw:
    image: openclaw:latest
    environment:
      - PROXY_MODE=true
      - PROXY_ENDPOINT=http://secureclaw:8080
    networks:
      - openclaw-net
    depends_on:
      - secureclaw

volumes:
  secureclaw-data:

networks:
  openclaw-net:
    driver: bridge
```

**2. Environment Configuration**

```bash
# SecureClaw Configuration
export SECURECLAW_MODE=proxy
export SECURECLAW_UPSTREAM=http://localhost:3000
export SECURECLAW_PORT=8443
export SECURECLAW_LOG_LEVEL=info

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

SecureClaw can protect any AI agent system through HTTP proxy mode.

### HTTP Proxy Mode

**1. Agent Configuration**

Configure your AI agent to route traffic through SecureClaw:

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
            'Authorization': f'Bearer {os.getenv("SECURECLAW_TOKEN")}'
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
        'Authorization': `Bearer ${process.env.SECURECLAW_TOKEN}`
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

Secure Model Context Protocol communications through SecureClaw MCP proxy.

### MCP Proxy Configuration

**1. MCP Server Setup**

Configure MCP servers to connect through SecureClaw:

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
      'Authorization': `Bearer ${process.env.SECURECLAW_TOKEN}`,
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

Integrate SecureClaw with monitoring and alerting systems.

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

Configure Prometheus to scrape SecureClaw metrics:

```yaml
# prometheus.yml
scrape_configs:
  - job_name: 'secureclaw'
    static_configs:
      - targets: ['localhost:8443']
    metrics_path: '/metrics'
    scrape_interval: 30s
    scrape_timeout: 10s
```

**2. Available Metrics**

SecureClaw exposes comprehensive security metrics:

```
# Security metrics
secureclaw_requests_total{agent_id, status}
secureclaw_security_violations_total{type, severity}
secureclaw_pii_detections_total{type}
secureclaw_prompt_injections_blocked_total
secureclaw_processing_duration_seconds{module}

# System metrics
secureclaw_active_agents
secureclaw_memory_usage_bytes
secureclaw_cpu_usage_percent
secureclaw_audit_entries_total
```

**3. Grafana Dashboard**

Import SecureClaw Grafana dashboard:

```json
{
  "dashboard": {
    "title": "SecureClaw Security Dashboard",
    "panels": [
      {
        "title": "Security Violations",
        "type": "stat",
        "targets": [
          {
            "expr": "sum(rate(secureclaw_security_violations_total[5m]))",
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
op service-account create "SecureClaw Bot" \
  --vault "SecureClaw Bot Credentials" \
  --permissions read

# Generate service account token
export OP_SERVICE_ACCOUNT_TOKEN="<service-account-token>"
```

**2. Vault Structure**

Organize credentials in dedicated vault:

```
SecureClaw Bot Credentials/
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
      "vault": "SecureClaw Bot Credentials"
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
        `op item get "${itemName}" --vault "SecureClaw Bot Credentials" --fields api_key --reveal`
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

Integrate SecureClaw security testing into development workflows.

### GitHub Actions Integration

**1. Security Testing Workflow**

```yaml
# .github/workflows/security-test.yml
name: SecureClaw Security Testing

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
      
      - name: Start SecureClaw
        run: |
          docker run -d --name secureclaw \
            -p 8443:8443 \
            -e SECURITY_LEVEL=enforce \
            -e TEST_MODE=true \
            secureclaw:latest
          
          # Wait for startup
          timeout 60 bash -c 'until curl -f http://localhost:8443/health; do sleep 5; done'

      - name: Run Security Tests
        run: |
          npm test -- --testNamePattern="security"
          
      - name: Security Scan
        run: |
          docker run --rm --network host \
            -v $(pwd):/workspace \
            secureclaw/security-scanner:latest \
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
name: Deploy with SecureClaw

on:
  release:
    types: [ created ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy SecureClaw
        run: |
          # Deploy SecureClaw first
          kubectl apply -f k8s/secureclaw/
          kubectl wait --for=condition=ready pod -l app=secureclaw
          
          # Deploy application behind SecureClaw
          kubectl apply -f k8s/app/
          
      - name: Verify Security Integration
        run: |
          # Test security endpoints
          kubectl port-forward svc/secureclaw 8443:8443 &
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
RUN addgroup -g 1001 -S secureclaw && \
    adduser -S secureclaw -u 1001

WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY --chown=secureclaw:secureclaw . .

# Security hardening
RUN chmod -R 755 /app && \
    chown -R secureclaw:secureclaw /app

USER secureclaw
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
        trivy image --exit-code 0 --severity LOW,MEDIUM secureclaw:latest
        trivy image --exit-code 1 --severity HIGH,CRITICAL secureclaw:latest
      "
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    depends_on:
      - secureclaw
```

This integration guide provides comprehensive instructions for deploying SecureClaw across various environments and systems while maintaining security best practices and operational efficiency.