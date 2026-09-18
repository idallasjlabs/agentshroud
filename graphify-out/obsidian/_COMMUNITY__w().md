---
type: community
cohesion: 0.08
members: 37
---

# _w()

**Cohesion:** 0.08 - loosely connected
**Members:** 37 nodes

## Members
- [[.test_containerized_compose_equivalents()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_containerized_compose_internal_network()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_containerized_compose_private_registry()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_containerized_fallback_evidence()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_containerized_no_compose_zero()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_containerized_no_cosign_no_pipeline_evidence()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_containerized_pipeline_evidence_full()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_containerized_public_image_zero()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_cosign_with_runtime_verification()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_cosign_with_wired_verifier_module()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_distinct_namespaces_partial_caps()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_docker_config_auths_full()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_empty_auths_zero()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_empty_sbom_scores_two()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_full_daemon_json()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_full_host_evidence()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_full_root_caps_zero()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_fully_isolated_container_scores_five()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_icc_disabled_with_validator()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_icc_only()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_namespace_check_exception_assumes_isolated()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_no_config_not_containerized_zero()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_no_cosign_outside_container_zero()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_no_kernel_info_zero()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_not_containerized_no_config_zero()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_sbom_with_packages_trivy_branches()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_shared_mount_namespace_returns_one()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[.test_unreadable_status_zero()]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestContainerRuntimeIsolation]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestDockerDaemonConfig]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestHostOsHardening]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestImageSigningProvenance]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestNetworkSegmentation]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestRegistrySecurity]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[TestSupplyChain_1]] - code - gateway/tests/test_scanner_integration_coverage.py
- [[Write a file under the sandbox root, creating parents.]] - rationale - gateway/tests/test_scanner_integration_coverage.py
- [[_w()]] - code - gateway/tests/test_scanner_integration_coverage.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/_w
SORT file.name ASC
```

## Connections to other communities
- 14 edges to [[_COMMUNITY_test_scanner_integration_coverage.py]]
- 8 edges to [[_COMMUNITY__age()]]
- 4 edges to [[_COMMUNITY_TestProcScans]]
- 3 edges to [[_COMMUNITY_TestOpenscapSummary]]
- 3 edges to [[_COMMUNITY_TestTrivyImageSummaries]]
- 2 edges to [[_COMMUNITY_TestGetSbom]]
- 2 edges to [[_COMMUNITY_TestIsFresh]]
- 2 edges to [[_COMMUNITY_TestTextReaders]]
- 2 edges to [[_COMMUNITY_TestLoadLatestJson]]
- 2 edges to [[_COMMUNITY_TestResourceAvailability]]
- 2 edges to [[_COMMUNITY_TestDaemonConfigReader]]
- 2 edges to [[_COMMUNITY_TestMandatoryGates]]
- 2 edges to [[_COMMUNITY_TestSecretsManagement]]
- 1 edge to [[_COMMUNITY_TestClamavSummary]]
- 1 edge to [[_COMMUNITY_TestFalcoSummary]]
- 1 edge to [[_COMMUNITY_TestWazuhSummary]]
- 1 edge to [[_COMMUNITY_TestFluentBitSummary]]
- 1 edge to [[_COMMUNITY_TestSocketAndPidProbes]]
- 1 edge to [[_COMMUNITY_TestTrivySummary]]
- 1 edge to [[_COMMUNITY_TestAiModelSupplyChain]]
- 1 edge to [[_COMMUNITY_TestIdentityAuth]]

## Top bridge nodes
- [[_w()]] - degree 73, connects to 21 communities
- [[TestContainerRuntimeIsolation]] - degree 7, connects to 1 community
- [[TestDockerDaemonConfig]] - degree 6, connects to 1 community
- [[TestImageSigningProvenance]] - degree 6, connects to 1 community
- [[TestRegistrySecurity]] - degree 6, connects to 1 community