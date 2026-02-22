# OpenClaw Bot SSH Configuration

**Date:** 2026-02-16
**Status:** ✅ SSH Key Generated and Configured

---

## SSH Key Generated

An SSH key has been generated inside the OpenClaw bot container for secure remote access.

### Public Key

**Add this public key to your Raspberry Pi and any other hosts the bot should access:**

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIE/kQadW0OjqtR7Ersmh+uutCIasXZ9HWUNUCNDEpHLO openclaw-bot@agentshroud.ai
```

---

## Setup Instructions

### Step 1: Add Public Key to Raspberry Pi

On your **Raspberry Pi**, run these commands:

```bash
# SSH into the Pi as idallasj (your primary user)
ssh idallasj@raspberrypi.tail240ea8.ts.net

# Create .ssh directory for agentshroud-bot if it doesn't exist
sudo mkdir -p /home/agentshroud-bot/.ssh

# Add the OpenClaw bot's public key
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIE/kQadW0OjqtR7Ersmh+uutCIasXZ9HWUNUCNDEpHLO openclaw-bot@agentshroud.ai" | \
    sudo tee -a /home/agentshroud-bot/.ssh/authorized_keys

# Set correct ownership and permissions
sudo chown -R agentshroud-bot:agentshroud-bot /home/agentshroud-bot/.ssh
sudo chmod 700 /home/agentshroud-bot/.ssh
sudo chmod 600 /home/agentshroud-bot/.ssh/authorized_keys

# Verify the key was added
sudo cat /home/agentshroud-bot/.ssh/authorized_keys
```

### Step 2: Test SSH Connection from OpenClaw Bot

From your **Mac** (where OpenClaw is running):

```bash
# Test SSH connection from the bot container
docker exec -u node openclaw-bot ssh -T pi-dev

# If successful, you should see a shell prompt or connection message
# First connection will ask to accept the host key - this is normal

# Alternative: Test with full command
docker exec -u node openclaw-bot ssh pi-dev "hostname && whoami"
# Expected output:
# raspberrypi
# agentshroud-bot
```

### Step 3: Verify from OpenClaw UI or Telegram

You can now ask the bot to SSH to the Pi:

**Telegram:**
```
SSH to pi-dev and run: git status
```

**Control UI:**
```
Can you SSH to raspberrypi and check the disk space with df -h?
```

---

## SSH Configuration Details

The bot has been configured with the following SSH settings:

### SSH Config File Location
`/home/node/.ssh/config` (inside container)

### Configured Hosts

#### Raspberry Pi (pi-dev)
```
Host pi-dev raspberrypi
    HostName raspberrypi.tail240ea8.ts.net
    User agentshroud-bot
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes
    StrictHostKeyChecking accept-new
    ServerAliveInterval 60
    ServerAliveCountMax 3
```

**Aliases:** `pi-dev`, `raspberrypi`
**User:** `agentshroud-bot`
**Hostname:** `raspberrypi.tail240ea8.ts.net`

### Default Settings (All Hosts)
```
Host *
    IdentityFile ~/.ssh/id_ed25519
    IdentitiesOnly yes
    StrictHostKeyChecking accept-new
    ServerAliveInterval 60
    ServerAliveCountMax 3
    AddKeysToAgent yes
```

---

## Adding Additional Hosts

To allow the bot to SSH to other machines:

### 1. Add Public Key to Target Host

On the **target machine**:

```bash
# Add the bot's public key to authorized_keys
mkdir -p ~/.ssh
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIE/kQadW0OjqtR7Ersmh+uutCIasXZ9HWUNUCNDEpHLO openclaw-bot@agentshroud.ai" >> ~/.ssh/authorized_keys
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
```

### 2. Add Host Configuration (Optional but Recommended)

On your **Mac**, add the host to the bot's SSH config:

```bash
docker exec -u node openclaw-bot bash -c 'cat >> /home/node/.ssh/config << "EOF"

# Custom Host
Host myserver
    HostName myserver.example.com
    User myusername
    IdentityFile ~/.ssh/id_ed25519
    Port 22
