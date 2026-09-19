#!/usr/bin/env python3
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Classification logic for scripts/check-soak-status.sh.

Separated from the shell script so it has real unit test coverage instead of
being "smoke-tested separately" as an inline bash-embedded heredoc. Pure
function, no I/O — the shell script owns fetching `openclaw cron list --json`
and the container's StartedAt; this module only classifies the result.
"""

from __future__ import annotations

import json
import sys
from typing import Any

# OpenClaw's own documented, intentional behavior (dist/heartbeat-D9QLafFo
# .mjs's isHeartbeatContentEffectivelyEmpty): a heartbeat job skips its API
# call when the agent's own scratch/notepad has no actionable tasks queued,
# to avoid burning an LLM call on nothing. Root-caused 2026-09-19 after this
# gate flagged 164 consecutive occurrences as NOT_SOAKED — confirmed via
# `openclaw cron scratch <id>`: the scratch content was OpenClaw's own
# default template ("Keep this file empty... to skip heartbeat API calls"),
# not corrupted or unset. This is a real, working-as-designed no-op, not
# evidence of a regression — must not block soaking. It also proves nothing
# happened, so it must not count toward min_successes either; a real job
# succeeding is still required to soak.
_BENIGN_SKIP_MARKERS = ("empty-heartbeat-file",)


def _is_benign_skip(job: dict[str, Any]) -> bool:
    if job.get("status") != "skipped":
        return False
    last_error = (job.get("state") or {}).get("lastError") or job.get("lastRunError") or ""
    return any(marker in last_error for marker in _BENIGN_SKIP_MARKERS)


def classify(
    jobs: list[dict[str, Any]], started_at_ms: int, min_successes: int
) -> tuple[bool, str]:
    """Return (soaked, message) for the given cron job list.

    soaked=True only if at least min_successes jobs completed with
    status == "ok" since started_at_ms, AND no job that ran since
    started_at_ms is in any other status (error, skipped, etc.) — an
    actively-failing job since redeploy blocks soak regardless of how many
    other jobs succeeded. A known-benign heartbeat skip (see
    _is_benign_skip) is excluded entirely: neutral, not a block and not a
    success.
    """
    since_boot = [
        j
        for j in jobs
        if (j.get("state") or {}).get("lastRunAtMs", 0) > started_at_ms and not _is_benign_skip(j)
    ]

    errored = [j for j in since_boot if j.get("status") != "ok"]
    succeeded = [j for j in since_boot if j.get("status") == "ok"]

    if errored:
        names = ", ".join(
            f"{j.get('name')} ({j.get('status')}: "
            f"{(j.get('state') or {}).get('lastError') or j.get('lastRunError') or 'no detail'})"
            for j in errored
        )
        return False, f"NOT_SOAKED errored_since_boot: {names}"

    if len(succeeded) >= min_successes:
        return True, f"SOAKED {len(succeeded)} successful run(s) since boot"

    return False, f"NOT_SOAKED only {len(succeeded)}/{min_successes} successful run(s) since boot"


def main() -> int:
    started_at_ms = int(sys.argv[1])
    min_successes = int(sys.argv[2])

    try:
        data = json.loads(sys.stdin.read())
    except Exception as e:  # noqa: BLE001 — surfaced to the caller, not swallowed
        print(f"PARSE_ERROR {e}")
        return 2

    jobs = data.get("jobs", [])
    for j in jobs:
        last_run = (j.get("state") or {}).get("lastRunAtMs", 0)
        if last_run > started_at_ms:
            print(
                f"  [soak-status] since-boot run: {j.get('name')} status={j.get('status')}",
                file=sys.stderr,
            )

    soaked, message = classify(jobs, started_at_ms, min_successes)
    print(message)
    return 0 if soaked else 1


if __name__ == "__main__":
    sys.exit(main())
