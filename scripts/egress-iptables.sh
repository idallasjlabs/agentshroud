#!/bin/bash
# egress-iptables.sh — Egress filtering rules for Docker network
# WARNING: Requires sudo. Run as: sudo bash scripts/egress-iptables.sh
#
# This script sets up iptables rules to restrict outbound traffic from
# Docker containers to only allowed destinations.

set -euo pipefail

# Configuration — edit these for your environment
DOCKER_NETWORK="${DOCKER_NETWORK:-secureclaw_network}"
DOCKER_BRIDGE="${DOCKER_BRIDGE:-br-secureclaw}"

# Allowed outbound destinations (add your domains/IPs here)
ALLOWED_IPS=(
    "1.1.1.1"          # Cloudflare DNS
    "1.0.0.1"          # Cloudflare DNS
    "8.8.8.8"          # Google DNS (for resolution)
)

ALLOWED_CIDRS=(
    # Add CIDRs for allowed services
    # "203.0.113.0/24"
)

ALLOWED_PORTS=(
    "53"    # DNS
    "80"    # HTTP
    "443"   # HTTPS
)

echo "=== SecureClaw Egress Filtering ==="
echo "Network: $DOCKER_NETWORK"
echo "Bridge:  $DOCKER_BRIDGE"
echo ""

# Check for root
if [[ $EUID -ne 0 ]]; then
    echo "ERROR: This script must be run as root (sudo)."
    exit 1
fi

# Create custom chain
iptables -N SECURECLAW_EGRESS 2>/dev/null || iptables -F SECURECLAW_EGRESS

# Allow established connections
iptables -A SECURECLAW_EGRESS -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allow loopback
iptables -A SECURECLAW_EGRESS -o lo -j ACCEPT

# Allow DNS
for port in "${ALLOWED_PORTS[@]}"; do
    iptables -A SECURECLAW_EGRESS -p tcp --dport "$port" -j ACCEPT
    iptables -A SECURECLAW_EGRESS -p udp --dport "$port" -j ACCEPT
done

# Allow specific IPs
for ip in "${ALLOWED_IPS[@]}"; do
    iptables -A SECURECLAW_EGRESS -d "$ip" -j ACCEPT
done

# Allow specific CIDRs
for cidr in "${ALLOWED_CIDRS[@]}"; do
    iptables -A SECURECLAW_EGRESS -d "$cidr" -j ACCEPT
done

# Default deny with logging
iptables -A SECURECLAW_EGRESS -j LOG --log-prefix "SECURECLAW_EGRESS_DENY: " --log-level 4
iptables -A SECURECLAW_EGRESS -j DROP

# Apply to Docker bridge
# Remove existing reference if any
iptables -D FORWARD -i "$DOCKER_BRIDGE" -j SECURECLAW_EGRESS 2>/dev/null || true
iptables -I FORWARD -i "$DOCKER_BRIDGE" -j SECURECLAW_EGRESS

echo "Egress filtering rules applied successfully."
echo "To remove: iptables -D FORWARD -i $DOCKER_BRIDGE -j SECURECLAW_EGRESS && iptables -F SECURECLAW_EGRESS && iptables -X SECURECLAW_EGRESS"
