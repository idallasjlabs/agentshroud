#!/bin/bash
set -e

###############################################################################
# One Claw Tied Behind Your Back - OpenClaw Deployment Script
# Automated setup for secure OpenClaw deployment on macOS
#
# Author: Isaiah Jefferson
# Project: Secure, isolated AI assistant deployment
# License: MIT
###############################################################################

PROJECT_NAME="one-claw-tied-behind-your-back"
INSTALL_DIR="$HOME/.oneclaw-secure"
COMPOSE_FILE="$INSTALL_DIR/docker compose.yml"
CONFIG_FILE="$INSTALL_DIR/config/oneclaw.json"
SECRETS_FILE="$INSTALL_DIR/secrets/.env"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}"
echo "╔════════════════════════════════════════════════════════════╗"
echo "║  One Claw Tied Behind Your Back - OpenClaw Deployment     ║"
echo "║  Secure containerized AI assistant for macOS               ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo -e "${NC}"
echo ""

# Function: Print colored messages
print_step() {
    echo -e "${BLUE}[$1]${NC} $2"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠️${NC}  $1"
}

print_error() {
    echo -e "${RED}ERROR:${NC} $1"
}

# Function: Check prerequisites
check_prerequisites() {
    print_step "1/10" "Checking prerequisites..."

    # Check macOS version
    if [[ $(uname) != "Darwin" ]]; then
        print_error "This script requires macOS"
        exit 1
    fi

    OS_VERSION=$(sw_vers -productVersion)
    print_success "macOS $OS_VERSION detected"

    # Check for Docker/OrbStack
    if command -v orb &> /dev/null; then
        DOCKER_RUNTIME="orbstack"
        DOCKER_CMD="orb"
        print_success "Found OrbStack (recommended)"
    elif command -v docker &> /dev/null; then
        DOCKER_RUNTIME="docker"
        DOCKER_CMD="docker"
        print_success "Found Docker Desktop"
    else
        print_error "Docker Desktop or OrbStack required"
        echo ""
        echo "Install OrbStack (recommended):"
        echo "  brew install --cask orbstack"
        echo ""
        echo "Or Docker Desktop:"
        echo "  brew install --cask docker"
        exit 1
    fi

    # Check if Docker is running
    if ! $DOCKER_CMD ps &> /dev/null; then
        print_error "$DOCKER_RUNTIME is not running"
        echo "Please start $DOCKER_RUNTIME and try again"
        exit 1
    fi

    # Check for Node.js 22+
    if command -v node &> /dev/null; then
        NODE_VERSION=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
        if [[ $NODE_VERSION -ge 22 ]]; then
            print_success "Node.js $(node -v) installed"
        else
            print_error "Node.js 22+ required (found: v$NODE_VERSION)"
            echo ""
            echo "Install Node.js 22:"
            echo "  brew install node@22"
            exit 1
        fi
    else
        print_error "Node.js not found"
        echo ""
        echo "Install Node.js 22:"
        echo "  brew install node@22"
        exit 1
    fi

    # Check for npm
    if ! command -v npm &> /dev/null; then
        print_error "npm not found (should come with Node.js)"
        exit 1
    fi

    # Check disk space (need at least 10GB)
    AVAILABLE_GB=$(df -g "$HOME" | awk 'NR==2 {print $4}')
    if [[ $AVAILABLE_GB -lt 10 ]]; then
        print_warning "Low disk space: ${AVAILABLE_GB}GB available (10GB recommended)"
        read -p "Continue anyway? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            exit 1
        fi
    else
        print_success "Sufficient disk space: ${AVAILABLE_GB}GB available"
    fi

    # Check for jq (optional but helpful)
    if ! command -v jq &> /dev/null; then
        print_warning "jq not installed (recommended for JSON processing)"
        echo "  Install with: brew install jq"
    fi

    echo ""
}

# Function: Setup directory structure
setup_directories() {
    print_step "2/10" "Setting up directories..."

    # Create main directories
    mkdir -p "$INSTALL_DIR"/{config,workspace,secrets,logs,macos-bridge}
    mkdir -p "$INSTALL_DIR/workspace"/{files,cache,tools}
    mkdir -p "$INSTALL_DIR/config"

    # Set strict permissions on secrets directory
    chmod 700 "$INSTALL_DIR/secrets"

    # Create .gitignore in install directory
    cat > "$INSTALL_DIR/.gitignore" <<'EOF'
# Never commit secrets
secrets/
*.env

# Logs
logs/
*.log

# Workspace data
workspace/

# macOS
.DS_Store
EOF

    print_success "Directories created at $INSTALL_DIR"
    echo ""
}

