---
source_file: "gateway/security/citation_verifier.py"
type: "code"
community: "Gateway Security Module"
location: "L113"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Gateway_Security_Module
---

# DraftEntry

## Connections
- [[.test_allowlisted_live_source_kept()]] - `calls` [EXTRACTED]
- [[.test_dropped_count_is_tamper_evident()]] - `calls` [EXTRACTED]
- [[.test_host_confusion_urls_rejected_and_never_fetched()]] - `calls` [EXTRACTED]
- [[.test_mixed_valid_and_invalid_keeps_only_valid()]] - `calls` [EXTRACTED]
- [[.test_multiple_valid_citations_all_kept()]] - `calls` [EXTRACTED]
- [[.test_no_candidate_urls_dropped()]] - `calls` [EXTRACTED]
- [[.test_off_allowlist_url_dropped_and_not_fetched()]] - `calls` [EXTRACTED]
- [[.test_report_all_unverified_is_empty()]] - `calls` [EXTRACTED]
- [[.test_report_keeps_verified_and_counts_dropped()]] - `calls` [EXTRACTED]
- [[.test_self_asserted_verified_is_ignored()]] - `calls` [EXTRACTED]
- [[.test_source_without_content_dropped()]] - `calls` [EXTRACTED]
- [[.test_ssrf_unsafe_urls_rejected_before_fetch()]] - `calls` [EXTRACTED]
- [[.test_unparseable_url_dropped()]] - `calls` [EXTRACTED]
- [[.test_unreachable_source_dropped()]] - `calls` [EXTRACTED]
- [[.test_verified_report_persists_with_intact_hashchain()]] - `calls` [EXTRACTED]
- [[.test_wildcard_allowlist_match_kept()]] - `calls` [EXTRACTED]
- [[.verify_entry()]] - `references` [EXTRACTED]
- [[.verify_report()]] - `references` [EXTRACTED]
- [[An unverified competitor claim submitted for citation checking.]] - `rationale_for` [EXTRACTED]
- [[Citation_1]] - `uses` [INFERRED]
- [[CompetitiveIntelReport_1]] - `uses` [INFERRED]
- [[CompetitorEntry_1]] - `uses` [INFERRED]
- [[ConfigUpdate]] - `uses` [INFERRED]
- [[FetchOutcome_1]] - `uses` [INFERRED]
- [[HTTPAuthorizationCredentials_1]] - `uses` [INFERRED]
- [[IntelDraftEntry]] - `uses` [INFERRED]
- [[IntelDraftRequest]] - `uses` [INFERRED]
- [[KillSwitchAction]] - `uses` [INFERRED]
- [[ModeRequest]] - `uses` [INFERRED]
- [[Path_40]] - `uses` [INFERRED]
- [[ServiceAction]] - `uses` [INFERRED]
- [[SkillGuardBlocked]] - `uses` [INFERRED]
- [[TestFetchOutcome]] - `uses` [INFERRED]
- [[TestMakeHttpxFetcher]] - `uses` [INFERRED]
- [[TestVerifyEntry]] - `uses` [INFERRED]
- [[TestVerifyReport]] - `uses` [INFERRED]
- [[UpdateRequest]] - `uses` [INFERRED]
- [[WebSocket_8]] - `uses` [INFERRED]
- [[_FakeFetcher]] - `uses` [INFERRED]
- [[_FakeStreamResponse]] - `uses` [INFERRED]
- [[api.py]] - `imports` [EXTRACTED]
- [[citation_verifier.py]] - `contains` [EXTRACTED]
- [[submit_competitive_intel()]] - `calls` [EXTRACTED]
- [[test_citation_verifier.py]] - `imports` [EXTRACTED]
- [[test_default_allowlist_uses_permanent_egress_domains()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Gateway_Security_Module