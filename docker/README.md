# Docker Configuration

This directory contains the hardened Docker container configuration for SecureClaw.

## Files (to be implemented in Week 1, Days 5-6)

- **Dockerfile** - Multi-stage build (builder + runtime)
- **docker-compose.yml** - Complete stack orchestration
- **seccomp-profile.json** - Custom seccomp security profile
- **network/**
  - `iptables-rules.sh` - Internet-only network rules
  - `tailscale-acl.json` - Tailscale VPN access control

## Security Features

- Rootless execution (USER 1000:1000)
- Read-only rootfs (where compatible with OpenClaw)
- Dropped capabilities (cap_drop: ALL, minimal cap_add)
- Network isolation (internet-only, no LAN access)
- Tailscale VPN for remote access
- Resource limits (memory, CPU, PIDs)
- Custom seccomp profile

## Implementation Status

🚧 **Not yet implemented** - Scheduled for Week 1, Days 5-6