# Function: Generate secrets
generate_secrets() {
    print_step "3/10" "Generating secrets..."

    # Generate random tokens
    GATEWAY_TOKEN=$(openssl rand -hex 32)
    WEBHOOK_SECRET=$(openssl rand -hex 32)
    BLUEBUBBLES_PASSWORD=$(openssl rand -hex 16)

    # Create .env file
    cat > "$SECRETS_FILE" <<EOF
# OpenClaw Secrets - NEVER commit to git or share publicly
# Generated: $(date)
# Project: One Claw Tied Behind Your Back

###############################################################################
# Gateway Authentication
###############################################################################
GATEWAY_TOKEN=$GATEWAY_TOKEN
OPENCLAW_GATEWAY_TOKEN=$GATEWAY_TOKEN

###############################################################################
# Webhook Authentication
###############################################################################
WEBHOOK_SECRET=$WEBHOOK_SECRET

###############################################################################
# BlueBubbles (iMessage Integration)
###############################################################################
BLUEBUBBLES_PASSWORD=$BLUEBUBBLES_PASSWORD

###############################################################################
# AI Provider API Keys
# REQUIRED: Add at least one AI provider API key
###############################################################################

# Anthropic Claude (Recommended)
ANTHROPIC_API_KEY=

# OpenAI (Optional)
OPENAI_API_KEY=

# Google Gemini (Optional)
GEMINI_API_KEY=

# OpenRouter (Optional - aggregator)
OPENROUTER_API_KEY=

###############################################################################
# Messaging Platform Tokens
###############################################################################

# Telegram (Recommended - create via @BotFather)
# Bot username: @therealidallasj
TELEGRAM_BOT_TOKEN=

# Slack (Optional)
SLACK_APP_TOKEN=
SLACK_BOT_TOKEN=

# Discord (Optional)
DISCORD_BOT_TOKEN=

###############################################################################
# Google Services (Gmail, Calendar, Tasks)
# Account: therealidallasj@gmail.com
###############################################################################

# Gmail API
GMAIL_CLIENT_ID=
GMAIL_CLIENT_SECRET=

# Google Calendar API
GOOGLE_CALENDAR_CLIENT_ID=
GOOGLE_CALENDAR_CLIENT_SECRET=

# Google Tasks API
GOOGLE_TASKS_CLIENT_ID=
GOOGLE_TASKS_CLIENT_SECRET=

###############################################################################
# Optional Services
###############################################################################

# PayPal (for purchases)
PAYPAL_CLIENT_ID=
PAYPAL_CLIENT_SECRET=

# Search APIs
BRAVE_API_KEY=
PERPLEXITY_API_KEY=

# Voice/TTS
ELEVENLABS_API_KEY=

# Web Scraping
FIRECRAWL_API_KEY=
EOF

    # Set strict permissions
    chmod 600 "$SECRETS_FILE"

    print_success "Secrets generated at $SECRETS_FILE"
    print_warning "IMPORTANT: Add your API keys to this file before starting OpenClaw"
    echo ""
}

