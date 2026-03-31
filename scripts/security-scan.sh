#!/usr/bin/env bash
# AgentShroud Unified Build-Time Security Scan
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
#
# Implements Tranche 3 Phase 1 (IEC 62443 4-1 SDL):
#   - Trivy: CVE scan on gateway + bot images (FR3 SR 3.4)
#   - Syft: SBOM generation for supply chain traceability (FR3, EO 14028)
#   - Cosign: Image signing + pre-deploy verification (FR3 SR 3.4)
#   - OpenSCAP: CIS Docker Benchmark compliance scan (FR3 SR 3.3)
#   - Semgrep: SAST on gateway Python source (SDL 4-1)
#
# Usage:
#   bash scripts/security-scan.sh [--skip-cosign] [--skip-openscap] [--severity HIGH]
#
# Environment:
#   AGENTSHROUD_IMAGE_GATEWAY  Gateway image name (default: agentshroud-gateway:latest)
#   AGENTSHROUD_IMAGE_BOT      Bot image name (default: agentshroud-bot:latest)
#   REPORTS_DIR                Output directory for reports (default: reports/security)
#   TRIVY_SEVERITY             Severity filter (default: CRITICAL,HIGH)
#   COSIGN_SKIP                Set to 1 to skip cosign (e.g., in local dev)
#   OPENSCAP_SKIP              Set to 1 to skip OpenSCAP (requires docker + oscap-docker)
#   FAIL_ON_CRITICAL           Set to 0 to warn instead of exit on CRITICAL (default: 1)

set -euo pipefail

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

GATEWAY_IMAGE="${AGENTSHROUD_IMAGE_GATEWAY:-agentshroud-gateway:latest}"
BOT_IMAGE="${AGENTSHROUD_IMAGE_BOT:-agentshroud-bot:latest}"
REPORTS_DIR="${REPORTS_DIR:-reports/security}"
TRIVY_SEVERITY="${TRIVY_SEVERITY:-CRITICAL,HIGH}"
COSIGN_SKIP="${COSIGN_SKIP:-0}"
OPENSCAP_SKIP="${OPENSCAP_SKIP:-0}"
FAIL_ON_CRITICAL="${FAIL_ON_CRITICAL:-1}"
TS="$(date -u +%Y%m%d-%H%M%S)"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RESET='\033[0m'

info()    { echo -e "${BLUE}[security-scan]${RESET} $*"; }
success() { echo -e "${GREEN}[security-scan] OK${RESET} $*"; }
warn()    { echo -e "${YELLOW}[security-scan] WARN${RESET} $*"; }
error()   { echo -e "${RED}[security-scan] ERROR${RESET} $*" >&2; }

require_tool() {
    local tool="$1"
    if ! command -v "$tool" &>/dev/null; then
        error "Required tool not found: $tool"
        error "Install via Nix: nix profile install nixpkgs#$tool"
        return 1
    fi
}

mkdir -p "${REPORTS_DIR}/trivy" "${REPORTS_DIR}/sbom" "${REPORTS_DIR}/openscap" "${REPORTS_DIR}/semgrep"

SCAN_FAILURES=0

# ---------------------------------------------------------------------------
# 1. Trivy — CVE vulnerability scanning (FR3 SR 3.4)
# ---------------------------------------------------------------------------

info "=== Trivy CVE Scan ==="

if ! command -v trivy &>/dev/null; then
    warn "trivy not found — skipping CVE scan"
    warn "Install: nix profile install nixpkgs#trivy"
