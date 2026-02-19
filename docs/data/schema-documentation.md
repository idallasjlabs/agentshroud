# SecureClaw Schema Documentation

This document defines the database schemas, configuration file formats, and Docker secrets structure used by SecureClaw.

## SQLite Database Schema

SecureClaw uses SQLite for persistent storage of approval queue and audit data.

### Approval Queue Schema

```sql
-- Approval queue table
CREATE TABLE approval_requests (
    id TEXT PRIMARY KEY,           -- UUID as string
    agent_id TEXT NOT NULL,
    action TEXT NOT NULL,          -- JSON serialized action
    status TEXT NOT NULL,          -- PENDING, APPROVED, DENIED, EXPIRED
    priority TEXT NOT NULL,        -- LOW, MEDIUM, HIGH, CRITICAL
    created_at TEXT NOT NULL,      -- ISO 8601 timestamp
    reviewed_at TEXT,              -- ISO 8601 timestamp, nullable
    reviewer TEXT,                 -- Admin identifier
    review_notes TEXT,             -- Optional admin notes
    expiry_at TEXT NOT NULL,       -- ISO 8601 timestamp
    
    CONSTRAINT valid_status CHECK (status IN ('PENDING', 'APPROVED', 'DENIED', 'EXPIRED')),
    CONSTRAINT valid_priority CHECK (priority IN ('LOW', 'MEDIUM', 'HIGH', 'CRITICAL')),
    CONSTRAINT reviewer_required CHECK (
        (status = 'PENDING' AND reviewer IS NULL) OR 
        (status != 'PENDING' AND reviewer IS NOT NULL)
    )
);

-- Indexes for performance
CREATE INDEX idx_approval_status_priority ON approval_requests(status, priority, created_at);
CREATE INDEX idx_approval_agent ON approval_requests(agent_id, created_at DESC);
CREATE INDEX idx_approval_expiry ON approval_requests(expiry_at) WHERE status = 'PENDING';

-- Agent trust levels table
CREATE TABLE agent_trust (
    agent_id TEXT PRIMARY KEY,
    level INTEGER NOT NULL,        -- 0-4 trust level
    last_promoted TEXT,            -- ISO 8601 timestamp, nullable
    total_actions INTEGER NOT NULL DEFAULT 0,
    violations INTEGER NOT NULL DEFAULT 0,
    last_violation TEXT,           -- ISO 8601 timestamp, nullable
    created_at TEXT NOT NULL,      -- ISO 8601 timestamp
    updated_at TEXT NOT NULL,      -- ISO 8601 timestamp
    
    CONSTRAINT valid_level CHECK (level >= 0 AND level <= 4),
    CONSTRAINT positive_counters CHECK (total_actions >= 0 AND violations >= 0)
);

CREATE INDEX idx_trust_level ON agent_trust(level, last_promoted);

-- Audit entries table (core audit log)
CREATE TABLE audit_entries (
    id TEXT PRIMARY KEY,           -- UUID as string
    timestamp TEXT NOT NULL,       -- ISO 8601 timestamp
    direction TEXT NOT NULL,       -- INBOUND, OUTBOUND
    content TEXT,                  -- Sanitized content (max 64KB)
    content_hash TEXT NOT NULL,    -- SHA-256 hex string
    previous_hash TEXT,            -- Previous entry hash for chaining
    chain_hash TEXT NOT NULL,      -- Cumulative integrity hash
    agent_id TEXT NOT NULL,
    threat_level TEXT NOT NULL,    -- LOW, MEDIUM, HIGH, CRITICAL
    pii_redacted INTEGER NOT NULL DEFAULT 0, -- SQLite boolean (0/1)
    
    CONSTRAINT valid_direction CHECK (direction IN ('INBOUND', 'OUTBOUND')),
    CONSTRAINT valid_threat CHECK (threat_level IN ('LOW', 'MEDIUM', 'HIGH', 'CRITICAL')),
    CONSTRAINT valid_hash CHECK (length(content_hash) = 64),
    CONSTRAINT valid_chain_hash CHECK (length(chain_hash) = 64)
);

-- Critical indexes for audit integrity
CREATE INDEX idx_audit_agent_time ON audit_entries(agent_id, timestamp DESC);
CREATE INDEX idx_audit_chain ON audit_entries(previous_hash, chain_hash);
CREATE UNIQUE INDEX idx_audit_chain_integrity ON audit_entries(chain_hash);

-- MCP audit entries (extends audit_entries)
CREATE TABLE mcp_audit_entries (
    id TEXT PRIMARY KEY,           -- References audit_entries.id
    server_name TEXT NOT NULL,
    tool_name TEXT NOT NULL,
    parameters TEXT,               -- JSON parameters
    duration_ms INTEGER,           -- Nullable for blocked calls
    blocked INTEGER NOT NULL DEFAULT 0, -- SQLite boolean
    block_reason TEXT,
    
    FOREIGN KEY (id) REFERENCES audit_entries(id) ON DELETE CASCADE,
    CONSTRAINT block_reason_required CHECK (
        (blocked = 0 AND block_reason IS NULL) OR 
        (blocked = 1 AND block_reason IS NOT NULL)
    )
);

CREATE INDEX idx_mcp_server_tool ON mcp_audit_entries(server_name, tool_name);
CREATE INDEX idx_mcp_blocked ON mcp_audit_entries(blocked, id);

-- Database initialization
INSERT INTO agent_trust (agent_id, level, created_at, updated_at) 
VALUES ('system', 4, datetime('now'), datetime('now'));

-- Trigger to update timestamps
CREATE TRIGGER update_trust_timestamp 
    AFTER UPDATE ON agent_trust
BEGIN
    UPDATE agent_trust SET updated_at = datetime('now') WHERE agent_id = NEW.agent_id;
END;
```

