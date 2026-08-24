#!/usr/bin/env python3
"""Deterministic prefetch for the CVE Triage cron job. Fetches both GitHub
security-advisories endpoints, diffs against the known-GHSA-IDs cache
(itself prefetched from marvin's registry by a companion command job), and
writes ONLY the genuinely new CVEs to a small file. Removes raw fetching,
pagination, and 31KB-file parsing from the agent's own task entirely --
the agent's job becomes: read this small file, analyze each new CVE (if
any), post to Telegram. Mirrors the pattern that fixed Hermes newsletters:
push everything deterministic out of the agent's own reasoning loop.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

REPOS = [
    ("openclaw", "openclaw/openclaw"),
    ("hermes-agent", "nousresearch/hermes-agent"),
]
CACHE_FILE = Path("/home/node/.openclaw/workspace/.ghsa-ids-cache.json")
OUT_FILE = Path("/home/node/.openclaw/workspace/.new-cves.json")


def curl_json(url):
    result = subprocess.run(
        ["curl", "-s", "-m", "20", "-w", "\n%{http_code}", url],
        capture_output=True, text=True, timeout=25,
    )
    body, _, status = result.stdout.rpartition("\n")
    return status.strip(), body


def known_ghsa_ids():
    if not CACHE_FILE.exists():
        return set(), "cache file missing"
    try:
        envelope = json.loads(CACHE_FILE.read_text())
    except Exception as e:
        return set(), f"cache file unparseable: {e}"
    stdout = envelope.get("stdout", "")
    ids = set(re.findall(r'"ghsa_id":\s*"([^"]+)"', stdout))
    return ids, None


def main():
    known, cache_error = known_ghsa_ids()
    new_cves = []
    fetch_errors = []

    for label, repo in REPOS:
        url = f"https://api.github.com/repos/{repo}/security-advisories?per_page=100"
        status, body = curl_json(url)
        if status != "200":
            fetch_errors.append(f"{label}: HTTP {status}")
            continue
        try:
            advisories = json.loads(body)
        except Exception as e:
            fetch_errors.append(f"{label}: unparseable response ({e})")
            continue
        if not isinstance(advisories, list):
            fetch_errors.append(f"{label}: unexpected response shape")
            continue
        for adv in advisories:
            ghsa_id = adv.get("ghsa_id")
            if not ghsa_id or ghsa_id in known:
                continue
            new_cves.append({
                "ghsa_id": ghsa_id,
                "cve_id": adv.get("cve_id"),
                "severity": adv.get("severity"),
                "cvss_score": (adv.get("cvss") or {}).get("score"),
                "summary": adv.get("summary"),
                "published_at": adv.get("published_at"),
                "html_url": adv.get("html_url"),
                "repo": label,
            })

    out = {
        "known_ghsa_count": len(known),
        "cache_error": cache_error,
        "fetch_errors": fetch_errors,
        "new_cve_count": len(new_cves),
        "new_cves": new_cves,
    }
    OUT_FILE.write_text(json.dumps(out, indent=2))
    print(f"known={len(known)} new={len(new_cves)} fetch_errors={fetch_errors} cache_error={cache_error}")


if __name__ == "__main__":
    main()
