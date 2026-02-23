#!/usr/bin/env python3
"""
Final integration script - very careful placement
"""

def update_imports_and_constructors():
    with open('gateway/proxy/web_proxy.py', 'r') as f:
        content = f.read()

    # Replace imports
    content = content.replace(
        'from ..security.dns_filter import DNSFilter', 
        'from ..security.dns_filter import DNSFilter, DNSFilterConfig'
    )
    content = content.replace(
        'from ..security.egress_monitor import EgressMonitor',
        'from ..security.egress_monitor import EgressMonitor, EgressMonitorConfig'
    )

    # Replace instantiations
    old_init = '''        # Network Security Modules
        self.dns_filter = DNSFilter()
        self.network_validator = NetworkValidator()
        self.egress_monitor = EgressMonitor()
        self.browser_security = BrowserSecurityGuard()
        self.oauth_security = OAuthSecurityValidator()'''

    new_init = '''        # Network Security Modules
        self.dns_filter = DNSFilter(DNSFilterConfig())
        self.network_validator = NetworkValidator()
        self.egress_monitor = EgressMonitor(EgressMonitorConfig())
        self.browser_security = BrowserSecurityGuard()
        self.oauth_security = OAuthSecurityValidator([])  # Empty allowed redirect URIs'''

    content = content.replace(old_init, new_init)

    with open('gateway/proxy/web_proxy.py', 'w') as f:
        f.write(content)
    
    print("Updated imports and constructors")

def add_dns_security_check():
    with open('gateway/proxy/web_proxy.py', 'r') as f:
        content = f.read()

    # Find the spot right after url_result assignment and before SSRF check
    dns_marker = "url_result = self.url_analyzer.analyze(url)"
    ssrf_marker = "# Hard block: SSRF"
    
    dns_check_code = '''
        # --- DNS Security Check ---
        try:
            if url_result.domain:
                dns_verdict = self.dns_filter.check(url_result.domain, 'web-proxy')
                if not dns_verdict.allowed:
                    result.action = ProxyAction.BLOCK
                    result.blocked = True
                    result.block_reason = f"DNS filter blocked: {dns_verdict.reason}"
                    self._stats["blocked"] += 1
                    self._audit("web_request_blocked_dns", url, {"method": method, "reason": dns_verdict.reason})
                    result.processing_time_ms = (time.time() - start) * 1000
                    return result
                elif dns_verdict.flagged:
                    if not hasattr(result, 'url_findings') or not result.url_findings:
                        result.url_findings = []
                    result.url_findings.append({
                        "category": "dns",
                        "severity": "medium",
                        "description": f"DNS flagged: {dns_verdict.reason}",
                        "detail": dns_verdict.reason
                    })
                    if result.action != ProxyAction.BLOCK:
                        result.action = ProxyAction.FLAG
        except Exception as e:
            logger.warning(f"DNS filter error for {url}: {e}")
            # Fail-closed: block the request on DNS filter error
            result.action = ProxyAction.BLOCK
            result.blocked = True
            result.block_reason = f"DNS security check failed: {str(e)}"
            self._stats["blocked"] += 1
            result.processing_time_ms = (time.time() - start) * 1000
            return result
'''

    # Split and insert
    parts = content.split(ssrf_marker)
    if len(parts) == 2:
        content = parts[0] + dns_check_code + "\n        " + ssrf_marker + parts[1]
        
        with open('gateway/proxy/web_proxy.py', 'w') as f:
            f.write(content)
        print("Added DNS security check")
    else:
        print("Could not find SSRF marker")