### Database Connection Configuration

```python
# Database connection settings
DATABASE_CONFIG = {
    "path": "/data/secureclaw.db",
    "timeout": 30.0,                # Connection timeout
    "check_same_thread": False,     # Allow multi-threading
    "journal_mode": "WAL",          # Write-Ahead Logging for performance
    "synchronous": "NORMAL",        # Balance performance vs durability
    "cache_size": -2048,            # 2MB cache
    "temp_store": "MEMORY",         # Use memory for temp tables
    "foreign_keys": True,           # Enable foreign key constraints
    "backup_interval": 3600,        # Backup every hour
    "vacuum_interval": 86400        # Daily VACUUM for maintenance
}
```

## In-Memory Data Structures

### Audit Chain State

```python
from dataclasses import dataclass
from typing import Optional, List
import time

@dataclass
class AuditChainState:
    """In-memory audit chain state for performance"""
    last_hash: Optional[str] = None      # Hash of last audit entry
    entry_count: int = 0                 # Total entries in chain
    last_verified: float = 0             # Last integrity verification time
    integrity_valid: bool = True         # Chain integrity status
    
    def verify_integrity(self) -> bool:
        """Verify chain integrity (called periodically)"""
        pass
    
    def append_entry(self, entry_hash: str, previous_hash: str) -> str:
        """Calculate chain hash for new entry"""
        import hashlib
        chain_data = f"{previous_hash}{entry_hash}"
        chain_hash = hashlib.sha256(chain_data.encode()).hexdigest()
        self.last_hash = chain_hash
        self.entry_count += 1
        return chain_hash

# Global chain state
audit_chain = AuditChainState()
```

### Trust Level Cache

```python
from typing import Dict, Tuple
import time

class TrustLevelCache:
    """In-memory cache for agent trust levels"""
    
    def __init__(self, ttl: int = 300):  # 5-minute TTL
        self.cache: Dict[str, Tuple[int, float]] = {}  # agent_id -> (level, timestamp)
        self.ttl = ttl
    
    def get_trust_level(self, agent_id: str) -> Optional[int]:
        """Get cached trust level"""
        if agent_id in self.cache:
            level, timestamp = self.cache[agent_id]
            if time.time() - timestamp < self.ttl:
                return level
            else:
                del self.cache[agent_id]  # Expired
        return None
    
    def set_trust_level(self, agent_id: str, level: int):
        """Cache trust level"""
        self.cache[agent_id] = (level, time.time())
    
    def invalidate(self, agent_id: str):
        """Remove from cache (on trust level change)"""
        self.cache.pop(agent_id, None)

# Global trust cache
trust_cache = TrustLevelCache()
```

