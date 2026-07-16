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
from typing import Any, Dict, List, Optional

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

# Telegram sendMessage caps the ``text`` field at 4096 UTF-16 code units. We keep a
# safety margin below that so no formatted alert can ever return HTTP 400 (Bad
# Request: message is too long). Applied both when building the upstream CVE
# summary and as a defensive final guard in ``_send_telegram``.
_TELEGRAM_MAX_CHARS = 4096
_TELEGRAM_SAFE_CHARS = 4000

# Upstream CVE alert lists at most this many GHSA ids inline; the remainder are
# folded into an "…and N more" indicator so the message stays under the cap
# regardless of how many new advisories a single sync discovers.
_UPSTREAM_ALERT_MAX_ITEMS = 15

# Path to store the last report timestamp so we avoid duplicate sends on restart.
_LAST_REPORT_PATH = Path("/var/log/security/trivy/.last_cve_report")
_LAST_UPSTREAM_CHECK_PATH = Path("/var/log/security/trivy/.last_upstream_cve_check")
_LAST_GHSA_INGEST_PATH = Path("/var/log/security/trivy/.last_ghsa_ingest")

# In-memory guards: track dates already processed this process lifetime.
# Prevents infinite send loops when the disk is full and the paths can't be written.
_sent_dates: set[str] = set()
_upstream_check_dates: set[str] = set()
_ghsa_ingest_dates: set[str] = set()


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


def _build_image_targets() -> List[str]:
    """Build the list of container image targets for Trivy image scanning.

    Combines the gateway image and env-var-configured images (AGENTSHROUD_TRIVY_IMAGES).
    Deduplicates while preserving order.
    """
    gateway_image = "agentshroud-gateway:latest"
    env_images: List[str] = [
        t.strip()
        for t in os.environ.get("AGENTSHROUD_TRIVY_IMAGES", "").split(",")
        if t.strip()
    ]
    seen: Dict[str, None] = {}
    for img in [gateway_image] + env_images:
        seen[img] = None
    return list(seen.keys())


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

    # Run Trivy filesystem scan in executor (blocking subprocess).
    report = await loop.run_in_executor(
        None, lambda: run_trivy_scan(target=scan_target)
    )

    # Persist report to shared volume.
    try:
        await loop.run_in_executor(None, lambda: save_report(report))
    except Exception as exc:
        logger.warning("Failed to save Trivy report: %s", exc)

    # Run image scans and collect per-image summaries for the digest.
    image_scan_lines: List[str] = []
    image_targets = _build_image_targets()
    for image_target in image_targets:
        try:
            _img = image_target  # capture for lambda
            img_report = await loop.run_in_executor(
                None,
                lambda _t=_img: run_trivy_scan(scan_type="image", target=_t),
            )
            try:
                await loop.run_in_executor(
                    None,
                    lambda r=img_report: save_report(
                        r,
                        report_prefix=f"image-{_img.replace(':', '-').replace('/', '-')}-",
                    ),
                )
            except Exception as save_exc:
                logger.warning(
                    "Failed to save Trivy image report for %s: %s",
                    image_target,
                    save_exc,
                )
            if img_report.get("error"):
                image_scan_lines.append(
                    f"🖼 `{image_target}`: scan error — `{img_report['error']}`"
                )
            else:
                n = img_report.get("total_vulnerabilities", 0)
                crit = (img_report.get("by_severity") or {}).get("CRITICAL", 0)
                high = (img_report.get("by_severity") or {}).get("HIGH", 0)
                icon = "🔴" if crit > 0 else "🟠" if high > 0 else "✅"
                image_scan_lines.append(
                    f"{icon} `{image_target}`: {n} finding(s)"
                    + (f" (CRIT:{crit} HIGH:{high})" if crit or high else "")
                )
        except Exception as exc:
            logger.warning("Image scan failed for %s: %s", image_target, exc)
            image_scan_lines.append(f"🖼 `{image_target}`: scan failed — `{exc}`")

    # Format the Telegram message.
    message = format_cve_report(report)

    # Append image scan summary section.
    if image_scan_lines:
        message = (
            message + "\n\n*Container Image Scans*\n" + "\n".join(image_scan_lines)
        )

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
    summary["image_scans"] = image_scan_lines
    return summary


