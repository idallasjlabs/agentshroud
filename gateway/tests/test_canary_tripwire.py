# Copyright (c) 2026 Isaiah Dallas Jefferson, Jr. AgentShroud\u2122
from __future__ import annotations
import base64
import codecs
import pytest
from gateway.security.canary_tripwire import CanaryTripwire, CanaryConfig, TripwireResponse

class TestCanaryTripwire:
    def setup_method(self):
        self.tw = CanaryTripwire()

    def test_plain_canary_detected(self):
        r = self.tw.scan("The SSN is 987-65-4321 found in records")
        assert r.detected and r.canary_value == "987-65-4321"

    def test_api_key_canary(self):
        r = self.tw.scan("Key: sk-test-REDTEAM123")
        assert r.detected and r.canary_value == "sk-test-REDTEAM123"

    def test_code_word_canary(self):
        r = self.tw.scan("This relates to Project Nightingale")
        assert r.detected and r.canary_value == "Project Nightingale"

    def test_case_insensitive(self):
        assert self.tw.scan("project nightingale is active").detected

    def test_reversed_canary(self):
        r = self.tw.scan("1234-56-789")
        assert r.detected and r.encoding == "reversed"

    def test_spaced_canary(self):
        assert self.tw.scan("9 8 7 6 5 4 3 2 1").detected

    def test_zero_width_bypass(self):
        assert self.tw.scan("987\u200b-\u200b65\u200b-\u200b4321").detected

    def test_base64_canary(self):
        encoded = base64.b64encode(b"987-65-4321").decode()
        r = self.tw.scan(f"Data: {encoded}")
        assert r.detected and r.encoding == "base64"

    def test_rot13_canary(self):
        rot = codecs.encode("Project Nightingale", "rot_13")
        r = self.tw.scan(rot)
        assert r.detected and r.encoding == "rot13"

    def test_url_encoded_canary(self):
        r = self.tw.scan("Value: %39%38%37%2D%36%35%2D%34%33%32%31")
        assert r.detected and r.encoding == "url_encoded"

    def test_normal_content_passes(self):
        assert not self.tw.scan("Hello, this is a normal response.").detected

    def test_counter_increments(self):
        assert self.tw.detection_count == 0
        self.tw.scan("987-65-4321")
        assert self.tw.detection_count == 1
        self.tw.scan("sk-test-REDTEAM123")
        assert self.tw.detection_count == 2

    def test_empty_input(self):
        assert not self.tw.scan("").detected

    def test_custom_config(self):
        tw = CanaryTripwire(CanaryConfig(values=["SECRETWORD"]))
        assert tw.scan("contains SECRETWORD here").detected
        assert not tw.scan("nothing here").detected

    def test_no_canaries(self):
        tw = CanaryTripwire(CanaryConfig(values=[]))
        assert not tw.scan("987-65-4321").detected

    # --- scan_response() bridge tests ---

    def test_scan_response_returns_tripwire_response(self):
        r = self.tw.scan_response(response_text="normal text", source="test")
        assert isinstance(r, TripwireResponse)

    def test_scan_response_blocks_on_canary(self):
        r = self.tw.scan_response(response_text="987-65-4321", source="pipeline")
        assert r.is_blocked is True
        assert "987-65-4321" in r.detections

    def test_scan_response_passes_clean_text(self):
        r = self.tw.scan_response(response_text="Hello, clean output.", source="pipeline")
        assert r.is_blocked is False
        assert r.detections == []

    def test_scan_response_no_block_when_block_disabled(self):
        tw = CanaryTripwire(CanaryConfig(block_on_detect=False))
        r = tw.scan_response(response_text="987-65-4321", source="pipeline")
        assert r.is_blocked is False
        assert "987-65-4321" in r.detections

    def test_scan_response_records_scan_method(self):
        r = self.tw.scan_response(response_text="987-65-4321", source="pipeline")
        assert len(r.scan_methods_used) > 0