# Function: Create OpenClaw configuration
create_config() {
    print_step "4/10" "Creating OpenClaw configuration..."

    cat > "$CONFIG_FILE" <<'EOF'
{
  "gateway": {
    "bind": "0.0.0.0",
    "port": 18789,
    "auth": {
      "mode": "token"
    },
    "tailscale": {
      "mode": "off"
    }
  },
  "agents": {
    "defaults": {
      "model": "anthropic/claude-opus-4-6",
      "sandbox": {
        "mode": "agent",
        "scope": "agent"
      },
      "workspace": "/workspace",
      "maxTurns": 50,
      "temperature": 0.7
    }
  },
  "channels": {
    "telegram": {
      "enabled": true,
      "dm": {
        "policy": "pairing"
      },
      "group": {
        "policy": "allowlist"
      }
    },
    "bluebubbles": {
      "enabled": true,
      "serverUrl": "http://host.docker.internal:3000",
      "webhookPath": "/bluebubbles-webhook",
      "dm": {
        "policy": "pairing"
      }
    },
    "webchat": {
      "enabled": true,
      "port": 18790
    }
  },
  "security": {
    "audit": {
      "enabled": true,
      "logPath": "/workspace/logs/audit.log",
      "retention": "30d"
    },
    "exec": {
      "approvals": {
        "enabled": true,
        "timeout": 300
      }
    },
    "sandbox": {
      "enabled": true,
      "allowedTools": ["bash", "read", "write", "sessions"]
    }
  },
  "skills": {
    "registry": "https://clawhub.ai",
    "autoUpdate": false,
    "verifySignatures": true
  },
  "browser": {
    "enabled": true,
    "headless": true,
    "userAgent": "OpenClaw/1.0"
  },
  "logging": {
    "level": "info",
    "format": "json",
    "outputs": ["file", "console"]
  }
}
EOF

    print_success "Configuration created at $CONFIG_FILE"
    echo ""
}

# Function: Create Docker Compose file
create_docker_compose() {
    print_step "5/10" "Creating Docker Compose configuration..."

    # Copy secure build files to install directory
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

    if [[ -f "$SCRIPT_DIR/docker compose.secure.yml" ]] && [[ -f "$SCRIPT_DIR/Dockerfile.secure" ]]; then
        cp "$SCRIPT_DIR/docker compose.secure.yml" "$COMPOSE_FILE"
        cp "$SCRIPT_DIR/Dockerfile.secure" "$INSTALL_DIR/Dockerfile"

        # Create .env file for docker compose
        cat > "$INSTALL_DIR/.env" <<EOF
OPENCLAW_WORKSPACE_DIR=$INSTALL_DIR/workspace
OPENCLAW_CONFIG_DIR=$INSTALL_DIR/config
OPENCLAW_LOGS_DIR=$INSTALL_DIR/logs
EOF

        print_success "Secure Docker Compose configuration created"
        print_success "Dockerfile copied (all builds happen in container)"
    else
        print_error "Secure Docker files not found in $SCRIPT_DIR"
        print_error "Please ensure docker compose.secure.yml and Dockerfile.secure exist"
        exit 1
    fi

    echo ""
}

# Function: Create macOS bridge service
create_macos_bridge() {
    print_step "6/10" "Creating macOS bridge service..."

    cd "$INSTALL_DIR/macos-bridge"

    # Create package.json
    cat > package.json <<'EOF'
{
  "name": "openclaw-macos-bridge",
  "version": "1.0.0",
  "description": "macOS-specific integration bridge for OpenClaw (BlueBubbles relay)",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  },
  "dependencies": {
    "express": "^4.18.2",
    "ws": "^8.16.0"
  },
  "author": "Isaiah Jefferson",
  "license": "MIT"
}
EOF

    # Create bridge service
    cat > index.js <<'EOF'
const express = require('express');
const WebSocket = require('ws');

const app = express();
app.use(express.json());

let ws;
let reconnectAttempts = 0;
const MAX_RECONNECT_ATTEMPTS = 5;

function connectWebSocket() {
  ws = new WebSocket('ws://localhost:18789');

  ws.on('open', () => {
    console.log('[Bridge] Connected to OpenClaw gateway');
    reconnectAttempts = 0;
  });

  ws.on('error', (error) => {
    console.error('[Bridge] WebSocket error:', error.message);
  });

  ws.on('close', () => {
    console.log('[Bridge] Disconnected from gateway');

    // Attempt to reconnect with exponential backoff
    if (reconnectAttempts < MAX_RECONNECT_ATTEMPTS) {
      const delay = Math.min(1000 * Math.pow(2, reconnectAttempts), 30000);
      console.log(`[Bridge] Reconnecting in ${delay}ms... (attempt ${reconnectAttempts + 1}/${MAX_RECONNECT_ATTEMPTS})`);
      reconnectAttempts++;
      setTimeout(connectWebSocket, delay);
    } else {
      console.error('[Bridge] Max reconnection attempts reached. Please check OpenClaw gateway.');
    }
  });

  ws.on('message', (data) => {
    console.log('[Bridge] Message from gateway:', data.toString().substring(0, 100));
  });
}

