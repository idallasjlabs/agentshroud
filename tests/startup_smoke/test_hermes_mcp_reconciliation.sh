#!/usr/bin/env bash
# Functional regression test: docker/bots/hermes/init-config.sh's MCP servers.json ->
# config.yaml reconciliation logic.
#
# Root cause this guards against (found 2026-08-01, live incident): the reconciliation
# was purely additive -- it only ever added/refreshed entries that servers.json marked
# enabled: true. It had NO code path to disable an entry already sitting in config.yaml
# from before servers.json was updated to disable it. docker/config/hermes/mcp/
# servers.json disabled "agentshroud-gateway" on 2026-07-18 (its url,
# http://gateway:8080/mcp, returns a genuine 404 -- the gateway has never served that
# endpoint), but the stale enabled:true copy already in the live config.yaml survived
# every boot since, causing ~213 failed MCP connection attempts/day indefinitely.
#
# This test extracts the actual embedded Python reconciliation logic from
# init-config.sh (not a reimplementation -- the real code under test) and runs it
# against fixture data, asserting: a stale enabled:true entry gets disabled when the
# source marks it enabled:false; re-running is idempotent; a fresh install with no
# mcp_servers key never picks up a disabled entry.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
INIT_SCRIPT="$REPO/docker/bots/hermes/init-config.sh"
WORKDIR="$(mktemp -d)"
trap 'rm -rf "$WORKDIR"' EXIT

fail=0
check() {
    local label="$1" condition="$2"
    if [[ "$condition" == "true" ]]; then
        echo "  OK : $label"
    else
        echo "  FAIL: $label" >&2
        fail=1
    fi
}

# Extract the embedded Python heredoc verbatim -- testing the REAL code, not a copy.
awk '/^import json, os, re, sys$/,/^PYEOF$/' "$INIT_SCRIPT" | sed '$d' > "$WORKDIR/reconcile.py"

if [[ ! -s "$WORKDIR/reconcile.py" ]]; then
    echo "  FAIL: could not extract reconciliation Python from $INIT_SCRIPT (heredoc markers changed?)" >&2
    exit 1
fi

cat > "$WORKDIR/servers.json" <<'EOF'
{
  "servers": {
    "agentshroud-gateway": {
      "description": "disabled - gateway never served this endpoint",
      "type": "http",
      "url": "http://gateway:8080/mcp",
      "enabled": false
    },
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp",
      "enabled": true
    }
  }
}
EOF

echo ""
echo "── Hermes MCP reconciliation: stale-disable regression ────────────────"

# Scenario 1: config.yaml has a STALE enabled:true copy of a now-disabled server
# (exactly the real incident state). Reconciliation must flip it to false.
cat > "$WORKDIR/config-stale.yaml" <<'EOF'
model:
  default: claude-opus-4-6
mcp_servers:
  agentshroud-gateway:
    url: http://gateway:8080/mcp
    enabled: true
  github:
    url: https://api.githubcopilot.com/mcp
    enabled: true
EOF

out="$(HERMES_MCP_SRC="$WORKDIR/servers.json" HERMES_MCP_CONFIG="$WORKDIR/config-stale.yaml" python3 "$WORKDIR/reconcile.py")"
check "reports the stale entry as changed/disabled" "$([[ "$out" == *"agentshroud-gateway"*"disabled"* ]] && echo true || echo false)"
check "agentshroud-gateway is enabled: false after reconciliation" \
    "$(grep -A2 '^  agentshroud-gateway:' "$WORKDIR/config-stale.yaml" | grep -q 'enabled: [Ff]alse' && echo true || echo false)"
check "github (still enabled upstream) is untouched and still enabled" \
    "$(grep -A2 '^  github:' "$WORKDIR/config-stale.yaml" | grep -q 'enabled: [Tt]rue' && echo true || echo false)"

# Scenario 2: idempotency -- re-running against the now-fixed config must be a no-op.
out2="$(HERMES_MCP_SRC="$WORKDIR/servers.json" HERMES_MCP_CONFIG="$WORKDIR/config-stale.yaml" python3 "$WORKDIR/reconcile.py")"
check "re-run is idempotent (UNCHANGED)" "$([[ "$out2" == "UNCHANGED" ]] && echo true || echo false)"

