#!/usr/bin/env bash
# shellcheck disable=SC2034,SC1091
# eval-run.sh — LLM golden-set evals and prompt checks (i-data-ai-ot gate)
# Contract and env: see lib.sh (--json, I_GATE=report|block, I_REPO, exit 0/1/2).
set -o pipefail
. "$(dirname "${BASH_SOURCE[0]}")/lib.sh"
T_NAME="eval-run"; T_SUMMARY="LLM golden-set evals and prompt checks (i-data-ai-ot gate)"
T_OPTIONS="Environment: I_EVAL_DIR (default evals/), I_EVAL_CMD='<cmd>' runs your eval harness against the golden sets."
t_parse "" "$@"; t_init
dir="${I_EVAL_DIR:-evals}"
sets="$(ls "$dir"/*.jsonl 2>/dev/null)"
if [ -z "$sets" ]; then
    if [ -n "$(git ls-files 'prompts/*' '*.prompt' 2>/dev/null | head -1)" ]; then
        t_skip eval "prompt files exist but no golden set in $dir/*.jsonl"
    else
        t_skip eval "no golden sets ($dir/*.jsonl) and no prompt files"
    fi
else
    for s in $sets; do
        n=0; badline=0
        while IFS= read -r line || [ -n "$line" ]; do
            [ -z "$line" ] && continue
            n=$((n+1))
            case "$line" in \{*\}) ;; *) badline=$n ;; esac
        done < "$s"
        [ "$badline" -eq 0 ] && [ "$n" -gt 0 ] && t_record "golden-$(basename "$s")" pass "$n cases" || t_record "golden-$(basename "$s")" fail "invalid or empty JSONL (line $badline)"
    done
    if [ -n "${I_EVAL_CMD:-}" ]; then t_run eval "$I_EVAL_CMD"; else t_skip eval "golden sets validated; set I_EVAL_CMD to score the model/prompt"; fi
fi
t_finish
