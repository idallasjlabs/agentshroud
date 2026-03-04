#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.

# Pi-hole Default Blocklists Setup Script
# This script configures Pi-hole with default security-focused blocklists on first startup

set -euo pipefail

PIHOLE_URL="http://pihole:80/admin/api.php"
PIHOLE_AUTH_FILE="/run/secrets/pihole_password"

# Wait for Pi-hole to be ready
echo "Waiting for Pi-hole to be ready..."
for i in {1..30}; do
    if curl -f "${PIHOLE_URL}?status" &>/dev/null; then
        echo "Pi-hole is ready"
        break
    fi
    if [ $i -eq 30 ]; then
        echo "ERROR: Pi-hole not ready after 30 attempts"
        exit 1
    fi
    sleep 2
done

# Get auth token if available
AUTH_TOKEN=""
if [ -f "$PIHOLE_AUTH_FILE" ]; then
    AUTH_TOKEN=$(cat "$PIHOLE_AUTH_FILE")
fi

# Default blocklists to configure
BLOCKLISTS=(
    "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"
    "https://big.oisd.nl/"
    "https://phishing.army/download/phishing_army_blocklist.txt"
)

echo "Configuring default blocklists..."

for blocklist in "${BLOCKLISTS[@]}"; do
    echo "Adding blocklist: $blocklist"
    
    # Add blocklist via Pi-hole API
    if [ -n "$AUTH_TOKEN" ]; then
        response=$(curl -s "${PIHOLE_URL}?list=add&address=${blocklist}&auth=${AUTH_TOKEN}" || echo "error")
    else
        response=$(curl -s "${PIHOLE_URL}?list=add&address=${blocklist}" || echo "error")
    fi
    
    if echo "$response" | grep -q "success"; then
        echo "Successfully added: $blocklist"
    else
        echo "Failed to add: $blocklist (response: $response)"
    fi
done

# Update gravity (reload blocklists)
echo "Updating gravity to load new blocklists..."
if [ -n "$AUTH_TOKEN" ]; then
    curl -s "${PIHOLE_URL}?updateGravity&auth=${AUTH_TOKEN}" > /dev/null
else
    curl -s "${PIHOLE_URL}?updateGravity" > /dev/null
fi

echo "Pi-hole blocklist setup completed successfully"
