#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# colima-firewall.sh — Apply network security rules inside Colima VM.
#
# Addresses: C1, C2, H4 from the container security audit (2026-03-05).
# See docs/security/container-security-audit-v0.8.0.md for full details.
#
# Run after Colima starts or on a cron schedule for self-healing.
# Usage: ./docker/scripts/colima-firewall.sh
#
# What this does:
#   1. Blocks bot container from reaching host SSH (C1/C2)
#   2. Blocks bot from direct pihole access (H4) — must go through gateway
#   3. Fixes Colima VM routing if internet access is lost (known vz driver issue)

set -euo pipefail

echo "[firewall] Applying AgentShroud network security rules..."

# ── Fix Colima VM internet routing (known vz driver issue) ───────────────────
# The eth0 default route (192.168.5.2) sometimes loses NAT.
# col0 (192.168.64.x) is the native macOS Virtualization.Framework path.
colima ssh -- bash -c '
  if ! curl -sf --connect-timeout 3 -o /dev/null https://google.com 2>/dev/null; then
    echo "[firewall] Internet broken — fixing route..."
    sudo ip route del default via 192.168.5.2 dev eth0 2>/dev/null || true
    sudo ip route add default via 192.168.64.1 dev col0 2>/dev/null || true
    echo "[firewall] Route fixed"
  else
    echo "[firewall] Internet OK"
  fi
'

# ── Apply iptables rules (idempotent) ────────────────────────────────────────
# DOCKER-USER chain runs before Docker's own rules.
# Bot container IP: 172.21.0.3 (agentshroud-isolated network)
# Pihole IP: 172.21.0.10
# Host gateway: 192.168.5.0/24

colima ssh -- bash -c '
  # Flush our rules (avoid duplicates on re-run)
  sudo iptables -F DOCKER-USER 2>/dev/null || true

  # ── C1/C2: Block bot network from reaching host SSH ──
  sudo iptables -A DOCKER-USER -s 172.21.0.0/16 -d 192.168.5.0/24 -p tcp --dport 22 -j DROP
  sudo iptables -A DOCKER-USER -s 172.21.0.0/16 -d 172.21.0.1 -p tcp --dport 22 -j DROP

  # ── H4: Block bot from direct pihole access (must go through gateway) ──
  sudo iptables -A DOCKER-USER -s 172.21.0.3 -d 172.21.0.10 -p tcp --dport 80 -j DROP
  sudo iptables -A DOCKER-USER -s 172.21.0.3 -d 172.21.0.10 -p tcp --dport 53 -j DROP
  sudo iptables -A DOCKER-USER -s 172.21.0.3 -d 172.21.0.10 -p udp --dport 53 -j DROP

  # ── RETURN: allow everything else (Docker handles the rest) ──
  sudo iptables -A DOCKER-USER -j RETURN

  echo "[firewall] DOCKER-USER rules applied:"
  sudo iptables -L DOCKER-USER -n --line-numbers
'

echo "[firewall] ✅ All network security rules active"