// BlueBubbles webhook relay
app.post('/bluebubbles-webhook', (req, res) => {
  console.log('[Bridge] Received BlueBubbles webhook');

  if (ws && ws.readyState === WebSocket.OPEN) {
    ws.send(JSON.stringify({
      type: 'bluebubbles_event',
      data: req.body,
      timestamp: Date.now()
    }));
    res.sendStatus(200);
  } else {
    console.error('[Bridge] WebSocket not connected, cannot relay webhook');
    res.status(503).json({ error: 'Gateway connection unavailable' });
  }
});

// Health check endpoint
app.get('/health', (req, res) => {
  const wsState = ws ? ['CONNECTING', 'OPEN', 'CLOSING', 'CLOSED'][ws.readyState] : 'DISCONNECTED';
  res.json({
    status: 'ok',
    websocket: wsState,
    uptime: process.uptime()
  });
});

// Start WebSocket connection
connectWebSocket();

// Start HTTP server
const PORT = 8765;
app.listen(PORT, '127.0.0.1', () => {
  console.log(`[Bridge] macOS Bridge listening on http://127.0.0.1:${PORT}`);
  console.log('[Bridge] Ready to relay BlueBubbles webhooks to OpenClaw container');
});

// Graceful shutdown
process.on('SIGTERM', () => {
  console.log('[Bridge] Received SIGTERM, shutting down gracefully...');
  if (ws) ws.close();
  process.exit(0);
});

process.on('SIGINT', () => {
  console.log('[Bridge] Received SIGINT, shutting down gracefully...');
  if (ws) ws.close();
  process.exit(0);
});
EOF

    # Install dependencies quietly
    echo "Installing bridge dependencies..."
    npm install --silent --no-progress 2>&1 | grep -v "^npm WARN" || true

    # Create LaunchAgent for auto-start
    mkdir -p ~/Library/LaunchAgents

    cat > ~/Library/LaunchAgents/com.oneclaw.macos-bridge.plist <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.oneclaw.macos-bridge</string>
    <key>ProgramArguments</key>
    <array>
        <string>$(which node)</string>
        <string>$INSTALL_DIR/macos-bridge/index.js</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <dict>
        <key>SuccessfulExit</key>
        <false/>
    </dict>
    <key>StandardErrorPath</key>
    <string>$INSTALL_DIR/logs/macos-bridge.err</string>
    <key>StandardOutPath</key>
    <string>$INSTALL_DIR/logs/macos-bridge.out</string>
    <key>WorkingDirectory</key>
    <string>$INSTALL_DIR/macos-bridge</string>
</dict>
</plist>
EOF

    print_success "macOS bridge service created"
    print_success "LaunchAgent created at ~/Library/LaunchAgents/com.oneclaw.macos-bridge.plist"
    echo ""
}

# Function: Configure firewall
configure_firewall() {
    print_step "7/10" "Configuring firewall..."

    # Create container-level firewall rules script
    cat > "$INSTALL_DIR/config/container-firewall.sh" <<'EOF'
#!/bin/sh
# Container-level firewall rules
# Block private IP ranges (RFC1918), allow internet

# Block private networks
iptables -A OUTPUT -d 192.168.0.0/16 -j DROP
iptables -A OUTPUT -d 172.16.0.0/12 -j DROP
iptables -A OUTPUT -d 10.0.0.0/8 -j DROP
iptables -A OUTPUT -d 169.254.0.0/16 -j DROP

# Allow localhost
iptables -A OUTPUT -d 127.0.0.0/8 -j ACCEPT

# Allow internet
iptables -A OUTPUT -j ACCEPT
EOF

    chmod +x "$INSTALL_DIR/config/container-firewall.sh"

    # Check for application firewalls
    if [[ -f "/Applications/Little Snitch.app/Contents/MacOS/Little Snitch" ]]; then
        print_success "Little Snitch detected"
        print_warning "Configure Little Snitch rules:"
        echo "  1. Open Little Snitch"
        echo "  2. Find process: com.docker.vpnkit"
        echo "  3. Block connections to: 192.168.0.0/16, 172.16.0.0/12, 10.0.0.0/8"
        echo "  4. Allow connections to: Internet"
    elif [[ -f "/Applications/LuLu.app/Contents/MacOS/LuLu" ]]; then
        print_success "Lulu detected"
        print_warning "Configure Lulu rules for com.docker.vpnkit to block LAN access"
    else
        print_warning "No application firewall detected"
        echo ""
        echo "For maximum security, install an application firewall:"
        echo "  Little Snitch (recommended): https://www.obdev.at/products/littlesnitch/"
        echo "  Lulu (free): brew install --cask lulu"
        echo ""
    fi

    echo ""
}

