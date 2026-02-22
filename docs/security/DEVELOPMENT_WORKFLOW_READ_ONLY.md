# Development Workflow: Read-Only Filesystem Strategy

**Date**: 2026-02-16
**Status**: Development Mode → Testing → Production Lockdown

---

## The Challenge

**Goal**: Production containers must be read-only (bot cannot modify OS)
**Reality**: During development, we need flexibility to install, configure, and debug

---

## Three-Phase Approach

### Phase A: Development Mode (Current)
**State**: `read_only: false`
**Purpose**: Install packages, configure services, debug issues
**Duration**: While actively adding features

### Phase B: Compatibility Testing
**State**: `read_only: true` (test mode)
**Purpose**: Verify all features work with read-only enabled
**Duration**: After each major feature addition

### Phase C: Production Lockdown
**State**: `read_only: true` (permanent)
**Purpose**: Immutable infrastructure, bot cannot modify OS
**Duration**: When feature development is complete

---

## Current Configuration Status

### What's Currently Writable (Development Mode)

```yaml
# docker/docker-compose.yml - CURRENT STATE
services:
  openclaw:
    read_only: false  # ← DEVELOPMENT MODE

  gateway:
    read_only: false  # ← DEVELOPMENT MODE
```

**Risk**: Bot CAN currently modify:
- `/usr/bin/`, `/usr/local/bin/` (system binaries)
- `/etc/` (system configuration)
- `/lib/`, `/usr/lib/` (system libraries)
- Container OS files

**Why This is OK Right Now**: We're actively installing Playwright, npm packages, and configuring services.

---

## Read-Only Compatibility Checklist

### For Each New Feature, Document:

#### 1. What Needs to WRITE?

**Example: Playwright Installation**
- ✅ `/home/node/.cache/ms-playwright/` - Browser binaries
- ✅ `/home/node/.npm/` - npm cache
- ✅ `/home/node/.local/` - User-local data
- ✅ `/tmp/` - Temporary files

**Solution**: All covered by existing tmpfs/volumes ✓

---

#### 2. What Needs to PERSIST?

**Example: 1Password Integration**
- ✅ `/home/node/.config/op/` - 1Password session
- ✅ `/run/secrets/` - Docker secrets (mounted read-only)

**Solution**:
- Session data → tmpfs on `/home/node/.config/`
- Secrets → Docker secrets (already read-only)

---

#### 3. What's System-Level?

**Example: OpenSCAP Installation**
- ❌ `/usr/share/xml/scap/` - SCAP content (requires apt install)
- ❌ `/usr/bin/oscap` - Binary (requires apt install)

**Solution**: Install during image build (Dockerfile), not at runtime

---

## Development Workflow

### Step 1: Add Feature (read_only: false)

```bash
# Current state - development mode
docker-compose up -d

# Install packages freely
docker exec openclaw-bot npm install playwright
docker exec openclaw-bot npx playwright install chromium

# Configure services
docker exec openclaw-bot node setup-service.js

# Debug and iterate
docker exec openclaw-bot bash
# Can modify anything, install packages, etc.
```

**Commit**: Feature working in development mode

---

### Step 2: Document Write Paths

Create a file documenting what the feature needs to write:

**File**: `docs/features/FEATURE_NAME_write_requirements.md`

```markdown
# Feature: Playwright Browser Automation

## Write Requirements

### Temporary (tmpfs):
- `/home/node/.cache/ms-playwright/` - Browser binaries (500MB)
- `/tmp/playwright-*` - Screenshot temp files

### Persistent (volume):
- `/home/node/.openclaw/skills/securebrowser/` - Skill files
- `/home/node/workspace/screenshots/` - Saved screenshots

### System-level (Dockerfile):
- Playwright dependencies installed via apt
```

---

### Step 3: Test Read-Only Compatibility

```bash
# Enable read-only mode
sed -i 's/read_only: false/read_only: true/g' docker/docker-compose.yml

# Rebuild and start
docker-compose down
docker-compose up -d --build

# Test the feature
docker exec openclaw-bot node test-feature.js

# Watch for read-only errors
docker logs openclaw-bot --follow 2>&1 | grep -i "read-only"
```

**If errors occur**:
1. Identify the path attempting write
2. Add to tmpfs or volume mount
3. Repeat test

---

### Step 4: Add Missing Mounts

If testing reveals missing write paths:

```yaml
# docker/docker-compose.yml
services:
  openclaw:
    read_only: true
    tmpfs:
      - /tmp:exec,mode=1777
      - /var/tmp:exec,mode=1777
      - /home/node/.npm:uid=1000,gid=1000
      - /home/node/.cache:uid=1000,gid=1000
      - /home/node/.local:uid=1000,gid=1000
      - /home/node/.config:uid=1000,gid=1000
      - /home/node/.playwright:uid=1000,gid=1000  # NEW: If needed
```

---

### Step 5: Verify OS Immutability

After read-only mode is working, verify bot CANNOT modify OS:

```bash
# Test system directories are protected
docker exec openclaw-bot touch /etc/test-file
# Expected: "Read-only file system"

docker exec openclaw-bot touch /usr/bin/test-file
# Expected: "Read-only file system"

docker exec openclaw-bot rm /bin/sh
# Expected: "Read-only file system"

# Test workspace IS writable
docker exec openclaw-bot touch /home/node/workspace/test-file
# Expected: Success

docker exec openclaw-bot touch /home/node/.openclaw/test-file
# Expected: Success
```

---

### Step 6: Revert to Development if Needed

If testing breaks functionality:

```bash
# Back to development mode
sed -i 's/read_only: true/read_only: false/g' docker/docker-compose.yml
docker-compose up -d --build

# Debug and fix
# Document additional write paths needed
# Add to tmpfs/volumes
# Repeat Step 3
```

---

## Current Features: Write Requirements

### Feature: 1Password Integration
- ✅ **Tmpfs**: `/home/node/.config/op/` - Session token
- ✅ **Secrets**: `/run/secrets/1password_bot_*` - Credentials (read-only)
- ✅ **Dockerfile**: `op` CLI binary installed
- **Read-Only Compatible**: ✅ YES

---

### Feature: SecureBrowser (Playwright)
- ✅ **Tmpfs**: `/home/node/.cache/ms-playwright/` - Browser binaries
- ✅ **Tmpfs**: `/tmp/playwright-*` - Temp files
- ✅ **Volume**: `/home/node/.openclaw/skills/` - Skill definitions
- ✅ **Dockerfile**: Playwright dependencies via apt
- **Read-Only Compatible**: ⏳ NOT TESTED YET

---

### Feature: iCloud/Gmail Services
- ✅ **Volume**: `/home/node/workspace/` - Test scripts
- ✅ **Tmpfs**: `/home/node/.cache/` - npm cache
- ✅ **Secrets**: Credentials via 1Password
- **Read-Only Compatible**: ✅ YES

---

### Feature: Gateway (FastAPI)
- ✅ **Volume**: `/app/data/` - SQLite ledger
- ✅ **Tmpfs**: `/tmp/` - Temp files
- ✅ **Dockerfile**: Python packages in image
- **Read-Only Compatible**: ⏳ NOT TESTED YET

---

## Planned Features: Write Requirements

### Feature: SSH Proxy (Phase 4)
- ⏳ **Volume**: `/home/node/.ssh/` - SSH keys
- ⏳ **Volume**: `/home/node/workspace/` - Command output
- ⏳ **Tmpfs**: `/tmp/ssh-*` - Temp session files
- **Preparation**: Already have `openclaw-ssh` volume

---

### Feature: Kill Switch (Phase 3B)
- ⏳ **Volume**: `/app/data/incidents/` - Incident reports
- ⏳ **Tmpfs**: `/tmp/` - Temp forensics
- **Preparation**: Needs volume for incident persistence

---

### Feature: OpenSCAP Scanning (Phase 3A)
- ⏳ **Dockerfile**: `oscap` binary and SCAP content
- ⏳ **Volume**: `/app/reports/` - Scan reports
- ⏳ **Tmpfs**: `/tmp/oscap-*` - Temp scan files
- **Preparation**: Must install in Dockerfile, not runtime

---

## Testing Procedure: Read-Only Lockdown

### Pre-Lockdown Checklist

Before enabling `read_only: true` permanently:

- [ ] All npm packages installed
- [ ] All system packages installed (Dockerfile)
- [ ] All skills registered and tested
- [ ] All volumes mounted correctly
- [ ] All tmpfs paths identified
- [ ] All Docker secrets in place
- [ ] Gateway database initialized
- [ ] Configuration files written

---

### Lockdown Procedure