### Rate Limiter State

```python
import time
from typing import Dict, Tuple

class TokenBucket:
    """Token bucket rate limiter implementation"""
    
    def __init__(self, max_tokens: int, refill_rate: float):
        self.max_tokens = max_tokens
        self.refill_rate = refill_rate        # Tokens per second
        self.tokens = max_tokens
        self.last_refill = time.time()
        self.blocked_until = 0.0              # Block expiry timestamp
    
    def consume(self, tokens: int = 1) -> bool:
        """Attempt to consume tokens"""
        now = time.time()
        
        # Check if still blocked
        if now < self.blocked_until:
            return False
        
        # Refill tokens
        elapsed = now - self.last_refill
        self.tokens = min(self.max_tokens, 
                         self.tokens + elapsed * self.refill_rate)
        self.last_refill = now
        
        # Check if enough tokens
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        
        return False
    
    def block_for(self, seconds: float):
        """Block for specified duration"""
        self.blocked_until = time.time() + seconds

class RateLimiterState:
    """Global rate limiter state"""
    
    def __init__(self):
        # agent_id -> resource -> TokenBucket
        self.buckets: Dict[str, Dict[str, TokenBucket]] = {}
    
    def get_bucket(self, agent_id: str, resource: str, 
                   max_tokens: int, refill_rate: float) -> TokenBucket:
        """Get or create token bucket"""
        if agent_id not in self.buckets:
            self.buckets[agent_id] = {}
        
        if resource not in self.buckets[agent_id]:
            self.buckets[agent_id][resource] = TokenBucket(max_tokens, refill_rate)
        
        return self.buckets[agent_id][resource]
    
    def cleanup_expired(self, max_age: float = 3600):
        """Remove old unused buckets"""
        now = time.time()
        for agent_id in list(self.buckets.keys()):
            agent_buckets = self.buckets[agent_id]
            for resource in list(agent_buckets.keys()):
                bucket = agent_buckets[resource]
                if now - bucket.last_refill > max_age:
                    del agent_buckets[resource]
            
            if not agent_buckets:
                del self.buckets[agent_id]

# Global rate limiter
rate_limiter = RateLimiterState()
```

## Configuration File Schemas

### Main Configuration (secureclaw.yaml)

