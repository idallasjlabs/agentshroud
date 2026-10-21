#!/usr/bin/env bash
# shellcheck disable=SC2034,SC1091
# sbom-verify.sh — SBOM, signature/provenance and license checks (i-release-gate gate)
# Contract and env: see lib.sh (--json, I_GATE=report|block, I_REPO, exit 0/1/2).
set -o pipefail
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
T_NAME="sbom-verify"; T_SUMMARY="SBOM, signature/provenance and license checks (i-release-gate gate)"
T_OPTIONS="Environment: I_SBOM=<file>; I_SBOM_SIG + I_COSIGN_KEY for signature; I_DENY_LICENSES (default 'AGPL-3.0 GPL-3.0')."
t_parse "" "$@"; t_init
sbom="${I_SBOM:-}"
if [ -z "$sbom" ]; then
    sbom="$(git ls-files 'sbom*.json' '*.cdx.json' '*.spdx.json' 'bom.json' 2>/dev/null | head -1)"
    [ -n "$sbom" ] || sbom="$(ls sbom*.json *.cdx.json *.spdx.json bom.json 2>/dev/null | head -1)"
fi
if [ -z "$sbom" ] || [ ! -f "$sbom" ]; then
    t_skip sbom "no SBOM found (set I_SBOM, or generate one with syft/cdxgen)"
else
    if /usr/bin/grep -q -E '"(components|packages)"' "$sbom" && head -c1 "$sbom" | /usr/bin/grep -q '{'; then
        t_record sbom-valid pass "$sbom has components/packages"
    else
        t_record sbom-valid fail "$sbom is not a CycloneDX/SPDX document"
    fi
    deny="${I_DENY_LICENSES:-AGPL-3.0 GPL-3.0}"; bad=""
    for l in $deny; do /usr/bin/grep -q "\"$l" "$sbom" && bad="$bad $l"; done
    [ -z "$bad" ] && t_record license-check pass "no denied licenses ($deny)" || t_record license-check fail "denied licenses present:$bad"
    if [ -n "${I_SBOM_SIG:-}" ] && [ -n "${I_COSIGN_KEY:-}" ]; then
        if t_have cosign signature; then t_run signature "cosign verify-blob --key $I_COSIGN_KEY --signature $I_SBOM_SIG $sbom"; fi
    else
        t_skip signature "set I_SBOM_SIG and I_COSIGN_KEY to verify the signature"
    fi
    if [ -n "$(git ls-files '*.intoto.jsonl' 2>/dev/null | head -1)" ]; then t_record provenance pass "in-toto attestation present"; else t_skip provenance "no *.intoto.jsonl provenance attestation"; fi
fi
t_finish
