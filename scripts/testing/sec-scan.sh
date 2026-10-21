#!/usr/bin/env bash
# shellcheck disable=SC2034,SC1091
# sec-scan.sh — SAST, secrets, SCA, IaC and image scanning (i-security-scanner gate)
# Contract and env: see lib.sh (--json, I_GATE=report|block, I_REPO, exit 0/1/2).
set -o pipefail
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
T_NAME="sec-scan"; T_SUMMARY="SAST, secrets, SCA, IaC and image scanning (i-security-scanner gate)"
T_OPTIONS="Environment: I_IMAGE=<ref> scans a container image; I_STAGING_URL=<url> enables DAST (staging only)."
t_parse "" "$@"; t_init
if t_have semgrep sast-semgrep; then t_run sast-semgrep "semgrep scan --config auto --error --quiet ."; fi
if t_have gitleaks secrets-gitleaks; then t_run secrets-gitleaks "gitleaks detect --no-banner --redact --source ."; fi  # pragma: allowlist secret
if t_have trivy sca-trivy; then t_run sca-trivy "trivy fs --quiet --exit-code 1 --severity HIGH,CRITICAL ."; fi
if [ -n "$(git ls-files '*.tf' '*.yaml' '*.yml' 'Dockerfile*' 2>/dev/null | head -1)" ]; then
    if t_have checkov iac-checkov; then t_run iac-checkov "checkov -d . --quiet --compact"; fi
else
    t_skip iac-checkov "no IaC files (*.tf, Dockerfile, yaml) found"
fi
if [ -n "${I_IMAGE:-}" ]; then
    if t_have trivy image-trivy; then t_run image-trivy "trivy image --quiet --exit-code 1 --severity HIGH,CRITICAL $I_IMAGE"; fi
else
    t_skip image-trivy "no container image given (set I_IMAGE)"
fi
if [ -n "${I_STAGING_URL:-}" ]; then
    case "$I_STAGING_URL" in *prod*) t_die "refusing DAST against a URL containing 'prod' — staging only" ;; esac
    t_skip dast "DAST runner not bundled; run your DAST tool against $I_STAGING_URL (staging only)"
else
    t_skip dast "DAST needs I_STAGING_URL (staging only)"
fi
t_finish