```yaml
# SecureClaw main configuration schema
api_version: "v1"
kind: "SecureClawConfig"

# Gateway settings
gateway:
  host: "0.0.0.0"
  port: 8443
  port_offset: 0                    # Auto-detected offset for port conflicts
  ssl:
    enabled: true
    cert_path: "/certs/server.crt"
    key_path: "/certs/server.key"
    verify_client: false
  
  # Request handling
  max_request_size: "10MB"
  timeout_seconds: 30
  keep_alive: true
  
  # Mode settings
  operational_mode: "ENFORCE"       # MONITOR, ENFORCE, LOCKDOWN
  startup_mode: "MONITOR"           # Initial mode on startup

# Security settings
security:
  # Kill switch configuration
  kill_switch:
    enabled: true
    soft_kill_triggers:
      - "high_violation_rate"       # >50 violations/hour
      - "multiple_failed_auth"      # >10 failures/minute
      - "resource_exhaustion"       # >90% memory/CPU
    hard_kill_triggers:
      - "audit_tampering"           # Integrity violation
      - "container_escape"          # Container breakout attempt
    panic_triggers:
      - "external_intrusion"        # Network intrusion detected
  
  # PII sanitization
  pii_sanitizer:
    enabled: true
    patterns:
      - "ssn"                       # Social Security Numbers
      - "credit_card"               # Credit card numbers
      - "email"                     # Email addresses
      - "phone"                     # Phone numbers
      - "ip_address"                # IP addresses
    replacement_text: "[REDACTED]"
    log_redactions: true
  
  # Trust management
  trust_manager:
    initial_level: 0                # New agents start untrusted
    auto_promotion: true            # Enable automatic promotions
    violation_reset: true           # Reset to level 0 on violation
    promotion_criteria:
      level_1:
        actions_required: 0
        violation_threshold: 0
        time_required_hours: 0
      level_2:
        actions_required: 100
        violation_threshold: 0
        time_required_hours: 168     # 7 days
      level_3:
        actions_required: 1000
        violation_rate_threshold: 0.05  # <5% violation rate
        time_required_hours: 720     # 30 days

# Audit settings
audit:
  enabled: true
  chain_integrity: true             # Enable blockchain-style chaining
  storage_backend: "sqlite"         # sqlite, postgresql
  retention_days: 2555              # ~7 years
  
  # Audit levels
  log_levels:
    requests: "INFO"
    responses: "INFO"
    blocks: "WARN"
    violations: "ERROR"
    system: "INFO"
  
  # Performance settings
  batch_size: 100                   # Bulk insert batch size
  flush_interval: 5                 # Seconds between flushes
  compression: true                 # Compress old audit data

# Approval queue settings
approval:
  enabled: true
  timeout_minutes:
    LOW: 240                        # 4 hours
    MEDIUM: 120                     # 2 hours
    HIGH: 60                        # 1 hour
    CRITICAL: 30                    # 30 minutes
  
  # Auto-approval rules
  auto_approve:
    enabled: true
    trust_level_threshold: 3        # Level 3+ agents
    whitelist:
      - "file_read"                 # Safe read operations
      - "web_fetch_safe_domains"    # Pre-approved domains
    blacklist:
      - "system_command"            # Always require approval
      - "file_write_system"         # System file modifications

# Rate limiting
rate_limiting:
  enabled: true
  algorithm: "token_bucket"
  
  # Per-trust-level limits
  limits:
    level_0:                        # Untrusted
      requests_per_minute: 10
      mcp_calls_per_hour: 5
      web_fetches_per_hour: 2
    level_1:                        # Basic
      requests_per_minute: 30
      mcp_calls_per_hour: 50
      web_fetches_per_hour: 20
    level_2:                        # Standard
      requests_per_minute: 100
      mcp_calls_per_hour: 200
      web_fetches_per_hour: 100
    level_3:                        # Trusted
      requests_per_minute: 300
      mcp_calls_per_hour: 500
      web_fetches_per_hour: 300
    level_4:                        # Admin
      requests_per_minute: 1000
      mcp_calls_per_hour: 2000
      web_fetches_per_hour: 1000
  
  # Burst settings
  burst_multiplier: 2.0             # Allow 2x burst capacity
  refill_interval: 1.0              # Refill every second

# Proxy settings
proxy:
  openclaw:
    host: "openclaw"
    port: 8000
    timeout: 30
    health_check: "/health"
  
  mcp:
    enabled: true
    timeout: 15
    max_concurrent: 10
    inspection:
      enabled: true
      check_params: true
      scan_results: true
  
  web:
    enabled: true
    timeout: 10
    max_size: "50MB"
    allowed_schemes: ["http", "https"]
    blocked_domains:
      - "malware.com"
      - "phishing.net"
    ssrf_protection: true
  
  ssh:
    enabled: true
    timeout: 30
    injection_check: true
    command_whitelist:
      - "ls"
      - "cat"
      - "pwd"
    command_blacklist:
      - "rm -rf"
      - "dd if="
      - ":(){ :|:& };:"              # Fork bomb

# Monitoring and alerting
monitoring:
  metrics:
    enabled: true
    endpoint: "/metrics"
    scrape_interval: 15
  
  health_checks:
    enabled: true
    endpoint: "/health"
    timeout: 5
    checks:
      - "database"
      - "openclaw"
      - "disk_space"
      - "memory_usage"
  
  alerts:
    webhook_url: "https://alerts.example.com/webhook"
    severity_threshold: "HIGH"      # Only alert on HIGH/CRITICAL
    rate_limit: 300                 # Max 1 alert per 5 minutes per type

# Development and debugging
development:
  debug: false
  log_level: "INFO"                 # DEBUG, INFO, WARN, ERROR
  profile: false                    # Enable performance profiling
  mock_openclaw: false             # Use mock OpenClaw for testing
```

