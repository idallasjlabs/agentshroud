# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
"""Daily CVE Report — container vulnerability digest + upstream agent CVE watch.

Two schedulers run in parallel, both at the configurable UTC report hour:

  1. **Trivy digest** — scans the container filesystem, formats a severity-bucketed
     report, and sends it to the owner via Telegram Bot API.

  2. **Upstream CVE watch** — fetches GitHub Security Advisories for the wrapped
     agent (OpenClaw), diffs against AGENT_CVE_REGISTRY, and sends a Telegram alert
     if any new CVE IDs are found that are not yet in the registry.

Triggers:
  - Daily schedule: configurable via AGENTSHROUD_CVE_REPORT_HOUR (default 06:00 UTC)
  - On-demand Trivy: POST /soc/v1/cve-report
"""

from __future__ import annotations

import asyncio
import json
import logging
import os
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Optional

from .trivy_report import SEVERITY_ORDER, generate_summary, run_trivy_scan, save_report

logger = logging.getLogger("agentshroud.security.daily_cve_report")

# Severity → emoji mapping for Telegram formatting.
_SEV_ICON = {
    "CRITICAL": "🔴",
    "HIGH": "🟠",
    "MEDIUM": "🟡",
    "LOW": "🟢",
    "UNKNOWN": "⚪",
}

# GitHub repository for the wrapped agent — used by the upstream CVE watch.
_OPENCLAW_GITHUB_REPO = "openclaw/openclaw"

# Path to store the last report timestamp so we avoid duplicate sends on restart.
_LAST_REPORT_PATH = Path("/var/log/security/trivy/.last_cve_report")
_LAST_UPSTREAM_CHECK_PATH = Path("/var/log/security/trivy/.last_upstream_cve_check")

# In-memory guards: track dates already processed this process lifetime.
# Prevents infinite send loops when the disk is full and the paths can't be written.
_sent_dates: set[str] = set()
_upstream_check_dates: set[str] = set()


def format_cve_report(report: dict[str, Any]) -> str:
    """Format a Trivy scan result into a Telegram-ready Markdown message.

    Args:
        report: Parsed Trivy report from ``parse_trivy_output()``.

    Returns:
        Markdown string suitable for Telegram ``parse_mode=Markdown``.
    """
    if report.get("error"):
        return (
            "⚠️ *AgentShroud™ Daily CVE Report*\n\n"
            f"Scan error: `{report['error']}`\n"
            "Run `/soc/v1/scan/trivy` to retry."
        )

    by_sev = report.get("by_severity", {})
    total = report.get("total_vulnerabilities", 0)
    ts = report.get("timestamp", datetime.now(timezone.utc).isoformat())

    # Header
    lines = ["🛡️ *AgentShroud™ Daily CVE Report*"]
    lines.append(f"📅 {ts[:10]}  |  🔍 {total} vulnerabilities\n")

    # Severity breakdown
    lines.append("*Severity Breakdown*")
    for sev in SEVERITY_ORDER:
        count = by_sev.get(sev, 0)
        if count > 0:
            lines.append(f"  {_SEV_ICON.get(sev, '⚪')} {sev}: *{count}*")

    # Affected packages
    pkg_count = report.get("affected_package_count", 0)
    if pkg_count:
        lines.append(f"\n📦 *{pkg_count}* affected package(s)")

    # Top CVEs table
    top = report.get("top_cves", [])[:10]
    if top:
        lines.append("\n*Top CVEs*")
        for cve in top:
            icon = _SEV_ICON.get(cve.get("severity", "UNKNOWN"), "⚪")
            cve_id = cve.get("id", "unknown")
            pkg = cve.get("package", "?")
            installed = cve.get("installed_version", "?")
            fixed = cve.get("fixed_version", "")
            title = cve.get("title", "")[:60]
            fix_str = f" → `{fixed}`" if fixed else " (no fix)"
            lines.append(f"  {icon} `{cve_id}` — {pkg} `{installed}`{fix_str}")
            if title:
                lines.append(f"      _{title}_")

    # Status summary
    summary = generate_summary(report)
    status = summary.get("status", "unknown")
    status_map = {
        "critical": "🚨 CRITICAL — immediate action required",
        "warning": "⚠️ WARNING — review recommended",
        "clean": "✅ CLEAN — no critical or high CVEs",
    }
    lines.append(f"\n*Status:* {status_map.get(status, status)}")
    lines.append("\n_Run_ `POST /soc/v1/cve-report` _to regenerate._")

    return "\n".join(lines)


