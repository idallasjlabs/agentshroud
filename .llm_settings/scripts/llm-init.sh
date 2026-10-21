#!/bin/bash
# llm-init.sh
#
# Deploy LLM AI tool configurations to a repository
# This sets up Claude Code (PRIMARY), Gemini CLI (SECONDARY),
# Codex CLI (TERTIARY), and GitHub Copilot CLI (QUATERNARY)
# Plus comprehensive security infrastructure
#
# Usage:
#   source llm-init.sh              # Load function into shell
#   llm-init                        # Deploy to current directory
#   llm-init /path/to/repo          # Deploy to specific directory
#   llm-init --dry-run              # Preview without making changes
#   llm-init -n /path/to/repo       # Dry run to specific directory
#   llm-init --mcp github --mcp atlassian-fluence . # Pin specific MCP servers
#   llm-init --mcp all .                            # Deploy all MCP servers
#   llm-init --mcp twg .                            # Check/report Atlassian Teamwork
#                                                    # Graph CLI status (opt-in, global,
#                                                    # not a per-repo MCP server — see
#                                                    # _llm_init_check_twg)

# zsh compatibility: avoid alias expansion conflict on function name
unalias llm-init 2>/dev/null || true

# Repos (matched by normalized git remote, not local path — the same repo
# is checked out at different paths on different hosts, e.g.
# ~/Development/services-data-lake on the dev machine vs.
# /home/dde/Production/services-data-lake on a production host) that require
# the impact-analysis push gate (see require_impact_analysis.sh). Add an
# entry here to turn the gate on for another repo; do not create or remove
# .impact-analysis-required by hand — _llm_init_ensure_production_gate_marker
# manages it.
PRODUCTION_GATE_REMOTES=(
    "FITDevOps/services-data-lake"
)

# ─────────────────────────────────────────────────────────────────────────────
# _llm_init_reconcile_settings_local <dry_run> <json_key>...
#
# After _llm_init_render_mcp has filtered .mcp.json, reconciles
# .claude/settings.local.json so selected servers are enabled:
#
#   1. Removes selected JSON keys from disabledMcpjsonServers (clears Claude Code
#      auto-deny entries that would silently block the selected servers).
#   2. Rebuilds enabledMcpjsonServers:
#        (existing entries ∩ live .mcp.json keys) ∪ selected
#      This prunes stale names (e.g. "github", "atlassian" → "github-fluence")
#      and ensures selected servers are present.
#   3. If settings.local.json does not exist, creates a minimal file with
#      enabledMcpjsonServers set to the selected keys only.
#
# Idempotent. No-op if jq is absent.
# ─────────────────────────────────────────────────────────────────────────────
_llm_init_reconcile_settings_local() {
    local _dry_run="$1"
    shift
    local -a _json_keys=("$@")
    local _settings=".claude/settings.local.json"

    if [ ${#_json_keys[@]} -eq 0 ]; then return 0; fi

    if ! command -v jq >/dev/null 2>&1; then
        echo "   ⚠️  [reconcile-settings] jq not found — $_settings not updated" >&2
        return 0
    fi

    # Build JSON array of selected keys
    local _sel_json
    _sel_json="$(printf '"%s",' "${_json_keys[@]}")"
    _sel_json="[${_sel_json%,}]"

    if [ ! -f "$_settings" ]; then
        if [ "$_dry_run" = "true" ]; then
            echo "   ℹ️  [dry-run] Would create $_settings with enabledMcpjsonServers: ${_json_keys[*]}"
        else
            printf '%s' "{\"enabledMcpjsonServers\": ${_sel_json}}" | jq . > "$_settings"
            echo "      ✅ $_settings (created with enabledMcpjsonServers)"
        fi
        return 0
    fi

    if [ "$_dry_run" = "true" ]; then
        echo "   ℹ️  [dry-run] Would reconcile $_settings: enable ${_json_keys[*]}"
        return 0
    fi

    # Get the live .mcp.json keys (canonical truth after filtering)
    local _live_keys="[]"
    if [ -f ".mcp.json" ]; then
        _live_keys="$(jq '[.mcpServers | keys[]]' .mcp.json 2>/dev/null || echo '[]')"
    fi

    local _tmp="${_settings}.rnd.$$"
    local _err="${_settings}.err.$$"

    if jq --argjson sel "$_sel_json" \
          --argjson live "$_live_keys" '
        # 1. Remove selected from disabledMcpjsonServers; drop the key if it becomes empty
        if .disabledMcpjsonServers then
            .disabledMcpjsonServers = (.disabledMcpjsonServers - $sel)
            | if (.disabledMcpjsonServers | length) == 0
              then del(.disabledMcpjsonServers) else . end
        else . end |
        # 2. Rebuild enabledMcpjsonServers:
        #    keep existing entries only if they still exist in live .mcp.json,
        #    then union with selected (deduplicated, sorted for stability)
        if .enabledMcpjsonServers then
            .enabledMcpjsonServers = (
                [ (.enabledMcpjsonServers // [])[]
                  | select(. as $e | $live | any(. == $e)) ]
                + $sel
                | unique
            )
        else
            .enabledMcpjsonServers = ($sel | unique)
        end
    ' "$_settings" > "$_tmp" 2>"$_err"; then
        if jq empty "$_tmp" 2>/dev/null; then
            # Use \mv to bypass 'mv -i' aliases that would prompt for confirmation
            \mv -f "$_tmp" "$_settings"
            rm -f "$_err"
            echo "      ✅ $_settings (MCP reconcile: enabled ${_json_keys[*]})"
        else
            rm -f "$_tmp"
            echo "   ❌ [reconcile-settings] jq produced invalid JSON — $_settings unchanged" >&2
            [ -s "$_err" ] && cat "$_err" >&2
            rm -f "$_err"
        fi
    else
        rm -f "$_tmp"
        echo "   ❌ [reconcile-settings] jq failed — $_settings unchanged" >&2
        [ -s "$_err" ] && cat "$_err" >&2
        rm -f "$_err"
    fi
}

# ─────────────────────────────────────────────────────────────────────────────
# Additional CLIs: OpenCode, Crush, Google Antigravity (agy), Grok Build, Pi, Oh My Pi
#
# Per-repo deployment next to the Claude/Gemini/Codex/Copilot output. Claude's
# `.mcp.json` (already filtered by _llm_init_render_mcp, gmail-<alias> included)
# is the single source of truth: each tool's MCP file is DERIVED from it with jq,
# so --mcp fluence|personal|all|gmail applies to every tool with no extra wiring.
#
#   tool      skills                 agents                 MCP file (schema)
#   opencode  .agents/skills¹        .opencode/agents/      opencode.json  mcp{type:local,command[],environment}
#   crush     .agents/skills         — (none documented)    .crush.json    mcp{type:stdio,command,args,env}
#   agy       .agents/skills         .agents/agents/        .agents/plugins/llm-settings/mcp_config.json  mcpServers{command,args,env}
#   grok      .claude/skills (native) .claude/agents (native) .grok/config.toml  [mcp_servers.<n>] (marked block)
#   pi        .agents/skills         — (no sub-agents)      .pi/mcp.json   mcpServers{command,args,env}
#   omp       .agents/skills         .omp/agents/           .omp/mcp.json  mcpServers{command,args,env}
#   ¹ OpenCode also reads .claude/skills; AGENTS.md (already synced) is the context file for all.
#
# --tools a,b,c|all selects the set (Claude is always deployed — it feeds the rest).
# ─────────────────────────────────────────────────────────────────────────────
_LLM_INIT_ALL_TOOLS="claude codex gemini copilot opencode crush agy grok pi omp cursor"
_LLM_INIT_TOOLS=" $_LLM_INIT_ALL_TOOLS "

# _llm_init_parse_tools <csv> — validates and sets _LLM_INIT_TOOLS. rc 2 on bad input.
_llm_init_parse_tools() {
    local _csv="${1:-}" _item _t _sel=" "
    local -a _items=()
    if [ -z "${_csv//[[:space:]]/}" ]; then
        echo "llm-init: --tools requires a value" >&2
        echo "          valid: ${_LLM_INIT_ALL_TOOLS// / | } | all" >&2
        return 2
    fi
    IFS=',' read -r -a _items <<< "$_csv"
    for _item in ${_items[@]+"${_items[@]}"}; do
        _t="$(printf '%s' "$_item" | tr '[:upper:]' '[:lower:]' | tr -d '[:space:]')"
        [ -z "$_t" ] && continue
        if [ "$_t" = "all" ]; then
            _sel=" $_LLM_INIT_ALL_TOOLS "
            continue
        fi
        case " $_LLM_INIT_ALL_TOOLS " in
            *" $_t "*) ;;
            *)
                echo "llm-init: unknown --tools value: '${_t}'" >&2
                echo "          valid: ${_LLM_INIT_ALL_TOOLS// / | } | all" >&2
                return 2 ;;
        esac
        case "$_sel" in *" $_t "*) ;; *) _sel="${_sel}${_t} " ;; esac
    done
    case "$_sel" in *" claude "*) ;; *) _sel=" claude${_sel}" ;; esac   # Claude is always deployed
    _LLM_INIT_TOOLS="$_sel"
}

# _llm_init_tool_enabled <tool> — rc 0 if the tool is in the current selection.
_llm_init_tool_enabled() {
    case " ${_LLM_INIT_TOOLS} " in *" ${1:-} "*) return 0 ;; esac
    return 1
}

# _llm_init_any_tool_enabled <tool>... — rc 0 if at least one is selected.
_llm_init_any_tool_enabled() {
    local _t
    for _t in "$@"; do
        _llm_init_tool_enabled "$_t" && return 0
    done
    return 1
}

# _llm_init_normalize_skill_name <SKILL.md> <dirname>
# Agent-skill loaders (OpenCode, Pi, agy, ...) require frontmatter `name` == the
# directory name. Rewrites (or adds) it in the DEPLOYED copy only; a file with no
# frontmatter gets a minimal one (name + first-heading description). Idempotent.
_llm_init_normalize_skill_name() {
    local _f="$1" _name="$2" _tmp _has_name _d
    [ -f "$_f" ] || return 0
    _tmp="$(mktemp "${TMPDIR:-/tmp}/llm-init-skillname.XXXXXX")" || return 0
    if [ "$(head -1 "$_f")" = "---" ]; then
        _has_name="$(awk 'NR==1{next} /^---[[:space:]]*$/{exit} /^name:/{print 1; exit}' "$_f")"
        if [ -n "$_has_name" ]; then
            awk -v n="$_name" '
                NR==1 { print; fm=1; next }
                fm==1 && /^---[[:space:]]*$/ { fm=2 }
                fm==1 && /^name:/ { print "name: " n; next }
                { print }
            ' "$_f" > "$_tmp"
        else
            awk -v n="$_name" 'NR==1 { print; print "name: " n; next } { print }' "$_f" > "$_tmp"
        fi
    else
        _d="$(grep -m1 '^# ' "$_f" | sed 's/^# //; s/\\/\\\\/g; s/"/\\"/g')"
        [ -n "$_d" ] || _d="${_name} skill"
        { printf -- '---\nname: %s\ndescription: "%s"\n---\n\n' "$_name" "$_d"; cat "$_f"; } > "$_tmp"
    fi
    cmp -s "$_tmp" "$_f" || cat "$_tmp" > "$_f"   # write in place: keeps mode/inode
    rm -f "$_tmp"
}

# Skill folder names. Agent-skill loaders (OpenCode, Crush, Grok, omp, Copilot, Pi, agy…) want the
# folder named after the skill (frontmatter name == folder, lowercase-hyphen, <=64 chars) and several
# of them also scan .claude/skills. Source folders are i-* but 22 skills declare a different name
# (i-aws → "aws"). So every managed skill is deployed under its effective NAME in both
# .claude/skills and .agents/skills: Claude Code's command is unchanged (it already uses the
# frontmatter name, else the folder) and every tool sees the same valid, duplicate-free set.
_LLM_INIT_SKILL_MAP=""

# _llm_init_skill_dest_name <SKILL.md> <source-dir-name> — effective name (folder name if the
# frontmatter name is missing or not a valid skill name).
_llm_init_skill_dest_name() {
    local _f="$1" _d="$2" _n=""
    if [ -f "$_f" ]; then
        _n="$(awk 'NR == 1 && $0 != "---" { exit } NR > 1 && $0 == "---" { exit }
            /^name:/ { sub(/^name:[ \t]*/, ""); gsub(/["\r]/, ""); sub(/[ \t]+$/, ""); print; exit }' "$_f")"
    fi
    if [ -n "$_n" ] && [ "${#_n}" -le 64 ] && [[ "$_n" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
        printf '%s' "$_n"
    else
        [ -n "$_n" ] && echo "   ⚠️  [skills] ${_d}: name '${_n}' is not a valid skill name — using the folder name" >&2
        printf '%s' "$_d"
    fi
}

# _llm_init_skill_map_load <llm_settings_src> — sets _LLM_INIT_SKILL_MAP ("<folder> <name>" lines)
# over ALL source skills (not just the profile) so names stay stable across profiles. The first
# skill (alphabetical) keeps a shared name; later claimants fall back to their folder, with a warning.
_llm_init_skill_map_load() {
    local _src="$1" _sd _d _n _seen=" "
    _LLM_INIT_SKILL_MAP=""
    for _sd in "$_src/skills"/*/; do
        [ -f "${_sd}SKILL.md" ] || continue
        _d="$(basename "$_sd")"
        _n="$(_llm_init_skill_dest_name "${_sd}SKILL.md" "$_d")"
        case "$_seen" in
            *" $_n "*)
                echo "   ⚠️  [skills] ${_d}: name '${_n}' is already used by another skill — using the folder name" >&2
                _n="$_d" ;;
        esac
        _seen="${_seen}${_n} "
        _LLM_INIT_SKILL_MAP="${_LLM_INIT_SKILL_MAP}${_d} ${_n}"$'\n'
    done
    return 0
}

# _llm_init_skill_name_for <source-dir-name> — deployed name (the folder itself if unmapped).
_llm_init_skill_name_for() {
    local _want="$1" _k _v
    while IFS=' ' read -r _k _v; do
        if [ "$_k" = "$_want" ]; then printf '%s' "$_v"; return 0; fi
    done <<< "$_LLM_INIT_SKILL_MAP"
    printf '%s' "$_want"
}

# _llm_init_deploy_shared_skills <dry_run> <llm_settings_src> <profile>
# Copies the profile-allowed skills into .agents/skills/<name>/ (the cross-tool
# directory read by Gemini CLI, OpenCode, Crush, agy, Pi, Oh My Pi and Cursor) with names normalized.
# Never wipes the directory (other tools install their own skills there); it only
# removes skills this repo manages but the profile excludes.
_llm_init_deploy_shared_skills() {
    local _dry="${1:-false}" _src="${2:-}" _profile="${3:-all}" _sd _n _count=0
    if ! _llm_init_any_tool_enabled gemini opencode crush agy pi omp cursor; then
        echo "   ⏭️  .agents/skills skipped (no selected tool reads it)"
        return 0
    fi
    if [ -z "$_src" ] || [ ! -d "$_src/skills" ]; then
        echo "   ⚠️  skills source not found — .agents/skills not deployed" >&2
        return 0
    fi
    [ "$_dry" = "true" ] || mkdir -p .agents/skills
    _llm_init_skill_map_load "$_src" 2>/dev/null
    local _dn
    for _sd in "$_src/skills"/*/; do
        _n="$(basename "$_sd")"
        [ -f "${_sd}SKILL.md" ] || continue
        _dn="$(_llm_init_skill_name_for "$_n")"
        # legacy folder from before skills were deployed under their name (managed folders only)
        if [ "$_dn" != "$_n" ] && [ "$_dry" != "true" ] && [ -d ".agents/skills/$_n" ]; then
            rm -rf ".agents/skills/$_n"
        fi
        if _llm_init_skill_allowed "$_n" "$_profile" "$_src"; then
            if [ "$_dry" != "true" ]; then
                mkdir -p ".agents/skills/$_dn"
                rsync -a "$_sd" ".agents/skills/$_dn/"
                _llm_init_normalize_skill_name ".agents/skills/$_dn/SKILL.md" "$_dn"
            fi
            _count=$((_count + 1))
        elif [ "$_dry" != "true" ] && [ -d ".agents/skills/$_dn" ]; then
            rm -rf ".agents/skills/$_dn"
        fi
    done
    echo "   ✅ .agents/skills/ synchronized ($_count skills [$_profile profile], names normalized)"
}

# _llm_init_gemini_dedupe_commands <dry_run>
# Gemini CLI turns every .agents/skills/<name> into the slash command /<name>. A generated
# .gemini/commands/<name>.toml with the same name makes Gemini rename both (/workspace.<name>
# and /<name>1), so the command is removed wherever a shared skill provides it. Commands for
# agents without a same-named skill stay.
_llm_init_gemini_dedupe_commands() {
    local _dry="${1:-false}" _c _n _k=0
    _llm_init_tool_enabled gemini || return 0
    [ -d .gemini/commands ] || return 0
    for _c in .gemini/commands/*.toml; do
        [ -f "$_c" ] || continue
        _n="$(basename "$_c" .toml)"
        [ -f ".agents/skills/$_n/SKILL.md" ] || continue
        [ "$_dry" = "true" ] || rm -f "$_c"
        _k=$((_k + 1))
    done
    [ "$_k" -gt 0 ] && echo "   ✅ .gemini/commands: $_k commands left to their .agents/skills skill (no name clashes)"
    return 0
}

# _llm_init_convert_agent <opencode|agy|omp|cursor> <src.md> <dest_dir> [name]
# Writes <dest_dir>/<name>.md with the minimal documented frontmatter for the tool:
#   opencode: description + mode: subagent        (name = filename)
#   agy:      name + description + model: inherit
#   cursor:   name + description + model: inherit   (same shape as agy; .cursor/agents)
#   omp:      name + description                 (reserved names main/sub renamed)
# Input is normalized (BOM/CRLF) and a missing description falls back to the first H1.
_llm_init_convert_agent() {
    local _tool="$1" _src="$2" _dest="$3" _override="${4:-}"
    local _fn _name _norm _desc _body
    _fn="$(basename "$_src")"
    [ "$_fn" = "README.md" ] && return 0
    _name="${_override:-${_fn%.md}}"
    _name="$(printf '%s' "$_name" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9_-]/-/g')"
    if [ "$_tool" = "omp" ]; then
        case "$_name" in main|sub) _name="${_name}-agent" ;; esac
    fi
    _norm="$(mktemp "${TMPDIR:-/tmp}/llm-init-agent.XXXXXX")" || return 0
    _llm_init_normalize_md "$_src" "$_norm"
    if [ "$(head -1 "$_norm")" = "---" ]; then
        _desc="$(awk '
            BEGIN{f=0; in_desc=0; line=""; done=0}
            /^---$/{f++; next}
            f==1 && /^description:/{
                in_desc=1
                sub(/^description:[[:space:]]*/,"")
                sub(/^[>|][[:space:]]*/,"")
                line=$0
                next
            }
            f==1 && in_desc && /^[[:space:]]/{
                sub(/^[[:space:]]*/,"")
                line=line " " $0
                next
            }
            f==1 && in_desc && !done{ done=1; print line; exit }
            f==2 && in_desc && !done{ done=1; print line; exit }
            END{ if(in_desc && !done && line!="") print line }
        ' "$_norm")"
        _body="$(awk 'BEGIN{count=0} /^---$/{count++; if(count==2){found=1; next}} found{print}' "$_norm")"
    else
        _desc=""
        _body="$(cat "$_norm")"
    fi
    [ -n "$_desc" ] || _desc="$(grep -m1 '^# ' "$_norm" | sed 's/^# //')"
    [ -n "$_desc" ] || _desc="${_name} agent"
    _desc="$(printf '%s' "$_desc" | sed "s/^[>|\"'[:space:]]*//" | sed "s/[[:space:]\"']*\$//" | tr '\n' ' ' | sed 's/  */ /g')"
    _desc="${_desc//\\/\\\\}"
    _desc="${_desc//\"/\\\"}"
    mkdir -p "$_dest"
    {
        printf -- '---\n'
        case "$_tool" in
            opencode) printf 'description: "%s"\nmode: subagent\n' "$_desc" ;;
            agy|cursor) printf 'name: %s\ndescription: "%s"\nmodel: inherit\n' "$_name" "$_desc" ;;
            omp)      printf 'name: %s\ndescription: "%s"\n' "$_name" "$_desc" ;;
        esac
        printf -- '---\n\n'
        printf '%s\n' "$_body"
    } > "${_dest}/${_name}.md"
    rm -f "$_norm"
}

# _llm_init_deploy_tool_agents <dry_run> <llm_settings_src> <profile>
# Agents for OpenCode (.opencode/agents), agy (.agents/agents), Oh My Pi (.omp/agents),
# from the same inputs the Gemini/Copilot converters use: allowed skills + agents/*.md.
_llm_init_deploy_tool_agents() {
    local _dry="${1:-false}" _src="${2:-}" _profile="${3:-all}"
    local _tool _dest _sd _n _af _count
    [ -n "$_src" ] || return 0
    for _tool in opencode agy omp cursor; do
        _llm_init_tool_enabled "$_tool" || continue
        case "$_tool" in
            opencode) _dest=".opencode/agents" ;;
            agy)      _dest=".agents/agents" ;;
            cursor)   _dest=".cursor/agents" ;;
            omp)      _dest=".omp/agents" ;;
        esac
        _count=0
        if [ "$_dry" = "true" ]; then
            echo "   ℹ️  [dry-run] Would deploy $_tool agents → $_dest/"
            continue
        fi
        mkdir -p "$_dest"
        _llm_init_skill_map_load "$_src" 2>/dev/null
        local _dn
        for _sd in "$_src/skills"/*/; do
            _n="$(basename "$_sd")"
            [ -f "${_sd}SKILL.md" ] || continue
            _dn="$(_llm_init_skill_name_for "$_n")"
            if [ "$_dn" != "$_n" ]; then rm -f "${_dest}/${_n}.md"; fi
            if _llm_init_skill_allowed "$_n" "$_profile" "$_src"; then
                _llm_init_convert_agent "$_tool" "${_sd}SKILL.md" "$_dest" "$_dn"
                _count=$((_count + 1))
            else
                rm -f "${_dest}/${_dn}.md"
            fi
        done
        if [ -d "$_src/agents" ]; then
            for _af in "$_src/agents"/*.md; do
                [ -f "$_af" ] || continue
                case "$(basename "$_af")" in _*|README.md) continue ;; esac
                _llm_init_convert_agent "$_tool" "$_af" "$_dest"
                _count=$((_count + 1))
            done
        fi
        echo "   ✅ $_dest/ synchronized ($_count agents)"
    done
}

# _llm_init_agent_reference_paths <dry_run> <llm_settings_src>
# An agent is one file, so a skill's `references/…` (shipped next to its SKILL.md) is not
# beside it: point every agent built from such a skill at .llm_settings/skills/<n>/references/.
_llm_init_agent_reference_paths() {
    local _dry="${1:-false}" _src="${2:-}" _sd _n _dn _d _f _k=0
    [ "$_dry" = "true" ] && return 0
    [ -n "$_src" ] && [ -d "$_src/skills" ] || return 0
    _llm_init_skill_map_load "$_src" 2>/dev/null
    for _sd in "$_src/skills"/*/; do
        [ -d "${_sd}references" ] || continue
        _n="$(basename "$_sd")"
        _dn="$(_llm_init_skill_name_for "$_n")"
        for _d in .claude/agents .codex/agents .gemini/agents .gemini/agent-prompts .github/agents \
                  .github/agent-prompts .opencode/agents .agents/agents .omp/agents .cursor/agents; do
            for _f in "$_d/$_n.md" "$_d/$_dn.md" "$_d/$_n.agent.md"; do
                [ -f "$_f" ] && grep -q -e '`references/' -e '(next to this file)' "$_f" || continue
                sed -e "s#\`references/#\`.llm_settings/skills/$_n/references/#g" \
                    -e 's# (next to this file)##g' "$_f" > "$_f.ref.$$" && \mv -f "$_f.ref.$$" "$_f"
                _k=$((_k + 1))
            done
        done
    done
    [ "$_k" -gt 0 ] && echo "   ✅ agents: $_k reference pointers set to .llm_settings/skills/<skill>/references/"
    return 0
}

# ── MCP emitters: derive each tool's MCP file from the canonical .mcp.json ──
# Claude-only keys (timeout, trust) are dropped. Every emitter warns and returns 0
# on problems (never fails llm-init) and never clobbers an unreadable user file.
_LLM_INIT_JQ_STD='def std: with_entries(.value |= ({command: .command, args: (.args // [])} + (if ((.env // {}) | length) > 0 then {env: .env} else {} end)));'

# _llm_init_mcp_src_ok <tool> — rc 0 if .mcp.json is usable; warns otherwise.
_llm_init_mcp_src_ok() {
    if [ -f .mcp.json ] && command -v jq >/dev/null 2>&1 \
        && jq -e '.mcpServers | type == "object"' .mcp.json >/dev/null 2>&1; then
        return 0
    fi
    echo "   ⚠️  [mcp-emit] .mcp.json missing/invalid (or jq not found) — $1 MCP config not written" >&2
    return 1
}

# _llm_init_emit_std_json <tool> <dest> — fully-owned {mcpServers:{n:{command,args,env}}} file.
_llm_init_emit_std_json() {
    local _tool="$1" _dest="$2" _tmp
    _llm_init_mcp_src_ok "$_tool" || return 0
    mkdir -p "$(dirname "$_dest")"
    _tmp="${_dest}.$$.tmp"
    if jq "${_LLM_INIT_JQ_STD}"' {mcpServers: (.mcpServers | std)}' .mcp.json > "$_tmp" 2>/dev/null \
        && jq empty "$_tmp" 2>/dev/null; then
        \mv -f "$_tmp" "$_dest"
        echo "      ✅ $_dest"
    else
        rm -f "$_tmp"
        echo "   ⚠️  [mcp-emit] could not write $_dest" >&2
    fi
    return 0
}

# Antigravity (agy) reads MCP only from ~/.gemini/config/mcp_config.json (user scope) or from a
# plugin's mcp_config.json — a workspace .agents/mcp_config.json is never loaded. So the repo's
# servers ship as the workspace plugin .agents/plugins/llm-settings (tools appear as
# llm-settings_<server>). The plugin's MCP working directory is undocumented, so repo-relative
# commands (./x, .llm_settings/…) are made absolute; bare PATH names (uvx, npx) stay as-is.
_llm_init_mcp_emit_agy() {
    local _dir=".agents/plugins/llm-settings" _dest _tmp
    _dest="${_dir}/mcp_config.json"
    rm -f .agents/mcp_config.json            # legacy llm-init output; agy never read it
    _llm_init_mcp_src_ok agy || return 0
    mkdir -p "$_dir"
    _tmp="${_dest}.$$.tmp"
    # agy starts plugin servers with the plugin folder as cwd: make repo-relative commands
    # relative to it (three levels up is the repo root), never host-specific absolute paths.
    if jq "${_LLM_INIT_JQ_STD}"' {mcpServers: (.mcpServers | std
            | with_entries(.value.command |= (if (startswith("/") | not) and test("/") then "../../../" + ltrimstr("./") else . end)))}' \
            .mcp.json > "$_tmp" 2>/dev/null && jq empty "$_tmp" 2>/dev/null; then
        \mv -f "$_tmp" "$_dest"
        printf '{\n  "name": "llm-settings"\n}\n' > "${_dir}/plugin.json"
        echo "      ✅ $_dest"
    else
        rm -f "$_tmp"
        echo "   ⚠️  [mcp-emit] could not write $_dest" >&2
    fi
    return 0
}

