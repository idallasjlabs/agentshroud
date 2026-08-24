#!/usr/bin/env bash
# remind_proposal_review.sh — PostToolUse hook (EditTool, WriteTool)
#
# Prints a non-blocking checklist after every file modification reminding
# the team to review the CHANGE PROPOSAL before committing.
#
# Exit 0 = allow (non-blocking — never stops execution)

set -euo pipefail

cat >&2 <<'REMINDER'
─────────────────────────────────────────────────────────────────
CHANGE PROPOSAL CHECKLIST — review before git commit:
  [ ] Change proposal was produced before this edit
  [ ] Scope matches the original request (no scope creep)
  [ ] Scalability assessed at 10× and 100× data volume
  [ ] All hard limits explicitly named
  [ ] Blast radius documented (direct + indirect dependencies)
  [ ] At least 2 alternatives were considered
  [ ] Rollback path documented
  [ ] Verification plan is in place
─────────────────────────────────────────────────────────────────
REMINDER

exit 0