# Scenario 3: fresh install (no mcp_servers key at all) must never add the disabled
# entry in the first place.
cat > "$WORKDIR/config-fresh.yaml" <<'EOF'
model:
  default: claude-opus-4-6
EOF
HERMES_MCP_SRC="$WORKDIR/servers.json" HERMES_MCP_CONFIG="$WORKDIR/config-fresh.yaml" python3 "$WORKDIR/reconcile.py" >/dev/null
check "fresh install adds github" \
    "$(grep -q 'github:' "$WORKDIR/config-fresh.yaml" && echo true || echo false)"
check "fresh install never adds the disabled agentshroud-gateway entry" \
    "$(! grep -q 'agentshroud-gateway' "$WORKDIR/config-fresh.yaml" && echo true || echo false)"

# ── Stdlib fallback (no PyYAML) ─────────────────────────────────────────────
# Hermes 0.22.5's python3 (and /opt/hermes/.venv) has no PyYAML, so the live
# container always takes the text fallback. On prod (2026-10-26) the fallback's
# block-only header regex missed an inline `mcp_servers: {}` and appended a second
# bare `mcp_servers:`. Hermes then rejected config.yaml ("duplicate key
# mcp_servers") and ran on its last good settings, ignoring every later change.
# A stub yaml.py on PYTHONPATH forces the same ImportError the container hits.
mkdir -p "$WORKDIR/noyaml"
echo 'raise ImportError("PyYAML blocked: exercise the stdlib fallback")' > "$WORKDIR/noyaml/yaml.py"
reconcile_noyaml() {  # $1 servers.json, $2 config.yaml
    PYTHONPATH="$WORKDIR/noyaml" HERMES_MCP_SRC="$1" HERMES_MCP_CONFIG="$2" python3 "$WORKDIR/reconcile.py"
}
count_key() { grep -c '^mcp_servers:' "$1" || true; }

# Prod's servers.json: nothing enabled, one entry explicitly disabled.
cat > "$WORKDIR/servers-disabled-only.json" <<'EOF'
{"servers": {"agentshroud-gateway": {"type": "http", "url": "http://gateway:8080/mcp", "enabled": false}}}
EOF

echo ""
echo "── Hermes MCP reconciliation: stdlib fallback, inline/duplicate keys ──"

# F1: prod's exact shape, inline `{}` followed by more top-level keys.
printf 'plugins:\n  enabled:\n    - conduit_push\nmcp_servers: {}\nSEARXNG_URL: http://searxng-local:8080\n' > "$WORKDIR/f1.yaml"
reconcile_noyaml "$WORKDIR/servers-disabled-only.json" "$WORKDIR/f1.yaml" >/dev/null
check "F1 inline {} with nothing to add: still exactly one mcp_servers key" "$([[ "$(count_key "$WORKDIR/f1.yaml")" == 1 ]] && echo true || echo false)"
check "F1 keys after it are preserved" "$(grep -q '^SEARXNG_URL: http://searxng-local:8080$' "$WORKDIR/f1.yaml" && echo true || echo false)"

# F2: inline `{}` with trailing spaces and a comment, and a server to add.
printf 'model:\n  default: x\nmcp_servers: {}   # managed by init\nother: 1\n' > "$WORKDIR/f2.yaml"
reconcile_noyaml "$WORKDIR/servers.json" "$WORKDIR/f2.yaml" >/dev/null
check "F2 inline {} + comment: exactly one mcp_servers key" "$([[ "$(count_key "$WORKDIR/f2.yaml")" == 1 ]] && echo true || echo false)"
check "F2 github added under it" "$(grep -A2 '^  github:' "$WORKDIR/f2.yaml" | grep -q 'enabled: true' && echo true || echo false)"
check "F2 keys after it are preserved" "$(grep -q '^other: 1$' "$WORKDIR/f2.yaml" && echo true || echo false)"

