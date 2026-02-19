# Deploying AgentShroud on macOS (Apple Silicon / Intel)

## Prerequisites

- **OS:** macOS 12 (Monterey) or later
- **Architecture:** arm64 (Apple Silicon) or x86_64 (Intel)
- **Software:** [Docker Desktop](https://www.docker.com/products/docker-desktop/), Git
- **Optional:** [Homebrew](https://brew.sh/) for installing tools

## Fresh Install

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/oneclaw.git
cd oneclaw
```

### 2. Install Docker Desktop

Download and install from [docker.com](https://www.docker.com/products/docker-desktop/) or via Homebrew:

```bash
brew install --cask docker
```

Launch Docker Desktop and wait for it to be ready (whale icon in menu bar).

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

## Apple Silicon vs Intel

Docker Desktop handles architecture differences transparently. Images build natively on both arm64 and x86_64. No special configuration is needed — just build and run.

## Running Without Docker (Native Python)

For gateway development, you can run the gateway directly without Docker:

```bash
# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r gateway/requirements.txt

# Run the gateway
uvicorn gateway.ingest_api.main:app --host 127.0.0.1 --port 8080
```

This is useful for rapid iteration during development. For production use, Docker is recommended.

## Updating to Latest Release

```bash
cd ~/oneclaw
git fetch --all --tags
git checkout v<new-version>
cd docker && docker compose build && docker compose up -d
```

See [updating.md](./updating.md) for the full update guide, including rollback.

## Docker Desktop Resource Allocation

By default, Docker Desktop may limit CPU and memory. For best performance:

1. Open **Docker Desktop → Settings → Resources**
2. Allocate at least **4 GB RAM** and **2 CPUs**
3. Increase disk image size if builds fail with "no space left"

On Apple Silicon Macs with 8 GB+ unified memory, the defaults are usually fine.
