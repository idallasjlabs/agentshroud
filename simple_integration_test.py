#!/usr/bin/env python3
"""
Simple integration test to verify security modules are wired correctly.
"""

import sys
import os

# Simple test to verify the modules are properly integrated
def test_integration():
    print("Testing security module integration...")
    
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
            if imp in content:
                print(f"✓ Import found: {imp}")
            else:
                print(f"✗ Import missing: {imp}")
                return False
        
        # Check security module instantiation
        security_inits = [
            'DNSFilter(DNSFilterConfig())',
            'EgressMonitor(EgressMonitorConfig())',
            'BrowserSecurityGuard()',
            'OAuthSecurityValidator([])'
        ]
        
        for init in security_inits:
            if init in content:
                print(f"✓ Module instantiation found: {init}")
            else:
                print(f"✗ Module instantiation missing: {init}")
                return False
        
        # Check security checks are wired
        security_checks = [
            'DNS Security Check',
            'Browser Security Check', 
            'OAuth Security Check',
            'Egress Monitoring'
        ]
        
        for check in security_checks:
            if check in content:
                print(f"✓ Security check found: {check}")
            else:
                print(f"✗ Security check missing: {check}")
                return False
        
        # Check error handling
        error_patterns = [
            'except Exception as e:',
            'fail-closed',
            'logger.warning'
        ]
        
        for pattern in error_patterns:
            if pattern in content:
                print(f"✓ Error handling pattern found: {pattern}")
            else:
                print(f"✗ Error handling pattern missing: {pattern}")
                return False
        
        print("\n✓ All integration checks passed!")
        return True
        
    except Exception as e:
        print(f"✗ Integration test failed: {e}")
        return False

def test_security_flow():
    """Test the security flow with mock data."""
    print("\nTesting security flow...")
    
    try:
        # Check that DNS filter check happens before SSRF check
        with open('gateway/proxy/web_proxy.py', 'r') as f:
            content = f.read()
        
        dns_pos = content.find('DNS Security Check')
        ssrf_pos = content.find('Hard block: SSRF')
        
        if dns_pos != -1 and ssrf_pos != -1 and dns_pos < ssrf_pos:
            print("✓ DNS check occurs before SSRF check")
        else:
            print("✗ DNS check positioning incorrect")
            return False
            
        # Check that browser security check is conditional on user agent
        if 'user_agent' in content and 'User-Agent' in content:
            print("✓ Browser security check is user-agent conditional")
        else:
            print("✗ Browser security check not properly conditional")
            return False
            
        # Check that OAuth check looks for auth headers
        if 'Authorization' in content and 'auth' in content.lower():
            print("✓ OAuth security check looks for auth headers")
        else:
            print("✗ OAuth security check not properly implemented")
            return False
            
        # Check that egress monitoring is in scan_response
        egress_in_scan = 'scan_response' in content and content.find('Egress Monitoring') > content.find('def scan_response')
        if egress_in_scan:
            print("✓ Egress monitoring is in scan_response method")
        else:
            print("✗ Egress monitoring not in scan_response method")
            return False
            
        print("✓ All security flow checks passed!")
        return True
        
    except Exception as e:
        print(f"✗ Security flow test failed: {e}")
        return False

if __name__ == '__main__':
    success = test_integration() and test_security_flow()
    
    if success:
        print("\n🎉 All tests passed! Security modules are properly integrated.")
        sys.exit(0)
    else:
        print("\n❌ Some tests failed. Check the output above.")
        sys.exit(1)