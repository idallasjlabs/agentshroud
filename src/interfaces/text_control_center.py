#!/usr/bin/env python3
"""
AgentShroud Text Control Center - Working Version
"""
import time
import os
import json
import urllib.request
import urllib.error
from datetime import datetime

GATEWAY_URL = os.getenv('GATEWAY_URL', 'http://localhost:8080')


def _api_get(endpoint):
    """Fetch JSON from gateway API, return dict or None on error."""
    try:
        req = urllib.request.Request(f"{GATEWAY_URL}{endpoint}")
        req.add_header('Content-Type', 'application/json')
        password = os.getenv('GATEWAY_PASSWORD', '')
        if password:
            req.add_header('Authorization', f'Bearer {password}')
        with urllib.request.urlopen(req, timeout=5) as resp:
            return json.loads(resp.read().decode())
    except Exception:
        return None


def display_dashboard():
    """Simple working dashboard"""
    print("\033[2J\033[H")  # Clear screen

    # Fetch live status from gateway
    status = _api_get('/status')
    if status and 'error' not in status:
        version = status.get('version', 'N/A')
        uptime_s = int(status.get('uptime_seconds', 0))
        uptime_str = f"{uptime_s // 3600}h {(uptime_s % 3600) // 60}m"
        gw_status = "ACTIVE"
    else:
        version = "N/A"
        uptime_str = "N/A"
        gw_status = "UNAVAILABLE"

    print("┌─ AGENTSHROUD CONTROL CENTER ──────────────────────┐")
    print("│ The Transparent Security Proxy for Agents         │")
    print("├────────────────────────────────────────────────────┤")
    print(f"│ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}                │")
    print("│                                                    │")
    print(f"│ Status:  {gw_status:<41}│")
    print(f"│ Version: {version:<41}│")
    print(f"│ Uptime:  {uptime_str:<41}│")
    print("│                                                    │")
    print("│ [Press Enter to refresh, 'q' + Enter to quit]     │")
    print("└────────────────────────────────────────────────────┘")


def main():
    print("AgentShroud Control Center Starting...")
    try:
        while True:
            display_dashboard()
            user_input = input().strip().lower()
            if user_input == 'q':
                break
    except KeyboardInterrupt:
        print("\nShutting down...")

if __name__ == "__main__":
    main()
