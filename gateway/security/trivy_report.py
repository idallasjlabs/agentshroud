"""Trivy vulnerability scanner integration.

Runs trivy as a local binary (not docker run) and parses JSON output.
"""

import json
import logging
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

SEVERITY_ORDER = ["CRITICAL", "HIGH", "MEDIUM", "LOW", "UNKNOWN"]

DEFAULT_LOG_DIR = Path("/var/log/security/trivy")


def run_trivy_scan(
    target: str = "/",
    scan_type: str = "fs",
    severity: str = "CRITICAL,HIGH,MEDIUM,LOW",
    timeout: int = 600,
    trivy_bin: str = "trivy",
) -> dict[str, Any]:
    """Run a Trivy scan and return parsed results.

    Args:
        target: Scan target (filesystem path or image name).
        scan_type: Trivy scan type (fs, image, rootfs, repo).
        severity: Comma-separated severity filter.
        timeout: Command timeout in seconds.
        trivy_bin: Path to trivy binary.

    Returns:
        Parsed scan results dict.
    """
    cmd = [
        trivy_bin,
        scan_type,
        "--format", "json",
        "--severity", severity,
        "--no-progress",
        "--timeout", f"{timeout}s",
        target,
    ]

    logger.info("Running Trivy scan: %s", " ".join(cmd))

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout + 30,
        )
    except subprocess.TimeoutExpired:
        logger.error("Trivy scan timed out after %ds", timeout)
        return {"error": "timeout", "raw_output": ""}
    except FileNotFoundError:
        logger.error("Trivy binary not found at: %s", trivy_bin)
        return {"error": "binary_not_found", "raw_output": ""}

    if result.returncode not in (0, 1):
        # returncode 1 = vulns found (expected)
        logger.warning("Trivy exited with code %d: %s", result.returncode, result.stderr[:500])

    try:
        raw = json.loads(result.stdout) if result.stdout.strip() else {}
    except json.JSONDecodeError:
        logger.error("Failed to parse Trivy JSON output")
        return {"error": "parse_error", "raw_output": result.stdout[:2000]}

    return parse_trivy_output(raw)


def parse_trivy_output(raw: dict[str, Any]) -> dict[str, Any]:
    """Parse raw Trivy JSON output into a structured summary.

    Args:
        raw: Raw JSON output from trivy.

    Returns:
        Structured summary with vulnerability counts, top CVEs, etc.
    """
    vulns_by_severity: dict[str, int] = {s: 0 for s in SEVERITY_ORDER}
    top_cves: list[dict[str, Any]] = []
    affected_packages: set[str] = set()
    all_vulns: list[dict[str, Any]] = []

    results = raw.get("Results", [])
    for result in results:
        target_name = result.get("Target", "unknown")
        for vuln in result.get("Vulnerabilities", []):
            sev = vuln.get("Severity", "UNKNOWN").upper()
            if sev in vulns_by_severity:
                vulns_by_severity[sev] += 1
            else:
                vulns_by_severity["UNKNOWN"] += 1

            pkg = vuln.get("PkgName", "unknown")
            affected_packages.add(pkg)

            entry = {
                "id": vuln.get("VulnerabilityID", ""),
                "severity": sev,
                "package": pkg,
                "installed_version": vuln.get("InstalledVersion", ""),
                "fixed_version": vuln.get("FixedVersion", ""),
                "title": vuln.get("Title", ""),
                "target": target_name,
            }
            all_vulns.append(entry)

    # Sort by severity, take top 20
    severity_rank = {s: i for i, s in enumerate(SEVERITY_ORDER)}
    all_vulns.sort(key=lambda v: severity_rank.get(v["severity"], 99))
    top_cves = all_vulns[:20]

    total = sum(vulns_by_severity.values())

    return {
        "scanner": "trivy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "total_vulnerabilities": total,
        "by_severity": vulns_by_severity,
        "top_cves": top_cves,
        "affected_packages": sorted(affected_packages),
        "affected_package_count": len(affected_packages),
        "error": None,
    }


def save_report(report: dict[str, Any], log_dir: Path = DEFAULT_LOG_DIR) -> Path:
    """Save a Trivy report to the log directory.

    Args:
        report: Parsed report dict.
        log_dir: Directory to save reports.

    Returns:
        Path to saved report file.
    """
    log_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    path = log_dir / f"trivy-{ts}.json"
    path.write_text(json.dumps(report, indent=2))
    logger.info("Trivy report saved to %s", path)
    return path


def generate_summary(report: dict[str, Any]) -> dict[str, Any]:
    """Generate a summary dict suitable for the health report.

    Args:
        report: Parsed Trivy report.

    Returns:
        Summary dict with tool name, status, findings count, details.
    """
    if report.get("error"):
        return {
            "tool": "trivy",
            "status": "error",
            "error": report["error"],
            "findings": 0,
            "critical": 0,
            "high": 0,
        }

    by_sev = report.get("by_severity", {})
    critical = by_sev.get("CRITICAL", 0)
    high = by_sev.get("HIGH", 0)

    if critical > 0:
        status = "critical"
    elif high > 0:
        status = "warning"
    else:
        status = "clean"

    return {
        "tool": "trivy",
        "status": status,
        "findings": report.get("total_vulnerabilities", 0),
        "critical": critical,
        "high": high,
        "medium": by_sev.get("MEDIUM", 0),
        "low": by_sev.get("LOW", 0),
        "affected_packages": report.get("affected_package_count", 0),
        "top_cves": [c["id"] for c in report.get("top_cves", [])[:5]],
        "timestamp": report.get("timestamp"),
    }