### Egress Configuration (egress-config.yml)

```yaml
# Network egress control configuration
api_version: "v1"
kind: "EgressConfig"

# DNS filtering
dns:
  enabled: true
  upstream_servers:
    - "1.1.1.1"                     # Cloudflare DNS
    - "8.8.8.8"                     # Google DNS
  
  # Blocked domains/patterns
  blocklist:
    domains:
      - "malware.example.com"
      - "phishing.example.net"
    patterns:
      - "*.suspicious.tld"
      - "*.crypto-mining.*"
    categories:
      - "malware"
      - "phishing"
      - "adult"
      - "gambling"
  
  # Allowed domains (whitelist mode)
  allowlist:
    enabled: false                  # Set true for whitelist-only mode
    domains:
      - "github.com"
      - "*.googleapis.com"
      - "registry.npmjs.org"

# URL analysis
url_analysis:
  enabled: true
  services:
    - name: "virustotal"
      api_key_secret: "virustotal-api-key"
      timeout: 5
    - name: "urlvoid"
      api_key_secret: "urlvoid-api-key"
      timeout: 3
  
  # SSRF protection
  ssrf_protection:
    enabled: true
    blocked_ranges:
      - "10.0.0.0/8"                # Private networks
      - "172.16.0.0/12"
      - "192.168.0.0/16"
      - "127.0.0.0/8"               # Loopback
      - "169.254.0.0/16"            # Link-local
      - "::1/128"                   # IPv6 loopback
      - "fe80::/10"                 # IPv6 link-local
    
    # Allowed private IPs (exceptions)
    allowed_private:
      - "192.168.1.100"             # Specific trusted internal services
  
  # Content analysis
  content_scan:
    enabled: true
    max_size: "10MB"
    scan_types:
      - "malware"
      - "pii"
      - "secrets"
    
    # File type restrictions
    allowed_types:
      - "text/plain"
      - "text/html"
      - "application/json"
      - "text/markdown"
    blocked_types:
      - "application/x-executable"
      - "application/x-dosexec"

# MCP server access control
mcp_access:
  # Default policy (ALLOW or DENY)
  default_policy: "DENY"
  
  # Per-server rules
  servers:
    filesystem:
      policy: "ALLOW"
      restrictions:
        trust_level_required: 2
        allowed_paths:
          - "/workspace/*"
          - "/tmp/*"
        blocked_paths:
          - "/etc/*"
          - "/root/*"
          - "/proc/*"
        max_file_size: "100MB"
    
    web:
      policy: "ALLOW"
      restrictions:
        trust_level_required: 1
        rate_limit: 100              # Per hour
        timeout: 10
    
    ssh:
      policy: "ALLOW"
      restrictions:
        trust_level_required: 3
        approval_required: true
        allowed_hosts:
          - "ssh://trusted-server:22"
        command_inspection: true

# Network policy
network:
  # Outbound connection rules
  outbound:
    default_policy: "ALLOW"
    
    # Port restrictions
    blocked_ports:
      - 22                          # SSH (use SSH proxy instead)
      - 23                          # Telnet
      - 135                         # RPC
      - 445                         # SMB
    
    allowed_ports:
      - 80                          # HTTP
      - 443                         # HTTPS
      - 587                         # SMTP TLS
      - 993                         # IMAP SSL
      - 5432                        # PostgreSQL (if needed)
  
  # Geographic restrictions
  geo_blocking:
    enabled: false
    blocked_countries: []           # ISO country codes
    allowed_countries: []           # Whitelist mode if not empty

# Logging and monitoring
logging:
  egress_events: true
  blocked_requests: true
  performance_metrics: true
  retention_days: 90
```

### MCP Configuration (mcp-config.yml)

