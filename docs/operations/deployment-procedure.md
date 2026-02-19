# SecureClaw Deployment Procedure

This document provides step-by-step instructions for deploying SecureClaw in production and development environments.

## Prerequisites

### System Requirements

**Minimum Hardware:**
- 4 CPU cores
- 8GB RAM
- 100GB disk space (SSD recommended)
- Network interface with internet access

**Recommended Hardware:**
- 8 CPU cores
- 16GB RAM
- 500GB disk space (SSD)
- 1Gbps network interface

### Software Dependencies

```bash
# Check system compatibility
uname -a
# Should show: Linux kernel 4.15+ (for modern Docker support)

# Required software versions
docker --version          # Docker 20.10+
docker compose version   # Docker Compose 2.0+
git --version            # Git 2.20+
openssl version          # OpenSSL 1.1.1+

# Optional but recommended
gpg --version            # GPG 2.2+ (for secret encryption)
```

### Network Requirements

| Port | Protocol | Purpose | Firewall Rule |
|------|----------|---------|---------------|
| 8443 | HTTPS | SecureClaw API | Allow from trusted networks |
| 8000 | HTTP | OpenClaw (internal) | Block external access |
| 3000 | HTTP | Grafana (optional) | Allow from admin networks |
| 9090 | HTTP | Prometheus (optional) | Allow from admin networks |

### 1Password Integration (Optional)

If using 1Password for secret management:

```bash
# Install 1Password CLI
curl -sS https://downloads.1password.com/linux/keys/1password.asc | \
  gpg --dearmor --output /usr/share/keyrings/1password-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/1password-archive-keyring.gpg] \
  https://downloads.1password.com/linux/debian/$(dpkg --print-architecture) stable main" | \
  tee /etc/apt/sources.list.d/1password.list

apt update && apt install 1password-cli

# Test connectivity
op --version
```

## Deployment Modes

SecureClaw supports two deployment modes:

### Proxy Mode (Recommended)

SecureClaw acts as a reverse proxy in front of OpenClaw:

```
Client → SecureClaw (8443) → OpenClaw (8000)
```

**Advantages:**
- Complete traffic interception
- No OpenClaw modifications required
- Centralized security controls
- Easy to deploy and manage

### Sidecar Mode (Advanced)

SecureClaw runs alongside OpenClaw with shared networking:

```
Client → Load Balancer → [SecureClaw + OpenClaw] Pod
```

**Advantages:**
- Lower latency
- Better for high-throughput scenarios
- Kubernetes-native deployment

**Note:** This guide focuses on Proxy Mode. For Sidecar Mode, see `kubernetes/README.md`.

## Step-by-Step Deployment

### Step 1: System Preparation

```bash
# 1. Update system packages
apt update && apt upgrade -y

# 2. Install Docker if not present
curl -fsSL https://get.docker.com | sh
usermod -aG docker $USER

# 3. Install Docker Compose
curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" \
  -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose

# 4. Create dedicated user (security best practice)
useradd -r -s /bin/bash -m -d /opt/secureclaw secureclaw
usermod -aG docker secureclaw

# 5. Create directory structure
sudo -u secureclaw mkdir -p /opt/secureclaw/{config,secrets,data,logs,backup}
```

### Step 2: Repository Clone and Configuration

```bash
# Switch to SecureClaw user
su - secureclaw
cd /opt/secureclaw

# Clone repository
git clone https://github.com/company/secureclaw.git .
git checkout v1.0.0  # Use specific version tag

# Verify files
ls -la
# Should show: docker-compose.yml, config/, scripts/, docs/

# Make scripts executable
chmod +x scripts/*.sh
```

### Step 3: Secret Configuration

#### Option A: Manual Secret Creation

```bash
# Generate secure random passwords
openssl rand -hex 32 > secrets/secureclaw-db-password.txt
openssl rand -hex 32 > secrets/admin-token.txt
openssl rand -base64 32 > secrets/webhook-secret.txt

# Create OpenClaw API key secret
echo "your_openclaw_api_key_here" > secrets/openclaw-api-key.txt

# Email credentials (if using SMTP notifications)
echo "your_smtp_password_here" > secrets/smtp-password.txt

# Optional: External service API keys
echo "your_virustotal_api_key" > secrets/virustotal-api-key.txt
echo "your_urlvoid_api_key" > secrets/urlvoid-api-key.txt

# Set proper permissions
chmod 600 secrets/*.txt
```

#### Option B: 1Password Integration