# Cursor CLI: .cursor/mcp.json (fully owned); its interpolation syntax is ${env:VAR}.
_llm_init_mcp_emit_cursor() {
    local _dest=".cursor/mcp.json" _tmp
    _llm_init_mcp_src_ok cursor || return 0
    mkdir -p .cursor
    _tmp="${_dest}.$$.tmp"
    if jq "${_LLM_INIT_JQ_STD}"' def envconv: gsub("\\$\\{(?<v>[A-Za-z_][A-Za-z0-9_]*)\\}"; "${env:\(.v)}");
            def conv: if type == "string" then envconv else . end;
            {mcpServers: (.mcpServers | std | with_entries(.value |= (
                .command |= conv | .args |= map(conv)
                | if has("env") then .env |= map_values(conv) else . end)))}' .mcp.json > "$_tmp" 2>/dev/null \
        && jq empty "$_tmp" 2>/dev/null; then
        \mv -f "$_tmp" "$_dest"
        echo "      ✅ $_dest"
    else
        rm -f "$_tmp"
        echo "   ⚠️  [mcp-emit] could not write $_dest" >&2
    fi
    return 0
}
_llm_init_mcp_emit_pi()  { _llm_init_emit_std_json pi .pi/mcp.json; }
_llm_init_mcp_emit_omp() { _llm_init_emit_std_json omp .omp/mcp.json; }

# _llm_init_emit_merge_json <tool> <dest> <jq-body>
# Keeps every key of <dest> except those <jq-body> sets (it receives the user's file as
# $base and `.mcpServers` as input). Invalid existing file → warn, leave untouched.
_llm_init_emit_merge_json() {
    local _tool="$1" _dest="$2" _body="$3" _base="{}" _tmp
    _llm_init_mcp_src_ok "$_tool" || return 0
    if [ -f "$_dest" ]; then
        if jq -e 'type == "object"' "$_dest" >/dev/null 2>&1; then
            _base="$(cat "$_dest")"
        else
            echo "   ⚠️  [mcp-emit] $_dest is not a valid JSON object — left unchanged" >&2
            return 0
        fi
    fi
    mkdir -p "$(dirname "$_dest")"
    _tmp="${_dest}.$$.tmp"
    if jq --argjson base "$_base" "$_body" .mcp.json > "$_tmp" 2>/dev/null && jq empty "$_tmp" 2>/dev/null; then
        \mv -f "$_tmp" "$_dest"
        echo "      ✅ $_dest"
    else
        rm -f "$_tmp"
        echo "   ⚠️  [mcp-emit] could not write $_dest" >&2
    fi
    return 0
}

