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

# Validate inputs to prevent command injection
if [[ ! "$DOCKER_NETWORK" =~ ^[a-zA-Z0-9_-]+$ ]]; then
    echo "ERROR: DOCKER_NETWORK contains invalid characters: $DOCKER_NETWORK"
    exit 1
fi
if [[ ! "$DOCKER_BRIDGE" =~ ^[a-zA-Z0-9_-]+$ ]]; then
    echo "ERROR: DOCKER_BRIDGE contains invalid characters: $DOCKER_BRIDGE"
    exit 1
fi

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

# Allow DNS to specified DNS servers only
for ip in "${ALLOWED_IPS[@]}"; do
    iptables -A SECURECLAW_EGRESS -d "$ip" -p udp --dport 53 -j ACCEPT
    iptables -A SECURECLAW_EGRESS -d "$ip" -p tcp --dport 53 -j ACCEPT
done

# Allow specific IPs on allowed ports only
for ip in "${ALLOWED_IPS[@]}"; do
    for port in "${ALLOWED_PORTS[@]}"; do
        [ "$port" = "53" ] && continue  # Already handled above
        iptables -A SECURECLAW_EGRESS -d "$ip" -p tcp --dport "$port" -j ACCEPT
    done
done

# Allow specific CIDRs on allowed ports only
for cidr in "${ALLOWED_CIDRS[@]}"; do
    for port in "${ALLOWED_PORTS[@]}"; do
        iptables -A SECURECLAW_EGRESS -d "$cidr" -p tcp --dport "$port" -j ACCEPT
    done
done

# Default deny with logging
iptables -A SECURECLAW_EGRESS -j LOG --log-prefix "SECURECLAW_EGRESS_DENY: " --log-level 4
iptables -A SECURECLAW_EGRESS -j DROP

# Apply to Docker bridge
# Remove existing reference if any
iptables -D FORWARD -i "$DOCKER_BRIDGE" -j SECURECLAW_EGRESS 2>/dev/null || true
iptables -I FORWARD -i "$DOCKER_BRIDGE" -j SECURECLAW_EGRESS

echo "Egress filtering rules applied successfully (IPv4)."

# IPv6: default deny all egress from Docker bridge
ip6tables -N SECURECLAW_EGRESS6 2>/dev/null || ip6tables -F SECURECLAW_EGRESS6
ip6tables -A SECURECLAW_EGRESS6 -m state --state ESTABLISHED,RELATED -j ACCEPT
ip6tables -A SECURECLAW_EGRESS6 -o lo -j ACCEPT
ip6tables -A SECURECLAW_EGRESS6 -j LOG --log-prefix "SECURECLAW_EGRESS6_DENY: " --log-level 4
ip6tables -A SECURECLAW_EGRESS6 -j DROP
ip6tables -D FORWARD -i "$DOCKER_BRIDGE" -j SECURECLAW_EGRESS6 2>/dev/null || true
ip6tables -I FORWARD -i "$DOCKER_BRIDGE" -j SECURECLAW_EGRESS6

echo "IPv6 egress deny-all applied."
echo ""
echo "To remove IPv4: iptables -D FORWARD -i $DOCKER_BRIDGE -j SECURECLAW_EGRESS && iptables -F SECURECLAW_EGRESS && iptables -X SECURECLAW_EGRESS"
echo "To remove IPv6: ip6tables -D FORWARD -i $DOCKER_BRIDGE -j SECURECLAW_EGRESS6 && ip6tables -F SECURECLAW_EGRESS6 && ip6tables -X SECURECLAW_EGRESS6"