```bash
# Set up 1Password service account
export OP_SERVICE_ACCOUNT_TOKEN="your_service_account_token"

# Create secrets from 1Password
op item get "SecureClaw DB Password" --fields password > secrets/secureclaw-db-password.txt
op item get "SecureClaw Admin Token" --fields token > secrets/admin-token.txt
op item get "OpenClaw API Key" --fields api_key > secrets/openclaw-api-key.txt

# Set proper permissions
chmod 600 secrets/*.txt
```

### Step 4: SSL Certificate Setup

#### Option A: Self-Signed Certificate (Development/Testing)

```bash
# Generate self-signed certificate
openssl req -x509 -newkey rsa:4096 -keyout secrets/ssl-key.pem \
  -out secrets/ssl-cert.pem -days 365 -nodes \
  -subj "/C=US/ST=State/L=City/O=Organization/CN=secureclaw.local"

# Set proper permissions
chmod 600 secrets/ssl-*.pem
```

#### Option B: Let's Encrypt Certificate (Production)

```bash
# Install Certbot
apt install certbot -y

# Generate certificate (replace with your domain)
certbot certonly --standalone -d your-domain.com

# Copy certificates to secrets directory
cp /etc/letsencrypt/live/your-domain.com/fullchain.pem secrets/ssl-cert.pem
cp /etc/letsencrypt/live/your-domain.com/privkey.pem secrets/ssl-key.pem

# Set proper permissions
chmod 600 secrets/ssl-*.pem

# Set up auto-renewal
crontab -e
# Add: 0 3 * * * certbot renew --quiet && docker compose restart secureclaw
```

#### Option C: Corporate Certificate Authority

```bash
# Copy certificates from your CA
cp /path/to/corporate.crt secrets/ssl-cert.pem
cp /path/to/corporate.key secrets/ssl-key.pem

# If using certificate chain
cat intermediate.crt root.crt >> secrets/ssl-cert.pem

# Set proper permissions
chmod 600 secrets/ssl-*.pem
```

### Step 5: Configuration Customization

```bash
# Copy example configuration
cp config/secureclaw.yaml.example config/secureclaw.yaml
cp config/egress-config.yml.example config/egress-config.yml
cp config/mcp-config.yml.example config/mcp-config.yml

# Edit main configuration
vim config/secureclaw.yaml
```

**Key configuration sections to customize:**

```yaml
# config/secureclaw.yaml
gateway:
  host: "0.0.0.0"                    # Change if binding to specific interface
  port: 8443                         # Default HTTPS port
  port_offset: 0                     # Will be auto-detected if port conflicts

security:
  kill_switch:
    enabled: true                    # Enable kill switch functionality
  pii_sanitizer:
    enabled: true                    # Enable PII detection and removal
  trust_manager:
    initial_level: 0                 # New agents start untrusted

proxy:
  openclaw:
    host: "openclaw"                 # Service name in Docker Compose
    port: 8000                       # OpenClaw port
    timeout: 30                      # Connection timeout

# Update with your specific needs
monitoring:
  alerts:
    webhook_url: "https://your-alerts.com/webhook"
    severity_threshold: "HIGH"
```

### Step 6: Port Configuration

SecureClaw includes automatic port conflict detection:

```bash
# Check for port conflicts
./scripts/check-ports.sh

# If port 8443 is in use, SecureClaw will auto-detect and use an offset
# You can also manually set the offset:
export SECURECLAW_PORT_OFFSET=100
# This will use port 8543 instead of 8443

# Verify the selected port
./scripts/show-ports.sh
```

### Step 7: Docker Secrets Creation

```bash
# Create Docker secrets from files
./scripts/create-secrets.sh

# Verify secrets were created
docker secret ls

# Expected output should include:
# secureclaw-db-password
# admin-token
# openclaw-api-key  
# ssl-cert
# ssl-key
```

### Step 8: Service Startup

```bash
# Start the stack
docker compose up -d

# Check service status
docker compose ps

# Expected output:
# secureclaw_secureclaw_1   Up   0.0.0.0:8443->8443/tcp
# secureclaw_openclaw_1     Up   8000/tcp
# secureclaw_db_1           Up   
# secureclaw_prometheus_1   Up   9090/tcp
# secureclaw_grafana_1      Up   3000/tcp

# View startup logs
docker compose logs -f secureclaw
```

### Step 9: Health Verification

```bash
# Wait for services to fully start (30-60 seconds)
sleep 60

# Test basic connectivity
curl -k https://localhost:8443/health
# Expected: {"status": "healthy", "timestamp": "..."}

# Test with custom port offset (if used)
ACTUAL_PORT=$((8443 + ${SECURECLAW_PORT_OFFSET:-0}))
curl -k https://localhost:$ACTUAL_PORT/health

# Detailed health check
curl -k -s https://localhost:8443/health/detailed | jq '.'

# Test admin endpoints
ADMIN_TOKEN=$(cat secrets/admin-token.txt)
curl -k -H "Authorization: Bearer $ADMIN_TOKEN" \
  https://localhost:8443/admin/config | jq '.gateway'
```