# Function: Create management scripts
create_management_scripts() {
    print_step "8/10" "Creating management scripts..."

    # Start script
    cat > "$INSTALL_DIR/start.sh" <<'STARTEOF'
#!/bin/bash
cd "$(dirname "$0")"

echo "Starting OpenClaw services..."
echo ""

# Start Docker containers
echo "Starting container..."
docker compose up -d

# Wait for gateway to be ready
echo "Waiting for gateway to be ready..."
for i in {1..30}; do
    if curl -s http://localhost:18789/health > /dev/null 2>&1; then
        echo "✓ Gateway is ready"
        break
    fi
    if [ $i -eq 30 ]; then
        echo "⚠️  Gateway health check timeout (may still be starting)"
    fi
    sleep 2
done

# Start macOS bridge
echo "Starting macOS bridge..."
launchctl load ~/Library/LaunchAgents/com.oneclaw.macos-bridge.plist 2>/dev/null || echo "Bridge already loaded"

echo ""
echo "✓ OpenClaw is running"
echo ""
echo "Access points:"
echo "  Gateway API: http://localhost:18789"
echo "  WebChat UI:  http://localhost:18790"
echo "  Bridge API:  http://localhost:8765"
echo ""
echo "View logs:"
echo "  ./logs.sh"
echo ""
STARTEOF

    # Stop script
    cat > "$INSTALL_DIR/stop.sh" <<'STOPEOF'
#!/bin/bash
cd "$(dirname "$0")"

echo "Stopping OpenClaw services..."

# Stop macOS bridge
launchctl unload ~/Library/LaunchAgents/com.oneclaw.macos-bridge.plist 2>/dev/null || true

# Stop Docker containers
docker compose down

echo "✓ All services stopped"
STOPEOF

    # Status script
    cat > "$INSTALL_DIR/status.sh" <<'STATUSEOF'
#!/bin/bash

echo "=== OpenClaw Status ==="
echo ""

echo "Container:"
docker ps --filter "name=oneclaw_gateway" --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
echo ""

echo "macOS Bridge:"
launchctl list | grep com.oneclaw.macos-bridge || echo "Not running"
echo ""

echo "Gateway Health:"
curl -s http://localhost:18789/health 2>/dev/null | jq . 2>/dev/null || echo "Gateway not responding"
echo ""

echo "Bridge Health:"
curl -s http://localhost:8765/health 2>/dev/null | jq . 2>/dev/null || echo "Bridge not responding"
echo ""

echo "Resource Usage:"
docker stats oneclaw_gateway --no-stream 2>/dev/null || echo "Container not running"
STATUSEOF

    # Logs script
    cat > "$INSTALL_DIR/logs.sh" <<'LOGSEOF'
#!/bin/bash
cd "$(dirname "$0")"

echo "=== OpenClaw Logs (Ctrl+C to exit) ==="
echo ""

docker compose logs -f --tail=100
LOGSEOF

    # Backup script
    cat > "$INSTALL_DIR/backup.sh" <<'BACKUPEOF'
#!/bin/bash
BACKUP_DIR="$HOME/openclaw-backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/openclaw_backup_$TIMESTAMP.tar.gz"

mkdir -p "$BACKUP_DIR"

echo "Creating backup..."
echo "Stopping services temporarily..."
cd "$HOME/.oneclaw-secure"
./stop.sh > /dev/null 2>&1

echo "Backing up configuration, workspace, and secrets..."
tar -czf "$BACKUP_FILE" \
    -C "$HOME/.oneclaw-secure" \
    config workspace secrets \
    2>/dev/null

echo "Restarting services..."
./start.sh > /dev/null 2>&1

echo ""
echo "✓ Backup created: $BACKUP_FILE"
echo "  Size: $(du -h "$BACKUP_FILE" | cut -f1)"
echo ""
echo "Restore with:"
echo "  tar -xzf $BACKUP_FILE -C $HOME/.oneclaw-secure"
BACKUPEOF

    # Make all scripts executable
    chmod +x "$INSTALL_DIR"/{start,stop,status,logs,backup}.sh

    print_success "Management scripts created"
    echo ""
}