def add_browser_and_oauth_checks():
    with open('gateway/proxy/web_proxy.py', 'r') as f:
        content = f.read()

    # Find the location after URL findings section but before audit
    marker = "if any(f.category == \"pii\" for f in url_result.findings):"
    
    # Find this section and add our checks after it
    if marker in content:
        parts = content.split(marker)
        if len(parts) == 2:
            # Find the next few lines after the PII check
            remaining = parts[1]
            lines = remaining.split('\n')
            
            # Find where to insert (after the self._stats["pii_in_urls"] += 1 line)
            insert_after = -1
            for i, line in enumerate(lines):
                if 'self._stats["pii_in_urls"]' in line:
                    insert_after = i + 1
                    break
            
            if insert_after > -1:
                # Insert browser and oauth checks
                security_checks = '''
        # --- Browser Security Check ---
        try:
            user_agent = (headers or {}).get('User-Agent', '').lower()
            if any(browser in user_agent for browser in ['mozilla', 'chrome', 'safari', 'edge', 'webkit']):
                url_reputation = self.browser_security.check_url_reputation(url)
                if url_reputation.value >= 3:  # HIGH or CRITICAL threat
                    result.action = ProxyAction.BLOCK
                    result.blocked = True
                    result.block_reason = f"Browser security blocked: {url_reputation.name} threat level"
                    self._stats["blocked"] += 1
                    self._audit("web_request_blocked_browser", url, {"method": method, "threat_level": url_reputation.name})
                    result.processing_time_ms = (time.time() - start) * 1000
                    return result
                elif url_reputation.value >= 2:  # MEDIUM threat
                    if not result.url_findings:
                        result.url_findings = []
                    result.url_findings.append({
                        "category": "browser_security",
                        "severity": "medium", 
                        "description": f"Browser security warning: {url_reputation.name} threat level",
                        "detail": f"URL reputation: {url_reputation.name}"
                    })
                    if result.action != ProxyAction.BLOCK:
                        result.action = ProxyAction.FLAG
        except Exception as e:
            logger.warning(f"Browser security error for {url}: {e}")
            # Fail-closed: block the request on browser security error  
            result.action = ProxyAction.BLOCK
            result.blocked = True
            result.block_reason = f"Browser security check failed: {str(e)}"
            self._stats["blocked"] += 1
            result.processing_time_ms = (time.time() - start) * 1000
            return result

        # --- OAuth Security Check ---
        try:
            auth_header = (headers or {}).get('Authorization', '')
            if auth_header or any(key.lower().startswith('auth') for key in (headers or {})):
                if not result.url_findings:
                    result.url_findings = []
                result.url_findings.append({
                    "category": "oauth_security",
                    "severity": "low",
                    "description": "Authentication headers detected",
                    "detail": "Request contains authorization or authentication headers"
                })
                if result.action == ProxyAction.ALLOW:
                    result.action = ProxyAction.FLAG
        except Exception as e:
            logger.warning(f"OAuth security error for {url}: {e}")
            # Don't fail-closed for OAuth as it might be a false positive
'''
                
                # Reconstruct
                new_lines = lines[:insert_after] + security_checks.split('\n') + lines[insert_after:]
                new_remaining = '\n'.join(new_lines)
                content = parts[0] + marker + new_remaining
                
                with open('gateway/proxy/web_proxy.py', 'w') as f:
                    f.write(content)
                print("Added browser and OAuth security checks")
            else:
                print("Could not find insertion point after PII check")
        else:
            print("Unexpected split result for PII marker")
    else:
        print("Could not find PII marker")

def add_egress_monitoring():
    with open('gateway/proxy/web_proxy.py', 'r') as f:
        content = f.read()

    # Find the end of scan_response method (before final return)
    marker = "result.processing_time_ms = (time.time() - start) * 1000\n        return result"
    
    egress_code = '''        # --- Egress Monitoring ---
        try:
            from ..security.egress_monitor import EgressEvent, EgressChannel
            from urllib.parse import urlparse
            
            parsed = urlparse(url)
            egress_event = EgressEvent(
                timestamp=time.time(),
                agent_id='web-proxy',
                channel=EgressChannel.HTTP,
                destination=parsed.hostname or url,
                metadata={
                    'url': url,
                    'status_code': status_code,
                    'content_type': content_type,
                    'response_size': response_size or len(body.encode('utf-8', errors='replace')),
                    'findings_count': len(result.content_findings),
                    'action': result.action.value
                }
            )
            self.egress_monitor.record(egress_event)
        except Exception as e:
            logger.warning(f"Egress monitoring error for {url}: {e}")
            # Continue processing - egress monitoring is for logging only

        ''' + marker

    # Replace only the last occurrence (in scan_response)
    parts = content.rsplit(marker, 1)
    if len(parts) == 2:
        content = parts[0] + egress_code + parts[1]
        
        with open('gateway/proxy/web_proxy.py', 'w') as f:
            f.write(content)
        print("Added egress monitoring")
    else:
        print("Could not find final return marker")

if __name__ == '__main__':
    update_imports_and_constructors()
    add_dns_security_check()
    add_browser_and_oauth_checks()
    add_egress_monitoring()
    print("Final integration complete!")