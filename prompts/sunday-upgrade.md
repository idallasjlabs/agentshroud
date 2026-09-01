# AgentShroud Weekly Upgrade — Sunday Maintenance Run

You are running headless (`claude -p`) from a Hermes cron job on marvin. There is no human watching. Do not ask questions; make the safest reasonable choice, record it, and continue. Everything you do must be evidence-based: never claim a step succeeded without showing the command output that proves it.

## Mission

AgentShroud is a security tool. Every Sunday, bring **every agent, component, and utility** in both the **dev** and **prod** stacks to the latest stable release, and **resolve every reported security finding**. Dev goes first. Prod is promoted only after dev passes all checks. If anything fails, roll back and report — a stack left running the old version is acceptable; a stack left broken is not.

## Ground rules

- Work only inside the AgentShroud project directories under `~/Development` (locate them with `ls ~/Development | grep -i shroud` and by reading any `README`, `CLAUDE.md`, `compose*.yml`, `Makefile`, or `scripts/` you find). Prefer the project's own scripts/Make targets over ad-hoc commands whenever they exist.
- Discover the environment layout from the repo, do not assume it: which compose files / profiles / env files / branches map to **dev** vs **prod**, and how the gateway, Hermes (`agentshroud-hermes-v2`), LibreChat, the docker-socket-proxy, `hermes-sandbox-*` containers, searxng, and any other services are wired. State the mapping you found in the report.
- **Latest release** means the latest stable, tagged release — not `main`, not pre-releases, not `:latest` floating tags. Pin every upgrade to an explicit version (image tag/digest, git tag, package version). Never leave a component on an unpinned tag.
- **Do not modify security policy.** Do not loosen gateway rules, allowlists, network policies, secrets handling, or sandbox restrictions to make an upgrade pass. If an upgrade requires a policy change, do not apply it: leave that component on its current version, flag it as BLOCKED in the report, and explain exactly what change the upstream release demands.
- **No-exceptions remediation (owner directive 2026-09-01, verbatim): "This is a security tool. All CVE must be resolved and all versions must be updated to latest release on Sunday no exceptions. If code changes are required, we need to make them."** Concretely: needing a CODE change (Dockerfile ARG bumps, dependency/lockfile updates, build tweaks) is NOT grounds for BLOCKED — make the change, commit it on the run's branch, test it, ship it through the dev→prod flow. The ONLY legitimate residuals are (a) CVEs with no fix released anywhere upstream — each individually documented in docs/security/cve-mitigation-matrix.md with evidence, and (b) upgrades that would require LOOSENING a security control (previous bullet — that stays BLOCKED). "The fix requires work" is never a reason to skip.
- Never print, log, or commit secrets. Never edit `.env` values other than version pins.
- Work on a branch named `chore/upgrade-YYYY-MM-DD` (today's date). Commit with clear messages. Do not push, merge, or open a PR unless the repo's CLAUDE.md/docs explicitly say the Sunday job should. Do not rewrite history.
- Keep a running log at `~/Development/<project>/reports/upgrade-YYYY-MM-DD.md` from the very start so a partial run still leaves a record.
- Time budget: if you are past 90 minutes and not finished, stop, ensure both stacks are healthy (roll back anything half-applied), and report what remains.

## Cross-account reality (marvin)

**Dev and prod are separate macOS accounts with separate Colima VMs** — this
session runs on the prod account (`ijefferson.admin`) and CANNOT start,
stop, or exec into the dev stack (`agentshroud-bot`'s VM). "Dev goes first"
is therefore enforced by a handoff contract:

- The dev account runs its own copy of this job **earlier** (03:00 ET) and
  stages a machine-readable result at
  `/Users/Shared/agentshroud-sunday/dev-result-YYYY-MM-DD.json`
  (`{"date","status":"PASS|FAIL","versions":{component:version,...},"notes"}`).
- **Before applying anything to prod**, read that file. If it is missing or
  `status` != `PASS`, apply NOTHING to prod: report every component as
  BLOCKED-awaiting-dev and stop after the inventory/scan phases (those are
  read-only and always run).
- Promote to prod **only the exact versions dev passed** — never a version
  dev didn't test, even if newer.

## Procedure

### 0. Preflight (both environments)
1. `git status` hygiene — with two sanctioned exceptions (added 2026-08-30
   after the first run correctly aborted on them; owner directed the gate be
   fixed rather than the tree):
   - `graphify-out/**` modifications NEVER count as dirty: repo hooks
     regenerate them on every branch switch (standing owner decision — never
     commit them from this job).
   - Other pre-existing uncommitted modifications: list them in the report,
     leave them strictly untouched, and PROCEED. All of your own commits must
     be pathspec-scoped (`git commit -- <paths>`, never `git add -A`, never a
     bare commit — repo hooks re-stage files behind you). Stop only if a file
     YOU need to change already has uncommitted modifications.
2. Record current state: `docker compose ... ps`, all image tags/digests in use, `git describe --tags` / lockfile versions for every component. This is your rollback baseline — save it to the report.
3. Confirm Colima and Docker are healthy and there is enough free disk for pulls (`df -h`, `docker system df`).
4. Confirm the rollback path actually works before touching anything: identify the exact commands to restore the baseline (previous tags, previous commit) and write them into the report.

### 1. Inventory
Build a complete table of every upgradable thing in the repo. Include, at minimum:
- Container images in every compose file (gateway, Hermes, LibreChat, MongoDB/Meilisearch/RAG or whatever LibreChat depends on, docker-socket-proxy, sandbox base images, searxng, voice gateway, OpenClaw, monitoring/sidecars).
- Language dependencies: `package.json`/lockfiles, `pyproject.toml`/`requirements*.txt`/`uv.lock`, `go.mod`, etc. for every agent, component, and utility in the repo.
- Base images in any local `Dockerfile`s.
- Agent definitions, skills, MCP servers, plugins, and Claude Code / Hermes config that pin versions.
- Git submodules or vendored code.
- Tooling (Colima, Docker CLI, compose plugin) — report available updates but only apply them if the project docs say the Sunday job owns host tooling.

For each item: current version, latest stable version, source URL you used to determine it, and whether a changelog mentions breaking changes or security fixes.

### 2. Security findings
Collect every open security report before upgrading so you can verify closure afterwards:
- `npm audit` / `pnpm audit` / `pip-audit` / `uv` audit / `cargo audit` / `govulncheck` as applicable.
- Image scanning with whatever the repo already uses (Trivy, Grype, Docker Scout). If none is configured and `trivy` is available, use `trivy image` and `trivy fs`. Do not install new scanners on the host without a documented mechanism.
- GitHub Dependabot / code-scanning alerts via `gh` if the repo is on GitHub and `gh auth status` succeeds.
- Any findings files the project already maintains (`SECURITY.md`, `security/`, prior `reports/`).
- **Wazuh / SOC alerts**: review open alerts from the Wazuh sidecar and the gateway's SOC surface (`/soc/v1/...` endpoints, `/var/log/security/` reports) for anything raised since the last Sunday run — these count as findings to close or explicitly ACCEPT, same as scanner output.

Record every finding with ID (CVE/GHSA), severity, affected component, and fixed-in version.

### 3. Upgrade DEV
1. Apply all version bumps from the inventory to the **dev** configuration only. One commit per logical component so a bad bump can be reverted alone.
2. Regenerate lockfiles; rebuild any local images; `docker compose pull` and bring dev up.
3. Verify — all of the following must pass, with output captured in the report:
   - Every container reaches `healthy`/`running` and stays there for at least 2 minutes with no restart loop (`docker compose ps`, `docker compose logs --since 5m` grep for `error|panic|fatal|traceback`).
   - The project's own test suite / smoke tests / `make test` / `make check`, if any.
   - Gateway end-to-end: a request through the agentshroud-gateway reaches Hermes and returns; a request that policy should block is still blocked. Use the existing test scripts or health endpoints — do not invent new attack traffic.
   - Hermes can still spawn a `hermes-sandbox-*` container through the docker-socket-proxy and it is torn down afterwards.
   - LibreChat responds on its health endpoint and can reach the gateway.
   - Re-run all audits/scans from step 2. Every finding must be either FIXED (show it gone) or explicitly ACCEPTED with a reason (no fix released yet, not reachable in our configuration) — never silently dropped.
4. If any check fails: revert the specific commit(s) responsible, bring dev back up, re-verify, and mark that component FAILED with the error. Continue with the remaining components. If dev cannot be made healthy at all, restore the full baseline and stop — do not touch prod.

### 4. Promote to PROD
Proceed **only if** dev is fully healthy and every finding is FIXED or ACCEPTED.
1. Apply exactly the version set that passed on dev — no new versions, no components that failed on dev.
2. Take a backup of any stateful services before upgrading them (LibreChat/Mongo data, Hermes state/config volumes) using the project's backup script or `docker run --rm -v <vol>:/data -v ~/Development/<project>/backups:/backup alpine tar czf /backup/<vol>-YYYY-MM-DD.tgz /data`. Verify the archive is non-empty.
3. Bring prod up and run the same verification suite as step 3.3.
4. If prod verification fails: restore the baseline immediately (previous tags + previous commit), restore volumes only if data was migrated irreversibly, re-verify prod is healthy, and mark the promotion ROLLED BACK.

### 5. Cleanup
- `docker image prune` only images superseded by this run (keep the rollback baseline images for one week — do not prune them).
- Remove stopped sandbox containers left over from testing.
- Ensure no test artefacts, backups, or logs are staged for commit.

### 6. Report
Finish `reports/upgrade-YYYY-MM-DD.md` with these sections, then print the whole file to stdout as the final output (Hermes captures stdout):

1. **Summary line** — one of: `ALL GREEN`, `PARTIAL (n components failed/blocked)`, `ROLLED BACK`, `ABORTED (reason)`.
2. **Environment mapping** you discovered (dev vs prod).
3. **Upgrade table** — component | env | before | after | status (UPGRADED / ALREADY CURRENT / FAILED / BLOCKED / SKIPPED) | notes.
4. **Security findings** — ID | severity | component | before | after (FIXED / ACCEPTED-with-reason / OPEN).
5. **Verification evidence** — the actual command outputs for each check in 3.3 and 4.3, trimmed to the relevant lines.
6. **Breaking changes / manual follow-ups** — anything from changelogs a human must read, and every BLOCKED item with the policy change it would require.
7. **Rollback instructions** — exact commands to return prod and dev to the pre-run baseline.
8. **Time spent** and whether the 90-minute budget was hit.

Never end the run with either stack in a non-healthy state.
