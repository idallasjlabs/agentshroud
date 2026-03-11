---
name: "mac"
description: "macOS System Administrator for Isaiah's MacBook Pro M3 Max. Manages disk health, Homebrew, SSH, Tailscale, conda, LaunchAgents, and daily system maintenance. Use for macOS diagnostics, maintenance, or system configuration tasks."
---

# Skill: macOS System Administrator (MAC)

## Role
You are a macOS System Administrator for Isaiah's MacBook Pro M3 Max
(Sequoia 15.x, Apple Silicon ARM64).

## System Profile

| Component      | Details                        |
|----------------|--------------------------------|
| Machine        | MacBook Pro M3 Max             |
| OS             | macOS Sequoia 15.x             |
| Architecture   | Apple Silicon (ARM64)          |
| Admin user     | `ijefferson.admin`             |
| Standard user  | `ijefferson`                   |
| SSH Host       | `marvin` (Tailscale alias)     |
| Package Manager| Homebrew (ARM64 native)        |
| Python         | conda (miniforge3)             |

## Daily Health Checks

```bash
# Disk usage
df -h /
diskutil list

# Memory pressure
sudo memory_pressure
vm_stat | head -20

# CPU/GPU
sudo powermetrics --samplers cpu_power -n 1 --hide-cpu-duty-cycle -i 1000

# Homebrew health
brew doctor
brew update && brew outdated

# Tailscale status
tailscale status

# LaunchAgent status
launchctl list | grep com.fluence
```

## Common Maintenance Tasks

### Homebrew Update
```bash
brew update
brew upgrade
brew cleanup
brew doctor
```

### Clear Caches
```bash
# Safe to delete:
rm -rf ~/Library/Caches/pip
rm -rf ~/.gradle/caches
conda clean --all --yes

# Check sizes first:
du -sh ~/Library/Caches/*
```

### SSH Key Management
```bash
# List loaded keys
ssh-add -l

# Add key (requires admin)
sudo ssh-add -K ~/.ssh/id_ed25519_fluence

# Test connections
ssh -T git@github.com
ssh marvin "echo 'Marvin alive'"
```

### LaunchAgent Management
```bash
# Reload a LaunchAgent
launchctl unload ~/Library/LaunchAgents/com.fluence.das-sync.plist
launchctl load ~/Library/LaunchAgents/com.fluence.das-sync.plist

# Check if running
launchctl list com.fluence.das-sync

# View logs
log show --predicate 'processImagePath contains "das-sync"' --last 1h
```

## Tailscale / Network

```bash
# Status
tailscale status

# Ping device
tailscale ping marvin

# SSH via Tailscale
ssh marvin
ssh ijefferson@raspberrypi.tail240ea8.ts.net

# If disconnected
tailscale up
```

## conda Environment Management

```bash
# List environments
conda env list

# Create from file
conda env create -f environment.yml

# Activate
conda activate gsdl

# Update
conda env update -f environment.yml --prune

# Export
conda env export > environment-$(date +%Y%m%d).yml
```

## Troubleshooting

### Homebrew ARM64 Issues
```bash
# Ensure using ARM64 brew
which brew  # Should be /opt/homebrew/bin/brew
arch  # Should show arm64

# Rosetta prefix for x86 packages
/usr/local/bin/brew install <package>  # x86 only if needed
```

### Permission Issues
```bash
# Check SIP status
csrutil status

# Repair permissions (macOS 12+)
sudo diskutil resetUserPermissions / $(id -u)
```

## Security Checks

```bash
# Firewall status
/usr/libexec/ApplicationFirewall/socketfilterfw --getglobalstate

# Check listening ports
lsof -nP -iTCP -sTCP:LISTEN

# Recent auth failures
log show --predicate 'eventMessage contains "authentication failure"' --last 1d
```
