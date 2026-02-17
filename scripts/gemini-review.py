#!/usr/bin/env python3
"""Lightweight Gemini API reviewer — no heavy CLI, just REST calls.

Usage:
    echo "diff content" | python3 scripts/gemini-review.py
    python3 scripts/gemini-review.py < diff.patch
    python3 scripts/gemini-review.py --diff "$(git diff main..HEAD)"
"""
import sys
import os
import json
import argparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError

API_KEY = os.environ.get("GEMINI_API_KEY", "")
MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent"

REVIEW_SYSTEM = """You are a senior code reviewer for SecureClaw, a security proxy for OpenClaw AI agents.
This is a security product — review with that lens.

Focus on:
1. Security: credential handling, injection, PII leaks, container security, audit gaps
2. Correctness: logic errors, edge cases, error handling, type safety
3. Testing: TDD compliance, coverage gaps (target >= 80%), test quality
4. Style: naming, structure, readability
5. Performance: runs on Raspberry Pi 4 (ARM64, 8GB RAM)

For each finding, output:
[SEVERITY] file:line — Description
  Suggested fix: ...

Severities: CRITICAL (blocks merge), HIGH (fix before merge), MEDIUM (fix soon), LOW (suggestion), INFO (observation).

If the code looks good, say so. Be constructive."""


def call_gemini(diff_text: str) -> str:
    """Call Gemini API and return the review text."""
    if not API_KEY:
        return "ERROR: GEMINI_API_KEY not set in environment"

    prompt = f"Review this code diff:\n\n```diff\n{diff_text}\n```"

    payload = json.dumps({
        "system_instruction": {"parts": [{"text": REVIEW_SYSTEM}]},
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.2,
            "maxOutputTokens": 8192,
        }
    }).encode("utf-8")

    req = Request(API_URL, data=payload, headers={
        "Content-Type": "application/json",
        "x-goog-api-key": API_KEY
    })

    try:
        with urlopen(req, timeout=120) as resp:
            data = json.loads(resp.read())
            candidates = data.get("candidates", [])
            if candidates:
                parts = candidates[0].get("content", {}).get("parts", [])
                return "".join(p.get("text", "") for p in parts)
            return "ERROR: No response from Gemini API"
    except HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        return f"ERROR: Gemini API returned {e.code}: {body[:500]}"
    except Exception as e:
        return f"ERROR: Gemini API call failed: {e}"


def main():
    parser = argparse.ArgumentParser(description="Lightweight Gemini code reviewer")
    parser.add_argument("--diff", type=str, help="Diff text (or pipe via stdin)")
    args = parser.parse_args()

    if args.diff:
        diff_text = args.diff
    elif not sys.stdin.isatty():
        diff_text = sys.stdin.read()
    else:
        print("Usage: echo 'diff' | python3 gemini-review.py", file=sys.stderr)
        print("   or: python3 gemini-review.py --diff '$(git diff)'", file=sys.stderr)
        sys.exit(1)

    if not diff_text.strip():
        print("No diff provided.")
        sys.exit(0)

    # Truncate very large diffs to avoid API limits
    max_chars = 120000
    if len(diff_text) > max_chars:
        diff_text = diff_text[:max_chars] + "\n\n[TRUNCATED — diff exceeded 120K chars]"
        print(f"Warning: diff truncated to {max_chars} chars", file=sys.stderr)

    result = call_gemini(diff_text)
    print(result)


if __name__ == "__main__":
    main()