EOF'
```

### 3. Test Connection

```bash
docker exec -u node openclaw-bot ssh -T myserver "whoami"
```

---

## Security Considerations

### ✅ Security Features Enabled

1. **Ed25519 Key**: Modern, secure elliptic curve cryptography
2. **No Passphrase**: Required for autonomous bot operation
3. **IdentitiesOnly**: Bot only uses specified key, not SSH agent
4. **StrictHostKeyChecking=accept-new**: Prevents MITM on first connect
5. **ServerAliveInterval**: Keeps connection alive through NAT/firewalls
6. **Key Stored in Volume**: Persists across container restarts

### ⚠️ Important Security Notes

1. **Private Key Location**: `/home/node/.ssh/id_ed25519` (inside container)
   - Stored in Docker volume: `openclaw-ssh`
   - Not accessible from host filesystem
   - Persists across container restarts

2. **No Passphrase**: The key has no passphrase for autonomous operation
   - **Implication**: Anyone with container access can use the key
   - **Mitigation**: Container runs as non-root, localhost-only binding
   - **Recommendation**: Only use for trusted dev/test environments

3. **Authorized Hosts**: Only add the public key to hosts you trust
   - Bot can execute commands on any host with this key
   - Review SSH audit logs regularly

4. **Key Rotation**: To rotate the key:
   ```bash
   # Generate new key
   docker exec -u node openclaw-bot ssh-keygen -t ed25519 -C "openclaw-bot@agentshroud.ai" -f /home/node/.ssh/id_ed25519_new -N ""

   # Update authorized_keys on all hosts
   # ... (add new public key)

   # Replace old key
   docker exec -u node openclaw-bot mv /home/node/.ssh/id_ed25519_new /home/node/.ssh/id_ed25519
   docker exec -u node openclaw-bot mv /home/node/.ssh/id_ed25519_new.pub /home/node/.ssh/id_ed25519.pub
   ```

---

## Usage Examples

### From Docker Command Line

```bash
# Basic SSH
docker exec -u node openclaw-bot ssh pi-dev

# Run single command
docker exec -u node openclaw-bot ssh pi-dev "uptime"

# Run multiple commands
docker exec -u node openclaw-bot ssh pi-dev "cd /home/agentshroud-bot/projects && git status"

# Copy file to Pi
docker exec -u node openclaw-bot scp /path/to/file pi-dev:/home/agentshroud-bot/

# Copy file from Pi
docker exec -u node openclaw-bot scp pi-dev:/home/agentshroud-bot/file.txt /tmp/
```

### From OpenClaw Bot (Natural Language)

**Via Telegram:**
```
Can you SSH to the Raspberry Pi and check if Docker is installed?
```

**Via Control UI:**
```
Please SSH to pi-dev and create a new directory: ~/projects/test
```

**Complex Task:**
```
SSH to raspberrypi, clone the agentshroud repo, install dependencies, and run tests
```

---

## Troubleshooting

### Problem: "Permission denied (publickey)"

**Solution:**
```bash
# 1. Verify public key is on target host
ssh idallasj@raspberrypi.tail240ea8.ts.net "sudo cat /home/agentshroud-bot/.ssh/authorized_keys"

# 2. Check permissions on target host
ssh idallasj@raspberrypi.tail240ea8.ts.net "sudo ls -la /home/agentshroud-bot/.ssh/"
# Should be: drwx------ (700) for .ssh/, -rw------- (600) for authorized_keys

# 3. Test with verbose output
docker exec -u node openclaw-bot ssh -vvv pi-dev
```

### Problem: "Bad owner or permissions on ~/.ssh/config"

**Solution:**
```bash
# Fix permissions
docker exec -u node openclaw-bot chmod 600 /home/node/.ssh/config
docker exec -u node openclaw-bot ls -la /home/node/.ssh/
# config should be: -rw------- 1 node node
```

### Problem: "Host key verification failed"

**Solution:**
```bash
# Remove old host key
docker exec -u node openclaw-bot ssh-keygen -R raspberrypi.tail240ea8.ts.net

# Retry connection (will accept new host key)
docker exec -u node openclaw-bot ssh pi-dev
```

### Problem: "Connection timeout"

**Possible causes:**
1. Tailscale not connected on Mac or Pi
   ```bash
   tailscale status
   ```
2. Firewall blocking SSH on Pi
   ```bash
   ssh idallasj@raspberrypi.tail240ea8.ts.net "sudo ufw status"
   ```
3. SSH not listening on Tailscale interface
   ```bash
   ssh idallasj@raspberrypi.tail240ea8.ts.net "sudo netstat -tlnp | grep :22"
   ```

---

## Backup and Recovery

### Backup SSH Keys

```bash
# Export private key (SECURE THIS FILE!)
docker cp openclaw-bot:/home/node/.ssh/id_ed25519 ~/secure-backup/openclaw-bot-ssh-key