async def run_and_send_cve_report(
    bot_token: str,
    owner_chat_id: str,
    base_url: str = "https://api.telegram.org",
    scan_target: str = "/",
) -> dict[str, Any]:
    """Run a Trivy scan, format the report, and send via Telegram.

    Args:
        bot_token: Telegram Bot API token.
        owner_chat_id: Chat ID to send the report to.
        base_url: Telegram API base URL (gateway-proxied in production).
        scan_target: Filesystem path to scan.

    Returns:
        Dict with scan summary and send status.
    """
    loop = asyncio.get_event_loop()

    # Run Trivy in executor (blocking subprocess).
    report = await loop.run_in_executor(None, lambda: run_trivy_scan(target=scan_target))

    # Persist report to shared volume.
    try:
        await loop.run_in_executor(None, lambda: save_report(report))
    except Exception as exc:
        logger.warning("Failed to save Trivy report: %s", exc)

    # Format the Telegram message.
    message = format_cve_report(report)

    # Send via Telegram Bot API.
    send_ok = False
    if bot_token and owner_chat_id:
        try:
            send_ok = await _send_telegram(bot_token, owner_chat_id, message, base_url)
        except Exception as exc:
            logger.error("Failed to send CVE report via Telegram: %s", exc)

    # Record timestamp — in-memory first (disk may be full).
    _sent_dates.add(datetime.now(timezone.utc).date().isoformat())
    try:
        _LAST_REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
        _LAST_REPORT_PATH.write_text(datetime.now(timezone.utc).isoformat())
    except Exception:
        pass

    summary = generate_summary(report)
    summary["telegram_sent"] = send_ok
    summary["message_preview"] = message[:200]
    return summary


async def _send_telegram(bot_token: str, chat_id: str, text: str, base_url: str) -> bool:
    """Send a message via Telegram Bot API. Returns True on success."""
    url = f"{base_url}/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown",
        "disable_web_page_preview": True,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    loop = asyncio.get_event_loop()
    resp = await loop.run_in_executor(
        None,
        lambda: urllib.request.urlopen(req, timeout=30),
    )
    result = json.loads(resp.read().decode("utf-8"))
    if result.get("ok"):
        logger.info("CVE report sent to chat_id=%s", chat_id)
        return True
    logger.warning("Telegram sendMessage failed: %s", result)
    return False


async def cve_report_scheduler(
    bot_token: str,
    owner_chat_id: str,
    base_url: str = "https://api.telegram.org",
    report_hour: int = 6,
) -> None:
    """Background loop: sends one CVE report per day at ``report_hour`` UTC.

    Runs forever; designed to be launched via ``asyncio.create_task()``.
    Skips if a report was already sent today (checked via _LAST_REPORT_PATH).
    """
    while True:
        try:
            now = datetime.now(timezone.utc)
            today_str = now.date().isoformat()

            # Next trigger: today at report_hour, or tomorrow if already past/sent.
            target = now.replace(hour=report_hour, minute=0, second=0, microsecond=0)
            already_sent = today_str in _sent_dates or _already_sent_today(now)

            if now >= target:
                if already_sent:
                    # Sleep until tomorrow's report_hour (timedelta avoids month-end overflow).
                    target = (target + timedelta(days=1)).replace(
                        hour=report_hour, minute=0, second=0, microsecond=0
                    )
                # else: trigger immediately (first run of the day).
            elif already_sent:
                # Sent today but target is still in the future — shouldn't happen, but be safe.
                target = (target + timedelta(days=1)).replace(
                    hour=report_hour, minute=0, second=0, microsecond=0
                )

            sleep_secs = max(0, (target - now).total_seconds())
            if sleep_secs > 0:
                logger.info(
                    "CVE report scheduler: next report in %.0f seconds (at %s UTC)",
                    sleep_secs,
                    target.strftime("%H:%M"),
                )
                await asyncio.sleep(sleep_secs)

            # Re-check after waking — another task may have sent while we slept.
            now = datetime.now(timezone.utc)
            today_str = now.date().isoformat()
            if today_str in _sent_dates or _already_sent_today(now):
                logger.info("CVE report already sent today, skipping.")
                continue

            logger.info("Running daily CVE report...")
            result = await run_and_send_cve_report(
                bot_token=bot_token,
                owner_chat_id=owner_chat_id,
                base_url=base_url,
            )
            logger.info(
                "Daily CVE report complete: %d findings, telegram_sent=%s",
                result.get("findings", 0),
                result.get("telegram_sent"),
            )
        except asyncio.CancelledError:
            logger.info("CVE report scheduler cancelled")
            return
        except Exception as exc:
            logger.error("CVE report scheduler error: %s", exc, exc_info=True)
            # Retry in 1 hour on failure — but record today so we don't spam.
            _sent_dates.add(datetime.now(timezone.utc).date().isoformat())
            await asyncio.sleep(3600)


