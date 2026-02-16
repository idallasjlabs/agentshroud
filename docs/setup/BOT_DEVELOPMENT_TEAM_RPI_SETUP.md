# SecureClaw Dev Environment — Raspberry Pi 4 (8GB) Setup Checklist

# SecureClaw Dev Environment — Raspberry Pi 4 (8GB) Setup Checklist

## Current System Profile

| Spec | Value |
|------|-------|
| Device | Raspberry Pi 4 Model B |
| RAM | 8GB |
| OS | Debian 11 (Bullseye) |
| Storage | 115GB (75GB free) |
| Hostname | raspberrypi.tail240ea8.ts.net |
| Primary User | idallasj |
| Bot User | secureclaw-bot |
| Network | Tailscale |

---

## Phase 1: OS Hardening & Cleanup

### SSH Hardening

- [ ] Disable password authentication (key-only)

```bash
sudo nano /etc/ssh/sshd_config
# Set:
# PasswordAuthentication no
# PermitRootLogin no
# PubkeyAuthentication yes
sudo systemctl restart sshd
```

- [ ] Create dedicated bot user with limited permissions

```bash
# SSH into the Pi
ssh idallasj@raspberrypi.tail240ea8.ts.net

# Create bot user
sudo useradd -m -s /bin/bash secureclaw-bot
sudo mkdir -p /home/secureclaw-bot/.ssh
# Add the bot's public key:
sudo nano /home/secureclaw-bot/.ssh/authorized_keys
sudo chown -R secureclaw-bot:secureclaw-bot /home/secureclaw-bot/.ssh
sudo chmod 700 /home/secureclaw-bot/.ssh
sudo chmod 600 /home/secureclaw-bot/.ssh/authorized_keys
```

- [ ] Restrict SSH access to Tailscale interface only

```bash
sudo nano /etc/ssh/sshd_config
# Add:
# ListenAddress raspberrypi.tail240ea8.ts.net
sudo systemctl restart sshd
```

- [ ] Set up UFW firewall

```bash
sudo apt install ufw
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow in on tailscale0 to any port 22
sudo ufw enable
```

### Snap Cleanup (Free Resources)

- [ ] List and remove unused snaps

```bash
snap list
# Remove snaps you don't need (you have a LOT of loop mounts):
sudo snap remove cool-retro-term
sudo snap remove gnome-42-2204
sudo snap remove gtk-common-themes
sudo snap remove snap-store
# If you don't need snap at all:
sudo apt purge snapd
```

### System Updates

- [ ] Update current packages

```bash
sudo apt update && sudo apt upgrade -y
sudo apt autoremove -y
```

- [ ] (Optional) Upgrade to Debian 12 Bookworm for newer packages

```bash
# Only if you're comfortable with a major upgrade
# Back up first!
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak
sudo sed -i 's/bullseye/bookworm/g' /etc/apt/sources.list
sudo apt update && sudo apt full-upgrade -y
```

---

## Phase 2: Development Tools

### Node.js (for OpenClaw & SecureClaw)

- [ ] Install Node.js 20 LTS via NodeSource

```bash
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo bash -
sudo apt install -y nodejs
node --version  # Should be 20.x
npm --version
```

### Docker & Docker Compose

- [ ] Install Docker

```bash
curl -fsSL https://get.docker.com | sh
sudo usermod -aG docker secureclaw-bot
sudo usermod -aG docker $USER
sudo systemctl enable docker
sudo systemctl start docker
```

- [ ] Install Docker Compose

```bash
sudo apt install -y docker-compose-plugin
docker compose version
```

- [ ] Verify Docker works

```bash
docker run --rm hello-world
```

### Git Configuration

- [ ] Install latest Git

```bash
sudo apt install -y git
git --version
```

- [ ] Configure bot user's Git identity

```bash
sudo -u secureclaw-bot git config --global user.name "secureclaw-bot"
sudo -u secureclaw-bot git config --global user.email "secureclaw-bot@users.noreply.github.com"
sudo -u secureclaw-bot git config --global init.defaultBranch main
```

### Python (for testing tools)

- [ ] Install Python 3 and pip

```bash
sudo apt install -y python3 python3-pip python3-venv
```

### Additional Dev Tools

- [ ] Install essential build tools

```bash
sudo apt install -y build-essential curl wget jq tree htop tmux
```

---

## Phase 3: GitHub Setup

### Bot Account (You Do This Manually)

- [ ] Create GitHub account (e.g., `secureclaw-bot`)
- [ ] Save credentials in 1Password
- [ ] Generate Personal Access Token (PAT) with scopes:
  - `repo` (full repo access)
  - `workflow` (GitHub Actions)
  - `write:packages` (if publishing containers)
- [ ] Store PAT in 1Password vault

### Repo Access

- [ ] Add `secureclaw-bot` as collaborator on SecureClaw repo (Write permission)
- [ ] Configure branch protection on `main`:
  - Require PR reviews
  - Require status checks to pass
  - No direct pushes

### Clone Repo on Pi

- [ ] Set up Git credentials for bot user