async def _send_telegram(
    bot_token: str, chat_id: str, text: str, base_url: str
) -> bool:
    """Send a message via Telegram Bot API. Returns True on success.

    ``text`` is defensively truncated to ``_TELEGRAM_SAFE_CHARS`` with a clear
    marker so that no caller can ever trigger an HTTP 400 ("message is too long")
    from an over-length payload.
    """
    if len(text) > _TELEGRAM_MAX_CHARS:
        marker = "\n…(truncated)"
        text = text[: _TELEGRAM_SAFE_CHARS - len(marker)] + marker
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


def check_upstream_cves(
    github_token: Optional[str] = None, agent_id: str = "openclaw"
) -> list[dict[str, Any]]:
    """Fetch one agent's GitHub Security Advisories and return advisories we don't track.

    Each wrapped agent has a COMPLETELY SEPARATE pipeline: this function fetches
    *only* ``agent_id``'s own upstream advisory repo and diffs *only* against
    ``agent_id``'s own registry list.  OpenClaw and Hermes never cross-check or
    share state — call this once per agent (see ``run_upstream_cve_check``).

    The registry's source-of-truth identifier is the **GHSA id** — the registry's
    own ``id`` field is a synthetic AgentShroud ref (``ASH-OCLAW-NNN`` /
    ``ASH-HERMES-NNN``) and is NOT comparable to upstream advisory ids.  An
    advisory is reported as "new" only when its ``ghsa_id`` is absent from that
    agent's set of tracked GHSA ids.  As a fallback, an advisory that carries a
    real ``cve_id`` already tracked in the same agent's registry is treated as
    known even if its GHSA id is not yet recorded.

    Args:
        github_token: Optional GitHub personal access token or fine-grained token
            with ``repo`` read scope. Without a token the API allows 60 req/hour
            per source IP — sufficient for a daily check.
        agent_id: Which wrapped agent to check (``"openclaw"`` / ``"hermes"``).
            Selects that agent's OWN registry list and OWN upstream repo.

    Returns:
        List of dicts with keys: id (the upstream GHSA id), ghsa_id, cve_id,
        summary, severity, cvss, published_at, html_url.

    Raises:
        urllib.error.URLError / OSError: on network failure.
        json.JSONDecodeError: if the API response is malformed.
        KeyError: if *agent_id* is not a registered agent.
    """
    from .agent_cve_registry import _AGENT_CVE_REGISTRIES, get_agent_ghsa_repo

    # This agent's OWN registry list — never merged with any other agent's.
    registry = _AGENT_CVE_REGISTRIES[agent_id]
    repo = get_agent_ghsa_repo(agent_id)

    # GHSA ids are the source of truth for "already tracked".
    known_ghsa: set[str] = {c["ghsa_id"] for c in registry if c.get("ghsa_id")}
    known_cve: set[str] = {c["cve_id"] for c in registry if c.get("cve_id")}

    url = f"https://api.github.com/repos/{repo}/security-advisories?per_page=100"
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
        ghsa_id: Optional[str] = adv.get("ghsa_id")
        if not ghsa_id:
            # No GHSA id means we cannot key it to the registry — skip.
            continue
        cve_id: Optional[str] = adv.get("cve_id")
        if ghsa_id in known_ghsa:
            continue
        if cve_id and cve_id in known_cve:
            # Already tracked under its CVE id; not a new advisory.
            continue
        cvss_block: dict[str, Any] = adv.get("cvss") or {}
        new_cves.append(
            {
                # Report the GHSA id as the primary identifier (source of truth).
                "id": ghsa_id,
                "ghsa_id": ghsa_id,
                "cve_id": cve_id,
                "summary": adv.get("summary", ""),
                "severity": (adv.get("severity") or "UNKNOWN").upper(),
                "cvss": cvss_block.get("score"),
                "published_at": adv.get("published_at", ""),
                "html_url": adv.get("html_url", ""),
            }
        )

    return new_cves