### Step 10: Initial Configuration

```bash
# Set up initial admin user (if applicable)
ADMIN_TOKEN=$(cat secrets/admin-token.txt)

# Create initial agent trust entries
curl -k -X POST -H "Authorization: Bearer $ADMIN_TOKEN" \
  https://localhost:8443/admin/agents \
  -d '{
    "agent_id": "default-agent",
    "trust_level": 1,
    "description": "Default agent for testing"
  }'

# Configure monitoring (if using Grafana)
./scripts/setup-monitoring.sh
```

## Monitoring Setup

### Grafana Dashboard Configuration

```bash
# Access Grafana
open https://localhost:3000

# Default login:
# Username: admin
# Password: admin (change immediately)

# Import SecureClaw dashboard
# 1. Go to Dashboards > Import
# 2. Upload: monitoring/grafana/secureclaw-dashboard.json
# 3. Configure data source: http://prometheus:9090

# Set up alerting
# 1. Go to Alerting > Alert Rules
# 2. Import: monitoring/grafana/alert-rules.json
```

### Prometheus Configuration

```bash
# Verify Prometheus is scraping SecureClaw metrics
curl http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | select(.labels.job=="secureclaw")'

# Check key metrics are available
curl 'http://localhost:9090/api/v1/query?query=secureclaw_requests_total'
```

## Post-Deployment Validation

### Functional Testing

```bash
# Create test script
cat > test-deployment.sh << 'EOF'
#!/bin/bash

set -e

ADMIN_TOKEN=$(cat secrets/admin-token.txt)
BASE_URL="https://localhost:8443"

echo "Testing SecureClaw deployment..."

# Test 1: Health check
echo "1. Health check..."
curl -k -f $BASE_URL/health > /dev/null && echo "✓ Health check passed"

# Test 2: Admin authentication
echo "2. Admin authentication..."
curl -k -f -H "Authorization: Bearer $ADMIN_TOKEN" \
  $BASE_URL/admin/config > /dev/null && echo "✓ Admin auth passed"

# Test 3: Trust level management
echo "3. Trust level management..."
curl -k -f -H "Authorization: Bearer $ADMIN_TOKEN" \
  $BASE_URL/admin/trust-levels > /dev/null && echo "✓ Trust levels accessible"

# Test 4: Audit system
echo "4. Audit system..."
curl -k -f -H "Authorization: Bearer $ADMIN_TOKEN" \
  $BASE_URL/admin/audit?limit=1 > /dev/null && echo "✓ Audit system working"

# Test 5: Kill switch
echo "5. Kill switch (status check only)..."
KILL_STATUS=$(curl -k -s -H "Authorization: Bearer $ADMIN_TOKEN" \
  $BASE_URL/admin/kill-switch | jq -r '.status')
[ "$KILL_STATUS" = "active" ] && echo "✓ Kill switch accessible"

echo "All tests passed! Deployment successful."
EOF

chmod +x test-deployment.sh
./test-deployment.sh
```

### Security Validation

```bash
# Test SSL certificate
echo | openssl s_client -connect localhost:8443 -servername localhost 2>/dev/null | \
  openssl x509 -noout -dates
# Should show valid certificate dates

# Test unauthorized access is blocked
curl -k -s -o /dev/null -w "%{http_code}" https://localhost:8443/admin/config
# Should return 401 (Unauthorized)

# Test kill switch functionality (careful - will block traffic!)
# ADMIN_TOKEN=$(cat secrets/admin-token.txt)
# curl -k -X POST -H "Authorization: Bearer $ADMIN_TOKEN" \
#   https://localhost:8443/admin/kill-switch \
#   -d '{"mode": "soft_kill", "reason": "deployment_test"}'
# 
# # Immediately deactivate
# curl -k -X POST -H "Authorization: Bearer $ADMIN_TOKEN" \
#   https://localhost:8443/admin/kill-switch \
#   -d '{"mode": "deactivate", "reason": "test_complete"}'
```

## Production Hardening

### Security Hardening

