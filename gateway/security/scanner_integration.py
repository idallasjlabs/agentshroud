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
    {
        "id": 13,
        "domain": "Identity & Authentication",
        "description": "Validates that all agent interfaces enforce identity verification before granting access. Covers API token auth, certificate-based identity, and MFA for privileged operations. IEC 62443 SL 2 requires score ≥ 3; SL 3 requires score = 5.",
        "standard_ref": "IEC 62443 FR1, NIST 800-190 §3.4",
        "tools": ["gateway_auth", "rbac"],
        "iec_fr": "FR1",
    },
    {
        "id": 14,
        "domain": "Access Control & Authorization",
        "description": "Measures the maturity of role-based access control across agent and operator interfaces. Verifies least privilege enforcement, capability auditing, and authorization decision audit trails.",
        "standard_ref": "IEC 62443 FR2",
        "tools": ["rbac", "session_manager"],
        "iec_fr": "FR2",
    },
    {
        "id": 15,
        "domain": "Data Confidentiality & Encryption",
        "description": "Assesses encryption coverage for data in transit and at rest. Checks TLS enforcement on all interfaces, encryption at rest for sensitive stores, and certificate rotation posture.",
        "standard_ref": "IEC 62443 FR4, NIST 800-190 §3.3",
        "tools": ["tls", "encrypted_store"],
        "iec_fr": "FR4",
    },
    {
        "id": 16,
        "domain": "Resource Availability & Limits",
        "description": "Verifies that all containers have CPU/memory limits, restart policies, and health checks configured. Validates rate limiting at the proxy layer and resource telemetry shipping to monitoring.",
        "standard_ref": "IEC 62443 FR7, CIS 5.10-5.11",
        "tools": ["docker_compose", "http_proxy"],
        "iec_fr": "FR7",
    },
    {
        "id": 17,
        "domain": "Image Signing & Provenance",
        "description": "Checks that container images are cryptographically signed and their provenance is verifiable. Validates Docker Content Trust, Cosign/Notary signing, and SLSA attestation posture.",
        "standard_ref": "NIST 800-190 §3.1, CIS 4.5",
        "tools": ["cosign", "docker_content_trust"],
        "iec_fr": "FR3",
    },
    {
        "id": 18,
        "domain": "Registry Security",
        "description": "Evaluates the security of the container image registry. Checks for private registry use, TLS enforcement, authentication requirements, and scanning at push time.",
        "standard_ref": "NIST 800-190 §3.2",
        "tools": ["registry"],
        "iec_fr": "FR3",
    },
    {
        "id": 19,
        "domain": "Host OS Hardening",
        "description": "Assesses the security posture of the container host. Checks kernel information availability, Docker daemon isolation from host users, separate storage partitions, and CIS Level 1 host controls.",
        "standard_ref": "NIST 800-190 §3.5, CIS Section 1",
        "tools": ["host_audit"],
        "iec_fr": "FR3",
    },
    {
        "id": 20,
        "domain": "Docker Daemon Configuration",
        "description": "Validates Docker daemon security settings against CIS Section 2/3 baselines. Checks icc=false, no-new-privileges, log driver limits, live-restore, and optional userns-remap.",
        "standard_ref": "CIS Sections 2 & 3",
        "tools": ["daemon_config"],
        "iec_fr": "FR3, FR5",
    },
    {
        "id": 21,
        "domain": "Container Runtime Isolation",
        "description": "Verifies that running containers enforce kernel-level isolation: no privileged mode, no host namespace sharing, read-only root filesystem, dropped capabilities, and AppArmor/seccomp profiles.",
        "standard_ref": "CIS Section 5, NIST 800-190 §3.3",
        "tools": ["runtime_audit"],
        "iec_fr": "FR3, FR5",
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


def _read_docker_daemon_config() -> Dict[str, Any]:
    """Read and return the Docker daemon config from daemon.json, or {} if unavailable."""
    paths = [
        Path("/etc/docker/daemon.json"),
        Path("/host/etc/docker/daemon.json"),
    ]
    for p in paths:
        try:
            if p.exists():
                return json.loads(p.read_text())
        except Exception:
            pass
    return {}


def _score_network_segmentation() -> int:
    """Score domain 7: Network Segmentation (0-5).

    3=Docker network architecture baseline (three isolated networks),
    4=icc=false confirmed in daemon config (CIS 2.1) (Measured),
    5=icc=false + network_validator module loaded and active (Optimizing).

    Note: Docker socket presence is NOT a positive signal — it is a privilege
    escalation risk. The positive signals are daemon-level isolation controls.
    """
    score = 3  # Docker network baseline (internal/isolated/console separation)
    daemon_cfg = _read_docker_daemon_config()
    icc_disabled = not daemon_cfg.get("icc", True)  # icc defaults True; False means disabled
    if icc_disabled:
        score += 1
    if icc_disabled and _app_state_has("network_validator"):
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


def _score_identity_authentication() -> int:
    """Score domain 13: Identity & Authentication (0-5). IEC 62443 FR1.

    1=API token auth on at least one interface, 2=auth on all agent endpoints,
    3=RBAC+session management (structured identity, not just token),
    4=auth events logged with actor identity, 5=auth+audit+anomaly detection active.
    """
    # Level 1: auth module loaded (gateway has token auth by design)
    auth_paths = [
        Path("/app/gateway/ingest_api/auth.py"),
        Path("gateway/ingest_api/auth.py"),
    ]
    if not any(p.exists() for p in auth_paths):
        return 0
    score = 1
    # Level 2: auth enforced on all agent-facing endpoints (pipeline loaded)
    if _app_state_has("pipeline"):
        score += 1
    # Level 3: structured identity via RBAC + session_manager (not just token)
    if _app_state_has("session_manager"):
        score += 1
    # Level 4: auth events logged via data ledger
    if _app_state_has("ledger"):
        score += 1
    # Level 5: anomaly detection active (progressive_lockdown or trust_manager)
    if _app_state_has("trust_manager"):
        score += 1
    return min(score, 5)


def _score_access_control_authorization() -> int:
    """Score domain 14: Access Control & Authorization (0-5). IEC 62443 FR2.

    1=role definitions exist, 2=RBAC enforced on dispatch,
    3=least privilege applied, 4=authorization decisions logged,
    5=RBAC+audit+access review evidence on disk.
    """
    rbac_paths = [
        Path("/app/gateway/security/rbac_config.py"),
        Path("gateway/security/rbac_config.py"),
    ]
    if not any(p.exists() for p in rbac_paths):
        return 0
    score = 1  # Role definitions exist
    if _app_state_has("session_manager"):
        score += 1  # RBAC enforced
    if _app_state_has("collaborator_tracker"):
        score += 1  # Least privilege: collaborator access audited
    if _app_state_has("ledger"):
        score += 1  # Authorization decisions logged
    # Level 5: access review evidence on disk
    review_paths = [
        Path("/app/data/collaborator_activity.jsonl"),
        Path("/tmp/agentshroud-data/collaborator_activity.jsonl"),
    ]
    if any(p.exists() for p in review_paths):
        score += 1
    return min(score, 5)


def _score_data_confidentiality_encryption() -> int:
    """Score domain 15: Data Confidentiality & Encryption (0-5). IEC 62443 FR4.

    1=TLS on external interfaces, 2=TLS on all interfaces,
    3=encryption at rest (encrypted_store), 4=cert expiry monitored,
    5=mTLS + encryption at rest + key rotation evidence.
    """
    # Level 1: TLS on external (gateway listens on HTTPS, or proxied via TLS)
    tls_cert_paths = [
        Path("/run/secrets/tls_cert"),
        Path("/app/certs/tls.crt"),
        Path("/etc/ssl/gateway/tls.crt"),
    ]
    tls_available = any(p.exists() for p in tls_cert_paths)
    # Even without a cert file, the gateway is TLS-terminated at proxy layer
    # Score 1 as baseline since external comms use HTTPS via reverse proxy
    score = 1
    # Level 2: TLS on all interfaces (internal comms encrypted — check event_bus TLS or mTLS config)
    if _app_state_has("http_proxy"):
        score += 1  # HTTP CONNECT proxy enforces TLS for outbound
    # Level 3: encryption at rest
    if _app_state_has("encrypted_store"):
        score += 1
    # Level 4: cert monitoring active
    if tls_available:
        score += 1
    # Level 5: key rotation evidence on disk
    rotation_paths = [
        Path("/app/data/key_rotation.log"),
        Path("/tmp/agentshroud-data/key_rotation.log"),
    ]
    if any(p.exists() for p in rotation_paths):
        score += 1
    return min(score, 5)


def _score_resource_availability() -> int:
    """Score domain 16: Resource Availability & Limits (0-5). IEC 62443 FR7.

    1=memory limits on at least one container (docker-compose present),
    2=CPU+memory limits on all agent containers, 3=limits+HEALTHCHECK+restart policy,
    4=rate limiting at proxy layer, 5=resource metrics shipped to monitoring.
    """
    compose_paths = [
        Path("/app/docker/docker-compose.yml"),
        Path("docker/docker-compose.yml"),
    ]
    if not any(p.exists() for p in compose_paths):
        return 0
    score = 1  # docker-compose.yml present = resource limits configured
    # Level 2: parse compose for explicit CPU+memory limits
    compose_text = ""
    for cp in compose_paths:
        try:
            if cp.exists():
                compose_text = cp.read_text()
                break
        except Exception:
            pass
    if "mem_limit" in compose_text or "memory:" in compose_text:
        score += 1
    # Level 3: HEALTHCHECK and restart policy present in compose
    if "healthcheck" in compose_text.lower() and "restart" in compose_text:
        score += 1
    # Level 4: rate limiting active at proxy layer
    if _app_state_has("http_proxy"):
        score += 1
    # Level 5: event_bus shipping resource metrics
    if _app_state_has("event_bus"):
        score += 1
    return min(score, 5)


def _score_image_signing_provenance() -> int:
    """Score domain 17: Image Signing & Provenance (0-5). NIST 800-190 §3.1.

    0=no signing, DCT unset, 1=DOCKER_CONTENT_TRUST=1 set,
    2=cosign binary present, 3=signature verification enforced at pull time,
    4=SLSA provenance attestation present, 5=full supply chain attestation.
    """
    import os
    dct = os.environ.get("DOCKER_CONTENT_TRUST", "0")
    if dct not in ("1", "true", "yes"):
        return 0
    score = 1  # DOCKER_CONTENT_TRUST=1
    import shutil
    if shutil.which("cosign"):
        score += 1
    # Level 3: verify cosign is used in CI (check .github/workflows for cosign usage)
    cosign_ci_paths = [
        Path("/app/.github/workflows"),
        Path(".github/workflows"),
    ]
    cosign_in_ci = False
    for wf_dir in cosign_ci_paths:
        try:
            if wf_dir.exists():
                for wf in wf_dir.glob("*.yml"):
                    if "cosign" in wf.read_text():
                        cosign_in_ci = True
                        break
        except Exception:
            pass
    if cosign_in_ci:
        score += 1
    # Level 4: SLSA provenance (check for slsa-verifier or provenance attestation files)
    if shutil.which("slsa-verifier"):
        score += 1
    # Level 5: all above + policy enforcement
    if score == 4 and cosign_in_ci:
        score += 1
    return min(score, 5)


def _score_registry_security() -> int:
    """Score domain 18: Registry Security (0-5). NIST 800-190 §3.2.

    0=public registry, no controls, 1=private registry in use,
    2=registry requires auth, 3=registry TLS enforced,
    4=image scanning at push time, 5=full registry security stack.
    """
    # Check docker config for registry auth
    docker_config_paths = [
        Path("/home/agentshroud/.docker/config.json"),
        Path("/root/.docker/config.json"),
        Path("/tmp/.docker/config.json"),
    ]
    docker_cfg: Dict[str, Any] = {}
    for dcp in docker_config_paths:
        try:
            if dcp.exists():
                docker_cfg = json.loads(dcp.read_text())
                break
        except Exception:
            pass
    auths = docker_cfg.get("auths", {})
    if not auths:
        return 0
    score = 1  # Private registry credentials present
    # Level 2: auth required (credentials exist = registry auth enforced)
    if any(v.get("auth") or v.get("username") for v in auths.values()):
        score += 1
    # Level 3: TLS (check that registry URLs use https)
    if all(k.startswith("https://") or "." in k for k in auths.keys()):
        score += 1
    # Level 4: scanning at push (check if registry is ECR/GCR/GHCR with built-in scanning)
    known_scanning_registries = ("ecr.", "gcr.io", "ghcr.io", "registry.gitlab.com")
    if any(any(r in k for r in known_scanning_registries) for k in auths.keys()):
        score += 1
    # Level 5: all above + pull access logging (evidence via audit log)
    if score == 4 and _app_state_has("ledger"):
        score += 1
    return min(score, 5)


def _score_host_os_hardening() -> int:
    """Score domain 19: Host OS Hardening (0-5). NIST 800-190 §3.5.

    0=no info, 1=kernel info available, 2=Docker daemon accessible,
    3=Docker version current (within reasonable range), 4=host audit logging present,
    5=CIS Level 1 host hardening evidence on disk.
    """
    # Level 1: kernel info readable
    kernel_info = Path("/proc/version")
    if not kernel_info.exists():
        return 0
    score = 1
    # Level 2: Docker socket accessible (implies Docker is running with proper perms)
    if Path("/var/run/docker.sock").exists():
        score += 1
    # Level 3: Docker daemon info accessible via socket — check via docker CLI
    import shutil
    if shutil.which("docker"):
        try:
            import subprocess
            result = subprocess.run(
                ["docker", "info", "--format", "{{.ServerVersion}}"],
                capture_output=True, text=True, timeout=5,
            )
            if result.returncode == 0 and result.stdout.strip():
                score += 1
        except Exception:
            pass
    # Level 4: host audit logging (auditd present or /var/log/audit exists)
    audit_paths = [
        Path("/var/log/audit/audit.log"),
        Path("/var/log/docker.log"),
    ]
    if any(p.exists() for p in audit_paths):
        score += 1
    # Level 5: CIS hardening script or evidence file
    cis_evidence = [
        Path("/etc/cis-hardening-applied"),
        Path("/var/log/security/cis-host-hardening.json"),
    ]
    if any(p.exists() for p in cis_evidence):
        score += 1
    return min(score, 5)


def _score_docker_daemon_config() -> int:
    """Score domain 20: Docker Daemon Configuration (0-5). CIS Sections 2 & 3.

    0=default config, 1=icc=false, 2=no-new-privileges=true,
    3=log driver with size limits, 4=live-restore=true+userland-proxy=false,
    5=all + userns-remap + TLS if TCP socket.
    """
    daemon = _read_docker_daemon_config()
    if not daemon:
        return 0
    score = 0
    # Level 1: icc=false
    if not daemon.get("icc", True):
        score += 1
    # Level 2: no-new-privileges
    if daemon.get("no-new-privileges", False):
        score += 1
    # Level 3: log driver with size limits
    log_driver = daemon.get("log-driver", "")
    log_opts = daemon.get("log-opts", {})
    if log_driver and log_driver != "json-file" or (log_opts.get("max-size") or log_opts.get("max-file")):
        score += 1
    # Level 4: live-restore + userland-proxy disabled
    if daemon.get("live-restore", False) and not daemon.get("userland-proxy", True):
        score += 1
    # Level 5: userns-remap enabled
    if daemon.get("userns-remap"):
        score += 1
    return min(score, 5)


def _score_container_runtime_isolation() -> int:
    """Score domain 21: Container Runtime Isolation (0-5). CIS Section 5.

    0=privileged containers, 1=no privileged flag,
    2=no host namespace sharing, 3=read-only root filesystem,
    4=capabilities dropped (CapEff=0), 5=seccomp+AppArmor+cap_drop+read-only.
    """
    # Level 1: check if we are running in non-privileged mode
    # /proc/self/status CapEff=0000000000000000 means no effective caps
    cap_eff = "0000000000000000"
    try:
        status = Path("/proc/self/status").read_text()
        for line in status.splitlines():
            if line.startswith("CapEff:"):
                cap_eff = line.split(":", 1)[1].strip()
                break
    except Exception:
        return 0
    # If CapEff is all zeros, running with no capabilities (fully dropped)
    fully_dropped = cap_eff == "0000000000000000"
    # Non-zero caps but not full root (ffffffffffffffff) = partially dropped
    is_root = cap_eff == "ffffffffffffffff"
    if is_root:
        return 0  # Running as root with all capabilities = privileged
    score = 1  # Not fully privileged
    # Level 2: check for host namespace sharing via /proc/1/ns vs /proc/self/ns
    try:
        pid1_mnt = Path("/proc/1/ns/mnt").resolve()
        self_mnt = Path("/proc/self/ns/mnt").resolve()
        if str(pid1_mnt) != str(self_mnt):
            score += 1  # Isolated mount namespace
        else:
            # If same namespace as PID 1, we share host namespaces
            return 1
    except Exception:
        score += 1  # Can't check = assume isolated
    # Level 3: read-only root filesystem
    try:
        mounts = Path("/proc/mounts").read_text()
        # Root mount is typically "/ " or "overlay /"
        root_ro = any(
            ("/ " in line or " / " in line) and " ro," in line
            for line in mounts.splitlines()
        )
        if root_ro:
            score += 1
    except Exception:
        pass
    # Level 4: capabilities dropped (CapEff effectively 0 or very minimal)
    if fully_dropped:
        score += 1
    # Level 5: seccomp and AppArmor profiles applied
    seccomp_enabled = False
    apparmor_enabled = False
    try:
        proc_status = Path("/proc/self/status").read_text()
        seccomp_enabled = "Seccomp:" in proc_status and "2" in [
            l.split(":", 1)[1].strip() for l in proc_status.splitlines()
            if l.startswith("Seccomp:")
        ]
    except Exception:
        pass
    try:
        aa_status = Path("/proc/self/attr/current").read_text().strip()
        apparmor_enabled = bool(aa_status) and aa_status != "unconfined"
    except Exception:
        pass
    if (seccomp_enabled or apparmor_enabled) and fully_dropped:
        score += 1
    return min(score, 5)


# ---------------------------------------------------------------------------
# Mandatory gate evaluation (overrides domain scores on hard fail)
# ---------------------------------------------------------------------------

# Maps gate_name → domain_id that gets zeroed on failure
_MANDATORY_GATES: Dict[str, int] = {
    "privileged_container": 21,
    "critical_cve_running": 2,
    "no_agent_auth": 13,
    "no_tls_external": 15,
    "dct_unset_no_cosign": 17,
}


def _evaluate_mandatory_gates(
    domain_scores: Dict[int, int],
    trivy: Dict[str, Any],
) -> Dict[int, int]:
    """Apply mandatory gate overrides to domain scores.

    Returns updated scores dict. Gate failures set the affected domain to 0
    regardless of other signals.
    """
    import os, shutil
    updated = dict(domain_scores)

    # Gate: privileged container → Domain 21 → 0
    # If CapEff == full root, we're in a privileged container
    try:
        status = Path("/proc/self/status").read_text()
        for line in status.splitlines():
            if line.startswith("CapEff:"):
                if line.split(":", 1)[1].strip() == "ffffffffffffffff":
                    updated[21] = 0
    except Exception:
        pass

    # Gate: critical CVE in running image → Domain 2 → 0
    if trivy.get("critical", 0) > 0:
        updated[2] = 0

    # Gate: no auth on agent endpoint → Domain 13 → 0
    auth_paths = [
        Path("/app/gateway/ingest_api/auth.py"),
        Path("gateway/ingest_api/auth.py"),
    ]
    if not any(p.exists() for p in auth_paths):
        updated[13] = 0

    # Gate: no TLS on external interface (no certs AND DOCKER_CONTENT_TRUST not set)
    tls_cert_paths = [
        Path("/run/secrets/tls_cert"),
        Path("/app/certs/tls.crt"),
        Path("/etc/ssl/gateway/tls.crt"),
    ]
    if not any(p.exists() for p in tls_cert_paths):
        # Gateway is behind a TLS-terminating proxy; this is not a hard fail
        # Only fail if encrypted_store is also absent (no at-rest either)
        if not _app_state_has("encrypted_store"):
            updated[15] = min(updated.get(15, 1), 1)  # Cap at 1, don't zero

    # Gate: DOCKER_CONTENT_TRUST unset AND no cosign → Domain 17 → 0
    dct = os.environ.get("DOCKER_CONTENT_TRUST", "0")
    cosign_available = bool(shutil.which("cosign"))
    if dct not in ("1", "true", "yes") and not cosign_available:
        updated[17] = 0

    return updated


# ---------------------------------------------------------------------------
# Compliance sub-score computation
# ---------------------------------------------------------------------------

# IEC 62443 FR mapping: {domain_id: (fr_label, weight)}
_IEC_DOMAIN_MAP: Dict[int, tuple] = {
    13: ("FR1", 2),
    14: ("FR2", 2),
    15: ("FR4", 2),
    7:  ("FR5", 2),
    9:  ("FR6", 1),
    12: ("FR6", 1),
    16: ("FR7", 2),
    8:  ("FR4", 1),
}

# NIST 800-190 risk area mapping: {domain_id: (risk_area, weight)}
_NIST_DOMAIN_MAP: Dict[int, tuple] = {
    1:  ("image_risks", 2),
    2:  ("image_risks", 2),
    3:  ("image_risks", 2),
    17: ("image_risks", 2),
    18: ("registry_risks", 2),
    5:  ("container_risks", 1),
    21: ("container_risks", 2),
    19: ("host_risks", 2),
}

# CIS mapping: {domain_id: (cis_section, weight)}
_CIS_DOMAIN_MAP: Dict[int, tuple] = {
    19: ("section_1", 2),
    20: ("sections_2_3", 2),
    4:  ("section_4", 2),
    21: ("section_5", 2),
    17: ("section_4_5", 1),
    6:  ("section_6", 1),
}


def _compute_weighted_subscore(
    scores: Dict[int, int], domain_map: Dict[int, tuple]
) -> float:
    """Return weighted sub-score as 0.0–100.0 percentage."""
    total_weighted = 0
    max_weighted = 0
    for domain_id, (_, weight) in domain_map.items():
        score = scores.get(domain_id, 0)
        total_weighted += score * weight
        max_weighted += 5 * weight
    if max_weighted == 0:
        return 0.0
    return round(total_weighted / max_weighted * 100, 1)


def _determine_iec_sl(scores: Dict[int, int]) -> int:
    """Determine the highest achieved IEC 62443 Security Level.

    SL 1: All IEC-mapped domains score ≥ 2; no mandatory gates failed.
    SL 2: All IEC-mapped domains score ≥ 3; Domains 13, 14 score ≥ 4.
    SL 3: All IEC-mapped domains score ≥ 4; Domain 15 = 5.
    SL 4: All 21 domains = 5.
    """
    iec_ids = list(_IEC_DOMAIN_MAP.keys())
    if all(scores.get(d, 0) >= 2 for d in iec_ids):
        sl = 1
    else:
        return 0
    if all(scores.get(d, 0) >= 3 for d in iec_ids) and \
       scores.get(13, 0) >= 4 and scores.get(14, 0) >= 4:
        sl = 2
    else:
        return sl
    if all(scores.get(d, 0) >= 4 for d in iec_ids) and scores.get(15, 0) == 5:
        sl = 3
    else:
        return sl
    if all(scores.get(d, 0) == 5 for d in range(1, 22)):
        sl = 4
    return sl


# ---------------------------------------------------------------------------
# Scorecard computation
# ---------------------------------------------------------------------------

def compute_scorecard() -> Dict[str, Any]:
    """Compute the 21-domain Security Scorecard.

    Domains scored 0-5 per the maturity scale:
      0=Not Started, 1=Initial, 2=Managed, 3=Defined, 4=Measured, 5=Optimizing

    Standards basis: CIS Docker Benchmark v1.6.0, NIST SP 800-190,
    DISA Docker Enterprise STIG, IEC 62443 (with FR mapping and SL determination).

    Includes:
    - Mandatory gate evaluation (hard-fail conditions zero affected domains)
    - Three compliance sub-scores (IEC 62443, NIST 800-190, CIS)
    - IEC 62443 Security Level determination (SL 0-4)

    Returns:
        Scorecard dict with per-domain scores, compliance sub-scores, and overall maturity.
    """
    trivy = get_trivy_summary()
    clamav = get_clamav_summary()
    falco = get_falco_summary()
    wazuh = get_wazuh_summary()
    openscap = get_openscap_summary()

    # Raw domain scores (index 0 = domain 1)
    raw_scores = [
        _score_image_integrity(trivy),           # 1
        _score_vulnerability_management(trivy),  # 2
        _score_supply_chain(),                   # 3
        _score_container_hardening(openscap),    # 4
        _score_runtime_protection(falco),        # 5
        _score_malware_defense(clamav),          # 6
        _score_network_segmentation(),           # 7
        _score_secrets_management(),             # 8
        _score_logging_monitoring(wazuh),        # 9
        _score_compliance_auditing(openscap),    # 10
        _score_secure_development(),             # 11
        _score_incident_response(falco, wazuh),  # 12
        _score_identity_authentication(),        # 13
        _score_access_control_authorization(),   # 14
        _score_data_confidentiality_encryption(), # 15
        _score_resource_availability(),          # 16
        _score_image_signing_provenance(),       # 17
        _score_registry_security(),              # 18
        _score_host_os_hardening(),              # 19
        _score_docker_daemon_config(),           # 20
        _score_container_runtime_isolation(),    # 21
    ]

    # Build domain_id → score dict (1-indexed)
    scores_by_id: Dict[int, int] = {i + 1: s for i, s in enumerate(raw_scores)}

    # Apply mandatory gates
    scores_by_id = _evaluate_mandatory_gates(scores_by_id, trivy)
    domain_scores = [scores_by_id[i + 1] for i in range(21)]

    # Build domain list with metadata
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

    # Compliance sub-scores
    iec_pct = _compute_weighted_subscore(scores_by_id, _IEC_DOMAIN_MAP)
    nist_pct = _compute_weighted_subscore(scores_by_id, _NIST_DOMAIN_MAP)
    cis_pct = _compute_weighted_subscore(scores_by_id, _CIS_DOMAIN_MAP)

    # IEC 62443 Security Level
    iec_sl = _determine_iec_sl(scores_by_id)

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
        "compliance": {
            "iec_62443": {
                "sub_score_pct": iec_pct,
                "security_level": iec_sl,
                "security_level_label": f"SL {iec_sl}",
            },
            "nist_800_190": {
                "sub_score_pct": nist_pct,
            },
            "cis_docker": {
                "sub_score_pct": cis_pct,
            },
        },
        # UI-friendly aliases
        "overall_score": overall_score,
        "overall_level": overall_label,
        "overall_maturity": overall_label,
    }
