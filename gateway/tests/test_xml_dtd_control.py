# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""Gateway XML DTD/entity control — CLAUDE.md 0.05 arm 2.

CVE-2026-6653 is a use-after-free in libxml2's xmlParseInternalSubset, CVSS 9.8,
with NO fixed version in ANY Debian release as of 2026-09-25 (present on both
bookworm and trixie). The vendor fix does not exist, so arm 1 is unavailable and
the gateway has to stop the input reaching a proxied agent's parser — whatever
libxml2 that agent happens to carry.

These tests assert the control BLOCKS rather than flags. Every other content
finding in this scanner is advisory, which is correct for prompt-injection
scoring; it is wrong for a memory-safety bug the agent cannot defend against,
because a flag that still delivers the document delivers the exploit with it.
"""
from __future__ import annotations

import unittest

from gateway.proxy.web_content_scanner import (
    FindingSeverity,
    WebContentScanner,
)


class TestDangerousXMLDetection(unittest.TestCase):
    def setUp(self) -> None:
        self.scanner = WebContentScanner()

    def test_doctype_internal_subset_detected(self) -> None:
        """The '[' block inside DOCTYPE is what xmlParseInternalSubset parses."""
        content = '<?xml version="1.0"?><!DOCTYPE foo [ <!ELEMENT foo ANY> ]><foo/>'
        result = self.scanner.scan(content, "application/xml")
        self.assertTrue(result.has_dangerous_xml)
        finding = next(f for f in result.findings if f.category == "dangerous_xml")
        self.assertEqual(finding.severity, FindingSeverity.CRITICAL)

    def test_entity_declaration_detected(self) -> None:
        """Entity declarations carry both XXE and billion-laughs."""
        content = '<!DOCTYPE d [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]><d>&xxe;</d>'
        result = self.scanner.scan(content, "application/xml")
        self.assertTrue(result.has_dangerous_xml)

    def test_external_dtd_reference_detected(self) -> None:
        """No internal subset, but still pulls a remote DTD."""
        content = '<?xml version="1.0"?><!DOCTYPE note SYSTEM "http://evil/n.dtd"><note/>'
        result = self.scanner.scan(content, "text/xml")
        self.assertTrue(result.has_dangerous_xml)

    def test_billion_laughs_detected(self) -> None:
        content = (
            '<!DOCTYPE lolz [ <!ENTITY lol "lol">'
            ' <!ENTITY lol2 "&lol;&lol;&lol;"> ]><lolz>&lol2;</lolz>'
        )
        result = self.scanner.scan(content, "application/xml")
        self.assertTrue(result.has_dangerous_xml)

    # ── The control must not fire on ordinary documents ──────────────────────
    def test_plain_xml_not_flagged(self) -> None:
        """A document with no DTD is untouched — this must not break feeds."""
        content = '<?xml version="1.0"?><rss version="2.0"><channel/></rss>'
        result = self.scanner.scan(content, "application/xml")
        self.assertFalse(result.has_dangerous_xml)

    def test_plain_html_not_flagged(self) -> None:
        """HTML5's bare <!DOCTYPE html> has no internal subset and is harmless."""
        content = "<!DOCTYPE html><html><body><p>hello</p></body></html>"
        result = self.scanner.scan(content, "text/html")
        self.assertFalse(result.has_dangerous_xml)

    def test_json_not_flagged(self) -> None:
        result = self.scanner.scan('{"a": 1}', "application/json")
        self.assertFalse(result.has_dangerous_xml)

    # ── Content-type is a hint from the origin, not a guarantee ──────────────
    def test_detected_when_mislabelled_as_text(self) -> None:
        """An attacker controls the Content-Type header, so sniff the body."""
        content = '<?xml version="1.0"?><!DOCTYPE d [ <!ENTITY e "x"> ]><d/>'
        result = self.scanner.scan(content, "text/plain")
        self.assertTrue(
            result.has_dangerous_xml,
            "a hostile origin must not evade the control by lying about Content-Type",
        )

    def test_detected_in_svg(self) -> None:
        content = '<!DOCTYPE svg [ <!ENTITY x "y"> ]><svg xmlns="http://www.w3.org/2000/svg"/>'
        result = self.scanner.scan(content, "image/svg+xml")
        self.assertTrue(result.has_dangerous_xml)

    def test_case_insensitive(self) -> None:
        content = '<?xml version="1.0"?><!doctype d [ <!entity e "x"> ]><d/>'
        result = self.scanner.scan(content, "application/xml")
        self.assertTrue(result.has_dangerous_xml)


