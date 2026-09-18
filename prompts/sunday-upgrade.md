# AgentShroud Weekly Upgrade — Sunday Maintenance Run

You are running as a Remote Control session (visible/steerable from the phone via claude.ai), launched by launchd via `scripts/sunday-upgrade.sh` in a detached tmux session on marvin — not headless `claude -p`, and not a Hermes cron job. Nobody is watching live unless Isaiah has attached via Remote Control or tmux. Do not ask questions; make the safest reasonable choice, record it, and continue. Everything you do must be evidence-based: never claim a step succeeded without showing the command output that proves it.

## Mission

AgentShroud is a security tool. Every Sunday, bring **every agent, component, and utility** in both the **dev** and **prod** stacks to the latest stable release, and **resolve every reported security finding**. Dev goes first. Prod is promoted only after dev passes all checks. If anything fails, roll back and report — a stack left running the old version is acceptable; a stack left broken is not.

## THE RUN IS JUDGED ON STATE CHANGE, NOT ON STEPS COMPLETED

Read this before anything else. It exists because of a real, measured failure:

**For seven weeks (2026-07-29 → 2026-09-15) this job reported PASS every Sunday
while upgrading nothing.** `OPENCLAW_VERSION` went in as `2026.7.1` and moved
exactly once, to the downstream rebuild counter `2026.7.1-2`, while npm shipped
`2026.8.1`, `2026.8.2`, `2026.9.1`, `2026.9.2`, `2026.9.3`, `2026.9.4`.
`HERMES_VERSION` moved once ever, in a feature PR, never in a Sunday run.

The mission text above was already correct and explicit. The instruction was not
the problem. The problem was that nothing verified the instruction was followed:
a session could skip the "latest stable version" lookup, run the deterministic
script — which rebuilds whatever the pin already says and exits 0 — and write a
truthful-looking PASS. Every gate measured that commands ran, none measured that
anything changed.

Therefore:

1. **A run that changes no version pin is a FAILED run** unless you prove, with
   command output, that every component is already on the latest stable release.
   "I ran the upgrade and it passed" is not evidence of an upgrade.
2. **Every component in the report carries an explicit `from → to`.** If from
   equals to, it must be accompanied by the discovery output proving latest ==
   current, with the source and timestamp. A report with no deltas and no
   already-latest proof is a failed run, and you must label it FAILED yourself.
3. **Never infer an upgrade from an exit code.** `sunday-upgrade-apply.sh`
   exiting 0 means the stack is healthy, NOT that it was upgraded. Exit code 25
   (`NOTHING_UPGRADED`) is that script telling you it detected a no-op while a
   newer release exists — treat it as a hard failure to be fixed this run, never
   as an acceptable outcome to report around.
4. **Do not trust your own summary over the machine's.** Before writing the
   report, re-read `docker/versions.env` and the handoff JSON's `upgraded` and
   `latest_openclaw_seen` fields. Report what those say, not what you intended.

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

## USE THE DETERMINISTIC SCRIPT — do not improvise these steps

`scripts/sunday-upgrade-apply.sh` owns every mechanical, verifiable step of this
run. It exists because improvising a production upgrade unattended is not
reliable: the 2026-09-06 run failed on both accounts before doing any work, and
the 2026-09-09 build stalled silently. **Do not hand-roll `docker compose build`,
health checks, rollback, or the dev handoff file — call the script.**

```bash
scripts/sunday-upgrade-apply.sh --env dev|prod [--phase preflight|baseline|scan|apply|verify|all] [--dry-run]
```

Exit code IS the result. Do not re-interpret it, and never report a pass the
script did not give you:

| Code | Meaning | What you do |
|------|---------|-------------|
| 0 | all requested phases passed | continue |
| 10 | preflight failed (disk, docker, compose, missing binary) | fix the named cause or stop; do not build |
| 20 | CVE gate exceeded `--max-critical` | triage findings, do not override |
| 30 | build/compose failed (rollback attempted) | report the named service that failed |
| 40 | verify failed — unhealthy/restart loop (rollback attempted) | report; do not retry blindly |
| 50 | rollback itself failed | **STOP. Escalate. The stack may be degraded.** |
| 127 | required binary missing | report the binary; do not work around it |

Required order for prod: `preflight` → `baseline` → `scan` → `apply` → `verify`.
`--phase all` does this. **`baseline` is not optional** — it captures the rollback
tags and generates `rollback.sh`; without it a failed apply has nothing to roll
back to and exits 50.