# Function: Build Docker image securely
build_docker_image() {
    print_step "9/10" "Building OpenClaw Docker image (secure build)..."
    echo ""
    echo "This process:"
    echo "  1. Clones OpenClaw source INSIDE the container"
    echo "  2. Builds everything IN the container"
    echo "  3. Creates final image with only runtime artifacts"
    echo "  4. Source code NEVER touches your host system"
    echo ""
    echo "This may take 5-15 minutes on first run..."
    echo ""

    cd "$INSTALL_DIR"

    # Build the image
    if docker build -t oneclaw-secure:latest -f Dockerfile . ; then
        print_success "Docker image built successfully"
        print_success "Image: oneclaw-secure:latest"
        echo ""
        echo "Security notes:"
        echo "  ✓ Source code never touched host filesystem"
        echo "  ✓ Build artifacts isolated in container"
        echo "  ✓ Final image is minimal and hardened"
    else
        print_error "Docker build failed"
        echo ""
        echo "Troubleshooting:"
        echo "  1. Check Docker is running: docker ps"
        echo "  2. Check disk space: df -h"
        echo "  3. Check logs above for errors"
        echo "  4. Ensure internet connectivity"
        exit 1
    fi

    echo ""
}

# Function: Display next steps
display_next_steps() {
    print_step "10/10" "Setup complete!"
    echo ""

    echo -e "${GREEN}"
    echo "╔════════════════════════════════════════════════════════════╗"
    echo "║  Installation Complete!                                    ║"
    echo "╚════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
    echo ""

    echo -e "${YELLOW}IMPORTANT: Complete these steps before starting OpenClaw:${NC}"
    echo ""

    echo "1. Add your API keys to:"
    echo "   $SECRETS_FILE"
    echo "   Required: ANTHROPIC_API_KEY or OPENAI_API_KEY"
    echo ""

    echo "2. Run the account setup wizard:"
    echo "   $INSTALL_DIR/setup-accounts.sh"
    echo "   (Creates accounts for: Gmail, Apple ID, Telegram, PayPal)"
    echo ""

    echo "3. Install BlueBubbles for iMessage (if using):"
    echo "   brew install --cask bluebubbles"
    echo "   Configure at: http://localhost:3000"
    echo ""

    echo "4. Configure application firewall (recommended):"
    echo "   Install Little Snitch: brew install --cask littlesnitch"
    echo "   Or Lulu (free): brew install --cask lulu"
    echo "   Block com.docker.vpnkit from accessing LAN"
    echo ""

    echo -e "${GREEN}When ready, start OpenClaw:${NC}"
    echo "   cd $INSTALL_DIR"
    echo "   ./start.sh"
    echo ""

    echo "Management commands:"
    echo "   Start:   ./start.sh"
    echo "   Stop:    ./stop.sh"
    echo "   Status:  ./status.sh"
    echo "   Logs:    ./logs.sh"
    echo "   Backup:  ./backup.sh"
    echo ""

    echo "Access points (after starting):"
    echo "   Gateway API: http://localhost:18789"
    echo "   WebChat UI:  http://localhost:18790"
    echo "   Bridge API:  http://localhost:8765"
    echo ""

    echo "Documentation:"
    echo "   OpenClaw Docs: https://docs.oneclaw.ai"
    echo "   GitHub: https://github.com/openclaw/openclaw"
    echo "   Your README: $INSTALL_DIR/README.md"
    echo ""

    echo -e "${BLUE}Project: One Claw Tied Behind Your Back${NC}"
    echo "Deployment directory: $INSTALL_DIR"
    echo ""
}

# Main execution
main() {
    check_prerequisites
    setup_directories
    generate_secrets
    create_config
    create_docker_compose
    create_macos_bridge
    configure_firewall
    create_management_scripts
    build_docker_image
    display_next_steps
}

# Run main function
main