class TestDangerousXMLIsBlockedNotFlagged(unittest.TestCase):
    """The distinction this whole control rests on."""

    def test_finding_severity_is_critical(self) -> None:
        scanner = WebContentScanner()
        content = '<!DOCTYPE d [ <!ENTITY e "x"> ]><d/>'
        result = scanner.scan(content, "application/xml")
        sev = [f.severity for f in result.findings if f.category == "dangerous_xml"]
        self.assertEqual(sev, [FindingSeverity.CRITICAL])

    def test_web_proxy_blocks_on_dangerous_xml(self) -> None:
        """Proves enforcement, not just detection."""
        import re as _re
        from pathlib import Path

        src = Path("gateway/proxy/web_proxy.py").read_text(encoding="utf-8")
        self.assertRegex(
            src,
            r"if scan\.has_dangerous_xml:",
            "web_proxy must consult the flag — a scanner nothing acts on is not a control",
        )
        block_region = src.split("if scan.has_dangerous_xml:", 1)[1][:1200]
        self.assertIn(
            "ProxyAction.BLOCK",
            block_region,
            "dangerous XML must BLOCK; FLAG still delivers the document to the parser",
        )
        self.assertTrue(
            _re.search(r"block_dangerous_xml", block_region),
            "the block must be overridable if a legitimate source needs a DTD",
        )


if __name__ == "__main__":
    unittest.main()


class TestTriageClassLevelCoverage(unittest.TestCase):
    """The durable statement is at the CLASS level, not per-CVE.

    A register entry accepts one CVE id. It cannot say "this whole class is
    compensated", so every future DTD/entity bug would need a new entry. The
    triage tool already thinks in classes, so the claim belongs there: the
    control matches the dangerous construct, not a signature, and therefore
    covers the next parser bug with no code change.
    """

    @staticmethod
    def _triage():
        import importlib.util
        import sys
        from pathlib import Path

        path = Path("scripts/triage-cve-mitigations.py")
        spec = importlib.util.spec_from_file_location("triage_mod", path)
        mod = importlib.util.module_from_spec(spec)
        # Register before exec: @dataclass resolves the module from sys.modules.
        sys.modules["triage_mod"] = mod
        spec.loader.exec_module(mod)
        return mod

    def test_libxml2_dtd_uaf_classifies_as_xxe_not_dos(self) -> None:
        """It calls itself DoS; the generic DOS profile is containment-only.

        Left as DOS it would inherit "contained, not prevented" (0.58), which
        understates a class the gateway now actually neutralises.
        """
        t = self._triage()
        cls = t.classify(
            "libxml2: Denial of Service via crafted XML input due to use-after-free",
            "Use After Free in libxml2's xmlParseInternalSubset ... improper "
            "entity resolution handling.",
        )
        self.assertEqual(cls, t.VulnClass.XXE)

    def test_xxe_class_is_covered_by_the_gateway_control(self) -> None:
        t = self._triage()
        profile = t.CLASS_PROFILE[t.VulnClass.XXE]
        self.assertEqual(profile.coverage, t.Coverage.FULL)
        self.assertIn("xml_dtd_control", profile.defense_layers)

    def test_unrelated_classes_unchanged(self) -> None:
        """The new rule runs first, so prove it does not swallow neighbours."""
        t = self._triage()
        self.assertEqual(
            t.classify("Regex denial of service", "catastrophic backtracking"),
            t.VulnClass.REDOS,
        )
        self.assertNotEqual(
            t.classify(
                "OpenSSH: Use-after-free during host key re-exchange",
                "ssh client UAF when a server changes its host key",
            ),
            t.VulnClass.XXE,
        )