def format_upstream_cve_alert(
    new_cves: list[dict[str, Any]], agent_label: str = "OpenClaw"
) -> str:
    """Format a Telegram alert for newly detected upstream CVEs.

    The alert is titled for a specific wrapped agent (*agent_label*) so OpenClaw
    and Hermes each get their own independent, clearly-labelled alert.

    The alert is a bounded *summary*: it lists at most ``_UPSTREAM_ALERT_MAX_ITEMS``
    advisories inline (severity icon + GHSA id + CVSS/severity), then folds any
    remainder into an "…and N more" indicator. This keeps the message well under
    Telegram's 4096-char ``sendMessage`` limit even when a single sync discovers
    ~100 new GHSA advisories — the historical HTTP 400 ("message is too long")
    failure. A final hard cap truncates defensively should the total still exceed
    the safe budget.

    Args:
        new_cves: List of CVE dicts from ``check_upstream_cves()``.

    Returns:
        Markdown string suitable for Telegram ``parse_mode=Markdown``, guaranteed
        to be at most ``_TELEGRAM_MAX_CHARS`` characters.
    """
    count = len(new_cves)
    plural = "s" if count > 1 else ""
    shown = new_cves[:_UPSTREAM_ALERT_MAX_ITEMS]
    remaining = count - len(shown)

    lines = [
        f"🚨 *AgentShroud™ — {count} New {agent_label} CVE{plural} Detected*",
        f"_{count} CVE{plural} not yet in the AgentShroud registry_\n",
    ]
    for cve in shown:
        icon = _SEV_ICON.get(cve.get("severity", "UNKNOWN"), "⚪")
        cvss_str = (
            f"CVSS {cve['cvss']}" if cve.get("cvss") else cve.get("severity", "UNKNOWN")
        )
        lines.append(f"{icon} `{cve['id']}` ({cvss_str})")

    if remaining > 0:
        lines.append(f"\n…and {remaining} more (see dashboard / CVE report)")

    lines.append(
        "\nℹ️ Auto-registered as *under_review* (honest — NOT claimed mitigated) "
        "by the daily sync. Triage status at `/soc/v1/agent-cves`."
    )
    message = "\n".join(lines)

    # Defensive hard cap: even with the item limit above, guarantee the summary
    # can never exceed Telegram's limit (e.g. pathologically long GHSA ids).
    if len(message) > _TELEGRAM_SAFE_CHARS:
        message = (
            message[: _TELEGRAM_SAFE_CHARS - len("\n…(truncated)")] + "\n…(truncated)"
        )
    return message


async def run_upstream_cve_check(
    bot_token: str,
    owner_chat_id: str,
    base_url: str = "https://api.telegram.org",
    github_token: Optional[str] = None,
    agent_id: str = "openclaw",
    always_report_zero: bool = False,
) -> dict[str, Any]:
    """Fetch one agent's upstream CVEs, alert via Telegram, honestly.

    Runs a single wrapped agent's independent pipeline: fetch *its* repo, diff vs
    *its* registry, alert with *its* label.  Call once per agent (the scheduler
    loops over registered agents) so OpenClaw and Hermes reports never mix.

    Args:
        bot_token: Telegram Bot API token.
        owner_chat_id: Chat ID to send the alert to.
        base_url: Telegram API base URL (gateway-proxied in production).
        github_token: Optional GitHub token for higher API rate limits.
        agent_id: Which wrapped agent to check (``"openclaw"`` / ``"hermes"``).
        always_report_zero: When True, send a short "0 new" Telegram note even
            when the agent has no new advisories.  The owner explicitly wants to
            SEE a Hermes report even when its feed is empty — this proves the
            pipeline is live and agent-agnostic.  Defaults to False (silence when
            nothing new, the historical OpenClaw behavior).

    Returns:
        Dict with keys: agent_id (str), new_cves (int), cve_ids (list),
        telegram_sent (bool), and optionally error (str).
    """
    from .agent_cve_registry import get_agent_cve_source

    try:
        agent_label = get_agent_cve_source(agent_id)["alert_title"]
    except KeyError:
        agent_label = agent_id.capitalize()

    loop = asyncio.get_event_loop()

    try:
        new_cves = await loop.run_in_executor(
            None, lambda: check_upstream_cves(github_token, agent_id)
        )
    except Exception as exc:
        logger.error("Upstream CVE check failed for %s: %s", agent_id, exc)
        return {
            "agent_id": agent_id,
            "new_cves": 0,
            "cve_ids": [],
            "telegram_sent": False,
            "error": str(exc),
        }

    result: dict[str, Any] = {
        "agent_id": agent_id,
        "new_cves": len(new_cves),
        "cve_ids": [c["id"] for c in new_cves],
        "telegram_sent": False,
    }

    if not new_cves:
        logger.info(
            "Upstream CVE check (%s): registry is current (no new CVEs found)", agent_id
        )
        if always_report_zero and bot_token and owner_chat_id:
            try:
                message = (
                    f"✅ *AgentShroud™ — {agent_label} CVE watch*\n"
                    f"_0 new advisories._ Registry is current; the "
                    f"{agent_label} pipeline is live and monitoring its own "
                    f"upstream feed independently."
                )
                result["telegram_sent"] = await _send_telegram(
                    bot_token, owner_chat_id, message, base_url
                )
            except Exception as exc:
                logger.error(
                    "Failed to send %s zero-CVE note via Telegram: %s", agent_id, exc
                )
        return result

    logger.warning(
        "Upstream CVE check (%s): %d new CVE(s) detected: %s",
        agent_id,
        len(new_cves),
        result["cve_ids"],
    )

    if bot_token and owner_chat_id:
        try:
            message = format_upstream_cve_alert(new_cves, agent_label)
            result["telegram_sent"] = await _send_telegram(
                bot_token, owner_chat_id, message, base_url
            )
        except Exception as exc:
            logger.error(
                "Failed to send %s upstream CVE alert via Telegram: %s", agent_id, exc
            )

    return result