```bash
sudo -u secureclaw-bot bash
mkdir -p ~/projects
cd ~/projects

# Store token securely (use 1Password CLI or credential helper)
git config --global credential.helper store
# Or better — use SSH key:
ssh-keygen -t ed25519 -C "secureclaw-bot@raspberrypi.tail240ea8.ts.net"
cat ~/.ssh/id_ed25519.pub
# Add this key to the bot's GitHub account → Settings → SSH Keys

git clone git@github.com:<your-username>/secureclaw.git
cd secureclaw
```

---

## Phase 4: Project Structure

- [ ] Initialize SecureClaw repo structure

```
secureclaw/
├── .github/
│   └── workflows/
│       ├── ci.yml              # Run tests on every PR
│       ├── deploy.yml          # Build & deploy Docker image
│       └── docs-check.yml      # Verify docs updated with code
├── docs/
│   ├── ARCHITECTURE.md
│   ├── SETUP.md
│   ├── API.md
│   ├── CONTRIBUTING.md
│   ├── CHANGELOG.md
│   ├── SECURITY.md
│   └── ROADMAP.md
├── src/
│   ├── proxy/                  # Proxy layer core
│   ├── auth/                   # Authentication module
│   ├── rules/                  # Security rules engine
│   └── index.ts
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── docker/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── docker-compose.dev.yml
│   └── entrypoint.sh           # gosu privilege drop
├── scripts/
│   ├── setup.sh
│   ├── test.sh
│   └── deploy.sh
├── .env.example
├── .gitignore
├── package.json
├── tsconfig.json
├── jest.config.ts
├── README.md
└── LICENSE
```

---

## Phase 5: CI/CD Pipeline (GitHub Actions)

- [ ] Create `.github/workflows/ci.yml`

```yaml
name: CI
on:
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: npm ci
      - run: npm run lint
      - run: npm run test -- --coverage
      - name: Check coverage threshold
        run: |
          COVERAGE=$(cat coverage/coverage-summary.json | jq '.total.lines.pct')
          if (( $(echo "$COVERAGE < 80" | bc -l) )); then
            echo "Coverage $COVERAGE% is below 80% threshold"
            exit 1
          fi
```

---

## Phase 6: Docker Configuration

- [ ] Create Dockerfile with gosu and security hardening

```dockerfile
FROM node:20-slim

# Install gosu for privilege dropping
RUN apt-get update && apt-get install -y --no-install-recommends \
    gosu \
    && rm -rf /var/lib/apt/lists/* \
    && gosu nobody true

# Create non-root user
RUN groupadd -r openclaw && useradd -r -g openclaw openclaw

WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .

# Health check
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD curl -f http://localhost:3000/health || exit 1

COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["node", "dist/index.js"]
```

- [ ] Create `docker/entrypoint.sh`

```bash
#!/bin/bash
set -e

# Run setup as root
chown -R openclaw:openclaw /app/data

# Drop privileges and exec
exec gosu openclaw "$@"
```

---

## Phase 7: Secret Management

- [ ] Install 1Password CLI on the Pi

```bash
# For arm64:
curl -sS https://downloads.1password.com/linux/keys/1password.asc | \
  sudo gpg --dearmor --output /usr/share/keyrings/1password-archive-keyring.gpg
echo "deb [arch=arm64 signed-by=/usr/share/keyrings/1password-archive-keyring.gpg] \
  https://downloads.1password.com/linux/debian/arm64 stable main" | \
  sudo tee /etc/apt/sources.list.d/1password.list
sudo apt update && sudo apt install -y 1password-cli
```

- [ ] Create `.env.template` with 1Password references

```bash
GITHUB_TOKEN=op://SecureClaw/GitHub-Bot-PAT/password
ANTHROPIC_API_KEY=op://SecureClaw/Anthropic-API/password
TELEGRAM_BOT_TOKEN=op://SecureClaw/Telegram-Bot/password
```

- [ ] Run services with secrets injected

```bash
op run --env-file=.env.template -- docker compose up
```

---

## Phase 8: Monitoring & Observability

- [ ] Add to existing Zabbix monitoring (you already have 200+ sites)
- [ ] Monitor:
  - CPU / RAM / Disk / Temperature (Pi-specific)
  - Docker container health
  - Git operations (push/pull success rate)
  - Test pass/fail rates
- [ ] Set up structured logging in SecureClaw

```bash
# Check Pi temperature (important for sustained workloads)
vcgencmd measure_temp
```

- [ ] Create a cron job for Pi temperature monitoring

```bash
# Add to crontab:
*/5 * * * * echo "$(date): $(vcgencmd measure_temp)" >> /var/log/pi-temp.log
```

---

## Phase 9: OpenClaw Agent Configuration

- [ ] Install OpenClaw on your primary machine (Mac)
- [ ] Configure SSH tool for Pi access: `secureclaw-bot@raspberrypi.tail240ea8.ts.net`
- [ ] Configure GitHub MCP server
- [ ] Configure Telegram bot for notifications
- [ ] Set Claude as AI model via Anthropic API key
- [ ] Configure development plan as agent skills/tasks

---

## Phase 10: Validation Checklist

Run these checks before starting development:

```bash
# On the Pi, as secureclaw-bot user:
node --version          # 20.x
npm --version           # 10.x
docker --version        # 24.x+
docker compose version  # 2.x
git --version           # 2.30+
python3 --version       # 3.9+
op --version            # 2.x

# Connectivity
ssh secureclaw-bot@raspberrypi.tail240ea8.ts.net "echo 'SSH OK'"
curl -s https://api.github.com/rate_limit | jq '.rate.remaining'

# Docker
docker run --rm hello-world

# Disk space
df -h /  # Should have 70GB+ free

# Temperature
vcgencmd measure_temp   # Should be under 70°C
```

---

## Cost Estimate

| Item | Cost |
|------|------|
| Raspberry Pi 4 8GB | Already owned |
| Anthropic API | ~$5-20/month depending on agent activity |
| 1Password | Existing plan |
| GitHub | Free (public repo) or existing plan |
| Tailscale | Free tier |
| Telegram Bot | Free |
| **Total incremental** | **~$5-20/month** |

---

## Important Notes

- **Throttle the agent**: The Pi's ARM CPU is slower than x86 for builds. Set reasonable timeouts.
- **Swap file**: Add a 4GB swap file as a safety net for memory-heavy test suites.

```bash
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

- **Backups**: Since this is your dev server, set up automated git push as implicit backup. The code lives on GitHub.
- **Pi temperature**: Under sustained load, consider a fan or heatsink. The Pi 4 throttles at 80°C.

--- OLD SETUP


**Last Updated:** 2026-02-16
**Target Device:** Raspberry Pi 4 Model B (8GB)
**Purpose:** Autonomous Bot Development Team execution environment

---

## Current System Profile

| Spec | Value |
|------|-------|
| Device | Raspberry Pi 4 Model B |
| RAM | 8GB |
| OS | Debian 11 (Bullseye) |
| Storage | 115GB (75GB free) |
| Network | Tailscale (existing) |
| Existing Services | 200+ Zabbix monitored sites |

---

## Phase 1: OS Hardening & Cleanup

### SSH Hardening

- [ ] **Disable password authentication (key-only)**

```bash
sudo nano /etc/ssh/sshd_config
# Set:
# PasswordAuthentication no
# PermitRootLogin no
# PubkeyAuthentication yes
sudo systemctl restart sshd
```

- [ ] **Create dedicated bot user with limited permissions**

```bash
sudo useradd -m -s /bin/bash secureclaw-bot
sudo mkdir -p /home/secureclaw-bot/.ssh

# Add the bot's public key:
sudo nano /home/secureclaw-bot/.ssh/authorized_keys
# Paste your public key here

sudo chown -R secureclaw-bot:secureclaw-bot /home/secureclaw-bot/.ssh
sudo chmod 700 /home/secureclaw-bot/.ssh
sudo chmod 600 /home/secureclaw-bot/.ssh/authorized_keys
```

- [ ] **Restrict SSH access to Tailscale interface only**

```bash
# First, get your Tailscale IP:
tailscale ip -4

sudo nano /etc/ssh/sshd_config
# Add:
# ListenAddress <your-tailscale-ip>
# Example: ListenAddress 100.64.x.x

sudo systemctl restart sshd

# Test SSH over Tailscale before closing current session!
# From another terminal:
ssh secureclaw-bot@<tailscale-ip>
```

- [ ] **Set up UFW firewall**

```bash
sudo apt install -y ufw

# Default policies
sudo ufw default deny incoming
sudo ufw default allow outgoing

# Allow SSH only on Tailscale interface
sudo ufw allow in on tailscale0 to any port 22

# Allow Docker (if needed externally)
sudo ufw allow in on tailscale0 to any port 8080

# Enable firewall
sudo ufw enable
sudo ufw status verbose
```

### Snap Cleanup (Free Resources)

- [ ] **List and remove unused snaps**

```bash
snap list

# Remove snaps you don't need (you have many loop mounts):
sudo snap remove cool-retro-term
sudo snap remove gnome-42-2204
sudo snap remove gtk-common-themes
sudo snap remove snap-store

# If you don't need snap at all (saves ~500MB RAM):
sudo apt purge snapd
sudo apt autoremove -y

# Verify reduced loop devices:
df -h | grep loop
```

### System Updates

- [ ] **Update current packages**

```bash
sudo apt update && sudo apt upgrade -y
sudo apt autoremove -y
sudo apt autoclean
```

- [ ] **(Optional) Upgrade to Debian 12 Bookworm for newer packages**

```bash
# Only if you're comfortable with a major upgrade
# BACKUP FIRST!

# Check current version
cat /etc/debian_version  # Should show 11.x

# Backup sources list
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bullseye.bak

# Update to Bookworm
sudo sed -i 's/bullseye/bookworm/g' /etc/apt/sources.list
sudo apt update
sudo apt full-upgrade -y

# Reboot
sudo reboot

# After reboot, verify:
cat /etc/debian_version  # Should show 12.x
```

---

## Phase 2: Development Tools

### Node.js (for OpenClaw & SecureClaw)

- [ ] **Install Node.js 20 LTS via NodeSource**

```bash
# Remove old Node.js if present
sudo apt remove -y nodejs npm

# Install Node.js 20 LTS
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo bash -
sudo apt install -y nodejs

# Verify installation
node --version   # Should be v20.x.x
npm --version    # Should be 10.x.x