_llm_init_mcp_emit_opencode() {
    _llm_init_emit_merge_json opencode opencode.json '
        def envconv: gsub("\\$\\{(?<v>[A-Za-z_][A-Za-z0-9_]*)\\}"; "{env:\(.v)}");
        (.mcpServers | with_entries(.value |= (
            {type: "local", command: ([.command] + (.args // [])), enabled: true}
            + (if ((.env // {}) | length) > 0
               then {environment: (.env | map_values(if type == "string" then envconv else . end))}
               else {} end)))) as $m
        | ({"$schema": "https://opencode.ai/config.json"} + $base)
        | .mcp = $m'
}

_llm_init_mcp_emit_crush() {
    _llm_init_emit_merge_json crush .crush.json '
        def envconv: gsub("\\$\\{(?<v>[A-Za-z_][A-Za-z0-9_]*)\\}"; "$\(.v)");
        (.mcpServers | with_entries(.value |= (
            {type: "stdio", command: .command, args: (.args // [])}
            + (if ((.env // {}) | length) > 0
               then {env: (.env | map_values(if type == "string" then envconv else . end))}
               else {} end)))) as $m
        | $base
        | .mcp = $m
        | .options.context_paths //= ["AGENTS.md", "CLAUDE.md"]'
}

# Grok Build: TOML, edited only between the llm-init markers; the rest of the file is the user's.
_llm_init_mcp_emit_grok() {
    local _dest=".grok/config.toml" _block _tmp _begin="# >>> llm-init mcp >>>" _end="# <<< llm-init mcp <<<"
    _llm_init_mcp_src_ok grok || return 0
    _block="$(jq -r '
        def k: if test("^[A-Za-z0-9_-]+$") then . else @json end;
        .mcpServers | to_entries[] |
            "[mcp_servers.\(.key | k)]",
            "command = \(.value.command | @json)",
            "args = \(.value.args // [] | @json)",
            (if ((.value.env // {}) | length) > 0
             then "", "[mcp_servers.\(.key | k).env]",
                  (.value.env | to_entries[] | "\(.key | k) = \(.value | tostring | @json)")
             else empty end),
            ""' .mcp.json 2>/dev/null)" || { echo "   ⚠️  [mcp-emit] could not render grok MCP block" >&2; return 0; }
    mkdir -p .grok
    _tmp="${_dest}.$$.tmp"
    if [ -f "$_dest" ]; then
        awk -v b="$_begin" -v e="$_end" '
            $0 == b { skip = 1; next }
            $0 == e { skip = 0; next }
            skip    { next }
            /^[[:space:]]*$/ { blank++; next }
                    { while (blank > 0) { print ""; blank-- } print }
        ' "$_dest" > "$_tmp"
    else
        : > "$_tmp"
    fi
    [ -s "$_tmp" ] && printf '\n' >> "$_tmp"
    {
        printf '%s\n' "$_begin"
        printf '# Generated from .mcp.json by llm-init (change with: llm-init --mcp ...). Do not edit inside this block.\n'
        [ -n "$_block" ] && printf '%s\n' "$_block"
        printf '%s\n' "$_end"
    } >> "$_tmp"
    \mv -f "$_tmp" "$_dest"
    echo "      ✅ $_dest"
    return 0
}

# _llm_init_mcp_emit_tools <dry_run> — emits for every selected new tool.
_llm_init_mcp_emit_tools() {
    local _dry="${1:-false}" _t
    for _t in opencode crush agy grok pi omp cursor; do
        _llm_init_tool_enabled "$_t" || continue
        if [ "$_dry" = "true" ]; then
            echo "   ℹ️  [dry-run] Would emit $_t MCP config from .mcp.json"
            continue
        fi
        "_llm_init_mcp_emit_$_t"
    done
    return 0
}

# ─────────────────────────────────────────────────────────────────────────────
# Testing agents (i- suite): agents-src/ is the single source; scripts/render-agents.sh
# renders it into .llm_settings/{agents,skills}, which the per-tool sync below converts for
# Claude, Codex, Gemini, Copilot and the additional CLIs. scripts/testing/ (the gate scripts
# the skills call) is copied into the target repo.
# ─────────────────────────────────────────────────────────────────────────────
_LLM_INIT_TESTING_AGENTS="i-test-architect i-unit-tdd i-code-reviewer i-security-scanner i-integration-qa i-system-nfr i-release-gate i-data-ai-ot"

# _llm_init_render_testing_agents <dry_run> <source_dir> — never fails llm-init.
_llm_init_render_testing_agents() {
    local _dry="${1:-false}" _src="$2" _gen="$2/scripts/render-agents.sh"
    if [ ! -f "$_gen" ] || [ ! -d "$_src/agents-src" ]; then
        echo "   ⏭️  testing agents: no agents-src/ in $_src — using committed .llm_settings files"
        return 0
    fi
    if [ "$_dry" = "true" ]; then
        if bash "$_gen" --root "$_src" --check >/dev/null 2>&1; then
            echo "   ℹ️  [dry-run] Would render testing agents from agents-src/ (generated files already in sync)"
        else
            echo "   ℹ️  [dry-run] Would render testing agents from agents-src/ (generated files differ and would be updated)"
        fi
        return 0
    fi
    if bash "$_gen" --root "$_src" >/dev/null 2>&1; then
        echo "   ✅ testing agents rendered from agents-src/"
    else
        echo "   ⚠️  testing agents: render failed — using committed .llm_settings files" >&2
    fi
    return 0
}

# _llm_init_testing_summary <dry_run> <source_dir> — copies the gate scripts and prints a per-tool summary.
_llm_init_testing_summary() {
    local _dry="${1:-false}" _src="$2" _n _total=0 _c _line="" _t
    local _names="$_LLM_INIT_TESTING_AGENTS"
    if [ -d "$_src/agents-src" ]; then
        _names="$(cd "$_src/agents-src" && ls -d i-*/ 2>/dev/null | tr -d '/' | tr '\n' ' ')"
    fi
    for _n in $_names; do _total=$((_total+1)); done
    if [ -d "$_src/scripts/testing" ]; then
        if [ "$_dry" = "true" ]; then
            echo "   ℹ️  [dry-run] Would copy scripts/testing/ (gate scripts) into the target repo"
        else
            mkdir -p scripts/testing && rsync -a "$_src/scripts/testing/" scripts/testing/ \
                && echo "   ✅ scripts/testing/ (gate scripts, I_GATE=report by default)"
        fi
    fi
    if [ "$_dry" = "true" ]; then
        echo "   ℹ️  [dry-run] Would deploy $_total testing agents + skills to every selected tool"
        return 0
    fi
    _llm_init_count_tool() { # <label> <path-template with %s>
        local _lbl="$1" _tpl="$2" _k=0 _x
        for _x in $_names; do
            # shellcheck disable=SC2059
            [ -s "$(printf "$_tpl" "$_x")" ] && _k=$((_k+1))
        done
        _line="$_line $_lbl $_k/$_total ·"
        [ -z "${_LLM_INIT_TEST_MIN:-}" ] && _LLM_INIT_TEST_MIN="$_k"
        [ "$_k" -lt "$_LLM_INIT_TEST_MIN" ] && _LLM_INIT_TEST_MIN="$_k"
        return 0
    }
    _LLM_INIT_TEST_MIN=""
    _llm_init_count_tool claude-agents ".claude/agents/%s.md"
    _llm_init_count_tool claude-skills ".claude/skills/%s/SKILL.md"
    _llm_init_tool_enabled codex   && _llm_init_count_tool codex   ".codex/agents/%s.md"
    _llm_init_tool_enabled gemini  && _llm_init_count_tool gemini  ".agents/skills/%s/SKILL.md"
    _llm_init_tool_enabled copilot && _llm_init_count_tool copilot ".github/agents/%s.agent.md"
    _c="${_LLM_INIT_TEST_MIN:-0}"
    if [ "$_c" -eq "$_total" ] && [ "$_total" -gt 0 ]; then
        echo "   ✅ Testing agents ($_c/$_total) deployed to every selected tool"
    else
        echo "   ⚠️  Testing agents ($_c/$_total) — some tools are missing agents"
    fi
    echo "      ${_line% ·}"
    unset -f _llm_init_count_tool
    unset _LLM_INIT_TEST_MIN
    return 0
}

# ─────────────────────────────────────────────────────────────────────────────
# Gmail MCP (workspace-mcp, one stdio entry per account: gmail-<alias>)
#
# Accounts live in a per-user, NON-secret file (one alias per line, # comments):
#   ${LLM_INIT_GMAIL_ACCOUNTS:-~/.config/llm-settings/gmail-accounts}
# Each alias becomes an entry "gmail-<alias>" that launches
# .llm_settings/mcp-servers/gmail/mcp-gmail.sh <alias> (own token store, OAuth
# client from env/Keychain — never written to any config). Entries are generated
# (not shipped in the source config files) because the alias list is per-user.
# ─────────────────────────────────────────────────────────────────────────────

# _llm_init_gmail_accounts — prints valid, de-duplicated aliases (one per line).
# Warnings go to stderr; never fails (always returns 0).
_llm_init_gmail_accounts() {
    local _f="${LLM_INIT_GMAIL_ACCOUNTS:-${HOME}/.config/llm-settings/gmail-accounts}"
    local _line _seen="|" _n=0
    if [ ! -f "$_f" ]; then
        echo "   ⚠️  [gmail] No gmail-accounts file at ${_f} — no gmail-<alias> entries rendered." >&2
        echo "       Create it with one account alias per line (e.g. 'personal'), then re-run llm-init." >&2
        return 0
    fi
    while IFS= read -r _line || [ -n "$_line" ]; do
        _line="${_line%%#*}"
        _line="${_line#"${_line%%[![:space:]]*}"}"   # trim leading whitespace
        _line="${_line%"${_line##*[![:space:]]}"}"   # trim trailing whitespace
        [ -z "$_line" ] && continue
        if ! [[ "$_line" =~ ^[a-z0-9][a-z0-9-]*$ ]]; then
            echo "   ⚠️  [gmail] Skipping invalid alias '${_line}' in ${_f} (use lowercase letters, digits, '-')" >&2
            continue
        fi
        case "$_seen" in *"|${_line}|"*) continue ;; esac
        _seen="${_seen}${_line}|"
        _n=$((_n + 1))
        printf '%s\n' "$_line"
    done < "$_f"
    if [ "$_n" -eq 0 ]; then
        echo "   ⚠️  [gmail] No valid aliases in the gmail-accounts file (${_f}) — no gmail-<alias> entries rendered." >&2
    fi
    return 0
}

# _llm_init_render_gmail <dry_run>
# Rewrites the gmail-* entries of .mcp.json, .gemini/settings.json, .github/mcp.json
# (jq) and .codex/config.toml (awk): purges every existing gmail-* entry, then adds
# one per current alias — so it is idempotent and removed aliases disappear.
# Sets the global array _LLM_INIT_GMAIL_KEYS to the rendered keys. Always returns 0.
_LLM_INIT_GMAIL_KEYS=()
_llm_init_render_gmail() {
    local _dry_run="${1:-false}"
    local _wrapper=".llm_settings/mcp-servers/gmail/mcp-gmail.sh"
    local -a _aliases=()
    local _a
    _LLM_INIT_GMAIL_KEYS=()
    while IFS= read -r _a; do
        [ -n "$_a" ] && _aliases+=("$_a")
    done < <(_llm_init_gmail_accounts)
    for _a in ${_aliases[@]+"${_aliases[@]}"}; do
        _LLM_INIT_GMAIL_KEYS+=("gmail-${_a}")
    done

    if [ "$_dry_run" = "true" ]; then
        if [ ${#_aliases[@]} -gt 0 ]; then
            echo "   ℹ️  [dry-run] Would render gmail MCP entries: ${_LLM_INIT_GMAIL_KEYS[*]}"
        fi
        return 0
    fi

    local _names_json="[]"
    if [ ${#_aliases[@]} -gt 0 ]; then
        _names_json="$(printf '"%s",' "${_aliases[@]}")"
        _names_json="[${_names_json%,}]"
    fi

    # ── JSON targets ──
    local _jf _tmp
    if command -v jq >/dev/null 2>&1; then
        for _jf in ".mcp.json" ".gemini/settings.json" ".github/mcp.json"; do
            [ -f "$_jf" ] || continue
            _tmp="${_jf}.gm.$$"
            if jq --argjson names "$_names_json" --arg cmd "$_wrapper" '
                    .mcpServers = (
                        ((.mcpServers // {}) | with_entries(select(.key | startswith("gmail-") | not)))
                        + ($names | map({key: ("gmail-" + .),
                                         value: {command: $cmd, args: [.], timeout: 60000, trust: false}})
                                  | from_entries))
                ' "$_jf" > "$_tmp" 2>/dev/null && jq empty "$_tmp" 2>/dev/null; then
                \mv -f "$_tmp" "$_jf"
            else
                rm -f "$_tmp"
                echo "   ⚠️  [gmail] Could not update ${_jf} — left unchanged" >&2
            fi
        done
    else
        echo "   ⚠️  [gmail] jq not found — gmail entries not rendered into JSON configs" >&2
    fi

    # ── Codex TOML: purge gmail-* tables (and their sub-tables), then append ──
    local _tf=".codex/config.toml"
    if [ -f "$_tf" ]; then
        _tmp="${_tf}.gm.$$"
        awk '
            /^\[+mcp_servers\.gmail-/ { skip = 1; next }
            /^\[/                     { skip = 0 }
            skip                      { next }
            /^[[:space:]]*$/          { blank++; next }
                                      { while (blank > 0) { print ""; blank-- } print }
        ' "$_tf" > "$_tmp" || { rm -f "$_tmp"; echo "   ⚠️  [gmail] awk failed for ${_tf} — left unchanged" >&2; return 0; }
        for _a in ${_aliases[@]+"${_aliases[@]}"}; do
            printf '\n[mcp_servers.gmail-%s]\ncommand = "%s"\nargs = ["%s"]\ntimeout = 60000\ntrust = false\n' \
                "$_a" "$_wrapper" "$_a" >> "$_tmp"
        done
        \mv -f "$_tmp" "$_tf"
    fi

    if [ ${#_aliases[@]} -gt 0 ]; then
        echo "      ✅ gmail MCP entries: ${_LLM_INIT_GMAIL_KEYS[*]}"
    fi
    return 0
}

# _llm_init_gmail_global_hint <dry_run>
# Hermes and OpenClaw are not configured per-repo by llm-init (Hermes runs in a
# container, OpenClaw under the agentshroud-bot account) and their MCP config syntax
# is not verified here, so this PRINTS what to add instead of guessing a command.
_llm_init_gmail_global_hint() {
    local _dry_run="${1:-false}"
    local _wrap _a
    local -a _aliases=()
    _wrap="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)/mcp-servers/gmail/mcp-gmail.sh"
    while IFS= read -r _a; do
        [ -n "$_a" ] && _aliases+=("$_a")
    done < <(_llm_init_gmail_accounts 2>/dev/null)
    [ ${#_aliases[@]} -gt 0 ] || return 0
    if [ "$_dry_run" = "true" ]; then
        echo "   ℹ️  [dry-run] Would print gmail MCP setup for Hermes / OpenClaw"
        return 0
    fi
    echo "   🧩 gmail → Hermes / OpenClaw (not managed by llm-init)"
    echo "      Add one stdio MCP server per account to each tool's own MCP config"
    echo "      (confirm the exact key names in that tool's docs):"
    for _a in "${_aliases[@]}"; do
        echo "        gmail-${_a}  →  ${_wrap} ${_a}"
    done
    echo "      Hermes runs in a container and OpenClaw under another account: each needs its own"
    echo "      accounts, uvx, OAuth client credentials and one-time consent — this Mac's Keychain is not visible there."
}

# ─────────────────────────────────────────────────────────────────────────────
# _llm_init_render_mcp [--dry-run]
#
# Reads .llm_settings/repo-tenants (in the current directory) and filters the
# three agent MCP registry files to retain only the selected atlassian-* entries.
# Non-atlassian entries (github, aws-api, xmind, etc.) are always preserved.
#
# Requires: jq (for .mcp.json / .gemini/settings.json); awk for .codex/config.toml.
# If jq is absent, JSON files are left unfiltered with a warning.
# ─────────────────────────────────────────────────────────────────────────────
_llm_init_render_mcp() {
    local _dry_run="${1:-false}"
    local _mcp_marker=".llm_settings/repo-mcp-servers"
    local _tenant_marker=".llm_settings/repo-tenants"

    # ── Decide filtering mode ─────────────────────────────────────────
    # If repo-mcp-servers exists → explicit server selection (new mode).
    # Otherwise fall back to Atlassian-only tenant filtering (legacy mode).

    if [ -f "$_mcp_marker" ]; then
        # ── NEW MODE: explicit MCP server selection ───────────────────
        local -a _selected_names=()
        while IFS= read -r _line; do
            _line="${_line%%#*}"           # strip inline comments
            _line="${_line//[[:space:]]/}" # strip whitespace
            [ -z "$_line" ] && continue
            _selected_names+=("$_line")
        done < "$_mcp_marker"

        # Map short names → JSON keys and TOML keys
        local -a _json_keys=()
        local -a _toml_keys=()
        local _sn _jk _tk
        local _gmail_selected=false
        for _sn in "${_selected_names[@]}"; do
            case "$_sn" in
                github)                _jk="github";                    _tk="github" ;;
                github-fluence)        _jk="github-fluence";            _tk="github-fluence" ;;
                github-agentshroud)    _jk="github-agentshroud";        _tk="github-agentshroud" ;;
                github-idallasj)       _jk="github-idallasj";           _tk="github-idallasj" ;;
                aws)                   _jk="awslabs.aws-api-mcp-server"; _tk="awslabs.aws-api-mcp-server" ;;
                xmind)                 _jk="xmind";                     _tk="xmind" ;;
                safari)                _jk="safari";                    _tk="safari" ;;
                home-assistant)        _jk="home-assistant";            _tk="home-assistant" ;;
                devonthink)            _jk="devonthink";                _tk="devonthink" ;;
                atlassian-fluence)     _jk="atlassian-fluence";         _tk="atlassian-fluence" ;;
                atlassian-agentshroud) _jk="atlassian-agentshroud";     _tk="atlassian-agentshroud" ;;
                atlassian-idallasj)    _jk="atlassian-idallasj";        _tk="atlassian-idallasj" ;;
                macuse) continue ;;  # global user-scope registration (_llm_init_ensure_macuse) — no per-repo file entry
                gmail) _gmail_selected=true; continue ;;  # generated per account (_llm_init_render_gmail) — no static entry
                twg) continue ;;  # global per-machine CLI, not an MCP server (_llm_init_check_twg) — no per-repo file entry
                *) echo "   ⚠️  [render-mcp] Unknown server '$_sn' in $_mcp_marker — skipping" >&2; continue ;;
            esac
            _json_keys+=("$_jk")
            _toml_keys+=("$_tk")
        done

        local _keys_str="${_selected_names[*]}"

        if [ "$_dry_run" = "true" ]; then
            echo "   ℹ️  [dry-run] Would render MCP configs (explicit selection): ${_keys_str}"
            $_gmail_selected && _llm_init_render_gmail true
            return 0
        fi

        echo "   🎛️  Rendering MCP configs — selected server(s): ${_keys_str}"

        # ── Filter JSON files with jq ─────────────────────────────────
        if command -v jq >/dev/null 2>&1; then
            if [ ${#_json_keys[@]} -eq 0 ] && ! $_gmail_selected; then
                echo "   ⚠️  [render-mcp] No valid servers selected — JSON files left unchanged" >&2
            else
                local _keys_json="[]"   # gmail-only selection: keep nothing static; gmail-* are added below
                if [ ${#_json_keys[@]} -gt 0 ]; then
                    _keys_json="$(printf '"%s",' "${_json_keys[@]}")"
                    _keys_json="[${_keys_json%,}]"
                fi
                # Keep ONLY entries whose key is in the explicit selection
                local _jq_filter='.mcpServers |= with_entries(select(.key as $k | $keep | any(. == $k)))'
                local _jf _tmp _err
                for _jf in ".mcp.json" ".gemini/settings.json" ".github/mcp.json"; do
                    if [ -f "$_jf" ]; then
                        # Validate JSON before filtering
                        if ! jq empty "$_jf" 2>/dev/null; then
                            echo "   ⚠️  [render-mcp] $_jf is not valid JSON — skipping filter" >&2
                            continue
                        fi
                        _tmp="${_jf}.rnd.$$"
                        _err="${_jf}.err.$$"
                        if jq --argjson keep "$_keys_json" "$_jq_filter" "$_jf" > "$_tmp" 2>"$_err"; then
                            # Validate jq output before overwriting
                            if jq empty "$_tmp" 2>/dev/null; then
                                # Use \mv -f to bypass 'mv -i' aliases (common in interactive shells)
                                \mv -f "$_tmp" "$_jf"
                                rm -f "$_err"
                                echo "      ✅ $_jf"
                            else
                                rm -f "$_tmp"
                                echo "   ❌ [render-mcp] jq produced invalid JSON for $_jf" >&2
                                [ -s "$_err" ] && cat "$_err" >&2
                                rm -f "$_err"
                            fi
                        else
                            rm -f "$_tmp"
                            echo "   ❌ [render-mcp] jq filter failed for $_jf — file unchanged" >&2
                            [ -s "$_err" ] && cat "$_err" >&2
                            rm -f "$_err"
                        fi
                    fi
                done
            fi
        else
            echo "   ⚠️  [render-mcp] jq not found — .mcp.json, .gemini/settings.json, and .github/mcp.json unfiltered" >&2
            echo "   ⚠️              Install jq for full per-server filtering" >&2
        fi

        # ── Filter TOML with awk — ALL [mcp_servers.*] sections ───────
        local _tf=".codex/config.toml"
        if [ -f "$_tf" ]; then
            local _toml_str="${_toml_keys[*]:-}"
            local _tmp="${_tf}.rnd.$$"
            # Handles [mcp_servers.key] (codex >= 0.154) and legacy [[mcp_servers.key]],
            # bare and quoted keys ("awslabs.aws-api-mcp-server"), and .env sub-tables.
            awk -v keep="$_toml_str" '
                BEGIN {
                    n = split(keep, arr, " ")
                    for (i = 1; i <= n; i++) keep_set[arr[i]] = 1
                    in_skip = 0
                }
                function out(line) { while (blank > 0) { print ""; blank-- } print line }
                function server_key(line,    k) {
                    k = line
                    sub(/^\[+mcp_servers\./, "", k)
                    sub(/\]+.*$/, "", k)
                    gsub(/"/, "", k)
                    return k
                }
                # Sub-table of a server (e.g. [mcp_servers.xmind.env] or
                # [mcp_servers."a.b".env]) — quoted keys hide their dots, so a
                # sub-table is: (quoted or dotless key) followed by ".something"
                /^\[mcp_servers\.("[^"]+"|[A-Za-z0-9_-]+)\.[A-Za-z0-9_.-]+\]/ {
                    if (!in_skip) out($0)
                    next
                }
                # Server header: single or double brackets, quoted or bare key
                /^\[+mcp_servers\.("[^"]+"|[A-Za-z0-9_-]+)\]+/ {
                    in_skip = (server_key($0) in keep_set) ? 0 : 1
                    if (!in_skip) out($0)
                    next
                }
                /^\[/ {
                    in_skip = 0
                    out($0)
                    next
                }
                # Blank lines wait for the next kept line: a dropped last server leaves no trailing blank
                !in_skip && /^[[:space:]]*$/ { blank++; next }
                !in_skip { out($0) }
            ' "$_tf" > "$_tmp" && \mv -f "$_tmp" "$_tf" && echo "      ✅ $_tf" || {
                rm -f "$_tmp"
                echo "   ⚠️  [render-mcp] awk filter failed for $_tf — file unchanged" >&2
            }
        fi

        # ── Reconcile .claude/settings.local.json ─────────────────────
        # Ensure selected servers are enabled (not in disabledMcpjsonServers)
        # and enabledMcpjsonServers reflects the current live .mcp.json keys.
        # ── Gmail: one generated entry per account (after filtering, before reconcile) ──
        if $_gmail_selected; then
            _llm_init_render_gmail "$_dry_run"
            _json_keys+=(${_LLM_INIT_GMAIL_KEYS[@]+"${_LLM_INIT_GMAIL_KEYS[@]}"})
        fi

        _llm_init_reconcile_settings_local "$_dry_run" ${_json_keys[@]+"${_json_keys[@]}"}

    else
        # ── LEGACY MODE: Atlassian-only tenant filtering ──────────────
        # repo-mcp-servers absent; filter only atlassian-* entries using repo-tenants.
        # All non-Atlassian servers are preserved unchanged (backward compatible).

        local -a _active_keys=()
        if [ -f "$_tenant_marker" ]; then
            while IFS= read -r _line; do
                _line="${_line%%#*}"           # strip inline comments
                _line="${_line//[[:space:]]/}" # strip whitespace
                [ -z "$_line" ] && continue
                case "$_line" in
                    fluenceenergy)   _active_keys+=("atlassian-fluence") ;;
                    therealidallasj) _active_keys+=("atlassian-idallasj") ;;
                    agentshroudai)   _active_keys+=("atlassian-agentshroud") ;;
                    *) echo "   ⚠️  [render-mcp] Unknown tenant '$_line' in $_tenant_marker — skipping" >&2 ;;
                esac
            done < "$_tenant_marker"
        fi
        [ ${#_active_keys[@]} -eq 0 ] && _active_keys=("atlassian-fluence")  # safe default

        local _keys_str="${_active_keys[*]}"

        if [ "$_dry_run" = "true" ]; then
            echo "   ℹ️  [dry-run] Would render MCP configs (Atlassian tenant filter): ${_keys_str}"
            return 0
        fi

        echo "   🎛️  Rendering MCP configs — active tenant(s): ${_keys_str}"

        # ── Filter JSON files with jq ─────────────────────────────────
        if command -v jq >/dev/null 2>&1; then
            local _keys_json
            _keys_json="$(printf '"%s",' "${_active_keys[@]}")"
            _keys_json="[${_keys_json%,}]"
            local _jq_filter
            _jq_filter='.mcpServers |= with_entries(select(
                (.key | startswith("atlassian-") | not) or
                (.key as $k | $keep | any(. == $k))
            ))'
            local _jf _tmp _err
            for _jf in ".mcp.json" ".gemini/settings.json" ".github/mcp.json"; do
                if [ -f "$_jf" ]; then
                    # Validate JSON before filtering
                    if ! jq empty "$_jf" 2>/dev/null; then
                        echo "   ⚠️  [render-mcp] $_jf is not valid JSON — skipping filter" >&2
                        continue
                    fi
                    _tmp="${_jf}.rnd.$$"
                    _err="${_jf}.err.$$"
                    if jq --argjson keep "$_keys_json" "$_jq_filter" "$_jf" > "$_tmp" 2>"$_err"; then
                        # Validate jq output before overwriting
                        if jq empty "$_tmp" 2>/dev/null; then
                            # Use \mv -f to bypass 'mv -i' aliases (common in interactive shells)
                            \mv -f "$_tmp" "$_jf"
                            rm -f "$_err"
                            echo "      ✅ $_jf"
                        else
                            rm -f "$_tmp"
                            echo "   ❌ [render-mcp] jq produced invalid JSON for $_jf" >&2
                            [ -s "$_err" ] && cat "$_err" >&2
                            rm -f "$_err"
                        fi
                    else
                        rm -f "$_tmp"
                        echo "   ❌ [render-mcp] jq filter failed for $_jf — file unchanged" >&2
                        [ -s "$_err" ] && cat "$_err" >&2
                        rm -f "$_err"
                    fi
                fi
            done
        else
            echo "   ⚠️  [render-mcp] jq not found — .mcp.json, .gemini/settings.json, and .github/mcp.json unfiltered" >&2
            echo "   ⚠️              Install jq for full per-tenant filtering" >&2
        fi

        # ── Filter TOML — only atlassian-* sections (legacy behavior) ─
        local _tf=".codex/config.toml"
        if [ -f "$_tf" ]; then
            local _tmp="${_tf}.rnd.$$"
            # Handles [mcp_servers.atlassian-*] (codex >= 0.154) and legacy [[...]]
            awk -v keep="$_keys_str" '
                BEGIN {
                    n = split(keep, arr, " ")
                    for (i = 1; i <= n; i++) keep_set[arr[i]] = 1
                    in_skip = 0
                }
                function out(line) { while (blank > 0) { print ""; blank-- } print line }
                /^\[mcp_servers\.atlassian-[A-Za-z_-]+\.[A-Za-z0-9_.-]+\]/ {
                    if (!in_skip) out($0)
                    next
                }
                /^\[+mcp_servers\.atlassian-[A-Za-z_-]+\]+/ {
                    key = $0
                    sub(/^\[+mcp_servers\./, "", key)
                    sub(/\]+.*$/, "", key)
                    in_skip = (key in keep_set) ? 0 : 1
                    if (!in_skip) out($0)
                    next
                }
                /^\[/ {
                    in_skip = 0
                    out($0)
                    next
                }
                # Blank lines wait for the next kept line: a dropped last server leaves no trailing blank
                !in_skip && /^[[:space:]]*$/ { blank++; next }
                !in_skip { out($0) }
            ' "$_tf" > "$_tmp" && \mv -f "$_tmp" "$_tf" && echo "      ✅ $_tf" || {
                rm -f "$_tmp"
                echo "   ⚠️  [render-mcp] awk filter failed for $_tf — file unchanged" >&2
            }
        fi
    fi
}

# ─────────────────────────────────────────────────────────────────────────────
# _llm_init_ensure_macuse <dry_run>
#
# macuse (https://macuse.app/) is a single macOS native-app MCP server. Unlike
# every other --mcp value it has no per-repo .mcp.json / .gemini/settings.json /
# .codex/config.toml entry — it registers once, globally, per machine via each
# CLI's own `mcp add --scope user` command. This function is idempotent (safe
# to call on every llm-init run) and macOS-only; it no-ops elsewhere.
# ─────────────────────────────────────────────────────────────────────────────
_llm_init_ensure_macuse() {
    local _dry_run="${1:-false}"
    local _bin="/Applications/Macuse.app/Contents/MacOS/macuse"

    if [ "$(uname -s)" != "Darwin" ]; then
        echo "   ℹ️  [macuse] Not on macOS — skipping (macuse is a macOS-only app)"
        return 0
    fi

    if [ ! -x "$_bin" ]; then
        echo "   ⚠️  [macuse] Not installed — skipping. Download from https://macuse.app/" >&2
        return 0
    fi

    echo "   🧩 macuse (global user-scope MCP registration)"

    # claude
    if command -v claude >/dev/null 2>&1; then
        if claude mcp list 2>/dev/null | grep -q '^macuse:'; then
            echo "      ✅ claude: already registered"
        elif [ "$_dry_run" = "true" ]; then
            echo "      ℹ️  [dry-run] Would run: claude mcp add --scope user macuse -- $_bin mcp"
        elif claude mcp add --scope user macuse -- "$_bin" mcp >/dev/null 2>&1; then
            echo "      ✅ claude: registered"
        else
            echo "      ⚠️  claude: registration failed" >&2
        fi
    else
        echo "      ⚠️  claude not found on PATH — skipping" >&2
    fi

    # gemini
    if command -v gemini >/dev/null 2>&1; then
        if gemini mcp list 2>/dev/null | grep -qi 'macuse'; then
            echo "      ✅ gemini: already registered"
        elif [ "$_dry_run" = "true" ]; then
            echo "      ℹ️  [dry-run] Would run: gemini mcp add --scope user macuse $_bin mcp"
        elif gemini mcp add --scope user macuse "$_bin" mcp >/dev/null 2>&1; then
            echo "      ✅ gemini: registered"
        else
            echo "      ⚠️  gemini: registration failed (or already present — 'gemini mcp list' syntax unverified)" >&2
        fi
    else
        echo "      ⚠️  gemini not found on PATH — skipping" >&2
    fi

    # codex (no --scope flag — mcp add is always global)
    if command -v codex >/dev/null 2>&1; then
        if codex mcp get macuse >/dev/null 2>&1; then
            echo "      ✅ codex: already registered"
        elif [ "$_dry_run" = "true" ]; then
            echo "      ℹ️  [dry-run] Would run: codex mcp add macuse -- $_bin mcp"
        elif codex mcp add macuse -- "$_bin" mcp >/dev/null 2>&1; then
            echo "      ✅ codex: registered"
        else
            echo "      ⚠️  codex: registration failed" >&2
        fi
    else
        echo "      ⚠️  codex not found on PATH — skipping" >&2
    fi
}

# ─────────────────────────────────────────────────────────────────────────────
# _llm_init_bounded <seconds> <command...>
#
# Runs an external CLI with stdin closed and a hard time limit, so a stalled
# network call (twg / sf) can never hang llm-init. Pure bash (macOS has no
# `timeout`). stdout/stderr pass through; the exit status is the command's, or
# 124 if it was killed for exceeding the limit.
# ─────────────────────────────────────────────────────────────────────────────
_llm_init_bounded() {
    local _secs="$1"; shift
    local _flag
    _flag="$(mktemp "${TMPDIR:-/tmp}/llm-init-bounded.XXXXXX")" || { "$@" </dev/null; return $?; }
    "$@" </dev/null &
    local _pid=$!
    ( sleep "$_secs"; if kill "$_pid" 2>/dev/null; then : > "$_flag.timeout"; fi ) >/dev/null 2>&1 &
    local _wd=$!
    local _rc=0
    wait "$_pid" 2>/dev/null || _rc=$?
    kill "$_wd" 2>/dev/null
    wait "$_wd" 2>/dev/null || true
    if [ -f "$_flag.timeout" ]; then _rc=124; fi
    rm -f "$_flag" "$_flag.timeout"
    return "$_rc"
}

# ─────────────────────────────────────────────────────────────────────────────
# _llm_init_mcp_context [server...]
#
# Classifies an (already group-expanded) MCP server selection so the twg / sf
# auth checks know which account scope the repo belongs to. Prints one of:
#   fluence   — only Fluence servers (github-fluence / atlassian-fluence)
#   personal  — only personal servers (github, *-idallasj, *-agentshroud)
#   mixed     — both (e.g. --mcp all)
#   none      — neither (neutral servers like aws/xmind/safari/twg only)
# Derived from the selection rather than stored, so the marker file format and
# the --mcp group definitions stay unchanged.
# ─────────────────────────────────────────────────────────────────────────────
_llm_init_mcp_context() {
    local _s _fl=false _pe=false
    for _s in "$@"; do
        case "$_s" in
            github-fluence|atlassian-fluence)
                _fl=true ;;
            github|github-idallasj|github-agentshroud|atlassian-idallasj|atlassian-agentshroud)
                _pe=true ;;
        esac
    done
    if $_fl && $_pe; then echo "mixed"
    elif $_fl; then echo "fluence"
    elif $_pe; then echo "personal"
    else echo "none"
    fi
}

# _llm_init_email_scope <email>
# Prints "fluence" if the address is on the Fluence domain, else "personal".
# Domain is overridable via LLM_INIT_FLUENCE_EMAIL_DOMAIN. Exact-domain match
# (case-insensitive) so look-alike domains are NOT treated as Fluence.
_llm_init_email_scope() {
    local _email _domain _want
    _email="$(printf '%s' "${1:-}" | tr '[:upper:]' '[:lower:]')"
    _domain="${_email##*@}"
    _want="$(printf '%s' "${LLM_INIT_FLUENCE_EMAIL_DOMAIN:-fluenceenergy.com}" | tr '[:upper:]' '[:lower:]')"
    if [ "$_domain" = "$_want" ]; then echo "fluence"; else echo "personal"; fi
}

# ─────────────────────────────────────────────────────────────────────────────
# _llm_init_check_twg <dry_run> [context]
#
# Atlassian Teamwork Graph CLI (https://teamwork-graph.atlassian.com/cli) is a
# single native binary, installed once per machine via its own OAuth 2.1 login
# flow — it is NOT an MCP server and has no per-repo .mcp.json /
# .gemini/settings.json / .codex/config.toml / .github/mcp.json entry. It ships
# its own "skills" that its installer drops into the GLOBAL ~/.agents/skills
# (read by Codex, Gemini CLI, GitHub Copilot, Cursor, Rovo Dev) and
# ~/.claude/skills (Claude Code) — distinct from the per-repo .claude/skills/
# this script manages, so there is nothing to rsync or convert here.
#
# This function only detects/reports status — it never runs the installer or
# logs in, since first-time setup requires a controlling terminal for OAuth
# consent. Idempotent (safe to call on every llm-init run).
#
# Account separation: twg holds ONE login per machine, and Fluence and personal
# Atlassian accounts must never be mixed. With context fluence|personal the
# logged-in account's email domain must match the repo scope; on mismatch it
# warns loudly and tells the user to re-authenticate. It never switches
# accounts and never fails llm-init (always returns 0). With context mixed
# (--mcp all) one login cannot satisfy both scopes, so it only reports which
# scope is active.
# ─────────────────────────────────────────────────────────────────────────────
_llm_init_check_twg() {
    local _dry_run="${1:-false}"
    local _ctx="${2:-none}"

    if ! command -v twg >/dev/null 2>&1; then
        echo "   ⚠️  [twg] Not installed — skipping. Install with:" >&2
        echo "       curl -fsSL --retry 2 https://teamwork-graph.atlassian.com/cli/install | bash" >&2
        echo "       (or paste into any agent: Install/setup TWG using https://teamwork-graph.atlassian.com/cli/AGENTS.md)" >&2
        return 0
    fi

    if [ "$_dry_run" = "true" ]; then
        echo "   ℹ️  [dry-run] Would run: twg doctor; twg whoami (account-scope check: ${_ctx})"
        return 0
    fi

    echo "   🧩 twg (Atlassian Teamwork Graph CLI, global per-machine install)"
    local _rc=0
    _llm_init_bounded "${LLM_INIT_CHECK_TIMEOUT:-20}" twg doctor >/dev/null 2>&1 || _rc=$?
    if [ "$_rc" -eq 0 ]; then
        echo "      ✅ twg doctor: passed"
    elif [ "$_rc" -eq 124 ]; then
        echo "      ⚠️  twg doctor: timed out after ${LLM_INIT_CHECK_TIMEOUT:-20}s — skipping twg checks (network?)" >&2
        return 0
    else
        echo "      ⚠️  twg doctor: reported issues — run 'twg doctor' directly for details" >&2
    fi

    [ "$_ctx" = "none" ] && return 0

    local _email _scope _who
    _rc=0
    _who="$(_llm_init_bounded "${LLM_INIT_CHECK_TIMEOUT:-20}" twg whoami 2>/dev/null)" || _rc=$?
    if [ "$_rc" -eq 124 ]; then
        echo "      ⚠️  twg whoami: timed out after ${LLM_INIT_CHECK_TIMEOUT:-20}s — account scope not verified" >&2
        return 0
    fi
    _email="$(printf '%s\n' "$_who" | sed -n 's/^[[:space:]]*Email:[[:space:]]*//p' | head -1)"
    if [ -z "$_email" ]; then
        echo "      ⚠️  twg: not authenticated. Run 'twg setup' in your own terminal (interactive browser login)" >&2
        echo "         using the ${_ctx/mixed/correct} Atlassian account for this repo." >&2
        return 0
    fi
    _scope="$(_llm_init_email_scope "$_email")"

    case "$_ctx" in
        mixed)
            echo "      ℹ️  twg account: ${_email} (${_scope} scope). This repo is mixed (fluence + personal):"
            echo "         one twg login serves both — confirm it is the right account before each twg use."
            ;;
        fluence|personal)
            if [ "$_scope" = "$_ctx" ]; then
                echo "      ✅ twg account: ${_email} (${_scope}) matches this repo's ${_ctx} scope"
            else
                echo "      ❌ twg account MISMATCH: logged in as ${_email} (${_scope}) but this repo is ${_ctx}-scoped." >&2
                echo "         Fluence and personal Atlassian accounts are not mixed. Do NOT use twg here until you" >&2
                echo "         re-authenticate with the ${_ctx} account: run 'twg setup' in your own terminal." >&2
            fi
            ;;
    esac
    return 0
}

# ─────────────────────────────────────────────────────────────────────────────
# _llm_init_check_sf <dry_run> [context]
#
# Salesforce CLI (sf) auth status for the Fluence org (alias ${SFQ_ORG:-fluence},
# Entra SSO login). Read-only: never logs in or opens a browser — when the org is
# not connected it prints the exact login command for the user to run. The org is
# Fluence-only, so a personal-scope repo skips the check. sf is provisioned via
# Nix/Home Manager; no install hint is given. Always returns 0.
# ─────────────────────────────────────────────────────────────────────────────
_llm_init_check_sf() {
    local _dry_run="${1:-false}"
    local _ctx="${2:-none}"
    local _org="${SFQ_ORG:-fluence}"
    local _url="${SFQ_INSTANCE_URL:-https://na2btfluence.my.salesforce.com}"

    case "$_ctx" in
        none) return 0 ;;
        personal)
            echo "   ℹ️  [sf] Skipped — Salesforce org '${_org}' is Fluence-only and this repo is personal-scoped."
            return 0 ;;
    esac

    if ! command -v sf >/dev/null 2>&1; then
        echo "   ⚠️  [sf] Salesforce CLI not found on PATH — skipping (provision via Nix/Home Manager)." >&2
        return 0
    fi

    if [ "$_dry_run" = "true" ]; then
        echo "   ℹ️  [dry-run] Would run: sf org display -o ${_org} --json"
        return 0
    fi

    echo "   🧩 sf (Salesforce CLI, org '${_org}')"
    local _status _json _rc=0
    _json="$(_llm_init_bounded "${LLM_INIT_CHECK_TIMEOUT:-20}" sf org display -o "$_org" --json 2>/dev/null)" || _rc=$?
    if [ "$_rc" -eq 124 ]; then
        echo "      ⚠️  sf org display: timed out after ${LLM_INIT_CHECK_TIMEOUT:-20}s — auth status not verified" >&2
        return 0
    fi
    _status="$(printf '%s' "$_json" \
        | python3 -c 'import json,sys; print(json.load(sys.stdin).get("result",{}).get("connectedStatus",""))' 2>/dev/null || true)"
    if [ "$_status" = "Connected" ]; then
        echo "      ✅ sf org '${_org}': Connected"
    else
        echo "      ⚠️  sf org '${_org}': not authenticated (${_status:-no saved login}). Authorize with:" >&2
        echo "         sf org login web -a ${_org} --instance-url ${_url}" >&2
        echo "         (Entra SSO, interactive — run it in your own terminal)" >&2
    fi
    return 0
}

# ─────────────────────────────────────────────────────────────────────────────
# _llm_init_normalize_md <src_file> <out_file>
#
# Normalizes a markdown file for the Gemini agent loader: strips a UTF-8 BOM,
# converts CRLF to LF, and drops leading blank lines. Gemini's frontmatter
# regex (^---) fails on a BOM and on blank lines before the fence; CRLF is
# tolerated by Gemini but normalized here so downstream awk/grep is exact.
# (gemini-cli packages/core/src/agents/agentLoader.ts + skillLoader.ts:34)
# ─────────────────────────────────────────────────────────────────────────────
_llm_init_normalize_md() {
    local _src="$1" _out="$2"
    local _bom
    _bom="$(printf '\357\273\277')"
    sed "1s/^${_bom}//" "$_src" | sed $'s/\r$//' | awk 'p||NF{p=1; print}' > "$_out"
}

# ─────────────────────────────────────────────────────────────────────────────
# _llm_init_gemini_excluded <name>
#
# Returns 0 if <name> is listed in .llm_settings/gemini-agent-exclude.txt
# (reference material that must not be deployed as an invocable agent).
# Checked against the deployed agent name; comments/blank lines ignored.
# ─────────────────────────────────────────────────────────────────────────────
_llm_init_gemini_excluded() {
    local _name="$1"
    local _list=".llm_settings/gemini-agent-exclude.txt"
    [ -f "$_list" ] || return 1
    grep -v '^[[:space:]]*#' "$_list" | grep -qxF "$_name"
}

# ─────────────────────────────────────────────────────────────────────────────
# _llm_init_convert_for_gemini <src_file> <dest_dir> [override_name]
#
# Writes a Gemini CLI-compatible agent file to dest_dir. Gemini validates
# frontmatter with a STRICT zod schema (unknown keys are rejected):
# localAgentSchema in packages/core/src/agents/agentLoader.ts (v0.59.0,
# lines 92-116). Accepted keys: kind, name, description, display_name,
# tools, mcp_servers, model, temperature, max_turns, timeout_mins.
# We emit only name + description; every other source key is preserved as
# a YAML comment inside the frontmatter (js-yaml discards comments before
# validation, so they are safe).
#   - name must match ^[a-z0-9-_]+$ (digit-prefixed names are rewritten)
#   - file must start with --- at byte 0 (no BOM, no leading blanks)
#   - No README.md in the agents directory
#
# Hosts run different Gemini CLI versions (e.g. 0.46.0 vs 0.59.0): the name+description-only
# frontmatter is accepted by every strict-schema version. Hosts whose CLI cannot load
# .gemini/agents/ at all can set LLM_INIT_GEMINI_AGENTS=off — the agent files are then skipped and
# the .gemini/commands/*.toml slash commands provide the same capabilities (a command whose name
# matches a .agents/skills skill is dropped: Gemini serves that skill as the slash command).
#
# <src_file>     : source .md file (agent stub or SKILL.md)
# <dest_dir>     : target directory (e.g. .gemini/agents)
# [override_name]: use this as the agent name instead of deriving from filename
#                  (needed for skills whose filename is always SKILL.md)
# ─────────────────────────────────────────────────────────────────────────────
_llm_init_convert_for_gemini() {
    local src_file="$1"
    local dest_dir="$2"
    local override_name="${3:-}"

    local filename agent_name dest_file desc body existing_desc

    # Per-host opt-out for Gemini CLI versions without subagent support (commands still deploy).
    [ "${LLM_INIT_GEMINI_AGENTS:-on}" = "off" ] && return 0

    filename=$(basename "$src_file")

    # Skip README
    [[ "$filename" == "README.md" ]] && return 0

    # Derive agent name from override or filename
    if [[ -n "$override_name" ]]; then
        agent_name="$override_name"
    else
        agent_name="${filename%.md}"
    fi

    # Enforce Gemini's name slug: ^[a-z0-9-_]+$ (agentLoader.ts:96)
    agent_name="$(printf '%s' "$agent_name" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9_-]/-/g')"

    # Rewrite names starting with a digit (e.g. 8d → eightd)
    if [[ "$agent_name" =~ ^[0-9] ]]; then
        case "${agent_name:0:1}" in
            0) agent_name="zero${agent_name:1}" ;;
            1) agent_name="one${agent_name:1}"  ;;
            2) agent_name="two${agent_name:1}"  ;;
            3) agent_name="three${agent_name:1}";;
            4) agent_name="four${agent_name:1}" ;;
            5) agent_name="five${agent_name:1}" ;;
            6) agent_name="six${agent_name:1}"  ;;
            7) agent_name="seven${agent_name:1}";;
            8) agent_name="eight${agent_name:1}";;
            9) agent_name="nine${agent_name:1}" ;;
        esac
    fi

    dest_file="${dest_dir}/${agent_name}.md"

    # Normalize BEFORE the frontmatter gate: a BOM, CRLF, or leading blank line
    # would silently misroute a frontmattered file to the no-frontmatter branch,
    # which then concatenates a second --- block — the exact failure Gemini
    # reports as "Missing mandatory YAML frontmatter" or garbage descriptions.
    local _norm
    _norm="$(mktemp "${TMPDIR:-/tmp}/llm-init-gemini.XXXXXX")"
    _llm_init_normalize_md "$src_file" "$_norm"

    local _weak_reason=""

    if head -1 "$_norm" | grep -q '^---$'; then
        # File has frontmatter — extract description, keep other keys as comments
        # description may span multiple lines (YAML block scalar with >)
        # Note: awk's END block runs even after exit, so use a printed flag to avoid double output
        existing_desc=$(awk '
            BEGIN{f=0; in_desc=0; line=""; done=0}
            /^---$/{f++; next}
            f==1 && /^description:/{
                in_desc=1
                sub(/^description:[[:space:]]*/,"")
                sub(/^[>|][[:space:]]*/,"")
                line=$0
                next
            }
            f==1 && in_desc && /^[[:space:]]/{
                sub(/^[[:space:]]*/,"")
                line=line " " $0
                next
            }
            f==1 && in_desc && !done{ done=1; print line; exit }
            f==2 && in_desc && !done{ done=1; print line; exit }
            END{ if(in_desc && !done && line!="") print line }
        ' "$_norm")

        # Preserve every non-name/description source key as a YAML comment
        # (js-yaml strips comments before zod validation — verified safe).
        # Continuation/list lines under a preserved key are commented too.
        local extra_keys_comments
        extra_keys_comments=$(awk '
            BEGIN{f=0; skip=1}
            /^---$/{f++; next}
            f==1 {
                if ($0 ~ /^[A-Za-z_][A-Za-z0-9_-]*:/) {
                    key=$0; sub(/:.*/,"",key)
                    skip = (key=="name" || key=="description") ? 1 : 0
                    if (!skip) print "# " $0
                } else if (!skip) {
                    print "# " $0
                }
                next
            }
            f>=2{exit}
        ' "$_norm")

        # Extract body (content after closing ---)
        body=$(awk 'BEGIN{count=0} /^---$/{count++; if(count==2){found=1; next}} found{print}' "$_norm")

        # Fallback: pull description from first H1 in the body
        if [[ -z "$existing_desc" ]]; then
            existing_desc=$(grep '^# ' "$_norm" | head -1 | sed 's/^# //')
            _weak_reason="description derived from first heading"
        fi
        if [[ -z "$existing_desc" ]]; then
            existing_desc="${agent_name} agent"
            _weak_reason="description is a generated placeholder"
        fi

        # Sanitize: strip YAML block scalar indicators and surrounding quotes, collapse whitespace
        existing_desc=$(printf '%s' "$existing_desc" \
            | sed 's/^[>|"[:space:]]*//' \
            | sed 's/[[:space:]"]*$//' \
            | tr '\n' ' ' \
            | sed 's/  */ /g')

        # Escape any remaining double-quotes inside the value
        existing_desc="${existing_desc//\"/\\\"}"

        # Always use the (possibly digit-fixed) agent_name as the frontmatter name
        {
            printf -- '---\n'
            printf 'name: %s\n' "$agent_name"
            printf 'description: "%s"\n' "$existing_desc"
            [[ -n "$extra_keys_comments" ]] && printf '%s\n' "$extra_keys_comments"
            printf -- '---\n'
            printf '\n'
            printf '> **[Gemini Standalone Mode]** Complete this task using direct MCP tool calls.\n'
            printf '> Do **not** invoke or reference other agents by name — all capabilities are\n'
            printf '> available through the MCP tools configured in `.gemini/settings.json`.\n'
            printf '\n'
            printf '%s\n' "$body"
        } > "$dest_file"
        desc="$existing_desc"
    else
        # No frontmatter — extract description from first H1 heading
        desc=$(grep '^# ' "$_norm" | head -1 | sed 's/^# //')
        _weak_reason="source has no frontmatter; description derived from first heading"
        if [[ -z "$desc" ]]; then
            desc="${agent_name} agent"
            _weak_reason="source has no frontmatter; description is a generated placeholder"
        fi
        desc="${desc//\"/\\\"}"

        {
            printf -- '---\n'
            printf 'name: %s\n' "$agent_name"
            printf 'description: "%s"\n' "$desc"
            printf -- '---\n'
            printf '\n'
            printf '> **[Gemini Standalone Mode]** Complete this task using direct MCP tool calls.\n'
            printf '> Do **not** invoke or reference other agents by name — all capabilities are\n'
            printf '> available through the MCP tools configured in `.gemini/settings.json`.\n'
            printf '\n'
            cat "$_norm"
        } > "$dest_file"
    fi
    rm -f "$_norm"

    # Gemini routes delegation off description — flag weak ones for rewrite
    if [[ -z "$_weak_reason" && ${#desc} -lt 80 ]]; then
        _weak_reason="description under 80 chars (${#desc})"
    fi
    if [[ -n "$_weak_reason" ]]; then
        echo "   ⚠️  [gemini-agent] '$agent_name': weak routing description — $_weak_reason" >&2
    fi
}

# ─────────────────────────────────────────────────────────────────────────────
# _llm_init_convert_for_copilot <src_file> <dest_dir> [override_name]
#
# Writes a GitHub Copilot CLI-compatible custom agent file to dest_dir.
# Copilot's documented frontmatter (docs.github.com/en/copilot/reference/
# custom-agents-configuration, verified Sept 2026): description is required;
# name, tools, model, disable-model-invocation, user-invocable, mcp-servers,
# metadata are optional — tools defaults to "all tools" if omitted, which we
# rely on rather than mapping Claude/Gemini tool names to Copilot aliases.
# File convention: <name>.agent.md (confirmed against the repo's existing
# hand-written .github/agents/*.agent.md files).
#
# Mirrors _llm_init_convert_for_gemini's normalize-then-extract pipeline
# (same repo convention of per-format duplication over a shared helper) but
# differs in: destination filename suffix (.agent.md, not .md), the banner
# text (references .github/mcp.json), and omits the `tools` key entirely.
#
# <src_file>     : source .md file (agent stub or SKILL.md)
# <dest_dir>     : target directory (e.g. .github/agents)
# [override_name]: use this as the agent name instead of deriving from filename
#                  (needed for skills whose filename is always SKILL.md)
# ─────────────────────────────────────────────────────────────────────────────
_llm_init_convert_for_copilot() {
    local src_file="$1"
    local dest_dir="$2"
    local override_name="${3:-}"

    local filename agent_name dest_file desc body existing_desc

    filename=$(basename "$src_file")

    # Skip README
    [[ "$filename" == "README.md" ]] && return 0

    # Derive agent name from override or filename
    if [[ -n "$override_name" ]]; then
        agent_name="$override_name"
    else
        agent_name="${filename%.md}"
    fi

    # Defensive slug sanitization (Copilot's accepted charset for `name` is
    # undocumented beyond "derived from filename" — applying the same safety
    # net as Gemini since skill directory names are already slug-safe today).
    agent_name="$(printf '%s' "$agent_name" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9_-]/-/g')"

    # Rewrite names starting with a digit (e.g. 8d → eightd)
    if [[ "$agent_name" =~ ^[0-9] ]]; then
        case "${agent_name:0:1}" in
            0) agent_name="zero${agent_name:1}" ;;
            1) agent_name="one${agent_name:1}"  ;;
            2) agent_name="two${agent_name:1}"  ;;
            3) agent_name="three${agent_name:1}";;
            4) agent_name="four${agent_name:1}" ;;
            5) agent_name="five${agent_name:1}" ;;
            6) agent_name="six${agent_name:1}"  ;;
            7) agent_name="seven${agent_name:1}";;
            8) agent_name="eight${agent_name:1}";;
            9) agent_name="nine${agent_name:1}" ;;
        esac
    fi

    dest_file="${dest_dir}/${agent_name}.agent.md"

    # Normalize BEFORE the frontmatter gate (see _llm_init_convert_for_gemini
    # for why: a BOM/CRLF/leading blank line would misroute a frontmattered
    # file to the no-frontmatter branch and produce a duplicate --- block).
    local _norm
    _norm="$(mktemp "${TMPDIR:-/tmp}/llm-init-copilot.XXXXXX")"
    _llm_init_normalize_md "$src_file" "$_norm"

    local _weak_reason=""

    if head -1 "$_norm" | grep -q '^---$'; then
        # File has frontmatter — extract description, keep other keys as comments
        existing_desc=$(awk '
            BEGIN{f=0; in_desc=0; line=""; done=0}
            /^---$/{f++; next}
            f==1 && /^description:/{
                in_desc=1
                sub(/^description:[[:space:]]*/,"")
                sub(/^[>|][[:space:]]*/,"")
                line=$0
                next
            }
            f==1 && in_desc && /^[[:space:]]/{
                sub(/^[[:space:]]*/,"")
                line=line " " $0
                next
            }
            f==1 && in_desc && !done{ done=1; print line; exit }
            f==2 && in_desc && !done{ done=1; print line; exit }
            END{ if(in_desc && !done && line!="") print line }
        ' "$_norm")

        # Preserve every non-name/description source key as a YAML comment
        # (Copilot's schema is more permissive than Gemini's strict zod
        # schema, but comments are inert either way).
        local extra_keys_comments
        extra_keys_comments=$(awk '
            BEGIN{f=0; skip=1}
            /^---$/{f++; next}
            f==1 {
                if ($0 ~ /^[A-Za-z_][A-Za-z0-9_-]*:/) {
                    key=$0; sub(/:.*/,"",key)
                    skip = (key=="name" || key=="description") ? 1 : 0
                    if (!skip) print "# " $0
                } else if (!skip) {
                    print "# " $0
                }
                next
            }
            f>=2{exit}
        ' "$_norm")

        # Extract body (content after closing ---)
        body=$(awk 'BEGIN{count=0} /^---$/{count++; if(count==2){found=1; next}} found{print}' "$_norm")

        # Fallback: pull description from first H1 in the body
        if [[ -z "$existing_desc" ]]; then
            existing_desc=$(grep '^# ' "$_norm" | head -1 | sed 's/^# //')
            _weak_reason="description derived from first heading"
        fi
        if [[ -z "$existing_desc" ]]; then
            existing_desc="${agent_name} agent"
            _weak_reason="description is a generated placeholder"
        fi

        # Sanitize: strip YAML block scalar indicators and surrounding quotes, collapse whitespace
        existing_desc=$(printf '%s' "$existing_desc" \
            | sed 's/^[>|"[:space:]]*//' \
            | sed 's/[[:space:]"]*$//' \
            | tr '\n' ' ' \
            | sed 's/  */ /g')

        # Escape any remaining double-quotes inside the value
        existing_desc="${existing_desc//\"/\\\"}"

        {
            printf -- '---\n'
            printf 'name: %s\n' "$agent_name"
            printf 'description: "%s"\n' "$existing_desc"
            [[ -n "$extra_keys_comments" ]] && printf '%s\n' "$extra_keys_comments"
            printf -- '---\n'
            printf '\n'
            printf '> **[Copilot Standalone Mode]** Complete this task using direct MCP tool calls.\n'
            printf '> Do **not** invoke or reference other agents by name — all capabilities are\n'
            printf '> available through the MCP tools configured in `.github/mcp.json`.\n'
            printf '\n'
            printf '%s\n' "$body"
        } > "$dest_file"
        desc="$existing_desc"
    else
        # No frontmatter — extract description from first H1 heading
        desc=$(grep '^# ' "$_norm" | head -1 | sed 's/^# //')
        _weak_reason="source has no frontmatter; description derived from first heading"
        if [[ -z "$desc" ]]; then
            desc="${agent_name} agent"
            _weak_reason="source has no frontmatter; description is a generated placeholder"
        fi
        desc="${desc//\"/\\\"}"

        {
            printf -- '---\n'
            printf 'name: %s\n' "$agent_name"
            printf 'description: "%s"\n' "$desc"
            printf -- '---\n'
            printf '\n'
            printf '> **[Copilot Standalone Mode]** Complete this task using direct MCP tool calls.\n'
            printf '> Do **not** invoke or reference other agents by name — all capabilities are\n'
            printf '> available through the MCP tools configured in `.github/mcp.json`.\n'
            printf '\n'
            cat "$_norm"
        } > "$dest_file"
    fi
    rm -f "$_norm"

    # Copilot's docs don't specify a minimum description length, but weak
    # descriptions hurt automatic agent routing there too — flag consistently.
    if [[ -z "$_weak_reason" && ${#desc} -lt 80 ]]; then
        _weak_reason="description under 80 chars (${#desc})"
    fi
    if [[ -n "$_weak_reason" ]]; then
        echo "   ⚠️  [copilot-agent] '$agent_name': weak routing description — $_weak_reason" >&2
    fi
}

# ─────────────────────────────────────────────────────────────────────────────
# _llm_init_convert_for_gemini_command <src_file> <dest_dir> [override_name]
#
# Writes a Gemini CLI custom slash-command TOML file to dest_dir, so skills
# are invocable as /i-agile etc. (not just @i-agile via .gemini/agents/
# subagents — see _llm_init_convert_for_gemini above). Gemini custom
# commands require a top-level `prompt` string; `description` is optional
# but included for /help. See https://geminicli.com/docs/cli/custom-commands/
#
# <src_file>     : source .md file (agent stub or SKILL.md)
# <dest_dir>     : target directory (e.g. .gemini/commands)
# [override_name]: use this as the command name instead of deriving from filename
#                  (needed for skills whose filename is always SKILL.md)
# ─────────────────────────────────────────────────────────────────────────────
_llm_init_convert_for_gemini_command() {
    local src_file="$1"
    local dest_dir="$2"
    local override_name="${3:-}"

    local filename agent_name dest_file desc body existing_desc

    filename=$(basename "$src_file")

    # Skip README
    [[ "$filename" == "README.md" ]] && return 0

    # Derive command name from override or filename
    if [[ -n "$override_name" ]]; then
        agent_name="$override_name"
    else
        agent_name="${filename%.md}"
    fi

    # Rewrite names starting with a digit (e.g. 8d → eightd)
    if [[ "$agent_name" =~ ^[0-9] ]]; then
        case "${agent_name:0:1}" in
            0) agent_name="zero${agent_name:1}" ;;
            1) agent_name="one${agent_name:1}"  ;;
            2) agent_name="two${agent_name:1}"  ;;
            3) agent_name="three${agent_name:1}";;
            4) agent_name="four${agent_name:1}" ;;
            5) agent_name="five${agent_name:1}" ;;
            6) agent_name="six${agent_name:1}"  ;;
            7) agent_name="seven${agent_name:1}";;
            8) agent_name="eight${agent_name:1}";;
            9) agent_name="nine${agent_name:1}" ;;
        esac
    fi

    dest_file="${dest_dir}/${agent_name}.toml"

    # Normalize BOM/CRLF/leading blanks before the frontmatter gate (same
    # misroute hazard as _llm_init_convert_for_gemini).
    local _norm
    _norm="$(mktemp "${TMPDIR:-/tmp}/llm-init-gemini-cmd.XXXXXX")"
    _llm_init_normalize_md "$src_file" "$_norm"

    if head -1 "$_norm" | grep -q '^---$'; then
        # File has frontmatter — extract description, strip all other keys
        existing_desc=$(awk '
            BEGIN{f=0; in_desc=0; line=""; done=0}
            /^---$/{f++; next}
            f==1 && /^description:/{
                in_desc=1
                sub(/^description:[[:space:]]*/,"")
                sub(/^[>|][[:space:]]*/,"")
                line=$0
                next
            }
            f==1 && in_desc && /^[[:space:]]/{
                sub(/^[[:space:]]*/,"")
                line=line " " $0
                next
            }
            f==1 && in_desc && !done{ done=1; print line; exit }
            f==2 && in_desc && !done{ done=1; print line; exit }
            END{ if(in_desc && !done && line!="") print line }
        ' "$_norm")

        # Extract body (content after closing ---)
        body=$(awk 'BEGIN{count=0} /^---$/{count++; if(count==2){found=1; next}} found{print}' "$_norm")

        # Fallback: pull description from first H1 in the body
        if [[ -z "$existing_desc" ]]; then
            existing_desc=$(grep '^# ' "$_norm" | head -1 | sed 's/^# //')
        fi
        [[ -z "$existing_desc" ]] && existing_desc="${agent_name} agent"

        # Sanitize: strip YAML block scalar indicators and surrounding quotes, collapse whitespace
        existing_desc=$(printf '%s' "$existing_desc" \
            | sed 's/^[>|"[:space:]]*//' \
            | sed 's/[[:space:]"]*$//' \
            | tr '\n' ' ' \
            | sed 's/  */ /g')
    else
        # No frontmatter — extract description from first H1 heading
        existing_desc=$(grep '^# ' "$_norm" | head -1 | sed 's/^# //')
        [[ -z "$existing_desc" ]] && existing_desc="${agent_name} agent"
        body=$(cat "$_norm")
    fi
    rm -f "$_norm"

    # Escape any remaining double-quotes for the TOML basic-string `description`
    existing_desc="${existing_desc//\"/\\\"}"

    local banner full_body
    banner=$(printf '> **[Gemini Standalone Mode]** Complete this task using direct MCP tool calls.\n> Do **not** invoke or reference other agents by name — all capabilities are\n> available through the MCP tools configured in `.gemini/settings.json`.\n')
    full_body="${banner}
${body}"

    {
        printf 'description = "%s"\n' "$existing_desc"
        if [[ "$full_body" == *"'''"* ]]; then
            # Rare fallback: body contains a literal ''' (the TOML literal
            # multi-line string delimiter) — switch to a basic multi-line
            # string and escape backslashes plus any run of 3+ double-quotes.
            local escaped="${full_body//\\/\\\\}"
            while [[ "$escaped" == *'"""'* ]]; do
                escaped="${escaped/\"\"\"/\"\"\\\"}"
            done
            printf 'prompt = """\n%s\n"""\n' "$escaped"
        else
            printf "prompt = '''\n%s\n'''\n" "$full_body"
        fi
    } > "$dest_file"
}

