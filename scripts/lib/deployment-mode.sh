# shellcheck shell=bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
#
# scripts/lib/deployment-mode.sh — which agents AgentShroud governs on this host.
#
# This is a *sourced* library, not an executable. AGENTSHROUD_DEPLOYMENT is one of:
#   local   agents that run on this host (OpenClaw, Hermes). The default, so a host
#           that never sets it keeps the stack it has always had.
#   cloud   hosted personal agents only (Claude Duet, Poke, ...), which reach this
#           host through the Inbound MCP Edge. No local agent containers.
#   hybrid  both.
#
# scripts/asb uses it to pick containers; scripts/post-deploy-check.sh uses it to
# know which containers MUST be running, so a missing agent is a failure rather than
# a skipped check. Public exposure (Tailscale Funnel) and enabling any vendor are
# separate owner steps; no mode turns either on.

# deployment_mode_resolve [ENV_FILE] — print the mode, or fail closed.
# The environment wins; otherwise the last AGENTSHROUD_DEPLOYMENT= line of ENV_FILE
# (read as text, never sourced); otherwise "local".
deployment_mode_resolve() {
  local env_file="${1:-}" mode="${AGENTSHROUD_DEPLOYMENT:-}"
  if [ -z "$mode" ] && [ -n "$env_file" ] && [ -f "$env_file" ]; then
    mode="$(sed -n 's/^AGENTSHROUD_DEPLOYMENT=//p' "$env_file" | tail -1 | tr -d "\"'\r")"
  fi
  mode="${mode:-local}"
  case "$mode" in
    local | cloud | hybrid) printf '%s\n' "$mode" ;;
    *)
      echo "ERROR: AGENTSHROUD_DEPLOYMENT='$mode' — must be local, cloud or hybrid" >&2
      return 1
      ;;
  esac
}

deployment_runs_local_agents() { [ "$1" = local ] || [ "$1" = hybrid ]; }

deployment_runs_edge() { [ "$1" = cloud ] || [ "$1" = hybrid ]; }

# deployment_profile_flags MODE — global compose flags (before build/up).
deployment_profile_flags() {
  if deployment_runs_edge "$1"; then echo "--profile edge"; else echo ""; fi
}

# deployment_up_flags MODE — flags for `compose up`. OpenClaw has no compose
# profile (it is the default agent), so cloud mode scales it to zero.
deployment_up_flags() {
  if deployment_runs_local_agents "$1"; then echo ""; else echo "--scale openclaw=0"; fi
}