```bash
# 1. Stop containers
docker-compose down

# 2. Enable read-only in docker-compose.yml
cat > docker/docker-compose.yml <<'EOF'
services:
  openclaw:
    read_only: true  # ← PRODUCTION MODE
    tmpfs:
      - /tmp:exec,mode=1777
      - /var/tmp:exec,mode=1777
      - /home/node/.npm:uid=1000,gid=1000
      - /home/node/.cache:uid=1000,gid=1000
      - /home/node/.local:uid=1000,gid=1000
      - /home/node/.config:uid=1000,gid=1000
    volumes:
      - openclaw-config:/home/node/.openclaw:rw
      - openclaw-workspace:/home/node/workspace:rw
      - openclaw-ssh:/home/node/.ssh:rw
    # ... rest of config

  gateway:
    read_only: true  # ← PRODUCTION MODE
    tmpfs:
      - /tmp:exec,mode=1777
      - /var/tmp:exec,mode=1777
    volumes:
      - gateway-data:/app/data:rw
    # ... rest of config
EOF

# 3. Rebuild with lockdown
docker-compose up -d --build

# 4. Wait for healthy
sleep 60
docker-compose ps

# 5. Verify read-only
docker inspect openclaw-bot --format '{{.HostConfig.ReadonlyRootfs}}'
# Expected: true

docker inspect openclaw-gateway --format '{{.HostConfig.ReadonlyRootfs}}'
# Expected: true

# 6. Test OS immutability
./docker/scripts/verify-security.sh
```

---

### Functional Testing (Read-Only Mode)

Test every major feature to ensure it still works:

```bash
# Test 1: 1Password retrieval
docker exec openclaw-bot 1password-skill get-field "Apple ID - agentshroud.ai" "oenclaw bot password"
# Expected: Password retrieved successfully

# Test 2: iCloud services
docker exec openclaw-bot node /home/node/icloud-services-working.js
# Expected: Calendar and Contacts connected

# Test 3: Gmail IMAP
docker exec openclaw-bot node /home/node/test-gmail-imap.js
# Expected: IMAP connected, 33 messages

# Test 4: Gateway API
curl -X POST http://localhost:8080/forward \
  -H "Authorization: Bearer $GATEWAY_PASSWORD" \
  -d '{"messages": [{"role": "user", "content": "hello"}]}'
# Expected: Response from LLM

# Test 5: Approval queue
curl http://localhost:8080/approval/queue \
  -H "Authorization: Bearer $GATEWAY_PASSWORD"
# Expected: Queue data returned

# Test 6: Audit ledger
curl http://localhost:8080/ledger \
  -H "Authorization: Bearer $GATEWAY_PASSWORD"
# Expected: Ledger entries

# Test 7: Telegram bot
# Send message via Telegram
# Expected: Bot responds

# Test 8: Bot cannot modify OS
docker exec openclaw-bot touch /etc/malicious-file
# Expected: "Read-only file system" error
```

---

### If Any Test Fails

1. **Identify the write path**:
   ```bash
   docker logs openclaw-bot --tail 100 | grep -i "read-only"
   ```

