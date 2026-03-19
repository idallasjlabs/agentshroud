# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
# Protected by common law trademark rights. Federal trademark registration pending.
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Unified scanner result aggregation for SOC.

Aggregates results from all security scanners:
  - Trivy (vulnerability scanning)
  - Falco (runtime detection)
  - ClamAV (malware defense)
  - Wazuh (HIDS / FIM)
  - OpenSCAP (compliance auditing)

Also computes the Container Security Scorecard (12 domains, 0-5 maturity scale)
based on CIS Docker Benchmark v1.6.0, NIST SP 800-190, DISA STIGs, and IEC 62443.
"""

import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

# Report directories — shared volumes mounted into gateway container
_TRIVY_REPORT_DIR = Path("/var/log/security/trivy")
_CLAMAV_REPORT_DIR = Path("/var/log/security/clamav")
_FALCO_ALERT_DIR = Path("/var/log/falco")
_WAZUH_ALERT_DIR = Path("/var/ossec/logs/alerts")
_OPENSCAP_REPORT_DIR = Path("/var/log/security/openscap")
_SBOM_REPORT_DIR = Path("/var/log/security/sbom")

# Maturity scale labels (0-5)
_MATURITY_LABELS: Dict[int, str] = {
    0: "Not Started",
    1: "Initial",
    2: "Managed",
    3: "Defined",
    4: "Measured",
    5: "Optimizing",
}

# Scorecard domain metadata (12 domains, IEC 62443 aligned)
_SCORECARD_DOMAINS: List[Dict[str, Any]] = [
    {
        "id": 1,
        "domain": "Image Integrity",
        "description": "Ensures container images are signed and tamper-proof before deployment. Prevents supply-chain attacks by verifying cryptographic signatures on every image pull.",
        "standard_ref": "NIST 800-190 §4.2, CIS 4.x",
        "tools": ["cosign", "trivy"],
        "iec_fr": "FR3",
    },
    {
        "id": 2,
        "domain": "Vulnerability Management",
        "description": "Continuously scans container images and OS packages for known CVEs. Tracks severity trends and enforces remediation SLAs to reduce exploitable attack surface.",
        "standard_ref": "NIST 800-190 §4.2, CIS 4.4",
        "tools": ["trivy"],
        "iec_fr": "FR3",
    },
    {
        "id": 3,
        "domain": "Supply Chain",
        "description": "Generates and validates a Software Bill of Materials (SBOM) for every build artifact. Verifies provenance and detects unauthorized or unexpected third-party dependencies.",
        "standard_ref": "IEC 62443 4-1 SDL, EO 14028",
        "tools": ["syft", "cosign"],
        "iec_fr": "FR3, SDL 4-1",
    },
    {
        "id": 4,
        "domain": "Container Hardening",
        "description": "Benchmarks container configuration against CIS Docker and DISA STIG baselines. Checks for root-user processes, unnecessary capabilities, writable filesystems, and unsafe mounts.",
        "standard_ref": "CIS 5.x, DISA STIG",
        "tools": ["openscap"],
        "iec_fr": "FR3",
    },
    {
        "id": 5,
        "domain": "Runtime Protection",
        "description": "Monitors live container behavior for anomalous syscalls, privilege escalation attempts, and policy violations. Triggers real-time alerts on suspicious activity at the kernel level.",
        "standard_ref": "NIST 800-190 §4.6, IEC FR3",
        "tools": ["falco"],
        "iec_fr": "FR3, FR6",
    },
    {
        "id": 6,
        "domain": "Malware Defense",
        "description": "Scans container filesystems and mounted volumes for known malware signatures, trojans, and rootkits using ClamAV. Detects malicious payloads that may enter through third-party packages.",
        "standard_ref": "IEC FR3 SR 3.2",
        "tools": ["clamav"],
        "iec_fr": "FR3",
    },
    {
        "id": 7,
        "domain": "Network Segmentation",
        "description": "Validates that Docker networks enforce least-privilege connectivity between containers. Ensures sensitive services are isolated from internet-facing components and bot workloads.",
        "standard_ref": "NIST 800-190 §4.5, IEC FR5",
        "tools": ["docker_networks"],
        "iec_fr": "FR5",
    },
    {
        "id": 8,
        "domain": "Secrets Management",
        "description": "Audits how credentials, API keys, and tokens are stored and rotated. Checks for hardcoded secrets in images, unencrypted env vars, and compliance with vault-based secret injection.",
        "standard_ref": "NIST 800-190 §4.3, IEC FR4",
        "tools": ["key_vault", "key_rotation"],
        "iec_fr": "FR4",
    },
    {
        "id": 9,
        "domain": "Logging & Monitoring",
        "description": "Verifies that all containers emit structured logs to a central aggregator and that alerting pipelines are active. Ensures audit trails are complete and tamper-evident.",
        "standard_ref": "NIST 800-190 §4.7, IEC FR6",
        "tools": ["fluent_bit", "wazuh"],
        "iec_fr": "FR6",
    },
    {
        "id": 10,
        "domain": "Compliance Auditing",
        "description": "Runs automated compliance checks against CIS, DISA STIG, and IEC 62443 control baselines. Produces audit-ready evidence of control implementation and identifies gaps requiring remediation.",
        "standard_ref": "CIS, DISA STIG, IEC FR7",
        "tools": ["openscap"],
        "iec_fr": "FR7",
    },
    {
        "id": 11,
        "domain": "Secure Development",
        "description": "Enforces secure coding practices through static analysis of application source code and Dockerfiles. Detects injection flaws, insecure defaults, and misconfigurations before they reach production.",
        "standard_ref": "IEC 62443 4-1, NIST SSDF",
        "tools": ["semgrep", "trivy"],
        "iec_fr": "SDL 4-1",
    },
    {
        "id": 12,
        "domain": "Incident Response",
        "description": "Measures readiness to detect, contain, and recover from security incidents. Validates that runbooks exist, alert-to-response pipelines are tested, and forensic evidence is preserved.",
        "standard_ref": "NIST 800-190 §4.8, IEC FR6",
        "tools": ["falco", "wazuh", "soc"],
        "iec_fr": "FR6",
    },
]


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

def _load_latest_json(directory: Path, prefix: str = "") -> Optional[Dict[str, Any]]:
    """Load the most recent JSON report file from a directory.

    Args:
        directory: Directory to search.
        prefix: Optional filename prefix filter.

    Returns:
        Parsed JSON dict or None if not found.
    """
    if not directory.exists():
        return None
    pattern = f"{prefix}*.json" if prefix else "*.json"
    files = sorted(directory.glob(pattern), reverse=True)
    if not files:
        return None
    try:
        return json.loads(files[0].read_text())
    except Exception as exc:
        logger.warning("Failed to load report from %s: %s", files[0], exc)
        return None


# ---------------------------------------------------------------------------
# Per-scanner summary accessors
# ---------------------------------------------------------------------------

def get_trivy_summary() -> Dict[str, Any]:
    """Return latest Trivy scan summary from saved reports."""
    from .trivy_report import generate_summary
    report = _load_latest_json(_TRIVY_REPORT_DIR, "trivy-")
    if report is None:
        return {"tool": "trivy", "status": "not_run", "findings": 0, "critical": 0, "high": 0}
    return generate_summary(report)


def get_clamav_summary() -> Dict[str, Any]:
    """Return latest ClamAV scan summary from saved reports."""
    from .clamav_scanner import generate_summary
    report = _load_latest_json(_CLAMAV_REPORT_DIR, "clamav-")
    if report is None:
        return {"tool": "clamav", "status": "not_run", "findings": 0, "critical": 0, "high": 0}
    return generate_summary(report)


def get_falco_summary() -> Dict[str, Any]:
    """Return latest Falco alert summary from the shared alert volume."""
    from .falco_monitor import read_alerts, generate_summary
    if not _FALCO_ALERT_DIR.exists():
        return {"tool": "falco", "status": "not_run", "findings": 0, "critical": 0, "high": 0}
    alerts = read_alerts(alert_dir=_FALCO_ALERT_DIR)
    return generate_summary(alerts)


def get_wazuh_summary() -> Dict[str, Any]:
    """Return latest Wazuh alert summary from the shared alert volume."""
    from .wazuh_client import read_alerts, generate_summary
    if not _WAZUH_ALERT_DIR.exists():
        return {"tool": "wazuh", "status": "not_run", "findings": 0, "critical": 0, "high": 0}
    alerts = read_alerts(alert_dir=_WAZUH_ALERT_DIR)
    return generate_summary(alerts)


def get_openscap_summary() -> Dict[str, Any]:
    """Return latest OpenSCAP compliance summary from saved reports."""
    report = _load_latest_json(_OPENSCAP_REPORT_DIR, "openscap-")
    if report is None:
        return {
            "tool": "openscap",
            "status": "not_run",
            "findings": 0,
            "critical": 0,
            "high": 0,
            "pass_count": 0,
            "fail_count": 0,
        }
    pass_count = report.get("pass_count", 0)
    fail_count = report.get("fail_count", 0)
    critical = report.get("critical", 0)
    if critical > 0:
        status = "critical"
    elif fail_count > 0:
        status = "warning"
    else:
        status = "clean"
    return {
        "tool": "openscap",
        "status": status,
        "findings": fail_count,
        "critical": critical,
        "high": report.get("high", 0),
        "pass_count": pass_count,
        "fail_count": fail_count,
        "profile": report.get("profile", ""),
        "timestamp": report.get("timestamp"),
    }


def get_sbom() -> Optional[Dict[str, Any]]:
    """Return the latest SBOM (Software Bill of Materials) as parsed JSON."""
    if not _SBOM_REPORT_DIR.exists():
        return None
    files = sorted(_SBOM_REPORT_DIR.glob("sbom-*.json"), reverse=True)
    if not files:
        return None
    try:
        return json.loads(files[0].read_text())
    except Exception as exc:
        logger.warning("Failed to load SBOM: %s", exc)
        return None


# ---------------------------------------------------------------------------
# Aggregation
# ---------------------------------------------------------------------------

def aggregate_results() -> Dict[str, Any]:
    """Aggregate results from all security scanners into a unified dict.

    Returns:
        Dict with overall status, per-scanner summaries, and total counts.
    """
    summaries = [
        get_trivy_summary(),
        get_clamav_summary(),
        get_falco_summary(),
        get_wazuh_summary(),
        get_openscap_summary(),
    ]

    any_critical = any(s.get("critical", 0) > 0 for s in summaries)
    any_high = any(s.get("high", 0) > 0 for s in summaries)
    all_not_run = all(s.get("status") == "not_run" for s in summaries)

    if all_not_run:
        overall_status = "not_configured"
    elif any_critical:
        overall_status = "critical"
    elif any_high:
        overall_status = "warning"
    else:
        overall_status = "clean"

    return {
        "status": overall_status,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "scanners": {s["tool"]: s for s in summaries},
        "totals": {
            "critical": sum(s.get("critical", 0) for s in summaries),
            "high": sum(s.get("high", 0) for s in summaries),
            "medium": sum(s.get("medium", 0) for s in summaries),
            "low": sum(s.get("low", 0) for s in summaries),
        },
    }


# ---------------------------------------------------------------------------
# Scorecard domain scorers
# ---------------------------------------------------------------------------

def _score_image_integrity(trivy: Dict[str, Any]) -> int:
    """Score domain 1: Image Integrity (0-5)."""
    score = 0
    # SBOM exists in report dir → Syft has run
    if _SBOM_REPORT_DIR.exists() and any(_SBOM_REPORT_DIR.glob("sbom-*.json")):
        score += 1
    # Trivy has run and found no criticals
    if trivy.get("status") not in ("not_run", "error"):
        score += 1
    if trivy.get("critical", 0) == 0 and trivy.get("status") not in ("not_run", "error"):
        score += 1
    # Cap at 3 — cosign automated in CI would push to 4-5
    return min(score, 3)


def _score_vulnerability_management(trivy: Dict[str, Any]) -> int:
    """Score domain 2: Vulnerability Management (0-5)."""
    if trivy.get("status") in ("not_run",):
        # Trivy module code exists → Initial (1)
        return 1
    if trivy.get("error"):
        return 1
    if trivy.get("critical", 0) == 0 and trivy.get("high", 0) == 0:
        # Automated, no criticals → Defined (3)
        return 3
    if trivy.get("critical", 0) == 0:
        # Running but high vulns present → Managed (2)
        return 2
    # Has criticals → Initial (1)
    return 1


def _score_supply_chain() -> int:
    """Score domain 3: Supply Chain (0-5)."""
    if _SBOM_REPORT_DIR.exists() and any(_SBOM_REPORT_DIR.glob("sbom-*.json")):
        # SBOM generated → Managed (2)
        return 2
    # No SBOM → Not Started (0)
    return 0


def _score_container_hardening(openscap: Dict[str, Any]) -> int:
    """Score domain 4: Container Hardening (0-5).

    Baseline of 3 because docker-compose.yml enforces cap_drop ALL,
    no-new-privileges, read_only rootfs, seccomp profiles, and resource limits.
    """
    score = 3  # Compose-level hardening baseline
    if openscap.get("status") not in ("not_run",):
        score += 1  # OpenSCAP scanning adds Measured
    if openscap.get("fail_count", 1) == 0 and openscap.get("status") not in ("not_run",):
        score += 1  # All checks passing → Optimizing
    return min(score, 5)


def _score_runtime_protection(falco: Dict[str, Any]) -> int:
    """Score domain 5: Runtime Protection (0-5)."""
    if falco.get("status") == "not_run":
        # Module code exists → Initial (1)
        return 1
    if falco.get("critical", 0) > 0:
        # Falco running but active criticals → Managed (2)
        return 2
    # Falco running, no criticals → Defined (3)
    return 3


def _score_malware_defense(clamav: Dict[str, Any]) -> int:
    """Score domain 6: Malware Defense (0-5)."""
    if clamav.get("status") == "not_run":
        # Module code exists → Initial (1)
        return 1
    if clamav.get("critical", 0) > 0:
        # Infected files found → Initial (still wired but failing)
        return 1
    # ClamAV running, clean → Defined (3)
    return 3


def _score_network_segmentation() -> int:
    """Score domain 7: Network Segmentation (0-5).

    Three Docker bridge networks (internal, isolated, console) with proper
    isolation already implemented. network_validator.py provides runtime audit.
    Hardcoded Defined (3) — kernel-level enforcement deferred to post-v1.0.
    """
    return 3


def _score_secrets_management() -> int:
    """Score domain 8: Secrets Management (0-5).

    Docker secrets + key_vault.py + key_rotation.py = Managed (2).
    key_vault stores secrets in-memory (no encryption at rest).
    Ephemeral audit trail. Deferred to v1.0 for Vault or encrypted store.
    """
    return 2


def _score_logging_monitoring(wazuh: Dict[str, Any]) -> int:
    """Score domain 9: Logging & Monitoring (0-5)."""
    score = 1  # SOC dashboard exists
    if wazuh.get("status") != "not_run":
        score += 1  # Wazuh agent running
    # Fluent Bit config present in the container
    fluent_bit_paths = [
        Path("/fluent-bit/etc/fluent-bit.conf"),
        Path("/etc/fluent-bit/fluent-bit.conf"),
    ]
    if any(p.exists() for p in fluent_bit_paths):
        score += 1  # Fluent Bit forwarding configured
    return min(score, 3)


def _score_compliance_auditing(openscap: Dict[str, Any]) -> int:
    """Score domain 10: Compliance Auditing (0-5)."""
    if openscap.get("status") == "not_run":
        # No scanning → Not Started (0)
        return 0
    if openscap.get("fail_count", 0) == 0:
        # Automated, all passing → Defined (3)
        return 3
    # Running but has failures → Managed (2)
    return 2


def _score_secure_development() -> int:
    """Score domain 11: Secure Development (0-5)."""
    score = 1  # Trivy used in build script = baseline Initial
    # Semgrep config present
    semgrep_paths = [
        Path(".semgrep.yml"),
        Path("/app/.semgrep.yml"),
        Path("/workspace/.semgrep.yml"),
    ]
    if any(p.exists() for p in semgrep_paths):
        score += 1
    # Pre-commit config present
    precommit_paths = [
        Path(".pre-commit-config.yaml"),
        Path("/app/.pre-commit-config.yaml"),
    ]
    if any(p.exists() for p in precommit_paths):
        score += 1
    return min(score, 3)


def _score_incident_response(falco: Dict[str, Any], wazuh: Dict[str, Any]) -> int:
    """Score domain 12: Incident Response (0-5)."""
    score = 1  # SOC correlation engine wired = baseline
    if falco.get("status") != "not_run":
        score += 1  # Falco → SOC event stream
    if wazuh.get("status") != "not_run":
        score += 1  # Wazuh → SOC event stream
    return min(score, 3)


# ---------------------------------------------------------------------------
# Scorecard computation
# ---------------------------------------------------------------------------

def compute_scorecard() -> Dict[str, Any]:
    """Compute the 12-domain Container Security Scorecard.

    Domains scored 0-5 per the maturity scale:
      0=Not Started, 1=Initial, 2=Managed, 3=Defined, 4=Measured, 5=Optimizing

    Standards basis: CIS Docker Benchmark v1.6.0, NIST SP 800-190,
    DISA Docker Enterprise STIG, IEC 62443.

    Returns:
        Scorecard dict with per-domain scores and overall maturity.
    """
    trivy = get_trivy_summary()
    clamav = get_clamav_summary()
    falco = get_falco_summary()
    wazuh = get_wazuh_summary()
    openscap = get_openscap_summary()

    domain_scores = [
        _score_image_integrity(trivy),
        _score_vulnerability_management(trivy),
        _score_supply_chain(),
        _score_container_hardening(openscap),
        _score_runtime_protection(falco),
        _score_malware_defense(clamav),
        _score_network_segmentation(),
        _score_secrets_management(),
        _score_logging_monitoring(wazuh),
        _score_compliance_auditing(openscap),
        _score_secure_development(),
        _score_incident_response(falco, wazuh),
    ]

    domains = []
    for meta, score in zip(_SCORECARD_DOMAINS, domain_scores):
        domains.append({
            **meta,
            "score": score,
            "maturity": _MATURITY_LABELS[score],
        })

    total = sum(domain_scores)
    max_total = len(domain_scores) * 5
    overall_pct = round((total / max_total) * 100)
    overall_maturity_idx = min(overall_pct // 20, 5)

    return {
        "version": "v0.9.0",
        "standard_basis": [
            "CIS Docker Benchmark v1.6.0",
            "NIST SP 800-190",
            "DISA Docker Enterprise STIG",
            "IEC 62443",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "domains": domains,
        "totals": {
            "score": total,
            "max": max_total,
            "percentage": overall_pct,
        },
        "overall_maturity": _MATURITY_LABELS[overall_maturity_idx],
    }
