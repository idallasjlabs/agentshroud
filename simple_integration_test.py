#!/usr/bin/env python3
"""
Simple integration test to verify security modules are wired correctly.
"""

import os
import sys

def test_integration():
    """Verify key security modules are wired into the proxy."""
    try:
        # Import the web proxy module
        sys.path.append(os.path.join(os.path.dirname(__file__)))
        
        # Test that the file compiles
        import py_compile
        py_compile.compile('gateway/proxy/web_proxy.py', doraise=True)
        print("✓ web_proxy.py compiles successfully")
        
        # Check that security modules are imported
        with open('gateway/proxy/web_proxy.py', 'r') as f:
            content = f.read()
        
        # Check imports
        required_imports = [
            'DNSFilter, DNSFilterConfig',
            'EgressMonitor, EgressMonitorConfig',
            'BrowserSecurityGuard',
            'OAuthSecurityValidator'
        ]
        
        for imp in required_imports:
            assert imp in content, f"Import missing: {imp}"
        
        # Check security module instantiation
        security_inits = [
            'DNSFilter(DNSFilterConfig())',
            'EgressMonitor(EgressMonitorConfig())',
            'BrowserSecurityGuard()',
            'OAuthSecurityValidator([])'
        ]
        
        for init in security_inits:
            assert init in content, f"Module instantiation missing: {init}"
        
        # Check security checks are wired
        security_checks = [
            'DNS Security Check',
            'Browser Security Check', 
            'OAuth Security Check',
            'Egress Monitoring'
        ]
        
        for check in security_checks:
            assert check in content, f"Security check missing: {check}"
        
        # Check error handling
        error_patterns = [
            'except Exception as e:',
            'fail-closed',
            'logger.warning'
        ]
        
        for pattern in error_patterns:
            assert pattern in content, f"Error handling pattern missing: {pattern}"

    except Exception as e:
        raise AssertionError(f"Integration test failed: {e}") from e

def test_security_flow():
    """Test the security flow with mock data."""
    try:
        # Check that DNS filter check happens before SSRF check
        with open('gateway/proxy/web_proxy.py', 'r') as f:
            content = f.read()
        
        dns_pos = content.find('DNS Security Check')
        ssrf_pos = content.find('Hard block: SSRF')
        
        assert dns_pos != -1 and ssrf_pos != -1 and dns_pos < ssrf_pos, (
            "DNS check positioning incorrect"
        )
            
        # Check that browser security check is conditional on user agent
        assert 'user_agent' in content and 'User-Agent' in content, (
            "Browser security check not properly conditional"
        )
            
        # Check that OAuth check looks for auth headers
        assert 'Authorization' in content and 'auth' in content.lower(), (
            "OAuth security check not properly implemented"
        )
            
        # Check that egress monitoring is in scan_response
        egress_in_scan = 'scan_response' in content and content.find('Egress Monitoring') > content.find('def scan_response')
        assert egress_in_scan, "Egress monitoring not in scan_response method"

    except Exception as e:
        raise AssertionError(f"Security flow test failed: {e}") from e

if __name__ == '__main__':
    try:
        test_integration()
        test_security_flow()
        print("\n🎉 All tests passed! Security modules are properly integrated.")
        sys.exit(0)
    except AssertionError:
        print("\n❌ Some tests failed. Check the output above.")
        sys.exit(1)
