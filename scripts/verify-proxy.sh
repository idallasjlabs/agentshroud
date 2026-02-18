#!/bin/zsh
# SecureClaw Proxy Verification Script
#
# Usage:
#   ./scripts/verify-proxy.sh           # Full verification
#   ./scripts/verify-proxy.sh --quick   # Quick smoke test
#   ./scripts/verify-proxy.sh --canary  # Send canary + check
#   ./scripts/verify-proxy.sh --chain   # Verify audit chain
#   ./scripts/verify-proxy.sh --bypass  # Test direct access blocked

set -euo pipefail

PYTHON="${HOME}/miniforge3/envs/oneclaw/bin/python"
PROJECT_DIR="${HOME}/Development/oneclaw"
cd "${PROJECT_DIR}"

GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

pass() { echo "${GREEN}PASS${NC}: $1"; }
fail() { echo "${RED}FAIL${NC}: $1"; FAILURES=$((FAILURES + 1)); }
info() { echo "${YELLOW}INFO${NC}: $1"; }

FAILURES=0
MODE="${1:---full}"

run_quick() {
    info "Quick smoke test..."

    # Test 1: Pipeline imports
    if "${PYTHON}" -c "from gateway.proxy.pipeline import SecurityPipeline; print('OK')" 2>/dev/null; then
        pass "Pipeline imports"
    else
        fail "Pipeline imports"
    fi

    # Test 2: Canary imports
    if "${PYTHON}" -c "from gateway.security.canary import run_canary; print('OK')" 2>/dev/null; then
        pass "Canary imports"
    else
        fail "Canary imports"
    fi

    # Test 3: Dashboard imports
    if "${PYTHON}" -c "from gateway.dashboard.proxy_status import ProxyDashboard; print('OK')" 2>/dev/null; then
        pass "Dashboard imports"
    else
        fail "Dashboard imports"
    fi
}

run_canary() {
    info "Running canary..."
    RESULT=$("${PYTHON}" -c "
import asyncio, json
from gateway.security.canary import run_canary
from gateway.proxy.pipeline import SecurityPipeline
from gateway.security.prompt_guard import PromptGuard
from gateway.security.trust_manager import TrustManager
from gateway.ingest_api.sanitizer import PIISanitizer
from gateway.ingest_api.config import PIIConfig

async def main():
    cfg = PIIConfig(engine='regex', entities=['US_SSN','CREDIT_CARD','PHONE_NUMBER','EMAIL_ADDRESS'], enabled=True)
    p = SecurityPipeline(prompt_guard=PromptGuard(), pii_sanitizer=PIISanitizer(cfg), trust_manager=TrustManager(db_path=':memory:'))
    p.trust_manager.register_agent('canary')
    r = await run_canary(pipeline=p)
    print(json.dumps(r.to_dict(), indent=2))

asyncio.run(main())
" 2>&1)

    echo "${RESULT}"
    if echo "${RESULT}" | grep -q '"verified": true'; then
        pass "Canary verification"
    else
        fail "Canary verification"
    fi
}

run_chain() {
    info "Verifying audit chain..."
    RESULT=$("${PYTHON}" -c "
import asyncio
from gateway.proxy.pipeline import SecurityPipeline
from gateway.security.prompt_guard import PromptGuard
from gateway.security.trust_manager import TrustManager
from gateway.ingest_api.sanitizer import PIISanitizer
from gateway.ingest_api.config import PIIConfig

async def main():
    cfg = PIIConfig(engine='regex', entities=['US_SSN'], enabled=True)
    p = SecurityPipeline(prompt_guard=PromptGuard(), pii_sanitizer=PIISanitizer(cfg), trust_manager=TrustManager(db_path=':memory:'))
    p.trust_manager.register_agent('test')
    for i in range(25):
        await p.process_inbound(f'chain test {i}', agent_id='test')
    valid, msg = p.verify_audit_chain()
    print(f'valid={valid} msg={msg}')

asyncio.run(main())
" 2>&1)

    echo "${RESULT}"
    if echo "${RESULT}" | grep -q 'valid=True'; then
        pass "Audit chain integrity"
    else
        fail "Audit chain integrity"
    fi
}

run_bypass() {
    info "Testing direct access blocked..."

    # Check docker-compose.secure.yml exists and OpenClaw has no ports
    if [ -f docker-compose.secure.yml ]; then
        if grep -q 'internal: true' docker-compose.secure.yml; then
            pass "Internal network is marked internal"
        else
            fail "Internal network not marked internal"
        fi

        # Check OpenClaw has no ports in secure mode
        OPENCLAW_SECTION=$(sed -n '/^\s*openclaw:/,/^\s*[a-z]/p' docker-compose.secure.yml)
        if echo "${OPENCLAW_SECTION}" | grep -q 'ports:'; then
            fail "OpenClaw exposes ports in proxy mode"
        else
            pass "OpenClaw has no port mappings in proxy mode"
        fi
    else
        fail "docker-compose.secure.yml not found"
    fi
}

run_full() {
    info "=== Full Proxy Verification ==="
    echo ""
    run_quick
    echo ""
    run_canary
    echo ""
    run_chain
    echo ""
    run_bypass
    echo ""

    # Run pytest
    info "Running E2E test suite..."
    if "${PYTHON}" -m pytest gateway/tests/test_e2e_proxy.py -v 2>&1; then
        pass "E2E test suite"
    else
        fail "E2E test suite"
    fi
}

case "${MODE}" in
    --quick)  run_quick ;;
    --canary) run_canary ;;
    --chain)  run_chain ;;
    --bypass) run_bypass ;;
    --full|*) run_full ;;
esac

echo ""
if [ "${FAILURES}" -eq 0 ]; then
    echo "${GREEN}All checks passed!${NC}"
    exit 0
else
    echo "${RED}${FAILURES} check(s) failed${NC}"
    exit 1
fi