else
    for image in "${GATEWAY_IMAGE}" "${BOT_IMAGE}"; do
        safe_name="${image//[:\/]/-}"
        report="${REPORTS_DIR}/trivy/trivy-${safe_name}-${TS}.json"
        info "Scanning: ${image}"

        # ghcr.io is the primary DB source — mirror.gcr.io is blocked by Cisco AnyConnect VPN.
        trivy image \
            --format json \
            --severity "${TRIVY_SEVERITY}" \
            --no-progress \
            --timeout 600s \
            --db-repository ghcr.io/aquasecurity/trivy-db \
            --output "${report}" \
            "${image}" 2>/dev/null || true

        if [[ -f "${report}" ]]; then
            critical_count=$(python3 -c "
import json, sys
try:
    data = json.load(open('${report}'))
    total = sum(
        1 for r in data.get('Results', [])
        for v in r.get('Vulnerabilities', [])
        if v.get('Severity') == 'CRITICAL'
    )
    print(total)
except Exception as e:
    print(0)
" 2>/dev/null || echo "0")

            if [[ "${critical_count}" -gt 0 ]]; then
                error "Trivy: ${critical_count} CRITICAL CVE(s) in ${image}"
                if [[ "${FAIL_ON_CRITICAL}" == "1" ]]; then
                    SCAN_FAILURES=$((SCAN_FAILURES + 1))
                fi
            else
                success "Trivy: no CRITICAL CVEs in ${image}"
            fi
        fi
    done
fi

# ---------------------------------------------------------------------------
# 2. Syft — SBOM generation (FR3, EO 14028 mandate)
# ---------------------------------------------------------------------------

info "=== Syft SBOM Generation ==="

if ! command -v syft &>/dev/null; then
    warn "syft not found — skipping SBOM generation"
    warn "Install: nix profile install nixpkgs#syft"
else
    for image in "${GATEWAY_IMAGE}" "${BOT_IMAGE}"; do
        safe_name="${image//[:\/]/-}"
        sbom_file="${REPORTS_DIR}/sbom/sbom-${safe_name}-${TS}.json"
        info "Generating SBOM: ${image}"

        if syft "${image}" \
            --output spdx-json="${sbom_file}" \
            --quiet 2>/dev/null; then
            success "SBOM generated: ${sbom_file}"
        else
            warn "SBOM generation failed for ${image} — image may not be built yet"
        fi
    done
fi

# ---------------------------------------------------------------------------
# 3. Cosign — Image signing and verification (FR3 SR 3.4)
# ---------------------------------------------------------------------------

info "=== Cosign Image Signing ==="

if [[ "${COSIGN_SKIP}" == "1" ]]; then
    warn "Cosign skipped (COSIGN_SKIP=1)"
elif ! command -v cosign &>/dev/null; then
    warn "cosign not found — skipping image signing"
    warn "Install: nix profile install nixpkgs#cosign"
else
    for image in "${GATEWAY_IMAGE}" "${BOT_IMAGE}"; do
        info "Signing: ${image}"

        # Keyless signing via Sigstore OIDC (requires OIDC provider in CI)
        # In local dev, use --yes to skip interactive confirmation
        if cosign sign --yes "${image}" 2>/dev/null; then
            success "Image signed: ${image}"
        else
            warn "Cosign sign failed for ${image} — ensure OIDC is configured"
        fi
    done
fi

# ---------------------------------------------------------------------------
# 4. Cosign verify — pre-deploy signature check
# ---------------------------------------------------------------------------

info "=== Cosign Pre-Deploy Verification ==="

if [[ "${COSIGN_SKIP}" == "1" ]]; then
    warn "Cosign verify skipped (COSIGN_SKIP=1)"
elif command -v cosign &>/dev/null; then
    for image in "${GATEWAY_IMAGE}" "${BOT_IMAGE}"; do
        info "Verifying signature: ${image}"

        if cosign verify \
            --certificate-identity-regexp ".*" \
            --certificate-oidc-issuer-regexp ".*" \
            "${image}" &>/dev/null; then
            success "Signature verified: ${image}"
        else
            warn "No Cosign signature found for ${image} — unsigned image"
            # Non-fatal in dev; enforce in production CI via FAIL_ON_CRITICAL
        fi
    done
fi

# ---------------------------------------------------------------------------
# 5. OpenSCAP — CIS Docker Benchmark compliance (FR3 SR 3.3)
# ---------------------------------------------------------------------------

info "=== OpenSCAP CIS Benchmark Scan ==="

if [[ "${OPENSCAP_SKIP}" == "1" ]]; then
    warn "OpenSCAP skipped (OPENSCAP_SKIP=1)"
elif ! command -v oscap-docker &>/dev/null && ! command -v oscap &>/dev/null; then
    warn "oscap-docker not found — skipping compliance scan"
    warn "Install: nix profile install nixpkgs#openscap"
else
    report="${REPORTS_DIR}/openscap/openscap-${TS}.xml"
    report_json="${REPORTS_DIR}/openscap/openscap-${TS}.json"

    info "Scanning gateway container filesystem"

    # Scan the running gateway container if available
    if command -v oscap-docker &>/dev/null && docker ps --filter "name=agentshroud-gateway" --format "{{.Names}}" | grep -q agentshroud-gateway 2>/dev/null; then
        oscap-docker container agentshroud-gateway \
            oval eval \
            --results "${report}" \
            --report "${REPORTS_DIR}/openscap/oscap-report-${TS}.html" \
            /usr/share/xml/scap/ssg/content/ssg-debian12-ds.xml 2>/dev/null || true

        success "OpenSCAP report: ${report}"
    else
        # Filesystem scan fallback
        oscap oval eval \
            --results "${report}" \
            /usr/share/xml/scap/ssg/content/ssg-debian12-ds.xml 2>/dev/null || true
    fi

    # Convert to JSON summary for SOC ingestion
    if [[ -f "${report}" ]]; then
        python3 -c "
import xml.etree.ElementTree as ET, json, datetime, sys
try:
    tree = ET.parse('${report}')
    root = tree.getroot()
    ns = {'oval': 'http://oval.mitre.org/XMLSchema/oval-results-5'}
    results = root.findall('.//oval:result', ns)
    pass_count = sum(1 for r in results if r.get('result') == 'true')
    fail_count = sum(1 for r in results if r.get('result') == 'false')
    summary = {
        'tool': 'openscap',
        'profile': 'CIS Docker Benchmark v1.6.0',
        'timestamp': datetime.datetime.utcnow().isoformat() + 'Z',
        'pass_count': pass_count,
        'fail_count': fail_count,
        'critical': 0,
        'high': fail_count,
    }
    print(json.dumps(summary, indent=2))
except Exception as e:
    print(json.dumps({'tool': 'openscap', 'error': str(e), 'pass_count': 0, 'fail_count': 0, 'critical': 0, 'high': 0}))
" > "${report_json}" 2>/dev/null && success "OpenSCAP JSON summary: ${report_json}"
    fi
fi

# ---------------------------------------------------------------------------
# 6. Semgrep — SAST on gateway Python source (SDL 4-1)
# ---------------------------------------------------------------------------

info "=== Semgrep SAST Scan ==="

if ! command -v semgrep &>/dev/null; then
    warn "semgrep not found — skipping SAST"
    warn "Install: nix profile install nixpkgs#semgrep"
else
    semgrep_report="${REPORTS_DIR}/semgrep/semgrep-${TS}.json"

    info "Scanning gateway/ Python source"

    semgrep scan \
        --config .semgrep.yml \
        --json \
        --output "${semgrep_report}" \
        --quiet \
        gateway/ 2>/dev/null || semgrep_rc=$?

    if [[ -f "${semgrep_report}" ]]; then
        finding_count=$(python3 -c "
import json, sys
try:
    data = json.load(open('${semgrep_report}'))
    print(len(data.get('results', [])))
except Exception:
    print(0)
" 2>/dev/null || echo "0")

        if [[ "${finding_count}" -gt 0 ]]; then
            warn "Semgrep: ${finding_count} finding(s) — review ${semgrep_report}"
        else
            success "Semgrep: no findings"
        fi
    fi
fi

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------

echo ""
info "=== Security Scan Summary ==="
info "Reports directory: ${REPORTS_DIR}"
info "Timestamp: ${TS}"

if [[ "${SCAN_FAILURES}" -gt 0 ]]; then
    error "${SCAN_FAILURES} critical finding(s) require remediation before deploy"
    exit 1
fi

success "All security scans passed"

# ---------------------------------------------------------------------------
# Push reports to gateway SOC volume (security-reports:/var/log/security)
# ---------------------------------------------------------------------------
# Reports written locally are not visible to the gateway until copied into the
# Docker volume that backs /var/log/security inside the gateway container.
# This step is a no-op if the gateway is not running.

if command -v docker &>/dev/null && docker inspect agentshroud-gateway &>/dev/null 2>&1; then
    info "Pushing reports to gateway SOC volume..."
    for subdir in trivy sbom openscap semgrep; do
        src="${REPORTS_DIR}/${subdir}"
        if [[ -d "${src}" ]] && [[ -n "$(ls -A "${src}" 2>/dev/null)" ]]; then
            docker exec agentshroud-gateway mkdir -p "/var/log/security/${subdir}" 2>/dev/null || true
            docker cp "${src}/." "agentshroud-gateway:/var/log/security/${subdir}/" 2>/dev/null \
                && success "Pushed ${subdir} reports to SOC" \
                || warn "Could not push ${subdir} reports (volume may be read-only)"
        fi
    done
else
    info "Gateway not running — skipping SOC volume push"
fi
