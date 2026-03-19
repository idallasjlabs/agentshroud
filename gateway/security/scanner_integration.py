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

def _is_fresh(report_dir: Path, prefix: str = "", max_age_hours: int = 24) -> bool:
    """Return True if the most recent report file was written within max_age_hours."""
    if not report_dir.exists():
        return False
    pattern = f"{prefix}*.json" if prefix else "*.json"
    files = sorted(report_dir.glob(pattern), reverse=True)
    if not files:
        return False
    try:
        age_hours = (datetime.now(timezone.utc).timestamp() - files[0].stat().st_mtime) / 3600
        return age_hours <= max_age_hours
    except Exception:
        return False


def _app_state_has(attr_name: str) -> bool:
    """Return True if app_state has a non-None attribute with the given name."""
    try:
        from ..ingest_api.state import app_state
        return getattr(app_state, attr_name, None) is not None
    except Exception:
        return False


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
    """Score domain 1: Image Integrity (0-5).

    1=SBOM exists, 2=Trivy ran, 3=zero criticals,
    4=zero criticals+highs (Measured), 5=all clean + scan fresh <24h (Optimizing).
    """
    score = 0
    sbom_exists = _SBOM_REPORT_DIR.exists() and any(_SBOM_REPORT_DIR.glob("sbom-*.json"))
    trivy_ran = trivy.get("status") not in ("not_run", "error")
    trivy_no_critical = trivy_ran and trivy.get("critical", 0) == 0
    trivy_no_high = trivy_ran and trivy.get("high", 0) == 0
    if sbom_exists:
        score += 1
    if trivy_ran:
        score += 1
    if trivy_no_critical:
        score += 1
    if trivy_no_critical and trivy_no_high:
        score += 1
    if sbom_exists and trivy_no_critical and trivy_no_high and _is_fresh(_TRIVY_REPORT_DIR, "trivy-"):
        score += 1
    return min(score, 5)


def _score_vulnerability_management(trivy: Dict[str, Any]) -> int:
    """Score domain 2: Vulnerability Management (0-5).

    1=module exists, 2=zero criticals, 3=zero criticals+highs,
    4=zero criticals+highs+mediums (Measured), 5=clean + scan fresh <24h (Optimizing).
    """
    if trivy.get("status") in ("not_run",) or trivy.get("error"):
        return 1
    if trivy.get("critical", 0) > 0:
        return 1
    if trivy.get("high", 0) > 0:
        return 2
    if trivy.get("medium", 0) > 0:
        return 3
    # Zero criticals + highs + mediums
    if _is_fresh(_TRIVY_REPORT_DIR, "trivy-"):
        return 5
    return 4


def _score_supply_chain() -> int:
    """Score domain 3: Supply Chain (0-5).

    0=no SBOM, 2=SBOM exists, 3=SBOM has packages,
    4=SBOM + Trivy cross-referenced (Measured), 5=SBOM + Trivy + zero criticals (Optimizing).
    """
    if not (_SBOM_REPORT_DIR.exists() and any(_SBOM_REPORT_DIR.glob("sbom-*.json"))):
        return 0
    sbom = get_sbom()
    packages = len(sbom.get("packages", [])) if sbom else 0
    if packages == 0:
        return 2
    trivy = get_trivy_summary()
    trivy_ran = trivy.get("status") not in ("not_run", "error")
    if not trivy_ran:
        return 3
    if trivy.get("critical", 0) > 0:
        return 4
    return 5


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
    """Score domain 5: Runtime Protection (0-5).

    1=module exists, 2=running with criticals, 4=running no criticals + actively monitoring,
    5=running no criticals + zero findings (Optimizing).
    """
    if falco.get("status") == "not_run":
        return 1
    if falco.get("critical", 0) > 0:
        return 2
    # Running, no criticals
    if falco.get("findings", 0) == 0:
        return 5  # Zero findings — clean
    return 4  # Has non-critical findings — actively monitoring


def _score_malware_defense(clamav: Dict[str, Any]) -> int:
    """Score domain 6: Malware Defense (0-5).

    1=module exists or infected, 3=running clean,
    4=running clean + workspace scanned (Measured),
    5=running clean + scanned + report fresh <24h (Optimizing).
    """
    if clamav.get("status") == "not_run":
        return 1
    if clamav.get("critical", 0) > 0:
        return 1
    # Running and clean
    if clamav.get("files_scanned", 0) > 0:
        if _is_fresh(_CLAMAV_REPORT_DIR, "clamav-"):
            return 5
        return 4
    return 3


def _score_network_segmentation() -> int:
    """Score domain 7: Network Segmentation (0-5).

    3=Docker network architecture baseline, 4=Docker socket accessible (Measured),
    5=network_validator runtime module loaded (Optimizing).
    """
    score = 3
    if Path("/var/run/docker.sock").exists():
        score += 1
    if _app_state_has("network_validator"):
        score += 1
    return min(score, 5)


