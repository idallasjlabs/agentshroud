#!/bin/zsh
# Canary cron job — runs canary verification and logs results
# Usage: Add to crontab: */15 * * * * /path/to/scripts/canary-cron.sh
#
# On failure: writes alert to ~/logs/canary-alert.log
# On success: logs to ~/logs/canary.log

PYTHON="${HOME}/miniforge3/envs/agentshroud/bin/python"
PROJECT_DIR="${HOME}/Development/agentshroud"
LOG_DIR="${HOME}/logs"
CANARY_LOG="${LOG_DIR}/canary.log"
ALERT_LOG="${LOG_DIR}/canary-alert.log"

mkdir -p "${LOG_DIR}"

TIMESTAMP=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

cd "${PROJECT_DIR}" || exit 1

# Run canary
RESULT=$("${PYTHON}" -c "
import asyncio
import json
from gateway.security.canary import run_canary
from gateway.proxy.pipeline import SecurityPipeline
from gateway.security.prompt_guard import PromptGuard
from gateway.security.trust_manager import TrustManager
from gateway.ingest_api.sanitizer import PIISanitizer
from gateway.ingest_api.config import PIIConfig

async def main():
    pii_config = PIIConfig(engine='regex', entities=['US_SSN','CREDIT_CARD','PHONE_NUMBER','EMAIL_ADDRESS'], enabled=True)
    pipeline = SecurityPipeline(
        prompt_guard=PromptGuard(),
        pii_sanitizer=PIISanitizer(pii_config),
        trust_manager=TrustManager(db_path=':memory:'),
    )
    pipeline.trust_manager.register_agent('canary')
    result = await run_canary(pipeline=pipeline)
    print(json.dumps(result.to_dict()))

asyncio.run(main())
" 2>&1)

EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ]; then
    echo "${TIMESTAMP} CANARY FAILED (exit code ${EXIT_CODE}): ${RESULT}" >> "${ALERT_LOG}"
    echo "${TIMESTAMP} FAIL" >> "${CANARY_LOG}"
    exit 1
fi

# Check if verified
VERIFIED=$(echo "${RESULT}" | python3 -c "import sys,json; print(json.load(sys.stdin).get('verified', False))" 2>/dev/null)

if [ "${VERIFIED}" = "True" ]; then
    echo "${TIMESTAMP} PASS ${RESULT}" >> "${CANARY_LOG}"
else
    echo "${TIMESTAMP} CANARY CHECKS FAILED: ${RESULT}" >> "${ALERT_LOG}"
    echo "${TIMESTAMP} FAIL ${RESULT}" >> "${CANARY_LOG}"
    exit 1
fi
