---
type: community
cohesion: 0.06
members: 57
---

# AgentTarget (2)

**Cohesion:** 0.06 - loosely connected
**Members:** 57 nodes

## Members
- [[dot-to_dict()_3]] - code - gateway/security/canary.py
- [[AgentShroud App Icon (64x64)]] - image - branding/icons/app/icon-64x64.png
- [[AgentShroud BadgeAvatar Logo Variant (120x120)]] - image - branding/logos/variants/badge-120x120.png
- [[AgentShroud Brand Collateral Mockup]] - image - branding/logos/png/logo-mockup.png
- [[AgentShroud Logo (SVG Wrapper, Embedded Raster)]] - image - branding/logos/svg/logo.svg
- [[AgentShroud Logo - GlowTransparent Variant]] - image - branding/logos/png/logo-transparent.png
- [[AgentShroud Primary Logo Lockup]] - image - branding/logos/png/logo.png
- [[AgentShroud macOS App Icon (1024x1024, Rounded Squircle)]] - image - branding/icons/app/icon-macos-rounded-1024x1024.png
- [[Any_9]] - code - gateway/security/canary.py
- [[Audit Ledger Module Badge Icon]] - image - branding/icons/modules/audit-ledger-256x256.png
- [[Canary result should serialize to dict properly.]] - rationale - gateway/tests/test_canary.py
- [[Canary should detect that fake PII was stripped.]] - rationale - gateway/tests/test_canary.py
- [[Canary should fail when no pipeline configured.]] - rationale - gateway/tests/test_canary.py
- [[Canary should pass proxy check with healthy forwarder.]] - rationale - gateway/tests/test_canary.py
- [[Canary should pass when pipeline is properly configured.]] - rationale - gateway/tests/test_canary.py
- [[Canary should verify audit chain integrity.]] - rationale - gateway/tests/test_canary.py
- [[CanaryCheck]] - code - gateway/security/canary.py
- [[CanaryResult]] - code - gateway/security/canary.py
- [[Credential Isolation Module Badge Icon]] - image - branding/icons/modules/credential-iso-256x256.png
- [[Drift Detector Module Badge Icon]] - image - branding/icons/modules/drift-detector-256x256.png
- [[Encrypted Store Module Badge Icon]] - image - branding/icons/modules/encrypted-store-256x256.png
- [[HTTP Proxy Module Badge Icon]] - image - branding/icons/modules/http-proxy-256x256.png
- [[Individual canary check result.]] - rationale - gateway/security/canary.py
- [[Kill Switch Module Badge Icon]] - image - branding/icons/modules/kill-switch-256x256.png
- [[PII Sanitizer Module Badge Icon]] - image - branding/icons/modules/pii-sanitizer-256x256.png
- [[Result of running the canary system.]] - rationale - gateway/security/canary.py
- [[Run the canary verification system.      Args         pipeline SecurityPipelin]] - rationale - gateway/security/canary.py
- [[SSH Proxy Module Badge Icon]] - image - branding/icons/modules/ssh-proxy-256x256.png
- [[Trust Manager Module Badge Icon]] - image - branding/icons/modules/trust-manager-256x256.png
- [[Verify canary message contains the expected fake PII.]] - rationale - gateway/tests/test_canary.py
- [[alert_dispatcher.py]] - code - gateway/security/alert_dispatcher.py
- [[canary-cron.sh embedded Python main()]] - code - scripts/canary-cron.sh
- [[canary.py]] - code - gateway/security/canary.py
- [[drift_detector.py]] - code - gateway/security/drift_detector.py
- [[encrypted_store.py]] - code - gateway/security/encrypted_store.py
- [[fail()]] - code - scripts/verify-proxy.sh
- [[healthy_forwarder()]] - code - gateway/tests/test_canary.py
- [[info()]] - code - scripts/verify-proxy.sh
- [[pass()]] - code - scripts/verify-proxy.sh
- [[run_bypass()]] - code - scripts/verify-proxy.sh
- [[run_canary()]] - code - scripts/verify-proxy.sh
- [[run_canary()_1]] - code - gateway/security/canary.py
- [[run_chain()]] - code - scripts/verify-proxy.sh
- [[run_full()]] - code - scripts/verify-proxy.sh
- [[run_quick()]] - code - scripts/verify-proxy.sh
- [[test_canary.py]] - code - gateway/tests/test_canary.py
- [[test_canary_fails_without_pipeline()]] - code - gateway/tests/test_canary.py
- [[test_canary_message_contains_fake_pii()]] - code - gateway/tests/test_canary.py
- [[test_canary_passes_with_pipeline()]] - code - gateway/tests/test_canary.py
- [[test_canary_result_serialization()]] - code - gateway/tests/test_canary.py
- [[test_canary_verifies_audit_chain()]] - code - gateway/tests/test_canary.py
- [[test_canary_verifies_pii_stripping()]] - code - gateway/tests/test_canary.py
- [[test_canary_with_healthy_forwarder()]] - code - gateway/tests/test_canary.py
- [[test_canary_with_unhealthy_forwarder()]] - code - gateway/tests/test_canary.py
- [[unhealthy_forwarder()]] - code - gateway/tests/test_canary.py
- [[verify-proxy.sh]] - code - scripts/verify-proxy.sh
- [[verify-proxy.sh script]] - code - scripts/verify-proxy.sh

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/AgentTarget_2
SORT file.name ASC
```

## Connections to other communities
- 8 edges to [[_COMMUNITY_AgentTarget]]
- 7 edges to [[_COMMUNITY_ContextGuard]]
- 7 edges to [[_COMMUNITY_SecurityPipeline (2)]]
- 4 edges to [[_COMMUNITY_PromptGuard]]
- 3 edges to [[_COMMUNITY_MCPPermissionManager]]
- 3 edges to [[_COMMUNITY_openclawskillsi-crSKILL]]
- 3 edges to [[_COMMUNITY_DelegationManager]]
- 2 edges to [[_COMMUNITY_LLMProxy.proxy_messages (non-streaming)]]
- 2 edges to [[_COMMUNITY_Common Queries]]
- 2 edges to [[_COMMUNITY_test_a2a_policy.py]]
- 1 edge to [[_COMMUNITY_socrouter.py]]
- 1 edge to [[_COMMUNITY_ResourceUsage]]
- 1 edge to [[_COMMUNITY_Colima & Docker Operations Guide — AgentShroud]]
- 1 edge to [[_COMMUNITY_NetworkSecurityFinding]]
- 1 edge to [[_COMMUNITY_system-requirements]]
- 1 edge to [[_COMMUNITY_EgressFilter]]
- 1 edge to [[_COMMUNITY_PortManager]]
- 1 edge to [[_COMMUNITY_agentshroud-blueteamSKILL.md (2)]]
- 1 edge to [[_COMMUNITY_check_command]]
- 1 edge to [[_COMMUNITY_asyncio]]
- 1 edge to [[_COMMUNITY_UserSessionManager (3)]]
- 1 edge to [[_COMMUNITY_test_soc_realtime_coverage.py]]
- 1 edge to [[_COMMUNITY_EnhancedApprovalQueue (`enhanced_queue.py`)]]
- 1 edge to [[_COMMUNITY_SSHProxy]]
- 1 edge to [[_COMMUNITY_test_llm_proxy.py]]
- 1 edge to [[_COMMUNITY_KillSwitchMonitor]]
- 1 edge to [[_COMMUNITY_test_voice_latency_guard.py]]
- 1 edge to [[_COMMUNITY_main.py]]

## Top bridge nodes
- [[test_canary.py]] - degree 21, connects to 8 communities
- [[alert_dispatcher.py]] - degree 10, connects to 7 communities
- [[AgentShroud macOS App Icon (1024x1024, Rounded Squircle)]] - degree 16, connects to 4 communities
- [[run_canary()]] - degree 11, connects to 4 communities
- [[encrypted_store.py]] - degree 6, connects to 4 communities
