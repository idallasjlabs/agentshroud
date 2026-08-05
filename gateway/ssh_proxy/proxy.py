# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""SSH Proxy module for AgentShroud Gateway

Executes SSH commands via asyncio subprocess with validation and timeout enforcement.
"""


import asyncio
import base64
import binascii
import posixpath
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


@dataclass
class SSHWriteResult:
    """Result of a structured SSH file-write operation (SSHProxy.write_file())"""

    host: str
    path: str
    bytes_written: int
    stdout: str
    stderr: str
    exit_code: int
    duration_seconds: float


# Path characters allowed in cwd: alphanumeric, /, -, _, ., space, @, ~
_CWD_SAFE = re.compile(r"^[A-Za-z0-9/_\-. @~]+$")

# === /ssh/write_file constants ===

# Approved repo checkout root on the SSH target host. Relative `path` values
# in a write_file() request resolve against this root. See
# SSHProxy.validate_write_file() for why the traversal check is pure
# string/pathlib normalization and NOT os.path.realpath()/Path.resolve().
_ALLOWED_WRITE_ROOT = "/Users/agentshroud-bot/Development/agentshroud"

# Parent directory of every git worktree used by the /i-hdev and /i-odev dev
# workflows. `git worktree add` deliberately creates SIBLING directories next
# to the primary checkout (e.g. .../Development/agentshroud-hdev-<slug>),
# never nested inside it — so absolute `path` values must be allowed anywhere
# under this parent, not just under _ALLOWED_WRITE_ROOT, or every worktree
# write is rejected by design. Confirmed via the /i-hdev end-to-end dry run
# 2026-08-05: the original single-root check made the whole worktree-based
# skill unusable.
#
# Still tightly bounded: the top-level directory name directly under this
# parent must EXACTLY match the primary checkout ("agentshroud") or the
# worktree naming convention this repo's skills use
# ("agentshroud-hdev-<slug>", "agentshroud-odev-<slug>") — a plain
# `.startswith("agentshroud")` check would let a sibling like
# "agentshroud-evil" slip through (it also starts with that string), so this
# is an exact regex match, not a prefix test.
_ALLOWED_WRITE_PARENT = "/Users/agentshroud-bot/Development"
_ALLOWED_WRITE_TOP_LEVEL_RE = re.compile(
    r"^agentshroud(?:-(?:hdev|odev)-[A-Za-z0-9](?:[A-Za-z0-9_-]*[A-Za-z0-9])?)?$"
)

# Decoded-content size cap for /ssh/write_file (exactly 500KB).
_MAX_WRITE_FILE_BYTES = 500_000

# Fixed remote script executed via `python3 -c` for every write_file() call.
# It is a CONSTANT — the same bytes run on every invocation regardless of
# request content. Path and file content are never interpolated into this
# string; they are sent as DATA on the SSH session's stdin (see
# SSHProxy.write_file()) and read by this script at runtime. This is what
# makes write_file() safe independent of validate_command()'s
# shell-metacharacter regex: there is no shell string built from
# attacker-influenced bytes anywhere in this path.
_REMOTE_WRITE_FILE_SCRIPT = (
    "import sys, base64, pathlib, re\n"
    f"_PARENT = {_ALLOWED_WRITE_PARENT!r}\n"
    f"_TOP_RE = re.compile({_ALLOWED_WRITE_TOP_LEVEL_RE.pattern!r})\n"
    "data = sys.stdin.buffer.read()\n"
    "path_b64, _, content_b64 = data.partition(b'\\n')\n"
    "path = base64.b64decode(path_b64).decode('utf-8')\n"
    "content = base64.b64decode(content_b64)\n"
    "if not path.startswith(_PARENT + '/'):\n"
    "    sys.stderr.write('path outside allowed root')\n"
    "    sys.exit(2)\n"
    "top_level, _, remainder = path[len(_PARENT) + 1:].partition('/')\n"
    "if not remainder or not _TOP_RE.match(top_level):\n"
    "    sys.stderr.write('path outside allowed root')\n"
    "    sys.exit(2)\n"
    "p = pathlib.Path(path)\n"
    "p.parent.mkdir(parents=True, exist_ok=True)\n"
    "p.write_bytes(content)\n"
    "sys.stdout.write(str(len(content)))\n"
)
# Base64 of the script above, computed once at import time from the constant
# text — never from request data. Embedding it as base64 sidesteps remote
# shell-quoting of the script body (base64's alphabet contains no shell
# metacharacters) while the outer `python3 -c "..."` string stays fixed.
_REMOTE_WRITE_FILE_SCRIPT_B64 = base64.b64encode(_REMOTE_WRITE_FILE_SCRIPT.encode("utf-8")).decode(
    "ascii"
)

# Comprehensive shell metacharacter/injection patterns
# Catches: ; | & ` $() ${} $VAR \n \r >> << > < and backslash sequences
INJECTION_PATTERNS = re.compile(
    r"[;|&`><]"  # basic shell metacharacters
    r"|\$\("  # $(...)
    r"|\$\{"  # ${...}
    r"|\$[A-Za-z_]"  # $VAR
    r"|\|\|"  # ||
    r"|&&"  # &&
    r"|[\n\r]"  # newlines
    r"|\\[nrtabfv\\]"  # backslash escape sequences
)


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
            matched = False
            for allowed in host.allowed_commands:
                if command == allowed:
                    matched = True
                    break
                # Allow "allowed_cmd arg1 arg2" if base matches and args have no injection
                if command.startswith(allowed + " "):
                    # Verify remaining args are safe (already checked by INJECTION_PATTERNS above)
                    matched = True
                    break
            if not matched:
                return False, f"Command not in allowed list for host {host_name}"

        return True, "OK"

    def is_auto_approved(self, host_name: str, command: str) -> bool:
        """Check if a command is auto-approved (no human approval needed).

        Auto-approve requires EXACT match — no extra arguments allowed.
        """
        if host_name not in self.config.hosts:
            return False
        host = self.config.hosts[host_name]
        return command in host.auto_approve_commands

    def validate_cwd(self, cwd: str) -> tuple[bool, str]:
        """Validate a remote working-directory path.  Must be absolute and shell-safe."""
        if not cwd.startswith("/") and not cwd.startswith("~"):
            return False, "cwd must be an absolute path or start with ~"
        if not _CWD_SAFE.match(cwd):
            return False, "cwd contains disallowed characters"
        return True, "OK"

    def validate_write_file(
        self, host_name: str, path: str, content_base64: str
    ) -> tuple[bool, str]:
        """Validate a structured /ssh/write_file request (host, path, content).

        Returns (is_valid, reason) — same signaling shape as
        validate_command()/validate_cwd().

        Host allowlist: reuses the identical membership check
        validate_command() performs (`host_name not in self.config.hosts`).
        There is no separate host-allowlist function in this module to call
        into — that one-line dict-membership test *is* the host-allowlist
        check everywhere in this class (validate_command() above and
        execute() below both inline the same test) — so it is reproduced
        verbatim here rather than factored out, to avoid touching
        validate_command() itself.

        Path-traversal safety: proven via PURE lexical normalization
        (posixpath.normpath), never os.path.realpath()/Path.resolve(). The
        destination path lives on the remote SSH target host, not on this
        gateway process's local disk, so there is nothing to stat locally —
        realpath()/resolve() would either raise (path doesn't exist on this
        machine) or resolve against the wrong filesystem entirely. Instead,
        posixpath.normpath collapses '..'/'.' segments lexically (e.g.
        "/a/b/../../etc" -> "/etc"), and we require the collapsed result to
        still be prefixed by _ALLOWED_WRITE_ROOT.
        """
        if host_name not in self.config.hosts:
            return False, f"Unknown host: {host_name}"

        if not path or not path.strip():
            return False, "Empty path"

        if "\x00" in path:
            return False, "Path contains a null byte"

        candidate = path if path.startswith("/") else f"{_ALLOWED_WRITE_ROOT}/{path}"
        normalized = posixpath.normpath(candidate)

        if not normalized.startswith(_ALLOWED_WRITE_PARENT + "/"):
            return False, f"Path escapes allowed root {_ALLOWED_WRITE_ROOT}: {path}"

        # Top-level directory directly under _ALLOWED_WRITE_PARENT must exactly
        # match the primary checkout or its git-worktree naming convention —
        # an EXACT regex match on the first path segment only, never a prefix
        # test (a bare `.startswith("agentshroud")` would let a sibling like
        # "agentshroud-evil" slip through, since that string also starts with
        # "agentshroud").
        rel = normalized[len(_ALLOWED_WRITE_PARENT) + 1 :]
        top_level, _, remainder = rel.partition("/")
        if not _ALLOWED_WRITE_TOP_LEVEL_RE.match(top_level):
            return False, f"Path escapes allowed root {_ALLOWED_WRITE_ROOT}: {path}"

        if not remainder:
            return (
                False,
                "Path must reference a file inside the checkout, not the checkout root itself",
            )

        try:
            decoded_len = len(base64.b64decode(content_base64, validate=True))
        except (binascii.Error, ValueError):
            return False, "content_base64 is not valid base64"

        if decoded_len > _MAX_WRITE_FILE_BYTES:
            return (
                False,
                f"Content exceeds maximum size of {_MAX_WRITE_FILE_BYTES} bytes "
                f"(decoded size: {decoded_len})",
            )

        return True, "OK"

    async def write_file(
        self,
        host_name: str,
        path: str,
        content_base64: str,
        timeout: int | None = None,
    ) -> SSHWriteResult:
        """Write file content to a remote host via structured (non-shell-string) transport.

        Mirrors execute()'s SSH transport (same ssh_args construction via
        asyncio.create_subprocess_exec) but the remote command is FIXED
        (see _REMOTE_WRITE_FILE_SCRIPT_B64) and both `path` and the decoded
        file content travel as DATA over the subprocess's stdin pipe —
        neither is ever concatenated into the remote command string. Caller
        is expected to have already called validate_write_file().
        """
        if host_name not in self.config.hosts:
            raise ValueError(f"Unknown host: {host_name}")

        host = self.config.hosts[host_name]
        effective_timeout = timeout or host.max_session_seconds

        ssh_args = [
            "ssh",
            "-o",
            "StrictHostKeyChecking=yes",
            "-o",
            "BatchMode=yes",
        ]
        if host.known_hosts_file:
            ssh_args.extend(["-o", f"UserKnownHostsFile={host.known_hosts_file}"])
        ssh_args.extend(["-p", str(host.port)])
        if host.key_path:
            ssh_args.extend(["-i", host.key_path])
        ssh_args.append(f"{host.username}@{host.host}")
        # Fixed, non-interpolated remote command: the base64 blob is the
        # module-level constant computed from _REMOTE_WRITE_FILE_SCRIPT at
        # import time, never from `path` or `content_base64`.
        remote_command = (
            'python3 -c "import base64,sys;exec(base64.b64decode('
            f"'{_REMOTE_WRITE_FILE_SCRIPT_B64}'))\""
        )
        ssh_args.append(remote_command)

        # path and content are sent as DATA on stdin, not as argv/command
        # text — shell metacharacters in either are inert here.
        stdin_payload = (
            base64.b64encode(path.encode("utf-8")) + b"\n" + content_base64.encode("ascii")
        )

        start = time.monotonic()
        try:
            proc = await asyncio.create_subprocess_exec(
                *ssh_args,
                stdin=asyncio.subprocess.PIPE,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
            )
            try:
                stdout_bytes, stderr_bytes = await asyncio.wait_for(
                    proc.communicate(input=stdin_payload), timeout=effective_timeout
                )
            except asyncio.TimeoutError:
                proc.kill()
                await proc.wait()
                duration = time.monotonic() - start
                return SSHWriteResult(
                    host=host_name,
                    path=path,
                    bytes_written=0,
                    stdout="",
                    stderr=f"Timeout: write exceeded {effective_timeout}s",
                    exit_code=-1,
                    duration_seconds=duration,
                )

            duration = time.monotonic() - start
            stdout_text = stdout_bytes.decode("utf-8", errors="replace")
            exit_code = proc.returncode if proc.returncode is not None else -1
            bytes_written = 0
            if exit_code == 0:
                try:
                    bytes_written = int(stdout_text.strip())
                except ValueError:
                    bytes_written = 0
            return SSHWriteResult(
                host=host_name,
                path=path,
                bytes_written=bytes_written,
                stdout=stdout_text,
                stderr=stderr_bytes.decode("utf-8", errors="replace"),
                exit_code=exit_code,
                duration_seconds=duration,
            )
        except OSError as e:
            duration = time.monotonic() - start
            return SSHWriteResult(
                host=host_name,
                path=path,
                bytes_written=0,
                stdout="",
                stderr=str(e),
                exit_code=-1,
                duration_seconds=duration,
            )
        except asyncio.CancelledError:
            duration = time.monotonic() - start
            return SSHWriteResult(
                host=host_name,
                path=path,
                bytes_written=0,
                stdout="",
                stderr="Cancelled",
                exit_code=-1,
                duration_seconds=duration,
            )

    async def execute(
        self, host_name: str, command: str, timeout: int | None = None, cwd: str | None = None
    ) -> SSHResult:
        """Execute a command on a remote host via SSH."""
        if host_name not in self.config.hosts:
            raise ValueError(f"Unknown host: {host_name}")

        host = self.config.hosts[host_name]
        effective_timeout = timeout or host.max_session_seconds

        # Build SSH command — reject unknown host keys for security
        ssh_args = [
            "ssh",
            "-o",
            "StrictHostKeyChecking=yes",
            "-o",
            "BatchMode=yes",
        ]
        if host.known_hosts_file:
            ssh_args.extend(["-o", f"UserKnownHostsFile={host.known_hosts_file}"])
        ssh_args.extend(["-p", str(host.port)])
        if host.key_path:
            ssh_args.extend(["-i", host.key_path])
        ssh_args.append(f"{host.username}@{host.host}")
        remote_command = f"cd {cwd} && {command}" if cwd else command
        ssh_args.append(remote_command)

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
                    stdout="",
                    stderr=f"Timeout: command exceeded {effective_timeout}s",
                    exit_code=-1,
                    duration_seconds=duration,
                    host=host_name,
                    command=command,
                )

            duration = time.monotonic() - start
            return SSHResult(
                stdout=stdout_bytes.decode("utf-8", errors="replace"),
                stderr=stderr_bytes.decode("utf-8", errors="replace"),
                exit_code=proc.returncode or 0,
                duration_seconds=duration,
                host=host_name,
                command=command,
            )
        except OSError as e:
            duration = time.monotonic() - start
            return SSHResult(
                stdout="",
                stderr=str(e),
                exit_code=-1,
                duration_seconds=duration,
                host=host_name,
                command=command,
            )
        except asyncio.CancelledError:
            duration = time.monotonic() - start
            return SSHResult(
                stdout="",
                stderr="Cancelled",
                exit_code=-1,
                duration_seconds=duration,
                host=host_name,
                command=command,
            )