```yaml
# MCP (Model Context Protocol) configuration
api_version: "v1"
kind: "MCPConfig"

# Global MCP settings
global:
  timeout_seconds: 30
  max_concurrent: 20
  retry_attempts: 3
  retry_backoff: 1.0                # Initial retry delay

# Server definitions
servers:
  filesystem:
    transport:
      type: "stdio"
      command: "npx"
      args:
        - "@modelcontextprotocol/server-filesystem"
        - "/workspace"
    
    # Security settings
    security:
      sandbox: true                 # Enable sandboxing
      allowed_operations:
        - "read_file"
        - "write_file"
        - "list_directory"
        - "create_directory"
      blocked_operations:
        - "delete_file"             # Require approval
        - "execute_file"            # Never allow
      
      # Path restrictions
      allowed_paths:
        - "/workspace/**"
        - "/tmp/**"
      blocked_paths:
        - "/etc/**"
        - "/root/**"
        - "/proc/**"
        - "/sys/**"
      
      # File size limits
      max_read_size: "10MB"
      max_write_size: "5MB"
    
    # Trust level requirements
    trust_requirements:
      read_file: 1                  # Basic trust
      write_file: 2                 # Standard trust
      create_directory: 2
      list_directory: 1
  
  web:
    transport:
      type: "stdio"
      command: "npx"
      args:
        - "@modelcontextprotocol/server-web"
    
    security:
      sandbox: true
      allowed_operations:
        - "fetch_url"
        - "search_web"
      blocked_operations: []
      
      # URL restrictions (in addition to egress config)
      allowed_schemes: ["http", "https"]
      max_response_size: "50MB"
      follow_redirects: true
      max_redirects: 5
    
    trust_requirements:
      fetch_url: 1
      search_web: 2
  
  ssh:
    transport:
      type: "stdio"
      command: "npx"
      args:
        - "@modelcontextprotocol/server-ssh"
    
    security:
      sandbox: true
      allowed_operations:
        - "execute_command"
        - "upload_file"
        - "download_file"
      blocked_operations:
        - "shell_access"            # Interactive shells blocked
      
      # Command restrictions
      command_inspection: true      # Deep command analysis
      allowed_commands:             # Whitelist approach
        - "ls"
        - "cat"
        - "pwd"
        - "whoami"
        - "df"
        - "ps"
      blocked_patterns:             # Additional safety net
        - "rm -rf"
        - "dd if="
        - ":(){ :|:& };:"           # Fork bomb
        - "curl * | bash"           # Dangerous pipes
      
      # Host restrictions
      allowed_hosts:
        - "ssh://dev-server:22"
        - "ssh://staging:22"
      
      # File transfer limits
      max_upload_size: "100MB"
      max_download_size: "100MB"
    
    trust_requirements:
      execute_command: 3            # Trusted agents only
      upload_file: 3
      download_file: 2

# Tool-specific configurations
tools:
  # File system tools
  read_file:
    rate_limit: 100                 # Per hour
    concurrent_limit: 5
    timeout: 10
  
  write_file:
    rate_limit: 50
    concurrent_limit: 3
    timeout: 15
    approval_required: false        # Auto-approve for trusted agents
  
  # Web tools
  fetch_url:
    rate_limit: 200
    concurrent_limit: 10
    timeout: 10
    cache_duration: 300             # Cache results for 5 minutes
  
  # SSH tools
  execute_command:
    rate_limit: 20                  # Very limited
    concurrent_limit: 1             # One at a time
    timeout: 60
    approval_required: true         # Always require approval
    audit_level: "VERBOSE"          # Full command logging

# Monitoring and debugging
monitoring:
  track_performance: true
  log_all_calls: true
  log_parameters: true              # Log sanitized parameters
  log_responses: false              # Don't log large responses
  
  # Performance thresholds
  slow_call_threshold: 5.0          # Seconds
  error_rate_threshold: 0.1         # 10% error rate triggers alert
  
  # Health checks
  health_check_interval: 30         # Seconds
  unhealthy_threshold: 3            # Failed checks before marking unhealthy
```

## Docker Secrets Structure

SecureClaw uses Docker secrets for sensitive configuration data.

### Secret File Structure