# ─────────────────────────────────────────────────────────────────────────────
# _llm_init_doctor_gemini <dry_run> [target_dir]
#
# Idempotent repair + validation for an already-deployed repo's Gemini config.
# Invoked via: llm-init doctor --gemini [--dry-run] [target_dir]
#
# Repairs (timestamped backup taken before the first change; restore command
# printed): BOM / CRLF / leading blank lines; missing frontmatter (name from
# filename slug, description from first heading or first non-blank line, cut
# to 200 chars); unknown frontmatter keys commented out (allowlist replicates
# gemini-cli v0.59.0 localAgentSchema, packages/core/src/agents/agentLoader.ts
# lines 92-116, .strict()); files listed in .llm_settings/gemini-agent-exclude.txt
# moved to .gemini/agent-prompts/; ui.theme removed from repo settings.json
# (theme is per-user — belongs in ~/.gemini/settings.json only).
# Flags (no autofix): weak routing descriptions, double-frontmatter artifacts,
# reference-material candidates, MCP servers whose command would fail.
# ─────────────────────────────────────────────────────────────────────────────
_LLM_GEMINI_AGENT_KEYS="kind name description display_name tools mcp_servers model temperature max_turns timeout_mins"

_llm_init_doctor_gemini() {
    local _dry="$1"
    local _target="${2:-.}"

    local _root
    _root="$(cd "$_target" 2>/dev/null && git rev-parse --show-toplevel 2>/dev/null)" || {
        echo "❌ doctor: '$_target' is not inside a git repository (repo root is resolved from git, never hardcoded)" >&2
        return 2
    }

    echo "🩺 Gemini doctor — repo: $_root"
    $_dry && echo "   ⚠️  DRY RUN — reporting only, no files will be modified"
    echo "   Schema: gemini-cli v0.59.0 localAgentSchema (packages/core/src/agents/agentLoader.ts:92-116, strict)"
    echo ""

    local _agents_dir="$_root/.gemini/agents"
    local _prompts_dir="$_root/.gemini/agent-prompts"
    local _settings="$_root/.gemini/settings.json"
    local _exclude_list="$_root/.llm_settings/gemini-agent-exclude.txt"
    local _backup_dir=""
    local _fixed=0 _flagged=0 _failed=0

    _doctor_backup() {
        # Lazily snapshot .gemini/ before the first mutation
        [ -n "$_backup_dir" ] && return 0
        _backup_dir="$_root/.llm_settings/backups/gemini-doctor-$(date +%Y%m%d-%H%M%S)"
        mkdir -p "$_backup_dir"
        cp -R "$_root/.gemini" "$_backup_dir/"
        echo "   💾 Backup: $_backup_dir"
        echo "      Restore with: rsync -a --delete '$_backup_dir/.gemini/' '$_root/.gemini/'"
    }

    # ── 1. Agent files ────────────────────────────────────────────────
    if [ -d "$_agents_dir" ]; then
        local _f _base _issues _norm _changed
        for _f in "$_agents_dir"/*.md; do
            [ -e "$_f" ] || continue
            _base="$(basename "$_f")"
            _issues=""

            # Encoding/layout problems the loader hard-fails on
            [ "$(head -c 3 "$_f" | od -An -tx1 | tr -d ' \n')" = "efbbbf" ] && _issues="${_issues}BOM "
            LC_ALL=C grep -q $'\r' "$_f" && _issues="${_issues}CRLF "
            [ -z "$(head -1 "$_f")" ] && [ -s "$_f" ] && _issues="${_issues}leading-blank "

            if [ -n "$_issues" ]; then
                if $_dry; then
                    echo "   🔧 [would fix] $_base: ${_issues}"
                else
                    _doctor_backup
                    _norm="$(mktemp "${TMPDIR:-/tmp}/gemini-doctor.XXXXXX")"
                    _llm_init_normalize_md "$_f" "$_norm"
                    \mv -f "$_norm" "$_f"
                    echo "   🔧 Fixed $_base: ${_issues}"
                fi
                _fixed=$((_fixed+1))
            fi

            # Missing frontmatter → generate (name from filename slug,
            # description from first heading / first non-blank line, ≤200 chars)
            if ! head -1 "$_f" | grep -q '^---$'; then
                local _gname _gdesc
                _gname="$(printf '%s' "${_base%.md}" | tr '[:upper:]' '[:lower:]' | sed 's/[^a-z0-9_-]/-/g')"
                _gdesc="$(grep -m1 '^# ' "$_f" | sed 's/^# //')"
                [ -z "$_gdesc" ] && _gdesc="$(grep -m1 -v '^[[:space:]]*$' "$_f")"
                _gdesc="$(printf '%.200s' "$_gdesc" | sed 's/"/\\"/g')"
                if $_dry; then
                    echo "   🔧 [would fix] $_base: missing frontmatter (name: $_gname)"
                else
                    _doctor_backup
                    _norm="$(mktemp "${TMPDIR:-/tmp}/gemini-doctor.XXXXXX")"
                    {
                        printf -- '---\nname: %s\ndescription: "%s"\n---\n\n' "$_gname" "$_gdesc"
                        cat "$_f"
                    } > "$_norm"
                    \mv -f "$_norm" "$_f"
                    echo "   🔧 Fixed $_base: added frontmatter (name: $_gname) — description is a fallback, rewrite it"
                fi
                _fixed=$((_fixed+1)); _flagged=$((_flagged+1))
            fi

            # Unknown frontmatter keys → comment out (incl. continuation lines)
            local _bad_keys
            _bad_keys="$(awk -v allow="$_LLM_GEMINI_AGENT_KEYS" '
                BEGIN{ n=split(allow, a, " "); for(i=1;i<=n;i++) ok[a[i]]=1; f=0 }
                /^---$/{ f++; next }
                f==1 && /^[A-Za-z_][A-Za-z0-9_-]*:/ {
                    key=$0; sub(/:.*/,"",key)
                    if (!(key in ok)) print key
                }
                f>=2{ exit }
            ' "$_f" | sort -u | tr '\n' ' ')"
            if [ -n "${_bad_keys% }" ]; then
                if $_dry; then
                    echo "   🔧 [would fix] $_base: comment out unknown key(s): ${_bad_keys}"
                else
                    _doctor_backup
                    _norm="$(mktemp "${TMPDIR:-/tmp}/gemini-doctor.XXXXXX")"
                    awk -v allow="$_LLM_GEMINI_AGENT_KEYS" '
                        BEGIN{ n=split(allow, a, " "); for(i=1;i<=n;i++) ok[a[i]]=1; f=0; skip=0 }
                        /^---$/{ f++; print; next }
                        f==1 {
                            if ($0 ~ /^[A-Za-z_][A-Za-z0-9_-]*:/) {
                                key=$0; sub(/:.*/,"",key)
                                skip = (key in ok) ? 0 : 1
                            }
                            if (skip) print "# " $0; else print
                            next
                        }
                        { print }
                    ' "$_f" > "$_norm"
                    \mv -f "$_norm" "$_f"
                    echo "   🔧 Fixed $_base: commented out unknown key(s): ${_bad_keys}"
                fi
                _fixed=$((_fixed+1))
            fi

            # Double-frontmatter artifact (old converter bug: a second ---
            # block whose next line is name:) — flag only, never autofix
            local _dupline
            _dupline="$(awk 'BEGIN{f=0} /^---$/{f++; if(f>=3){print NR; exit}}' "$_f")"
            if [ -n "$_dupline" ] && sed -n "$((_dupline+1))p" "$_f" | grep -q '^name:'; then
                echo "   🚩 $_base: possible double-frontmatter artifact (extra --- + name: at line $_dupline) — inspect manually"
                _flagged=$((_flagged+1))
            fi

            # Validation replicating the loader (fail = Gemini would reject)
            local _vname _vdesc
            _vname="$(awk 'BEGIN{f=0} /^---$/{f++; next} f==1 && /^name:/{sub(/^name:[[:space:]]*/,""); print; exit}' "$_f")"
            _vdesc="$(awk 'BEGIN{f=0} /^---$/{f++; next} f==1 && /^description:/{sub(/^description:[[:space:]]*/,""); print; exit}' "$_f")"
            if ! head -1 "$_f" | grep -q '^---$'; then
                echo "   ❌ $_base: does not start with --- (loader: 'Missing mandatory YAML frontmatter')"
                _failed=$((_failed+1))
            elif [ -z "$_vname" ]; then
                echo "   ❌ $_base: missing required 'name'"
                _failed=$((_failed+1))
            elif ! printf '%s' "$_vname" | grep -Eq '^[a-z0-9_-]+$'; then
                echo "   ❌ $_base: name '$_vname' violates slug ^[a-z0-9-_]+\$"
                _failed=$((_failed+1))
            elif [ -z "$_vdesc" ] || [ "$_vdesc" = '""' ]; then
                echo "   ❌ $_base: missing/empty required 'description'"
                _failed=$((_failed+1))
            fi

            # Weak routing description — flag
            local _dlen
            _dlen="$(printf '%s' "$_vdesc" | sed 's/^"//; s/"$//' | wc -c | tr -d ' ')"
            if [ -n "$_vdesc" ] && [ "$_dlen" -lt 80 ]; then
                echo "   🚩 $_base: weak routing description (${_dlen} chars) — rewrite for delegation quality"
                _flagged=$((_flagged+1))
            fi

            # Reference-material handling: move ONLY if explicitly listed
            local _aname="${_base%.md}"
            if [ -f "$_exclude_list" ] && grep -v '^[[:space:]]*#' "$_exclude_list" | grep -qxF "$_aname"; then
                if $_dry; then
                    echo "   🔧 [would fix] $_base: listed as reference material → move to .gemini/agent-prompts/"
                else
                    _doctor_backup
                    mkdir -p "$_prompts_dir"
                    \mv -f "$_f" "$_prompts_dir/$_base"
                    echo "   🔧 Moved $_base → .gemini/agent-prompts/ (reference material, per exclude list)"
                fi
                _fixed=$((_fixed+1))
                continue
            elif ! grep -Eiq 'you are|your role|act as|you will|your (task|job|responsibility)' "$_f"; then
                echo "   🚩 $_base: no agent framing detected — reference material? Add to $_exclude_list to relocate"
                _flagged=$((_flagged+1))
            fi
        done
    else
        echo "   ⚠️  No .gemini/agents/ directory — nothing to check"
    fi
    echo ""

    # ── 2. settings.json ──────────────────────────────────────────────
    echo "   ⚙️  .gemini/settings.json"
    if [ -f "$_settings" ]; then
        if command -v jq >/dev/null 2>&1; then
            if ! jq empty "$_settings" 2>/dev/null; then
                echo "   ❌ settings.json: invalid JSON"
                _failed=$((_failed+1))
            else
                # ui.theme must never be committed at repo level (per-user setting)
                if [ "$(jq -r '.ui.theme // empty' "$_settings")" != "" ]; then
                    if $_dry; then
                        echo "   🔧 [would fix] settings.json: remove repo-level ui.theme (theme is per-user)"
                    else
                        _doctor_backup
                        local _tmp="$_settings.doc.$$"
                        jq 'del(.ui.theme) | if .ui == {} then del(.ui) else . end' "$_settings" > "$_tmp" \
                            && \mv -f "$_tmp" "$_settings" \
                            && echo "   🔧 Fixed settings.json: removed repo-level ui.theme"
                    fi
                    _fixed=$((_fixed+1))
                fi
                # MCP server launchability
                local _srv _cmd _url
                while IFS= read -r _srv; do
                    _cmd="$(jq -r --arg s "$_srv" '.mcpServers[$s].command // empty' "$_settings")"
                    _url="$(jq -r --arg s "$_srv" '.mcpServers[$s].url // .mcpServers[$s].httpUrl // empty' "$_settings")"
                    if [ -n "$_url" ]; then
                        echo "      ℹ️  $_srv: remote ($_url) — reachability not checked"
                    elif [ -z "$_cmd" ]; then
                        echo "      ❌ $_srv: no command and no url"
                        _failed=$((_failed+1))
                    elif [ -x "$_cmd" ] || [ -x "$_root/$_cmd" ] || command -v "$_cmd" >/dev/null 2>&1; then
                        echo "      ✅ $_srv: command resolves"
                    else
                        echo "      ❌ $_srv: command not found/executable: $_cmd"
                        _failed=$((_failed+1))
                    fi
                done < <(jq -r '.mcpServers // {} | keys[]' "$_settings")
            fi
        else
            echo "   ⚠️  jq not found — settings.json checks skipped"
        fi
    else
        echo "   ⚠️  No .gemini/settings.json"
    fi
    echo ""

    # ── Summary ───────────────────────────────────────────────────────
    echo "   ── doctor summary ──────────────────────────────"
    echo "   fixes applied/planned: $_fixed   flags: $_flagged   validation failures: $_failed"
    [ -n "$_backup_dir" ] && echo "   restore: rsync -a --delete '$_backup_dir/.gemini/' '$_root/.gemini/'"
    echo ""
    echo "   📋 git status (repo changes here affect everyone who pulls):"
    git -C "$_root" status --short | sed 's/^/      /'
    echo ""
    [ "$_failed" -gt 0 ] && return 1
    return 0
}

# ─────────────────────────────────────────────────────────────────────────────
# _llm_init_doctor_agy [target_dir]
#
# READ-ONLY diagnostics for "agy (Antigravity CLI) does not see this repo's
# skills/agents". Invoked via: llm-init doctor --agy [target_dir]
#
# Checks: host + llm_settings commit; agy binary/version (vs the version the
# .agents/ layout was tested with) and PATH shadowing; ~/.gemini/antigravity-cli
# trustedWorkspaces; .agents/{skills,agents,plugins/llm-settings} layout and
# repo-tools selection; per-skill frontmatter (name == folder, description) and
# the 24000-byte SKILL.md limit; agent frontmatter; broken symlinks; drift vs a
# fresh render from llm_settings; `agy plugin validate`; name collisions with
# ~/.agents/skills; recent skill/agent/plugin errors in cli.log (redacted).
# Ends with a sorted key=value fingerprint — diff it between a working and a
# failing host. Writes nothing, makes no auth calls, never prints settings.json
# contents or tokens. rc 0 healthy, 1 problems found, 2 usage/not a repo.
# ─────────────────────────────────────────────────────────────────────────────
_LLM_INIT_AGY_TESTED_VERSION="1.4.2"   # the agy release the .agents/ layout was verified with
_LLM_INIT_AGY_SKILL_LIMIT=24000        # agy loads only the first 24000 bytes of a SKILL.md