On dev, the script writes `/Users/Shared/agentshroud-sunday/dev-result-<date>.json`
itself on success, and `status=FAIL` via an EXIT trap otherwise. Do not write that
file by hand.

Things the script will refuse to do, all of them deliberate — do NOT work around
them, report them instead:
- Build when the build context has uncommitted changes (would bake unreviewed WIP
  into a production image). Commit the work first, or report it.
  `--allow-dirty-build` exists but requires a real reason stated in the report.
- Start when Docker storage is below 25GiB free.
- Report a CVE pass when no scanner is installed.

**Your remaining job is judgement, not mechanics:** decide which versions are
candidates, read changelogs for breaking changes, triage findings the scan
surfaces, and write the report. The script decides whether a change ships.

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

**EVERYTHING MEANS EVERYTHING** (owner directive 2026-09-15). The scope is every
versioned thing in this repo — every wrapped agent (OpenClaw, Hermes, and any
future agent AgentShroud proxies) AND every supporting tool: Wazuh, Falco,
ClamAV, Trivy, OpenSCAP, Semgrep, Cosign, Syft, Fluent Bit, docker-socket-proxy,
searxng, LibreChat and its datastores, voice gateway, sandbox base images, every
base image, every lockfile, every skill/MCP server/plugin, every patch anchor,
every submodule. The list below is illustrative, not exhaustive. Nobody should
have to enumerate this for you — if you are wondering whether something counts,
it counts.

A component with no newer release is reported as *already latest, verified
against \<source\> on \<date\>*. A component simply MISSING from the table is a
failed run — silence is not evidence of currency, and that is exactly how seven
weeks of no-op upgrades went unnoticed.

Build a complete table of every upgradable thing in the repo. Include, at minimum:
- Container images in every compose file (gateway, Hermes, LibreChat, MongoDB/Meilisearch/RAG or whatever LibreChat depends on, docker-socket-proxy, sandbox base images, searxng, voice gateway, OpenClaw, monitoring/sidecars).
- Language dependencies: `package.json`/lockfiles, `pyproject.toml`/`requirements*.txt`/`uv.lock`, `go.mod`, etc. for every agent, component, and utility in the repo.
- Base images in any local `Dockerfile`s.
- Agent definitions, skills, MCP servers, plugins, and Claude Code / Hermes config that pin versions.
- Git submodules or vendored code.
- Tooling (Colima, Docker CLI, compose plugin) — report available updates but only apply them if the project docs say the Sunday job owns host tooling.

For each item: current version, latest stable version, source URL you used to determine it, and whether a changelog mentions breaking changes or security fixes.

**Do not determine "latest" from memory, from the changelog you happen to read,
or from a model's belief about what version exists.** For the two wrapped agents
this is mechanical and must be run, with its output pasted into the report:

```bash
python3 scripts/discover_upstream_versions.py            # human-readable
python3 scripts/discover_upstream_versions.py --json     # for the report
```

It resolves OpenClaw from the npm registry (the Dockerfile installs
`openclaw@${OPENCLAW_VERSION}` from npm and asserts the installed version
matches the pin, so npm is the source of truth) and Hermes from Docker Hub tags,
including the digest. Stable releases only — `-beta`/`-rc`/`-alpha` never ship
unattended, while a numeric `-N` suffix IS a real patch release.

If discovery reports UNKNOWN for a component, that is "could not determine",
never "already current". Treat it as a finding and resolve it — an unreachable
registry is a blocked run, not a clean one.

For everything else in the inventory, cite the command and its output (`npm view
<pkg> version`, `gh release list`, registry API, etc.). A version with no cited
source is not an answer.

### 2. Security findings
Collect every open security report before upgrading so you can verify closure afterwards:
- `npm audit` / `pnpm audit` / `pip-audit` / `uv` audit / `cargo audit` / `govulncheck` as applicable.
- Image scanning with whatever the repo already uses (Trivy, Grype, Docker Scout). If none is configured and `trivy` is available, use `trivy image` and `trivy fs`. Do not install new scanners on the host without a documented mechanism.
- GitHub Dependabot / code-scanning alerts via `gh` if the repo is on GitHub and `gh auth status` succeeds.
- Any findings files the project already maintains (`SECURITY.md`, `security/`, prior `reports/`).
- **Wazuh / SOC alerts**: review open alerts from the Wazuh sidecar and the gateway's SOC surface (`/soc/v1/...` endpoints, `/var/log/security/` reports) for anything raised since the last Sunday run — these count as findings to close or explicitly ACCEPT, same as scanner output.

