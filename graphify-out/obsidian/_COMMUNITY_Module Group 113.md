---
type: community
cohesion: 0.07
members: 40
---

# Module Group 113

**Cohesion:** 0.07 - loosely connected
**Members:** 40 nodes

## Members
- [[.analyze_content()]] - code - gateway/security/browser_security.py
- [[.analyze_screenshot()]] - code - gateway/security/browser_security.py
- [[.can_enter_credentials()]] - code - gateway/security/browser_security.py
- [[.check_url_reputation()]] - code - gateway/security/browser_security.py
- [[.test_data_uri_blocked()]] - code - gateway/tests/test_browser_security.py
- [[.test_excessive_subdomains()]] - code - gateway/tests/test_browser_security.py
- [[.test_fake_captcha()]] - code - gateway/tests/test_browser_security.py
- [[.test_fake_dialog_detected()]] - code - gateway/tests/test_browser_security.py
- [[.test_fake_windows_alert()]] - code - gateway/tests/test_browser_security.py
- [[.test_homograph_attack()]] - code - gateway/tests/test_browser_security.py
- [[.test_hook_can_flag_threat()]] - code - gateway/tests/test_browser_security.py
- [[.test_http_blocked()]] - code - gateway/tests/test_browser_security.py
- [[.test_https_allowed()]] - code - gateway/tests/test_browser_security.py
- [[.test_ip_address_url()]] - code - gateway/tests/test_browser_security.py
- [[.test_ip_blocked_for_credentials()]] - code - gateway/tests/test_browser_security.py
- [[.test_known_phishing_pattern()]] - code - gateway/tests/test_browser_security.py
- [[.test_legitimate_url()]] - code - gateway/tests/test_browser_security.py
- [[.test_localhost_allowed()]] - code - gateway/tests/test_browser_security.py
- [[.test_multiple_threats_aggregated()]] - code - gateway/tests/test_browser_security.py
- [[.test_no_hook_returns_none_threat()]] - code - gateway/tests/test_browser_security.py
- [[.test_safe_content_passes()]] - code - gateway/tests/test_browser_security.py
- [[.test_screenshot_hook_registered()]] - code - gateway/tests/test_browser_security.py
- [[.test_suspicious_domain_blocked()]] - code - gateway/tests/test_browser_security.py
- [[.test_suspicious_subdomain()]] - code - gateway/tests/test_browser_security.py
- [[.test_tech_support_scam()]] - code - gateway/tests/test_browser_security.py
- [[.test_urgent_action_required()]] - code - gateway/tests/test_browser_security.py
- [[CredentialEntryBlocked]] - code - gateway/security/browser_security.py
- [[Exception_1]] - code
- [[IntEnum]] - code
- [[PhishingURLDetected]] - code - gateway/security/browser_security.py
- [[SocialEngineeringDetected]] - code - gateway/security/browser_security.py
- [[TestCredentialProtection]] - code - gateway/tests/test_browser_security.py
- [[TestScreenshotAnalysis]] - code - gateway/tests/test_browser_security.py
- [[TestSocialEngineeringDetection]] - code - gateway/tests/test_browser_security.py
- [[TestURLReputation]] - code - gateway/tests/test_browser_security.py
- [[ThreatAssessment]] - code - gateway/security/browser_security.py
- [[ThreatLevel_1]] - code - gateway/security/browser_security.py
- [[browser_security.py]] - code - gateway/security/browser_security.py
- [[guard()]] - code - gateway/tests/test_browser_security.py
- [[test_browser_security.py]] - code - gateway/tests/test_browser_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Module_Group_113
SORT file.name ASC
```

## Connections to other communities
- 12 edges to [[_COMMUNITY_RBAC Middleware & Ingest API]]
- 9 edges to [[_COMMUNITY_PII Sanitizer & Resource Guard]]
- 1 edge to [[_COMMUNITY_Agent Routing & Request Models]]
- 1 edge to [[_COMMUNITY_CLI & Core Gateway Routes]]
- 1 edge to [[_COMMUNITY_Module Group 95]]
- 1 edge to [[_COMMUNITY_Module Group 102]]
- 1 edge to [[_COMMUNITY_Module Group 103]]
- 1 edge to [[_COMMUNITY_Module Group 67]]
- 1 edge to [[_COMMUNITY_URL Analyzer & Content Scanner]]
- 1 edge to [[_COMMUNITY_Progressive Trust Levels]]
- 1 edge to [[_COMMUNITY_Alert Dispatcher]]
- 1 edge to [[_COMMUNITY_Module Group 137]]
- 1 edge to [[_COMMUNITY_Environment Guard & Leak Detection]]
- 1 edge to [[_COMMUNITY_Module Group 110]]

## Top bridge nodes
- [[Exception_1]] - degree 9, connects to 6 communities
- [[ThreatAssessment]] - degree 22, connects to 5 communities
- [[browser_security.py]] - degree 9, connects to 2 communities
- [[IntEnum]] - degree 3, connects to 2 communities
- [[TestSocialEngineeringDetection]] - degree 12, connects to 1 community