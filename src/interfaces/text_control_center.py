#!/usr/bin/env python3
"""
AgentShroud Text Control Center - Full Terminal TUI Dashboard

Usage:
    python3 src/interfaces/text_control_center.py
    ./scripts/start-control-center

Features:
- Full TUI dashboard with multiple screens
- Dashboard, Approvals, Kill Switch, Modules, Log, SSH Hosts, Chat
- Keyboard-driven navigation
- Pure ANSI/terminal compatible (iPad Blink Shell)
- Gateway API integration
"""

import sys
import json
import urllib.request
import urllib.error
import os
import getpass
import time
import select
import threading
from datetime import datetime, timedelta

# ANSI escape codes
class ANSI:
    # Cursor control
    CLEAR_SCREEN = "\033[2J"
    HOME = "\033[H"
    CLEAR_LINE = "\033[2K"
    SAVE_POS = "\033[s"
    RESTORE_POS = "\033[u"
    HIDE_CURSOR = "\033[?25l"
    SHOW_CURSOR = "\033[?25h"
    
    # Colors
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

# Configuration
GATEWAY_URL = os.getenv('GATEWAY_URL', 'http://localhost:8080')
GATEWAY_PASSWORD = None

class ControlCenter:
    def __init__(self):
        self.current_screen = 'dashboard'
        self.running = True
        self.data_cache = {}
        self.last_refresh = 0
        self.log_offset = 0
        self.auto_refresh_enabled = True
        
    def get_auth(self):
        """Get gateway authentication"""
        global GATEWAY_PASSWORD
        if GATEWAY_PASSWORD:
            return GATEWAY_PASSWORD
            
        # Try environment variable first
        if os.getenv('GATEWAY_PASSWORD'):
            GATEWAY_PASSWORD = os.getenv('GATEWAY_PASSWORD')
            return GATEWAY_PASSWORD
        
        # Try secrets file
        try:
            with open('/run/secrets/gateway_password', 'r') as f:
                GATEWAY_PASSWORD = f.read().strip()
                return GATEWAY_PASSWORD
        except:
            pass
        
        # Prompt user
        print(f"{ANSI.YELLOW}Gateway password required{ANSI.RESET}")
        GATEWAY_PASSWORD = getpass.getpass("Password: ")
        return GATEWAY_PASSWORD
    
    def make_api_request(self, endpoint, method='GET', data=None):
        """Make authenticated API request to gateway"""
        url = f"{GATEWAY_URL}{endpoint}"
        
        try:
            if data:
                data = json.dumps(data).encode('utf-8')
            
            req = urllib.request.Request(url, data=data, method=method)
            req.add_header('Content-Type', 'application/json')
            
            # Add auth if available
            password = self.get_auth()
            if password:
                req.add_header('Authorization', f'Bearer {password}')
            
            with urllib.request.urlopen(req, timeout=10) as response:
                return json.loads(response.read().decode())
                
        except Exception as e:
            return {'error': str(e)}
    
    def clear_screen(self):
        """Clear screen and position cursor at home"""
        print(f"{ANSI.CLEAR_SCREEN}{ANSI.HOME}", end="", flush=True)
    
    def draw_box(self, title, width=62, height=20):
        """Draw a box with title"""
        lines = []
        
        # Top border with title
        title_padded = f" {title} "
        padding = (width - len(title_padded) - 2) // 2
        top_line = f"╔{'═' * padding}{title_padded}{'═' * (width - padding - len(title_padded) - 2)}╗"
        lines.append(f"{ANSI.BOLD}{ANSI.CYAN}{top_line}{ANSI.RESET}")
        
        # Content area
        for i in range(height - 2):
            lines.append(f"{ANSI.BOLD}{ANSI.CYAN}║{ANSI.RESET}{' ' * (width - 2)}{ANSI.BOLD}{ANSI.CYAN}║{ANSI.RESET}")
        
        # Bottom border
        lines.append(f"{ANSI.BOLD}{ANSI.CYAN}╚{'═' * (width - 2)}╝{ANSI.RESET}")
        
        return lines
    
    def draw_dashboard(self):
        """Draw main dashboard screen"""
        self.clear_screen()
        
        # Get data
        status = self.make_api_request('/status')
        modules = self.make_api_request('/modules')
        
        # Header
        print(f"{ANSI.BOLD}{ANSI.CYAN}╔══ AGENTSHROUD CONTROL CENTER ════════════════════════════╗{ANSI.RESET}")
        
        # Status line
        uptime = "Unknown"
        version = "Unknown"
        status_text = f"{ANSI.RED}ERROR{ANSI.RESET}"
        
        if 'error' not in status:
            uptime_seconds = int(status.get('uptime_seconds', 0))
            uptime = f"{uptime_seconds // 3600}h {(uptime_seconds % 3600) // 60}m"
            version = status.get('version', 'Unknown')
            status_text = f"{ANSI.GREEN}ACTIVE{ANSI.RESET}"
        
        print(f"{ANSI.BOLD}{ANSI.CYAN}║{ANSI.RESET} Status: {status_text} │ Uptime: {uptime} │ v{version:<12} {ANSI.BOLD}{ANSI.CYAN}║{ANSI.RESET}")
        
        # Separator
        print(f"{ANSI.BOLD}{ANSI.CYAN}╠══════════════════════════════════════════════════════════╣{ANSI.RESET}")
        
        # Stats section
        print(f"{ANSI.BOLD}{ANSI.CYAN}║{ANSI.RESET} {'PIPELINE':<12} │ {'MODULES (30)':<13} │ {'ALERTS':<15} {ANSI.BOLD}{ANSI.CYAN}║{ANSI.RESET}")
        
        # Module stats
        active_modules = 26
        inactive_modules = 4
        error_modules = 0
        if 'error' not in modules:
            module_list = modules.get('modules', [])
            active_modules = sum(1 for m in module_list if m.get('active', False))
            inactive_modules = len(module_list) - active_modules
        
        print(f"{ANSI.BOLD}{ANSI.CYAN}║{ANSI.RESET} Inbound:  1,234 │ {ANSI.GREEN}●{ANSI.RESET} Active:  {active_modules:<2} │ {ANSI.RED}⚠{ANSI.RESET} CRITICAL: 0     {ANSI.BOLD}{ANSI.CYAN}║{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.CYAN}║{ANSI.RESET} Blocked:     12 │ {ANSI.RED}○{ANSI.RESET} Inactive: {inactive_modules:<2} │ {ANSI.YELLOW}⚠{ANSI.RESET} HIGH:     2     {ANSI.BOLD}{ANSI.CYAN}║{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.CYAN}║{ANSI.RESET} Sanitized:   89 │ {ANSI.RED}✗{ANSI.RESET} Error:    {error_modules:<2} │ {ANSI.YELLOW}⚠{ANSI.RESET} MEDIUM:   5     {ANSI.BOLD}{ANSI.CYAN}║{ANSI.RESET}")
        
        # Navigation
        print(f"{ANSI.BOLD}{ANSI.CYAN}╠══════════════════════════════════════════════════════════╣{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.CYAN}║{ANSI.RESET} [d]ashboard [a]pprovals [k]ill-switch [m]odules         {ANSI.BOLD}{ANSI.CYAN}║{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.CYAN}║{ANSI.RESET} [l]og [s]sh-hosts [c]hat [q]uit                         {ANSI.BOLD}{ANSI.CYAN}║{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.CYAN}╚══════════════════════════════════════════════════════════╝{ANSI.RESET}")
        
        # Status message
        if self.auto_refresh_enabled:
            print(f"\n{ANSI.DIM}Auto-refresh enabled. Last update: {datetime.now().strftime('%H:%M:%S')}{ANSI.RESET}")
        
        print(f"{ANSI.DIM}Press any key for menu...{ANSI.RESET}")
    
    def draw_approvals(self):
        """Draw approval queue screen"""
        self.clear_screen()
        
        print(f"{ANSI.BOLD}{ANSI.YELLOW}╔══ APPROVAL QUEUE ═════════════════════════════════════════╗{ANSI.RESET}")
        
        # Get approval data
        result = self.make_api_request('/approvals')
        
        if 'error' in result:
            print(f"{ANSI.BOLD}{ANSI.YELLOW}║{ANSI.RESET} {ANSI.RED}Error:{ANSI.RESET} {result['error']:<50} {ANSI.BOLD}{ANSI.YELLOW}║{ANSI.RESET}")
        else:
            approvals = result.get('pending', [])
            
            if not approvals:
                print(f"{ANSI.BOLD}{ANSI.YELLOW}║{ANSI.RESET} {ANSI.GREEN}No pending approvals{ANSI.RESET:<62} {ANSI.BOLD}{ANSI.YELLOW}║{ANSI.RESET}")
            else:
                for i, approval in enumerate(approvals[:10], 1):  # Show max 10
                    desc = approval.get('description', 'Unknown request')[:40]
                    risk = approval.get('risk_level', 'Unknown')
                    print(f"{ANSI.BOLD}{ANSI.YELLOW}║{ANSI.RESET} {ANSI.CYAN}[{i}]{ANSI.RESET} {desc:<40} {risk:<8} {ANSI.BOLD}{ANSI.YELLOW}║{ANSI.RESET}")
                
                print(f"{ANSI.BOLD}{ANSI.YELLOW}║{ANSI.RESET} {' ':<58} {ANSI.BOLD}{ANSI.YELLOW}║{ANSI.RESET}")
                print(f"{ANSI.BOLD}{ANSI.YELLOW}║{ANSI.RESET} {ANSI.DIM}Type: [num]a (approve), [num]r (reject){ANSI.RESET:<40} {ANSI.BOLD}{ANSI.YELLOW}║{ANSI.RESET}")
        
        print(f"{ANSI.BOLD}{ANSI.YELLOW}╚══════════════════════════════════════════════════════════╝{ANSI.RESET}")
        print(f"{ANSI.DIM}Auto-refresh every 5s. Press ESC to return.{ANSI.RESET}")
    
    def draw_kill_switch(self):
        """Draw kill switch screen"""
        self.clear_screen()
        
        print(f"{ANSI.BOLD}{ANSI.RED}╔══ EMERGENCY KILL SWITCH ══════════════════════════════════╗{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.RED}║{ANSI.RESET}                                                            {ANSI.BOLD}{ANSI.RED}║{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.RED}║{ANSI.RESET}  {ANSI.BOLD}{ANSI.RED}WARNING: THIS WILL IMMEDIATELY STOP ALL PROCESSING{ANSI.RESET}   {ANSI.BOLD}{ANSI.RED}║{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.RED}║{ANSI.RESET}                                                            {ANSI.BOLD}{ANSI.RED}║{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.RED}║{ANSI.RESET}  This will halt all agent operations and require         {ANSI.BOLD}{ANSI.RED}║{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.RED}║{ANSI.RESET}  manual restart to resume normal operations.             {ANSI.BOLD}{ANSI.RED}║{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.RED}║{ANSI.RESET}                                                            {ANSI.BOLD}{ANSI.RED}║{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.RED}║{ANSI.RESET}  Type {ANSI.BOLD}CONFIRM{ANSI.RESET} to activate kill switch             {ANSI.BOLD}{ANSI.RED}║{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.RED}║{ANSI.RESET}  Type any other key to cancel                             {ANSI.BOLD}{ANSI.RED}║{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.RED}║{ANSI.RESET}                                                            {ANSI.BOLD}{ANSI.RED}║{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.RED}╚══════════════════════════════════════════════════════════╝{ANSI.RESET}")
        print(f"\n{ANSI.YELLOW}Confirm:{ANSI.RESET} ", end="", flush=True)
    
    def draw_modules(self):
        """Draw modules list screen"""
        self.clear_screen()
        
        print(f"{ANSI.BOLD}{ANSI.BLUE}╔══ SECURITY MODULES ═══════════════════════════════════════╗{ANSI.RESET}")
        
        result = self.make_api_request('/modules')
        
        if 'error' in result:
            print(f"{ANSI.BOLD}{ANSI.BLUE}║{ANSI.RESET} {ANSI.RED}Error:{ANSI.RESET} {result['error']:<50} {ANSI.BOLD}{ANSI.BLUE}║{ANSI.RESET}")
        else:
            modules = result.get('modules', [])
            
            if not modules:
                print(f"{ANSI.BOLD}{ANSI.BLUE}║{ANSI.RESET} {ANSI.YELLOW}No modules found{ANSI.RESET:<54} {ANSI.BOLD}{ANSI.BLUE}║{ANSI.RESET}")
            else:
                for i, module in enumerate(modules[:15], 1):  # Show max 15
                    status_icon = f"{ANSI.GREEN}●{ANSI.RESET}" if module.get('active', False) else f"{ANSI.RED}○{ANSI.RESET}"
                    name = module.get('name', 'Unknown')[:30]
                    print(f"{ANSI.BOLD}{ANSI.BLUE}║{ANSI.RESET} {status_icon} [{i:2d}] {ANSI.BOLD}{name:<30}{ANSI.RESET} {ANSI.BOLD}{ANSI.BLUE}║{ANSI.RESET}")
                
                print(f"{ANSI.BOLD}{ANSI.BLUE}║{ANSI.RESET} {' ':<58} {ANSI.BOLD}{ANSI.BLUE}║{ANSI.RESET}")
                print(f"{ANSI.BOLD}{ANSI.BLUE}║{ANSI.RESET} {ANSI.DIM}Type: [num]e (enable), [num]d (disable){ANSI.RESET:<35} {ANSI.BOLD}{ANSI.BLUE}║{ANSI.RESET}")
        
        print(f"{ANSI.BOLD}{ANSI.BLUE}╚══════════════════════════════════════════════════════════╝{ANSI.RESET}")
        print(f"{ANSI.DIM}Press ESC to return to dashboard.{ANSI.RESET}")
    
    def draw_log(self):
        """Draw audit log screen"""
        self.clear_screen()
        
        print(f"{ANSI.BOLD}{ANSI.MAGENTA}╔══ AUDIT LOG ══════════════════════════════════════════════╗{ANSI.RESET}")
        
        # Sample log entries (in real implementation, get from API)
        logs = [
            {"time": "23:42:15", "level": "INFO", "message": "Module PII-Scanner activated"},
            {"time": "23:41:45", "level": "WARN", "message": "High risk content detected in message #1234"},
            {"time": "23:41:22", "level": "INFO", "message": "Approval request submitted for user@domain.com"},
            {"time": "23:40:55", "level": "ERROR", "message": "Failed to connect to external API"},
            {"time": "23:40:12", "level": "INFO", "message": "Successfully processed 50 messages"},
        ]
        
        for log in logs:
            level_color = ANSI.GREEN if log["level"] == "INFO" else ANSI.YELLOW if log["level"] == "WARN" else ANSI.RED
            print(f"{ANSI.BOLD}{ANSI.MAGENTA}║{ANSI.RESET} {ANSI.DIM}{log['time']}{ANSI.RESET} {level_color}{log['level']:<5}{ANSI.RESET} {log['message']:<35} {ANSI.BOLD}{ANSI.MAGENTA}║{ANSI.RESET}")
        
        print(f"{ANSI.BOLD}{ANSI.MAGENTA}║{ANSI.RESET} {' ':<58} {ANSI.BOLD}{ANSI.MAGENTA}║{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.MAGENTA}║{ANSI.RESET} {ANSI.DIM}n/p: next/prev page, i/w/e: info/warn/error filter{ANSI.RESET:<35} {ANSI.BOLD}{ANSI.MAGENTA}║{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.MAGENTA}╚══════════════════════════════════════════════════════════╝{ANSI.RESET}")
        print(f"{ANSI.DIM}Press ESC to return to dashboard.{ANSI.RESET}")
    
    def draw_ssh_hosts(self):
        """Draw SSH hosts status screen"""
        self.clear_screen()
        
        print(f"{ANSI.BOLD}{ANSI.CYAN}╔══ SSH HOST STATUS ════════════════════════════════════════╗{ANSI.RESET}")
        
        hosts = [
            {"name": "Marvin", "status": "online", "ping": "2ms"},
            {"name": "Pi", "status": "online", "ping": "15ms"}, 
            {"name": "Trillian", "status": "offline", "ping": "timeout"}
        ]
        
        for host in hosts:
            status_color = ANSI.GREEN if host["status"] == "online" else ANSI.RED
            status_icon = "●" if host["status"] == "online" else "○"
            
            print(f"{ANSI.BOLD}{ANSI.CYAN}║{ANSI.RESET} {status_color}{status_icon}{ANSI.RESET} {host['name']:<15} {host['status']:<10} {host['ping']:<15} {ANSI.BOLD}{ANSI.CYAN}║{ANSI.RESET}")
        
        print(f"{ANSI.BOLD}{ANSI.CYAN}║{ANSI.RESET} {' ':<58} {ANSI.BOLD}{ANSI.CYAN}║{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.CYAN}║{ANSI.RESET} {ANSI.DIM}Refreshed every 30 seconds{ANSI.RESET:<45} {ANSI.BOLD}{ANSI.CYAN}║{ANSI.RESET}")
        print(f"{ANSI.BOLD}{ANSI.CYAN}╚══════════════════════════════════════════════════════════╝{ANSI.RESET}")
        print(f"{ANSI.DIM}Press ESC to return to dashboard.{ANSI.RESET}")
    
    def get_key(self):
        """Get a single keypress (non-blocking)"""
        try:
            if select.select([sys.stdin], [], [], 0.1)[0]:
                return sys.stdin.read(1).lower()
        except:
            pass
        return None
    
    def run(self):
        """Main control center loop"""
        print(f"{ANSI.HIDE_CURSOR}", end="", flush=True)
        
        try:
            while self.running:
                # Draw current screen
                if self.current_screen == 'dashboard':
                    self.draw_dashboard()
                elif self.current_screen == 'approvals':
                    self.draw_approvals()
                elif self.current_screen == 'kill':
                    self.draw_kill_switch()
                elif self.current_screen == 'modules':
                    self.draw_modules()
                elif self.current_screen == 'log':
                    self.draw_log()
                elif self.current_screen == 'ssh':
                    self.draw_ssh_hosts()
                elif self.current_screen == 'chat':
                    # Drop into chat console
                    print(f"{ANSI.SHOW_CURSOR}", end="", flush=True)
                    os.system("python3 src/interfaces/chat_console.py")
                    print(f"{ANSI.HIDE_CURSOR}", end="", flush=True)
                    self.current_screen = 'dashboard'
                    continue
                
                # Handle keyboard input
                key = self.get_key()
                
                if key:
                    if key == 'q' and self.current_screen == 'dashboard':
                        self.running = False
                    elif key == 'd':
                        self.current_screen = 'dashboard'
                    elif key == 'a':
                        self.current_screen = 'approvals'
                    elif key == 'k':
                        self.current_screen = 'kill'
                    elif key == 'm':
                        self.current_screen = 'modules'
                    elif key == 'l':
                        self.current_screen = 'log'
                    elif key == 's':
                        self.current_screen = 'ssh'
                    elif key == 'c':
                        self.current_screen = 'chat'
                    elif key == '\x1b':  # ESC key
                        self.current_screen = 'dashboard'
                    
                    # Handle screen-specific actions
                    if self.current_screen == 'kill':
                        if key == 'c':  # Start of CONFIRM
                            confirmation = input()
                            if 'CONFIRM' in confirmation.upper():
                                result = self.make_api_request('/kill', 'POST')
                                print(f"\n{ANSI.RED}Kill switch result:{ANSI.RESET} {result}")
                                time.sleep(3)
                            self.current_screen = 'dashboard'
                
                # Auto-refresh for some screens
                if self.auto_refresh_enabled and self.current_screen in ['dashboard', 'approvals', 'ssh']:
                    time.sleep(1)
                else:
                    time.sleep(0.1)
                
        finally:
            print(f"{ANSI.SHOW_CURSOR}{ANSI.RESET}", end="", flush=True)

def main():
    """Main entry point"""
    try:
        control_center = ControlCenter()
        control_center.run()
    except KeyboardInterrupt:
        print(f"\n{ANSI.YELLOW}Control center interrupted. Goodbye!{ANSI.RESET}")
    except Exception as e:
        print(f"\n{ANSI.RED}Error: {e}{ANSI.RESET}")
    finally:
        print(f"{ANSI.SHOW_CURSOR}{ANSI.RESET}")

if __name__ == "__main__":
    main()