# Export public key
docker cp openclaw-bot:/home/node/.ssh/id_ed25519.pub ~/secure-backup/openclaw-bot-ssh-key.pub

# Encrypt backup (recommended)
openssl enc -aes-256-cbc -salt -in ~/secure-backup/openclaw-bot-ssh-key -out ~/secure-backup/openclaw-bot-ssh-key.enc
rm ~/secure-backup/openclaw-bot-ssh-key  # Remove unencrypted copy
```

### Restore SSH Keys

```bash
# Decrypt backup (if encrypted)
openssl enc -aes-256-cbc -d -in ~/secure-backup/openclaw-bot-ssh-key.enc -out /tmp/openclaw-bot-ssh-key

# Copy keys into container
docker cp /tmp/openclaw-bot-ssh-key openclaw-bot:/home/node/.ssh/id_ed25519
docker cp ~/secure-backup/openclaw-bot-ssh-key.pub openclaw-bot:/home/node/.ssh/id_ed25519.pub

# Fix permissions
docker exec -u node openclaw-bot chmod 600 /home/node/.ssh/id_ed25519
docker exec -u node openclaw-bot chmod 644 /home/node/.ssh/id_ed25519.pub

# Clean up temporary files
rm /tmp/openclaw-bot-ssh-key
```

---

## Verification Checklist

Run these commands to verify the setup is complete:

```bash
# 1. Check SSH key exists in container
docker exec openclaw-bot ls -la /home/node/.ssh/
# Expected: id_ed25519 (private), id_ed25519.pub (public), config

# 2. Check SSH config is valid
docker exec -u node openclaw-bot ssh -G pi-dev | grep -E "hostname|user|identityfile"
# Expected:
#   hostname raspberrypi.tail240ea8.ts.net
#   user agentshroud-bot
#   identityfile ~/.ssh/id_ed25519

# 3. Check public key is on Pi
ssh idallasj@raspberrypi.tail240ea8.ts.net "sudo cat /home/agentshroud-bot/.ssh/authorized_keys | grep openclaw-bot"
# Expected: ssh-ed25519 AAAAC3Nza... openclaw-bot@agentshroud.ai

# 4. Test bot SSH connection
docker exec -u node openclaw-bot ssh -T -o BatchMode=yes pi-dev "echo 'SSH Success!'"
# Expected: SSH Success!

# 5. Verify SSH from OpenClaw works
# Via Telegram or Control UI:
# "SSH to pi-dev and run: whoami"
# Expected: agentshroud-bot
```

---

## Next Steps

1. ✅ **SSH Key Generated** - Complete
2. ⏳ **Add Key to Raspberry Pi** - Follow Step 1 above
3. ⏳ **Test Connection** - Follow Step 2 above
4. ⏳ **Begin Bot Development Team Setup** - See `BOT_DEVELOPMENT_TEAM_RPI_SETUP.md`

---

## Quick Reference

### 🔐 Credentials in 1Password
All SSH connection details are stored in 1Password:
- Raspberry Pi hostname: `raspberrypi.tail240ea8.ts.net`
- Username: `agentshroud-bot` (hyphen, not underscore)
- SSH public key (also documented below)

### Public Key (Copy-Paste Ready)
```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIE/kQadW0OjqtR7Ersmh+uutCIasXZ9HWUNUCNDEpHLO openclaw-bot@agentshroud.ai
```

### One-Liner to Add to Pi
```bash
echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIE/kQadW0OjqtR7Ersmh+uutCIasXZ9HWUNUCNDEpHLO openclaw-bot@agentshroud.ai" | sudo tee -a /home/agentshroud-bot/.ssh/authorized_keys && sudo chown agentshroud-bot:agentshroud-bot /home/agentshroud-bot/.ssh/authorized_keys && sudo chmod 600 /home/agentshroud-bot/.ssh/authorized_keys
```

### Test Connection
```bash
docker exec -u node openclaw-bot ssh pi-dev "hostname && whoami"
# Expected output:
# raspberrypi
# agentshroud-bot
```

---

**Last Updated:** 2026-02-16
**SSH Key Fingerprint:** SHA256:uKiLmqySVY5QkQZY962/UKjFPDWWz/q8yczCDI0l4Ck