# Agents whose report is sent even when they have zero new advisories, so the
# owner can SEE that the pipeline is live for that agent (agent-agnostic proof).
# Hermes's upstream (nousresearch/hermes-agent) currently publishes 0 advisories.
_ALWAYS_REPORT_ZERO_AGENTS: frozenset[str] = frozenset({"hermes"})


async def run_upstream_cve_check_all_agents(
    bot_token: str,
    owner_chat_id: str,
    base_url: str = "https://api.telegram.org",
    github_token: Optional[str] = None,
) -> list[dict[str, Any]]:
    """Run the upstream CVE check for EVERY registered agent, independently.

    Iterates the per-agent CVE config (``list_cve_agents``) and runs each agent's
    fully separate pipeline in turn: OpenClaw checks ``openclaw/openclaw`` vs the
    OpenClaw registry; Hermes checks ``nousresearch/hermes-agent`` vs the Hermes
    registry.  No shared state, no combined counters, no cross-agent dedup — each
    agent produces its own result dict and its own Telegram alert.  A failure in
    one agent's check never blocks another agent's report.

    Returns:
        A list of per-agent result dicts (one per registered agent), each as
        returned by :func:`run_upstream_cve_check`.
    """
    from .agent_cve_registry import list_cve_agents

    results: list[dict[str, Any]] = []
    for agent_id in list_cve_agents():
        try:
            result = await run_upstream_cve_check(
                bot_token=bot_token,
                owner_chat_id=owner_chat_id,
                base_url=base_url,
                github_token=github_token,
                agent_id=agent_id,
                always_report_zero=agent_id in _ALWAYS_REPORT_ZERO_AGENTS,
            )
        except Exception as exc:  # isolate: one agent's failure never blocks another
            logger.error("Per-agent CVE check failed for %s: %s", agent_id, exc)
            result = {
                "agent_id": agent_id,
                "new_cves": 0,
                "cve_ids": [],
                "telegram_sent": False,
                "error": str(exc),
            }
        results.append(result)
    return results


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
            if today_str in _upstream_check_dates or _already_checked_upstream_today(
                now
            ):
                logger.info("Upstream CVE check already done today, skipping.")
                continue

            logger.info("Running upstream CVE check (per-agent)...")
            results = await run_upstream_cve_check_all_agents(
                bot_token=bot_token,
                owner_chat_id=owner_chat_id,
                base_url=base_url,
                github_token=github_token,
            )
            result = {
                "new_cves": sum(r.get("new_cves", 0) for r in results),
                "telegram_sent": any(r.get("telegram_sent") for r in results),
            }

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
            logger.error("Upstream CVE check scheduler error: %s", exc, exc_info=True)
            # Record today so we don't loop and spam on persistent errors.
            _upstream_check_dates.add(datetime.now(timezone.utc).date().isoformat())
            await asyncio.sleep(3600)