# F3: inline NON-empty flow mapping. The fallback cannot parse it safely, so it
# must leave the file byte-identical rather than append a duplicate.
printf 'mcp_servers: {github: {url: https://example.invalid, enabled: true}}\nother: 1\n' > "$WORKDIR/f3.yaml"
cp "$WORKDIR/f3.yaml" "$WORKDIR/f3.orig"
reconcile_noyaml "$WORKDIR/servers.json" "$WORKDIR/f3.yaml" >/dev/null
check "F3 inline non-empty mapping: file left untouched" "$(cmp -s "$WORKDIR/f3.yaml" "$WORKDIR/f3.orig" && echo true || echo false)"

# F4: an already-duplicated file (prod's state after the bad boot) collapses to one.
printf 'mcp_servers: {}\nSEARXNG_URL: http://searxng-local:8080\n\nmcp_servers:\n' > "$WORKDIR/f4.yaml"
reconcile_noyaml "$WORKDIR/servers-disabled-only.json" "$WORKDIR/f4.yaml" >/dev/null
check "F4 duplicate mcp_servers keys collapse to one" "$([[ "$(count_key "$WORKDIR/f4.yaml")" == 1 ]] && echo true || echo false)"
check "F4 SEARXNG_URL survives the collapse" "$(grep -q '^SEARXNG_URL:' "$WORKDIR/f4.yaml" && echo true || echo false)"
check "F4 the surviving key is never a bare null" "$(! grep -qE '^mcp_servers:[[:space:]]*$' "$WORKDIR/f4.yaml" || grep -qE '^  [^ ]' "$WORKDIR/f4.yaml" && echo true || echo false)"

# F5: existing block form still reconciles under the fallback (stale-disable case).
cp "$WORKDIR/config-stale.yaml" "$WORKDIR/f5.yaml"
sed -i.bak 's/enabled: [Ff]alse/enabled: true/' "$WORKDIR/f5.yaml"
reconcile_noyaml "$WORKDIR/servers.json" "$WORKDIR/f5.yaml" >/dev/null
check "F5 block form: one key, agentshroud-gateway disabled" \
    "$([[ "$(count_key "$WORKDIR/f5.yaml")" == 1 ]] && grep -A2 '^  agentshroud-gateway:' "$WORKDIR/f5.yaml" | grep -q 'enabled: false' && echo true || echo false)"

# F6: no key at all, nothing to add: exactly one key is written, never a bare null.
printf 'model:\n  default: x\n' > "$WORKDIR/f6.yaml"
reconcile_noyaml "$WORKDIR/servers-disabled-only.json" "$WORKDIR/f6.yaml" >/dev/null
check "F6 no key: exactly one mcp_servers key added" "$([[ "$(count_key "$WORKDIR/f6.yaml")" == 1 ]] && echo true || echo false)"
check "F6 empty result is written as {} (not null)" "$(grep -qE '^mcp_servers: \{\}$' "$WORKDIR/f6.yaml" && echo true || echo false)"

# F7: every fallback fixture is a fixed point: a second run changes nothing.
idem=true
for f in f1 f2 f3 f4 f5 f6; do
    src="$WORKDIR/servers.json"; [[ "$f" == f1 || "$f" == f4 || "$f" == f6 ]] && src="$WORKDIR/servers-disabled-only.json"
    cp "$WORKDIR/$f.yaml" "$WORKDIR/$f.run1"
    out="$(reconcile_noyaml "$src" "$WORKDIR/$f.yaml")"
    if ! cmp -s "$WORKDIR/$f.yaml" "$WORKDIR/$f.run1" || [[ "$out" == CHANGED* ]]; then idem=false; echo "    not idempotent: $f ($out)" >&2; fi
done
check "F7 second run is byte-identical and reports no change, for F1-F6" "$idem"

echo ""
if [[ "$fail" -eq 0 ]]; then
    echo "  ALL CHECKS PASSED"
    exit 0
else
    echo "  ONE OR MORE CHECKS FAILED" >&2
    exit 1
fi