# Install global utilities
sudo npm install -g npm@latest
sudo npm install -g typescript ts-node nodemon
```

### Docker & Docker Compose

- [ ] **Install Docker**

```bash
# Install Docker
curl -fsSL https://get.docker.com | sh

# Add users to docker group
sudo usermod -aG docker secureclaw-bot
sudo usermod -aG docker $USER

# Enable Docker service
sudo systemctl enable docker
sudo systemctl start docker

# IMPORTANT: Log out and back in for group changes to take effect
```

- [ ] **Install Docker Compose**

```bash
# Install Docker Compose plugin
sudo apt install -y docker-compose-plugin

# Verify installation
docker compose version  # Should be v2.x.x
```

- [ ] **Verify Docker works**

```bash
# Test as current user
docker run --rm hello-world

# Test as bot user
sudo -u secureclaw-bot docker run --rm hello-world

# Check Docker info
docker info | grep "Storage Driver"
docker info | grep "Cgroup Driver"
```

- [ ] **Optimize Docker for Raspberry Pi**

```bash
# Create daemon.json for optimization
sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json > /dev/null <<EOF
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  },
  "storage-driver": "overlay2",
  "userland-proxy": false
}
EOF

sudo systemctl restart docker
```

### Git Configuration

- [ ] **Install latest Git**

```bash
sudo apt install -y git

# Verify version
git --version  # Should be 2.30+ (2.39+ on Bookworm)
```

- [ ] **Configure bot user's Git identity**

```bash
sudo -u secureclaw-bot git config --global user.name "secureclaw-bot"
sudo -u secureclaw-bot git config --global user.email "secureclaw-bot@users.noreply.github.com"
sudo -u secureclaw-bot git config --global init.defaultBranch main
sudo -u secureclaw-bot git config --global pull.rebase false
sudo -u secureclaw-bot git config --global core.editor "nano"
```

### Python (for testing tools)

- [ ] **Install Python 3 and pip**

```bash
sudo apt install -y python3 python3-pip python3-venv python3-dev

# Verify installation
python3 --version  # Should be 3.9+ (3.11+ on Bookworm)
pip3 --version

# Install common testing tools
pip3 install --user pytest black pylint mypy
```

### Additional Dev Tools

- [ ] **Install essential build tools**

```bash
sudo apt install -y \
  build-essential \
  curl \
  wget \
  jq \
  tree \
  htop \
  tmux \
  vim \
  ripgrep \
  fd-find \
  ncdu

# For monitoring Pi temperature
sudo apt install -y libraspberrypi-bin
```

---

## Phase 3: GitHub Setup

### Bot Account (Manual Setup Required)

- [ ] **Create GitHub account**
  - Username: `secureclaw-bot` (or your preferred name)
  - Email: Create dedicated email for bot
  - Enable 2FA

- [ ] **Save credentials in 1Password**
  - Vault: SecureClaw
  - Item: "GitHub Bot Account"
  - Include: username, password, 2FA recovery codes

- [ ] **Generate Personal Access Token (PAT)**
  1. Go to: https://github.com/settings/tokens
  2. Click "Generate new token (classic)"
  3. Name: "SecureClaw Bot Development"
  4. Scopes:
     - `repo` (full repo access)
     - `workflow` (GitHub Actions)
     - `write:packages` (if publishing containers)
  5. Generate and copy token
  6. Store in 1Password: "GitHub Bot PAT"

### Repo Access

- [ ] **Add `secureclaw-bot` as collaborator**
  1. Go to repo: Settings → Collaborators
  2. Add `secureclaw-bot` with **Write** permission
  3. Bot account accepts invitation

- [ ] **Configure branch protection on `main`**
  1. Settings → Branches → Add rule
  2. Branch name pattern: `main`
  3. Enable:
     - ✓ Require pull request reviews before merging
     - ✓ Require status checks to pass before merging
     - ✓ Require branches to be up to date before merging
     - ✓ Include administrators
  4. Save changes

### Clone Repo on Pi

- [ ] **Set up SSH key for bot user**

```bash
# Switch to bot user
sudo -u secureclaw-bot bash

# Generate SSH key
ssh-keygen -t ed25519 -C "secureclaw-bot@github" -f ~/.ssh/id_ed25519_github
# Press Enter for no passphrase (bot needs unattended access)

# Display public key
cat ~/.ssh/id_ed25519_github.pub
# Copy this key

# Configure SSH
cat >> ~/.ssh/config <<EOF
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_github
  IdentitiesOnly yes
EOF

chmod 600 ~/.ssh/config
```

- [ ] **Add SSH key to GitHub bot account**
  1. Log in as bot account
  2. Go to: Settings → SSH and GPG keys
  3. Click "New SSH key"
  4. Title: "Raspberry Pi 4 - SecureClaw Dev"
  5. Paste public key
  6. Add key

- [ ] **Clone SecureClaw repository**

```bash
# Still as secureclaw-bot user
mkdir -p ~/projects
cd ~/projects

# Test SSH connection
ssh -T git@github.com
# Should see: "Hi secureclaw-bot! You've successfully authenticated..."

# Clone repo
git clone git@github.com:<your-username>/oneclaw.git secureclaw
cd secureclaw

