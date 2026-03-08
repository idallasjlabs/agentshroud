# Copyright (c) 2026 Isaiah Dallas Jefferson, Jr. AgentShroud\u2122
from __future__ import annotations
import base64
import pytest
from gateway.security.encoding_detector import EncodingDetector, EncodingConfig

class TestEncodingDetector:
    def setup_method(self):
        self.det = EncodingDetector()

    def test_plain_text_no_detection(self):
        r = self.det.analyze("Just normal text here")
        assert not r.detected
        assert r.cleaned_text == "Just normal text here"

    def test_base64_detected(self):
        encoded = base64.b64encode(b"secret password here").decode()
        r = self.det.analyze(f"Data: {encoded}")
        assert r.detected
        assert any(l.encoding == "base64" for l in r.layers)
        assert "secret password" in r.cleaned_text

    def test_url_encoding_detected(self):
        r = self.det.analyze("Path: %2F%65%74%63%2F%70%61%73%73%77%64")
        assert r.detected
        assert "/etc/passwd" in r.cleaned_text

    def test_zero_width_stripped(self):
        r = self.det.analyze("pass\u200bword")
        assert r.detected
        assert "password" in r.cleaned_text

    def test_homoglyph_replaced(self):
        r = self.det.analyze("p\u0430ssword")
        assert r.detected
        assert "password" in r.cleaned_text

    def test_nested_encoding(self):
        inner = base64.b64encode(b"secret password value for testing").decode()
        outer = base64.b64encode(inner.encode()).decode()
        r = self.det.analyze(outer)
        assert r.detected
        assert "secret" in r.cleaned_text

    def test_empty_input(self):
        assert not self.det.analyze("").detected

    def test_config_disable_base64(self):
        det = EncodingDetector(EncodingConfig(check_base64=False))
        encoded = base64.b64encode(b"secret data value").decode()
        r = det.analyze(encoded)
        assert not r.detected