def _score_secrets_management() -> int:
    """Score domain 8: Secrets Management (0-5).

    2=Docker secrets + key_vault baseline, 3=runtime secrets mounted (Defined),
    4=key_rotation module present (Measured), 5=encrypted_store initialized (Optimizing).
    """
    score = 2
    # Runtime secrets mounted at /run/secrets
    secrets_dir = Path("/run/secrets")
    if secrets_dir.exists():
        try:
            if any(secrets_dir.iterdir()):
                score += 1
        except Exception:
            pass
    # key_rotation module present
    key_rotation_paths = [
        Path("/app/gateway/security/key_rotation.py"),
        Path("gateway/security/key_rotation.py"),
    ]
    if any(p.exists() for p in key_rotation_paths):
        score += 1
    # encrypted_store initialized in app_state
    if _app_state_has("encrypted_store"):
        score += 1
    return min(score, 5)


def _score_logging_monitoring(wazuh: Dict[str, Any]) -> int:
    """Score domain 9: Logging & Monitoring (0-5).

    1=SOC exists, 2=Wazuh running, 3=Fluent Bit config,
    4=event_bus active (Measured), 5=all three pillars present (Optimizing).
    """
    score = 1  # SOC dashboard exists
    wazuh_running = wazuh.get("status") != "not_run"
    if wazuh_running:
        score += 1
    fluent_bit_paths = [
        Path("/fluent-bit/etc/fluent-bit.conf"),
        Path("/etc/fluent-bit/fluent-bit.conf"),
    ]
    fluent_bit_present = any(p.exists() for p in fluent_bit_paths)
    if fluent_bit_present:
        score += 1
    event_bus_active = _app_state_has("event_bus")
    if event_bus_active:
        score += 1
    # Optimizing: all monitoring pillars present simultaneously
    if fluent_bit_present and wazuh_running and event_bus_active:
        score += 1
    return min(score, 5)


def _score_compliance_auditing(openscap: Dict[str, Any]) -> int:
    """Score domain 10: Compliance Auditing (0-5).

    0=not run, 2=has failures, 3=zero failures,
    4=zero failures + report on disk (Measured), 5=zero failures + fresh report <24h (Optimizing).
    """
    if openscap.get("status") == "not_run":
        return 0
    if openscap.get("fail_count", 0) > 0:
        return 2
    # Zero failures — at least Defined (3)
    report_exists = _OPENSCAP_REPORT_DIR.exists() and any(_OPENSCAP_REPORT_DIR.glob("openscap-*.json"))
    if not report_exists:
        return 3
    if _is_fresh(_OPENSCAP_REPORT_DIR, "openscap-"):
        return 5
    return 4


def _score_secure_development() -> int:
    """Score domain 11: Secure Development (0-5).

    1=Trivy in build, 2=semgrep config, 3=pre-commit config,
    4=gitleaks config (Measured), 5=SDL documentation present (Optimizing).
    """
    score = 1  # Trivy used in build script = baseline Initial
    semgrep_paths = [
        Path(".semgrep.yml"),
        Path("/app/.semgrep.yml"),
        Path("/workspace/.semgrep.yml"),
    ]
    if any(p.exists() for p in semgrep_paths):
        score += 1
    precommit_paths = [
        Path(".pre-commit-config.yaml"),
        Path("/app/.pre-commit-config.yaml"),
    ]
    if any(p.exists() for p in precommit_paths):
        score += 1
    gitleaks_paths = [
        Path(".gitleaks.toml"),
        Path("gitleaks.toml"),
        Path("/app/.gitleaks.toml"),
        Path("/app/gitleaks.toml"),
    ]
    if any(p.exists() for p in gitleaks_paths):
        score += 1
    sdl_doc_paths = [
        Path("CONTRIBUTING.md"),
        Path("/app/CONTRIBUTING.md"),
        Path("SECURITY.md"),
        Path("/app/SECURITY.md"),
    ]
    if any(p.exists() for p in sdl_doc_paths):
        score += 1
    return min(score, 5)


def _score_incident_response(falco: Dict[str, Any], wazuh: Dict[str, Any]) -> int:
    """Score domain 12: Incident Response (0-5).

    1=SOC exists, 2=Falco running, 3=Wazuh running,
    4=soc_correlation engine initialized (Measured), 5=killswitch available (Optimizing).
    """
    score = 1  # SOC correlation engine wired = baseline
    if falco.get("status") != "not_run":
        score += 1
    if wazuh.get("status") != "not_run":
        score += 1
    if _app_state_has("soc_correlation"):
        score += 1
    killswitch_paths = [
        Path("/app/docker/scripts/killswitch.sh"),
        Path("docker/scripts/killswitch.sh"),
    ]
    if any(p.exists() for p in killswitch_paths):
        score += 1
    return min(score, 5)


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

    overall_score = round(total / max_total * 5, 2) if max_total else 0.0
    overall_label = _MATURITY_LABELS[overall_maturity_idx]

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
        # UI-friendly aliases
        "overall_score": overall_score,
        "overall_level": overall_label,
        "overall_maturity": overall_label,
    }
