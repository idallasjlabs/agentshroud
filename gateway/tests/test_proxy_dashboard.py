"""Tests for the proxy dashboard status display."""

import pytest
import time

from gateway.dashboard.proxy_status import ProxyDashboard, ProxyStatusReport


def test_dashboard_default_unprotected():
    """Dashboard should default to unprotected mode."""
    dash = ProxyDashboard()
    report = dash.get_report()
    assert report.mode == "unprotected"


def test_dashboard_set_proxy_mode():
    """Dashboard should reflect proxy mode."""
    dash = ProxyDashboard()
    dash.set_mode("proxy")
    report = dash.get_report()
    assert report.mode == "proxy"
    display = dash.get_display()
    assert "ACTIVE" in display["proxy_mode"]
    assert "\u2705" in display["proxy_mode"]


def test_dashboard_set_sidecar_mode():
    """Dashboard should reflect sidecar mode with warning."""
    dash = ProxyDashboard()
    dash.set_mode("sidecar")
    display = dash.get_display()
    assert "Sidecar" in display["proxy_mode"]
    assert "\u26a0" in display["proxy_mode"]


def test_dashboard_message_tracking():
    """Dashboard should track proxied messages."""
    dash = ProxyDashboard()
    dash.record_message_proxied()
    report = dash.get_report()
    assert report.last_message_proxied_ago >= 0
    assert report.last_message_proxied_ago < 5


def test_dashboard_pii_counting():
    """Dashboard should count PII redactions."""
    dash = ProxyDashboard()
    dash.record_pii_redaction(3)
    dash.record_pii_redaction(2)
    report = dash.get_report()
    assert report.pii_sanitized_today == 5


def test_dashboard_audit_status():
    """Dashboard should show audit chain status."""
    dash = ProxyDashboard()
    dash.update_audit_status(entries=42, valid=True)
    report = dash.get_report()
    assert report.audit_chain_entries == 42
    assert report.audit_chain_valid is True
    display = dash.get_display()
    assert "42 entries" in display["audit_chain"]
    assert "VERIFIED" in display["audit_chain"]


def test_dashboard_audit_broken():
    """Dashboard should show broken audit chain."""
    dash = ProxyDashboard()
    dash.update_audit_status(entries=10, valid=False)
    display = dash.get_display()
    assert "BROKEN" in display["audit_chain"]


def test_dashboard_direct_access():
    """Dashboard should track direct access status."""
    dash = ProxyDashboard()
    dash.update_direct_access(blocked=True)
    report = dash.get_report()
    assert report.direct_access_blocked is True
    assert report.direct_access_last_tested >= 0


def test_dashboard_canary_status():
    """Dashboard should track canary results."""
    dash = ProxyDashboard()
    dash.update_canary(passed=True)
    report = dash.get_report()
    assert report.canary_passed is True
    display = dash.get_display()
    assert "PASSED" in display["canary"]


def test_dashboard_canary_failed():
    """Dashboard should show failed canary."""
    dash = ProxyDashboard()
    dash.update_canary(passed=False)
    display = dash.get_display()
    assert "FAILED" in display["canary"]


def test_dashboard_uptime():
    """Dashboard should track uptime."""
    dash = ProxyDashboard()
    report = dash.get_report()
    assert report.uptime_seconds >= 0


def test_dashboard_display_all_fields():
    """Dashboard display should include all required fields."""
    dash = ProxyDashboard()
    dash.set_mode("proxy")
    display = dash.get_display()
    assert "proxy_mode" in display
    assert "last_proxied" in display
    assert "pii_today" in display
    assert "audit_chain" in display
    assert "direct_access" in display
    assert "canary" in display


def test_status_report_to_display():
    """ProxyStatusReport.to_display should produce readable strings."""
    report = ProxyStatusReport(
        mode="proxy",
        mode_icon="\u2705",
        last_message_proxied_ago=5.0,
        pii_sanitized_today=10,
        audit_chain_entries=100,
        audit_chain_valid=True,
        direct_access_blocked=True,
        direct_access_last_tested=2.0,
        canary_passed=True,
        canary_last_run=60.0,
        uptime_seconds=3600.0,
    )
    display = report.to_display()
    assert "5s ago" in display["last_proxied"]
    assert "10" in display["pii_today"]
    assert "100 entries" in display["audit_chain"]