# ── GHSA source-of-truth ingest ───────────────────────────────────────────────


def _already_ingested_ghsa_today(now: datetime) -> bool:
    """Check if the GHSA ingest already ran today (disk-based, secondary guard)."""
    try:
        if _LAST_GHSA_INGEST_PATH.exists():
            last = datetime.fromisoformat(_LAST_GHSA_INGEST_PATH.read_text().strip())
            return last.date() == now.date()
    except Exception:
        pass
    return False


async def ghsa_ingest_scheduler(
    bot_token: str,
    owner_chat_id: str,
    base_url: str = "https://api.telegram.org",
    ingest_hour: int = 7,
    github_token: Optional[str] = None,
) -> None:
    """Background loop: pull the GHSA feed as source of truth once per day.

    This is a *distinct* daily task from ``upstream_cve_check_scheduler`` — it
    runs at its own configurable UTC hour (``AGENTSHROUD_GHSA_INGEST_HOUR``,
    default 07:00) and treats the GitHub Security-Advisory GHSA ids as the
    authoritative set.  It reports genuinely-new advisories (GHSA ids absent from
    the registry) via ``run_upstream_cve_check``, which now diffs on ``ghsa_id``.

    Kept separate from the CVE-report / upstream-check schedulers so a GHSA feed
    refresh can be scheduled independently of the Trivy digest cadence.  Designed
    to be launched via ``asyncio.create_task()``.
    """
    while True:
        try:
            now = datetime.now(timezone.utc)
            today_str = now.date().isoformat()

            target = now.replace(hour=ingest_hour, minute=0, second=0, microsecond=0)
            already = today_str in _ghsa_ingest_dates or _already_ingested_ghsa_today(
                now
            )

            if now >= target:
                if already:
                    target = (target + timedelta(days=1)).replace(
                        hour=ingest_hour, minute=0, second=0, microsecond=0
                    )
                # else: trigger immediately (first run of the day).
            elif already:
                target = (target + timedelta(days=1)).replace(
                    hour=ingest_hour, minute=0, second=0, microsecond=0
                )

            sleep_secs = max(0.0, (target - now).total_seconds())
            if sleep_secs > 0:
                logger.info(
                    "GHSA ingest scheduler: next ingest in %.0f seconds (at %s UTC)",
                    sleep_secs,
                    target.strftime("%H:%M"),
                )
                await asyncio.sleep(sleep_secs)

            now = datetime.now(timezone.utc)
            today_str = now.date().isoformat()
            if today_str in _ghsa_ingest_dates or _already_ingested_ghsa_today(now):
                logger.info("GHSA ingest already done today, skipping.")
                continue

            logger.info("Running GHSA source-of-truth ingest (per-agent)...")
            results = await run_upstream_cve_check_all_agents(
                bot_token=bot_token,
                owner_chat_id=owner_chat_id,
                base_url=base_url,
                github_token=github_token,
            )
            result = {
                "new_cves": sum(r.get("new_cves", 0) for r in results),
                "telegram_sent": any(r.get("telegram_sent") for r in results),
            }

            _ghsa_ingest_dates.add(datetime.now(timezone.utc).date().isoformat())
            try:
                _LAST_GHSA_INGEST_PATH.parent.mkdir(parents=True, exist_ok=True)
                _LAST_GHSA_INGEST_PATH.write_text(
                    datetime.now(timezone.utc).isoformat()
                )
            except Exception:
                pass

            logger.info(
                "GHSA ingest complete: %d new advisory(ies), telegram_sent=%s",
                result.get("new_cves", 0),
                result.get("telegram_sent"),
            )

        except asyncio.CancelledError:
            logger.info("GHSA ingest scheduler cancelled")
            return
        except Exception as exc:
            logger.error("GHSA ingest scheduler error: %s", exc, exc_info=True)
            _ghsa_ingest_dates.add(datetime.now(timezone.utc).date().isoformat())
            await asyncio.sleep(3600)