# Verify
git remote -v
git status
```

---

## Phase 4: Project Structure

- [ ] **Initialize SecureClaw repo structure**

```bash
cd ~/projects/secureclaw

# Create directory structure
mkdir -p .github/workflows
mkdir -p docs
mkdir -p src/{proxy,auth,rules}
mkdir -p tests/{unit,integration,e2e}
mkdir -p docker
mkdir -p scripts

# Create placeholder files
touch .github/workflows/{ci.yml,deploy.yml,docs-check.yml}
touch docs/{ARCHITECTURE.md,SETUP.md,API.md,CONTRIBUTING.md,CHANGELOG.md,SECURITY.md,ROADMAP.md}
touch src/index.ts
touch docker/{Dockerfile,docker-compose.yml,docker-compose.dev.yml,entrypoint.sh}
touch scripts/{setup.sh,test.sh,deploy.sh}
touch {.env.example,.gitignore,package.json,tsconfig.json,jest.config.ts}

# Make scripts executable
chmod +x docker/entrypoint.sh
chmod +x scripts/*.sh
```

**Recommended structure:**
```
secureclaw/
├── .github/
│   └── workflows/
│       ├── ci.yml              # Run tests on every PR
│       ├── deploy.yml          # Build & deploy Docker image
│       └── docs-check.yml      # Verify docs updated with code
├── docs/
│   ├── ARCHITECTURE.md         # System design
│   ├── SETUP.md                # Installation guide
│   ├── API.md                  # API documentation
│   ├── CONTRIBUTING.md         # Contribution guidelines
│   ├── CHANGELOG.md            # Version history
│   ├── SECURITY.md             # Security policy
│   └── ROADMAP.md              # Future plans
├── src/
│   ├── proxy/                  # Proxy layer core
│   ├── auth/                   # Authentication module
│   ├── rules/                  # Security rules engine
│   └── index.ts                # Application entry point
├── tests/
│   ├── unit/                   # Unit tests
│   ├── integration/            # Integration tests
│   └── e2e/                    # End-to-end tests
├── docker/
│   ├── Dockerfile              # Production container
│   ├── docker-compose.yml      # Production compose
│   ├── docker-compose.dev.yml  # Development compose
│   └── entrypoint.sh           # gosu privilege drop
├── scripts/
│   ├── setup.sh                # Environment setup
│   ├── test.sh                 # Test runner
│   └── deploy.sh               # Deployment script
├── .env.example                # Environment template
├── .gitignore                  # Git ignore rules
├── package.json                # Node.js dependencies
├── tsconfig.json               # TypeScript config
├── jest.config.ts              # Jest test config
├── README.md                   # Project overview
└── LICENSE                     # License file
```

---

## Phase 5: CI/CD Pipeline (GitHub Actions)

- [ ] **Create `.github/workflows/ci.yml`**

```yaml
name: CI

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [20.x]

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
          cache: 'npm'

      - name: Install dependencies
        run: npm ci

      - name: Run linter
        run: npm run lint

      - name: Run type check
        run: npm run type-check

      - name: Run tests with coverage
        run: npm run test -- --coverage

      - name: Check coverage threshold
        run: |
          COVERAGE=$(cat coverage/coverage-summary.json | jq '.total.lines.pct')
          echo "Coverage: $COVERAGE%"
          if (( $(echo "$COVERAGE < 80" | bc -l) )); then
            echo "❌ Coverage $COVERAGE% is below 80% threshold"
            exit 1
          fi
          echo "✅ Coverage threshold met"

      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage/coverage-final.json
          flags: unittests
          name: codecov-umbrella

  build:
    runs-on: ubuntu-latest
    needs: test

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20.x

      - name: Install dependencies
        run: npm ci

      - name: Build
        run: npm run build

      - name: Test Docker build
        run: docker build -t secureclaw:test .
```

- [ ] **Create `.github/workflows/deploy.yml`**

```yaml
name: Deploy

on:
  push:
    branches: [main]
    tags:
      - 'v*'

jobs:
  deploy:
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v3

      - name: Login to GitHub Container Registry
        uses: docker/login-action@v3
        with:
          registry: ghcr.io
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}

      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ghcr.io/${{ github.repository }}
          tags: |
            type=ref,event=branch
            type=ref,event=pr
            type=semver,pattern={{version}}
            type=semver,pattern={{major}}.{{minor}}

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          platforms: linux/amd64,linux/arm64
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
          cache-from: type=gha
          cache-to: type=gha,mode=max
```

---

## Phase 6: Docker Configuration

- [ ] **Create `docker/Dockerfile` with gosu and security hardening**

```dockerfile
FROM node:20-slim

# Install gosu for privilege dropping
RUN apt-get update && apt-get install -y --no-install-recommends \
    gosu \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && gosu nobody true

# Create non-root user
RUN groupadd -r secureclaw && useradd -r -g secureclaw secureclaw

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy application code
COPY . .

# Build TypeScript (if needed)
RUN npm run build || true

# Create data directory
RUN mkdir -p /app/data && chown secureclaw:secureclaw /app/data

# Health check
HEALTHCHECK --interval=30s --timeout=5s --retries=3 --start-period=10s \
  CMD curl -f http://localhost:3000/health || exit 1

# Copy entrypoint script
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Security hardening
RUN rm -rf /tmp/* /var/tmp/* /root/.npm /root/.cache

# Switch to non-root user context (will be enforced by entrypoint)
USER secureclaw

EXPOSE 3000

ENTRYPOINT ["/entrypoint.sh"]
CMD ["node", "dist/index.js"]
```

- [ ] **Create `docker/entrypoint.sh`**

```bash
#!/bin/bash
set -e

# If running as root, drop privileges
if [ "$(id -u)" = "0" ]; then
    echo "[entrypoint] Running as root, dropping privileges to secureclaw user"

    # Ensure data directory has correct ownership
    chown -R secureclaw:secureclaw /app/data 2>/dev/null || true

    # Execute command as secureclaw user
    exec gosu secureclaw "$@"
else
    # Already running as non-root, execute directly
    echo "[entrypoint] Running as user $(whoami)"
    exec "$@"
fi
```

- [ ] **Create `docker/docker-compose.yml`**

```yaml
version: '3.8'

services:
  secureclaw:
    build:
      context: ..
      dockerfile: docker/Dockerfile
    container_name: secureclaw
    restart: unless-stopped

    ports:
      - "127.0.0.1:3000:3000"  # Localhost only

    volumes:
      - secureclaw-data:/app/data

    environment:
      - NODE_ENV=production
      - LOG_LEVEL=info

    security_opt:
      - no-new-privileges:true

    cap_drop:
      - ALL

    read_only: true

    tmpfs:
      - /tmp:noexec,nosuid,size=100m

    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 30s

    mem_limit: 2g
    memswap_limit: 2g
    cpus: 2.0
    pids_limit: 100

volumes:
  secureclaw-data:
    driver: local
```

---

## Phase 7: Secret Management

- [ ] **Install 1Password CLI on the Pi**

```bash
# For ARM64 (Raspberry Pi 4)
curl -sS https://downloads.1password.com/linux/keys/1password.asc | \
  sudo gpg --dearmor --output /usr/share/keyrings/1password-archive-keyring.gpg

echo "deb [arch=arm64 signed-by=/usr/share/keyrings/1password-archive-keyring.gpg] \
  https://downloads.1password.com/linux/debian/arm64 stable main" | \
  sudo tee /etc/apt/sources.list.d/1password.list

sudo apt update && sudo apt install -y 1password-cli

# Verify installation
op --version
```

- [ ] **Sign in to 1Password**

```bash
# Sign in to your account
op signin

# Or with service account token
export OP_SERVICE_ACCOUNT_TOKEN="your-service-account-token"

# Test access
op vault list
```

- [ ] **Create `.env.example` template**

```bash
# SecureClaw Environment Variables
# Copy to .env and fill in values

# GitHub
GITHUB_TOKEN=your-github-pat-here
GITHUB_REPO=username/secureclaw

# Anthropic API
ANTHROPIC_API_KEY=sk-ant-api03-...

# Telegram Bot
TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHI...

# Database
DATABASE_URL=sqlite:///app/data/secureclaw.db

# Logging
LOG_LEVEL=info

# Feature Flags
ENABLE_TELEGRAM=true
ENABLE_GITHUB_INTEGRATION=true
```

- [ ] **Create `.env.template` with 1Password references**

```bash
# SecureClaw Environment Variables (1Password)
# Run with: op run --env-file=.env.template -- <command>

GITHUB_TOKEN=op://SecureClaw/GitHub-Bot-PAT/password
ANTHROPIC_API_KEY=op://SecureClaw/Anthropic-API/password
TELEGRAM_BOT_TOKEN=op://SecureClaw/Telegram-Bot/password
DATABASE_URL=sqlite:///app/data/secureclaw.db
LOG_LEVEL=info
ENABLE_TELEGRAM=true
ENABLE_GITHUB_INTEGRATION=true
```

- [ ] **Run services with secrets injected**

```bash
# Using 1Password CLI
op run --env-file=.env.template -- docker compose up -d

# Or create Docker secrets
op read "op://SecureClaw/GitHub-Bot-PAT/password" > docker/secrets/github_token.txt
op read "op://SecureClaw/Anthropic-API/password" > docker/secrets/anthropic_api_key.txt
op read "op://SecureClaw/Telegram-Bot/password" > docker/secrets/telegram_bot_token.txt
```

---

## Phase 8: Monitoring & Observability

- [ ] **Add to existing Zabbix monitoring**
  1. Create new host: "Raspberry Pi 4 - SecureClaw Dev"
  2. Add templates:
     - Linux by Zabbix agent
     - Docker by Zabbix agent 2
     - Custom: Raspberry Pi Temperature

- [ ] **Monitor key metrics:**
  - CPU usage (%)
  - RAM usage (%)
  - Disk usage (%)
  - Temperature (°C)
  - Docker container health
  - Git operations (push/pull success rate)
  - Test pass/fail rates
  - GitHub API rate limit

- [ ] **Set up structured logging in SecureClaw**

Create `src/logger.ts`:
```typescript
import winston from 'winston';

export const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.errors({ stack: true }),
    winston.format.json()
  ),
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({
      filename: '/app/data/logs/error.log',
      level: 'error'
    }),
    new winston.transports.File({
      filename: '/app/data/logs/combined.log'
    })
  ]
});
```

- [ ] **Create Pi temperature monitoring script**

```bash
# Create monitoring script
sudo tee /usr/local/bin/check-pi-temp.sh > /dev/null <<'EOF'
#!/bin/bash
TEMP=$(vcgencmd measure_temp | awk -F'=' '{print $2}' | awk -F"'" '{print $1}')
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
echo "$TIMESTAMP: $TEMP°C" >> /var/log/pi-temp.log

# Alert if over 75°C
if (( $(echo "$TEMP > 75" | bc -l) )); then
    echo "$TIMESTAMP: WARNING - Temperature $TEMP°C exceeds 75°C threshold" | \
        logger -t pi-temp-monitor
fi
EOF

sudo chmod +x /usr/local/bin/check-pi-temp.sh

# Add to crontab
(crontab -l 2>/dev/null; echo "*/5 * * * * /usr/local/bin/check-pi-temp.sh") | crontab -