_llm_init_doctor_agy() {
    local _target="${1:-.}"
    local _root
    _root="$(cd "$_target" 2>/dev/null && git rev-parse --show-toplevel 2>/dev/null)" || {
        echo "❌ doctor: '$_target' is not inside a git repository" >&2
        return 2
    }
    _root="$(cd "$_root" && pwd -P)"

    local _failed=0 _warned=0 _suspect=""
    local _state="$HOME/.gemini/antigravity-cli"
    _agy_doc_bad()  { echo "   ❌ $*"; _failed=$((_failed+1)); }
    _agy_doc_warn() { echo "   ⚠️  $*"; _warned=$((_warned+1)); }
    _agy_doc_ok()   { echo "   ✅ $*"; }
    local _shown=0
    _agy_doc_item() { # per-skill/agent failure: counted always, printed for the first 20
        _failed=$((_failed+1)); _shown=$((_shown+1))
        [ "$_shown" -le 20 ] && echo "   ❌ $*"
        [ "$_shown" -eq 21 ] && echo "   ❌ … more skill/agent problems (counted in the summary, not shown)"
        return 0
    }
    _agy_doc_fm()   { # <file> <key> — frontmatter value, quotes/CR stripped
        tr -d '\r' < "$1" | awk -v k="$2" 'NR==1 && $0!="---"{exit} NR==1{next} /^---[[:space:]]*$/{exit}
            $0 ~ "^"k":" { sub("^"k":[[:space:]]*",""); gsub(/^["'"'"']|["'"'"'][[:space:]]*$/,""); print; exit }'
    }

    echo "🩺 agy doctor — repo: $_root (read-only)"
    echo ""

    # ── 1. Host + llm_settings source ─────────────────────────────────
    local _host _os _src_root="" _src="" _c _src_commit="none" _repo_commit
    _host="$(hostname -s 2>/dev/null || hostname)"
    if [ "$(uname -s)" = "Darwin" ]; then
        _os="Darwin-$(uname -m)-$(sw_vers -productVersion 2>/dev/null)"
    else
        _os="$(uname -s)-$(uname -m)-$(uname -r)"
    fi
    for _c in "${LLM_SETTINGS_DIR:-}" \
              "$(cd "$(dirname "${BASH_SOURCE[0]:-.}")/../.." 2>/dev/null && pwd -P)" \
              "$HOME/Development/llm_settings"; do
        [ -n "$_c" ] || continue
        if [ -d "$_c/.llm_settings/skills" ]; then _src_root="$_c"; _src="$_c/.llm_settings"; break; fi
        if [ -d "$_c/llm_settings/skills" ];  then _src_root="$_c"; _src="$_c/llm_settings";  break; fi
    done
    _repo_commit="$(git -C "$_root" rev-parse --short HEAD 2>/dev/null || echo none)"
    echo "🖥️  Host: $_host  ($_os, bash $BASH_VERSION)"
    if [ -n "$_src_root" ]; then
        _src_commit="$(git -C "$_src_root" rev-parse --short HEAD 2>/dev/null || echo unknown)"
        echo "      llm_settings: $_src_root @ $_src_commit"
        if [ -n "$(git -C "$_src_root" status --porcelain --untracked-files=no 2>/dev/null)" ]; then
            _agy_doc_warn "llm_settings checkout has uncommitted changes — hosts may not be deploying the same source"
        fi
        local _behind
        _behind="$(git -C "$_src_root" rev-list --count HEAD..origin/main 2>/dev/null || echo 0)"
        if [ "${_behind:-0}" -gt 0 ] 2>/dev/null; then
            _agy_doc_warn "llm_settings is $_behind commit(s) behind origin/main (as of the last fetch) — git pull, then re-run llm-init"
        fi
    else
        _agy_doc_bad "llm_settings source not found — set LLM_SETTINGS_DIR (drift check skipped)"
    fi
    echo "      repo commit: $_repo_commit"
    echo ""

    # ── 2. agy binary + version ───────────────────────────────────────
    echo "🔎 agy binary"
    local _bin="" _ver="none" _p _sums=""
    if [ -x "$HOME/.local/bin/agy" ]; then
        _bin="$HOME/.local/bin/agy"           # same resolution order as _agy_bin in ~/.aliasesrc
    else
        _bin="$(type -P agy 2>/dev/null || true)"
    fi
    if [ -z "$_bin" ]; then
        _agy_doc_bad "agy binary not found (~/.local/bin/agy or PATH)"
    else
        _ver="$(_llm_init_bounded 10 "$_bin" --version 2>/dev/null | grep -Eo '[0-9]+(\.[0-9]+)+' | head -1)"
        [ -n "$_ver" ] || _ver="unknown"
        if [ "$_ver" = "$_LLM_INIT_AGY_TESTED_VERSION" ]; then
            _agy_doc_ok "agy $_ver at $_bin (the version llm-init's agy layout was tested with)"
        else
            _agy_doc_warn "agy $_ver at $_bin — llm-init's agy layout was tested with $_LLM_INIT_AGY_TESTED_VERSION"
            _suspect="agy $_ver (tested: $_LLM_INIT_AGY_TESTED_VERSION)"
        fi
        echo "      binary modified: $(date -r "$_bin" '+%Y-%m-%d %H:%M' 2>/dev/null || stat -c %y "$_bin" 2>/dev/null | cut -c1-16) (agy self-updates — see ~/.gemini/antigravity-cli/updater)"
        if [ -f "$_state/updater/update_status.json" ] && command -v jq >/dev/null 2>&1; then
            echo "      updater: $(jq -r '.message // empty' "$_state/updater/update_status.json" 2>/dev/null | cut -c1-120)"
        fi
        # Several different agy binaries on PATH → which one runs depends on the shell
        for _p in "$HOME/.local/bin/agy" $(type -aP agy 2>/dev/null); do
            [ -x "$_p" ] || continue
            _sums="${_sums}$(cksum < "$_p" | awk '{print $1}') $_p"$'\n'
        done
        if [ "$(printf '%s' "$_sums" | awk 'NF{print $1}' | sort -u | wc -l | tr -d ' ')" -gt 1 ]; then
            _agy_doc_warn "different agy binaries found — the one that runs depends on PATH:"
            printf '%s' "$_sums" | awk 'NF{print "      • " $2}' | sort -u
        fi
    fi
    echo ""

    # ── 3. agy user state: trusted workspaces ─────────────────────────
    echo "🗂️  agy state (~/.gemini/antigravity-cli)"
    local _settings="$_state/settings.json" _trusted="no"
    if [ ! -f "$_settings" ]; then
        _agy_doc_bad "no ~/.gemini/antigravity-cli/settings.json — has agy been started on this host?"
        _trusted="unknown"
    elif ! command -v jq >/dev/null 2>&1; then
        _agy_doc_warn "jq not found — trustedWorkspaces check skipped"
        _trusted="unknown"
    elif ! jq empty "$_settings" 2>/dev/null; then
        _agy_doc_bad "settings.json is not valid JSON"
        _trusted="unknown"
    else
        local _w _wp
        while IFS= read -r _w; do
            [ -n "$_w" ] || continue
            _wp="$(cd "$_w" 2>/dev/null && pwd -P || printf '%s' "${_w%/}")"
            case "$_root/" in "$_wp"/*) _trusted="yes"; break ;; esac
        done < <(jq -r '.trustedWorkspaces // [] | .[]' "$_settings" 2>/dev/null)
        if [ "$_trusted" = "yes" ]; then
            _agy_doc_ok "repo is trusted (covered by trustedWorkspaces entry $_wp)"
        else
            _agy_doc_bad "repo is not in trustedWorkspaces — agy may ignore workspace skills/agents/plugins; start agy in $_root once and accept the trust prompt"
        fi
        echo "      permissions.allow entries: $(jq '.permissions.allow // [] | length' "$_settings" 2>/dev/null)"
    fi
    if [ -f "$HOME/.config/gcloud/application_default_credentials.json" ]; then
        echo "      ADC credentials file: present (validity not checked)"
    else
        echo "      ADC credentials file: absent (the agy wrapper needs it to chat; listing skills does not)"
    fi
    echo ""

    # ── 4. Layout ─────────────────────────────────────────────────────
    echo "📁 Layout (.agents/)"
    local _sk="$_root/.agents/skills" _ag="$_root/.agents/agents" _pl="$_root/.agents/plugins/llm-settings"
    [ -d "$_sk" ] && _agy_doc_ok ".agents/skills present" || _agy_doc_bad ".agents/skills missing — run llm-init in this repo"
    [ -d "$_ag" ] && _agy_doc_ok ".agents/agents present" || _agy_doc_bad ".agents/agents missing — run llm-init in this repo"
    if [ -f "$_pl/plugin.json" ] && [ -f "$_pl/mcp_config.json" ]; then
        _agy_doc_ok ".agents/plugins/llm-settings/{plugin.json,mcp_config.json} present"
    else
        _agy_doc_bad ".agents/plugins/llm-settings incomplete (plugin.json + mcp_config.json) — run llm-init"
    fi
    # Plugin MCP commands: agy starts them with the plugin folder as cwd, so a repo-relative
    # command must resolve from there (../../../<path>); an absolute path only works on the
    # host that wrote it.
    if [ -f "$_pl/mcp_config.json" ] && command -v jq >/dev/null 2>&1; then
        local _srv _cmd _mcp_ok=0 _mcp_bad=0
        while IFS=$'\t' read -r _srv _cmd; do
            [ -n "$_srv" ] || continue
            case "$_cmd" in
                "") ;;   # url-based server — nothing to resolve
                /*)  if [ -x "$_cmd" ]; then _mcp_ok=$((_mcp_ok+1)); else
                         _agy_doc_bad "MCP server $_srv: $_cmd does not exist here — absolute path written on another host? re-run llm-init"
                         _mcp_bad=$((_mcp_bad+1)); fi ;;
                */*) if [ -x "$_pl/$_cmd" ]; then _mcp_ok=$((_mcp_ok+1)); else
                         _agy_doc_bad "MCP server $_srv: $_cmd does not resolve from .agents/plugins/llm-settings/"
                         _mcp_bad=$((_mcp_bad+1)); fi ;;
                *)   if command -v "$_cmd" >/dev/null 2>&1; then _mcp_ok=$((_mcp_ok+1)); else
                         _agy_doc_warn "MCP server $_srv: $_cmd not on this shell's PATH (agy's PATH may differ)"; fi ;;
            esac
        done < <(jq -r '.mcpServers // {} | to_entries[] | "\(.key)\t\(.value.command // "")"' "$_pl/mcp_config.json" 2>/dev/null)
        [ "$_mcp_bad" -eq 0 ] && _agy_doc_ok "plugin MCP commands resolve ($_mcp_ok checked)"
    fi
    [ -f "$_root/.agents/mcp_config.json" ] && _agy_doc_warn "legacy .agents/mcp_config.json present (agy ignores it; llm-init removes it)"
    [ -d "$_root/.agent" ] && _agy_doc_warn ".agent/ (singular) exists — llm-init deploys to .agents/; check which one this agy version reads"
    local _rt="$_root/.llm_settings/repo-tools"
    if [ -f "$_rt" ]; then
        if grep -v '^#' "$_rt" | tr -d '[:blank:]' | grep -qxE 'agy|all'; then
            _agy_doc_ok ".llm_settings/repo-tools selects agy"
        else
            _agy_doc_bad "agy is not selected in .llm_settings/repo-tools — run: llm-init --tools <current list>,agy ."
        fi
    else
        _agy_doc_warn "no .llm_settings/repo-tools — repo was deployed by an older llm-init; re-run llm-init"
    fi
    echo ""

    # ── 5. Skills ─────────────────────────────────────────────────────
    echo "📚 Skills"
    local _skills_count=0 _oversize=0 _d _f _n _v _sz
    if [ -d "$_sk" ]; then
        for _d in "$_sk"/*/; do
            [ -d "$_d" ] || continue
            _n="$(basename "$_d")"; _f="${_d}SKILL.md"
            if [ ! -f "$_f" ]; then _agy_doc_item "skill $_n: no SKILL.md"; continue; fi
            _skills_count=$((_skills_count+1))
            [ "$(head -c 3 "$_f" | od -An -tx1 | tr -d ' \n')" = "efbbbf" ] && _agy_doc_item "skill $_n: UTF-8 BOM before frontmatter"
            LC_ALL=C grep -q $'\r' "$_f" && _agy_doc_item "skill $_n: CRLF line endings"
            if [ "$(head -1 "$_f" | tr -d '\r' | sed $'s/^\xef\xbb\xbf//')" != "---" ]; then
                _agy_doc_item "skill $_n: no YAML frontmatter"
            else
                _v="$(_agy_doc_fm "$_f" name)"
                if [ -z "$_v" ]; then
                    _agy_doc_item "skill $_n: frontmatter has no name"
                elif [ "$_v" != "$_n" ]; then
                    _agy_doc_item "skill $_n: frontmatter name '$_v' ≠ folder '$_n' (agy requires them equal)"
                elif [ "${#_v}" -gt 64 ] || ! [[ "$_v" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
                    _agy_doc_item "skill $_n: name is not lowercase-hyphen ≤64 chars"
                fi
                [ -n "$(_agy_doc_fm "$_f" description)" ] || _agy_doc_item "skill $_n: frontmatter has no description"
            fi
            _sz="$(wc -c < "$_f" | tr -d ' ')"
            if [ "$_sz" -gt "$_LLM_INIT_AGY_SKILL_LIMIT" ]; then
                _agy_doc_item "skill $_n: SKILL.md is $_sz bytes > $_LLM_INIT_AGY_SKILL_LIMIT (agy reads only the first $_LLM_INIT_AGY_SKILL_LIMIT) — move sections to references/"
                _oversize=$((_oversize+1))
            fi
        done
        echo "      $_skills_count skill(s) checked"
    fi

    # ── 6. Agents ─────────────────────────────────────────────────────
    echo "🤖 Agents"
    local _agents_count=0
    if [ -d "$_ag" ]; then
        for _f in "$_ag"/*.md; do
            [ -f "$_f" ] || continue
            _n="$(basename "$_f" .md)"
            _agents_count=$((_agents_count+1))
            if [ "$(head -1 "$_f" | tr -d '\r')" != "---" ]; then
                _agy_doc_item "agent $_n: no YAML frontmatter"
                continue
            fi
            _v="$(_agy_doc_fm "$_f" name)"
            [ -n "$_v" ] || _agy_doc_item "agent $_n: frontmatter has no name"
            [ -z "$_v" ] || [ "$_v" = "$_n" ] || _agy_doc_item "agent $_n: frontmatter name '$_v' ≠ filename"
            [ -n "$(_agy_doc_fm "$_f" description)" ] || _agy_doc_item "agent $_n: frontmatter has no description"
        done
        echo "      $_agents_count agent(s) checked"
    fi

    # ── 7. Broken symlinks ────────────────────────────────────────────
    local _l
    if [ -d "$_root/.agents" ]; then
        while IFS= read -r _l; do
            _agy_doc_bad "broken symlink: ${_l#"$_root"/}"
        done < <(find "$_root/.agents" -type l ! -exec test -e {} \; -print 2>/dev/null)
    fi
    echo ""

    # ── 8. Drift vs a fresh render from llm_settings ──────────────────
    echo "🔁 Drift (deployed vs llm_settings @ $_src_commit)"
    local _drift=0 _missing=0 _exp _e _rel
    if [ -n "$_src" ] && [ -d "$_sk" ]; then
        _exp="$(mktemp -d "${TMPDIR:-/tmp}/agy-doctor.XXXXXX")"
        ( cd "$_exp" \
            && _LLM_INIT_TOOLS=" claude agy " _llm_init_deploy_shared_skills false "$_src" all \
            && _LLM_INIT_TOOLS=" claude agy " _llm_init_deploy_tool_agents false "$_src" all ) >/dev/null 2>&1
        for _d in "$_exp/.agents/skills"/*/; do
            [ -d "$_d" ] || continue
            _n="$(basename "$_d")"
            if [ ! -d "$_sk/$_n" ]; then _missing=$((_missing+1)); continue; fi
            while IFS= read -r _e; do
                _rel="${_e#"$_exp"/}"
                if ! cmp -s "$_e" "$_root/$_rel"; then
                    _drift=$((_drift+1))
                    [ "$_drift" -le 10 ] && echo "      ≠ $_rel"
                fi
            done < <(find "$_d" -type f 2>/dev/null)
        done
        for _e in "$_exp/.agents/agents"/*.md; do
            [ -f "$_e" ] || continue
            _rel="${_e#"$_exp"/}"
            if [ ! -f "$_root/$_rel" ]; then _missing=$((_missing+1))
            elif ! cmp -s "$_e" "$_root/$_rel"; then
                _drift=$((_drift+1))
                [ "$_drift" -le 10 ] && echo "      ≠ $_rel"
            fi
        done
        rm -rf "$_exp"
        if [ "$_drift" -gt 0 ]; then
            _agy_doc_bad "$_drift deployed file(s) differ from llm_settings — re-run llm-init in $_root"
        else
            _agy_doc_ok "deployed skills/agents match llm_settings"
        fi
        [ "$_missing" -gt 0 ] && _agy_doc_warn "$_missing skill(s)/agent(s) in llm_settings are not deployed here (expected with a --skills profile; otherwise re-run llm-init)"
    else
        echo "      skipped (no llm_settings source or no .agents/skills)"
    fi
    echo ""

    # ── 9. agy's own view ─────────────────────────────────────────────
    echo "🔌 agy plugin check"
    local _pv="skipped" _vj _errs
    if [ -n "$_bin" ] && command -v jq >/dev/null 2>&1; then
        _vj="$(cd "$_root" && _llm_init_bounded 20 "$_bin" plugin validate .agents/plugins/llm-settings --json 2>/dev/null)"
        if printf '%s' "$_vj" | jq -e 'type == "object"' >/dev/null 2>&1; then
            _errs="$(printf '%s' "$_vj" | jq '[.findings[]? | select(.severity == "error")] | length')"
            if [ "$_errs" = "0" ]; then
                _pv="ok"
                _agy_doc_ok "agy plugin validate: ok $(printf '%s' "$_vj" | jq -c '.components // {}')"
            else
                _pv="fail"
                _agy_doc_bad "agy plugin validate: $_errs error(s)"
                printf '%s' "$_vj" | jq -r '.findings[]? | "      • \(.severity): \(.file): \(.message)"' | head -5
            fi
        else
            _pv="unknown"
            _agy_doc_warn "agy plugin validate returned no JSON (agy $_ver may not support it)"
        fi
        if (cd "$_root" && _llm_init_bounded 20 "$_bin" plugin list --json 2>/dev/null) \
                | jq -e 'map(.name) | index("llm-settings") != null' >/dev/null 2>&1; then
            echo "      ℹ️  agy plugin list includes llm-settings"
        else
            echo "      ℹ️  agy plugin list does not include llm-settings (it may only list installed plugins)"
        fi
    else
        echo "      skipped (no agy binary or no jq)"
    fi
    echo ""

    # ── 10. Collisions with user-level skills ─────────────────────────
    local _col=""
    if [ -d "$HOME/.agents/skills" ] && [ -d "$_sk" ]; then
        for _d in "$HOME/.agents/skills"/*/; do
            [ -d "$_d" ] || continue
            _n="$(basename "$_d")"
            [ -d "$_sk/$_n" ] && _col="${_col} $_n"
        done
        [ -n "$_col" ] && _agy_doc_warn "skill name(s) in both ~/.agents/skills and the repo:${_col} — agy may load either copy"
    fi

    # ── 11. Recent agy log errors (redacted) ──────────────────────────
    local _hits
    if [ -f "$_state/cli.log" ]; then
        _hits="$(tail -n 300 "$_state/cli.log" 2>/dev/null \
            | grep -E '^[EWF][0-9]{4} ' | grep -iE 'skill|agent|plugin|workspace' | tail -n 10 \
            | sed -E 's/(ya29\.|sk-|ghp_|gho_|github_pat_|AIza)[A-Za-z0-9._-]+/\1<redacted>/g;
                      s/(([Tt]oken|TOKEN|[Kk]ey|KEY|[Ss]ecret|SECRET|[Pp]assword|PASSWORD|[Aa]uthorization)[=:][[:space:]]*)[^[:space:]]+/\1<redacted>/g;
                      s/[A-Za-z0-9+\/_=-]{40,}/<redacted>/g' \
            | cut -c1-200)"
        if tail -n 300 "$_state/cli.log" 2>/dev/null | grep -q 'not logged into Antigravity'; then
            _agy_doc_warn "agy's last session logged 'You are not logged into Antigravity' — start agy and sign in, then re-check (workspace loading may depend on it)"
        fi
        if [ -n "$_hits" ]; then
            _agy_doc_warn "recent ~/.gemini/antigravity-cli/cli.log errors/warnings about skills/agents/plugins/workspace:"
            printf '%s\n' "$_hits" | sed 's/^/      │ /'
        fi
    fi
    echo ""

    # ── Fingerprint (diff between hosts) ──────────────────────────────
    local _sksha="none" _agsha="none"
    [ -d "$_sk" ] && _sksha="$(cd "$_root/.agents" && find skills -type f 2>/dev/null | LC_ALL=C sort \
        | while IFS= read -r _f; do cksum "$_f"; done | cksum | awk '{print $1}')"
    [ -d "$_ag" ] && _agsha="$(cd "$_root/.agents" && find agents -type f 2>/dev/null | LC_ALL=C sort \
        | while IFS= read -r _f; do cksum "$_f"; done | cksum | awk '{print $1}')"
    echo "--- agy-doctor fingerprint ---"
    {
        echo "agents_count=$_agents_count"
        echo "agents_sha=$_agsha"
        echo "agy_path=$(printf '%s' "$_bin" | sed "s|^$HOME|~|")"
        echo "agy_version=$_ver"
        echo "drift_count=$_drift"
        echo "host=$_host"
        echo "llm_settings_commit=$_src_commit"
        echo "os=$_os"
        echo "oversize_count=$_oversize"
        echo "plugin_validate=$_pv"
        echo "repo_commit=$_repo_commit"
        echo "skills_count=$_skills_count"
        echo "skills_sha=$_sksha"
        echo "trusted=$_trusted"
    } | LC_ALL=C sort
    echo "--- end fingerprint ---"
    echo ""

    # ── Summary ───────────────────────────────────────────────────────
    echo "   ── agy doctor summary ──────────────────────────"
    echo "   ❌ Failures: $_failed   ⚠️  Warnings: $_warned"
    if [ "$_failed" -eq 0 ] && [ -n "$_suspect" ]; then
        echo "   🧭 The deploy is correct on disk; the remaining difference is $_suspect."
        echo "      Compare with a working host:"
        echo "      diff <(ssh <good-host> 'cd <repo> && llm-init doctor --agy' | sed -n '/fingerprint ---/,/end fingerprint/p') \\"
        echo "           <(ssh <bad-host>  'cd <repo> && llm-init doctor --agy' | sed -n '/fingerprint ---/,/end fingerprint/p')"
    fi
    echo ""
    [ "$_failed" -gt 0 ] && return 1
    return 0
}

# ─────────────────────────────────────────────────────────────────────────────
# _llm_init_shell_bootstrap [--theme <name>]
#
# OPT-IN user-level bootstrap (never run by a repo deploy): installs the
# shell-matched gemini/vertex wrapper snippet to ~/.gemini-vertex.<shell> and
# adds a guarded source line to the matching rc file. Optionally sets
# ui.theme in ~/.gemini/settings.json (user scope ONLY — theme depends on
# each person's terminal background and must never land in repo settings).
# Detects the user's shell from $SHELL; never assumes zsh. The snippets are
# side-effect free at source time (no venv creation, no gcloud calls).
# ─────────────────────────────────────────────────────────────────────────────
_llm_init_shell_bootstrap() {
    local _theme=""
    while [ $# -gt 0 ]; do
        case "$1" in
            --theme) shift; _theme="${1:-}"; [ -z "$_theme" ] && { echo "llm-init: --theme requires a value (e.g. 'ANSI Light')" >&2; return 2; }; shift ;;
            *) echo "llm-init: unknown --shell-bootstrap arg: '$1'" >&2; return 2 ;;
        esac
    done

    local _src_dir=""
    if [ -n "${BASH_SOURCE[0]:-}" ]; then
        _src_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/../shell" 2>/dev/null && pwd)"
    fi
    [ -z "$_src_dir" ] && [ -d ".llm_settings/shell" ] && _src_dir="$(cd .llm_settings/shell && pwd)"
    if [ -z "$_src_dir" ] || [ ! -d "$_src_dir" ]; then
        echo "❌ shell-bootstrap: snippet directory not found (.llm_settings/shell/)" >&2
        return 1
    fi

    local _shell_name _rc _snippet
    case "${SHELL:-}" in
        */zsh)  _shell_name="zsh";  _rc="$HOME/.zshrc";  _snippet="gemini-vertex.zsh" ;;
        */bash) _shell_name="bash"; _rc="$HOME/.bashrc"; _snippet="gemini-vertex.bash" ;;
        *)
            echo "❌ shell-bootstrap: unsupported \$SHELL '${SHELL:-unset}' (zsh and bash supported)" >&2
            return 1 ;;
    esac

    local _dest="$HOME/.gemini-vertex.$_shell_name"
    echo "🐚 Shell bootstrap ($_shell_name)"
    cp "$_src_dir/$_snippet" "$_dest"
    if [ "$_shell_name" = "bash" ]; then
        bash -n "$_dest" || { echo "❌ $_dest failed bash -n" >&2; return 1; }
    else
        zsh -n "$_dest" 2>/dev/null || { echo "❌ $_dest failed zsh -n" >&2; return 1; }
    fi
    echo "   ✅ Installed $_dest (syntax-checked)"

    local _guard="[ -f \"\$HOME/.gemini-vertex.$_shell_name\" ] && . \"\$HOME/.gemini-vertex.$_shell_name\""
    if [ -f "$_rc" ] && grep -qF ".gemini-vertex.$_shell_name" "$_rc"; then
        echo "   ✅ $_rc already sources the snippet"
    else
        printf '\n# Gemini CLI via Vertex AI (installed by llm-init --shell-bootstrap)\n%s\n' "$_guard" >> "$_rc"
        echo "   ✅ Added guarded source line to $_rc"
    fi

    if [ -n "$_theme" ]; then
        local _usettings="$HOME/.gemini/settings.json"
        if command -v jq >/dev/null 2>&1; then
            mkdir -p "$HOME/.gemini"
            [ -f "$_usettings" ] || printf '{}' > "$_usettings"
            local _tmp="$_usettings.sb.$$"
            jq --arg t "$_theme" '.ui.theme = $t' "$_usettings" > "$_tmp" && \mv -f "$_tmp" "$_usettings" \
                && echo "   ✅ Set ui.theme='$_theme' in $_usettings (user scope only)"
        else
            echo "   ⚠️  jq not found — set ui.theme manually in $_usettings" >&2
        fi
    fi
    echo "   Done. Open a new shell (or: . $_rc) to pick up the wrapper."
}