def _already_sent_today(now: datetime) -> bool:
    """Check if a Trivy report was already sent today (disk-based, secondary to _sent_dates)."""
    try:
        if _LAST_REPORT_PATH.exists():
            last = datetime.fromisoformat(_LAST_REPORT_PATH.read_text().strip())
            return last.date() == now.date()
    except Exception:
        pass
    return False


def _already_checked_upstream_today(now: datetime) -> bool:
    """Check if the upstream CVE watch already ran today (disk-based)."""
    try:
        if _LAST_UPSTREAM_CHECK_PATH.exists():
            last = datetime.fromisoformat(_LAST_UPSTREAM_CHECK_PATH.read_text().strip())
            return last.date() == now.date()
    except Exception:
        pass
    return False


# ── Upstream CVE watch ────────────────────────────────────────────────────────


def check_upstream_cves(github_token: Optional[str] = None) -> list[dict[str, Any]]:
    """Fetch OpenClaw GitHub Security Advisories and return CVEs not in the registry.

    Calls the GitHub Security Advisories API for the wrapped agent repo, extracts
    CVE IDs, and returns entries whose IDs are absent from AGENT_CVE_REGISTRY.

    Args:
        github_token: Optional GitHub personal access token or fine-grained token
            with ``repo`` read scope. Without a token the API allows 60 req/hour
            per source IP — sufficient for a daily check.

    Returns:
        List of dicts with keys: id, summary, severity, cvss, published_at, html_url.

    Raises:
        urllib.error.URLError / OSError: on network failure.
        json.JSONDecodeError: if the API response is malformed.
    """
    from .agent_cve_registry import AGENT_CVE_REGISTRY

    known_ids: set[str] = {c["id"] for c in AGENT_CVE_REGISTRY}

    url = (
        f"https://api.github.com/repos/{_OPENCLAW_GITHUB_REPO}"
        "/security-advisories?per_page=100"
    )
    headers: dict[str, str] = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "AgentShroud-CVE-Watch/1.0",
    }
    if github_token:
        headers["Authorization"] = f"Bearer {github_token}"

    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        advisories: list[dict[str, Any]] = json.loads(resp.read().decode("utf-8"))

    new_cves: list[dict[str, Any]] = []
    for adv in advisories:
        cve_id: Optional[str] = adv.get("cve_id")
        if not cve_id or cve_id in known_ids:
            continue
        cvss_block: dict[str, Any] = adv.get("cvss") or {}
        new_cves.append(
            {
                "id": cve_id,
                "summary": adv.get("summary", ""),
                "severity": (adv.get("severity") or "UNKNOWN").upper(),
                "cvss": cvss_block.get("score"),
                "published_at": adv.get("published_at", ""),
                "html_url": adv.get("html_url", ""),
            }
        )

    return new_cves


def format_upstream_cve_alert(new_cves: list[dict[str, Any]]) -> str:
    """Format a Telegram alert for newly detected upstream CVEs.

    Args:
        new_cves: List of CVE dicts from ``check_upstream_cves()``.

    Returns:
        Markdown string suitable for Telegram ``parse_mode=Markdown``.
    """
    count = len(new_cves)
    plural = "s" if count > 1 else ""
    lines = [
        f"🚨 *AgentShroud™ — {count} New OpenClaw CVE{plural} Detected*",
        f"_{count} CVE{plural} not yet in the AgentShroud registry_\n",
    ]
    for cve in new_cves:
        icon = _SEV_ICON.get(cve.get("severity", "UNKNOWN"), "⚪")
        cvss_str = f"CVSS {cve['cvss']}" if cve.get("cvss") else cve.get("severity", "UNKNOWN")
        lines.append(f"{icon} `{cve['id']}` ({cvss_str})")
        summary = (cve.get("summary") or "")[:80]
        if summary:
            lines.append(f"    _{summary}_")
        pub = (cve.get("published_at") or "")[:10]
        if pub:
            lines.append(f"    📅 Disclosed: {pub}")
        lines.append("")

    lines.append(
        "⚠️ *Action required:* triage and add to `gateway/security/agent_cve_registry.py`"
    )
    return "\n".join(lines)