# Create log rotation
sudo tee /etc/logrotate.d/pi-temp > /dev/null <<EOF
/var/log/pi-temp.log {
    weekly
    rotate 4
    compress
    missingok
    notifempty
}
EOF
```

- [ ] **Install monitoring tools**

```bash
# Install monitoring utilities
sudo apt install -y sysstat iotop iftop

# Enable sysstat
sudo systemctl enable sysstat
sudo systemctl start sysstat
```

---

## Phase 9: OpenClaw Agent Configuration

**On your primary machine (Mac):**

- [ ] **Install OpenClaw**

```bash
npm install -g openclaw@latest
openclaw --version
```

- [ ] **Initialize OpenClaw configuration**

```bash
openclaw init

# Configure:
# - Model: anthropic/claude-opus-4-6
# - Telegram: @therealidallasj_bot
# - Gateway: localhost:18789
```

- [ ] **Configure SSH tool for Pi access**

Add to OpenClaw config or skills:
```json
{
  "ssh_targets": {
    "pi-dev": {
      "host": "<tailscale-ip>",
      "user": "secureclaw-bot",
      "key": "~/.ssh/id_ed25519",
      "description": "Raspberry Pi 4 development server"
    }
  }
}
```

- [ ] **Configure GitHub MCP server**

```bash
# Install GitHub MCP server
npm install -g @modelcontextprotocol/server-github

