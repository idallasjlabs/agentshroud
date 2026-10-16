---
type: community
cohesion: 0.07
members: 37
---

# ConsentFramework

**Cohesion:** 0.07 - loosely connected
**Members:** 37 nodes

## Members
- [[dot-can_enter_credentials()]] - code - gateway/security/browser_security.py
- [[dot-check_url_reputation()]] - code - gateway/security/browser_security.py
- [[dot-test_data_uri_blocked()]] - code - gateway/tests/test_browser_security.py
- [[dot-test_excessive_subdomains()]] - code - gateway/tests/test_browser_security.py
- [[dot-test_fake_captcha()]] - code - gateway/tests/test_browser_security.py
- [[dot-test_fake_dialog_detected()]] - code - gateway/tests/test_browser_security.py
- [[dot-test_fake_windows_alert()]] - code - gateway/tests/test_browser_security.py
- [[dot-test_homograph_attack()]] - code - gateway/tests/test_browser_security.py
- [[dot-test_hook_can_flag_threat()]] - code - gateway/tests/test_browser_security.py
- [[dot-test_http_blocked()]] - code - gateway/tests/test_browser_security.py
- [[dot-test_https_allowed()]] - code - gateway/tests/test_browser_security.py
- [[dot-test_ip_address_url()]] - code - gateway/tests/test_browser_security.py
- [[dot-test_ip_blocked_for_credentials()]] - code - gateway/tests/test_browser_security.py
- [[dot-test_known_phishing_pattern()]] - code - gateway/tests/test_browser_security.py
- [[dot-test_legitimate_url()]] - code - gateway/tests/test_browser_security.py
- [[dot-test_localhost_allowed()]] - code - gateway/tests/test_browser_security.py
- [[dot-test_multiple_threats_aggregated()]] - code - gateway/tests/test_browser_security.py
- [[dot-test_no_hook_returns_none_threat()]] - code - gateway/tests/test_browser_security.py
- [[dot-test_safe_content_passes()]] - code - gateway/tests/test_browser_security.py
- [[dot-test_screenshot_hook_registered()]] - code - gateway/tests/test_browser_security.py
- [[dot-test_suspicious_domain_blocked()]] - code - gateway/tests/test_browser_security.py
- [[dot-test_suspicious_subdomain()]] - code - gateway/tests/test_browser_security.py
- [[dot-test_tech_support_scam()]] - code - gateway/tests/test_browser_security.py
- [[dot-test_urgent_action_required()]] - code - gateway/tests/test_browser_security.py
- [[CredentialEntryBlocked]] - code - gateway/security/browser_security.py
- [[Exception_1]] - code
- [[PhishingURLDetected]] - code - gateway/security/browser_security.py
- [[SocialEngineeringDetected]] - code - gateway/security/browser_security.py
- [[TestCredentialProtection]] - code - gateway/tests/test_browser_security.py
- [[TestScreenshotAnalysis]] - code - gateway/tests/test_browser_security.py
- [[TestSocialEngineeringDetection]] - code - gateway/tests/test_browser_security.py
- [[TestURLReputation]] - code - gateway/tests/test_browser_security.py
- [[ThreatLevel]] - code - gateway/security/browser_security.py
- [[Wu et al. 2026 (arXiv2601.07263) — Browser-based agent social engineering attacks]] - paper - docs/vault/02 - Modules/Security Modules/browser_security.py.md
- [[browser_security.py]] - code - gateway/security/browser_security.py
- [[guard()_2]] - code - gateway/tests/test_browser_security.py
- [[test_browser_security.py]] - code - gateway/tests/test_browser_security.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/ConsentFramework
SORT file.name ASC
```

## Connections to other communities
- 9 edges to [[_COMMUNITY_MiddlewareManager]]
- 8 edges to [[_COMMUNITY_AlertDispatcher]]
- 2 edges to [[_COMMUNITY_AgentTarget]]
- 2 edges to [[_COMMUNITY_ConsentFramework_1]]
- 2 edges to [[_COMMUNITY_SessionManager]]
- 2 edges to [[_COMMUNITY_TestToolChainAnalyzer]]
- 1 edge to [[_COMMUNITY_Request]]
- 1 edge to [[_COMMUNITY_ProxyAction]]
- 1 edge to [[_COMMUNITY_SkillGuard]]
- 1 edge to [[_COMMUNITY_ResourceGuard]]
- 1 edge to [[_COMMUNITY_CompetitiveIntelReport]]
- 1 edge to [[_COMMUNITY_SecureBrowser]]
- 1 edge to [[_COMMUNITY_SecureBrowser_1]]
- 1 edge to [[_COMMUNITY_SecureBrowser_2]]
- 1 edge to [[_COMMUNITY_SecureBrowser_3]]
- 1 edge to [[_COMMUNITY_api.py]]
- 1 edge to [[_COMMUNITY_ApprovalQueueConfig]]

## Top bridge nodes
- [[Exception_1]] - degree 17, connects to 13 communities
- [[browser_security.py]] - degree 11, connects to 5 communities
- [[ThreatLevel]] - degree 9, connects to 3 communities
- [[TestSocialEngineeringDetection]] - degree 12, connects to 2 communities
- [[TestURLReputation]] - degree 12, connects to 2 communities
