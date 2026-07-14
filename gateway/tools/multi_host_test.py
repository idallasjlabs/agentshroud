# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""
Multi-Host Test Runner — run a command across lab hosts and aggregate results.

SCRUM-91 (part 1 of 2): run the repo test/smoke command (or any command) on
each lab host over SSH, collect per-host exit codes plus a short output tail,
and print an aggregated PASS/FAIL summary. The overall exit code is non-zero if
ANY host failed or was unreachable — so a change can be validated on every
runtime (x86/arm, differing container state) before a coordinated deploy.

Design notes:
    * The per-host executor is injectable (``runner`` argument). Production wires
      it to SSH; tests inject a fake so no real network is touched.
    * ``--dry-run`` prints the plan and touches nothing (no runner is called).
    * Unreachable hosts are marked UNREACHABLE and do NOT abort the run; the
      other hosts still execute.

The coordinated multi-host DEPLOY (rolling apply + health-gated promotion) is a
separate, larger follow-up and is intentionally NOT implemented here.

Usage (library):
    from gateway.tools.multi_host_test import run_multi_host, DEFAULT_HOSTS
    result = run_multi_host(DEFAULT_HOSTS, "bash scripts/smoke.sh", runner=my_runner)
    print(result.render_summary())
    sys.exit(result.exit_code)

Usage (CLI, via scripts/multi-host-test.sh):
    python -m gateway.tools.multi_host_test --hosts marvin,trillian -- bash scripts/smoke.sh