# Configure in OpenClaw
openclaw mcp add github
```

- [ ] **Configure development workflow**

Create OpenClaw skill or system prompt:
```markdown
# Bot Development Team Workflow

You are part of an autonomous development team working on SecureClaw.

## Your Environment
- Development server: Raspberry Pi 4 (8GB) at <tailscale-ip>
- Repository: git@github.com:username/secureclaw.git
- CI/CD: GitHub Actions
- Communication: Telegram (@therealidallasj_bot)

## Workflow
1. Receive task from user via Telegram
2. SSH to pi-dev and pull latest code
3. Create feature branch
4. Implement changes with tests
5. Run test suite locally
6. Commit and push to GitHub
7. Open pull request
8. Respond to user with PR link
9. Monitor CI status
10. Merge when approved

## Commands Available
- ssh pi-dev "command"
- git operations via GitHub MCP
- docker compose commands
- npm scripts
```

---

## Phase 10: Validation Checklist

### System Verification

Run these checks before starting development:

```bash
# On the Pi, as secureclaw-bot user:

echo "=== Node.js ==="
node --version          # Expected: v20.x.x
npm --version           # Expected: 10.x.x

echo "=== Docker ==="
docker --version        # Expected: 24.x+
docker compose version  # Expected: v2.x
docker run --rm hello-world

echo "=== Git ==="
git --version           # Expected: 2.30+
git config user.name    # Expected: secureclaw-bot
git config user.email   # Expected: secureclaw-bot@...

echo "=== Python ==="
python3 --version       # Expected: 3.9+ (3.11+ on Bookworm)
pip3 --version

echo "=== 1Password ==="
op --version            # Expected: 2.x
op vault list           # Should list vaults

echo "=== System Resources ==="
free -h                 # RAM usage
df -h /                 # Disk space (should have 70GB+ free)
vcgencmd measure_temp   # Temperature (should be < 70°C)

echo "=== Network ==="
tailscale status        # Tailscale connection
tailscale ip -4         # Your Tailscale IP
ping -c 3 8.8.8.8       # Internet connectivity

echo "=== SSH ==="
ssh -T git@github.com   # GitHub SSH key
# Expected: "Hi secureclaw-bot! You've successfully authenticated..."

echo "=== Firewall ==="
sudo ufw status verbose # Should show SSH allowed on tailscale0
```

### GitHub Integration Test

```bash
# Clone test
cd ~/projects
rm -rf secureclaw-test
git clone git@github.com:<username>/secureclaw.git secureclaw-test
cd secureclaw-test

# Make test commit
git checkout -b test-setup
echo "# Test" >> TEST.md
git add TEST.md
git commit -m "test: setup verification"
git push origin test-setup

# Verify on GitHub web interface
# Clean up
git checkout main
git branch -D test-setup
git push origin --delete test-setup
cd ..
rm -rf secureclaw-test
```

### Docker Test

```bash
# Build test
cd ~/projects/secureclaw
docker build -f docker/Dockerfile -t secureclaw:test .

