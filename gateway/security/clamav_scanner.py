# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""ClamAV antivirus scanner integration.

Runs clamscan/freshclam as local binaries and parses output.
"""


import logging
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

DEFAULT_LOG_DIR = Path("/var/log/security/clamav")


def update_virus_db(freshclam_bin: str = "freshclam", timeout: int = 300) -> dict[str, Any]:
    """Update ClamAV virus database using freshclam.

    Args:
        freshclam_bin: Path to freshclam binary.
        timeout: Command timeout in seconds.

    Returns:
        Dict with update status.
    """
    cmd = [freshclam_bin, "--no-warnings"]
    logger.info("Updating ClamAV virus database")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return {"status": "error", "error": "timeout"}
    except FileNotFoundError:
        return {"status": "error", "error": "binary_not_found"}

    return {
        "status": "ok" if result.returncode == 0 else "warning",
        "output": result.stdout[:1000],
        "returncode": result.returncode,
    }


def run_clamscan(
    target: str = "/home",
    recursive: bool = True,
    timeout: int = 600,
    clamscan_bin: str = "clamscan",
    exclude_patterns: list[str] | None = None,
) -> dict[str, Any]:
    """Run ClamAV scan and return parsed results.

    Args:
        target: Directory or file to scan.
        recursive: Scan directories recursively.
        timeout: Command timeout in seconds.
        clamscan_bin: Path to clamscan binary.
        exclude_patterns: List of regex patterns to exclude.

    Returns:
        Parsed scan results dict.
    """
    cmd = [clamscan_bin, "--no-summary"]
    if recursive:
        cmd.append("-r")
    if exclude_patterns:
        for pat in exclude_patterns:
            cmd.extend(["--exclude", pat])
    cmd.append(target)

    logger.info("Running ClamAV scan on: %s", target)

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return {"error": "timeout", "scanner": "clamav"}
    except FileNotFoundError:
        return {"error": "binary_not_found", "scanner": "clamav"}

    return parse_clamscan_output(result.stdout, result.returncode)


def parse_clamscan_output(output: str, returncode: int = 0) -> dict[str, Any]:
    """Parse clamscan output into structured results.

    Args:
        output: Raw stdout from clamscan.
        returncode: Process return code (0=clean, 1=infected found).

    Returns:
        Structured results dict.
    """
    infected_files: list[dict[str, str]] = []
    scanned_files = 0
    errors = 0

    for line in output.strip().splitlines():
        line = line.strip()
        if not line:
            continue

        # Infected file: /path/to/file: Eicar-Signature FOUND
        match = re.match(r"^(.+?):\s+(.+?)\s+FOUND$", line)
        if match:
            infected_files.append(
                {
                    "file": match.group(1),
                    "signature": match.group(2),
                }
            )
            continue

        # OK lines
        if line.endswith(": OK"):
            scanned_files += 1
            continue

        # Error lines
        if "ERROR" in line or "WARNING" in line:
            errors += 1

    # Also count infected as scanned
    scanned_files += len(infected_files)

    return {
        "scanner": "clamav",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "scanned_files": scanned_files,
        "infected_files": infected_files,
        "infected_count": len(infected_files),
        "errors": errors,
        "returncode": returncode,
        "error": None,
    }


def save_report(report: dict[str, Any], log_dir: Path = DEFAULT_LOG_DIR) -> Path:
    """Save a ClamAV report to the log directory."""
    import json

    log_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    path = log_dir / f"clamav-{ts}.json"
    path.write_text(json.dumps(report, indent=2))
    logger.info("ClamAV report saved to %s", path)
    return path


async def scan_bytes(data: bytes, timeout: int = 30) -> dict[str, Any]:
    """Stream bytes to clamdscan for inline malware scanning.

    Uses ``clamdscan --stream -`` which pipes stdin directly to the running
    clamd daemon socket — no temp file required, safe for untrusted data.

    Fail mode: if clamd is unavailable or times out, returns error with
    infected_count=0 so the caller can choose fail-open (log + allow).

    Args:
        data: Raw bytes to scan (decoded base64, file content, etc.).
        timeout: Maximum seconds to wait for clamdscan.

    Returns:
        Parsed scan result dict, always includes ``infected_count`` key.
    """
    import asyncio

    if not data:
        return {"scanner": "clamav", "infected_count": 0, "scanned_bytes": 0, "error": None}

    try:
        proc = await asyncio.create_subprocess_exec(
            "clamdscan",
            "--stream",
            "--no-summary",
            "-",
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, _ = await asyncio.wait_for(proc.communicate(input=data), timeout=timeout)
        output = stdout.decode("utf-8", errors="replace")
        result = parse_clamscan_output(output, proc.returncode)
        result["scanned_bytes"] = len(data)
        return result
    except asyncio.TimeoutError:
        logger.warning("ClamAV scan_bytes timed out after %ds", timeout)
        return {
            "scanner": "clamav",
            "infected_count": 0,
            "error": "timeout",
            "scanned_bytes": len(data),
        }
    except FileNotFoundError:
        return {
            "scanner": "clamav",
            "infected_count": 0,
            "error": "binary_not_found",
            "scanned_bytes": len(data),
        }
    except Exception as exc:
        logger.error("ClamAV scan_bytes error: %s", exc)
        return {
            "scanner": "clamav",
            "infected_count": 0,
            "error": str(exc),
            "scanned_bytes": len(data),
        }


def generate_summary(report: dict[str, Any]) -> dict[str, Any]:
    """Generate a summary dict suitable for the health report.

    Args:
        report: Parsed ClamAV report.

    Returns:
        Summary dict.
    """
    if report.get("error"):
        return {
            "tool": "clamav",
            "status": "error",
            "error": report["error"],
            "findings": 0,
            "critical": 0,
            "high": 0,
        }

    infected = report.get("infected_count", 0)
    status = "critical" if infected > 0 else "clean"

    return {
        "tool": "clamav",
        "status": status,
        "findings": infected,
        "critical": infected,  # All malware is critical
        "high": 0,
        "medium": 0,
        "low": 0,
        "scanned_files": report.get("scanned_files", 0),
        "infected_files": [f["file"] for f in report.get("infected_files", [])],
        "signatures": [f["signature"] for f in report.get("infected_files", [])],
        "timestamp": report.get("timestamp"),
    }