2. **Determine if it's legitimate**:
   - Temporary data? → Add to tmpfs
   - Persistent data? → Add to volume
   - System modification? → FIX THE CODE (this shouldn't happen)

3. **Temporarily disable read-only**:
   ```bash
   sed -i 's/read_only: true/read_only: false/g' docker/docker-compose.yml
   docker-compose up -d
   ```

4. **Debug and fix**:
   - Install missing package in Dockerfile
   - Add missing tmpfs mount
   - Fix code to use proper paths

5. **Re-test with read-only enabled**

---

## Emergency Rollback

If read-only mode breaks production:

```bash
# Quick rollback to development mode
docker-compose down
git checkout docker/docker-compose.yml  # Revert changes
docker-compose up -d

# System is now writable again for emergency fixes
```

---

## Current Recommendation

**For Right Now (Active Development)**:

```yaml
# docker/docker-compose.yml - KEEP AS-IS
services:
  openclaw:
    read_only: false  # Development mode

  gateway:
    read_only: false  # Development mode
```

**When to Enable Read-Only**:

1. ✅ **After Phase 3A is complete** (seccomp, security hardening)
2. ✅ **After Phase 3B is complete** (kill switch)
3. ✅ **Before Phase 6** (documentation and compliance)
4. ✅ **Before external hosting**
5. ✅ **Before multi-tenant deployment**

**Testing Cadence**:

- 🔄 **After each major feature**: Quick read-only test (30 min)
- 🔄 **After each phase**: Full read-only test (2 hours)
- ✅ **Final lockdown**: Before v1.0 release

---

## Write Paths Inventory

### Currently Documented

| Path | Type | Purpose | Mounted |
|------|------|---------|---------|
| `/home/node/.openclaw/` | Volume | OpenClaw config, skills, memory | ✅ Yes |
| `/home/node/workspace/` | Volume | Bot workspace, scripts | ✅ Yes |
| `/home/node/.ssh/` | Volume | SSH keys | ✅ Yes |
| `/tmp/` | tmpfs | Temporary files | ✅ Yes |
| `/var/tmp/` | tmpfs | Temporary files | ✅ Yes |
| `/home/node/.npm/` | tmpfs | npm cache | ✅ Yes |
| `/home/node/.cache/` | tmpfs | Application cache | ✅ Yes |
| `/home/node/.local/` | tmpfs | User-local data | ✅ Yes |
| `/home/node/.config/` | tmpfs | App config cache | ✅ Yes |
| `/app/data/` | Volume | Gateway database | ✅ Yes |

### Potentially Needed (Discovered During Testing)

| Path | Type | Purpose | Status |
|------|------|---------|--------|
| `/home/node/.playwright/` | tmpfs? | Playwright cache | ⏳ Test needed |
| `/home/node/.op/` | tmpfs | 1Password session | ⏳ Test needed |
| `/var/log/` | tmpfs? | Application logs | ⏳ Test needed |

---

## Development Mode Script

Create helper script for toggling modes:

**File**: `docker/scripts/toggle-readonly.sh`

```bash
#!/bin/bash
set -euo pipefail

MODE="${1:-}"

if [ "$MODE" = "dev" ]; then
    echo "🔧 Enabling DEVELOPMENT mode (read-write)"
    sed -i 's/read_only: true/read_only: false/g' docker/docker-compose.yml
    echo "✅ Containers will be writable"

elif [ "$MODE" = "prod" ]; then
    echo "🔒 Enabling PRODUCTION mode (read-only)"
    sed -i 's/read_only: false/read_only: true/g' docker/docker-compose.yml
    echo "✅ Containers will be read-only"

elif [ "$MODE" = "test" ]; then
    echo "🧪 Testing read-only mode..."

    # Enable read-only
    sed -i 's/read_only: false/read_only: true/g' docker/docker-compose.yml

    # Rebuild
    docker-compose down
    docker-compose up -d --build

    # Wait for healthy
    echo "Waiting for containers to be healthy..."
    sleep 30

    # Test OS immutability
    echo ""
    echo "Testing OS immutability..."

    if docker exec openclaw-bot touch /etc/test-file 2>&1 | grep -q "Read-only file system"; then
        echo "✅ OpenClaw OS is read-only"
    else
        echo "❌ OpenClaw OS is WRITABLE (BAD)"
    fi

    if docker exec openclaw-bot touch /home/node/workspace/test-file 2>&1; then
        echo "✅ OpenClaw workspace is writable"
        docker exec openclaw-bot rm /home/node/workspace/test-file
    else
        echo "❌ OpenClaw workspace is read-only (BAD)"
    fi

    if docker exec openclaw-gateway touch /etc/test-file 2>&1 | grep -q "Read-only file system"; then
        echo "✅ Gateway OS is read-only"
    else
        echo "❌ Gateway OS is WRITABLE (BAD)"
    fi

    if docker exec openclaw-gateway touch /app/data/test-file 2>&1; then
        echo "✅ Gateway data is writable"
        docker exec openclaw-gateway rm /app/data/test-file
    else
        echo "❌ Gateway data is read-only (BAD)"
    fi

    echo ""
    echo "Read-only test complete!"

else
    echo "Usage: $0 {dev|prod|test}"
    echo ""
    echo "  dev   - Enable development mode (read-write)"
    echo "  prod  - Enable production mode (read-only)"
    echo "  test  - Test read-only mode and verify"
    exit 1
fi

echo ""
echo "Run 'docker-compose up -d' to apply changes"
```

**Usage**:
```bash
# Switch to development mode
./docker/scripts/toggle-readonly.sh dev
docker-compose up -d

# Test read-only compatibility
./docker/scripts/toggle-readonly.sh test

# Switch to production mode
./docker/scripts/toggle-readonly.sh prod
docker-compose up -d
```

---

## Summary

**Current State**: Development mode (`read_only: false`)
**Reason**: Active feature development (Playwright, services, skills)

**Process**:
1. ✅ Add features in development mode
2. ✅ Document write requirements
3. ✅ Test with read-only enabled
4. ✅ Add missing tmpfs/volumes
5. ✅ Verify OS immutability
6. ✅ Lock down for production

**Target State**: Production mode (`read_only: true`)
**Timeline**: After Phase 3-4 features complete, before external hosting

**Safety**: Can always roll back to development mode if issues arise

---

**This balances security (read-only is the goal) with practicality (we need flexibility during development).**
