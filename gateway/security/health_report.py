# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
from __future__ import annotations

# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""Security health report generator.

Aggregates data from all security tools, calculates a weighted score,
tracks history in SQLite, and generates formatted reports.
"""


import json
import logging
import sqlite3
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

DEFAULT_DB_PATH = Path("/var/log/security/health_history.db")

# Scoring weights
WEIGHTS = {
    "trivy": 0.25,
    "clamav": 0.20,
    "falco": 0.25,
    "wazuh": 0.15,
    "gateway": 0.15,
}

# Severity deductions (per finding)
SEVERITY_DEDUCTIONS = {
    "CRITICAL": 20,
    "critical": 20,
    "HIGH": 10,
    "high": 10,
    "MEDIUM": 3,
    "medium": 3,
    "LOW": 1,
    "low": 1,
}

# Grade thresholds
GRADE_THRESHOLDS = [
    (90, "A"),
    (80, "B"),
    (70, "C"),
    (60, "D"),
    (0, "F"),
]


def calculate_tool_score(summary: dict[str, Any]) -> float:
    """Calculate score for a single tool (0-100).

    Args:
        summary: Tool summary dict with critical/high/medium/low counts.

    Returns:
        Score from 0 to 100.
    """
    if summary.get("status") == "error":
        return 50.0  # Unknown = middle score

    score = 100.0
    score -= summary.get("critical", 0) * SEVERITY_DEDUCTIONS["CRITICAL"]
    score -= summary.get("high", 0) * SEVERITY_DEDUCTIONS["HIGH"]
    score -= summary.get("medium", 0) * SEVERITY_DEDUCTIONS["MEDIUM"]
    score -= summary.get("low", 0) * SEVERITY_DEDUCTIONS["LOW"]

    return max(0.0, min(100.0, score))


def calculate_overall_score(summaries: dict[str, dict[str, Any]]) -> float:
    """Calculate weighted overall security score.

    Args:
        summaries: Dict mapping tool name to summary dict.

    Returns:
        Weighted score from 0 to 100.
    """
    total_weight = 0.0
    weighted_score = 0.0

    for tool, weight in WEIGHTS.items():
        if tool in summaries:
            tool_score = calculate_tool_score(summaries[tool])
            weighted_score += tool_score * weight
            total_weight += weight

    if total_weight == 0:
        return 100.0

    return weighted_score / total_weight


def score_to_grade(score: float) -> str:
    """Convert score to letter grade.

    Args:
        score: Numeric score (0-100).

    Returns:
        Letter grade (A-F).
    """
    for threshold, grade in GRADE_THRESHOLDS:
        if score >= threshold:
            return grade
    return "F"


def init_db(db_path: Path = DEFAULT_DB_PATH) -> sqlite3.Connection:
    """Initialize the SQLite database for history tracking.

    Args:
        db_path: Path to SQLite database.

    Returns:
        Database connection.
    """
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.execute("""
        CREATE TABLE IF NOT EXISTS health_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            score REAL NOT NULL,
            grade TEXT NOT NULL,
            details TEXT NOT NULL
        )
    """)
    conn.commit()
    return conn


def save_to_history(
    score: float,
    grade: str,
    details: dict[str, Any],
    db_path: Path = DEFAULT_DB_PATH,
) -> None:
    """Save a health report to history.

    Args:
        score: Overall score.
        grade: Letter grade.
        details: Full report details.
        db_path: Path to SQLite database.
    """
    conn = init_db(db_path)
    try:
        conn.execute(
            "INSERT INTO health_history (timestamp, score, grade, details) VALUES (?, ?, ?, ?)",
            (datetime.now(timezone.utc).isoformat(), score, grade, json.dumps(details)),
        )
        conn.commit()
    finally:
        conn.close()


def get_trend(days: int = 7, db_path: Path = DEFAULT_DB_PATH) -> list[dict[str, Any]]:
    """Get score trend for the last N days.

    Args:
        days: Number of days to look back.
        db_path: Path to SQLite database.

    Returns:
        List of {timestamp, score, grade} dicts.
    """
    if not db_path.exists():
        return []

    conn = init_db(db_path)
    try:
        cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).isoformat()
        rows = conn.execute(
            "SELECT timestamp, score, grade FROM health_history WHERE timestamp >= ? ORDER BY timestamp",
            (cutoff,),
        ).fetchall()
        return [{"timestamp": r[0], "score": r[1], "grade": r[2]} for r in rows]
    finally:
        conn.close()


def generate_report(
    summaries: dict[str, dict[str, Any]],
    db_path: Path = DEFAULT_DB_PATH,
    save_history: bool = True,
) -> dict[str, Any]:
    """Generate a full health report.

    Args:
        summaries: Dict mapping tool name to summary dict.
        db_path: Path to SQLite database for history.
        save_history: Whether to save this report to history.

    Returns:
        Full report dict.
    """
    score = calculate_overall_score(summaries)
    grade = score_to_grade(score)

    # Per-tool scores
    tool_scores = {}
    for tool in WEIGHTS:
        if tool in summaries:
            tool_scores[tool] = {
                "score": calculate_tool_score(summaries[tool]),
                "weight": WEIGHTS[tool],
                "summary": summaries[tool],
            }

    trend = get_trend(days=7, db_path=db_path)

    # Recommendations
    recommendations = []
    for tool, info in tool_scores.items():
        s = info["summary"]
        if s.get("critical", 0) > 0:
            recommendations.append(
                f"🔴 {tool.upper()}: {s['critical']} CRITICAL findings — immediate action required"
            )
        if s.get("high", 0) > 0:
            recommendations.append(
                f"🟠 {tool.upper()}: {s['high']} HIGH findings — review soon"
            )

    if not recommendations:
        recommendations.append("✅ No critical or high findings — looking good!")

    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "overall_score": round(score, 1),
        "grade": grade,
        "tool_scores": tool_scores,
        "trend": trend,
        "recommendations": recommendations,
        "total_findings": sum(s.get("findings", 0) for s in summaries.values()),
        "total_critical": sum(s.get("critical", 0) for s in summaries.values()),
        "total_high": sum(s.get("high", 0) for s in summaries.values()),
    }

    if save_history:
        try:
            save_to_history(score, grade, report, db_path)
        except Exception as e:
            logger.warning("Failed to save health history: %s", e)

    return report


def format_report(report: dict[str, Any]) -> str:
    """Format a health report as a human-readable string.

    Args:
        report: Full report dict from generate_report().

    Returns:
        Formatted report string.
    """
    lines = [
        "🛡️ AgentShroud Security Health Report",
        f"📅 {report['timestamp'][:10]}",
        "",
        f"Overall Score: {report['overall_score']}/100 (Grade: {report['grade']})",
        f"Total Findings: {report['total_findings']} ({report['total_critical']} critical, {report['total_high']} high)",
        "",
        "── Per-Tool Summary ──",
    ]

    for tool, info in report.get("tool_scores", {}).items():
        s = info["summary"]
        status_icon = {
            "clean": "✅",
            "warning": "⚠️",
            "critical": "🔴",
            "error": "❌",
            "info": "ℹ️",
        }.get(s.get("status", ""), "❓")
        lines.append(
            f"  {status_icon} {tool.upper()}: {info['score']:.0f}/100 "
            f"(C:{s.get('critical', 0)} H:{s.get('high', 0)} M:{s.get('medium', 0)} L:{s.get('low', 0)})"
        )

    # Trend
    trend = report.get("trend", [])
    if trend:
        lines.append("")
        lines.append("── 7-Day Trend ──")
        for t in trend[-7:]:
            lines.append(f"  {t['timestamp'][:10]}: {t['score']:.0f} ({t['grade']})")

    # Recommendations
    lines.append("")
    lines.append("── Recommendations ──")
    for rec in report.get("recommendations", []):
        lines.append(f"  {rec}")

    return "\n".join(lines)
