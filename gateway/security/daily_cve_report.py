# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr., first used in February 2026.
"""Daily CVE Report — container vulnerability digest delivered via Telegram.

Runs Trivy against the container filesystem, formats a severity-bucketed
report with the top CVEs, and sends it to the owner via Telegram Bot API.

The report is triggered:
  1. On a daily schedule (configurable via AGENTSHROUD_CVE_REPORT_HOUR, default 06:00 UTC)
  2. On-demand via POST /soc/v1/cve-report
"""
from __future__ import annotations

import asyncio
import json
import logging
import os
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

from .trivy_report import run_trivy_scan, save_report, generate_summary, SEVERITY_ORDER

logger = logging.getLogger("agentshroud.security.daily_cve_report")

# Severity → emoji mapping for Telegram formatting.
_SEV_ICON = {
    "CRITICAL": "🔴",
    "HIGH": "🟠",
    "MEDIUM": "🟡",
    "LOW": "🟢",
    "UNKNOWN": "⚪",
}

# Path to store the last report timestamp so we avoid duplicate sends on restart.
_LAST_REPORT_PATH = Path("/var/log/security/trivy/.last_cve_report")


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
    report = await loop.run_in_executor(
        None, lambda: run_trivy_scan(target=scan_target)
    )

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

    # Record timestamp.
    try:
        _LAST_REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
        _LAST_REPORT_PATH.write_text(datetime.now(timezone.utc).isoformat())
    except Exception:
        pass

    summary = generate_summary(report)
    summary["telegram_sent"] = send_ok
    summary["message_preview"] = message[:200]
    return summary


async def _send_telegram(
    bot_token: str, chat_id: str, text: str, base_url: str
) -> bool:
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
        url, data=data,
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
            # Next trigger: today at report_hour, or tomorrow if we've already passed it.
            target = now.replace(hour=report_hour, minute=0, second=0, microsecond=0)
            if now >= target:
                # Check if we already sent today.
                if _already_sent_today(now):
                    # Sleep until tomorrow's report_hour.
                    target = target.replace(day=target.day + 1)
                # else: trigger immediately (first run of the day).

            sleep_secs = max(0, (target - now).total_seconds())
            if sleep_secs > 0:
                logger.info(
                    "CVE report scheduler: next report in %.0f seconds (at %s UTC)",
                    sleep_secs, target.strftime("%H:%M"),
                )
                await asyncio.sleep(sleep_secs)

            logger.info("Running daily CVE report...")
            result = await run_and_send_cve_report(
                bot_token=bot_token,
                owner_chat_id=owner_chat_id,
                base_url=base_url,
            )
            logger.info(
                "Daily CVE report complete: %d findings, telegram_sent=%s",
                result.get("findings", 0), result.get("telegram_sent"),
            )
        except asyncio.CancelledError:
            logger.info("CVE report scheduler cancelled")
            return
        except Exception as exc:
            logger.error("CVE report scheduler error: %s", exc, exc_info=True)
            # Retry in 1 hour on failure.
            await asyncio.sleep(3600)


def _already_sent_today(now: datetime) -> bool:
    """Check if a report was already sent today."""
    try:
        if _LAST_REPORT_PATH.exists():
            last = datetime.fromisoformat(_LAST_REPORT_PATH.read_text().strip())
            return last.date() == now.date()
    except Exception:
        pass
    return False