```bash
# Docker secrets directory structure
/run/secrets/
├── secureclaw-db-password          # Database password
├── openclaw-api-key               # OpenClaw API key
├── virustotal-api-key             # VirusTotal API key (optional)
├── urlvoid-api-key                # URLVoid API key (optional)
├── smtp-password                  # Email notification password
├── webhook-secret                 # Alert webhook secret
├── ssl-cert                       # SSL certificate
├── ssl-key                        # SSL private key
└── admin-token                    # Admin API token
```

### Secret Definitions (docker-compose.yml)

```yaml
secrets:
  secureclaw-db-password:
    external: true                  # Created externally
  
  openclaw-api-key:
    file: ./secrets/openclaw-api-key.txt
  
  virustotal-api-key:
    file: ./secrets/virustotal-api-key.txt
  
  urlvoid-api-key:
    file: ./secrets/urlvoid-api-key.txt
  
  smtp-password:
    file: ./secrets/smtp-password.txt
  
  webhook-secret:
    file: ./secrets/webhook-secret.txt
  
  ssl-cert:
    file: ./certs/server.crt
  
  ssl-key:
    file: ./certs/server.key
  
  admin-token:
    file: ./secrets/admin-token.txt

services:
  secureclaw:
    image: secureclaw:latest
    secrets:
      - secureclaw-db-password
      - openclaw-api-key
      - virustotal-api-key
      - urlvoid-api-key
      - smtp-password
      - webhook-secret
      - ssl-cert
      - ssl-key
      - admin-token
    environment:
      - SECURECLAW_DB_PASSWORD_FILE=/run/secrets/secureclaw-db-password
      - OPENCLAW_API_KEY_FILE=/run/secrets/openclaw-api-key
      - VIRUSTOTAL_API_KEY_FILE=/run/secrets/virustotal-api-key
      - URLVOID_API_KEY_FILE=/run/secrets/urlvoid-api-key
      - SMTP_PASSWORD_FILE=/run/secrets/smtp-password
      - WEBHOOK_SECRET_FILE=/run/secrets/webhook-secret
      - SSL_CERT_FILE=/run/secrets/ssl-cert
      - SSL_KEY_FILE=/run/secrets/ssl-key
      - ADMIN_TOKEN_FILE=/run/secrets/admin-token
```

### Secret Content Examples

```bash
# openclaw-api-key.txt
sk-1234567890abcdef1234567890abcdef

# virustotal-api-key.txt (optional)
a1b2c3d4e5f6789012345678901234567890abcd

# smtp-password.txt
app_specific_password_from_gmail

# webhook-secret.txt
webhook_signing_secret_for_alerts

# admin-token.txt (JWT or API key)
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# Database password generation
openssl rand -hex 32 > secrets/secureclaw-db-password.txt
```

### Secret Rotation Script

```bash
#!/bin/bash
# rotate-secrets.sh - Rotate Docker secrets

SECRET_NAME="$1"
NEW_SECRET_FILE="$2"

if [ -z "$SECRET_NAME" ] || [ -z "$NEW_SECRET_FILE" ]; then
    echo "Usage: $0 <secret-name> <new-secret-file>"
    exit 1
fi

# Create new secret with timestamp
TIMESTAMP=$(date +%s)
NEW_SECRET="${SECRET_NAME}_${TIMESTAMP}"

echo "Creating new secret: $NEW_SECRET"
docker secret create "$NEW_SECRET" "$NEW_SECRET_FILE"

echo "Updating service to use new secret..."
docker service update --secret-rm "$SECRET_NAME" \
                      --secret-add "source=${NEW_SECRET},target=${SECRET_NAME}" \
                      secureclaw

echo "Removing old secret..."
docker secret rm "$SECRET_NAME"

echo "Renaming new secret..."
docker secret create "$SECRET_NAME" "$NEW_SECRET_FILE"
docker secret rm "$NEW_SECRET"

echo "Secret rotation complete for: $SECRET_NAME"
```

This schema documentation provides the complete data structure foundation for SecureClaw, ensuring consistency across all components and proper handling of sensitive data through Docker secrets.