# ─────────────────────────────────────────────────────────────────────────────
# _llm_init_merge_claude_md <src> <tgt> <dry_run>
#
# Smart CLAUDE.md deployment:
#   - No target       → deploy full template (as before)
#   - Has markers     → replace only the llm-init block, preserve repo sections
#   - No markers      → preserve entirely (repo owns its own CLAUDE.md)
# ─────────────────────────────────────────────────────────────────────────────
_llm_init_merge_claude_md() {
    local _src="$1"
    local _tgt="$2"
    local _dry_run="${3:-false}"

    local _start_marker="## LLM OPERATING CONTEXT (llm-init)"
    local _end_marker="END OF LLM OPERATING CONTEXT (llm-init)"

    # Case 1: No target — deploy full template
    if [ ! -f "$_tgt" ]; then
        if $_dry_run; then
            echo "   ℹ️  [dry-run] Would deploy CLAUDE.md (new)"
        else
            cp "$_src" "$_tgt"
            echo "   ✅ CLAUDE.md deployed (new)"
        fi
        return 0
    fi

    # Case 2: Target exists WITHOUT markers — preserve entirely
    if ! grep -q "$_start_marker" "$_tgt"; then
        echo "   ✅ CLAUDE.md preserved (no llm-init markers; repo-specific file kept as-is)"
        return 0
    fi

    # Case 3: Target exists WITH markers — replace only the llm-init block
    if ! grep -q "$_start_marker" "$_src"; then
        echo "   ⚠️  Source CLAUDE.md missing llm-init markers; skipping merge"
        return 1
    fi

    if $_dry_run; then
        echo "   ℹ️  [dry-run] Would update llm-init block in existing CLAUDE.md (repo sections preserved)"
        return 0
    fi

    # Line-number-based extraction (portable: macOS + Linux)
    local _tgt_start _tgt_end _src_start _src_end
    _tgt_start=$(grep -n "$_start_marker" "$_tgt" | head -1 | cut -d: -f1)
    _tgt_end=$(grep -n "$_end_marker"   "$_tgt" | head -1 | cut -d: -f1)
    _src_start=$(grep -n "$_start_marker" "$_src" | head -1 | cut -d: -f1)
    _src_end=$(grep -n "$_end_marker"   "$_src" | head -1 | cut -d: -f1)

    # The ── ruler line before start marker and after end marker belong to the block
    local _tgt_block_start=$(( _tgt_start - 1 ))
    local _tgt_block_end=$(( _tgt_end + 1 ))
    local _src_block_start=$(( _src_start - 1 ))
    local _src_block_end=$(( _src_end + 1 ))

    local _tmpfile
    _tmpfile="$(mktemp "${_tgt}.merge.XXXXXX")"

    {
        head -n $(( _tgt_block_start - 1 )) "$_tgt"
        sed -n "${_src_block_start},${_src_block_end}p" "$_src"
        tail -n +$(( _tgt_block_end + 1 )) "$_tgt"
    } > "$_tmpfile"

    \mv -f "$_tmpfile" "$_tgt"
    echo "   ✅ CLAUDE.md updated (llm-init block refreshed, repo-specific sections preserved)"
}

# ─────────────────────────────────────────────────────────────────────────────
# _llm_init_ensure_production_gate_marker <dry_run>
#
# Creates .impact-analysis-required at the repo root (cwd — llm-init has
# already cd'd into target_dir by this point) if, and only if, the current
# repo's git remote matches an entry in PRODUCTION_GATE_REMOTES. Matching is
# by normalized remote identity ("owner/repo"), not local path, since the
# same repo is checked out at different paths on different hosts.
#
# Idempotent: no-op if the marker already exists. Never removes the marker,
# and never touches it in a repo that isn't in the allowlist — a marker
# placed there manually for other reasons is left alone.
# ─────────────────────────────────────────────────────────────────────────────
_llm_init_ensure_production_gate_marker() {
    local _dry_run="$1"

    local _remote_url
    _remote_url="$(git config --get remote.origin.url 2>/dev/null || echo "")"
    [ -n "$_remote_url" ] || return 0

    local _remote_id="$_remote_url"
    _remote_id="${_remote_id%.git}"
    _remote_id="${_remote_id#git@github.com:}"
    _remote_id="${_remote_id#https://github.com/}"
    _remote_id="${_remote_id#http://github.com/}"

    local _match=false _candidate
    for _candidate in "${PRODUCTION_GATE_REMOTES[@]}"; do
        if [ "$_remote_id" = "$_candidate" ]; then
            _match=true
            break
        fi
    done
    $_match || return 0

    if [ -f ".impact-analysis-required" ]; then
        echo "   📌 .impact-analysis-required already present (impact-analysis push gate active)"
        return 0
    fi

    if $_dry_run; then
        echo "   🔍 [dry-run] Would create .impact-analysis-required (repo '$_remote_id' is in PRODUCTION_GATE_REMOTES)"
        return 0
    fi

    cat > ".impact-analysis-required" <<'MARKER'
# This repo requires an impact-analysis artifact (.impact-analysis/<branch>.md)
# before any `git push` or `gh pr create` will be allowed through Claude Code.
# Auto-managed by llm-init.sh for repos in PRODUCTION_GATE_REMOTES — do not
# delete by hand if you want the gate to stay off after the next sync;
# instead remove the repo from that list in llm-init.sh.
MARKER
    echo "   ✅ .impact-analysis-required created (repo '$_remote_id' is in PRODUCTION_GATE_REMOTES — impact-analysis push gate now active)"
}

# ─────────────────────────────────────────────────────────────────────────────
# _llm_init_skill_allowed <skill_name> <profile> <llm_settings_src>
#
# Returns 0 (true) if the skill should be deployed for the given profile.
# profile "all" always returns 0. Other profiles check the corresponding
# .llm_settings/skill-profiles/<profile>.txt file (lines starting with #
# are comments and are ignored).
# ─────────────────────────────────────────────────────────────────────────────
_llm_init_skill_allowed() {
    local _skill="$1"
    local _profile="$2"
    local _src="$3"
    [ "$_profile" = "all" ] && return 0
    local _pfile="$_src/skill-profiles/${_profile}.txt"
    [ -f "$_pfile" ] || return 0  # profile file missing — allow all (safe fallback)
    grep -qxF "$_skill" "$_pfile" && return 0
    return 1
}

