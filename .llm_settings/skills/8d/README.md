# 8D Root Cause Analysis

**Command:** `/8d` (Claude Code) | paste `.gemini/agents/8d.md` (Gemini/Codex)
**Platforms:** Claude Code (native `/skill`) | Gemini CLI, Codex CLI (paste agent file)

## Purpose

Use this skill when performing root cause analysis on incidents in battery energy storage systems (BESS) and industrial control systems. Triggers include: any mention of 'root cause', 'RCA', '8D', 'incident analysis', 'fault analysis', 'error investigation', 'correlated events', 'anomaly detection', or when a user provides an Array ID, timestamp, and error data point for investigation. This skill follows the 8D (Eight Disciplines) methodology adapted for data-driven analysis of control system incidents. It integrates with AWS Athena for querying telemetry, metadata, and configuration data. No source code analysis is performed — all investigation is conducted through operational data, device metadata, and optionally XML configuration files that describe device relationships and system topology.

## Usage

Invoke with `/8d` in Claude Code, or `@8d` in Gemini/Codex CLI.

## Related Skills

See [SKILLS_GUIDE.md](../reference/SKILLS_GUIDE.md) for the complete skill catalog.