Record every finding with ID (CVE/GHSA), severity, affected component, and fixed-in version.

### 2b. AgentShroud-side remediation — the vendor's fix is NOT the finish line

Owner directive 2026-09-15: **an upgrade alone does not close a CVE.** Upgrading
OpenClaw removes that flaw from OpenClaw; it does nothing for the next agent
AgentShroud proxies, or for the same flaw class reappearing next month. The
product thesis is that AgentShroud protects the agents behind it, so a CVE found
in ANY wrapped tool is a requirement against the gateway, independent of whether
the vendor has patched it.

So each Sunday, for every advisory in this run, do BOTH arms:

- **Arm 1 — vendor fix.** Upgrade to the fixed version (steps 1/3/4).
- **Arm 2 — AgentShroud control.** Classify the advisory and ask: *if a proxied
  agent had this flaw and no vendor patch existed, would AgentShroud stop the
  attack?* Run the triage, which already computes this per vulnerability class:

  ```bash
  python3 scripts/triage-cve-mitigations.py --apply
  ```

  Its `Coverage` verdict is the answer: `FULL` (controls neutralise the class),
  `PARTIAL` (residual gap), or `NONE` — **and `NONE` is a GAP, which is work,
  not a status to record and move on from.**

For every class returning `NONE` or `PARTIAL`, the gap becomes tracked work this
run: open a Jira issue (§6) describing the control AgentShroud needs, and
implement it where it is safely in scope. These controls belong at the gateway
so they apply to EVERY proxied agent — an allowlist the gateway enforces protects
a third-party agent that never had the vendor's patch at all.

Worked example from the 2026-09-15 registry, to make the shape concrete. These
OpenClaw advisories are all authorization bypasses:
`GHSA-58qx-6m8p-wh2j` (Slack group DMs could skip sender allowlists, 8.8),
`GHSA-rrxp-5mx8-mvhh` (inbound voice calls could inherit owner tool
authorization, 8.8), `GHSA-wwcw-jfpp-gpxw` (native tools could ignore per-chat
policy, 8.8), `GHSA-7cp7-87pj-p32v` (skill dispatch could skip owner-only
policy, 8.3). The vendor fix is "upgrade past 2026.8.1". The AgentShroud
requirement is different and outlives it: **sender allowlisting, tool
authorization, and per-chat policy must be enforced at the gateway, for any
agent, so that an agent which skips its own check is still stopped.**

Honesty rules, unchanged and non-negotiable:
- NEVER promote an advisory to `*_mitigated` without citing the specific control
  and, where a test can prove the block, the test. An uncited mitigation claim is
  the security theater §2 of CLAUDE.md forbids.
- `under_review` is an honest holding state, not an outcome. An advisory still in
  `under_review` at the end of a run is unfinished work and must appear in the
  report as such.

### 3. Upgrade DEV
0. **Act on discovery.** For every component where step 1 showed latest != current,
   edit the pin in `docker/versions.env` NOW. This is the step that was silently
   skipped for seven weeks. If you finish this section without having edited a
   pin, you must be able to paste discovery output proving every component was
   already latest — otherwise you have not done the job.

   **Needing a code change is NOT a reason to skip a bump** (owner directive,
   quoted in the ground rules). A new upstream release routinely breaks a patch
   anchor, a config path, or a build arg — this repo already carries patches that
   re-anchor against specific versions (e.g. the Hermes telegram `base_url` patch
   made tolerant of both v0.20.1 and v0.20.6 layouts). Fixing those anchors is
   YOUR job on this run: make the change, commit it, rebuild, verify. Escalate to
   BLOCKED only if the fix would require loosening a security control.

