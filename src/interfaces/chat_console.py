#!/usr/bin/env python3
"""
AgentShroud Text Chat Console - Chat with OpenClaw as Admin

Usage:
    python3 src/interfaces/chat_console.py
    ./scripts/chat-console
"""
import sys
import json
import urllib.request
import urllib.error
from datetime import datetime

# Configuration
GATEWAY_URL = "http://localhost:8080"
OPENCLAW_URL = "http://localhost:18790"

def print_banner():
    """Display chat console banner"""
    print("\033[2J\033[H")  # Clear screen
    print("=" * 70)
    print("  AgentShroud Chat Console - Admin Interface")
    print("  Connected to OpenClaw via Gateway")
    print("=" * 70)
    print("Commands: /help, /status, /quit")
    print("=" * 70)
    print()

def print_help():
    """Show help message"""
    print("\nAvailable Commands:")
    print("  /help     - Show this help message")
    print("  /status   - Check system status")
    print("  /quit     - Exit chat console")
    print("  Just type your message to chat with OpenClaw")
    print()

def check_status():
    """Check gateway and bot status"""
    try:
        with urllib.request.urlopen(f"{GATEWAY_URL}/status", timeout=5) as response:
            data = json.loads(response.read().decode())
            print(f"\n✓ Gateway Status: {data['status']}")
            print(f"  Version: {data['version']}")
            print(f"  Uptime: {int(data['uptime_seconds'])}s")
            print(f"  PII Engine: {data['pii_engine']}")
    except Exception as e:
        print(f"\n✗ Gateway error: {e}")

    # Check OpenClaw UI
    try:
        with urllib.request.urlopen(OPENCLAW_URL, timeout=5) as response:
            if response.status == 200:
                print(f"✓ OpenClaw UI: Accessible")
    except Exception as e:
        print(f"✗ OpenClaw error: {e}")
    print()

def send_message(message):
    """Send message to OpenClaw via gateway"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # For now, just echo back (placeholder for real API integration)
    print(f"\n[{timestamp}] You: {message}")
    print(f"[{timestamp}] Bot: API integration pending - message received")
    print("           (Requires gateway /forward endpoint configuration)")
    print()

def main():
    """Main chat loop"""
    print_banner()

    # Check system status on startup
    check_status()

    print("Ready to chat. Type your message (or /help for commands):\n")

    try:
        while True:
            try:
                # Get user input
                user_input = input("You: ").strip()

                if not user_input:
                    continue

                # Handle commands
                if user_input.startswith('/'):
                    command = user_input.lower()

                    if command == '/quit' or command == '/exit' or command == '/q':
                        print("\nExiting chat console...")
                        break
                    elif command == '/help' or command == '/?':
                        print_help()
                    elif command == '/status':
                        check_status()
                    else:
                        print(f"Unknown command: {command}")
                        print("Type /help for available commands")
                else:
                    # Send regular message
                    send_message(user_input)

            except EOFError:
                print("\n\nExiting...")
                break

    except KeyboardInterrupt:
        print("\n\nInterrupted. Exiting...")

    print("\nGoodbye!\n")

if __name__ == "__main__":
    main()