llm-init() {
    # ── Argument Parsing ───────────────────────────────────────────
    local dry_run=false target_dir="."
    local keep_existing_mcp=false
    local -a mcp_servers=()
    local skill_profile="all"
    local tools_arg=""
    _LLM_INIT_TOOLS=" $_LLM_INIT_ALL_TOOLS "   # reset: llm-init may run several times in one shell
    local env_store=""
    # ── Subcommand dispatch (must precede flag parsing — the catch-all
    #    below would otherwise swallow 'doctor' as a target directory) ──
    if [[ "${1:-}" == "doctor" ]]; then
        shift
        local _doc_mode="" _doc_dry=false _doc_target="."
        while [[ $# -gt 0 ]]; do
            case "$1" in
                --gemini)     _doc_mode=gemini; shift ;;
                --agy)        _doc_mode=agy; shift ;;
                --dry-run|-n) _doc_dry=true; shift ;;
                *)            _doc_target="$1"; shift ;;
            esac
        done
        case "$_doc_mode" in
            gemini) _llm_init_doctor_gemini "$_doc_dry" "$_doc_target"; return $? ;;
            agy)    _llm_init_doctor_agy "$_doc_target"; return $? ;;   # always read-only
        esac
        echo "llm-init doctor: specify a mode — currently supported: --gemini, --agy" >&2
        echo "  usage: llm-init doctor --gemini [--dry-run] [target_dir]" >&2
        echo "         llm-init doctor --agy [target_dir]" >&2
        return 2
    fi
    if [[ "${1:-}" == "--shell-bootstrap" ]]; then
        shift
        _llm_init_shell_bootstrap "$@"
        return $?
    fi

    while [[ $# -gt 0 ]]; do
        case "$1" in
            --dry-run|-n) dry_run=true; shift ;;
            --keep) keep_existing_mcp=true; shift ;;
            --mcp)
                shift
                case "${1:-}" in
                    github|github-idallasj|github-fluence|github-agentshroud|\
                    aws|xmind|safari|home-assistant|devonthink|gmail|macuse|twg|\
                    atlassian-fluence|atlassian-agentshroud|atlassian-idallasj)
                        mcp_servers+=("$1") ;;
                    all)
                        # macuse and twg are intentionally excluded — both register/run
                        # globally at user scope (not a per-repo file entry) and must
                        # stay opt-in.
                        mcp_servers+=("github" "github-idallasj" "github-fluence" "github-agentshroud" \
                                      "aws" "xmind" "safari" "home-assistant" "devonthink" "gmail" \
                                      "atlassian-fluence" "atlassian-agentshroud" "atlassian-idallasj") ;;
                    fluence)
                        mcp_servers+=("github-fluence" "atlassian-fluence" "aws") ;;
                    personal)
                        # "all" minus the fluence trio — macuse and twg stay opt-in-only, same as "all".
                        mcp_servers+=("github" "github-idallasj" "github-agentshroud" \
                                      "xmind" "safari" "home-assistant" "devonthink" "gmail" \
                                      "atlassian-agentshroud" "atlassian-idallasj") ;;
                    "")
                        echo "llm-init: --mcp requires a value" >&2
                        echo "          valid: github | github-idallasj | github-fluence | github-agentshroud |" >&2
                        echo "                 aws | xmind | safari | home-assistant | devonthink | gmail | macuse | twg |" >&2
                        echo "                 atlassian-fluence | atlassian-agentshroud | atlassian-idallasj |" >&2
                        echo "                 all | fluence | personal" >&2
                        return 2 ;;
                    *)
                        echo "llm-init: unknown --mcp value: '$1'" >&2
                        echo "          valid: github | github-idallasj | github-fluence | github-agentshroud |" >&2
                        echo "                 aws | xmind | safari | home-assistant | devonthink | gmail | macuse | twg |" >&2
                        echo "                 atlassian-fluence | atlassian-agentshroud | atlassian-idallasj |" >&2
                        echo "                 all | fluence | personal" >&2
                        return 2 ;;
                esac
                shift ;;
            --skills)
                shift
                case "${1:-}" in
                    development|podcast|all)
                        skill_profile="$1" ;;
                    "")
                        echo "llm-init: --skills requires a value" >&2
                        echo "          valid: development | podcast | all" >&2
                        return 2 ;;
                    *)
                        echo "llm-init: unknown --skills value: '$1'" >&2
                        echo "          valid: development | podcast | all" >&2
                        return 2 ;;
                esac
                shift ;;
            --tools)
                shift
                _llm_init_parse_tools "${1:-}" || return 2
                tools_arg="$1"
                shift ;;
            --env)
                shift
                # "." is the target-directory idiom, not a store path — even
                # though it isn't a "--" flag, treat it as absent so it falls
                # through to the positional target_dir handler below instead
                # of being swallowed as env_store (see llm-init --help
                # examples: `--env .` is meant to use the default store).
                if [[ -n "${1:-}" && ! "$1" =~ ^-- && "$1" != "." ]]; then
                    env_store="$1"; shift
                else
                    env_store="$HOME/.llm-secrets"
                fi ;;
            --help|-h)
                echo "Usage: llm-init [options] [target_directory]"
                echo ""
                echo "  --dry-run, -n          Preview changes without modifying anything"
                echo ""
                echo "  --mcp <server>         Select MCP servers to deploy (repeatable)."
                echo "                         Unselected servers are REMOVED from .mcp.json,"
                echo "                         .gemini/settings.json, .codex/config.toml, and"
                echo "                         .github/mcp.json."
                echo "                         Writes .llm_settings/repo-mcp-servers (per-repo)."
                echo "                         Values:"
                echo "                           github                → GitHub MCP (generic/legacy)"
                echo "                           github-idallasj       → github.com/idallasj (personal)"
                echo "                           github-fluence        → github.com/fluenceenergy (work)"
                echo "                           github-agentshroud    → github.com/agentshroud"
                echo "                           aws                   → AWS API MCP (readonly, uvx)"
                echo "                           xmind                 → XMind mind-map MCP (npx)"
                echo "                           safari                → Safari browser automation MCP"
                echo "                           home-assistant        → Home Assistant MCP (SSE)"
                echo "                           devonthink            → DEVONthink MCP (HTTP bridge)"
                echo "                           gmail                 → Gmail MCP, one gmail-<alias> entry per account in"
                echo "                                                   ~/.config/llm-settings/gmail-accounts (send off by default)"
                echo "                           macuse                → macuse native-app MCP (macOS only)"
                echo "                           twg                   → Atlassian Teamwork Graph CLI status check"
                echo "                           atlassian-fluence     → fluenceenergy.atlassian.net"
                echo "                           atlassian-agentshroud → agentshroudai.atlassian.net"
                echo "                           atlassian-idallasj    → idallasj.atlassian.net (OAuth)"
                echo "                           all                   → all of the above EXCEPT macuse and twg"
                echo "                           fluence               → github-fluence + atlassian-fluence + aws"
                echo "                           personal              → all EXCEPT macuse, twg, and the fluence trio"
                echo "                         Examples:"
                echo "                           llm-init --mcp github-fluence --mcp atlassian-fluence ."
                echo "                           llm-init --mcp github-idallasj --mcp home-assistant ."
                echo "                           llm-init --mcp github --mcp safari --mcp home-assistant ."
                echo "                           llm-init --mcp all ."
                echo "                           llm-init --mcp fluence ."
                echo "                           llm-init --mcp personal ."
                echo "                           llm-init --mcp macuse ."
                echo "                           llm-init --mcp twg ."
                echo "                         Every --mcp run REPLACES the existing selection (only the"
                echo "                         servers given this run remain) — add --keep to ADD to the"
                echo "                         existing selection instead:"
                echo "                           llm-init --mcp home-assistant --keep ."
                echo "                         Omit --mcp entirely to preserve existing selection unchanged;"
                echo "                         if no selection file exists, all servers are kept (backward"
                echo "                         compat)."
                echo ""
                echo "                         macuse and twg are different from every other value: neither"
                echo "                         has a per-repo .mcp.json entry. macuse runs an idempotent"
                echo "                         'claude/gemini/codex mcp add --scope user ...' once per"
                echo "                         machine (global registration, not scoped to this repo). twg"
                echo "                         is not an MCP server at all — it's a separately-installed"
                echo "                         CLI+skills tool (see .llm_settings/docs/MCP_README.md); this"
                echo "                         flag only runs 'twg doctor' to report its status."
                echo ""
                echo "                         Any selection that includes Fluence or personal servers"
                echo "                         (all | fluence | personal) also runs read-only auth checks"
                echo "                         (never a login): twg must be logged in as the account matching"
                echo "                         the repo scope (Fluence and personal Atlassian accounts are"
                echo "                         never mixed; override domain with LLM_INIT_FLUENCE_EMAIL_DOMAIN),"
                echo "                         and sf org 'fluence' (SFQ_ORG / SFQ_INSTANCE_URL) must be"
                echo "                         connected — skipped for personal. Mismatches warn and print"
                echo "                         the re-auth command."
                echo ""
                echo "  --skills <profile>     Select which skills to deploy (default: all):"
                echo "                           all         → all skills — Claude, Gemini, Codex"
                echo "                           development → engineering repos incl. security-focused"
                echo "                           podcast     → development + podcast pipeline skills"
                echo "                         Profile definitions: .llm_settings/skill-profiles/<profile>.txt"
                echo "                         To restore skills: re-run llm-init --skills <profile> ."
                echo ""
                echo "  --tools <list>         Comma-separated CLIs to deploy (default: all):"
                echo "                           claude codex gemini copilot opencode crush agy grok pi omp cursor"
                echo "                         Claude is always deployed (it feeds the others). Per tool:"
                echo "                           opencode → opencode.json + .opencode/agents + .agents/skills"
                echo "                           crush    → .crush.json + .agents/skills"
                echo "                           agy      → .agents/{skills,agents,plugins/llm-settings} (Antigravity)"
                echo "                           grok     → .grok/config.toml (reads .claude/skills + agents natively)"
                echo "                           pi       → .pi/mcp.json + .agents/skills"
                echo "                           omp      → .omp/{mcp.json,agents} + .agents/skills (Oh My Pi)"
                echo "                           cursor   → .cursor/{mcp.json,agents} + .agents/skills (cursor-agent)"
                echo "                         MCP files are derived from the filtered .mcp.json, so --mcp"
                echo "                         applies to every tool. Persisted in .llm_settings/repo-tools"
                echo "                         (sticky when --tools is omitted); other tools' files are never"
                echo "                         deleted when deselected."
                echo ""
                echo "  --env [PATH]           Deploy .env files from local secrets store to target repo."
                echo "                         Always overwrites existing .env files (store is authoritative)."
                echo "                         Scoped to selected --mcp servers; if no --mcp given, deploys all."
                echo "                         Missing store entries are skipped (non-fatal)."
                echo "                         Default store: ~/.llm-secrets"
                echo "                         Run setup-env-store.sh first to create the store."
                echo "                         Example: llm-init --env ."
                echo "                                  llm-init --mcp github-idallasj --env ."
                echo "                                  llm-init --env ~/my-secrets ."
                echo ""
                echo "  doctor --gemini        Repair + validate an already-deployed repo's Gemini"
                echo "                         config (agents frontmatter, settings.json, MCP servers)."
                echo "                         Idempotent; takes a timestamped backup before changes."
                echo "                         Usage: llm-init doctor --gemini [--dry-run] [target_dir]"
                echo ""
                echo "  doctor --agy           Read-only diagnostics for agy (Antigravity) not seeing"
                echo "                         this repo's skills/agents: binary + version, trusted"
                echo "                         workspace, .agents/ layout, frontmatter, 24000-byte"
                echo "                         SKILL.md limit, drift vs llm_settings, plugin validate."
                echo "                         Ends with a fingerprint to diff between hosts."
                echo "                         Usage: llm-init doctor --agy [target_dir]"
                echo ""
                echo "  --shell-bootstrap      OPT-IN user-level setup: installs the gemini/vertex"
                echo "                         wrapper snippet for YOUR shell (~/.gemini-vertex.zsh"
                echo "                         or .bash) and adds a guarded source line to your rc."
                echo "                         Optional: --theme <name> sets ui.theme in"
                echo "                         ~/.gemini/settings.json (user scope only — never repo)."
                echo ""
                echo "  --help,    -h          Show this help message"
                echo "  target_directory       Directory to deploy to (default: .)"
                echo ""
                echo "  Note: --mcp filtering of JSON files requires jq."
                echo "        TOML filtering (.codex/config.toml) uses awk (always available)."
                return 0 ;;
            *) target_dir="$1"; shift ;;
        esac
    done

    local rsync_dry=""
    $dry_run && rsync_dry="--dry-run"
    $dry_run && echo "⚠️  DRY RUN MODE — no files will be modified" && echo ""

    # ── Platform Detection ─────────────────────────────────────────
    local os_type
    os_type="$(uname -s)"

    local pkg_manager=""
    case "$os_type" in
        Darwin)
            command -v brew &>/dev/null && pkg_manager="brew" ;;
        Linux)
            if   command -v apt-get &>/dev/null; then pkg_manager="apt"
            elif command -v dnf     &>/dev/null; then pkg_manager="dnf"
            elif command -v yum     &>/dev/null; then pkg_manager="yum"
            elif command -v pacman  &>/dev/null; then pkg_manager="pacman"
            elif command -v brew    &>/dev/null; then pkg_manager="brew"
            fi ;;
    esac

    # ── Tool Path Resolution ───────────────────────────────────────
    local uvx_path="" npx_path=""
    command -v uvx &>/dev/null && uvx_path="$(command -v uvx)"
    # Linux fallback: pipx/uvx commonly installs to ~/.local/bin which may not be in PATH
    if [ -z "$uvx_path" ] && [ -x "$HOME/.local/bin/uvx" ]; then
        uvx_path="$HOME/.local/bin/uvx"
    fi
    command -v npx &>/dev/null && npx_path="$(command -v npx)"

    # Build platform-appropriate PATH for MCP env blocks
    local mcp_path="/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
    case "$os_type" in
        Darwin) [ -d "/opt/homebrew/bin" ] && mcp_path="/opt/homebrew/bin:$mcp_path" ;;
        Linux)
            [ -d "$HOME/.local/bin" ] && mcp_path="$HOME/.local/bin:$mcp_path"
            [ -d "$HOME/.cargo/bin" ] && mcp_path="$HOME/.cargo/bin:$mcp_path" ;;
    esac

    # ── Source Directory Resolution ────────────────────────────────
    local source_dir=""

    # 1. Explicit env var override
    if [ -n "${LLM_SETTINGS_DIR:-}" ] && [ -d "$LLM_SETTINGS_DIR" ]; then
        source_dir="$LLM_SETTINGS_DIR"
    fi

    # 2. Script self-location (resolve BASH_SOURCE[0] up two levels)
    if [ -z "$source_dir" ] && [ -n "${BASH_SOURCE[0]:-}" ]; then
        local _script="${BASH_SOURCE[0]}"
        # Resolve symlinks cross-platform
        if [ "$os_type" = "Darwin" ]; then
            # macOS: no readlink -f; manual loop
            local _link
            while [ -L "$_script" ]; do
                _link="$(readlink "$_script")"
                case "$_link" in
                    /*) _script="$_link" ;;
                    *)  _script="$(dirname "$_script")/$_link" ;;
                esac
            done
        else
            _script="$(readlink -f "$_script" 2>/dev/null || echo "$_script")"
        fi
        local _candidate
        _candidate="$(cd "$(dirname "$_script")/../.." 2>/dev/null && pwd)"
        # Guard: if the candidate equals the current working directory, it is likely
        # a deployed target repo (sourced via relative path), not the llm_settings
        # source.  Skip BASH_SOURCE resolution and fall through to well-known paths.
        local _cwd
        _cwd="$(pwd)"
        if [ "$_candidate" != "$_cwd" ] && \
           [ -d "${_candidate}/.claude" ] && \
           { [ -d "${_candidate}/.llm_settings" ] || [ -d "${_candidate}/llm_settings" ]; }; then
            source_dir="$_candidate"
        fi
    fi

    # 3. Well-known paths
    if [ -z "$source_dir" ]; then
        local _wk
        for _wk in \
            "$HOME/Development/llm_settings" \
            "$HOME/Development/LLM_Settings" \
            "$HOME/dev/llm_settings" \
            "$HOME/repos/llm_settings"; do
            if [ -d "${_wk}/.claude" ] && { [ -d "${_wk}/.llm_settings" ] || [ -d "${_wk}/llm_settings" ]; }; then
                source_dir="$_wk"
                break
            fi
        done
    fi

    # 4. Fail with clear message
    if [ -z "$source_dir" ]; then
        echo "❌ Error: Cannot locate llm_settings source directory."
        echo "   Set the LLM_SETTINGS_DIR environment variable to the repo root."
        echo "   Example: export LLM_SETTINGS_DIR=\$HOME/Development/llm_settings"
        return 1
    fi

    # Resolve canonical LLM settings source directory (.llm_settings preferred, llm_settings legacy fallback)
    local llm_settings_src=""
    if [ -d "$source_dir/.llm_settings" ]; then
        llm_settings_src="$source_dir/.llm_settings"
    elif [ -d "$source_dir/llm_settings" ]; then
        llm_settings_src="$source_dir/llm_settings"
    fi

    # ── Install Hint Helper ────────────────────────────────────────
    # Called from within llm-init(); sees $pkg_manager via bash dynamic scoping.
    _install_hint() {
        local tool="$1"
        case "$tool" in
            uv)
                case "$pkg_manager" in
                    brew) echo "brew install uv" ;;
                    *)    echo "curl -LsSf https://astral.sh/uv/install.sh | sh" ;;
                esac ;;
            gh)
                case "$pkg_manager" in
                    brew)    echo "brew install gh" ;;
                    apt)     echo "sudo apt install gh" ;;
                    dnf|yum) echo "sudo dnf install gh" ;;
                    *)       echo "https://cli.github.com" ;;
                esac ;;
            awscli)
                case "$pkg_manager" in
                    brew)    echo "brew install awscli" ;;
                    apt)     echo "sudo apt install awscli" ;;
                    dnf|yum) echo "sudo dnf install awscli" ;;
                    *)       echo "https://aws.amazon.com/cli/" ;;
                esac ;;
            gitleaks)
                case "$pkg_manager" in
                    brew) echo "brew install gitleaks" ;;
                    *)    echo "go install github.com/gitleaks/gitleaks/v8@latest  (or https://github.com/gitleaks/gitleaks#installing)" ;;
                esac ;;
            git-secrets)
                case "$pkg_manager" in
                    brew) echo "brew install git-secrets" ;;
                    *)    echo "https://github.com/awslabs/git-secrets#installing-git-secrets" ;;
                esac ;;
            direnv)
                case "$pkg_manager" in
                    brew)    echo "brew install direnv" ;;
                    apt)     echo "sudo apt install direnv" ;;
                    dnf|yum) echo "sudo dnf install direnv" ;;
                    *)       echo "https://direnv.net/docs/installation.html" ;;
                esac ;;
            rsync)
                case "$pkg_manager" in
                    brew)    echo "brew install rsync" ;;
                    apt)     echo "sudo apt-get install -y rsync" ;;
                    dnf|yum) echo "sudo dnf install rsync" ;;
                    pacman)  echo "sudo pacman -S --noconfirm rsync" ;;
                    *)       echo "install rsync via your system package manager" ;;
                esac ;;
        esac
    }

    echo "🚀 Deploying LLM AI tool configurations..."
    echo "   Platform: $os_type (${pkg_manager:-no package manager detected})"
    echo "   uvx:      ${uvx_path:-not found}"
    echo "   Source:   $source_dir"
    echo "   Target:   $target_dir"
    echo "   Mode:     Synchronize (add new, update existing, remove obsolete)"
    echo ""

    # Verify source directory exists
    if [ ! -d "$source_dir" ]; then
        echo "❌ Error: Source directory not found: $source_dir"
        return 1
    fi

    # Create target directory if it doesn't exist
    if [ ! -d "$target_dir" ]; then
        echo "❌ Error: Target directory not found: $target_dir"
        return 1
    fi

    # Check for rsync (required for synchronization)
    if ! command -v rsync &> /dev/null; then
        echo "❌ Error: rsync not found (required for synchronization)"
        echo "   Install with: $(_install_hint rsync)"
        return 1
    fi

    # Navigate to target directory
    cd "$target_dir" || return 1

    # Migration: Clean up old deployment structure
    echo "🧹 Checking for old deployment structure..."
    local cleaned=false

    # Old files/directories to remove
    local old_items=(
        "github-mcp-server"
        "AI_TOOLS_CONFIGURATION_GUIDE.md"
        "CONFIGURATION_SUMMARY.md"
        "MCP_README.md"
        "MCP_ADDITIONAL_SERVICES.md"
        "GEMINI.md"
        ".llm_env_example"
        "new-skills"
        "llm_settings"
        # Stale nested scope copies — created when llm-init was previously run
        # on the llm_settings repo itself. These must not exist in target repos.
        ".llm_settings/scripts/.claude"
        ".llm_settings/scripts/.gemini"
        ".llm_settings/scripts/.codex"
        ".llm_settings/scripts/.github"
        ".llm_settings/scripts/.mcp.json"
        ".llm_settings/scripts/.llm_settings"
    )

    for item in "${old_items[@]}"; do
        if [ -e "$item" ]; then
            if git ls-files --error-unmatch "$item" >/dev/null 2>&1; then
                echo "   🗑️  Removing tracked: $item"
                $dry_run || git rm -rf "$item" 2>/dev/null
                cleaned=true
            elif [ -d "$item" ]; then
                echo "   🗑️  Removing directory: $item"
                $dry_run || rm -rf "$item"
                cleaned=true
            elif [ -f "$item" ]; then
                echo "   🗑️  Removing file: $item"
                $dry_run || rm -f "$item"
                cleaned=true
            fi
        fi
    done

    # Glob-safe cleanup for new-skills-*.tgz — use find to avoid zsh "no matches found" error
    while IFS= read -r _tgz; do
        echo "   🗑️  Removing file: $_tgz"
        $dry_run || rm -f "$_tgz"
        cleaned=true
    done < <(find "$target_dir" -maxdepth 1 -name 'new-skills-*.tgz' -type f 2>/dev/null)

    if [ "$cleaned" = true ]; then
        echo "   ✅ Old deployment cleaned up"
    else
        echo "   ✅ No old deployment found (clean target)"
    fi
    echo ""

    # Check prerequisites
    echo "📋 Checking prerequisites..."
    echo ""

    # Check for uvx (required for AWS MCP)
    if [ -n "$uvx_path" ]; then
        echo "   ✅ uvx found at $uvx_path"
    else
        echo "   ⚠️  uvx not found - AWS MCP will not work"
        echo "      Install with: $(_install_hint uv)"
    fi

    # Check for gh CLI (helpful for GitHub MCP)
    if command -v gh &> /dev/null; then
        echo "   ✅ gh CLI found"
    else
        echo "   ⚠️  gh CLI not found - GitHub MCP token setup may be manual"
        echo "      Install with: $(_install_hint gh)"
    fi

    # Check for AWS CLI
    if command -v aws &> /dev/null; then
        echo "   ✅ aws CLI found"
    else
        echo "   ⚠️  aws CLI not found - AWS MCP requires AWS credentials"
        echo "      Install with: $(_install_hint awscli)"
    fi

    # Check for git security tools
    if command -v gitleaks &> /dev/null; then
        echo "   ✅ gitleaks found"
    else
        echo "   ⚠️  gitleaks not found"
        echo "      Install with: $(_install_hint gitleaks)"
    fi

    if command -v git-secrets &> /dev/null; then
        echo "   ✅ git-secrets found"
    else
        echo "   ⚠️  git-secrets not found"
        echo "      Install with: $(_install_hint git-secrets)"
    fi

    # Check for pre-commit framework
    if command -v pre-commit &> /dev/null; then
        echo "   ✅ pre-commit found"
    else
        echo "   ⚠️  pre-commit not found - Install with: pip install pre-commit"
        echo "      (Will fall back to manual git hooks)"
    fi

    # Check for direnv
    if command -v direnv &> /dev/null; then
        echo "   ✅ direnv found"
    else
        echo "   ⚠️  direnv not found"
        echo "      Install with: $(_install_hint direnv)"
        echo "      (Recommended for secure environment variables)"
    fi
    echo ""

    # ── MCP Server Selection Marker File ──────────────────────────
    echo "🔌 MCP Server Selection"
    local _mcp_marker_file=".llm_settings/repo-mcp-servers"
    if [ ${#mcp_servers[@]} -gt 0 ]; then
        # --keep: seed the new selection with whatever is already on disk, so this
        # run ADDS to it instead of replacing it. Without --keep (default), only
        # this run's servers survive — matches every other CLI's normal semantics.
        local -a _mcp_seed=()
        if $keep_existing_mcp && [ -f "$_mcp_marker_file" ]; then
            while IFS= read -r _line; do
                _line="${_line%%#*}"
                _line="${_line//[[:space:]]/}"
                [ -z "$_line" ] && continue
                _mcp_seed+=("$_line")
            done < "$_mcp_marker_file"
        fi
        # Deduplicate while preserving order (seed first, then this run's selection)
        local -a _mcp_deduped=()
        local _mcp_seen=""
        for _ms in ${_mcp_seed[@]+"${_mcp_seed[@]}"} "${mcp_servers[@]}"; do
            if [[ "$_mcp_seen" != *"|${_ms}|"* ]]; then
                _mcp_deduped+=("$_ms")
                _mcp_seen="${_mcp_seen}|${_ms}|"
            fi
        done
        if ! $dry_run; then
            mkdir -p .llm_settings
            {
                printf '# llm-init MCP server selection — generated %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
                printf '# Values: github | aws | xmind | safari | home-assistant | devonthink | gmail | macuse | twg |\n'
                printf '#         atlassian-fluence | atlassian-agentshroud | atlassian-idallasj |\n'
                printf '#         all | fluence | personal\n'
                printf '# (macuse registers globally per-machine — see _llm_init_ensure_macuse)\n'
                printf '# (twg is not an MCP server — see _llm_init_check_twg)\n'
                printf '# Change with:  llm-init --mcp <server> [--mcp <server>]... [--keep] .\n'
                printf '# --keep adds to the existing selection instead of replacing it.\n'
                printf '%s\n' "${_mcp_deduped[@]}"
            } > "$_mcp_marker_file"
            if $keep_existing_mcp; then
                echo "   📌 Added MCP server(s) (kept existing): ${_mcp_deduped[*]} → $_mcp_marker_file"
            else
                echo "   📌 Set MCP server(s) (replaced existing): ${_mcp_deduped[*]} → $_mcp_marker_file"
            fi
        else
            echo "   ℹ️  [dry-run] Would write $_mcp_marker_file: ${_mcp_deduped[*]}"
        fi
    elif [ -f "$_mcp_marker_file" ]; then
        local _current_mcp
        _current_mcp="$(grep -v '^#' "$_mcp_marker_file" | tr -d '[:space:]' | tr '\n' ' ' | sed 's/ $//')"
        echo "   📌 Preserving existing MCP selection: ${_current_mcp:-all}"
    else
        echo "   📌 No --mcp flag — all servers kept (backward compat)"
    fi
    echo ""

    # ── Tool Selection Marker File (--tools) ──────────────────────
    local _tools_marker_file=".llm_settings/repo-tools"
    if [ -n "$tools_arg" ]; then
        if ! $dry_run; then
            mkdir -p .llm_settings
            {
                printf '# llm-init tool selection — generated %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
                printf '# Values: all | claude | codex | gemini | copilot | opencode | crush | agy | grok | pi | omp | cursor\n'
                printf '# Claude is always deployed. Change with:  llm-init --tools a,b,c .\n'
                printf '%s\n' "$tools_arg" | tr ',' '\n' | tr -d '[:blank:]' | tr '[:upper:]' '[:lower:]' | grep -v '^$'
            } > "$_tools_marker_file"
        fi
        echo "🧰 Tools: ${_LLM_INIT_TOOLS//  / } (set via --tools)"
    elif [ -f "$_tools_marker_file" ]; then
        local _tools_csv
        _tools_csv="$(grep -v '^#' "$_tools_marker_file" | tr -d '[:blank:]' | grep -v '^$' | tr '\n' ',' | sed 's/,$//')"
        if [ -n "$_tools_csv" ] && _llm_init_parse_tools "$_tools_csv" 2>/dev/null; then
            echo "🧰 Tools: ${_LLM_INIT_TOOLS//  / } (from $_tools_marker_file)"
        else
            _LLM_INIT_TOOLS=" $_LLM_INIT_ALL_TOOLS "
            echo "🧰 Tools: all (unreadable $_tools_marker_file — using default)"
        fi
    else
        if ! $dry_run; then
            mkdir -p .llm_settings
            {
                printf '# llm-init tool selection — generated %s\n' "$(date -u +%Y-%m-%dT%H:%M:%SZ)"
                printf '# Values: all | claude | codex | gemini | copilot | opencode | crush | agy | grok | pi | omp | cursor\n'
                printf '# Claude is always deployed. Change with:  llm-init --tools a,b,c .\n'
                printf 'all\n'
            } > "$_tools_marker_file"
        fi
        echo "🧰 Tools: all (default)"
    fi
    echo ""

    echo "🧪 Testing agents (i- suite)..."
    _llm_init_render_testing_agents "$dry_run" "$source_dir"
    echo ""

    echo "📦 Copying configurations..."
    echo ""

    # 1. Claude Code (PRIMARY Developer)
    echo "1️⃣  Claude Code (PRIMARY)"
    if [ -d "$source_dir/.claude" ]; then
        rsync -a $rsync_dry --delete \
            --exclude='settings.local.json' \
            --exclude='*.local.*' \
            --exclude='.cache/' \
            --exclude='tmp/' \
            --exclude='logs/' \
            --exclude='.credentials.json' \
            --exclude='history.jsonl' \
            --exclude='debug/' \
            --exclude='file-history/' \
            --exclude='paste-cache/' \
            --exclude='session-env/' \
            --exclude='shell-snapshots/' \
            --exclude='stats-cache.json' \
            --exclude='statsig/' \
            --exclude='todos/' \
            --exclude='agents/' \
            --exclude='skills/' \
            --exclude='worktrees/' \
            "$source_dir/.claude/" .claude/
        echo "   ✅ .claude/ synchronized (secrets preserved)"

        # Sync skills from canonical source (.llm_settings/skills/) into .claude/skills/
        if [ -d "$llm_settings_src/skills" ]; then
            # Clean up existing skills directory to remove obsolete skills
            if ! $dry_run && [ -d ".claude/skills" ]; then
                rm -rf .claude/skills/*
            fi

            $dry_run || mkdir -p ".claude/skills"
            _llm_init_skill_map_load "$llm_settings_src"

            local skill_count=0
            for skill_dir in "$llm_settings_src/skills"/*/; do
                local skill_name skill_dest
                skill_name=$(basename "$skill_dir")
                if [ -f "$skill_dir/SKILL.md" ]; then
                    _llm_init_skill_allowed "$skill_name" "$skill_profile" "$llm_settings_src" || continue
                    skill_dest="$(_llm_init_skill_name_for "$skill_name")"
                    if ! $dry_run; then
                        # rsync entire directory so skills with subdirectories (e.g. graphify/references/) are fully deployed
                        rsync -a "$skill_dir" ".claude/skills/$skill_dest/"
                        _llm_init_normalize_skill_name ".claude/skills/$skill_dest/SKILL.md" "$skill_dest"
                    fi
                    ((skill_count++))
                fi
            done
            echo "   ✅ .claude/skills/ synchronized ($skill_count skills [$skill_profile profile])"
        fi

        # Sync agents from canonical source (.llm_settings/agents/) into .claude/agents/
        if [ -d "$llm_settings_src/agents" ]; then
            $dry_run || rm -rf .claude/agents
            $dry_run || mkdir -p .claude/agents
            local agent_count=0
            for agent_file in "$llm_settings_src/agents"/*.md; do
                [ -f "$agent_file" ] || continue
                $dry_run || cp "$agent_file" ".claude/agents/$(basename "$agent_file")"
                ((agent_count++))
            done
            echo "   ✅ .claude/agents/ synchronized ($agent_count agents from .llm_settings/agents/)"
        fi

        # Deploy ORCHESTRATOR.md
        if [ -f "$source_dir/.claude/ORCHESTRATOR.md" ]; then
            $dry_run || cp "$source_dir/.claude/ORCHESTRATOR.md" ".claude/ORCHESTRATOR.md"
            echo "   ✅ .claude/ORCHESTRATOR.md deployed"
        fi
    else
        echo "   ⚠️  .claude/ directory not found in source"
    fi

    if [ -f "$source_dir/CLAUDE.md" ]; then
        _llm_init_merge_claude_md "$source_dir/CLAUDE.md" "./CLAUDE.md" "$dry_run"
    else
        echo "   ⚠️  CLAUDE.md not found in source"
    fi

    _llm_init_ensure_production_gate_marker "$dry_run"

    echo ""

    # 2. Gemini CLI (SECONDARY Agent)
    echo "2️⃣  Gemini CLI (SECONDARY)"
    if ! _llm_init_tool_enabled gemini; then
        echo "   ⏭️  Skipped (not in --tools)"
    elif [ -d "$llm_settings_src/.gemini" ]; then
        rsync -a $rsync_dry --delete \
            --exclude='settings.local.json' \
            --exclude='*.local.*' \
            --exclude='.cache/' \
            --exclude='tmp/' \
            --exclude='logs/' \
            --exclude='agents/' \
            --exclude='commands/' \
            "$llm_settings_src/.gemini/" .gemini/
        # Patch hardcoded macOS paths after sync (skip in dry-run)
        if ! $dry_run && [ -f ".gemini/settings.json" ] && [ -n "$uvx_path" ]; then
            sed -i.bak \
                -e "s|/opt/homebrew/bin/uvx|$uvx_path|g" \
                -e "s|/opt/homebrew/bin/npx|${npx_path:-/opt/homebrew/bin/npx}|g" \
                -e "s|/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin|$mcp_path|g" \
                .gemini/settings.json
            # Validate JSON after sed patching
            if command -v jq >/dev/null 2>&1 && ! jq empty .gemini/settings.json 2>/dev/null; then
                echo "   ❌ Path patching corrupted .gemini/settings.json — restoring backup" >&2
                mv .gemini/settings.json.bak .gemini/settings.json
            else
                rm -f .gemini/settings.json.bak
            fi
        fi
        # Sync agents from canonical source (.llm_settings/skills/) into .gemini/agents/
        # All files are converted to Gemini format: name+description frontmatter only,
        # digit-prefixed filenames rewritten, README.md excluded.
        if [ -d "$llm_settings_src/skills" ]; then
            $dry_run || rm -rf .gemini/agents
            $dry_run || mkdir -p .gemini/agents
            $dry_run || rm -rf .gemini/commands
            $dry_run || mkdir -p .gemini/commands
            $dry_run || rm -rf .gemini/agent-prompts
            local gemini_skill_count=0
            for skill_dir in "$llm_settings_src/skills"/*/; do
                local skill_name
                skill_name=$(basename "$skill_dir")
                if [ -f "$skill_dir/SKILL.md" ]; then
                    _llm_init_skill_allowed "$skill_name" "$skill_profile" "$llm_settings_src" || continue
                    # Reference material never deploys as an invocable agent —
                    # it goes to .gemini/agent-prompts/ verbatim instead
                    if _llm_init_gemini_excluded "$skill_name"; then
                        if ! $dry_run; then
                            mkdir -p .gemini/agent-prompts
                            cp "$skill_dir/SKILL.md" ".gemini/agent-prompts/${skill_name}.md"
                        fi
                        continue
                    fi
                    $dry_run || _llm_init_convert_for_gemini "$skill_dir/SKILL.md" ".gemini/agents" "$skill_name"
                    $dry_run || _llm_init_convert_for_gemini_command "$skill_dir/SKILL.md" ".gemini/commands" "$skill_name"
                    ((gemini_skill_count++))
                fi
            done
            # Also sync agents from .llm_settings/agents/ into .gemini/agents/ + .gemini/commands/
            if [ -d "$llm_settings_src/agents" ]; then
                for agent_file in "$llm_settings_src/agents"/*.md; do
                    [ -f "$agent_file" ] || continue
                    if _llm_init_gemini_excluded "$(basename "${agent_file%.md}")"; then
                        if ! $dry_run; then
                            mkdir -p .gemini/agent-prompts
                            cp "$agent_file" ".gemini/agent-prompts/$(basename "$agent_file")"
                        fi
                        continue
                    fi
                    $dry_run || _llm_init_convert_for_gemini "$agent_file" ".gemini/agents"
                    $dry_run || _llm_init_convert_for_gemini_command "$agent_file" ".gemini/commands"
                done
            fi
            # Also sync agents from MCP server templates (e.g. github/.gemini/agents/)
            if [ -d "$llm_settings_src/mcp-servers/github/.gemini/agents" ]; then
                for agent_file in "$llm_settings_src/mcp-servers/github/.gemini/agents"/*.md; do
                    [ -f "$agent_file" ] || continue
                    [[ "$(basename "$agent_file")" == "README.md" ]] && continue
                    $dry_run || _llm_init_convert_for_gemini "$agent_file" ".gemini/agents"
                    $dry_run || _llm_init_convert_for_gemini_command "$agent_file" ".gemini/commands"
                done
            fi
            echo "   ✅ .gemini/ synchronized ($gemini_skill_count skills [$skill_profile profile] + agents + commands, MCP configured)"
        else
            local gemini_agents
            gemini_agents=$(ls .gemini/agents/*.md 2>/dev/null | wc -l | tr -d ' ')
            echo "   ✅ .gemini/ synchronized ($gemini_agents agents, MCP configured)"
        fi
    else
        echo "   ⚠️  .gemini/ directory not found in source"
    fi
    echo ""

    # 3. Codex CLI (TERTIARY Agent)
    echo "3️⃣  Codex CLI (TERTIARY)"
    if ! _llm_init_tool_enabled codex; then
        echo "   ⏭️  Skipped (not in --tools)"
    elif [ -d "$llm_settings_src/.codex" ]; then
        rsync -a $rsync_dry --delete \
            --exclude='config.local.toml' \
            --exclude='*.local.*' \
            --exclude='.cache/' \
            --exclude='tmp/' \
            --exclude='logs/' \
            --exclude='agents/' \
            "$llm_settings_src/.codex/" .codex/
        # Patch hardcoded macOS paths after sync (skip in dry-run)
        if ! $dry_run && [ -f ".codex/config.toml" ] && [ -n "$uvx_path" ]; then
            sed -i.bak \
                -e "s|/opt/homebrew/bin/uvx|$uvx_path|g" \
                -e "s|/opt/homebrew/bin/npx|${npx_path:-/opt/homebrew/bin/npx}|g" \
                .codex/config.toml
            rm -f .codex/config.toml.bak
        fi
        # Sync agents from canonical source (.llm_settings/skills/) into .codex/agents/
        if [ -d "$llm_settings_src/skills" ]; then
            $dry_run || rm -rf .codex/agents
            $dry_run || mkdir -p .codex/agents
            local codex_skill_count=0
            for skill_dir in "$llm_settings_src/skills"/*/; do
                local skill_name
                skill_name=$(basename "$skill_dir")
                if [ -f "$skill_dir/SKILL.md" ]; then
                    _llm_init_skill_allowed "$skill_name" "$skill_profile" "$llm_settings_src" || continue
                    $dry_run || cp "$skill_dir/SKILL.md" ".codex/agents/$skill_name.md"
                    ((codex_skill_count++))
                fi
            done
            # Also sync agents from .llm_settings/agents/ into .codex/agents/
            if [ -d "$llm_settings_src/agents" ]; then
                for agent_file in "$llm_settings_src/agents"/*.md; do
                    [ -f "$agent_file" ] || continue
                    $dry_run || cp "$agent_file" ".codex/agents/$(basename "$agent_file")"
                done
            fi
            echo "   ✅ .codex/ synchronized ($codex_skill_count skills [$skill_profile profile] + agents, MCP configured)"
        else
            local codex_agents
            codex_agents=$(ls .codex/agents/*.md 2>/dev/null | wc -l | tr -d ' ')
            echo "   ✅ .codex/ synchronized ($codex_agents agents, MCP configured)"
        fi
    else
        echo "   ⚠️  .codex/ directory not found in source"
    fi

    if [ -f "$source_dir/AGENTS.md" ]; then
        rsync -a $rsync_dry "$source_dir/AGENTS.md" .
        echo "   ✅ AGENTS.md synchronized"
    else
        echo "   ⚠️  AGENTS.md not found in source"
    fi

    # Deploy ORCHESTRATOR.md to .gemini/, .codex/, and .github/ for workflow parity
    if [ -f "$source_dir/.claude/ORCHESTRATOR.md" ]; then
        if _llm_init_tool_enabled gemini; then
            $dry_run || cp "$source_dir/.claude/ORCHESTRATOR.md" ".gemini/ORCHESTRATOR.md"
            echo "   ✅ .gemini/ORCHESTRATOR.md deployed"
        fi
        if _llm_init_tool_enabled codex; then
            $dry_run || cp "$source_dir/.claude/ORCHESTRATOR.md" ".codex/ORCHESTRATOR.md"
            echo "   ✅ .codex/ORCHESTRATOR.md deployed"
        fi
        if _llm_init_tool_enabled copilot; then
            $dry_run || mkdir -p .github
            $dry_run || cp "$source_dir/.claude/ORCHESTRATOR.md" ".github/ORCHESTRATOR.md"
            echo "   ✅ .github/ORCHESTRATOR.md deployed"
        fi
    fi
    echo ""

    # 4. GitHub Copilot CLI (QUATERNARY Agent)
    echo "4️⃣  GitHub Copilot CLI (QUATERNARY)"
    if ! _llm_init_tool_enabled copilot; then
        echo "   ⏭️  Skipped (not in --tools)"
    elif [ -d "$source_dir/.github" ]; then
        $dry_run || mkdir -p .github

        if [ -f "$source_dir/.github/COPILOT_CLI_SETUP.md" ]; then
            rsync -a $rsync_dry "$source_dir/.github/COPILOT_CLI_SETUP.md" .github/
            echo "   ✅ .github/COPILOT_CLI_SETUP.md synchronized"
        fi

        if [ -f "$source_dir/.github/copilot-config.json.example" ]; then
            rsync -a $rsync_dry "$source_dir/.github/copilot-config.json.example" .github/
            echo "   ✅ .github/copilot-config.json.example synchronized"
        fi

        # Sync + patch .github/mcp.json (repo-committed, auto-loaded per Copilot CLI's
        # own MCP config precedence — same mcpServers JSON shape as .mcp.json).
        if [ -n "$llm_settings_src" ] && [ -f "$llm_settings_src/.github/mcp.json" ]; then
            $dry_run || mkdir -p .github
            rsync -a $rsync_dry "$llm_settings_src/.github/mcp.json" .github/
            if ! $dry_run && [ -f ".github/mcp.json" ] && [ -n "$uvx_path" ]; then
                sed -i.bak \
                    -e "s|/opt/homebrew/bin/uvx|$uvx_path|g" \
                    -e "s|/opt/homebrew/bin/npx|${npx_path:-/opt/homebrew/bin/npx}|g" \
                    -e "s|/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin|$mcp_path|g" \
                    .github/mcp.json
                if command -v jq >/dev/null 2>&1 && ! jq empty .github/mcp.json 2>/dev/null; then
                    echo "   ❌ Path patching corrupted .github/mcp.json — restoring backup" >&2
                    mv .github/mcp.json.bak .github/mcp.json
                else
                    rm -f .github/mcp.json.bak
                fi
            fi
            echo "   ✅ .github/mcp.json synchronized"
        else
            echo "   ⚠️  .github/mcp.json not found in source"
        fi

        # copilot-instructions.md — same smart merge CLAUDE.md gets (full deploy if
        # absent, preserve if unmarked, replace-block if marked).
        if [ -f "$source_dir/CLAUDE.md" ]; then
            $dry_run || mkdir -p .github
            _llm_init_merge_claude_md "$source_dir/CLAUDE.md" "./.github/copilot-instructions.md" "$dry_run"
        fi

        # Sync agents from canonical source (.llm_settings/skills/) into .github/agents/.
        # Skills convert to Copilot's .agent.md format (name+description frontmatter,
        # tools omitted — defaults to all); reference material routes to
        # .github/agent-prompts/ verbatim instead of becoming an invocable agent.
        if [ -d "$llm_settings_src/skills" ]; then
            $dry_run || rm -rf .github/agents
            $dry_run || mkdir -p .github/agents
            $dry_run || rm -rf .github/agent-prompts
            local copilot_skill_count=0
            for skill_dir in "$llm_settings_src/skills"/*/; do
                local skill_name
                skill_name=$(basename "$skill_dir")
                if [ -f "$skill_dir/SKILL.md" ]; then
                    _llm_init_skill_allowed "$skill_name" "$skill_profile" "$llm_settings_src" || continue
                    if _llm_init_gemini_excluded "$skill_name"; then
                        if ! $dry_run; then
                            mkdir -p .github/agent-prompts
                            cp "$skill_dir/SKILL.md" ".github/agent-prompts/${skill_name}.md"
                        fi
                        continue
                    fi
                    $dry_run || _llm_init_convert_for_copilot "$skill_dir/SKILL.md" ".github/agents" "$skill_name"
                    ((copilot_skill_count++))
                fi
            done
            # Also sync agents from .llm_settings/agents/ into .github/agents/
            if [ -d "$llm_settings_src/agents" ]; then
                for agent_file in "$llm_settings_src/agents"/*.md; do
                    [ -f "$agent_file" ] || continue
                    if _llm_init_gemini_excluded "$(basename "${agent_file%.md}")"; then
                        if ! $dry_run; then
                            mkdir -p .github/agent-prompts
                            cp "$agent_file" ".github/agent-prompts/$(basename "$agent_file")"
                        fi
                        continue
                    fi
                    $dry_run || _llm_init_convert_for_copilot "$agent_file" ".github/agents"
                done
            fi
            echo "   ✅ .github/agents/ synchronized ($copilot_skill_count skills [$skill_profile profile] + agents, MCP configured)"
        else
            local copilot_agents
            copilot_agents=$(ls .github/agents/*.agent.md 2>/dev/null | wc -l | tr -d ' ')
            echo "   ✅ .github/agents/ synchronized ($copilot_agents agents, MCP configured)"
        fi
    else
        echo "   ⚠️  .github/ directory not found in source"
    fi
    echo ""

    # 4b. Additional CLIs: OpenCode, Crush, Antigravity (agy), Grok Build, Pi, Oh My Pi
    echo "🧰 OpenCode / Crush / Antigravity / Grok Build / Pi / Oh My Pi (+ Gemini skills)"
    if _llm_init_any_tool_enabled gemini opencode crush agy grok pi omp cursor; then
        _llm_init_deploy_shared_skills "$dry_run" "$llm_settings_src" "$skill_profile"
        _llm_init_gemini_dedupe_commands "$dry_run"
        _llm_init_deploy_tool_agents "$dry_run" "$llm_settings_src" "$skill_profile"
        echo "   ℹ️  Grok Build reads .claude/skills and .claude/agents natively; Crush and Pi have no agent format"
        echo "   ℹ️  Their MCP config is derived from the filtered .mcp.json (see MCP filtering below)"
    else
        echo "   ⏭️  Skipped (none selected in --tools)"
    fi
    _llm_init_agent_reference_paths "$dry_run" "$llm_settings_src"
    echo ""

    # 5. MCP Configuration
    echo "5️⃣  MCP Servers"
    if [ -n "$llm_settings_src" ] && [ -f "$llm_settings_src/.mcp.json" ]; then
        rsync -a $rsync_dry "$llm_settings_src/.mcp.json" .
        # Patch hardcoded macOS paths after sync (skip in dry-run)
        if ! $dry_run && [ -f ".mcp.json" ] && [ -n "$uvx_path" ]; then
            sed -i.bak \
                -e "s|/opt/homebrew/bin/uvx|$uvx_path|g" \
                -e "s|/opt/homebrew/bin/npx|${npx_path:-/opt/homebrew/bin/npx}|g" \
                -e "s|/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin|$mcp_path|g" \
                .mcp.json
            # Validate JSON after sed patching
            if command -v jq >/dev/null 2>&1 && ! jq empty .mcp.json 2>/dev/null; then
                echo "   ❌ Path patching corrupted .mcp.json — restoring backup" >&2
                mv .mcp.json.bak .mcp.json
            else
                rm -f .mcp.json.bak
            fi
        fi
        echo "   ✅ .mcp.json synchronized"
    else
        echo "   ⚠️  .mcp.json not found in source"
    fi
    echo ""

    # 6. LLM Settings (all subdirectories synchronized recursively)
    echo "6️⃣  LLM Settings Directory"
    if [ -n "$llm_settings_src" ] && [ -d "$llm_settings_src" ]; then
        $dry_run || mkdir -p .llm_settings

        # Synchronize llm_settings with secrets/local files excluded
        rsync -a $rsync_dry --delete \
            --filter='include .env.example' \
            --filter='include .env.*.example' \
            --filter='include .llm_env_example' \
            --filter='exclude .env' \
            --filter='exclude .env.*' \
            --filter='exclude .llm_env' \
            --filter='exclude *.local.*' \
            --filter='protect .env' \
            --filter='protect .env.*' \
            --filter='protect .llm_env' \
            --filter='protect *.local.*' \
            --filter='exclude repo-tenants' \
            --filter='protect repo-tenants' \
            --filter='exclude repo-mcp-servers' \
            --filter='protect repo-mcp-servers' \
            --filter='exclude repo-tools' \
            --filter='protect repo-tools' \
            --exclude='.DS_Store' \
            --exclude='.cache/' \
            --exclude='tmp/' \
            --exclude='logs/' \
            --exclude='*token*' \
            --exclude='*secret*' \
            --exclude='*credential*' \
            --exclude='*password*' \
            --exclude='*.pem' \
            --exclude='*.key' \
            --exclude='mcp-servers/*/.claude' \
            --exclude='scripts/.claude/' \
            --exclude='scripts/.gemini/' \
            --exclude='scripts/.codex/' \
            --exclude='scripts/.github/' \
            --exclude='scripts/.mcp.json' \
            --exclude='scripts/.llm_settings/' \
            "$llm_settings_src/" .llm_settings/

        # Make scripts executable
        if ! $dry_run; then
            find .llm_settings/scripts -type f -name '*.sh' -exec chmod +x {} \; 2>/dev/null || true
            find .llm_settings/git-hooks -type f -exec chmod +x {} \; 2>/dev/null || true
            find .llm_settings/mcp-servers -type f -name '*.sh' -exec chmod +x {} \; 2>/dev/null || true
        fi

        echo "   ✅ .llm_settings/ synchronized (secrets preserved, scripts executable)"

        # ── Env file deployment (--env flag) ──────────────────────────
        if [[ -n "${env_store:-}" ]]; then
            local env_src="$env_store/mcp-servers"
            echo ""
            echo "🔑 Deploying .env files from: $env_src"

            if [[ -d "$env_src" ]]; then
                local _env_deployed=0 _env_missing=0
                local -a _env_paths=()

                if [[ ${#mcp_servers[@]} -gt 0 ]]; then
                    # Scoped to selected MCP servers
                    for _srv in "${mcp_servers[@]}"; do
                        case "$_srv" in
                            github)                _env_paths+=("github/default") ;;
                            github-idallasj)       _env_paths+=("github/idallasj") ;;
                            github-fluence)        _env_paths+=("github/fluence") ;;
                            github-agentshroud)    _env_paths+=("github/agentshroud") ;;
                            atlassian-fluence)     _env_paths+=("atlassian/fluence") ;;
                            atlassian-agentshroud) _env_paths+=("atlassian/agentshroud") ;;
                            atlassian-idallasj)    _env_paths+=("atlassian/idallasj") ;;
                            home-assistant)        _env_paths+=("home-assistant") ;;
                            devonthink)            _env_paths+=("devonthink") ;;
                            # aws, xmind, safari have no credentials — skip silently
                        esac
                    done
                else
                    # No --mcp filter: deploy all .env files in store
                    while IFS= read -r -d '' _src_env; do
                        local _rel="${_src_env#"$env_src/"}"
                        _env_paths+=("$(dirname "$_rel")")
                    done < <(find "$env_src" -name ".env" -type f -print0 2>/dev/null | sort -z)
                fi

                for _rel_dir in "${_env_paths[@]}"; do
                    local _src_env="$env_src/$_rel_dir/.env"
                    local _dest=".llm_settings/mcp-servers/$_rel_dir/.env"
                    local _dest_dir=".llm_settings/mcp-servers/$_rel_dir"

                    if [[ ! -f "$_src_env" ]]; then
                        echo "   ⚠️  Not in store (skipped): $_rel_dir/.env"
                        ((_env_missing++)) || true
                        continue
                    fi

                    if $dry_run; then
                        echo "   (dry-run) ✅ Deployed: $_rel_dir/.env"
                    else
                        mkdir -p "$_dest_dir"
                        cp "$_src_env" "$_dest"
                        chmod 600 "$_dest"
                        echo "   ✅ Deployed: $_rel_dir/.env"
                    fi
                    ((_env_deployed++)) || true
                done

                echo "   Deployed: $_env_deployed | Not in store (skipped): $_env_missing"
            else
                echo "   ⚠️  Secrets store not found: $env_src"
                echo "      Run: .llm_settings/scripts/security/setup-env-store.sh"
            fi
        fi
    else
        echo "   ⚠️  .llm_settings/ directory not found in source"
    fi

    # Enforce legacy -> dot-directory migration in target repo
    # (handles edge cases where legacy folder survives cleanup)
    if [ -d "llm_settings" ]; then
        if [ -d ".llm_settings" ]; then
            if [ -f "llm_settings/scripts/llm-init.sh" ] || [ -d "llm_settings/skills" ] || [ -d "llm_settings/agents" ]; then
                echo "   🧹 Removing legacy llm_settings/ (migrated to .llm_settings/)"
                $dry_run || rm -rf "llm_settings"
            fi
        else
            echo "   🔁 Migrating legacy llm_settings/ -> .llm_settings/"
            if $dry_run; then
                echo "   ℹ️  [dry-run] Would move llm_settings to .llm_settings"
            else
                mv "llm_settings" ".llm_settings"
            fi
        fi
    fi
    echo ""

    # 7. Git Security Configuration
    echo "7️⃣  Git Security Configuration"

    # Deploy .gitignore (augment if exists)
    if [ -f "$llm_settings_src/templates/.gitignore" ]; then
        if [ -f ".gitignore" ]; then
            if $dry_run; then
                echo "   ℹ️  [dry-run] Would merge missing patterns into existing .gitignore"
            else
                cat "$llm_settings_src/templates/.gitignore" >> .gitignore
                awk '!seen[$0]++' .gitignore > .gitignore.tmp && mv .gitignore.tmp .gitignore
                echo "   ✅ .gitignore augmented with missing template patterns"
            fi
        else
            rsync -a $rsync_dry "$llm_settings_src/templates/.gitignore" .
            echo "   ✅ .gitignore deployed from template"
        fi
    else
        echo "   ⚠️  .gitignore template not found in source"
    fi

    # Deploy .pre-commit-config.yaml (preserve existing if present)
    if [ -f "$llm_settings_src/templates/.pre-commit-config.yaml" ]; then
        if [ -f ".pre-commit-config.yaml" ]; then
            echo "   ✅ .pre-commit-config.yaml preserved (existing repo config kept)"
        else
            rsync -a $rsync_dry "$llm_settings_src/templates/.pre-commit-config.yaml" .
            echo "   ✅ .pre-commit-config.yaml deployed"
        fi
    else
        echo "   ⚠️  .pre-commit-config.yaml template not found in source"
    fi

    # Deploy .gitallowed (always augment if exists)
    if [ -f "$llm_settings_src/templates/.gitallowed" ]; then
        if [ -f ".gitallowed" ]; then
            if $dry_run; then
                echo "   ℹ️  [dry-run] Would merge template patterns into existing .gitallowed"
            else
                # Append template patterns if not already present
                cat "$llm_settings_src/templates/.gitallowed" >> .gitallowed
                # Remove duplicates while preserving comments
                awk '!seen[$0]++' .gitallowed > .gitallowed.tmp && mv .gitallowed.tmp .gitallowed
                echo "   ✅ .gitallowed merged with template"
            fi
        else
            rsync -a $rsync_dry "$llm_settings_src/templates/.gitallowed" .
            echo "   ✅ .gitallowed deployed from template"
        fi
    else
        echo "   ⚠️  .gitallowed template not found in source"
    fi

    # Deploy gitleaks.toml (augment if existing)
    if [ -f "$llm_settings_src/git-hooks/gitleaks.toml" ]; then
        if [ -f "gitleaks.toml" ]; then
            if $dry_run; then
                echo "   ℹ️  [dry-run] Would augment existing gitleaks.toml (non-destructive)"
            else
                if grep -q "path = \".llm_settings/git-hooks/gitleaks.toml\"" gitleaks.toml 2>/dev/null || grep -q "regexes = \\['REDACTED'\\]" gitleaks.toml 2>/dev/null; then
                    echo "   ✅ gitleaks.toml preserved (already contains llm_settings rule)"
                elif grep -q "^\\[extend\\]" gitleaks.toml 2>/dev/null; then
                    echo "   ⚠️  gitleaks.toml has [extend] already; skipped auto-merge to avoid breaking existing config"
                    echo "      Add manually: path = \".llm_settings/git-hooks/gitleaks.toml\" under [extend]"
                else
                    {
                        echo ""
                        echo "# Added by llm-init: extend with llm_settings defaults"
                        echo "[extend]"
                        echo "path = \".llm_settings/git-hooks/gitleaks.toml\""
                    } >> gitleaks.toml
                    echo "   ✅ gitleaks.toml augmented via [extend] path to .llm_settings/git-hooks/gitleaks.toml"
                fi
            fi
        else
            rsync -a $rsync_dry "$llm_settings_src/git-hooks/gitleaks.toml" .
            echo "   ✅ gitleaks.toml deployed (custom gitleaks config)"
        fi
    else
        echo "   ⚠️  gitleaks.toml not found in source"
    fi

    # Check if this is a git repository (handles both normal repos and git worktrees)
    if git rev-parse --git-dir > /dev/null 2>&1; then
        # Install pre-commit hooks if pre-commit is available
        if command -v pre-commit &> /dev/null && [ -f ".pre-commit-config.yaml" ]; then
            echo "   🔒 Installing pre-commit hooks..."
            if $dry_run; then
                echo "   ℹ️  [dry-run] Would install pre-commit hooks"
            else
                _pc_install_err="$(mktemp)"
                if pre-commit install --install-hooks >"$_pc_install_err" 2>&1 || pre-commit install >"$_pc_install_err" 2>&1; then
                    _pc_installed=true
                else
                    _pc_installed=false
                fi

                if $_pc_installed; then
                    # Create secrets baseline if detect-secrets is configured
                    # The deployed .pre-commit-config.yaml passes --baseline .secrets.baseline,
                    # so the file MUST exist or the detect-secrets hook fails on every commit.
                    if grep -q "detect-secrets" ".pre-commit-config.yaml" 2>/dev/null; then
                        if [ ! -f ".secrets.baseline" ]; then
                            echo "   📊 Creating secrets baseline..."
                            if command -v detect-secrets &> /dev/null; then
                                detect-secrets scan > .secrets.baseline 2>/dev/null || true
                            else
                                python3 -m detect_secrets scan > .secrets.baseline 2>/dev/null || true
                            fi
                            if [ -s ".secrets.baseline" ]; then
                                echo "   ✅ .secrets.baseline created"
                            else
                                rm -f .secrets.baseline
                                echo "   ⚠️  detect-secrets CLI not available — .secrets.baseline NOT created."
                                echo "      The detect-secrets pre-commit hook will fail until you run:"
                                echo "      pipx install detect-secrets && detect-secrets scan > .secrets.baseline"
                            fi
                        fi
                    fi

                    echo "   ✅ Pre-commit hooks installed"

                    # Optional: Run once to verify
                    read -p "   Run pre-commit on all files now? [y/N] " -n 1 -r
                    echo
                    if [[ $REPLY =~ ^[Yy]$ ]]; then
                        echo "   🔍 Running pre-commit checks..."
                        pre-commit run --all-files || true
                        echo ""
                    fi
                else
                    echo "   ⚠️  Pre-commit hooks NOT installed:"
                    sed 's/^/      /' "$_pc_install_err"
                    if grep -q "core.hooksPath" "$_pc_install_err"; then
                        echo "      Fix with: git config --unset-all core.hooksPath"
                        echo "      Then re-run: pre-commit install --install-hooks"
                    else
                        echo "      Resolve the error above, then run: pre-commit install --install-hooks"
                    fi
                fi
                rm -f "$_pc_install_err"
            fi
        else
            # Fall back to manual git hooks
            if [ -f ".llm_settings/git-hooks/install.sh" ]; then
                echo "   🔒 Installing fallback git hooks..."
                if $dry_run; then
                    echo "   ℹ️  [dry-run] Would install fallback git hooks"
                else
                    chmod +x .llm_settings/git-hooks/install.sh
                    # Run in current directory context (ensure .git is visible)
                    if (cd "$(pwd)" && .llm_settings/git-hooks/install.sh 2>&1); then
                        echo "   ✅ Fallback git hooks installed"
                    else
                        echo "   ⚠️  Fallback hook installation failed (not a git repo)"
                    fi
                fi
            else
                echo "   ⚠️  Git hooks installer not found"
            fi

            if ! command -v pre-commit &> /dev/null; then
                echo "   💡 Tip: Install pre-commit for better security"
                echo "      pip install pre-commit"
            fi
        fi
    else
        echo "   ⚠️  Not a git repository - hooks not installed"
        echo "      Run 'pre-commit install' or '.llm_settings/git-hooks/install.sh' after git init"
    fi
    echo ""

    # 8. Security Scripts & Audit
    echo "8️⃣  Security Setup"
    if [ -d ".llm_settings/scripts/security" ]; then
        echo "   ✅ Security scripts available:"
        echo "      - setup-direnv.sh      (secure environment variables)"
        echo "      - setup-pgpass.sh      (PostgreSQL passwords)"
        echo "      - security-audit.sh    (scan for secrets in history)"
        echo "      - quick-setup.sh       (run all security setup)"

        # Optionally run security audit
        if git rev-parse --git-dir > /dev/null 2>&1; then
            if $dry_run; then
                echo "   ℹ️  [dry-run] Would prompt: Run security audit now?"
            else
                read -p "   Run security audit now? [y/N] " -n 1 -r
                echo
                if [[ $REPLY =~ ^[Yy]$ ]]; then
                    echo ""
                    .llm_settings/scripts/security/security-audit.sh
                    echo ""
                fi
            fi
        fi
    else
        echo "   ⚠️  Security scripts not found in source"
    fi
    echo ""

    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "✅ LLM AI tool configurations synchronized successfully!"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "🔄 Synchronization behavior:"
    echo "   ✅ Added new files from source"
    echo "   ✅ Updated existing files to match source"
    echo "   ✅ Removed obsolete files (no longer in source)"
    echo "   ✅ Preserved secrets (.env, *.local.*, credentials, tokens)"
    echo ""
    echo "📁 Files synchronized:"
    echo "   - .claude/                      (agents, skills, hooks, settings)"
    echo "   - .gemini/                      (agents, settings.json, GEMINI.md)"
    echo "   - .codex/                       (agents, config.toml)"
    echo "   - .github/                      (agents, mcp.json, copilot-instructions.md)"
    echo "   - .mcp.json                     (MCP servers for Claude Code)"
    echo "   - .gitignore                    (comprehensive security template)"
    echo "   - .pre-commit-config.yaml       (secret detection framework)"
    echo "   - .gitallowed                   (false positive patterns)"
    if [ -f "$(git rev-parse --git-common-dir 2>/dev/null)/hooks/pre-commit" ]; then
        echo "   - .git/hooks/pre-commit         (secret scanning protection)"
    fi
    echo "   - CLAUDE.md                     (primary developer context)"
    echo "   - AGENTS.md                     (secondary/tertiary agent context)"
    echo "   - .llm_settings/                 (organized LLM configuration)"
    echo "     ├── agents/                   (real subagent definitions — all CLIs)"
    echo "     ├── ci-cd/                    (CI/CD pipeline definitions)"
    echo "     ├── docs/                     (documentation files)"
    echo "     ├── env/                      (environment templates)"
    echo "     ├── git-hooks/                (fallback security hooks)"
    echo "     ├── mcp-servers/              (GitHub & Atlassian MCP servers)"
    echo "     ├── podcast/                  (podcast pipeline definitions)"
    echo "     ├── scripts/                  (deployment & security scripts)"
    echo "     │   ├── llm-init.sh"
    echo "     │   └── security/             (direnv, pgpass, audit)"
    echo "     ├── skills/                   (60 skill definitions — all CLIs)"
    echo "     ├── sre/                      (SRE runbooks and definitions)"
    echo "     ├── templates/                (.gitignore, pre-commit, .gitallowed)"
    echo "     └── WORKFLOW.md               (multi-agent workflow guide)"
    echo ""
    echo "📝 Next steps:"
    echo "   1. 📖 Read: .llm_settings/docs/SECURITY_GUIDE.md"
    echo "   2. 📖 Read: .llm_settings/docs/CONFIGURATION_SUMMARY.md"
    echo "   3. 🔒 Security: .llm_settings/scripts/security/quick-setup.sh"
    echo "   4. 🔌 MCP GitHub: cp .llm_settings/mcp-servers/github/.env.example .env"
    echo "   5. 🔌 MCP User: .llm_settings/scripts/setup-mcp-user.sh (global config)"
    echo "   6. ☁️  AWS: export AWS_PROFILE=default AWS_REGION=us-east-1"
    echo "   7. 🏠 Home Assistant MCP: export HA_TOKEN=<long-lived-access-token>"
    echo "      (Settings → Security → Long-Lived Access Tokens → Create Token)"
    echo "      Optional: export HA_BASE_URL=http://homeassistant.local:8123"
    echo "   8. 🤖 Test tools:"
    echo "      - claude      (PRIMARY developer)"
    echo "      - gemini      (SECONDARY agent)"
    echo "      - codex       (TERTIARY agent)"
    echo "      - copilot     (QUATERNARY agent)"
    echo ""
    echo "🔌 MCP Servers configured:"
    echo "   - GitHub          (.llm_settings/mcp-servers/github/)"
    echo "   - Atlassian       (.llm_settings/mcp-servers/atlassian/)"
    echo "   - AWS API         (via uvx awslabs.aws-api-mcp-server)"
    echo "   - XMind Generator (via npx xmind-generator-mcp)"
    echo "   - Safari          (via npx safari-mcp)"
    echo "   - Home Assistant  (.llm_settings/mcp-servers/home-assistant/)"
    echo "   - macuse          (opt-in via --mcp macuse; global user-scope, macOS only)"
    echo "   - twg             (opt-in via --mcp twg; not an MCP server — status check only, see docs/MCP_README.md)"
    echo ""
    echo "   📝 Project-level: .mcp.json (works in this repo only)"
    echo "   💡 User-level: Run setup-mcp-user.sh to enable 'claude mcp list'"
    echo "   🔧 Select servers per-repo: llm-init --mcp <server> [--mcp <server>]... ."
    echo ""

    # Offer to configure user-level MCP servers
    if [ -f ".llm_settings/scripts/setup-mcp-user.sh" ]; then
        if $dry_run; then
            echo "   ℹ️  [dry-run] Would prompt: Configure MCP servers globally?"
        else
            read -p "   Configure MCP servers globally (user-level)? [y/N] " -n 1 -r
            echo
            if [[ $REPLY =~ ^[Yy]$ ]]; then
                echo ""
                .llm_settings/scripts/setup-mcp-user.sh
                echo ""
            else
                echo "   ⏭️  Skipped user-level MCP setup"
                echo "      Run later with: .llm_settings/scripts/setup-mcp-user.sh"
                echo ""
            fi
        fi
    fi

    # Apply MCP server filtering after all rsync operations
    echo ""
    echo "🎛️  Applying MCP server filtering..."
    _llm_init_render_mcp "$dry_run"
    echo ""

    # MCP for OpenCode / Crush / agy / Grok / Pi / Oh My Pi — derived from the filtered .mcp.json
    if _llm_init_any_tool_enabled opencode crush agy grok pi omp cursor; then
        echo "🧰 Emitting MCP config for the additional CLIs..."
        _llm_init_mcp_emit_tools "$dry_run"
        echo ""
    fi

    echo "🧪 Testing agents summary..."
    _llm_init_testing_summary "$dry_run" "$source_dir"
    echo ""

    # macuse: global user-scope MCP registration (opt-in via --mcp macuse).
    # Not part of the per-repo file rendering above — see _llm_init_ensure_macuse.
    local _macuse_selected=false _ms
    for _ms in "${mcp_servers[@]:-}"; do
        [ "$_ms" = "macuse" ] && _macuse_selected=true
    done
    if ! $_macuse_selected && [ ${#mcp_servers[@]} -eq 0 ] \
        && [ -f "$_mcp_marker_file" ] && grep -qx 'macuse' "$_mcp_marker_file" 2>/dev/null; then
        _macuse_selected=true  # sticky: no --mcp given this run, but prior selection included macuse
    fi
    if $_macuse_selected; then
        _llm_init_ensure_macuse "$dry_run"
        echo ""
    fi

    # twg: Atlassian Teamwork Graph CLI status check (opt-in via --mcp twg).
    # Not part of the per-repo file rendering above — see _llm_init_check_twg.
    local _twg_selected=false _tw
    for _tw in "${mcp_servers[@]:-}"; do
        [ "$_tw" = "twg" ] && _twg_selected=true
    done
    if ! $_twg_selected && [ ${#mcp_servers[@]} -eq 0 ] \
        && [ -f "$_mcp_marker_file" ] && grep -qx 'twg' "$_mcp_marker_file" 2>/dev/null; then
        _twg_selected=true  # sticky: no --mcp given this run, but prior selection included twg
    fi
    # Account-scope context (fluence | personal | mixed | none), derived from this
    # run's selection or, when no --mcp was given, the sticky marker. Drives the
    # twg account-separation guard and the sf auth check (both warn-only).
    local -a _ctx_servers=()
    local _cl
    if [ ${#mcp_servers[@]} -gt 0 ]; then
        _ctx_servers=("${mcp_servers[@]}")
    elif [ -f "$_mcp_marker_file" ]; then
        while IFS= read -r _cl; do
            _cl="${_cl%%#*}"; _cl="${_cl//[[:space:]]/}"
            [ -n "$_cl" ] && _ctx_servers+=("$_cl")
        done < "$_mcp_marker_file"
    fi
    local _mcp_ctx
    _mcp_ctx="$(_llm_init_mcp_context ${_ctx_servers[@]+"${_ctx_servers[@]}"})"
    if [ "$_mcp_ctx" != "none" ]; then
        _twg_selected=true  # group selection implies the read-only twg check (guarded by account scope)
    fi
    if $_twg_selected; then
        _llm_init_check_twg "$dry_run" "$_mcp_ctx"
        echo ""
    fi
    if [ "$_mcp_ctx" != "none" ]; then
        _llm_init_check_sf "$dry_run" "$_mcp_ctx"
        echo ""
    fi

    # gmail: Hermes / OpenClaw are outside llm-init's per-repo rendering — print setup.
    local _gm_selected=false _gm
    for _gm in ${_ctx_servers[@]+"${_ctx_servers[@]}"}; do
        [ "$_gm" = "gmail" ] && _gm_selected=true
    done
    if $_gm_selected; then
        _llm_init_gmail_global_hint "$dry_run"
        echo ""
    fi

    # Security status
    echo "🔒 Security features installed:"
    if command -v pre-commit &> /dev/null && [ -f ".pre-commit-config.yaml" ]; then
        echo "   ✅ Pre-commit framework (gitleaks + detect-secrets + validators)"
        echo "   ✅ Comprehensive .gitignore (200+ patterns)"
        echo "   ✅ .gitallowed (false positive patterns)"
        echo "   ✅ Secret scanning on every commit"
        echo ""
        echo "   💡 Pre-commit commands:"
        echo "      pre-commit run --all-files    # Run all hooks manually"
        echo "      pre-commit autoupdate         # Update hook versions"
        echo "      git commit --no-verify        # Skip hooks (emergency only)"
    elif [ -f "$(git rev-parse --git-common-dir 2>/dev/null)/hooks/pre-commit" ]; then
        echo "   ✅ Git hooks (gitleaks + git-secrets)"
        echo "   ✅ Comprehensive .gitignore (200+ patterns)"
        echo "   ✅ .gitallowed (false positive patterns)"
        echo "   ✅ Secret scanning on every commit"
        echo ""
        echo "   💡 Upgrade to pre-commit framework:"
        echo "      pip install pre-commit"
        echo "      pre-commit install"
    else
        echo "   ⚠️  No hooks installed (not a git repository)"
    fi
    echo ""

    echo "🧪 Test git security:"
    echo "   echo 'password=secret123' > test.txt"
    echo "   git add test.txt"
    echo "   git commit -m 'test'  # Should be blocked!"
    echo "   rm test.txt"
    echo ""
    echo "🔒 Security best practices:"
    echo "   ✅ Never commit .env files (use direnv instead)"
    echo "   ✅ Never commit API keys (use AWS Secrets Manager)"
    echo "   ✅ Never commit passwords (use ~/.pgpass for PostgreSQL)"
    echo "   ✅ Run security audit periodically"
    echo "   ✅ Review all files before committing"
    echo ""
    echo "📚 Documentation:"
    echo "   - Security Guide:     .llm_settings/docs/SECURITY_GUIDE.md"
    echo "   - AI Tools Guide:     .llm_settings/docs/AI_TOOLS_CONFIGURATION_GUIDE.md"
    echo "   - Quick Reference:    .llm_settings/docs/CONFIGURATION_SUMMARY.md"
    echo ""
}

# Export function if script is sourced
if [[ "${BASH_SOURCE[0]}" != "${0}" ]]; then
    export -f llm-init
    export -f _llm_init_render_mcp
    export -f _llm_init_ensure_macuse
    export -f _llm_init_check_twg
    export -f _llm_init_bounded
    export -f _llm_init_mcp_context
    export -f _llm_init_email_scope
    export -f _llm_init_check_sf
    export -f _llm_init_parse_tools
    export -f _llm_init_tool_enabled
    export -f _llm_init_any_tool_enabled
    export -f _llm_init_normalize_skill_name
    export -f _llm_init_deploy_shared_skills
    export -f _llm_init_gemini_dedupe_commands
    export -f _llm_init_agent_reference_paths
    export -f _llm_init_convert_agent
    export -f _llm_init_deploy_tool_agents
    export -f _llm_init_mcp_src_ok
    export -f _llm_init_emit_std_json
    export -f _llm_init_emit_merge_json
    export -f _llm_init_mcp_emit_agy
    export -f _llm_init_mcp_emit_cursor
    export -f _llm_init_mcp_emit_pi
    export -f _llm_init_mcp_emit_omp
    export -f _llm_init_mcp_emit_opencode
    export -f _llm_init_mcp_emit_crush
    export -f _llm_init_skill_dest_name
    export -f _llm_init_skill_map_load
    export -f _llm_init_skill_name_for
    export -f _llm_init_mcp_emit_grok
    export -f _llm_init_mcp_emit_tools
    export -f _llm_init_render_testing_agents
    export -f _llm_init_testing_summary
    export -f _llm_init_gmail_accounts
    export -f _llm_init_render_gmail
    export -f _llm_init_gmail_global_hint
    export -f _llm_init_normalize_md
    export -f _llm_init_gemini_excluded
    export -f _llm_init_doctor_gemini
    export -f _llm_init_doctor_agy
    export -f _llm_init_shell_bootstrap
    echo "✅ llm-init function loaded"
    echo "   Usage: llm-init [--dry-run] [--mcp <server>]... [--keep] [--skills <profile>] [--tools <list>] [target_directory]"
    echo "   MCP servers: github | aws | xmind | safari | home-assistant | devonthink | gmail | macuse | twg |"
    echo "                atlassian-fluence | atlassian-agentshroud | atlassian-idallasj |"
    echo "                all | fluence | personal"
    echo "   --keep: add to the existing MCP selection instead of replacing it"
    echo "   Run: llm-init --help for full usage"
fi

# If script is executed (not sourced), run the function
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    llm-init "$@"
fi