1. Apply all version bumps from the inventory to the **dev** configuration only. One commit per logical component so a bad bump can be reverted alone.
2. Regenerate lockfiles; rebuild any local images; `docker compose pull` and bring dev up.
3. Verify — all of the following must pass, with output captured in the report:
   - Every container reaches `healthy`/`running` and stays there for at least 2 minutes with no restart loop (`docker compose ps`, `docker compose logs --since 5m` grep for `error|panic|fatal|traceback`).
   - The project's own test suite / smoke tests / `make test` / `make check`, if any.
   - Gateway end-to-end: a request through the agentshroud-gateway reaches Hermes and returns; a request that policy should block is still blocked. Use the existing test scripts or health endpoints — do not invent new attack traffic.
   - Hermes can still spawn a `hermes-sandbox-*` container through the docker-socket-proxy and it is torn down afterwards.
   - LibreChat responds on its health endpoint and can reach the gateway.
   - Re-run all audits/scans from step 2. Every finding must be either FIXED (show it gone) or explicitly ACCEPTED with a reason (no fix released yet, not reachable in our configuration) — never silently dropped.
   - **Soak, not just boot.** `docker compose ps` healthy proves the process started — it does not prove anything actually WORKED (the 2026-09-18 postmortem: models.json/openai-local routing, the missing sandbox image, and two op-proxy allowlist gaps all shipped past a fully-green boot check because nothing exercised the code path that was actually broken until a real cron job hit it days later). Run `bash scripts/check-soak-status.sh` against dev's OpenClaw container and require it to report `SOAKED` — either by waiting for a real scheduled run, or by triggering one on demand (`openclaw cron run <id>` for a representative job, e.g. the main heartbeat) and re-checking. A `NOT_SOAKED` result with an `errored_since_boot` reason is a FAILED check for this run, same as any other — do not proceed to promote past it. (Hermes has no equivalent automated check yet — its cron CLI has no `--json` output; verify at least one real Hermes job manually and note that in the report as a known gap, not a skipped step.)
4. If any check fails: revert the specific commit(s) responsible, bring dev back up, re-verify, and mark that component FAILED with the error. Continue with the remaining components. If dev cannot be made healthy at all, restore the full baseline and stop — do not touch prod.

### 4. Promote to PROD
Proceed **only if** dev is fully healthy and every finding is FIXED or ACCEPTED.
0. **Prove dev and prod are about to build the same artifact.** "It passed in dev" means nothing if prod's checkout has drifted (stale pull, an unpushed local commit, a stray version override). Run `bash scripts/check-version-pins-parity.sh` in BOTH environments — dev's own checkout and prod's (via the `@agentshroud` coordination session, never by connecting to prod directly). Both must report `PASS` before proceeding. A `FAIL` means the checkouts have diverged; reconcile via the normal PR/merge flow before promoting, do not skip this and promote anyway.
1. Apply exactly the version set that passed on dev — no new versions, no components that failed on dev.
2. Take a backup of any stateful services before upgrading them (LibreChat/Mongo data, Hermes state/config volumes) using the project's backup script or `docker run --rm -v <vol>:/data -v ~/Development/<project>/backups:/backup alpine tar czf /backup/<vol>-YYYY-MM-DD.tgz /data`. Verify the archive is non-empty.
3. Bring prod up and run the same verification suite as step 3.3.
4. If prod verification fails: restore the baseline immediately (previous tags + previous commit), restore volumes only if data was migrated irreversibly, re-verify prod is healthy, and mark the promotion ROLLED BACK.

### 5. Cleanup
- `docker image prune` only images superseded by this run (keep the rollback baseline images for one week — do not prune them).
- Remove stopped sandbox containers left over from testing.
- Ensure no test artefacts, backups, or logs are staged for commit.

### 6. Jira tracking (standard procedure, owner directive 2026-08-30)
Every Sunday run is tracked in a Jira ticket (project **SCRUM**, cloudId
`7a044ff7-e2cf-40e6-b6f0-e3e080898fbb`) via the Atlassian MCP tools:

- **Dev run (03:00)**: at start, create the run ticket — summary
  `Sunday Upgrade YYYY-MM-DD`, description = planned scope from the inventory
  phase. Include the ticket key in the dev-result JSON (`"jira":"SCRUM-nnn"`)
  so the prod run finds it.
- **Connector**: use the plain `mcp__atlassian__*` tools with the cloudId
  above passed explicitly — the named connectors (atlassian-agentshroud /
  atlassian-idallasj) have broken OAuth on the prod account and would falsely
  trip the "MCP unavailable" path every run.
- **Both runs**: post a **detailed comment at the end of each phase**
  (inventory, scans, upgrade-per-component, verification, cleanup) — what was
  done, what changed, evidence snippets, and any FAILED/BLOCKED item with its
  reason. Comment as you go, not retroactively — a run that dies mid-way must
  leave a trail of exactly how far it got.
- **Prod run (06:00)**: comment on the SAME ticket from the dev-result JSON
  (never a new ticket): the promote/blocked decision, versions applied, and
  verification results.
- **On completion**: post a **comprehensive summary comment** mirroring the
  report sections below, then transition the ticket to Done only if the
  summary line is `ALL GREEN`; otherwise leave it open with a `needs-attention`
  label so the open ticket itself flags the follow-up.
- If the Atlassian MCP tools are unavailable in the session, say so explicitly
  in the report's manual follow-ups section — never silently skip Jira.

### 7. Report
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