"""

import argparse
import shlex
import subprocess  # nosec B404 - used only to invoke ssh with a fixed, non-shell argv
import sys
from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Optional, Sequence

# Default lab host inventory (see docker/config/ssh/config for canonical entries).
# These are SSH host aliases resolvable as `agentshroud-bot@<host>` — NOT secrets.
DEFAULT_HOSTS: tuple[str, ...] = ("marvin", "trillian", "raspberrypi")

# Default remote user and command, overridable from the CLI / wrapper.
DEFAULT_USER = "agentshroud-bot"
DEFAULT_COMMAND = "bash scripts/smoke.sh"

# Sentinel exit code used when a host cannot be reached (SSH connect failure).
# 255 is what OpenSSH itself returns on connection errors, so we reuse it.
UNREACHABLE_EXIT = 255

# How many trailing lines of remote output to keep per host in the summary.
DEFAULT_TAIL_LINES = 5


class HostStatus(str, Enum):
    """Outcome classification for a single host."""

    PASS = "PASS"
    FAIL = "FAIL"
    UNREACHABLE = "UNREACHABLE"


@dataclass
class HostResult:
    """Result of running the command on a single host."""

    host: str
    status: HostStatus
    exit_code: int
    output_tail: str = ""

    @property
    def ok(self) -> bool:
        """True only when the host ran the command and it exited 0."""
        return self.status is HostStatus.PASS


# A runner takes (host, command) and returns (exit_code, combined_output).
# An exit code of UNREACHABLE_EXIT signals an SSH connection failure.
HostRunner = Callable[[str, str], tuple[int, str]]


def parse_hosts(raw: Optional[str], default: Sequence[str] = DEFAULT_HOSTS) -> list[str]:
    """Parse a comma/whitespace-separated host list into a de-duplicated list.

    Empty/None falls back to ``default``. Order is preserved; duplicates are
    dropped (first occurrence wins). Whitespace around each entry is stripped.
    """
    if raw is None or not raw.strip():
        return list(default)
    # Allow both commas and whitespace as separators.
    tokens = [t.strip() for t in raw.replace(",", " ").split()]
    seen: set[str] = set()
    hosts: list[str] = []
    for tok in tokens:
        if tok and tok not in seen:
            seen.add(tok)
            hosts.append(tok)
    return hosts or list(default)


def tail(text: str, lines: int = DEFAULT_TAIL_LINES) -> str:
    """Return the last ``lines`` non-trailing-empty lines of ``text``."""
    if not text:
        return ""
    stripped = text.rstrip("\n")
    if not stripped:
        return ""
    return "\n".join(stripped.splitlines()[-lines:])


def classify(exit_code: int) -> HostStatus:
    """Map a runner exit code to a HostStatus."""
    if exit_code == UNREACHABLE_EXIT:
        return HostStatus.UNREACHABLE
    return HostStatus.PASS if exit_code == 0 else HostStatus.FAIL


@dataclass
class MultiHostResult:
    """Aggregated outcome across all hosts."""

    results: list[HostResult] = field(default_factory=list)

    @property
    def passed(self) -> list[HostResult]:
        return [r for r in self.results if r.status is HostStatus.PASS]

    @property
    def failed(self) -> list[HostResult]:
        return [r for r in self.results if r.status is HostStatus.FAIL]

    @property
    def unreachable(self) -> list[HostResult]:
        return [r for r in self.results if r.status is HostStatus.UNREACHABLE]

    @property
    def all_ok(self) -> bool:
        """True only if every host passed (none failed or unreachable)."""
        return bool(self.results) and all(r.ok for r in self.results)

    @property
    def exit_code(self) -> int:
        """0 iff all hosts passed; 1 otherwise (incl. empty / any unreachable)."""
        return 0 if self.all_ok else 1

    def render_summary(self) -> str:
        """Render an aligned PASS/FAIL table plus a totals line."""
        header_host = "HOST"
        header_status = "STATUS"
        header_exit = "EXIT"
        host_w = max([len(header_host), *(len(r.host) for r in self.results)] or [len(header_host)])
        status_w = max(len(header_status), len(HostStatus.UNREACHABLE.value))

        lines = []
        lines.append("╔" + "═" * 54 + "╗")
        lines.append("║  AgentShroud™ — Multi-Host Test Results" + " " * 14 + "║")
        lines.append("╚" + "═" * 54 + "╝")
        lines.append(f"{header_host:<{host_w}}  {header_status:<{status_w}}  {header_exit}")
        lines.append("-" * (host_w + status_w + 10))
        for r in self.results:
            lines.append(f"{r.host:<{host_w}}  {r.status.value:<{status_w}}  {r.exit_code}")
        lines.append("-" * (host_w + status_w + 10))
        total = len(self.results)
        lines.append(
            f"Hosts: {total}  "
            f"Passed: {len(self.passed)}  "
            f"Failed: {len(self.failed)}  "
            f"Unreachable: {len(self.unreachable)}"
        )
        lines.append("OVERALL: " + ("PASS" if self.all_ok else "FAIL"))
        return "\n".join(lines)


def run_multi_host(
    hosts: Sequence[str],
    command: str,
    runner: HostRunner,
    tail_lines: int = DEFAULT_TAIL_LINES,
    on_host: Optional[Callable[[HostResult], None]] = None,
) -> MultiHostResult:
    """Run ``command`` on each host via ``runner`` and aggregate the results.

    A runner raising an exception is treated as UNREACHABLE for that host so a
    single flaky host never aborts the whole sweep. ``on_host`` (optional) is
    invoked with each HostResult as it completes, for live progress output.
    """
    agg = MultiHostResult()
    for host in hosts:
        try:
            exit_code, output = runner(host, command)
        except Exception as exc:  # noqa: BLE001 - any runner failure = unreachable
            exit_code, output = UNREACHABLE_EXIT, f"runner error: {exc}"
        status = classify(exit_code)
        result = HostResult(
            host=host,
            status=status,
            exit_code=exit_code,
            output_tail=tail(output, tail_lines),
        )
        agg.results.append(result)
        if on_host is not None:
            on_host(result)
    return agg


def build_ssh_argv(host: str, command: str, user: str = DEFAULT_USER) -> list[str]:
    """Build the ssh argv for a host. Non-interactive, fail-fast on connect.

    ``BatchMode=yes`` ensures ssh never blocks on a password prompt (returns
    an error instead), and ``ConnectTimeout`` bounds unreachable hosts.
    """
    return [
        "ssh",
        "-o",
        "BatchMode=yes",
        "-o",
        "ConnectTimeout=10",
        "-o",
        "StrictHostKeyChecking=accept-new",
        f"{user}@{host}",
        command,
    ]


def ssh_runner(user: str = DEFAULT_USER) -> HostRunner:
    """Return a HostRunner that executes the command on the host over SSH.

    SSH connection failures surface as OpenSSH's own exit code 255, which
    ``classify`` maps to UNREACHABLE. Command failures surface as the remote
    command's exit code.
    """

    def _run(host: str, command: str) -> tuple[int, str]:
        argv = build_ssh_argv(host, command, user=user)
        proc = subprocess.run(  # nosec B603 - fixed argv, no shell, host from allowlist
            argv,
            capture_output=True,
            text=True,
            check=False,
        )
        return proc.returncode, (proc.stdout or "") + (proc.stderr or "")

    return _run


def _dry_run_report(hosts: Sequence[str], command: str, user: str) -> str:
    """Describe exactly what would run, without executing anything."""
    lines = ["[DRY RUN] Multi-host test plan (nothing executed):"]
    lines.append(f"  command : {command}")
    lines.append(f"  user    : {user}")
    lines.append(f"  hosts   : {', '.join(hosts)}")
    for host in hosts:
        argv = build_ssh_argv(host, command, user=user)
        lines.append("    " + " ".join(shlex.quote(a) for a in argv))
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="multi_host_test",
        description="Run a command across lab hosts over SSH and aggregate results.",
    )
    parser.add_argument(
        "--hosts",
        default=None,
        help="Comma/space-separated host list (default: %s)" % ",".join(DEFAULT_HOSTS),
    )
    parser.add_argument(
        "--user",
        default=DEFAULT_USER,
        help="Remote SSH user (default: %(default)s)",
    )
    parser.add_argument(
        "--tail-lines",
        type=int,
        default=DEFAULT_TAIL_LINES,
        help="Trailing output lines to show per host (default: %(default)s)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the plan and exit 0 without touching any host.",
    )
    parser.add_argument(
        "command",
        nargs=argparse.REMAINDER,
        help="Command to run on each host (after `--`). Defaults to the smoke suite.",
    )
    return parser


def _resolve_command(tokens: list[str]) -> str:
    """Turn argparse REMAINDER tokens into a command string.

    Drops a leading ``--`` separator if argparse retained it. Falls back to the
    default smoke command when nothing is supplied.
    """
    if tokens and tokens[0] == "--":
        tokens = tokens[1:]
    if not tokens:
        return DEFAULT_COMMAND
    # Preserve the exact tokens the user passed after `--`.
    return " ".join(tokens)


def main(argv: Optional[Sequence[str]] = None, runner: Optional[HostRunner] = None) -> int:
    """CLI entry point. Returns the aggregated exit code (0 = all passed)."""
    args = build_parser().parse_args(list(argv) if argv is not None else None)
    hosts = parse_hosts(args.hosts)
    command = _resolve_command(list(args.command))

    if args.dry_run:
        print(_dry_run_report(hosts, command, args.user))
        return 0

    active_runner = runner if runner is not None else ssh_runner(user=args.user)

    def _progress(result: HostResult) -> None:
        print(f"  [{result.status.value}] {result.host} (exit {result.exit_code})")
        if result.output_tail:
            for line in result.output_tail.splitlines():
                print(f"      {line}")

    print(f"Running on {len(hosts)} host(s): {', '.join(hosts)}")
    print(f"Command: {command}\n")
    result = run_multi_host(
        hosts, command, active_runner, tail_lines=args.tail_lines, on_host=_progress
    )
    print("\n" + result.render_summary())
    return result.exit_code


if __name__ == "__main__":  # pragma: no cover - exercised via subprocess in tests
    sys.exit(main())