async def run_upstream_cve_check(
    bot_token: str,
    owner_chat_id: str,
    base_url: str = "https://api.telegram.org",
    github_token: Optional[str] = None,
) -> dict[str, Any]:
    """Fetch upstream CVEs, alert via Telegram if new ones are found.

    Args:
        bot_token: Telegram Bot API token.
        owner_chat_id: Chat ID to send the alert to.
        base_url: Telegram API base URL (gateway-proxied in production).
        github_token: Optional GitHub token for higher API rate limits.

    Returns:
        Dict with keys: new_cves (int), cve_ids (list), telegram_sent (bool),
        and optionally error (str).
    """
    loop = asyncio.get_event_loop()

    try:
        new_cves = await loop.run_in_executor(
            None, lambda: check_upstream_cves(github_token)
        )
    except Exception as exc:
        logger.error("Upstream CVE check failed: %s", exc)
        return {"new_cves": 0, "cve_ids": [], "telegram_sent": False, "error": str(exc)}

    result: dict[str, Any] = {
        "new_cves": len(new_cves),
        "cve_ids": [c["id"] for c in new_cves],
        "telegram_sent": False,
    }

    if not new_cves:
        logger.info("Upstream CVE check: registry is current (no new CVEs found)")
        return result

    logger.warning(
        "Upstream CVE check: %d new CVE(s) detected: %s",
        len(new_cves),
        result["cve_ids"],
    )

    if bot_token and owner_chat_id:
        try:
            message = format_upstream_cve_alert(new_cves)
            result["telegram_sent"] = await _send_telegram(
                bot_token, owner_chat_id, message, base_url
            )
        except Exception as exc:
            logger.error("Failed to send upstream CVE alert via Telegram: %s", exc)

    return result


async def upstream_cve_check_scheduler(
    bot_token: str,
    owner_chat_id: str,
    base_url: str = "https://api.telegram.org",
    report_hour: int = 6,
    github_token: Optional[str] = None,
) -> None:
    """Background loop: checks for new upstream agent CVEs once per day at report_hour UTC.

    Runs 5 minutes after the Trivy report hour to avoid thundering-herd on the
    Telegram Bot API. Designed to be launched via ``asyncio.create_task()``.
    """
    # Offset by 5 minutes from the Trivy report so both messages don't land simultaneously.
    _CHECK_MINUTE = 5

    while True:
        try:
            now = datetime.now(timezone.utc)
            today_str = now.date().isoformat()

            target = now.replace(
                hour=report_hour, minute=_CHECK_MINUTE, second=0, microsecond=0
            )
            already_checked = (
                today_str in _upstream_check_dates
                or _already_checked_upstream_today(now)
            )

            if now >= target:
                if already_checked:
                    target = (target + timedelta(days=1)).replace(
                        hour=report_hour, minute=_CHECK_MINUTE, second=0, microsecond=0
                    )
                # else: trigger immediately (first run of the day after offset window).
            elif already_checked:
                target = (target + timedelta(days=1)).replace(
                    hour=report_hour, minute=_CHECK_MINUTE, second=0, microsecond=0
                )

            sleep_secs = max(0.0, (target - now).total_seconds())
            if sleep_secs > 0:
                logger.info(
                    "Upstream CVE check scheduler: next check in %.0f seconds (at %s UTC)",
                    sleep_secs,
                    target.strftime("%H:%M"),
                )
                await asyncio.sleep(sleep_secs)

            # Re-check after waking — guard against duplicate runs.
            now = datetime.now(timezone.utc)
            today_str = now.date().isoformat()
            if today_str in _upstream_check_dates or _already_checked_upstream_today(now):
                logger.info("Upstream CVE check already done today, skipping.")
                continue

            logger.info("Running upstream CVE check...")
            result = await run_upstream_cve_check(
                bot_token=bot_token,
                owner_chat_id=owner_chat_id,
                base_url=base_url,
                github_token=github_token,
            )

            # Record completion — in-memory first (disk may be full).
            _upstream_check_dates.add(datetime.now(timezone.utc).date().isoformat())
            try:
                _LAST_UPSTREAM_CHECK_PATH.parent.mkdir(parents=True, exist_ok=True)
                _LAST_UPSTREAM_CHECK_PATH.write_text(
                    datetime.now(timezone.utc).isoformat()
                )
            except Exception:
                pass

            logger.info(
                "Upstream CVE check complete: %d new CVE(s), telegram_sent=%s",
                result.get("new_cves", 0),
                result.get("telegram_sent"),
            )

        except asyncio.CancelledError:
            logger.info("Upstream CVE check scheduler cancelled")
            return
        except Exception as exc:
            logger.error(
                "Upstream CVE check scheduler error: %s", exc, exc_info=True
            )
            # Record today so we don't loop and spam on persistent errors.
            _upstream_check_dates.add(datetime.now(timezone.utc).date().isoformat())
            await asyncio.sleep(3600)
