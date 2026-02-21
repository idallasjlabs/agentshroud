#!/usr/bin/env python3
"""
AgentShroud Text Control Center - Working Version
"""
import time
import os
from datetime import datetime

def display_dashboard():
    """Simple working dashboard"""
    print("\033[2J\033[H")  # Clear screen
    print("┌─ AGENTSHROUD CONTROL CENTER ──────────────────────┐")
    print("│ The Transparent Security Proxy for Agents         │")
    print("├────────────────────────────────────────────────────┤")
    print(f"│ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}                │")
    print("│                                                    │")
    print("│ Status: ACTIVE                                     │")
    print("│ Version: v0.3.0                                    │")
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
