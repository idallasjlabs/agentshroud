# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# AgentShroud™ is a trademark of Isaiah Dallas Jefferson, Jr. (USPTO Serial No. 99728633)
# Patent Pending — U.S. Provisional Application No. 64/018,744
# Unauthorized reproduction, distribution, or use of the AgentShroud name or brand is strictly prohibited.
"""SkillGuard — skill supply-chain scanning (SCRUM-97).

Agents in AgentShroud can install/load skills (OpenClaw skills, MCP servers,
agent definitions).  A malicious or compromised skill is a classic software
supply-chain attack vector: it runs with the agent's trust and toolset.
``skill_installation`` already routes through the approval queue
(``gateway/approval_queue/queue.py``); SkillGuard adds the automated *content
inspection* that feeds that decision — it scans a skill/MCP/agent-definition
payload BEFORE it is trusted, deployed, or loaded, and recommends
ALLOW / FLAG / BLOCK.

.. warning::

   **Scope and honesty (not security theater).**  These are regex/heuristic
   signatures.  They catch *naive, unobfuscated* forms of the patterns below
   (a plaintext ``exec(base64.b64decode(...))``, a literal ``curl … | sh``, a
   wildcard tool grant).  They do **not** perform data-flow, taint, or AST
   analysis and are trivially evadable by a determined attacker (string
   concatenation, indirect ``getattr`` dispatch, novel encodings, runtime
   assembly, non-Python payloads).  SkillGuard is **best-effort
   defense-in-depth behind the approval queue** — a fast first-pass filter that
   surfaces obvious badness for a human deploy decision.  It is **not** a
   complete supply-chain control and must not be relied on as the only gate.
   Unscannable artefacts (unreadable or oversized) are treated as untrusted and
   BLOCKED rather than silently skipped.

Design mirrors ``gateway/proxy/mcp_inspector.py``: an ``Enum`` severity ladder,
frozen ``Finding`` dataclasses, and a ``ScanResult`` that exposes ``blocked`` and
the highest severity.  Heuristics are concrete and testable — never a stub that
returns ALLOW.

Standards alignment:
- OWASP Top 10 for Agentic Applications — supply-chain / tool poisoning.
- MITRE ATLAS — ML supply-chain compromise.
- IEC 62443 FR3 (System Integrity) — inspect artefacts before trust.

Detection categories (see the ``_RULES`` table for the exact patterns):
- ``obfuscation``          — exec/eval of base64/hex-decoded blobs, opaque blobs
- ``exfiltration``         — outbound HTTP(S) posts / urlopen to external hosts
- ``exec_of_download``     — curl|wget piped into a shell interpreter
- ``shell_exec``           — subprocess(..., shell=True) / os.system with a pipe
- ``secret_access``        — reads of ssh keys, aws creds, secret files, token env
- ``path_traversal``       — ``../`` escapes and writes to system paths
- ``privilege_escalation`` — manifest grants (tool wildcards, approval bypass, sudo)
- ``known_malicious``      — reverse-shell / crypto-miner indicators
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from enum import IntEnum
from typing import Mapping

logger = logging.getLogger("agentshroud.security.skill_guard")

__all__ = [
    "Severity",
    "Recommendation",
    "Finding",
    "ScanResult",
    "SkillGuard",
    "SkillScanError",
]


class SkillScanError(ValueError):
    """Raised when SkillGuard is handed content it cannot scan."""


class Severity(IntEnum):
    """Ordered severity ladder (``IntEnum`` so comparisons work)."""

    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4


class Recommendation(IntEnum):
    """What the caller should do with the scanned skill."""

    ALLOW = 0
    FLAG = 1
    BLOCK = 2


@dataclass(frozen=True)
class Finding:
    """A single supply-chain finding within a scanned skill artefact."""

    category: str
    severity: Severity
    description: str
    location: str  # "<file>:<line>" or "<file>"
    pattern: str
    snippet: str


@dataclass
class ScanResult:
    """Aggregated result of scanning a skill file or an entire skill tree."""

    findings: list[Finding] = field(default_factory=list)

    @property
    def severity(self) -> Severity:
        """Highest severity across all findings (``NONE`` when clean)."""
        if not self.findings:
            return Severity.NONE
        return max(f.severity for f in self.findings)

    @property
    def recommendation(self) -> Recommendation:
        """ALLOW below MEDIUM, FLAG at MEDIUM/HIGH, BLOCK at CRITICAL."""
        sev = self.severity
        if sev >= Severity.CRITICAL:
            return Recommendation.BLOCK
        if sev >= Severity.MEDIUM:
            return Recommendation.FLAG
        return Recommendation.ALLOW

    @property
    def blocked(self) -> bool:
        return self.recommendation is Recommendation.BLOCK

    def extend(self, other: "ScanResult") -> None:
        self.findings.extend(other.findings)


# ---------------------------------------------------------------------------
# Detection rules
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class _Rule:
    category: str
    severity: Severity
    description: str
    pattern: "re.Pattern[str]"


def _c(expr: str) -> "re.Pattern[str]":
    return re.compile(expr, re.IGNORECASE)


# CRITICAL — active code execution of attacker-controlled / decoded content.
_RULES: tuple[_Rule, ...] = (
    # --- obfuscation: exec/eval of decoded payloads -----------------------
    _Rule(
        "obfuscation",
        Severity.CRITICAL,
        "exec/eval of a base64/hex/codec-decoded payload (obfuscated dropper)",
        _c(
            r"(?:exec|eval)\s*\(\s*(?:base64\.b64decode|codecs\.decode|bytes\.fromhex|"
            r"\w+\.decode\s*\(\s*['\"]?(?:base64|hex|rot13)|__import__\s*\(\s*['\"]base64)"
        ),
    ),
    _Rule(
        "obfuscation",
        Severity.HIGH,
        "eval/exec on a decoded/deobfuscated string",
        _c(r"(?:exec|eval)\s*\(\s*\w*decode\w*\s*\("),
    ),
    # --- exec_of_download: pipe a download straight into a shell ----------
    _Rule(
        "exec_of_download",
        Severity.CRITICAL,
        "downloads content and pipes it into a shell interpreter",
        _c(
            r"(?:curl|wget)\b[^\n|]*https?://[^\n|]*\|\s*(?:ba)?sh\b|"
            r"(?:curl|wget)\b[^\n|]*\|\s*(?:ba|z|fi)?sh\b"
        ),
    ),
    # --- exfiltration: outbound network calls -----------------------------
    _Rule(
        "exfiltration",
        Severity.HIGH,
        "outbound HTTP request (possible data exfiltration)",
        _c(
            r"requests\.(?:post|put|patch|get)\s*\(\s*['\"]https?://|"
            r"urlopen\s*\(\s*['\"]?https?://|"
            r"httpx\.(?:post|get|Client)\s*\(\s*['\"]?https?://|"
            r"socket\.create_connection\s*\("
        ),
    ),
    # --- shell_exec: shelling out with untrusted composition --------------
    _Rule(
        "shell_exec",
        Severity.HIGH,
        "subprocess/system shell execution (shell=True or os.system)",
        _c(
            r"subprocess\.(?:run|call|Popen|check_output|check_call)\s*\([^)]*shell\s*=\s*True|"
            r"\bos\.system\s*\(|\bos\.popen\s*\(|\bcommands\.getoutput\s*\("
        ),
    ),
    # --- secret_access: reading credentials / secret material -------------
    _Rule(
        "secret_access",
        Severity.HIGH,
        "reads private keys / credential files / secret material",
        _c(
            r"(?:\.ssh/id_[a-z]+|\.aws/credentials|\.aws/config|/run/secrets/|"
            r"/etc/shadow|\.netrc|\.docker/config\.json|"
            r"agentshroud-secrets|id_rsa|id_ed25519|BEGIN\s+(?:RSA\s+)?PRIVATE\s+KEY)"
        ),
    ),
    _Rule(
        "secret_access",
        Severity.MEDIUM,
        "reads secret-bearing environment variables (token/secret/password/key)",
        _c(
            r"os\.environ(?:\.get)?\s*[\[\(]\s*['\"][A-Z0-9_]*"
            r"(?:TOKEN|SECRET|PASSWORD|PASSWD|APIKEY|API_KEY|PRIVATE_KEY|CREDENTIAL)"
        ),
    ),
    # --- path_traversal ----------------------------------------------------
    _Rule(
        "path_traversal",
        Severity.HIGH,
        "path traversal escape sequence (../)",
        # Match even a single `../` — the earlier `{2,}` missed open('../secrets/key').
        # ``../`` requires the slash, so dotted names (``a.b.c``, ``from ..pkg``,
        # ``1.5``) never match: none of them contain the `./` sequence.
        _c(r"(?:\.\./)+"),
    ),
    _Rule(
        "path_traversal",
        Severity.HIGH,
        "writes to a sensitive system path",
        _c(
            r"open\s*\(\s*['\"](?:/etc/|/root/|/var/spool/cron|/usr/bin/|/usr/local/bin/|"
            r"/etc/cron\.[a-z]+/)[^'\"]*['\"]\s*,\s*['\"][wa]"
        ),
    ),
    # --- privilege_escalation: manifest / definition grants ---------------
    _Rule(
        "privilege_escalation",
        Severity.HIGH,
        "manifest grants wildcard tool/permission access",
        _c(
            r"['\"](?:tools|permissions|allow|allowFrom|scopes)['\"]\s*:\s*"
            r"(?:['\"]\*['\"]|\[\s*['\"]\*['\"])"
        ),
    ),
    _Rule(
        "privilege_escalation",
        Severity.HIGH,
        "manifest disables approval or self-elevates to high risk",
        _c(
            r"['\"](?:requires_approval|require_approval|needs_approval)['\"]\s*:\s*false|"
            r"['\"](?:high_risk|highRisk|privileged|admin)['\"]\s*:\s*true"
        ),
    ),
    _Rule(
        "privilege_escalation",
        Severity.HIGH,
        "manifest command escalates privileges (sudo/su/chmod 777)",
        _c(
            r"['\"](?:command|cmd|entrypoint)['\"]\s*:\s*['\"](?:sudo|su|doas)\b|"
            r"\bsudo\s+(?:-\w+\s+)*\S|\bchmod\s+(?:-R\s+)?[0-7]*7{2,}\b"
        ),
    ),
    # --- known_malicious ---------------------------------------------------
    _Rule(
        "known_malicious",
        Severity.CRITICAL,
        "reverse-shell indicator (dup2 stdio onto a socket / pty.spawn shell)",
        _c(
            r"os\.dup2\s*\(\s*\w+\.fileno\s*\(\s*\)\s*,\s*[012]\s*\)|"
            r"pty\.spawn\s*\(\s*['\"]?/bin/(?:ba)?sh|"
            r"/bin/(?:ba)?sh['\"]?\s*,?\s*['\"]?-i['\"]?"
        ),
    ),
    _Rule(
        "known_malicious",
        Severity.HIGH,
        "crypto-miner indicator (stratum pool / known miner)",
        _c(r"stratum\+tcp://|xmrig|minexmr|nanopool\.org|--coin\s+monero|coinhive"),
    ),
)

# Opaque-blob heuristic: a long contiguous base64/hex run with no whitespace is a
# strong obfuscation signal even without an explicit exec sink.
_BASE64_BLOB = re.compile(r"[A-Za-z0-9+/]{120,}={0,2}")
_HEX_BLOB = re.compile(r"(?:0x)?[0-9a-fA-F]{160,}")


class SkillGuard:
    """Scan skill / MCP / agent-definition payloads for supply-chain risk.

    Usage::

        guard = SkillGuard()
        result = guard.scan_file("skills/x/run.py", content)
        if result.blocked:
            reject(result)

        tree_result = guard.scan_skill_tree({name: content, ...})
        if tree_result.blocked:
            reject_deploy(tree_result)
    """

    # Cap per-file scanning to a sane size; skills are text, not blobs.
    _MAX_SCAN_BYTES = 2_000_000

    def __init__(self, rules: tuple[_Rule, ...] | None = None) -> None:
        self._rules = rules if rules is not None else _RULES

    # ------------------------------------------------------------------
    # Single artefact
    # ------------------------------------------------------------------

    def scan_file(self, name: str, content: str) -> ScanResult:
        """Scan one skill artefact (``name`` = relative path, ``content`` = text)."""
        if not isinstance(content, str):
            raise SkillScanError(
                f"SkillGuard.scan_file expects str content for {name!r}, "
                f"got {type(content).__name__}"
            )

        result = ScanResult()
        if not content:
            return result

        # Oversized artefacts cannot be fully scanned, yet deploy copies them in
        # full — an attacker can hide a payload past the cap.  Unscannable ⇒ not
        # trusted: emit a BLOCK-level finding.  We still scan the visible prefix
        # so any obvious badness inside the cap is reported alongside it.
        oversized = len(content) > self._MAX_SCAN_BYTES
        text = content[: self._MAX_SCAN_BYTES]
        lines = text.splitlines()

        if oversized:
            result.findings.append(
                Finding(
                    category="unscannable",
                    severity=Severity.CRITICAL,
                    description=(
                        f"file exceeds scan cap ({len(content)} > "
                        f"{self._MAX_SCAN_BYTES} bytes) — cannot be fully inspected, "
                        "treated as untrusted"
                    ),
                    location=name,
                    pattern="oversized_unscannable",
                    snippet=f"<{len(content)} bytes>",
                )
            )

        for rule in self._rules:
            for match in rule.pattern.finditer(text):
                line_no = text.count("\n", 0, match.start()) + 1
                snippet = self._line_at(lines, line_no)
                result.findings.append(
                    Finding(
                        category=rule.category,
                        severity=rule.severity,
                        description=rule.description,
                        location=f"{name}:{line_no}",
                        pattern=rule.pattern.pattern[:80],
                        snippet=snippet,
                    )
                )

        self._scan_opaque_blobs(name, text, lines, result)

        if result.findings:
            logger.warning(
                "SkillGuard: %d finding(s) in %s (severity=%s, recommend=%s)",
                len(result.findings),
                name,
                result.severity.name,
                result.recommendation.name,
            )
        return result

    def _scan_opaque_blobs(
        self, name: str, text: str, lines: list[str], result: ScanResult
    ) -> None:
        """Flag long opaque base64/hex runs as probable obfuscated payloads."""
        already_critical = any(
            f.category == "obfuscation" and f.severity is Severity.CRITICAL for f in result.findings
        )
        for pattern, label in ((_BASE64_BLOB, "base64"), (_HEX_BLOB, "hex")):
            match = pattern.search(text)
            if not match:
                continue
            line_no = text.count("\n", 0, match.start()) + 1
            # Elevate to HIGH if an exec/eval sink is co-present; else MEDIUM.
            severity = Severity.HIGH if already_critical else Severity.MEDIUM
            result.findings.append(
                Finding(
                    category="obfuscation",
                    severity=severity,
                    description=f"long opaque {label} blob (possible packed payload)",
                    location=f"{name}:{line_no}",
                    pattern=f"opaque_{label}_blob",
                    snippet=(match.group(0)[:40] + "…"),
                )
            )

    @staticmethod
    def _line_at(lines: list[str], line_no: int) -> str:
        idx = line_no - 1
        if 0 <= idx < len(lines):
            return lines[idx].strip()[:200]
        return ""

    # ------------------------------------------------------------------
    # Whole tree (manifest-shaped mapping of relpath -> content)
    # ------------------------------------------------------------------

    def scan_skill_tree(self, files: Mapping[str, str]) -> ScanResult:
        """Scan every file in a skill/MCP/agent tree and aggregate findings.

        ``files`` maps a manifest-style relative path (e.g.
        ``skills/graphify/SKILL.md``) to its text content — the exact shape
        produced by walking ``SkillsManifest`` source entries.
        """
        aggregate = ScanResult()
        for name in sorted(files):
            aggregate.extend(self.scan_file(name, files[name]))
        return aggregate
