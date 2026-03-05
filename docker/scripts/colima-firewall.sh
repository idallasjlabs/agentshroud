#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# colima-firewall.sh — Apply network security rules inside Colima VM.
#
# SECURITY (C1/C2 fix): Block bot container from reaching host SSH.
# Without this, any code running inside the bot container can SSH to
# the host using raw TCP sockets, bypassing OpenClaw approval queue.
#
# Run after Colima starts: ./docker/scripts/colima-firewall.sh
# Add to Colima post-start hook or provision script.

set -euo pipefail

echo "Applying AgentShroud network security rules..."

# Block bot subnet (isolated network) from reaching host SSH
colima ssh -- bash -c "
  # Drop existing AgentShroud rules to avoid duplicates
  sudo iptables -D DOCKER-USER -s 172.21.0.0/16 -d 192.168.5.0/24 -p tcp --dport 22 -j DROP 2>/dev/null || true
  sudo iptables -D DOCKER-USER -s 172.21.0.0/16 -d 172.21.0.1 -p tcp --dport 22 -j DROP 2>/dev/null || true
  
  # Re-add rules
  sudo iptables -I DOCKER-USER -s 172.21.0.0/16 -d 192.168.5.0/24 -p tcp --dport 22 -j DROP
  sudo iptables -I DOCKER-USER -s 172.21.0.0/16 -d 172.21.0.1 -p tcp --dport 22 -j DROP
  
  echo DOCKER-USER rules:
  sudo iptables -L DOCKER-USER -n --line-numbers
"

echo "✅ Network security rules applied"
