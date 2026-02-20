# Deploying AgentShroud on Linux (x86_64 / aarch64)

## Prerequisites

- **OS:** Ubuntu 22.04+, Debian 12+, or any modern Linux distribution
- **Architecture:** x86_64 or aarch64
- **Software:** Docker, Docker Compose v2, Git
- **Resources:** 4 GB+ RAM, 10 GB+ free disk space

## Fresh Install

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/agentshroud.git
cd agentshroud
```

### 2. Install Docker

**Ubuntu / Debian:**

```bash
sudo apt update && sudo apt install -y docker.io docker-compose-plugin
sudo usermod -aG docker "$USER"
newgrp docker
```

**Fedora / RHEL:**

```bash
sudo dnf install -y docker docker-compose-plugin
sudo systemctl enable --now docker
sudo usermod -aG docker "$USER"
newgrp docker
```

Verify:

```bash
docker run --rm hello-world
```

### 3. Set Up Secrets

```bash
./docker/secrets/setup-secrets.sh
```

### 4. Configure AgentShroud

```bash
cp agentshroud.yaml.example agentshroud.yaml   # if an example exists
nano agentshroud.yaml
```

### 5. Build and Start

```bash
cd docker
docker compose build
docker compose up -d
```

### 6. Verify

```bash
curl http://localhost:8080/status
```

## VPS Deployment Notes

### Non-Root User

Run AgentShroud as a non-root user with Docker group access:

```bash
sudo adduser agentshroud --disabled-password
sudo usermod -aG docker agentshroud
sudo su - agentshroud
```

### Firewall

Only expose the ports you need. For a private deployment behind Tailscale, you may not need to open any public ports:

```bash
# UFW example — allow SSH only
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw enable
```

If you need public HTTP access:

```bash
sudo ufw allow 8080/tcp
```

## Systemd Service for Auto-Start

Create `/etc/systemd/system/agentshroud.service`:

```ini
[Unit]
Description=AgentShroud Gateway
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
User=agentshroud
WorkingDirectory=/home/agentshroud/agentshroud/docker
ExecStart=/usr/bin/docker compose up -d
ExecStop=/usr/bin/docker compose down
TimeoutStartSec=120

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now agentshroud
```

## Updating to Latest Release

```bash
cd ~/agentshroud
git fetch --all --tags
git checkout v<new-version>
cd docker && docker compose build && docker compose up -d
```

See [updating.md](./updating.md) for the full update guide, including rollback.

## Architecture Notes

Docker images build natively on your host architecture. If you need multi-arch images (e.g., building on x86_64 for aarch64 deployment), use Docker Buildx:

```bash
docker buildx create --use
docker buildx build --platform linux/amd64,linux/arm64 -t agentshroud:latest .
```

For single-machine deployments, native builds are simpler and faster.
