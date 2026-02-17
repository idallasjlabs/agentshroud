"""SSH Proxy module for SecureClaw Gateway

Executes SSH commands via asyncio subprocess with validation and timeout enforcement.
"""

import asyncio
import re
import time
from dataclasses import dataclass

from gateway.ingest_api.ssh_config import SSHConfig


@dataclass
class SSHResult:
    """Result of an SSH command execution"""
    stdout: str
    stderr: str
    exit_code: int
    duration_seconds: float
    host: str
    command: str


# Shell metacharacters that indicate injection attempts
INJECTION_PATTERNS = re.compile(r"[;|&`]|\$\(|\|\||&&")


class SSHProxy:
    """SSH command proxy with validation and audit support"""

    def __init__(self, config: SSHConfig):
        self.config = config

    def validate_command(self, host_name: str, command: str) -> tuple[bool, str]:
        """Validate a command against allow/deny lists and injection patterns.

        Returns (is_valid, reason).
        """
        if not command or not command.strip():
            return False, "Empty command"

        if host_name not in self.config.hosts:
            return False, f"Unknown host: {host_name}"

        # Check injection patterns
        if INJECTION_PATTERNS.search(command):
            return False, "Shell metacharacter injection detected"

        host = self.config.hosts[host_name]

        # Check global denied commands
        for denied in self.config.global_denied_commands:
            if denied in command:
                return False, f"Command denied by global policy: {denied}"

        # Check host denied commands
        for denied in host.denied_commands:
            if denied in command:
                return False, f"Command denied: {denied}"

        # Check allowlist (if non-empty, command must match one)
        if host.allowed_commands:
            if not any(command == allowed or command.startswith(allowed + " ") or allowed == command.split()[0]
                       for allowed in host.allowed_commands):
                return False, f"Command not in allowed list for host {host_name}"

        return True, "OK"

    def is_auto_approved(self, host_name: str, command: str) -> bool:
        """Check if a command is auto-approved (no human approval needed)."""
        if host_name not in self.config.hosts:
            return False
        host = self.config.hosts[host_name]
        return command in host.auto_approve_commands

    async def execute(self, host_name: str, command: str, timeout: int | None = None) -> SSHResult:
        """Execute a command on a remote host via SSH."""
        if host_name not in self.config.hosts:
            raise ValueError(f"Unknown host: {host_name}")

        host = self.config.hosts[host_name]
        effective_timeout = timeout or host.max_session_seconds

        # Build SSH command
        ssh_args = ["ssh", "-o", "StrictHostKeyChecking=no", "-o", "BatchMode=yes",
                     "-p", str(host.port)]
        if host.key_path:
            ssh_args.extend(["-i", host.key_path])
        ssh_args.append(f"{host.username}@{host.host}")
        ssh_args.append(command)

        start = time.monotonic()
        try:
            proc = await asyncio.create_subprocess_exec(
                *ssh_args,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            try:
                stdout_bytes, stderr_bytes = await asyncio.wait_for(
                    proc.communicate(), timeout=effective_timeout
                )
            except asyncio.TimeoutError:
                proc.kill()
                await proc.wait()
                duration = time.monotonic() - start
                return SSHResult(
                    stdout="", stderr=f"Timeout: command exceeded {effective_timeout}s",
                    exit_code=-1, duration_seconds=duration,
                    host=host_name, command=command,
                )

            duration = time.monotonic() - start
            return SSHResult(
                stdout=stdout_bytes.decode("utf-8", errors="replace"),
                stderr=stderr_bytes.decode("utf-8", errors="replace"),
                exit_code=proc.returncode or 0,
                duration_seconds=duration,
                host=host_name, command=command,
            )
        except Exception as e:
            duration = time.monotonic() - start
            return SSHResult(
                stdout="", stderr=str(e), exit_code=-1,
                duration_seconds=duration, host=host_name, command=command,
            )
