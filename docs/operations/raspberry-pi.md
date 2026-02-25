# Deploying AgentShroud on Raspberry Pi (aarch64)

## Prerequisites

- **Hardware:** Raspberry Pi 4 (4 GB+ RAM recommended)
- **OS:** Raspberry Pi OS 64-bit (Bookworm) or Debian 11+
- **Software:** Docker, Docker Compose v2, Git
- **Network:** Internet access for pulling images and cloning the repo

## Fresh Install

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/agentshroud.git
cd agentshroud
```

### 2. Install Docker

```bash
sudo apt update && sudo apt install -y docker.io docker-compose-plugin
sudo usermod -aG docker "$USER"
newgrp docker
```

Verify Docker is working:

```bash
docker run --rm hello-world
```

### 3. Set Up Secrets

```bash
./docker/secrets/setup-secrets.sh
```

Follow the prompts to configure API keys and credentials.

### 4. Configure AgentShroud

Edit `agentshroud.yaml` with your desired settings:

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

You should see a JSON response confirming the gateway is running.

## Pi-Specific Notes

### ARM64 Builds

All Docker images are built natively on the Pi's ARM64 architecture. Initial builds may take 10–20 minutes depending on your SD card or SSD speed.

### Memory and Swap

The Pi 4 with 4 GB RAM can run AgentShroud, but we recommend configuring at least **2 GB of swap** to avoid OOM kills during Docker builds:

```bash
sudo dphys-swapfile swapoff
sudo sed -i 's/CONF_SWAPSIZE=.*/CONF_SWAPSIZE=2048/' /etc/dphys-swapfile
sudo dphys-swapfile setup
sudo dphys-swapfile swapon
```

Verify:

```bash
free -h
```

### seccomp on ARM64

Docker's default seccomp profile works on ARM64. If you use a custom seccomp profile (e.g., `docker/seccomp/`), ensure it includes ARM64-specific syscalls like `arm_fadvise64_64` and `arm_sync_file_range`.

## Updating to Latest Release

### From Git (tracking main)

```bash
cd ~/Development/agentshroud
git pull origin main
cd docker && docker compose build && docker compose up -d
```

### From a Tagged Release

```bash
cd ~/Development/agentshroud
git fetch --all --tags
git checkout v0.2.0
cd docker && docker compose build && docker compose up -d
```

## Tailscale Remote Access (Optional)

To access your Pi remotely over Tailscale:

```bash
curl -fsSL https://tailscale.com/install.sh | sh
sudo tailscale up
```

Your Pi will be reachable at its Tailscale hostname (e.g., `raspberrypi.tail240ea8.ts.net`). No port forwarding required.

## Troubleshooting

### Out-of-Memory (OOM) Kills

- Check `dmesg | grep -i oom` for OOM events.
- Increase swap (see above) or reduce concurrent build jobs.
- Consider `docker compose build --parallel 1` to limit parallelism.

### Slow Builds

- Use an SSD instead of an SD card — dramatically improves I/O.
- Pre-pull base images: `docker pull python:3.13-slim`
- Use Docker BuildKit: `DOCKER_BUILDKIT=1 docker compose build`

### Container Won't Start

```bash
docker compose logs -f          # check logs
docker compose ps               # check container status
docker compose down && docker compose up -d   # restart
```