```bash
# 1. Disable unnecessary services
systemctl disable apache2 nginx  # If not needed
systemctl stop apache2 nginx

# 2. Configure firewall
ufw enable
ufw default deny incoming
ufw default allow outgoing
ufw allow from 10.0.0.0/8 to any port 8443    # Internal networks only
ufw allow from 192.168.0.0/16 to any port 8443
ufw allow ssh

# 3. Set up log rotation
cat > /etc/logrotate.d/secureclaw << 'EOF'
/opt/secureclaw/logs/*.log {
    daily
    rotate 30
    compress
    delaycompress
    missingok
    notifempty
    create 0644 secureclaw secureclaw
    postrotate
        docker compose -f /opt/secureclaw/docker-compose.yml restart secureclaw
    endscript
}
EOF

# 4. Set up automated backups
cat > /opt/secureclaw/scripts/backup.sh << 'EOF'
#!/bin/bash
BACKUP_DIR="/backup/secureclaw/$(date +%Y/%m)"
mkdir -p "$BACKUP_DIR"

# Database backup
docker compose exec -T secureclaw sqlite3 /data/secureclaw.db \
  ".backup $BACKUP_DIR/audit_$(date +%Y%m%d_%H%M%S).db"

# Configuration backup
cp -r /opt/secureclaw/config "$BACKUP_DIR/config_$(date +%Y%m%d)/"

# Compress and clean up
tar czf "$BACKUP_DIR/backup_$(date +%Y%m%d).tar.gz" \
  "$BACKUP_DIR"/*.db "$BACKUP_DIR"/config_*
rm -rf "$BACKUP_DIR"/*.db "$BACKUP_DIR"/config_*

# Keep only 30 days of backups
find /backup/secureclaw -name "*.tar.gz" -mtime +30 -delete
EOF

chmod +x /opt/secureclaw/scripts/backup.sh

# Add to cron
crontab -u secureclaw -e
# Add: 0 2 * * * /opt/secureclaw/scripts/backup.sh
```

### Performance Tuning

```bash
# 1. Optimize Docker settings
cat > /etc/docker/daemon.json << 'EOF'
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  },
  "default-shm-size": "128m"
}
EOF

systemctl restart docker

# 2. Set resource limits in docker-compose.yml
# Add to services:
#   secureclaw:
#     mem_limit: 4g
#     mem_reservation: 2g
#     cpus: '2.0'

# 3. Optimize SQLite performance
# (Already configured in schema-documentation.md)
```

## Troubleshooting Common Issues

### Port Already in Use

```bash
# Check what's using port 8443
lsof -i :8443

# Option 1: Kill the conflicting process
kill $(lsof -t -i :8443)

# Option 2: Use port offset
export SECURECLAW_PORT_OFFSET=100
docker compose down
docker compose up -d

# Option 3: Change configuration
# Edit docker-compose.yml and change port mapping
```

### SSL Certificate Issues

```bash
# Check certificate validity
openssl x509 -in secrets/ssl-cert.pem -text -noout

# Common issues:
# - Expired certificate: Regenerate or renew
# - Wrong hostname: Check CN/SAN fields
# - Invalid format: Ensure PEM format

# Test certificate with openssl
echo | openssl s_client -connect localhost:8443 -servername localhost
```

### Container Won't Start

```bash
# Check logs
docker compose logs secureclaw

# Common issues:
# - Missing secrets: Run create-secrets.sh
# - Permission issues: Check file ownership
# - Port conflicts: Use port offset
# - Invalid config: Validate YAML syntax

# Debug startup
docker compose run --rm secureclaw python -c "
import yaml
with open('/config/secureclaw.yaml') as f:
    config = yaml.safe_load(f)
    print('Configuration loaded successfully')
"
```

### Database Connection Issues

```bash
# Check database file permissions
ls -la /opt/secureclaw/data/

# Should be owned by 999:999 (Docker user)
chown -R 999:999 /opt/secureclaw/data/

# Test database connectivity
docker compose exec secureclaw sqlite3 /data/secureclaw.db ".databases"
```

## Maintenance Procedures

### Regular Maintenance Tasks

| Frequency | Task | Command |
|-----------|------|---------|
| Daily | Check system health | `./scripts/health-check.sh` |
| Daily | Rotate logs | Automatic via logrotate |
| Weekly | Update system packages | `apt update && apt upgrade` |
| Weekly | Backup database | `./scripts/backup.sh` |
| Monthly | Review audit logs | Access Grafana dashboard |
| Monthly | Update SecureClaw | `./scripts/update-secureclaw.sh` |
| Quarterly | Security review | Review configurations and access |
| Quarterly | DR test | Test backup/restore procedures |

### Update Procedure

```bash
# 1. Backup current state
./scripts/backup.sh

# 2. Pull latest version
git fetch --tags
git checkout v1.1.0  # Use specific version

# 3. Update configuration if needed
# Check CHANGELOG.md for configuration changes

# 4. Pull new Docker images
docker compose pull

# 5. Restart services
docker compose down
docker compose up -d

# 6. Verify deployment
./test-deployment.sh
```

This deployment procedure ensures a secure, reliable SecureClaw installation. Always test in a development environment before deploying to production, and maintain regular backups of configuration and audit data.