# Run test
docker run --rm secureclaw:test node --version

# Cleanup
docker rmi secureclaw:test
```

### Performance Test

```bash
# CPU stress test (2 minutes)
stress-ng --cpu 4 --timeout 120s --metrics-brief

# Temperature monitoring during stress
watch -n 1 'vcgencmd measure_temp'

# Expected: Should stay below 80°C under load
```

---

## Cost Estimate

| Item | Cost/Month | Notes |
|------|------------|-------|
| Raspberry Pi 4 8GB | $0 | Already owned |
| Anthropic API | $5-20 | Depends on agent activity |
| 1Password | $0 | Existing plan |
| GitHub | $0 | Free for public repos |
| Tailscale | $0 | Free tier |
| Telegram Bot | $0 | Always free |
| Electricity (Pi) | ~$2 | 15W × 24h × $0.15/kWh × 30 days |
| **Total** | **$7-22/month** | |

---

## Performance Considerations

### CPU Throttling
The Pi's ARM Cortex-A72 is slower than x86 for builds:
- Node.js build time: ~2-3x slower than x86
- Docker builds: ~2-3x slower
- **Recommendation:** Use multi-stage Docker builds, cache aggressively

### Memory Management
With 8GB RAM:
- Docker: Up to 4GB
- Node.js processes: Up to 2GB
- System: 2GB reserved
- **Recommendation:** Set memory limits on all containers

### Disk I/O
MicroSD card is slow:
- **Recommendation:** Consider USB 3.0 SSD for Docker volumes
- **Alternative:** Use overlay2 storage driver (already configured)

### Network
100 Mbps Ethernet:
- Sufficient for git operations
- May be slow for large Docker image pulls
- **Recommendation:** Pre-pull base images

### Temperature Management
Pi 4 throttles at 80°C:
- Add heatsink or fan if sustained load expected
- Monitor temperature with `/usr/local/bin/check-pi-temp.sh`
- **Critical:** Keep ambient temperature below 25°C

---

## Important Notes

### Add Swap File

```bash
# Create 4GB swap file as safety net
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# Make permanent
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

# Verify
free -h
swapon --show
```

### Backup Strategy

Since this is your dev server, use git as implicit backup:
- All code lives on GitHub
- Auto-push on successful builds
- Keep audit logs in separate volume
- Backup 1Password vault weekly

### Cooling Recommendations

For sustained loads:
- **Passive:** Official Pi 4 case with heatsink
- **Active:** Argon ONE M.2 case (adds M.2 SSD support)
- **Budget:** 5V fan connected to GPIO pins

### Power Supply

Use official Pi 4 power supply (5V/3A):
- Cheap supplies cause undervoltage
- Check with: `vcgencmd get_throttled`
- Output `0x0` = OK, anything else = problem

### Security Hardening Checklist

- [x] SSH key-only authentication
- [x] SSH restricted to Tailscale
- [x] UFW firewall enabled
- [x] Dedicated bot user with limited permissions
- [x] Docker with user namespaces (automatic with new setup)
- [x] No root containers
- [x] Docker secrets for sensitive data
- [ ] Fail2ban for SSH brute-force protection (optional)
- [ ] Automated security updates (optional)

### Optional: Automated Security Updates

```bash
sudo apt install -y unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## Troubleshooting

### SSH Connection Refused
```bash
# Check SSH service
sudo systemctl status sshd

# Check firewall
sudo ufw status verbose

# Verify Tailscale
tailscale status
```

### Docker Permission Denied
```bash
# Verify user in docker group
groups | grep docker

# If not, add and re-login
sudo usermod -aG docker $USER
# Log out and back in
```

### Out of Memory
```bash
# Check memory
free -h

# Check Docker container limits
docker stats

# Add swap if needed (see above)
```

### High Temperature
```bash
# Check current temperature
vcgencmd measure_temp

# Check throttling
vcgencmd get_throttled
# 0x0 = OK
# 0x50000 = throttling occurred

# Solutions:
# 1. Add heatsink/fan
# 2. Improve ventilation
# 3. Reduce container CPU limits
```

### Slow Builds
```bash
# Use build cache
docker build --cache-from=secureclaw:latest

# Multi-stage builds
# (Already in Dockerfile)

# Pre-pull base images
docker pull node:20-slim
```

---

## Next Steps After Setup

1. **Test bot development workflow:**
   ```bash
   # From your Mac:
   openclaw "SSH to the Pi and run 'git status' in the secureclaw repo"
   ```

2. **Create first feature:**
   ```bash
   openclaw "Create a new feature branch and implement basic health check endpoint"
   ```

3. **Verify CI/CD:**
   - Check GitHub Actions runs
   - Verify tests pass
   - Confirm coverage reports

4. **Monitor for 24 hours:**
   - Check temperature logs
   - Review Zabbix alerts
   - Verify no memory issues

5. **Document learnings:**
   - Add to ROADMAP.md
   - Update SETUP.md with Pi-specific notes

---

**Setup Complete!** 🎉

Your Raspberry Pi 4 is now ready to run the autonomous Bot Development Team for SecureClaw.

**Last Updated:** 2026-02-16
**Setup Guide Version:** 1.0
