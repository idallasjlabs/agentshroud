# Graph Report - agentshroud-graphify  (2026-11-23)

## Corpus Check
- 2004 files · ~2,842,568 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 89 file(s) not represented in the graph (top: (none) 51, .done 6, .toml 5)

## Summary
- 41752 nodes · 61564 edges · 2835 communities (1860 shown, 975 thin omitted)
- Extraction: 93% EXTRACTED · 7% INFERRED · 0% AMBIGUOUS · INFERRED: 4467 edges (avg confidence: 0.9)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d26e248e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- MiddlewareManager
- AgentShroud Semgrep SAST Configuration
- _make_sanitizer
- middleware.py
- TelegramAPIProxy
- ResourceGuard
- test_soc_realtime_coverage.py
- gateway/ingest_api/ledger.py (DataLedger)
- ToolChainAnalyzer
- KillSwitchMonitor
- soc/router.py
- Progressive Trust Ladder (threshold-gated promotion + typed-violation demotion)
- FakeRBAC
- PIIConfig
- ToolResultInjectionScanner
- test_soc_router_coverage.py
- MemoryLifecycleManager
- Only DENY egress decisions persisted to audit store (ALLOW caused 57M+ row/32GB unbounded growth)
- ._make_proxy
- gateway/soc/auth.py (get_caller)
- services.py
- v0.9.0 cron-email fix: SMTP/IMAP ports 465/587/993 allowed for OpenClaw cron email
- CVE-2026-31045 — indirect prompt injection via tool results
- SSHProxy
- asyncio
- AsyncMock
- PathIsolationManager
- TrustManager
- RedactionResult
- get_trivy_summary
- EnhancedApprovalQueue
- test_e2e_proxy.py
- EdgeOAuthService
- lifespan.py
- asyncio
- load_config
- TestParanoidConfig
- PromptGuard
- _INTERNAL_SERVICE_ATTRS (internal gateway service table)
- main.rs
- test_web_api_coverage.py
- test_edge_service_routes.py
- test_agent_cve_registry.py
- verify-proxy.sh
- gateway/ingest_api/routes/dashboard.py (_create_ws_token)
- AgentTarget
- voice_gateway app (FastAPI)
- Sliding-window sentinel-joined security filter for streaming voice pipeline
- discover_upstream_versions.py
- api.py
- EdgeStore
- WebProxy
- TestConfigValidation
- test_llm_proxy.py
- PermissionLevel
- fake_urlopen
- PII Sanitizer Mitigation (Presidio + custom regex)
- IntelReportStore
- openclaw/skills/i-cr/SKILL.md
- EgressFilter
- .get_or_create_session
- group_workspace.py (GroupWorkspaceManager)
- ingest_api/main.py
- AuditChain
- scanner_integration.py
- test_voice_gateway.py
- version_routes.py
- test_scanner_integration.py
- UserSessionManager
- test_security_audit.py
- A2APolicyEngine
- NetworkValidator
- AgentRegistry
- test_soc_bots.py
- sync-cve-registry.py
- Test Falco Watcher Module
- SessionManager
- test_voice_latency_guard.py
- gateway/ingest_api/auth.py (RateLimiter, verify_token)
- DifferentialPIIDetector
- test_edge_facades.py
- test_http_proxy_coverage.py
- soc.js
- .from_source
- ToolResultSanitizer.sanitize_tool_result
- HTTPConnectProxy
- http_proxy.py (HTTPConnectProxy)
- cli/main.py
- _make_proxy
- TrustConfig
- hermes/skills/i-bs/README.md
- AgentShroud v0.8.0 "Watchtower" Release Plan
- KillSwitchConfig
- A2AProxy
- AgentShroud — System Overview
- chatbot/main.py
- ._extract_first_egress_target
- Privacy Policy Enforcement Tests
- test_ws_e_rt2_inbound_encoding.py
- DraftEntry
- test_mfa_guard.py
- app
- FalcoAlertWatcher
- WebProxyResult
- triage-cve-mitigations.py
- MCPToolCall
- Added
- TestEgressApprovalQueue
- test_edge_network_isolation.py
- find-ports.sh
- MCPPermissionManager
- _canonicalize_ip_literal
- patch
- CronStateMonitor
- test_collaborator_responses.py
- EncryptedStore
- PrivacyPolicyEnforcer
- .agents/skills/i-cr/SKILL.md
- upgrade-2026-09-21.md
- _make_proxy
- hc-ping.com must be egress-allowlisted or Hermes dead-man's-switch heartbeat fires permanently
- URLAnalyzer
- KeyRotationManager
- test_e2e_watchtower.py
- ApprovalRequest
- citation_verifier module
- sunday-upgrade-apply.sh
- fake_owner_notice
- EgressPolicy
- LLMProxy.proxy_messages (non-streaming)
- TestOutboundInfoFilter
- parse_trivy_output
- test_mcp_proxy_coverage.py
- gateway/security/skill_guard.py (SkillGuard)
- gateway LLM proxy local-model routing (llm_proxy.py)
- test_anthropic_openai_translator.py
- rewrite_registry_text
- web/api.py (POST /api/intel/reports)
- GroupWorkspaceManager
- upgrade-2026-10-12.md
- Slow-drip / coordinated multi-channel exfiltration anomaly detection
- Output Canary System Tests
- test_llm_proxy_failover.py
- KeyVault
- AgentShroud v0.7.0 Enforcement Audit Results
- ._run_and_read
- asyncio
- asyncio
- test_security_regressions_v1_2.py
- llm-init.sh
- aiohttp ClientSession closed-session crash-loop fix (partial)
- test_config_hot_reload.py
- Maloyan & Namiot 2026 — MCP security analysis (arXiv:2601.17548)
- 2. Security Analysis
- test_forward_stream.py
- ContainerSnapshot
- _engine
- SecurityPipeline
- Test DNS Blocklist Suite
- mcp
- telegram_proxy.py
- test_telegram_proxy_inbound.py
- IEC 62443 Compliance Matrix — AgentShroud
- test_redteam_probes.py
- AgentShroud Security Architecture
- test_telegram_replay.py
- dashboard.html (Control Center Template)
- test_bots_ssh_exec_wrapper.py
- Colima & Docker Operations Guide — AgentShroud
- _stub_client
- SCLClient
- DNSFilterConfig
- TokenValidator
- AgentShroud v0.9.0
- hermes/skills/i-cr/SKILL.md
- Skill: MCP AWS Profile Configuration (MCPM-AWS-PROFILE)
- _wrap_response
- Quality Assurance (SKILL)
- AgentShroud Agentic OS
- OpenClaw Workspace Usage Guide
- LOCAL_PROVIDER_KEY derivation (mode-derived, not ref-derived)
- test_hermes_model_resolver.py
- MCPServerConfig
- mcp_proxy.py
- MCPAuditTrail
- test_security_toolchain.py
- check_benchmark_regression.py
- _token
- test_runtime_engines.py
- Release Notes - AgentShroud v0.9.0
- EgressEvent
- setup-https-proxy proxyCreateConnection
- AgentShroud™ Brand Guidelines
- SecureBrowser - Enterprise Secure Browser Automation
- group_rbac.py (GroupRoleResolver)
- AgentShroud™ README
- Wu et al. 2026 — Browser-based attacks on AI agents (arXiv:2601.07263)
- _make_multipart_body
- Any
- Telegram Formatting Rule (bold only, no headers or tables)
- _make_cve
- GatewayEmailService
- AgentShroud Dev Environment — Raspberry Pi 4 (8GB) Setup Checklist
- get_engine
- SubagentMonitor
- test_gemini_openai_translator.py
- test_jira_dev_ticket.py
- TestMultiTurnTracker
- mock_stream
- SecureBrowser
- CI/CD Pipeline Advisor (SKILL)
- SecurityConfig
- Report Delivery Format Instructions
- AgentShroud Docker Configuration
- Auto-start a stopped Colima VM (step 1a)
- AgentShroud™ CVE Mitigation Matrix
- ContextGuard
- SecureBrowser
- OpenClaw Bot SSH Configuration
- SecureBrowser
- test_clamav_pipeline.py
- BrowserSecurityGuard
- test_session_manager.py
- SecureBrowser
- ProxyDashboard
- AppleContainerEngine
- TestNormalizeForSpeech
- check-vendor-compat.sh
- test_playback_state.c (host-native unit tests, SCRUM-59)
- lifespan
- test_mcp_proxy.py
- Step-by-Step Deployment
- _make_report
- OutputCanary
- SecureBrowser Skill
- Development Workflow: Read-Only Filesystem Strategy
- ADR-006: Multi-Runtime Container Support
- What Does OpenClaw Actually Need to Write?
- SCRUM-81 (Jira weekly review ticket)
- MetadataGuard
- gateway/runtime/config.py (RuntimeConfig)
- ConfigIntegrityMonitor
- SharedMemoryManager
- RateLimitGuard
- asyncio
- test_benchmark_regression.py
- Mac App Discovery Skill
- S8 no raw ssh/agentshroud-bot@/real Tailscale FQDN in baked bot config
- S6 setup-secrets.sh read_secret_masked routes display output to /dev/tty
- AgentShroud Documentation
- PodmanEngine
- _sleep
- TestPathIsolationManager
- .test_collaborator_web_access_imperative_with_url_queues_owner_approval
- ingest_api/config.py
- The 8D Investigation Process
- AWS Cloud Management & FinOps Agent
- The 8D Investigation Process
- AgentShroud Phase 3 - Quick Start Guide
- AgentShroud Audit Specification
- get_wazuh_summary
- key_rotation_config.py (KeyRotationConfig)
- Output Schema Enforcer Tests (C25)
- _make_filter
- Skill: UX Expert (UX)
- migrate-cve-registry-ghsa.py
- REQUIRED NOTES — PRODUCE EVERY ONE OF THESE
- Skill: UX Expert (UX)
- TestPIIDetection
- Security Architecture
- CREDENTIAL-PROTECTION-IMPLEMENTED.md
- AgentShroud Access Control Matrix
- CanaryTripwire
- DataExfilVolumeGuard
- SkillGuard
- Job details
- Browser — Secure Browser Automation
- Browser — Secure Browser Automation
- TestEgressTelegramNotify
- _w
- AgentShroud Weekly Upgrade — 2026-09-22 (DEV run, account: agentshroud-bot)
- test_skill_guard.py
- start-control-center
- Goal: Codex is a secondary/tertiary agent used for test augmentation, validation, and safe refactors AFTER tests pass.
- AgentShroud Device Pairing Management
- sunday-scan.sh
- AgentShroud v0.9.0 — Human Interface Testing Guide
- prompt_guard.py
- 10. Troubleshooting
- Local-Model Job Quality Matrix
- start.sh
- graphify reference: extra exports and benchmark
- Skills by Category
- graphify reference: extra exports and benchmark
- Skills by Category
- Container runtime auto-detection contract (SCRUM-92)
- test_scorecard_integrity.py
- asyncio
- _run_4b
- TestWebProxySecurityIntegration
- _t
- Security Module Inventory
- test_module_stats.py
- TestMultilingualInjection
- TestPromptProtection
- GroupRoleResolver
- ProgressiveLockdown
- A2APeerTestDouble
- Skill: MCP AWS Profile Configuration (MCPM-AWS-PROFILE)
- test_collaborator_tracker.py
- classify
- get_trivy_image_summaries
- GitGuard
- Skill: Mindmap Architect (MM)
- Skill: UI Expert (UI)
- Mode A — Single task
- iCloud Services
- TestProductionCompose
- Skill: Mindmap Architect (MM)
- test_env_guard_class.py
- Skill: UI Expert (UI)
- iCloud Services
- test_forward_routing.py
- Skill: MCP AWS Profile Configuration (MCPM-AWS-PROFILE)
- Slack Channel Setup
- forward-routing agent_id propagation into security pipeline
- Incident → Test Backfill Rule (R3 extension): every postmortem must add a regression test in the same PR as the fix, not deferred
- AgentShroud User Guide
- Skill: MCP AWS Profile Configuration (MCPM-AWS-PROFILE)
- Skill: MCP AWS Profile Configuration (MCPM-AWS-PROFILE)
- AgentShroud: A Transparent Proxy Framework for Enterprise Governance of Autonomous AI Agents
- Phase Review: P0 - Core Pipeline Wiring
- Telegram & Gmail Integration Guide
- test_cli_coverage.py
- Skill: MCP AWS Profile Configuration (MCPM-AWS-PROFILE)
- graphify reference: extra exports and benchmark
- Coding Agent (bash-first)
- .agents/skills/i-tw/SKILL.md
- Prompt: Daily Component Health Digest
- hermes/SOUL.md
- Atlas — Curriculum Architect
- wakeword.c
- Skill: MCP AWS Profile Configuration (MCPM-AWS-PROFILE)
- Skill: MCP AWS Profile Configuration (MCPM-AWS-PROFILE)
- _ctx
- AgentShroud Project Terminology
- AgentShroud Prerequisites
- AgentShroud Weekly Upgrade Report — 2026-08-30
- test_daily_cve_report.py
- test_jira_weekly_review.py
- test_scanner_integration_coverage.py
- test_soc_egress_endpoints.py
- OpenClaw Setup Guide - agentshroud.ai Bot
- TeamsConfig
- OutputSchemaEnforcer
- DELIVERABLE 1 — Domain-by-Domain Assessment
- Canvas Skill
- OWNER_USER_IDS bypass mechanism
- ws_client.c
- GroupRegistry
- Hermes v0.16.0 OpenAI-Client Compatibility Incident (3-day cron outage)
- _req
- TestCollaboratorPersistence
- apply-patches.js
- AgentShroud Operations Runbook
- Google Services Setup - Calendar, Contacts, Keep
- hermes_dashboard_ws_proxy
- ESP32-S3-BOX-3 Voice Terminal — Manual Setup Runbook
- daily_cve_report.py
- What You Must Do When Invoked
- Phase 3 Requirements: Working Chat Container
- OpenClaw Cron Jobs Reference & Recreation Guide
- DockerEngine
- Hermes Cron Jobs Reference & Recreation Guide
- is_quota_exhausted
- What You Must Do When Invoked
- System Instructions: Credential Security (Ultra-Conservative)
- AgentShroud Security Policy - Final Decision
- app_main.c
- HeuristicClassifier
- archive_old_events
- asyncio
- gen.py
- Telegram callback_query TTL expiry logged at DEBUG not ERROR
- xurl — Agent Skill Reference
- AWS Cloud Management & FinOps Agent
- AgentShroud Security Overview v0.8.0
- Workstream D — Sync agents/skills/MCP from `~/.llm_settings` into both bots
- ESP32-S3-BOX-3 Voice Terminal for Hermes (behind AgentShroud)
- Skill: MCP Auth Reset (MCPM-AUTH-RESET)
- Network Topology
- GIT-GUARD Skill Definition
- AWS Cloud Management & FinOps Agent
- PHASE_3A_3B_IMPLEMENTATION.md
- AWS Cloud Management & FinOps Agent
- AgentShroud Color Palette
- Credential Security Policy
- .cursor/mcp.json
- Skill: MCP Auth Reset (MCPM-AUTH-RESET)
- generate-cve-page.py
- agentshroud-ieee-paper.md
- Skill: MCP Auth Reset (MCPM-AUTH-RESET)
- .github/mcp.json
- .mcp.json
- .omp/mcp.json
- .pi/mcp.json
- 🛡️ AgentShroud Release Plan
- 1. Accomplishments This Phase
- make_httpx_fetcher
- WebContentScanner
- smoke.sh Startup Smoke Runner
- AgentShroud Security Value Proposition
- TestContributingMdAccuracy
- AWS Cloud Management & FinOps Agent
- Skill: MCP Auth Reset (MCPM-AUTH-RESET)
- AgentShroud Security Hardening Plan
- AWS Cloud Management & FinOps Agent
- Sunday Upgrade 2026-11-15 — DEV run (agentshroud-bot), 01:00–02:25 ET
- AgentShroud Deployment Architecture
- Skill: Technical Illustrator (TI)
- plan_remediation
- 1Password op-proxy (POST /credentials/op-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s)
- Enterprise Security Feature Priorities
- Skill: Technical Illustrator (TI)
- Phase 3: MITIGATE (Rollback First!)
- Skill: Technical Illustrator (TI)
- Skill: MCP Auth Reset (MCPM-AUTH-RESET)
- Voice Terminal — ESP32-S3-BOX-3 (Optional AgentShroud Add-On)
- OpenClaw Skill Metadata Schema (frontmatter convention)
- AgentShroud: Enterprise Governance for Autonomous AI Agents
- v0.8.0 — "Watchtower" (Complete Security + Everything We Know Today)
- agentshroud-blueteam/SKILL.md
- AWS Cloud Management & FinOps Agent
- Hermes Agent — Connection Setup
- heuristic_classifier.py (HeuristicClassifier)
- Skill: MCP Auth Reset (MCPM-AUTH-RESET)
- CollaboratorActivityTracker
- Skill: UX Expert (UX)
- Pre-Deployment Checklist
- ApprovalStore
- browser-extension/manifest.json
- AgentShroud Operations Cheat Sheet
- i-sec-defense SKILL (Blue Team Security Auditor, AgentShroud)
- Pre-Deployment Checklist
- Skill: UX Expert (UX)
- Pre-Purge Secret Rotation Checklist
- generate_branding_assets.py
- version_routes APIRouter — /api/v1/versions
- _AGENT_CVE_SOURCES
- jira_weekly_review.py
- Skill: UX Expert (UX)
- Deploying AgentShroud on Raspberry Pi (aarch64)
- iCloud Services Setup - Complete Guide
- ContributorManager
- Container Security Policy — AgentShroud
- test_file_sandbox_message_gate.py
- Skill: UX Expert (UX)
- Security Modules (58)
- Skill: UX Expert (UX)
- AgentShroud v0.8.0 "Watchtower" — Comprehensive Wiring Audit
- Skill: UX Expert (UX)
- graphify Skill
- Production Testing Procedures  ⚠️  NO SEPARATE DEV ENVIRONMENT
- Distributed OpenClaw Node Architecture — Raspberry Pi 4
- background.js
- dashboard/README.md
- Browser — Secure Browser Automation
- Production Testing Procedures  ⚠️  NO SEPARATE DEV ENVIRONMENT
- Production Testing Procedures  ⚠️  NO SEPARATE DEV ENVIRONMENT
- OpenClaw Management Scripts
- AgentShroud v0.8.0 — Full Security & Functionality Audit
- Multi-Agent Role Matrix
- AgentShroud Security Value Proposition - Revised
- REQUIRED NOTES — PRODUCE EVERY ONE OF THESE
- Cross-bot reply misrouting fix via contextvar-scoped send token
- Message Composition with MML (MIME Meta Language)
- Browser — Secure Browser Automation
- Wang et al. 2026 — Event injection attacks (arXiv:2602.08412)
- REQUIRED NOTES — PRODUCE EVERY ONE OF THESE
- Browser — Secure Browser Automation
- REQUIRED NOTES — PRODUCE EVERY ONE OF THESE
- Plan: AgentShroud Security Hardening — Real Agent Containment
- REQUIRED NOTES — PRODUCE EVERY ONE OF THESE
- Required: ≥ 4.5 for text, ≥ 3.0 for UI elements
- 3. AWS API MCP Authentication Reset
- Skill: MCP Doctor (MCPM-DOCTOR)
- Skill: Project Management (PM)
- Audit Ledger (SHA-256 hash only)
- setup-secrets.sh
- ManifestEntry
- AgentShroud Phase Review — 2026-02-24-final
- AgentShroud Data Dictionary
- model_usage.py
- 02-infrastructure.md
- AWS Cloud Management & FinOps Agent
- Required: ≥ 4.5 for text, ≥ 3.0 for UI elements
- 3. Brutally Honest Self-Assessment
- Skill: Project Management (PM)
- Required: ≥ 4.5 for text, ≥ 3.0 for UI elements
- Skill: MCP Doctor (MCPM-DOCTOR)
- test_playback_state.c
- AgentShroud Consolidated Issues Report
- Any
- AgentShroud Development Team — Agile Structure
- test_group_isolation.py
- test_security_integration.py
- pick_latest_stable
- Cosign signature verification of container images (fail-closed on missing binary/timeout/bad signature)
- TestToolResultSanitizer
- Sunday Upgrade 2026-11-08 (DEV run, account `agentshroud-bot`)
- Browser — Secure Browser Automation
- REQUIRED NOTES — PRODUCE EVERY ONE OF THESE
- Browser — Secure Browser Automation
- REQUIRED NOTES — PRODUCE EVERY ONE OF THESE
- Browser — Secure Browser Automation
- REQUIRED NOTES — PRODUCE EVERY ONE OF THESE
- AgentShroud™ — Project Knowledge Base
- API Keys Setup Guide
- Test-Driven Development README
- test_memory_lifecycle.py
- Route map (by router)
- v0.9.0 — "Sentinel" (Blue Team Remediation + Data Isolation + SOC)
- competitive-report-*.md dated reports
- Approval Queue (human-in-the-loop)
- AgentShroud Schema Documentation
- Phase 1 — Raw Collection
- AgentShroud Red Team Adversarial Tester
- Socrates — Dialogue Architect
- AgentShroud Red Team Adversarial Tester
- _run_asgi
- asyncio
- TestNewPatternsV080
- read_secret
- gh-issues — Auto-fix GitHub Issues with Parallel Sub-agents
- AgentShroud Weekly Upgrade — 2026-09-06
- Known Log Messages
- SecureBrowser Security Policies
- Skill Creation Process
- Inbound MCP Edge — Agent Coverage and Vendor Onboarding
- AgentShroud Incident Response Plan
- AlertTelegramRelay
- _is_op_reference_allowed
- AgentShroud Typography Guidelines
- ToolACLEnforcer
- Project Management (SKILL)
- Phase 3: MITIGATE (Rollback First!)
- Integration Guide
- deployment-mode.sh
- 10. Security Supply Chain Analysis
- Browser — Secure Browser Automation (SKILL)
- ServiceManager
- Phase 3: MITIGATE (Rollback First!)
- Atlas — Curriculum Architect
- Skill: MCP Auth Reset (MCPM-AUTH-RESET)
- TestManifest
- Currently Unmitigable Residual Class
- TestRejected
- AlertDispatcher
- _make_proxy
- ControlCenter
- AgentShroud — Master Feature List (Everything Ever Mentioned)
- Skill: Mindmap Architect (MM)
- Skill: UI Expert (UI)
- Implement gateway-level outbound information filtering module
- package_skill
- iCloud Services
- iCloud Services
- Function Details
- Function Details
- Skill: Mindmap Architect (MM)
- Detailed Profiles
- Skill: UI Expert (UI)
- iCloud Services
- Mode A — Single task
- Mode A — Single task
- LogBuffer
- Skill: Mindmap Architect (MM)
- Mode A — Single task
- Skill: UI Expert (UI)
- LOW — Informational
- Apple Services Setup Guide
- Enterprise Governance Proxy System (invention)
- MCP AWS Profile Configuration README
- Skill: MCP Auth Reset (MCPM-AUTH-RESET)
- Patch 1b — _send_to_platform Telegram call site (fixes cron Deliver:telegram bypass)
- AgentShroud Branding Assets Index
- AgentShroud Brand Quick Reference
- Browser Extension
- Contributing to AgentShroud™
- 03-data.md
- test_dns_canvas_coverage.py
- _handle
- test_soc_edge.py
- is_overloaded
- AuditStore
- canvas_proxy.py
- TestOAuthInjection
- test_cron_jobs_prompts.py
- _get_gmail_app_password
- check_command
- test_edge_profiles.py
- Deploying AgentShroud on Linux (x86_64 / aarch64)
- 3. Security Controls
- classify
- AgentShroud System Status Report
- TestFabricatedSecurityNotice
- AgentShroud Recovery Plan v0.4.0
- Remediation
- Implement per-user session isolation using Telegram user ID
- Remediation
- test_telegram_pipeline.py
- AgentShroud Sunday Upgrade — 2026-09-14 (dev account, agentshroud-bot@marvin)
- _call_llm_stream
- iCloud Services
- soc/models.py
- Skill: Mindmap Architect (MM)
- Skill: UI Expert (UI)
- Skill: Mindmap Architect (MM)
- Skill: UI Expert (UI)
- Security Implementation Verification
- iCloud Services
- Security Verification Report
- iOS / macOS Shortcuts — Relay to AgentShroud
- Skill: Mindmap Architect (MM)
- Skill: UI Expert (UI)
- iCloud Services
- AgentShroud macOS App Icon (1024x1024, Rounded Squircle)
- AgentShroud Security Assessment — v0.8.0
- Numbered security control catalog (C8, C9, C18, C47, ...)
- test-sunday-upgrade-scan.sh
- ADR-005: SHA-256 Hash Chain Audit Integrity
- ADR-001: Transparent Proxy vs Agent Modification
- Skill: Audit Branch (AB) — Merge Regression Detection
- Skill: Create PR with Pre-Flight Audit (CRPR)
- Mode A — Single task
- .agents/agents/i-tw.md
- internal network (isolated, internal:true)
- Gateway Management/Control-Plane API (v1.3.0)
- Apple Reminders CLI (remindctl)
- 8. Governance Model
- 1.4 Implementation Plan
- .cursor/agents/i-tw.md
- Skill: Audit Branch (AB) — Merge Regression Detection
- Skill: Create PR with Pre-Flight Audit (CRPR)
- update-bot-agents.sh
- openclaw/skills/i-tw/SKILL.md
- AgentShroud Blue Team Security Auditor
- Future Features & Roadmap
- Skill: Audit Branch (AB) — Merge Regression Detection
- Skill: Create PR with Pre-Flight Audit (CRPR)
- AgentShroud Phase Review — 2026-03-05 (Round 2)
- WebhookReceiver
- AuditExporter
- AgentShroud Blue Team Security Auditor
- Backup & Restore Runbook — AgentShroud
- test_shared_memory.py
- Docker Commands Reference
- i-tw.agent.md
- Gateway /mcp/proxy and /mcp/result endpoints
- Features
- .omp/agents/i-tw.md
- scripts/sync-cve-registry.py (GHSA auto-register)
- .opencode/agents/i-tw.md
- v1.3.0 — Platform Expansion (53 items)
- The 8D Investigation Process
- The 8D Investigation Process
- .new
- The 8D Investigation Process
- AgentShroud v0.8.0 "Watchtower" — Execution Summary (Draft)
- Phase 3A/3B Implementation Verification Results
- Make gateway source code, config, and security policies read-only to the agent
- AgentShroud Sunday Upgrade Report — 2026-09-20 (PROD run)
- parse_clamscan_output
- ServerConfig
- LockdownLevel
- browser_security.py
- test_tool_acl.py
- SSHResult
- ._run_proxy
- test_hermes_cron_seed.py
- TestMetadataGuard
- The 8D Investigation Process
- The 8D Investigation Process
- The 8D Investigation Process
- Per-agent API key scoping, redaction, leak detection, and rotation
- Mode A — Single task
- Mode A — Single task
- Phase 1 — Raw Collection
- tts.py
- Feature: Global Monitor-Only Mode ("Observatory Mode")
- OpenSCAP
- AgentShroud Security Verification (13-check driver)
- Phase 1 — Raw Collection
- browser-extension/package.json
- Mode A — Single task
- Applies to: Claude Code (primary) · Gemini CLI (secondary) · Codex CLI (tertiary)
- OpenClaw Bot Container
- Technical Specification
- Technical Specification
- Mode A — Single task
- Prod/Dev Env-Split Keep-List Defect
- Phase 1 — Raw Collection
- TELEGRAM_ISSUES.md
- SSH Capability Architecture Document
- AgentShroud -- USPTO Trademark Application
- What You Must Do When Invoked
- http_proxy.py
- fastapi.md
- DNSBlocklist
- ._relay
- sync-llm-settings.sh
- iCloud Services
- TestAuth
- GitHub Skill
- DNSForwarderProtocol
- Deploying AgentShroud on macOS (Apple Silicon / Intel)
- 4. Compliance & Standards Alignment
- v1.0.0 "Fortress" — Ship-Ready Public Release (116 items)
- 🟠 HIGH: Security & Logic Issues
- ._looks_like_safe_collaborator_info_query
- ._check_impl
- Flip core security modules from monitor to enforce mode
- Publish SecureBrowser to ClawHub - Step-by-Step Guide
- test_soc_services_coverage.py
- TestMultiBotContextvarRouting
- Mode A — Single task
- AgentShroud Deployment & Troubleshooting Runbook
- Phase 1 — Raw Collection
- canary-deploy.sh (blue/green canary deploy)
- Mode A — Single task
- Mode A — Single task
- consent_framework.py
- Mode A — Single task
- Phase 1 — Raw Collection
- WS-E Security Audit — AgentShroud v1.2 (Gateway + OpenClaw + Hermes)
- Mode A — Single task
- Mode A — Single task
- Phase 1 — Raw Collection
- mcp_oauth_preflight.py
- All Environment Variables
- AgentShroud Documentation
- Security Audit - One Shroud Over Every Wire
- Claude Code skill catalog (59 skills)
- docs/README.md
- Skill: Security Review (SEC)
- Workflow: Survey → Draft → Inject → Confirm
- Skill: Test-Driven Development (TDD)
- AgentShroud (system, C4 context)
- AgentShroud System Architecture Document (SAD)
- Per-Agent Container Isolation Architecture
- Core Components
- main.py
- Colima & Docker Operations Guide
- llm_proxy.py
- Mnemosyne — Retention Engineer
- Skill: Security Review (SEC)
- Workflow: Survey → Draft → Inject → Confirm
- Skill: Test-Driven Development (TDD)
- pipeline.py — Security Pipeline
- EgressTelegramNotifier
- TestKillSwitchScript
- Skill: Test-Driven Development (TDD)
- Skill: Technical Illustrator (TI)
- main command dispatcher (case $COMMAND)
- STPA-Sec Analysis of AgentShroud
- Skill: Technical Illustrator (TI)
- IDENTITY.md - Who I Am
- AgentShroud Security Scripts Reference
- SlackAPIProxy
- AuditEvent
- Steps
- test_image_verifier.py
- TestLogSanitizer
- Fixed
- OAuthSecurityValidator
- test_adversarial_injection.py
- TestAgentsRegistry
- export-bot-conversations.py
- TestSSRFDetection
- Skill: Technical Illustrator (TI)
- Skill: Technical Illustrator (TI)
- AgentShroud v0.8.0 — Peer Review Round 3 (FINAL)
- Critical Findings
- Skill: Technical Illustrator (TI)
- What You Must Do When Invoked
- multi-host-test.sh
- Pre-Deployment Checklist
- update-conduit-push.sh
- What You Must Do When Invoked
- Pre-Deployment Checklist
- Pre-Deployment Checklist
- 1. Accomplishments This Phase
- Findings
- Blue Team Security Assessment — AgentShroud v0.8.0 Round 3 (Final)
- jira_dev_ticket.py
- env_guard.py
- ._is_valid_domain_name
- AgentShroud™ v0.8.0 "Watchtower" — Complete Feature List
- Local LLM Support — Implementation Review
- ConsentFramework
- CredentialInjector
- asyncio
- TestEmailSend
- Technical Illustrator (i-ti)
- iMessage Integration Status
- Trademark Statements
- Credential Management - 1Password Integration
- Credential Isolation — Gateway op-proxy (ACTIVE)
- dashboard_bridge.py (Hermes)
- test_check_benchmark_regression.py
- Athena — Knowledge Distiller
- GSDE&G Development Master Checklist
- Athena — Knowledge Distiller
- .test_gives_up_and_marks_sent_after_max_retries
- gateway-seccomp.json (Docker seccomp profile)
- ledger row (id, timestamp, source, hashes, sanitized flag, expires_at)
- test_dashboard_endpoints.py
- Red Team Assessment v1.2.0
- SSH Configuration Guide
- MultiHostResult
- TestEdgeKill
- BlockingPipeline
- What You Must Do When Invoked
- Pre-Deployment Checklist
- 2026-03-08 — AI Engineering OS v1.0 Integration
- chat-console
- What You Must Do When Invoked
- AgentShroud™ — Trademark Prior Use Record
- Pre-Deployment Checklist
- What You Must Do When Invoked
- Pre-Deployment Checklist
- Post-v1.0.0 — Deferred
- Production Testing Procedures  ⚠️  NO SEPARATE DEV ENVIRONMENT
- Production Testing Procedures  ⚠️  NO SEPARATE DEV ENVIRONMENT
- AgentShroud Security Analysis & Hardening
- US_SSN regex tightened to exclude CVE IDs
- Add information filtering to prevent agent self-disclosure
- Browser-Fetch Skill for 1Password Share Links
- AgentShroud Weekly Upgrade Report — 2026-08-30
- AgentShroud Sunday Upgrade — 2026-09-06 (dev-only, read-only inventory → scoped fixes)
- Session Summary - February 14, 2026
- 1. Accomplishments This Phase
- AgentShroud v0.9.0
- Incident Response Playbook — AgentShroud
- TestExfiltrationDetection
- TestEgressFilterConfig
- EnvelopeSigner
- ToolResultSanitizerConfig
- _patch_urlopen
- Incident: Conduit/Hermes instability, 2026-10-16 (overnight)
- AgentShroud v0.8.0 — 25-Domain Prompt Injection Defense Assessment & Roadmap
- test_voice_stt_model_ab.py
- dashboard_endpoints.py
- _TrustCaptor
- TestBuildCollaboratorSafeInfoResponse
- TestVersionRoutes
- ADR-002: Default-Allow Security Philosophy
- Three-Network Architecture (external/mgmt/internal)
- ADR-007: Zero-Config Security (docker-compose up = fully secured)
- ADR-008-progressive-trust-levels.md
- Bear Notes
- sendMessage() JS — POST /forward from browser chat UI
- SecurityFinding
- Daedalus — Concept Illustrator
- Daedalus — Concept Illustrator
- gog/SKILL.md
- Recommendations for Production Deployment
- AgentShroud -- USPTO Provisional Patent Application
- ENTERPRISE GOVERNANCE PROXY SYSTEM AND METHOD FOR POLICY-ENFORCED INTERCEPTION, INSPECTION, AND MEDIATION OF AUTONOMOUS AI AGENT COMMUNICATIONS WITH EXTERNAL SYSTEMS
- Production Testing Procedures  ⚠️  NO SEPARATE DEV ENVIRONMENT
- Production Testing Procedures  ⚠️  NO SEPARATE DEV ENVIRONMENT
- Production Testing Procedures  ⚠️  NO SEPARATE DEV ENVIRONMENT
- Required: ≥ 4.5 for text, ≥ 3.0 for UI elements
- Skill: MCP Doctor (MCPM-DOCTOR)
- Common Operations
- tailscale-serve.sh
- Plan: Proxying HexStrike AI MCP Agents via AgentShroud
- Skill: Project Management (PM)
- Required: ≥ 4.5 for text, ≥ 3.0 for UI elements
- AgentShroud Recovery Plan v0.4.0
- Skill: MCP Doctor (MCPM-DOCTOR)
- Skill: Project Management (PM)
- Skill: MCP Doctor (MCPM-DOCTOR)
- Skill: Project Management (PM)
- start-agentshroud.sh
- Work Completed
- Updating AgentShroud
- Crash Recovery
- _age
- Telegram Channel Setup
- test_edge_fuzz.py
- ScanResult
- test_lifespan_prune.py
- OAuthRequest
- ADR-004: API Keys Never in Agent Container
- TestOpenAPIContract
- Skill: Data Validation (DATA-VAL)
- TestGroupRoleResolver
- test_hermes_forwarder_drops_non_http
- Identity Reference - AgentShroud System
- Required: ≥ 4.5 for text, ≥ 3.0 for UI elements
- AgentShroud Changelog
- AgentShroud Sunday Upgrade — 2026-09-23 14:00 ET (DEV run, afternoon continuation)
- 01-architecture.md
- Skill: MCP Doctor (MCPM-DOCTOR)
- Skill: Project Management (PM)
- Skill: Data Validation (DATA-VAL)
- Required: ≥ 4.5 for text, ≥ 3.0 for UI elements
- REPORT STRUCTURE
- Skill: MCP Doctor (MCPM-DOCTOR)
- Skill: Data Validation (DATA-VAL)
- Skill: Project Management (PM)
- Skill: MCP Tools Usage (MCP-TOOLS)
- REPORT STRUCTURE
- Required: ≥ 4.5 for text, ≥ 3.0 for UI elements
- 34 Security Modules Pipeline (P0-P3)
- Approval queue (notify Isaiah via Telegram, wait up to 1 hour)
- Skill: MCP Doctor (MCPM-DOCTOR)
- installer.py
- Skill: Project Management (PM)
- AgentShroud Red Team Adversarial Tester
- Socrates — Dialogue Architect
- AgentShroud Red Team Adversarial Tester
- Workflow (follow in order)
- ScanResult
- Socrates — Dialogue Architect
- AgentShroud Red Team Adversarial Tester
- 9. Deep Security Hardening (v0.9.0)
- Socrates — Dialogue Architect
- Socrates — Dialogue Architect
- Required Software
- One Shroud Over Every Wire: A Story About Trust, Isolation, and AI Assistants
- AgentShroud v0.7.0 — Red Team Remediation Plan
- Blue Team Security Assessment — AgentShroud v0.8.0 Round 2
- Findings & Mitigations
- AgentShroud Threat Model (STRIDE Analysis)
- AgentShroud Web Control Center - Implementation Summary
- AgentShroud Module Inventory
- Google Calendar & Contacts - Quick Setup
- alert_dispatcher.py
- drift_detector.py
- encrypted_store.py
- Function Details
- .get
- Function Details
- trust_manager.py
- test_channel_ownership.py
- A2APolicyConfig
- TestMemoryLifecycleManager
- Skill: Git Workflow Guardian (GIT-GUARD)
- Output Sections (ALL required)
- Skill: Pull Request (PR) Generator
- Management Dashboard
- test_middleware_coverage.py
- Socrates — Dialogue Architect
- TestObservatoryMode
- test_progressive_lockdown.py
- TestMultiBotIsolation
- Turbo Fieldfare (MLX inference backend)
- Discord (Via `message`)
- Skill: Git Workflow Guardian (GIT-GUARD)
- _patch_open
- .test_fetch_paginates_via_link_cursor
- Vulcan — Subject Matter Auditor
- Skill: Git Workflow Guardian (GIT-GUARD)
- MCPProxy
- Skill: Pull Request (PR) Generator
- TestReplayBufferOffsetParsing
- AgentShroud Gateway (holds 1Password service account)
- AgentShroud Data Flow Diagrams (doc)
- Claude Code (claude-sonnet-4-6) — Lead Engineer / Primary Developer
- Threat Model
- Voice Terminal Main IDF Component Manifest
- test_multi_host_test.py
- AgentShroud Red Team Adversarial Tester
- Socrates — Dialogue Architect
- session-prompt-setup.sh
- AgentShroud™ Communication Templates
- AgentShroud Red Team Adversarial Tester
- Socrates — Dialogue Architect
- AgentShroud Red Team Adversarial Tester
- 4. Defense-in-Depth Container Security
- v0.9.0 "Sentinel" — Data Isolation + SOC + Remediation (37 items)
- v0.8.0 "Watchtower" — Security Fixes + Module Wiring (104 items)
- AgentShroud Sunday Upgrade — 2026-09-23 (DEV run)
- Socrates — Dialogue Architect
- test_deployment_mode.py
- AgentShroud Red Team Adversarial Tester
- Actions
- generate-job-schedule.py
- tmux Session Control
- switch_model.sh
- STRIDE Threat Analysis
- Atlas — Curriculum Architect
- Phase 3: MITIGATE (Rollback First!)
- Atlas — Curriculum Architect
- properties
- Atlas — Curriculum Architect
- Phase 3: MITIGATE (Rollback First!)
- Layer-by-Layer Breakdown
- middleware.py
- models.py
- clamav_scanner.py
- 7. Pi-hole DNS Security Layer (Built-In)
- AgentShroud v1.2.0 — Blue Team Security Assessment
- AgentShroud v1.2.0 — Red Team Assessment
- server.py
- Function Details
- prompt_guard.py
- Function Details
- Gateway Python Dependencies (`gateway/requirements.txt`)
- CredentialInjectorConfig
- TestRewriteRequestHeaders
- TestStartupScannerKeying
- TestAtomicRegistryWrites
- Atlas — Curriculum Architect
- Features
- Phase 3: MITIGATE (Rollback First!)
- Hermes Dev Workflow (HDEV) Skill
- Atlas — Curriculum Architect
- Phase 3: MITIGATE (Rollback First!)
- Security Review (SEC)
- Key Skills in Detail
- Atlas — Curriculum Architect
- EU AI Act & NIST Alignment Matrix — AgentShroud™
- AgentShroud Hermes — System Identity
- Sunday Upgrade 2026-11-01 (DEV run, account agentshroud-bot)
- Oracle — Feedback Analyst
- AgentShroud Hermes — System Identity
- Daily CVE Triage & Remediation Scan
- Phase 3: MITIGATE (Rollback First!)
- Himalaya Configuration Reference
- Common Queries
- test_colima_and_sdk_patch_fallback_resolution.sh
- Output Sections (ALL required)
- properties
- Planning Docs Index (redteam, reviews, recovery, version buckets)
- SECTION 1: COVER SHEET (Form PTO/SB/16)
- SECTION 3: DRAWINGS
- ota.c
- Output Sections (ALL required)
- Himalaya Email CLI
- _run
- auth.py
- TestAggregateResults
- ledger.py
- sanitizer.py
- version_routes.py
- Function Details
- apple_engine.py
- Function Details
- agent_isolation.py
- dns_filter.py
- wazuh_client.py
- ANTHROPIC_BASE_URL
- Attack Teardowns: How AgentShroud Stops RovoBlast and Cross-Turn Coordination Attacks
- agentshroud-bot
- agentshroud-gateway
- PathRewriteResult
- TestMemoryIntegrityMonitor
- _FakeRBAC
- TestWebSocketHandshakeAuth
- _audit_entry
- Output Sections (ALL required)
- Output Sections (ALL required)
- A2A (Agent-to-Agent) Protocol Threat Analysis
- ADR-001: Transparent Proxy Decision
- Output Sections (ALL required)
- Examples
- Skill: Audit Branch (AB) — Merge Regression Detection
- Skill: Create PR with Pre-Flight Audit (CRPR)
- System Audit & Documentation
- AgentShroud Blue Team Security Auditor
- System Audit & Documentation
- SSH Proxy Threat Model (6 threats)
- AgentShroud Blue Team Security Auditor
- Skill: Audit Branch (AB) — Merge Regression Detection
- Skill: Create PR with Pre-Flight Audit (CRPR)
- §3 — Bot Pipeline Integrity Checks
- §1 — Re-run of Prior Scenarios
- System Audit & Documentation
- AgentShroud Blue Team Security Auditor
- System Audit & Documentation
- System Audit & Documentation
- Deployment Runbook — AgentShroud
- Available MCP Servers
- CI/CD Quality Gates (14 jobs, 6 workflows)
- Docker Compose (infra diagram)
- Migration Path (SSH → Distributed Node)
- OpenClaw Control UI Pairing Instructions
- Telegram Bot Setup for OpenClaw
- i-gg SKILL — Git Workflow Guardian (GIT-GUARD)
- i-icloud SKILL — iCloud Services
- Skill: CI/CD Pipeline Advisor (CICD)
- Domain allowlisted? (agentshroud.yaml proxy.allowed_domains)
- Bot Container (agent decides: reply + tool call)
- What is the symptom?
- Phase 2 — Security Core (HMAC Auth + PII Sanitizer, HTTP CONNECT Proxy, Approval Queue)
- 1Password Vault Sharing Instructions
- BROWSER_FETCH_SKILL.md
- AgentShroud Sequence Diagrams
- Shutdown & Recovery
- mcp_audit.py
- gh-issues/SKILL.md
- Sprint Cadence Decision
- mcp_inspector.py
- i-ti SKILL.md (Technical Illustrator, Mermaid diagrams)
- telegram_proxy.py
- web_content_scanner.py
- MCP Auth Reset Skill
- `docs/planning/` — Index
- docker_engine.py
- Synthetic /v1/models/<id> shim for hermes v0.16.0 OAuth-token preflight incompatibility
- 📋 Detailed Step-by-Step
- egress_config.py
- egress_filter.py
- canary-deploy.sh
- egress_monitor.py
- gemini-review.py
- falco_monitor.py
- input_normalizer.py
- scripts/security-scan.sh
- Competitive Security Matrix — AgentShroud vs AI Agent Platforms
- OPENCLAW_SANDBOX_MODE
- check_upstream_cves
- DelegationManager
- ReportStore
- run_trivy_scan
- TestEnvelopeSigner
- _tool_req
- multi_host_test.py
- patch
- DELIVERABLE 3 — v0.8.0 Implementation Items
- _mock_dir_with_files
- §4 — Hermes-Specific Section (NEW — first assessment)
- §2 — New Multi-Bot Attack Scenarios (v1.1+ Surface)
- TestCheckClamd
- Docker Desktop Network Settings — Cisco AnyConnect VPN Compatibility
- _sync
- TestOriginAwareAuthorization
- AGENTS.md — Codex CLI Guidance
- Claude Code — Primary development agent
- Skill: Audit Branch (AB) — Merge Regression Detection
- Skill: Create PR with Pre-Flight Audit (CRPR)
- i-eightd SKILL — 8D Root Cause Analysis
- System Audit & Documentation
- AgentShroud Blue Team Security Auditor
- Test Coverage Report (AgentShroud v1.3.0)
- Skill: Audit Branch (AB) — Merge Regression Detection
- Skill: Create PR with Pre-Flight Audit (CRPR)
- System Audit & Documentation
- AgentShroud Blue Team Security Auditor
- Skill: Audit Branch (AB) — Merge Regression Detection
- Tailscale mesh VPN (tail240ea8.ts.net)
- AgentShroud Sequence Diagrams (doc)
- AgentShroud State Diagrams (doc)
- Assess severity
- agentshroud-gateway container (starts first)
- SECTION 2: MARK INFORMATION
- AGENTSHROUD standard character mark
- iot_button_register_cb
- iot_button_register_cb
- AgentShroud State Diagrams
- telegram_egress_notify.py
- SubagentMonitor._log_event
- ToolChainAnalyzer.analyze_tool_call
- 🎯 High-Value Features (Justify the Effort)
- Skill: Create PR with Pre-Flight Audit (CRPR)
- System Audit & Documentation
- AgentShroud Blue Team Security Auditor
- sync-version.sh
- GitHub Branch Protection — `main`
- main
- 75 Security Modules
- skill.json
- test_wire_llm_settings.js
- container-runtime.sh (detection shim)
- Technical Specification
- Technical Specification
- AgentShroud Brand Guidelines
- allowed_hours
- Future Enhancements
- properties
- Technical Specification
- Output Sections (ALL required)
- Output Sections (ALL required)
- AgentShroud™ Brand Guidelines
- 1password-skill.sh
- mcp-proxy-wrapper.js
- AgentShroud Control UI Connection Guide
- Use Cases
- event_bus.py
- mcp-proxy-wrapper.js
- Function Details
- url_analyzer.py
- security.py
- Procedure
- Voice Gateway Service (STT/TTS WebSocket Bridge to Governed Path)
- Skill: Pre-Change Analysis (PCA)
- v1.6.0 Release — Voice Terminal
- canary.py
- Key Benefits
- log_sanitizer.py
- trivy_report.py
- Gateway Container Startup Failures
- ClamAV (malware detection)
- Secret Backend Cascade (macOS Keychain → 1Password CLI → homedir file)
- Browser — Secure Browser Automation
- Daedalus — Concept Illustrator
- _output
- ._rewrite_known_runtime_errors
- iCloud Data Manager (ICLOUD)
- GroupRole
- ToolResultSanitizer
- _run
- TestDeterministicPresidioInit
- TestParseHostsLine
- test_group_rbac.py
- Incident Response (INCIDENT)
- Security Controls
- TestReadOnlyMemberGroupContext
- TestHeuristicClassifier
- Socrates — Dialogue Architect
- TestInfoLeakage
- TestEgressFilter
- _patch_exists
- TestWebSearchLog
- _entry
- Technical Specification
- Daedalus — Concept Illustrator
- Data Validation (DATA-VAL)
- 8D Root Cause Analysis
- Hermes — Podcast Production Orchestrator
- iCloud Data Manager (ICLOUD)
- Technical Specification
- MCP Auth Reset (MCPM-AUTH-RESET)
- Technical Specification
- Sunday Upgrade 2026-11-22 (DEV run, account `agentshroud-bot`)
- Morning Checklist (5 minutes)
- asb
- Part 2 — Red-Team Attack Run (SCRUM-73)
- Skill: Security Review (SEC)
- Workflow: Survey → Draft → Inject → Confirm
- Skill: Test-Driven Development (TDD)
- Salesforce CLI (`sf`) Agent
- Salesforce CLI (`sf`) Agent
- forwarder.js
- Summary
- test_collaborator_greeter.py
- SOC Command Center — Five Pillars
- active
- COMMUNICATION-TEMPLATES.md
- SECTION 9: IMPORTANT NOTES
- Default Monitor-Mode Egress Rationale
- AgentShroud Data Flow Diagrams
- Changelog — AgentShroud™
- Skill: Security Review (SEC)
- Workflow: Survey → Draft → Inject → Confirm
- Skill: Test-Driven Development (TDD)
- Salesforce CLI (`sf`) Agent
- AgentShroud™ Security Policy
- AgentShroud Weekly Upgrade — 2026-09-21 (DEV run, account: agentshroud-bot)
- Skill: Security Review (SEC)
- Pre-commit hook strategy (framework vs manual)
- browse.py — SecureBrowser CLI (OpenClaw)
- Workflow: Survey → Draft → Inject → Confirm
- Troubleshooting
- 🆘 Troubleshooting
- AgentShroud v0.7.0 - Blue Team Security Audit Report
- v0.6.0 Baseline Results
- agentshroud-manage.sh
- launch-instance.sh
- openclaw_triage.sh
- Step-by-Step Installation
- I - Information Disclosure
- router.py
- mcp_config.py
- web_proxy.py
- compose_generator.py
- config.py
- agentshroud.yaml
- test_all_modules_enforce.py
- Docker Volumes
- Troubleshooting Matrix
- Health Checks
- Kill Switch Procedure
- parse_query
- EnvironmentGuard
- make_fake_socket_module
- ._suppress_qwen3_thinking
- test_delegation.py
- TestCanvasAuthHelpers
- test_integration.py
- run_multi_host
- TestGroupMemoryWriteACL
- TestTelegramTokenRegistry
- TestParseModeStrippedAfterPIIRedaction
- API Documentation
- Resources
- camsnap/SKILL.md
- Canvas Upstream Hostname Regression (v1.1.0 container rename)
- test_us_ssn_regex_tightened.py
- Fail-Closed Outbound: pipeline exception blocks delivery to non-owner
- Skill: Security Review (SEC)
- GSDL-715 (silent regression incident)
- agent_isolation.py (AgentRegistry)
- Workflow: Survey → Draft → Inject → Confirm
- Salesforce CLI (`sf`) Agent
- Skill: Test-Driven Development (TDD)
- pending (bot submits action requiring approval)
- Outbound Infrastructure Content Filter (deny-list for hostnames, tool names, user IDs)
- Red Team Finding 02: No Human Approval for High-Risk Tool Calls
- Skill: Security Review (SEC)
- Workflow: Survey → Draft → Inject → Confirm
- Skill: Test-Driven Development (TDD)
- SECURITY_VALUE_PROPOSITION.md
- test_container_dns_check.py
- Incident Log — Conduit connectivity + prod stability, 2026-10-15/16
- Salesforce CLI (`sf`) Agent
- Skill: Security Review (SEC)
- i-vulcan SKILL.md (Subject Matter Auditor, podcast QA gate)
- MCP OAuth preflight checker (mcp_oauth_preflight.py)
- pre-commit-hook.sh
- Workflow: Survey → Draft → Inject → Confirm
- 8D Root Cause Analysis SKILL (OpenClaw)
- iCloud Services Skill
- Skill: Test-Driven Development (TDD)
- Salesforce CLI (`sf`) Agent
- lib.sh
- Technical Details
- Manual Usage (Current Method)
- 🎨 Customize Skill Page (Optional)
- Usage
- Dockerfile — Gateway
- Athena — Knowledge Distiller
- GSDE&G Development Master Checklist
- Athena — Knowledge Distiller
- Salesforce CLI (`sf`) Agent
- TestLifespan
- Athena — Knowledge Distiller
- GSDE&G Development Master Checklist
- AgentShroud™ — OpenClaw Local-Model Tool-Use Instructions
- setup-https-proxy.js
- GSDE&G Development Master Checklist
- DEVELOPER.md — Development Context for AgentShroud
- colima-health-check.sh
- CVE Registry — Manual Review List
- workspace.sh
- ADR-009: Enforce-by-Default Security Philosophy
- Inbound MCP Edge — Plan (awaiting owner approval)
- Inbound MCP Edge — Design
- Collaborator Setup Checklist
- Startup Sequence
- E - Elevation of Privilege
- ssh_config.py
- apply-patches.js
- forwarder.py
- web_config.py
- First Time Setup
- _FakeWSConnect
- compute_backoff
- get_sbom
- ._is_domain_allowed
- TestMemberGroupContext
- §5 — Trivy Container Scan Results
- _fake_stats
- Startup Flow Diagram
- deploy-crush.sh — global Crush skill deployment
- graphify reference: GitHub clone and cross-repo merge
- graphify reference: transcribe video and audio
- Audit Branch (Merge Regression Detection)
- kaizen Skill (stub)
- 75 Active Security Modules — no stubs, fully wired
- MCP tools available — GitHub (repos/PRs/issues), Atlassian (Jira/Confluence)
- shared network (sidecar mode bridge)
- Claude Code (PRIMARY agent)
- blogwatcher/SKILL.md
- blucli/SKILL.md
- browser-fetch skill.json (tool manifest)
- TestKillSwitchVerification
- [1.3.0] "Reliability" (2026-07-21)
- TestSetMode
- statusline.sh
- EU AI Act & NIST Alignment Matrix
- gen-code-graph.sh
- AgentShroud Config with Tool Risk Tiers (example)
- Changed
- OpenClaw cron: Collaborator Report - Morning (Telegram HTML, PII filter rules)
- graphify reference: GitHub clone and cross-repo merge
- graphify reference: GitHub clone and cross-repo merge
- openclaw-identity.md (OpenClaw bot identity)
- upgrade.sh
- Diagram 08: Entity Relationship Diagram
- Gateway observability (GET /status, GET /ledger, MCP audit log, HTTP CONNECT proxy stats)
- eightctl/SKILL.md
- test_playback_state/stubs/freertos/FreeRTOS.h
- FakeClock
- test_wakeword_state/stubs/freertos/FreeRTOS.h
- TestRBACConfig
- agentshroud-gateway pyproject config
- Agent CVE Registry module (_AGENT_CVE_REGISTRIES etc.)
- MemoryIntegrityMonitor
- TrustManager._update_score
- Test Kill Switch Monitor
- TestIsContainerRunning
- TestWebSecurity
- .test_full_access_collaborator_passes_despite_multi_turn_middleware_block_without_interrogative
- AgentShroud Weekly Upgrade — 2026-09-20 (DEV run, account: agentshroud-bot)
- startInstall
- gifgrep/SKILL.md
- goplaces/SKILL.md
- .test_activity_command_renders_entries
- TestSSRFBlocking
- Athena — Knowledge Distiller
- GSDE&G Development Master Checklist
- i-hermes README (Podcast Production Orchestrator)
- kaizen Skill (stub)
- pre-commit as single owner of .git/hooks/pre-commit
- deploy.sh
- promote-firmware.sh
- Athena — Knowledge Distiller
- GSDE&G Development Master Checklist
- Athena — Knowledge Distiller
- GSDE&G Development Master Checklist
- init_skill.py
- Weather Skill
- chat_console.py
- Daedalus — Concept Illustrator
- Daedalus — Concept Illustrator
- docs
- Accepted-Risk Register for Sunday Upgrade CVE Gate
- .agents/skills/graphify/references/extraction-spec.md
- .agents/skills/i-agile/SKILL.md
- .agents/skills/i-architecture-review/SKILL.md
- .agents/skills/i-chaos-engineering/SKILL.md
- .agents/skills/i-devsecops/SKILL.md
- .agents/skills/i-incident-response/SKILL.md
- .agents/skills/i-kanban/SKILL.md
- .agents/skills/i-observability/SKILL.md
- Scrum Ceremony Facilitation
- .agents/skills/i-scrum/SKILL.md
- .agents/skills/i-value-stream-mapping/SKILL.md
- Prove the Outcome, Never the Steps — assert on state deltas not exit codes
- asb CLI — Deployment Tool
- Daedalus — Concept Illustrator
- run-standalone.sh
- Inbound MCP Edge — Phase 0 Discovery
- Tailscale Remote Access Setup
- Control-Plane / Data-Plane Separation
- Gateway-Enforced Intel Verification (SCRUM-75)
- GitGuardian ignored-paths + ignored-matches for synthetic test fixtures
- Trivy (vulnerability scanner)
- AGENTSHROUD_ENV auto-detected from invoking account
- hermes/skills/graphify/references/extraction-spec.md
- Constrained query-vocabulary expansion
- ElevenLabs Text-to-Dialogue API
- Git History Purge Plan
- hermes/skills/i-chaos-engineering/SKILL.md
- i-daedalus README — Concept Illustrator
- hermes/skills/i-devsecops/SKILL.md
- i-hermes README — Podcast Production Orchestrator
- i-incident-response SKILL (stub)
- hermes/skills/i-incident-response/SKILL.md
- hermes/skills/i-kaizen/SKILL.md
- hermes/skills/i-kanban/SKILL.md
- i-mac README — macOS System Administrator (MAC)
- Quick Reference — AgentShroud
- hermes/skills/i-scrum/SKILL.md
- hermes/skills/i-value-stream-mapping/SKILL.md
- graphify.serve MCP stdio Server
- openclaw/skills/graphify/references/extraction-spec.md
- graphify clone command
- EnhancedApprovalQueue (`enhanced_queue.py`)
- sidecar.py
- curriculum.md (input requirement)
- openclaw/skills/i-chaos-engineering/SKILL.md
- openclaw/skills/i-incident-response/SKILL.md
- Dockerfile — Bot (OpenClaw)
- ._handle
- APPROVAL_ITEMS entity
- Diagram 18: Runbook
- Alert Thresholds (approval queue 1h timeout, context 200K hard limit, op-proxy 6 retries)
- Hermes Cannot Force-Switch to Custom-Named Local Model (Gap #8)
- Architecture Overview.md
- SlackSocketClient
- audio.c (ES7210 mic / ES8311 speaker driver)
- _PII_PATTERNS (URL PII regex set)
- deep_security_test
- Scorecard Data Integrity Tests (no stub inflation)
- MiddlewareManager Session Enforcement Tests
- SharedMemoryManager Merged Memory Tests
- SlackAPIProxy Socket Mode Relay (apps.connections.open) Tests
- SOC Auth WS Token Issuance/Redemption Tests
- SOC Models SecurityEvent Tests
- InstructionEnvelope
- FileIntegrityRecord
- ContentThreat
- ._get_engine
- TestClassicOverride
- test_api_contract_fuzz.py
- test_credential_injector.py
- checkPrereqs
- loadRuntimes
- Dependabot Configuration
- test_egress_callback_stale.py
- i-tdd README.md
- Internal MCP gateway pattern (Entra-fronted)
- Red-Green-Refactor TDD loop (playbook)
- Secret-in-history remediation (BFG / git-filter-repo)
- Branding Specialist README (OpenClaw)
- Daedalus Concept Illustrator README (OpenClaw)
- Rationale: agentshroud-gateway MCP server disabled (no /mcp route, crash-loop correlation)
- test_proxy_gemini_translation_failure_falls_through_gracefully
- bsp/esp-bsp.h stub (playback state test)
- freertos/FreeRTOS.h stub (playback state test)
- feature-priorities.md
- plan.md
- ContextGuard Bug — should_block_message() Always Returns False (monitor-only in enforce mode)
- activate-lockdown.sh
- canary-cron.sh
- TestInboundChokepointWiring
- codex-review.sh
- TestScanParameterAllowlists
- deploy-gateway.sh
- egress-iptables.sh
- emergency-rollback.sh
- parse_hosts
- export-openapi.sh
- TestCollabLockdownNotifications
- TestResourceGuardAlertBridge
- test_scorecard_scoring.py
- TestEgressSSRF
- run-tests-batched.sh
- TestListServices
- TestServiceManagerGetLogs
- _adv
- TestTelegramProxyRouteMultiBot
- TestTrustProgression
- Daedalus — Concept Illustrator
- Daedalus — Concept Illustrator
- Daedalus — Concept Illustrator
- export-email-reports.py
- oracle — best use
- Skill: Data Validation (DATA-VAL)
- Available MCP Servers
- verify-greeter-state.sh
- agentshroud-blueteam/references/steve-hay-assessment.md
- browser/package.json
- agentshroud-redteam/references/steve-hay-assessment.md
- agentshroud-redteam/references/steve-hay-plan.md
- S3 apply-patches.js validates xoxb-/xapp- Slack token prefixes
- AgentShroud Sunday Upgrade — 2026-09-26 (DEV run)
- skills/icloud/scripts/calendar.js
- dlp
- Skill: Data Validation (DATA-VAL)
- Available MCP Servers
- Security Pipeline Flow
- hermes/skills/i-browser/package.json
- hermes/skills/i-icloud/scripts/calendar.js
- openclaw/skills/i-browser/package.json
- Owner-elevation-over-unverified-origin refusal (owner directive 2026-09-15)
- openclaw/skills/i-icloud/scripts/calendar.js
- container-net-diag.sh
- Cross-Turn Correlation Capability
- ADR-003: Two-Network Container Isolation
- iMessage Integration Fix - Using imsg + imessage-exporter
- How to Fix (5 Minutes)
- AgentShroud™ LLM Provider Setup & Switching Guide
- engine.py
- docker-compose.yml
- v0.8.0 Watchtower Complete Feature List Final
- Agile Skill (stub)
- Architecture Review Skill (stub)
- BDD Skill (stub)
- Chaos Engineering Skill
- Create PR with Pre-Flight Audit (CRPR) Skill
- DevSecOps Skill
- Observability Skill
- Pre-Change Analysis (PCA)
- Session Prompt Generator
- SRE Practices
- Value Stream Mapping Skill
- Build-config pinning — sdkconfig.defaults pins TCP_MSS/stack/WDT/TCP buffers
- scripts/check-vendor-compat.sh — A2A JSON-RPC smoke check
- deepseek-r1-0528-qwen3-8b 404 — alias mismatched oMLX real catalog ID
- nemotron-named models misclassified as needing cloud provider in local mode
- omlx-keepwarm.sh — keeps gemma model resident (cold 5.06s vs warm 0.69s)
- Voice robustness — volume-command STT tolerance + stream timeout/repr logging
- Approval queue — email/file-deletion/external-API/skill-install must route through it
- Docker sidecar integrity — falco/clamav/fluent-bit in-process, wazuh-agent standalone sidecar
- Graphify query-first-then-keep-current workflow
- Knowledge Map — Obsidian vault entry points
- Multi-Agent Hierarchy — Claude primary, Gemini/Codex secondary/tertiary
- No Security Theater — no stubs/placeholders/fake green
- Performance baseline — inbound latency <0.5ms arm64/macOS
- PII redaction — presidio engine 0.9 confidence minimum
- Prime Directive — no new files, minimal diffs
- Test-Driven Development default (Red-Green-Refactor)
- MCP Server: atlassian-fluence
- MCP Server: atlassian-idallasj
- MCP Server: awslabs.aws-api-mcp-server
- MCP Server: devonthink
- MCP Server: github
- MCP Server: github-fluence
- MCP Server: github-idallasj
- MCP Server: home-assistant
- MCP Server: safari
- MCP Server: xmind
- Generic AI Agent Integration (HTTP Proxy Mode)
- EnhancedApprovalQueue.broadcast (SCRUM-154 bounded)
- EnhancedApprovalQueue.decide
- EnhancedApprovalQueue._notify_telegram
- EnhancedApprovalQueue.submit
- EnhancedApprovalQueue.submit_tool_request
- EnhancedApprovalQueue.wait_for_decision
- Seccomp Profiles
- SCRUM-154 Fix: submit()/decide() held the approval lock while broadcasting to a hung WebSocket client, deadlocking indefinitely — fixed with a bounded per-client broadcast timeout
- MCP Integrations (GitHub, Atlassian, AWS, XMind)
- Atlassian MCP Server (Jira + Confluence, concept)
- AWS API MCP Server (concept)
- AWS Athena (data lakehouse)
- AWS Glue Jobs
- AWS Step Functions
- Performance Baseline v1.0.0
- AgentShroud Logo — Glow/Light Variant
- Apple Touch Icon (AgentShroud logo mark)
- Favicon 128x128 (AgentShroud logo mark)
- Favicon 16x16 (AgentShroud logo mark)
- Favicon 256x256 (AgentShroud logo mark)
- Favicon 32x32 (AgentShroud logo mark)
- Favicon 512x512 (AgentShroud logo mark)
- Favicon 96x96 (AgentShroud logo mark)
- PWA Icon 192x192 (AgentShroud logo mark)
- App Icon 128x128 (AgentShroud logo mark)
- App Icon 16x16 (AgentShroud logo mark)
- App Icon 256x256 (AgentShroud logo mark)
- App Icon 32x32 (AgentShroud logo mark)
- App Icon 512x512 (AgentShroud logo mark)
- AgentShroud Badge Icon 180x180
- AgentShroud Badge Icon 60x60
- AgentShroud Logo on Brand Blue Background
- AgentShroud Logo on Dark Background
- AgentShroud Logo on White Background
- AgentShroud Presentation Content Slide Template
- AgentShroud Presentation Title Slide
- AgentShroud GitHub Social Preview Image
- AgentShroud LinkedIn Banner
- AgentShroud LinkedIn Profile Image
- AgentShroud Open Graph Preview Image
- AgentShroud Telegram Avatar
- AgentShroud Twitter/X Header
- AgentShroud Twitter/X Profile Image
- HTTP 401 — Unauthorized
- Egress Filter Errors
- LLM Operating Context — Isaiah Jefferson
- Chatbot Service Dependencies (requirements.txt)
- Error Index
- Restart Procedure
- TestAuditStore
- agentshroud-soc Cargo package
- TestCredentialInjector
- Critical/High/Medium/Low tool risk tiers gating approval requirement
- TestCredentialLeakDetection
- CVE-2026-35190 — execute_command owner-only fix
- CVE-2026-9367 — command injection bypass via terminal_tool
- TestAuditTrail
- ConfigurationSetting (data entity)
- DNSQuery (data entity)
- SessionState (data entity)
- TestSecurityPolicyProtection
- TestReadAccess
- AGENTSHROUD_VERSION fallback to docker/versions.env
- Cron: Agentic AI Threat Intelligence
- OpenClaw cron: Agentic AI Threat Intelligence
- Cron: Daily Competitive Analysis Email
- Cron: Monthly Chaos Engineering Drill
- docker-compose.secure.yml — Proxy Mode Deployment
- docker-compose.sidecar.yml — Sidecar Mode Deployment
- Newsletter: Chat Front-ends & Search Infra
- Newsletter: Coding Agent CLIs
- Newsletter: Mac Clustering
- Newsletter: Model Version Tracker
- Newsletter: Personal AI Assistants
- Weekly Hermes Stability Report
- --watch debounce avoids per-file rebuild storms
- Token-reduction benchmark gated at 5,000 words
- Node ID format must match AST extractor
- Per-subfolder graphify-out avoids output clobbering
- LLM writes its own Whisper domain-hint prompt
- build_merge() avoids NetworkX round-trip (#801)
- Prune old nodes for changed files before AST re-insert (#1178)
- /i-crpr skill
- .github/workflows/merge-regression-audit.yml
- Raw-flag triage discipline (74-merge sweep)
- Vulcan (i-vulcan skill, script approver)
- BDD Skill (Gherkin Given/When/Then specs)
- browser-fetch package.json
- Chaos Engineering Skill
- i-devsecops SKILL (stub)
- i-gitops SKILL (stub)
- Jira Ticket Per Dev Batch (Standing Rule)
- i-kanban SKILL (stub)
- i-scrum SKILL
- i-sdlc SKILL
- Stale Cron Session Claim Cleanup
- CVE Triage Report Cron Prompt
- /graphify add URL Ingestion
- Token Reduction Benchmark
- Neo4j Export / Push
- Hyperedges Rule (max 3/chunk)
- Native CLAUDE.md Integration
- /graphify explain command
- /graphify path command
- Self-Written Whisper Domain-Hint Prompt
- --cluster-only Flow
- Community Detection / Clustering
- Cumulative Token Cost Tracker
- Gemini Semantic Extraction Backend
- Obsidian Vault Export (opt-in --obsidian)
- scripts/audit_merge_regression.py
- .github/workflows/merge-regression-audit.yml
- podcast_plan.json (voice config)
- script.md (Vulcan-approved dialogue input)
- Audit-log-every-fetch design rationale
- GSDE&G Skills Reference Guide
- docker/QUICKSTART.md — 5-minute stack launch guide
- Dev VM CPU niceness enforcement (step 1b)
- docker/versions.env version pins
- Roadmap (v0.9.5 → v0.9.8 → v1.0.0 → Post-v1.0.0)
- AgentShroud Gateway OpenAPI Spec v1.2.1
- API Documentation (planned, under development)
- Diagram 07: Data Flow
- SCHEMA_VERSION entity
- Diagram 12: Credential Flow
- Diagram 17: State — Bot Session
- Diagram 20: Observability Map
- Diagram 22: Dependency Graph
- Phase Review v0.8.0 Enforcement Hardening Round 1 — 2026-03-05
- AI Agent
- Behavioral Pattern Analysis
- Redaction
- Threat Intelligence
- Unicode Bypass
- docs/README.md — documentation structure index and project phase status
- TestAgentShroudSourceCodeProtection
- TestReportAPI
- _mock_dir_with_fresh_files
- TestDependencySecurity
- TestManagementWSTokenScoping
- Voice Terminal CMakeLists (IDF v5.4 BSP patch)
- _make_client
- TestFailsLoudly
- audio_init() — mic/speaker codec init
- audio_preinit() — claims I2S at 16 kHz before display init
- audio_set_volume() — spoken volume command target
- audio_volume_tick() — zipper-free ramp + NVS persist
- .test_proxy_request_returns_ack_only_updates_when_all_dropped
- ota.c (self-update over HTTPS)
- OTA API Header
- .test_collaborator_rate_limit_resets_after_window
- remote_log.h (WS-mirrored diagnostic log declaration)
- UI Face API Header
- TestConfig
- wakeword.h (PTT/WakeNet public API)
- _skills_reload_impl
- Skill: Data Validation (DATA-VAL)
- ws_ctrl_cb_t (server control frame callback type)
- Available MCP Servers
- Skill: Data Validation (DATA-VAL)
- Available MCP Servers
- Skill: Data Validation (DATA-VAL)
- Available MCP Servers
- browser-fetch/package.json
- AgentShroud Sunday Upgrade — 2026-09-06 (dev-only, read-only inventory → scoped fixes)
- Sunday Upgrade 2026-10-11 — DEV run (agentshroud-bot, 03:00 ET)
- custom/icloud/scripts/calendar.js
- test_apply_patches.js
- PIISanitizer.block_credentials
- gateway/__init__.py
- AgentShroud Gateway OpenAPI Spec
- LLMProxy
- SecurityPipeline.process_outbound
- _INJECTION_PATTERNS (prompt injection regex set)
- Skill: Git Workflow Guardian (GIT-GUARD)
- Cross-Bot Trust Ledger (Module 27)
- ToolACLEnforcer.check_tool_rate_limit
- ToolACLEnforcer.get_allowed_tools
- Origin-Aware Authorization (refuse owner elevation over unverified origin)
- ToolChainAnalyzer.sanitize_tool_params (C34)
- ToolChainAnalyzer.score_reversibility (C37)
- soc.html — unified SOC web dashboard SPA template
- test_default_summary_equals_openclaw_summary
- test_list_cve_agents_returns_wrapped_agents_and_security_tools
- test_agent_cve_registry.py (integrity guard suite)
- test_unknown_bot_id_raises_key_error
- test_alert_telegram_relay.py — AlertTelegramRelay tests
- test_anthropic_openai_translator.py — Anthropic/OpenAI translator tests
- Test Cron Jobs Prompts Module
- Test Data Ledger
- Skill: Pull Request (PR) Generator
- Post-Retry Rate Limit Failover Tests
- Security Scanner Aggregation and Scorecard Tests
- Drift Detection in Pipeline
- Security Integration — Full Pipeline Tests
- Session Isolation End-to-End Tests
- UserSessionManager Isolation Tests
- WebhookReceiver Session Isolation Integration
- SharedMemoryManager Group Memory Read/Write Tests
- SharedMemoryManager User Private Memory Tests
- SlackAPIProxy Outbound Scanning Tests
- SlackSocketClient Reconnect Backoff Tests
- SOC Auth Session Token Tests
- SOC Egress EgressRequest Model Tests
- SOC Models ServiceDescriptor Tests
- SSH Exec Endpoint Tests (allowlist, deny, injection)
- Lifespan 64-Worker Executor and HTTP Peek Filter Tests
- ToolChainAnalyzer Exfiltration Pattern Detection Tests
- ToolResultInjectionScanner Test Suite
- GitHub FUNDING Configuration
- Bug Report Issue Template
- Feature Request Issue Template
- GitHub MCP Server (concept)
- Block Destructive Branches — CI guard for flagged or mass-deletion PRs
- GSDE&G Team (concept)
- i-sre SKILL.md (SRE practices skill, minimal stub)
- i-value-stream-mapping SKILL.md (minimal stub)
- IAM Policies
- calendar.js (iCloud CalDAV skill)
- Suspected prompt-injection / phishing message (fake tailscale.tm credential request)
- Dev Hermes polled prod's Hermes Telegram bot token all night
- Vulcan — Subject Matter Auditor
- POST /forward/stream (streaming voice pipeline)
- Gemini CLI (SECONDARY agent configuration)
- GitHub Copilot CLI (QUATERNARY agent, .agent.md profiles)
- CLAUDE.md as the repo constitution
- AWS RDS MCP server
- AWS Step Functions MCP server
- Production testing guidelines (test isolation patterns)
- pre-commit (gitleaks + git-secrets gate)
- markmap-mcp-server (MCP server)
- .mcp.json (project MCP servers)
- Mermaid Brand Theme Init Block
- Learning System (Continuous Improvement)
- i-security-reviewer.md (security-reviewer agent)
- openclaw agents/_README.txt (50+ specialized agents)
- cd (Continuous Delivery) SKILL stub (OpenClaw)
- chaos-engineering SKILL stub (OpenClaw)
- ci (Continuous Integration) SKILL stub (OpenClaw)
- Vulcan — Subject Matter Auditor
- esp_err.h stub (playback state test)
- esp_log.h stub (playback state test)
- curriculum.md (podcast pipeline learning objectives artifact)
- script.md (podcast pipeline dialogue artifact)
- show_notes.md (podcast pipeline distilled content artifact)
- PostgreSQL RDS (fe-gsdl-poc-database)
- pre-commit check-yaml hook (--unsafe)
- pre-commit gitleaks hook (v8.18.1)
- Whitespace/EOF fixers exclude vendored SCAP datastream
- pre-commit semgrep local hook (new findings only, system semgrep)
- Proxy Layer
- OpenClaw research/web_search domains pre-approved after 210-denial SOC saturation incident
- SCRUM-110: restart recovery must preserve original timeout_action, not hardcoded deny
- SCRUM-154: hung WebSocket client must not wedge the approval lock
- Red Team Canary Values (FAKE_SSN, FAKE_KEY, Project Nightingale)
- BLOCKED-Awaiting-Dev Outcome
- Stale Baseline Turns Rollback Into Unintended Revert
- AgentShroud Brand Guidelines
- Quickstart
- Skill: Git Workflow Guardian (GIT-GUARD)
- detect_runtime
- append_finding.py
- append_trend_log.py
- asb canary [service]
- asb rollback
- CLASS_PROFILE
- Collaborator Greeter State Debug Helper
- SCRUM-154 — blocking response.read() froze the gateway event loop
- SecureClaw Project (concept)
- Skill: Pull Request (PR) Generator
- P1-P4 Incident Severity Matrix
- browser-fetch package.json
- Vulcan — Subject Matter Auditor
- CodexBar Model Cost Usage CLI Summarizer
- Apache License 2.0 (skill-creator)
- Skill Package Symlink Security Tests
- render_md_email.py
- Admin CLI Chat Console (OpenClaw via Gateway)
- Python/Boto3/AWS moto test pattern
- PostgreSQL SAVEPOINT/ROLLBACK test pattern
- Zabbix API unittest.mock test pattern
- Skill: Pull Request (PR) Generator
- apply-patches.js Behavioral Smoke Test Suite (Node.js)
- S1 start-agentshroud.sh launches openclaw with --stack-size=65536
- S2 apply-patches.js sets channels.telegram.apiRoot
- S4 OpenClaw Dockerfile COPYs apply-patches.js from docker/config/openclaw/
- SDK patch path resolution via the real openclaw binary
- Vulcan — Subject Matter Auditor
- Starting a Development Task via Hermes / OpenClaw
- v0.9.0 Human Interface Testing Guide
- Voice Gateway Python Package Init
- Voice Gateway Uvicorn Entrypoint (port 8765, WS ping disabled)
- Voice Gateway FastAPI Server
- AgentShroud Setup Guide
- xmind-generator-mcp (MCP server)
- On-site Zabbix MySQL (200+ sites)
- Architecture Overview
- [1.5.0] "A2A Governance" (2026-08-14)
- ssh_proxy.py
- api.py
- falco-rules.yaml
- pytest.ini
- wazuh-ossec.conf
- AgentShroud Sunday Upgrade — 2026-09-25 (DEV run)
- Final report
- sunday-upgrade.sh
- AGENTSHROUD_MODE
- Presidio Analyzer
- Container Errors
- PII Pipeline Errors
- load_all_secret_file_values
- ClassificationResult
- test_chat_completions_alias.py
- test_clamav_scan_unavailable_degrades_silently
- _script
- TestAnalyzeRequestForRBAC
- TestConsentCookieBinding
- TestInstructionNonce
- TestUserMemoryWriteACL
- ._handler
- .test_collaborator_rate_limit_notice_is_sent_for_each_limited_message
- TestTelegram400Retry
- TestToolRateLimiting
- TestCVE2026_9367TerminalToolDenied
- test_v1_models_synthetic.py
- TrustManager
- Skill: Git Workflow Guardian (GIT-GUARD)
- Skill: Pull Request (PR) Generator
- Vulcan — Subject Matter Auditor
- Skill: Git Workflow Guardian (GIT-GUARD)
- Skill: Pull Request (PR) Generator
- Vulcan — Subject Matter Auditor
- Skill: Git Workflow Guardian (GIT-GUARD)
- Skill: Pull Request (PR) Generator
- Vulcan — Subject Matter Auditor
- VIII. Evaluation
- SOUL
- 📱 Required Accounts & Services
- Sunday Upgrade 2026-10-04 — DEV run (agentshroud-bot, 03:00 ET)
- Hermes — Reference Verifier
- Mnemosyne — Retention Engineer
- Oracle — Feedback Analyst
- Hermes — Reference Verifier
- Mnemosyne — Retention Engineer
- Oracle — Feedback Analyst
- AgentShroud Primary Logo
- [0.9.0] — feat/v0.9.0-soc-team-collab — "Sentinel" (2026-03-18)
- Owner vs Bot Telegram Identity Separation
- health_check
- test_main.py
- Hermes — Reference Verifier
- Collaborators
- Mnemosyne — Retention Engineer
- Hermes — Reference Verifier
- AgentShroud v1.2.0 Master Plan
- Oracle — Feedback Analyst
- AgentShroud — Collaborator Knowledge Base
- Mnemosyne — Retention Engineer
- Oracle — Feedback Analyst
- Usage
- docker-cleanup.sh
- docker/scripts/security-scan.sh
- port_manager.py
- GATEWAY_OP_PROXY_URL
- HTTP_PROXY / HTTPS_PROXY
- [Unreleased] — feat/v0.8.0-enforcement-hardening (session 3 — 2026-03-15)
- TELEGRAM_API_BASE_URL
- OpenClaw
- python-jose
- spaCy
- 06-operations.md
- MCP Proxy Errors
- Test Gmail Credential Retrieval
- GitHub Copilot CLI Setup Guide
- Prompt Injection Blocks
- SSH Proxy Errors
- ._sanitize_reason
- AuditExportConfig
- .record_activity
- MemoryLifecycleConfig
- TestLeakDetection
- test_credential_isolation.py
- TestRunningImageResolution
- TestSensitivePathBlocking
- TestCriticalGuardInitFailClosed
- TestScanToolResult
- TestIsPathAllowedForUser
- tail
- TestConfigurationProtection
- TestSystemPathProtection
- TestWorkspaceAccessPreserved
- TestSecurityViolationLogging
- TestEdgeCases
- TestAsyncSave
- TestSecurity
- fs
- TestContainerRuntimeIsolation
- [Unreleased] — feat/http-connect-proxy + feat/credential-isolation
- .test_events_api_envelope_dispatches_handle_event
- .test_hello_message_not_dispatched
- TestEdgeEnroll
- Available MCP Servers
- Sunday upgrade 2026-10-25 (DEV run, account agentshroud-bot)
- copilot-instructions.md
- 4. Technical Environment Baseline
- test_sync_cve_registry_ghsa.py
- TestNvdAppend
- TestNvdReportOnly
- TestPromptInjectionDetection
- TestTriageClassLevelCoverage
- Hermes — Reference Verifier
- Mnemosyne — Retention Engineer
- Oracle — Feedback Analyst
- postmortem.md
- quick-setup.sh script
- Workstream B: Security Features from Competitive Intel
- Hermes — Reference Verifier
- Mnemosyne — Retention Engineer
- Oracle — Feedback Analyst
- Hermes — Reference Verifier
- [1.1.1] — fix/guard-wiring-and-ops-hardening (2026-06-10)
- AgentShroud Data Assets (root)
- Mnemosyne — Retention Engineer
- VII. v0.8.0 Remediation
- Oracle — Feedback Analyst
- PHASE 1: SECURITY FIX (CURRENT PRIORITY)
- test-edge-isolation.sh
- run_sourced
- Model usage
- notion
- Model-Specific Parameters
- Summarize
- Skill: CI/CD Pipeline Advisor (CICD)
- Skill: Code Review (CR)
- Skill: CI/CD Pipeline Advisor (CICD)
- Animation Guidelines
- chat
- TestAsyncClient
- Workstream E — Blue + red team security scan, both bots
- TestAuth
- schema.json
- Skill: CI/CD Pipeline Advisor (CICD)
- Skill: Code Review (CR)
- crashwatch.sh
- _handle
- Quick Navigation
- Inbound MCP Edge — Threat Model
- Apple Platform Integration
- cve-mitigation-matrix.md
- RBAC collaborator_user_ids list (gateway/security/rbac_config.py)
- Important Notes
- Troubleshooting
- installer.py
- CI Workflows
- gitleaks.toml
- SSH Config
- SECTION 5: IMPORTANT NOTES
- AGENTSHROUD_CONFIG
- Troubleshooting
- Basic Usage
- Installation
- Security & Permissions
- 11. Hard Guardrails (Non-Negotiables)
- LOG_LEVEL
- ClamAV
- Playwright
- Pydantic
- Trivy
- Docker Networks
- Delegation
- ._cleanup_expired
- test_report_store.py
- PHASE 3: iMESSAGE INTEGRATION TEST
- TestOverallDetectionRate
- TestModuleConfigDefaults
- .test_concurrent_log_event_two_connections_keeps_linear_chain
- TestFetchDockerhubTagsUsesCurl
- TestNormalDNSResolution
- CVE Triage — Gaps & Development Plan (OpenClaw)
- TestDNSTunnelingDetection
- TestTelegramDispatch
- Workstream C — Full local-model parity for both bots
- TestStreamingProxyStatusPropagation
- TestAuditQueries
- TestSetConfig
- TestReviewHardening
- TestLLMProxyEndpoints
- TestIsFresh
- TestSkillsReloadEndpoint
- _FakeUnixSocket
- TestTrustInheritance
- TestCollaboratorAccess
- TestAuditChain
- Skill: CI/CD Pipeline Advisor (CICD)
- Skill: Code Review (CR)
- AgentShroud Hermes — System Identity
- Skill: CI/CD Pipeline Advisor (CICD)
- Skill: Code Review (CR)
- Skill: CI/CD Pipeline Advisor (CICD)
- Skill: Code Review (CR)
- launchd/install.sh
- Control Center
- browser/browse.js
- Co-Branding Guidelines
- Brand Applications
- hermes/skills/i-browser/browse.js
- i-ps SKILL (Production Safety Checklist / PROD-SAFETY)
- openclaw/skills/i-browser/browse.js
- IDENTITY.md - Who I Am
- Critical Vulnerabilities Identified in OpenClaw (2026)
- Technical Decisions
- AgentShroud Session Issue Register — 2026-03-14
- Phase 2: Development Tools
- Performance Considerations
- Troubleshooting
- Security Verification
- Common Workflows
- Custom Agents
- Repository Context
- 0.1) MULTI-AGENT HIERARCHY (CLAUDE CODE IS PRIMARY)
- 13. Anti-Patterns to Avoid
- 14. Decision-Making Hierarchy
- 3. Strategic Operating Model
- 5. Governance & Risk Doctrine
- 6. Working Style Contract
- 7. Output Formatting Contract
- 8. Automation Doctrine
- Step 3: Configure Secrets Management
- AgentShroud — Vault Home
- browser-fetch.js
- text_control_center.py / agentshroud_manager.py
- proxy_status.py
- aiosqlite
- httpx
- .verify_export_integrity
- ingest_api/models.py
- delegation.py
- _score_secure_development
- TestAccessControl
- _FakeAsyncClient
- TestDNSFilterConfig
- TestDmIsolation
- _FakeStreamClient
- _FakeStreamResponse
- TestCrossSessionAccess
- TestSaveAndGet
- TestComplianceMaths
- TestComputeBotScorecard
- TestRegistrySecurity
- TestScoreVulnerabilityManagement
- .test_run_resets_backoff_after_successful_connect
- TestSnapshotSmoke
- .test_stranger_rate_limit_notice_includes_reset_time
- .test_forward_to_telegram_handles_http_error_non_json
- TestOwnerMirrorCoalescing
- ._results
- TestHiddenContent
- TestPIIDetection
- gsd.md
- 8. Docker System Pruning
- Common Scenarios
- browser-fetch.js
- Browser Fetch Skill
- CodexBar CLI quick ref (usage + cost)
- 6. Tailscale — secure ESP→Hermes link ✅ LIVE (see docs/integrations/voice-terminal-esp32-s3.md)
- 7) CODEX CLI OPERATIONAL RULES
- Apollo — Audio Systems Producer
- Athena — Knowledge Distiller
- Atlas — Curriculum Architect
- Agentic AI Threat Intelligence Cron Prompt
- Authentication
- Context Management
- Configuration Files
- Role & Restrictions
- 12. Quality Threshold Definition
- 1) PROJECT IDENTITY
- 2) HOW TO WORK IN THIS REPO (SDLC EXPECTATIONS)
- 4) LANGUAGE & TOOLING STANDARDS
- 9. Multi-Agent Orchestration Rules
- AWS Cloud Management & FinOps
- Browser — Secure Browser Automation
- Daedalus — Concept Illustrator
- 8D Root Cause Analysis
- graphify Step 3 - Parts A, B and C
- Hermes — Podcast Production Orchestrator
- Branding Specialist (BS)
- CI/CD Pipeline Advisor (CICD)
- Code Review (CR)
- Mode B — Comprehensive review sweep
- GSDE&G Development Master Checklist (MC)
- Mode B — Comprehensive review sweep
- Pull Request Generator (PR)
- Incident Response (INCIDENT)
- Production Safety Checklist (PROD-SAFETY)
- iCloud Data Manager (ICLOUD)
- macOS System Administrator (MAC)
- Mnemosyne — Retention Engineer
- Oracle — Feedback Analyst
- System Audit Documentation
- System Audit Vault
- Blue Team Security Auditor (SEC-DEFENSE)
- Red Team Adversarial Tester (SEC-OFFENSE)
- Socrates — Dialogue Architect
- Vulcan — Subject Matter Auditor
- 7. CI/CD Quality Gates
- Press Kit
- Logo Usage
- _check_rate_limit
- TestErrorSanitization
- _Instr
- tools
- Apollo — Audio Systems Producer
- Athena — Knowledge Distiller
- Atlas — Curriculum Architect
- GSDE&G Development Master Checklist (MC)
- MCP Auth Reset (MCPM-AUTH-RESET)
- MCP AWS Profile Configuration (MCPM-AWS-PROFILE)
- MCP Doctor (MCPM-DOCTOR)
- MCP Tools Usage (MCPM)
- Mnemosyne — Retention Engineer
- Oracle — Feedback Analyst
- Project Management (PM)
- Pull Request Generator (PR)
- System Audit Documentation
- Blue Team Security Auditor (SEC-DEFENSE)
- cve_prefetch.py
- Apollo — Audio Systems Producer
- Athena — Knowledge Distiller
- Atlas — Curriculum Architect
- AWS Cloud Management & FinOps
- Browser — Secure Browser Automation
- Branding Specialist (BS)
- CI/CD Pipeline Advisor (CICD)
- Code Review (CR)
- Git Workflow Guardian (GIT-GUARD)
- MCP Doctor (MCPM-DOCTOR)
- Mnemosyne — Retention Engineer
- Oracle — Feedback Analyst
- Project Management (PM)
- Pull Request Generator (PR)
- Incident Response (INCIDENT)
- Production Safety Checklist (PROD-SAFETY)
- Quality Assurance (QA)
- System Audit Documentation
- gateway-start.sh entrypoint
- PERMANENT_EGRESS_DOMAINS
- System Audit Vault
- direnv-based environment variable management
- Blue Team Security Auditor (SEC-DEFENSE)
- Red Team Adversarial Tester (SEC-OFFENSE)
- Security Review (SEC)
- Socrates — Dialogue Architect
- Test-Driven Development (TDD)
- Technical Illustrator (TI)
- Technical Writer (TW)
- Vulcan — Subject Matter Auditor
- security-scheduler.sh
- verify-security.sh
- run
- ADR-001: Proxy-layer inversion model
- AgentShroud — Diagram Library
- 1Password Integration
- Configuration Reference
- Updating
- test_slack_socket_client.py
- _LegacyStubApprovalQueue
- _StubAuditStore
- TestDelegateBasic
- TestListAndCleanup
- TestSingleUseGrants
- _HeadFakeClient
- TestFilterOutboundResponse
- TestFalcoSummary
- TestGetSbom
- TestRuntimeProtectionAndMalware
- TestTrivyImageSummaries
- TestWazuhSummary
- TestScoreIncidentResponse
- TestScoreMalwareDefense
- TestScoreRuntimeProtection
- .test_get_wss_url_returns_url_on_success
- test_dashboard_fallback_when_template_missing
- TestSubagentMonitorConfig
- TestSubagentTracking
- TestDefaultBotId
- TestAdminAccess
- TestOwnerAccess
- TestDefenseLayerVocabulary
- container-runtime.sh
- test-container-runtime.sh
- test-skills-sync.sh
- Multi-Layer Detection Strategy
- generate_image.py
- OpenAI Whisper API (curl)
- test_hermes_edge_delegate_profile.sh
- test_hermes_mcp_reconciliation.sh
- test_launchd_install.sh
- test_setup_secrets.sh
- test_sunday_prompt_unattended.sh
- test_sunday_upgrade_head_guard.sh
- 2) WHAT YOU SHOULD DO (YOUR JOBS)
- i-code-reviewer — Code reviewer and change-impact analyst (pre-commit)
- i-data-ai-ot — Data, AI/LLM and OT/BESS tester (any stage)
- i-integration-qa — Integration and regression QA (PR/CI)
- i-release-gate — Release gate and operational readiness (release / post-deploy)
- i-security-scanner — Security scanner (pre-commit)
- i-system-nfr — System and non-functional tester (pre-release)
- i-test-architect — Test architect (planning)
- i-unit-tdd — Unit-level TDD owner (implement)
- Skill: Code review and impact analysis (Pre-commit)
- Skill: Data, AI/LLM and OT/BESS testing (any stage)
- Skill: Integration and regression QA (PR/CI)
- Skill: Release gate (Release / post-deploy)
- Skill: Security scanning (Pre-commit)
- Skill: System and non-functional testing (Pre-release)
- Skill: Test architecture (Plan stage)
- Skill: Unit-level TDD (Implement stage)
- Brand Approval Process
- Brand Identity
- 🎨 Quick Access
- claude_repo_setup.sh
- max_concurrency
- max_response_bytes
- per_vendor_per_minute
- i-code-reviewer — Code reviewer and change-impact analyst (pre-commit)
- i-data-ai-ot — Data, AI/LLM and OT/BESS tester (any stage)
- i-integration-qa — Integration and regression QA (PR/CI)
- i-release-gate — Release gate and operational readiness (release / post-deploy)
- i-security-scanner — Security scanner (pre-commit)
- i-system-nfr — System and non-functional tester (pre-release)
- i-test-architect — Test architect (planning)
- i-unit-tdd — Unit-level TDD owner (implement)
- hermes/manifest.json
- graphify reference: commit hook and native CLAUDE.md integration
- openclaw/manifest.json
- context.md
- agentshroud-ssh-exec.sh
- agentshroud-ssh-write-file.sh
- health-check.sh
- init-openclaw-config.sh
- killswitch.sh
- security-entrypoint.sh
- test-get-credential.sh
- test-op-auth.sh
- Priority 3: User Experience Improvements
- Priority 4: Advanced Agent Capabilities
- Data Documentation
- Flows Documentation
- Integrations Documentation
- Post-fable-5 Task Delegation
- Project Documentation
- Requirements Documentation
- Competitive Analysis Reports Archive
- Step 5: Configure Ports
- Step 2: Choose Your Container Runtime
- Prerequisites
- Testing Documentation
- ._teams_config
- test_api_alerts_endpoint_emits_bus_event
- TestEnrollment
- .test_mcp_proxy_endpoint
- TestExtractFilePaths
- TestAgenticScorers
- TestFluentBitSummary
- TestLoadLatestJson
- TestResourceAvailability
- TestSocketAndPidProbes
- TestTrivySummary
- TestScoreContainerHardening
- TestScoreLoggingMonitoring
- TestScoreNetworkSegmentation
- TestScoreSecretsManagement
- TestStatusMappings
- TestZeroWidthAttacks
- BufferHandler
- i-code-reviewer — Code reviewer and change-impact analyst (pre-commit)
- i-data-ai-ot — Data, AI/LLM and OT/BESS tester (any stage)
- i-integration-qa — Integration and regression QA (PR/CI)
- i-release-gate — Release gate and operational readiness (release / post-deploy)
- i-security-scanner — Security scanner (pre-commit)
- i-system-nfr — System and non-functional tester (pre-release)
- i-test-architect — Test architect (planning)
- i-unit-tdd — Unit-level TDD owner (implement)
- git-hooks/install.sh
- i-code-reviewer — Code reviewer and change-impact analyst (pre-commit)
- [Unreleased] — feat/v0.8.0-enforcement-hardening (session 2 — 2026-03-14)
- i-data-ai-ot — Data, AI/LLM and OT/BESS tester (any stage)
- i-integration-qa — Integration and regression QA (PR/CI)
- [1.5.2] (2026-08-23)
- i-release-gate — Release gate and operational readiness (release / post-deploy)
- i-security-scanner — Security scanner (pre-commit)
- i-system-nfr — System and non-functional tester (pre-release)
- i-test-architect — Test architect (planning)
- i-unit-tdd — Unit-level TDD owner (implement)
- i-code-reviewer — Code reviewer and change-impact analyst (pre-commit)
- i-data-ai-ot — Data, AI/LLM and OT/BESS tester (any stage)
- i-integration-qa — Integration and regression QA (PR/CI)
- i-release-gate — Release gate and operational readiness (release / post-deploy)
- i-security-scanner — Security scanner (pre-commit)
- i-system-nfr — System and non-functional tester (pre-release)
- i-test-architect — Test architect (planning)
- i-unit-tdd — Unit-level TDD owner (implement)
- 1. The Problem: Unsecured AI Agents
- 6. Competitive Landscape
- Summary
- impact-map.sh
- Authentication and Authorization Framework
- Obsidian
- find-sessions.sh
- Video Frames (ffmpeg)
- Voice Call
- Type Scale
- Platform-Specific
- DELIVERABLE 4 — v1.0 Roadmap
- 1) REPOSITORY OVERVIEW
- 4) LANGUAGE & TOOLING STANDARDS
- 8) CODEX CLI CONFIGURATION
- Color Usage
- Typography in Practice
- block_credential_write.sh
- agentshroud-secrets.sh
- heartbeat.sh
- daily-checkin.sh
- AgentShroud Falco Rules
- bot-access-audit.sh
- security-report.sh
- security-report-retention.sh
- external network (gateway host-facing bridge)
- AGENTSHROUD_HERMES_DISABLE_TELEGRAM opt-in
- Hermes launched via docker run, not compose
- Collaborator workspace SOUL.md (Isaiah persona)
- AgentShroud Daily Check-in (Hermes Prompt)
- Daily Memory Journal (Hermes Prompt)
- Monthly Chaos Engineering Drill (Hermes Prompt)
- Weekly Kaizen Review (Hermes Prompt)
- Sandbox Container Reaper
- Daily summary state tracking
- Colima VM default-route auto-heal (step 2)
- Container net-diag expected-failure baseline (step 5)
- DOCKER-USER iptables reapply + verify (step 3)
- 120s freshclam timeout rationale (bounded failure over outage)
- Env-split cron enable/disable pass (dev enables, prod disables)
- start-agentshroud.sh (OpenClaw entrypoint)
- Pending OpenClaw migration repair (openclaw doctor --fix) before gateway start
- OpenClaw/Hermes/MCP sandbox container reaper
- Hermes CVE table (#cves-hermes, paginated)
- AgentShroud Infrastructure (own images reported in full)
- Mitigation status badges (crit/high/med/low/ok/partial)
- OpenClaw CVE table (#cves, paginated)
- VT_AGENTS table (direct/hermes/openclaw)
- gateway package __init__
- BotConfig
- TestPromptExtraction
- test_webhook_receiver_passes_agent_id_as_bot_id
- mgr
- _HERMES_CVE_REGISTRY (HERMES_CVE_REGISTRY alias)
- _OPENCLAW_CVE_REGISTRY (AGENT_CVE_REGISTRY alias)
- _AGENT_CVE_SOURCES (per-agent CVE pipeline config)
- PERMANENT_EGRESS_DOMAINS canonical allowlist
- _build_bridge() — test-local reimplementation of the ResourceGuard→AlertDispatcher bridge closure
- no_exec
- test_edge_guard_allowlist_holds_even_if_inner_app_serves_everything
- Ingest API (POST /ingest)
- Hermes cron jobs paused by empty AGENTSHROUD_PROD_CRON_KEEP on container recreate
- init-openclaw-config.sh runs doctor --fix before version seed (schema v23->v24 trap)
- OpenClaw sandbox mode set off (named volume vs bind-mount mismatch)
- asb build
- asb down
- is_stable
- pick_latest_hermes_tag
- pick_latest_stable
- triage_agent
- triage_entry
- 1Password iCloud Credential Retrieval
- S17 Hermes run-standalone.sh resource caps: prod 3g/1.5, dev 2g/1.0, env override honoured
- colima-vm-flags behavioral check (2026-10-16)
- Strip comments before grepping for regressions
- TestMemoryIntegrityRegistration
- TestAppStateHas
- TestScoreSecureDevelopment
- .test_owner_pending_command_shows_pending_active_and_revoked
- .test_collaborator_direct_file_query_returns_protect_file_notice
- .test_collaborator_rate_limit_notice_includes_retry_window
- .test_healthcheck_with_leading_whitespace_is_handled_locally
- .test_healthcheck_with_fullwidth_chars_is_handled_locally
- .test_self_diagnostic_with_punctuation_is_handled_locally_for_collaborator
- .test_self_diagnose_with_mention_is_handled_locally
- .test_self_diagnose_with_zero_width_char_is_handled_locally
- .test_logging
- validate-skills-manifest.sh
- nano-pdf
- transcribe.sh
- sag
- wait-for-text.sh
- frame.sh
- test_bot_boot_live.sh
- test_bot_boot_static.sh
- test_hermes_chown_coverage.sh
- test_hermes_cron_html_email.sh
- test_openclaw_model_provider_consistency.sh
- test_openclaw_photo.sh
- test_openclaw_readiness_retry.sh
- test_sunday_upgrade_session_guard.sh
- .agents/agents/i-agile.md
- .agents/agents/i-architecture-review.md
- .agents/agents/i-bdd.md
- .agents/agents/i-cd.md
- .agents/agents/i-chaos-engineering.md
- .agents/agents/i-ci.md
- .agents/agents/i-devsecops.md
- .agents/agents/i-gitops.md
- .agents/agents/i-incident-response.md
- .agents/agents/i-kaizen.md
- .agents/agents/i-kanban.md
- .agents/agents/i-observability.md
- .agents/agents/i-prod-safety.md
- .agents/agents/i-scrum.md
- .agents/agents/i-sdlc.md
- .agents/agents/i-security-reviewer.md
- .agents/agents/i-sre.md
- .agents/agents/i-value-stream-mapping.md
- .agents/skills/i-cd/SKILL.md
- .agents/skills/i-ci/SKILL.md
- MCP Auth Reset README
- MCP Doctor README
- MCP Tools Usage (README)
- i-prod-safety/SKILL.md
- Security Review (SEC) README
- AgentShroud Tagline
- auto_format_python.sh
- block_credential_read.sh
- block_main_commits.sh
- remind_proposal_review.sh
- run_targeted_tests.sh
- warn_dangerous_bash.sh
- .cursor/agents/i-agile.md
- .cursor/agents/i-architecture-review.md
- .cursor/agents/i-bdd.md
- .cursor/agents/i-cd.md
- .cursor/agents/i-chaos-engineering.md
- .cursor/agents/i-ci.md
- .cursor/agents/i-devsecops.md
- .cursor/agents/i-gitops.md
- .cursor/agents/i-incident-response.md
- .cursor/agents/i-kaizen.md
- .cursor/agents/i-kanban.md
- .cursor/agents/i-observability.md
- .cursor/agents/i-prod-safety.md
- .cursor/agents/i-scrum.md
- .cursor/agents/i-sdlc.md
- .cursor/agents/i-security-reviewer.md
- .cursor/agents/i-sre.md
- .cursor/agents/i-value-stream-mapping.md
- email_helper.sh
- hermes/skills/i-agile/SKILL.md
- hermes/skills/i-architecture-review/SKILL.md
- hermes/skills/i-observability/SKILL.md
- GSDE&G Skills Reference Guide
- i-socrates README (Dialogue Architect)
- prefetch-ghsa-registry.sh
- openclaw/skills/i-agile/SKILL.md
- openclaw/skills/i-architecture-review/SKILL.md
- openclaw/skills/i-bdd/SKILL.md
- openclaw/skills/i-observability/SKILL.md
- openclaw/skills/i-scrum/SKILL.md
- openclaw/skills/i-sdlc/SKILL.md
- openclaw/skills/i-sre/SKILL.md
- openclaw/skills/i-value-stream-mapping/SKILL.md
- check-status.sh
- colima-firewall.sh
- devices.sh
- entrypoint-agentshroud.sh
- gateway-start.sh
- hermes-cron-dedup.sh
- logs.sh
- patch-anthropic-sdk.sh
- patch-slack-sdk.sh
- patch-telegram-sdk.sh
- patch-ws-proxy.sh
- restart.sh
- scan.sh
- set-model.sh
- telegram.sh
- test-system.sh
- toggle-readonly.sh
- approval_queue/__init__.py
- cli/__init__.py
- inbound_edge/__init__.py
- .flush
- ingest_api/__init__.py
- security/__init__.py
- skills/__init__.py
- soc/__init__.py
- tests/__init__.py
- test_get_activity_filters_by_bot_id
- test_get_activity_summary_by_bot_empty_when_no_file
- test_pruner_short_numeric_ids_are_test_fixtures
- Path Isolation Manager Tests
- .setup_method
- verify.sh
- web/__init__.py
- i-agile.agent.md
- i-architecture-review.agent.md
- i-bdd.agent.md
- i-cd.agent.md
- i-chaos-engineering.agent.md
- i-ci.agent.md
- i-devsecops.agent.md
- i-gitops.agent.md
- i-incident-response.agent.md
- i-kaizen.agent.md
- i-kanban.agent.md
- i-observability.agent.md
- i-prod-safety.agent.md
- i-scrum.agent.md
- i-sdlc.agent.md
- i-security-reviewer.agent.md
- i-sre.agent.md
- i-value-stream-mapping.agent.md
- ci-cd/README.md
- pre-commit
- podcast/README.md
- clean-env-keep-local.sh
- clean-env-quick-keep-local.sh
- perform_mcp_oauth_preflight.sh
- setup-mcp-user.sh
- sre/README.md
- .omp/agents/i-agile.md
- .omp/agents/i-architecture-review.md
- .omp/agents/i-bdd.md
- .omp/agents/i-cd.md
- .omp/agents/i-chaos-engineering.md
- .omp/agents/i-ci.md
- .omp/agents/i-devsecops.md
- .omp/agents/i-gitops.md
- .omp/agents/i-incident-response.md
- .omp/agents/i-kaizen.md
- .omp/agents/i-kanban.md
- .omp/agents/i-observability.md
- .omp/agents/i-prod-safety.md
- .omp/agents/i-scrum.md
- .omp/agents/i-sdlc.md
- .omp/agents/i-security-reviewer.md
- .omp/agents/i-sre.md
- .omp/agents/i-value-stream-mapping.md
- .opencode/agents/i-agile.md
- .opencode/agents/i-architecture-review.md
- .opencode/agents/i-bdd.md
- .opencode/agents/i-cd.md
- .opencode/agents/i-chaos-engineering.md
- .opencode/agents/i-ci.md
- .opencode/agents/i-devsecops.md
- .opencode/agents/i-gitops.md
- .opencode/agents/i-incident-response.md
- .opencode/agents/i-kaizen.md
- .opencode/agents/i-kanban.md
- .opencode/agents/i-observability.md
- .opencode/agents/i-prod-safety.md
- .opencode/agents/i-scrum.md
- .opencode/agents/i-sdlc.md
- .opencode/agents/i-security-reviewer.md
- .opencode/agents/i-sre.md
- .opencode/agents/i-value-stream-mapping.md
- sunday-upgrade-report.sh
- eval-run.sh
- release-check.sh
- run-integration.sh
- run-unit.sh
- sbom-verify.sh
- sec-scan.sh
- testing/smoke.sh
- sql-fixtures.sh
- telemetry-check.sh
- agentshroud-blueteam/references/steve-hay-plan.md
- run-as-root.sh
- clawhub/SKILL.md
- gemini/SKILL.md
- mcporter/SKILL.md
- nano-banana-pro/SKILL.md
- openai-whisper/SKILL.md
- ordercli/SKILL.md
- songsee/SKILL.md
- spotify-player/SKILL.md
- things-mac/SKILL.md
- wacli/SKILL.md
- bsp/esp-bsp.h stub (wakeword PTT test)
- freertos/FreeRTOS.h stub (wakeword PTT test)
- Upstream A2A Gap #78298 — SSRF Push-Notification Callback URL Bypass
- Upstream Hermes Gap #80534 — Peer Identity Resolved From Socket/X-Forwarded-For Instead Of Bearer Token
- Upstream A2A Gap #83701 — Task/ContextId Collision Hijack
- Kaizen Fix: AlertDispatcher now retries 3x with exponential backoff instead of failing on a single 10s timeout, which had been the top gateway error category (14/week) at ERROR level
- 3+ auth failures within 5 minutes escalates event severity to critical
- Falco (runtime security monitoring)
- C46 Signed Instruction Envelopes (HMAC-SHA256 tamper detection for system prompts/tool results)
- Large-write-then-network-activity staging/exfiltration pattern detection
- Trivy (container vulnerability scanning)
- Wazuh (file integrity monitoring)
- XML injection-block filtering (function_calls/thinking/system-reminder/invoke/parameter)
- PTB HTTPXRequest __slots__ Crash-Loop Fix Rationale
- patch_telegram_send_base_url.py patch driver
- Cron: Daily CVE Triage & Remediation Scan
- jobs.yaml (Hermes cron)
- Multi-LLM Review Loop (Codex+Gemini review, Claude fixer)
- calendar.js — iCloud Calendar Management
- i-sad README (System Audit Documentation)
- Per-chat group agent + binding reconciliation (Patch 1e)
- LOCAL_PROVIDER_KEY mode-derivation design
- apply-patches.js patch driver (openclaw.json)
- Telegram channel-wide fallback binding design
- Telegram dmPolicy=open security tradeoff
- Telegram channel token/dmPolicy/allowlist patch (Patch 3)
- daily-checkin.sh (marvin/pi status check)
- prefetch-ghsa-registry.sh (known-GHSA-ID cache prefetch)
- AgentShroud (security proxy)
- Kill Switch
- MCP (Model Context Protocol)
- OpenClaw
- Proxy Mode
- Sidecar Mode
- SSRF (Server-Side Request Forgery)
- Trust Management
- Zero-Config Deployment
- Zero-Trust Architecture
- Hermes A2A Plugin Upstream Gaps (#83701, #80534/#80779, #78298, #77872, #81042)
- OpenSCAP dependency note
- playback_step() — reproduces tts_task's gate-open/drain branches for testing
- group_router.py (GroupApprovalRouter)
- agentshroud-soc CLI Group
- AgentShroud Security Dashboard (index.html)
- rate_limiter (module-level instance)
- gateway/ingest_api/ssh_config.py (SSHConfig)
- MCPProxy.check_approval_required
- MCPProxy.process_tool_call
- MCPProxy.process_tool_result
- SecurityPipeline.process_inbound
- web_config.py (WebProxyConfig)
- web_proxy.py (WebProxy)
- gateway/runtime/docker_engine.py (DockerEngine)
- gateway/runtime/podman_engine.py (PodmanEngine)
- gateway/runtime/security.py (get_features_for_runtime)
- CollaboratorActivityTracker.record_activity
- gateway/security/dns_filter.py (DNSFilterConfig)
- gateway/security/drift_detector.py (DriftDetector)
- gateway/security/encrypted_store.py (EncryptedStore)
- gateway/security/file_sandbox.py (FileSandbox)
- intel_report module (CompetitiveIntelReport, IntelReportStore)
- key_rotation.py (KeyRotationManager)
- gateway/security/key_vault.py (KeyVault)
- killswitch_config.py (KillSwitchConfig)
- killswitch_monitor.py (KillSwitchMonitor)
- gateway/security/metadata_guard.py (MetadataGuard)
- gateway/security/network_validator.py (NetworkValidator)
- gateway/security/prompt_guard.py (PromptGuard)
- session_manager.py (UserSessionManager)
- shared_memory.py (SharedMemoryManager)
- ADMIN_TOOLS
- COLLABORATOR_ALLOWED_TOOLS
- PRIVATE_TOOLS
- ToolChainAnalyzer._load_custom_patterns
- ToolChainAnalyzer._load_default_patterns
- gateway/skills/manifest.py (SkillsManifest)
- gateway/skills/scan.py (scan CLI)
- gateway/soc/services.py (ServiceManager)
- Collaborator Tracker Tests
- Test Dashboard Endpoints Suite
- Test File Sandbox Message Gate Suite
- Test Group Config
- test_enforce_real_queue_high_risk_not_downgraded_to_allow (regression guard)
- Outbound Information Filter Tests
- Progressive Lockdown UX Tests
- Round 2 Security Hardening Tests
- agentshroud_manager (version manager)
- CI Workflow
- Security Scan workflow (security-scan.yml)
- Chen et al. 2026 — Agent configuration vulnerabilities / session hijacking (arXiv:2602.14364)
- Chen et al. 2026 (arXiv:2602.14364) — Session Hijacking
- Chen et al. 2026 (arXiv:2602.14364) — MCP config shell injection / secret exfiltration
- Maloyan & Namiot 2026 (arXiv:2601.17548) — Malicious MCP server configuration attacks
- Wang et al. 2026 (arXiv:2602.08412) — Confused Deputy / Event Injection Attacks
- Wu et al. 2026 (arXiv:2601.07263) — Browser-based agent social engineering attacks
- agentshroud-gateway
- agentshroud-soc
- Owner-allowlist checked before PII sanitisation to avoid CVE/date-dense body collapse
- 0.9 PII Confidence Floor (CLAUDE.md §7.8)
- plan_remediation
- read_pin
- write_pin
- scripts/smoke.sh (static startup smoke suite)
- SecurityPipeline (external, referenced)
- SecureBrowser SKILL
- WS-E RT-2 Inbound Encoding Bypass Fix Rationale
- audio.h stub (wakeword PTT test)
- esp_err.h stub (wakeword PTT test)
- esp_log.h stub (wakeword PTT test)

## God Nodes (most connected - your core abstractions)
1. `_wrap_response()` - 236 edges
2. `_make_update()` - 219 edges
3. `FakeRBAC` - 219 edges
4. `_make_sanitizer()` - 218 edges
5. `TelegramAPIProxy` - 213 edges
6. `PassthroughPipeline` - 207 edges
7. `TestInboundPipelineOnGetUpdates` - 204 edges
8. `TestOutboundPipelineIntegration` - 185 edges
9. `lifespan()` - 119 edges
10. `LLMProxy` - 117 edges

## Surprising Connections (you probably didn't know these)
- `Read-Only Root FS Constraint — what breaks without proper mounts` --semantically_similar_to--> `toggle-readonly.sh mode switcher`  [INFERRED] [semantically similar]
  docs/architecture/OPENCLAW_WRITE_REQUIREMENTS.md → docker/scripts/toggle-readonly.sh
- `Read-Only Root FS Constraint — what breaks without proper mounts` --semantically_similar_to--> `AgentShroud Security Verification (13-check driver)`  [INFERRED] [semantically similar]
  docs/architecture/OPENCLAW_WRITE_REQUIREMENTS.md → docker/scripts/verify-security.sh
- `Phase 3 Container Security Hardening Baseline` --semantically_similar_to--> `AgentShroud Security Verification (13-check driver)`  [INFERRED] [semantically similar]
  docs/architecture/PHASE3_REQUIREMENTS.md → docker/scripts/verify-security.sh
- `75 Security Modules` --semantically_similar_to--> `7-Layer Security Architecture`  [INFERRED] [semantically similar]
  README.md → SECURITY.md
- `Native Python gateway dev run: uvicorn gateway.ingest_api.main:app --host 127.0.0.1 --port 8080` --semantically_similar_to--> `AgentShroud Gateway (Trust Zone 1): holds 1Password service account, enforces policy, signs ledger entries, controls approval queue, HMAC/JWT validation`  [INFERRED] [semantically similar]
  docs/operations/macos.md → docs/diagrams/images/diagram-11-trust-boundary.png

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **asb profile-aware rebuild: _PROFILE_FLAG reaches compose build so voice-gateway is rebuilt, enforced by S16** — scripts_asb_profile_flag, scripts_asb_rebuild_subcommand, scripts_asb_clean_rebuild_subcommand, scripts_asb_compose_profile_gating, tests_startup_smoke_test_bot_boot_static_s16 [EXTRACTED 1.00]
- **Bot boot static smoke-test suite** — tests_startup_smoke_test_bot_boot_static_s1, tests_startup_smoke_test_bot_boot_static_s2, tests_startup_smoke_test_bot_boot_static_s3, tests_startup_smoke_test_bot_boot_static_s4, tests_startup_smoke_test_bot_boot_static_s5, tests_startup_smoke_test_bot_boot_static_s6, tests_startup_smoke_test_bot_boot_static_s7, tests_startup_smoke_test_bot_boot_static_s8, tests_startup_smoke_test_bot_boot_static_s9, tests_startup_smoke_test_bot_boot_static_s10, tests_startup_smoke_test_bot_boot_static_s11, tests_startup_smoke_test_bot_boot_static_s12, tests_startup_smoke_test_bot_boot_static_s13, tests_startup_smoke_test_bot_boot_static_s14, tests_startup_smoke_test_bot_boot_static_s15, tests_startup_smoke_test_bot_boot_static_s16, tests_startup_smoke_test_bot_boot_static_s17 [EXTRACTED 1.00]
- **Colima health-check self-heal recovery paths** — docker_scripts_colima_health_check_auto_start_stopped_vm, docker_scripts_colima_health_check_socket_forward_repair, docker_scripts_colima_health_check_colima_vm_flags, docker_scripts_colima_health_check_upgrade_in_progress, docker_scripts_colima_health_check_resolve_docker_host, docker_scripts_colima_health_check_default_route_autoheal, docker_scripts_colima_health_check_iptables_reapply [EXTRACTED 1.00]
- **Four-tier credential backend cascade (Keychain / secret-tool / 1Password / file)** — docker_setup_secrets_detect_backend, docker_setup_secrets_ensure_keychain, docker_setup_secrets_keychain_get, docker_setup_secrets_keychain_store, docker_setup_secrets_op_ref_for, docker_setup_secrets_op_get, docker_setup_secrets_get_secret, docker_setup_secrets_store_secret [EXTRACTED 1.00]
- **CVE Arm-2 triage tooling and its open gaps** — scripts_triage_cve_mitigations, scripts_sync_cve_registry, gateway_security_agent_cve_registry, docs_security_cve_triage_gaps, reports_upgrade_2026_09_22_cve_triage_running_version_gap, reports_upgrade_2026_09_26_nvd_append_bug, reports_upgrade_2026_09_24_gap_report_delta_bug, reports_upgrade_2026_10_04_scrum_185 [EXTRACTED 1.00]
- **Hermes container boot flow (docker run -> s6 main program -> init-config -> cron/secret reconciliation)** — docker_bots_hermes_run_standalone_cmd_up, docker_bots_hermes_start, docker_bots_hermes_init_config, docker_bots_hermes_init_config_prod_cron_keep_reconciliation, docker_bots_hermes_start_missing_secrets_banner, docker_bots_hermes_start_model_lock [EXTRACTED 1.00]
- **Hermes standalone docker run launch flow** — docker_bots_hermes_run_standalone_cmd_up, docker_bots_hermes_run_standalone_wait_for_gateway_healthy, docker_bots_hermes_run_standalone_secret_mount_args, docker_bots_hermes_run_standalone_feedbin_env_args, docker_bots_hermes_run_standalone_dashboard_auth_env_args, docker_bots_hermes_run_standalone_dashboard_host_default, docker_bots_hermes_run_standalone_version_fallback, docker_bots_hermes_run_standalone_hermes_resource_caps [EXTRACTED 1.00]
- **Per-backend request shims applied in both proxy paths (Rapid-MLX thinking/null-widening, Fieldflare field strip, model-ID normalization)** — gateway_proxy_llm_proxy_normalize_local_model, gateway_proxy_llm_proxy_suppress_qwen3_thinking, gateway_proxy_llm_proxy_widen_optional_tool_param_types, gateway_proxy_llm_proxy_strip_fieldflare_unsupported_fields, gateway_proxy_llm_proxy_proxy_messages, gateway_proxy_llm_proxy_proxy_messages_streaming, gateway_proxy_llm_proxy_local_model_routes [EXTRACTED 1.00]
- **2026-10-16 streaming upstream-status propagation fix (StreamHead)** — gateway_proxy_llm_proxy_streamhead, gateway_proxy_llm_proxy_proxy_messages_streaming, gateway_ingest_api_main_llm_api_proxy, gateway_tests_test_main_endpoints_teststreamingproxystatuspropagation, gateway_tests_test_llm_proxy_test_streaming_with_head_reports_upstream_400_and_body, gateway_tests_test_llm_proxy_test_streaming_default_contract_yields_only_bytes [EXTRACTED 1.00]
- **Sunday apply: sequential per-service build with disk/HEAD gates, compose up, verify, and rollback on any failure** — scripts_sunday_upgrade_apply_phase_baseline, scripts_sunday_upgrade_apply_phase_apply, scripts_sunday_upgrade_apply_ensure_build_space, scripts_sunday_upgrade_apply_build_one_service, scripts_sunday_upgrade_apply_wait_for_docker, scripts_sunday_upgrade_apply_phase_verify, scripts_sunday_upgrade_apply_attempt_rollback, scripts_sunday_upgrade_apply_rollback_target_predates_config, scripts_sunday_upgrade_apply_exit_code_contract [EXTRACTED 1.00]
- **Working-tree HEAD guard: record at start, re-assert before and inside every build iteration, proven by test** — scripts_sunday_upgrade_apply_record_head, scripts_sunday_upgrade_apply_assert_head_unchanged, scripts_sunday_upgrade_apply_head_at_start, scripts_sunday_upgrade_apply_phase_apply, scripts_sunday_upgrade_apply_shared_working_tree_guard, tests_startup_smoke_test_sunday_upgrade_head_guard_extraction, tests_startup_smoke_test_sunday_upgrade_head_guard_head_moved_check, tests_startup_smoke_test_sunday_upgrade_head_guard_loop_wiring_check [EXTRACTED 1.00]
- **Honest CVE mitigation triage: classify, version-drift-safe source_fix, per-agent isolation** — scripts_triage_cve_mitigations_triage_entry, gateway_tests_test_triage_cve_mitigations_testtriageentry, gateway_security_agent_cve_registry_openclaw_cve_registry, scripts_check_version_pins_parity [INFERRED 0.75]
- **Local-backend request compatibility shims** — gateway_proxy_llm_proxy_llmproxy_suppress_qwen3_thinking, gateway_proxy_llm_proxy_llmproxy_widen_optional_tool_param_types, gateway_proxy_llm_proxy_llmproxy_strip_fieldflare_unsupported_fields, gateway_proxy_llm_proxy_llmproxy_normalize_local_model [INFERRED 0.85]
- **Secret scanning defense-in-depth (gitleaks CI, gitleaks hook, detect-secrets, git-secrets, trivy .gitallowed skip)** — pre_commit_config_gitleaks_hook, pre_commit_config_detect_secrets_hook, pre_commit_config_git_secrets_hook [INFERRED 0.85]

## Communities (2835 total, 975 thin omitted)

### Community 0 - "MiddlewareManager"
Cohesion: 0.03
Nodes (49): MiddlewareManager, MiddlewareResult, Any, Exception, Extract user ID from request data., Enforce per-user, per-bot session isolation rules. Each (user_id, bot_id) pair…, Check if user_id is the system owner via RBAC config (single source of truth)., Extract potential file paths from message content. (+41 more)

### Community 1 - "AgentShroud Semgrep SAST Configuration"
Cohesion: 0.12
Nodes (15): Checklist, IEC 62443 Reference, Summary, Type of Change, AgentShroud Semgrep SAST Configuration, Rule: agentshroud-assert-security-check, Rule: agentshroud-hardcoded-password, Rule: agentshroud-log-sensitive-key (+7 more)

### Community 2 - "_make_sanitizer"
Cohesion: 0.01
Nodes (188): _make_sanitizer(), asyncio, Underscore-delimited embedding_provider wording should still trigger rewrite., Collaborator multi-turn disclosure block prose should be normalized., Collaborator outbound text with raw file/trace leakage markers should be…, Collaborator form payload with raw tool/file leakage markers should be blocked., Caption-only payloads should not bypass collaborator leak normalization., Form caption field should be filtered the same as text/draft/message fields. (+180 more)

### Community 3 - "middleware.py"
Cohesion: 0.01
Nodes (166): fail(), ok(), run(), warn(), Initialize all security modules., Middleware Manager - P1 Security Hardening Orchestrates security modules for…, ApprovalHardening, ApprovalHardeningConfig (+158 more)

### Community 4 - "TelegramAPIProxy"
Cohesion: 0.01
Nodes (133): format_unknown_group(), Slack API Proxy — secures outbound bot → Slack traffic. Outbound: Bot Slack API…, Best-effort guardrail: collaborator prompts requesting direct file access., Detect conceptual file-purpose questions without direct content requests., Detect plain-language model status questions for deterministic local reply., Detect collaborator prompts probing sensitive filesystem paths/secrets., Detect collaborator prompts attempting path traversal style file access., Detect collaborator prompts targeting cloud metadata endpoints. (+125 more)

### Community 5 - "ResourceGuard"
Cohesion: 0.02
Nodes (78): t_resource(), get_resource_guard(), Any, Exception, Add a callback function to be called when resource alerts are triggered., Start background monitoring task., Stop background monitoring task cleanly., Best-effort cleanup for test contexts that don't call stop(). (+70 more)

### Community 6 - "test_soc_realtime_coverage.py"
Cohesion: 0.03
Nodes (42): _get_config_token(), _get_rbac_manager(), issue_session_token(), issue_ws_token(), Issue a short-lived, single-use WebSocket token for a user., Consume a WS token and return the user_id, or None if invalid/expired., FastAPI dependency: resolve Bearer/cookie token → user_id → role., Constant-time comparison against the gateway shared secret. (+34 more)

### Community 8 - "ToolChainAnalyzer"
Cohesion: 0.02
Nodes (72): ChainAction, ChainMatch, ChainPattern, ParamScanResult, Any, callable, Enum, str (+64 more)

### Community 9 - "KillSwitchMonitor"
Cohesion: 0.07
Nodes (27): deque, KillSwitchMonitor, Any, Check if the agent is responding within expected parameters. Returns: Dict…, Detect unusual patterns that might indicate rogue behavior. Args: tool_calls:…, Get current kill switch monitor status. Returns: Dict containing current status…, Monitor and verify kill switch functionality. Provides automated verification…, Test if the kill switch script exists. (+19 more)

### Community 10 - "soc/router.py"
Cohesion: 0.02
Nodes (278): Action, _ensure_collab_dir(), _load_collab_store(), load_persisted_collaborators(), load_removed_collaborator_ids(), pause_collaborator(), persist_approved_collaborator(), Enum (+270 more)

### Community 12 - "FakeRBAC"
Cohesion: 0.02
Nodes (95): FakeRBAC, _make_update(), PassthroughPipeline, Collaborator /revoke command must be blocked and quarantined., Punctuation-obfuscated blocked commands should still be quarantined., Pipeline that allows everything., Unicode zero-width obfuscation should not bypass blocked command enforcement., Leading whitespace/newline should not bypass collaborator blocked commands. (+87 more)

### Community 13 - "PIIConfig"
Cohesion: 0.01
Nodes (181): PIIConfig, PII detection and redaction configuration, PIISanitizer, Initialize Microsoft Presidio engines Falls back to regex if Presidio/spaCy…, PII detection and redaction engine Attempts to use Microsoft Presidio with…, Initialize sanitizer Args: config: PII configuration from agentshroud.yaml, Return current enforcement mode Returns: "enforce" or "monitor", Block credential display via untrusted sources (e.g., Telegram) Args: content:… (+173 more)

### Community 14 - "ToolResultInjectionScanner"
Cohesion: 0.03
Nodes (61): Any, Concise collaborator-safe reason text without internal leakage., Find first embedded tool-call JSON object inside arbitrary text., Remove Telegram HTML formatting tags from collaborator outbound text., Return True only when every Telegram-supported HTML open tag has a matching…, HTML-escape PII redaction placeholders so they render as literal text instead…, Filter outbound bot messages (sendMessage, etc.)., Extract the boundary token from a multipart Content-Type header. (+53 more)

### Community 15 - "test_soc_router_coverage.py"
Cohesion: 0.01
Nodes (85): _docker_exec_bot(), _unix_call(), _fetch_latest_release(), _file_hash(), Query GitHub releases API. Returns {"tag_name": ..., "html_url": ...} or…, Run a command inside the agentshroud-openclaw container via the Docker socket.…, client(), FakeAuditStore (+77 more)

### Community 16 - "MemoryLifecycleManager"
Cohesion: 0.11
Nodes (16): MemoryLifecycleManager, Any, Path, Archive a file to the archive directory., Enforce retention policy for daily notes., Enforce size limit for MEMORY.md file., Run all lifecycle maintenance tasks., Clean up old threat records. (+8 more)

### Community 18 - "._make_proxy"
Cohesion: 0.02
Nodes (62): _make_group_update(), Collaborator block notice should retry with deterministic unavailable fallback…, Owner block notice should retry with owner-specific fallback when first send…, Owner messages are never rate-limited by the collaborator limiter., Even a generic message triggers _send_collaborator_safe_info_response…, A blocked slash command must always produce a protected notice., Unknown users must always receive either a pending notice or a rate-limit…, Tests for lockdown UX: /unlock fix, collaborator notifications, /locked,… (+54 more)

### Community 20 - "services.py"
Cohesion: 0.10
Nodes (17): _check_clamd(), _check_fluent_bit(), _check_openscap(), _check_wazuh_agent(), _engine_health_to_health(), _engine_status_to_service_status(), _inspect_via_socket(), _known_services() (+9 more)

### Community 23 - "SSHProxy"
Cohesion: 0.02
Nodes (51): SSH command proxy with validation and audit support, Validate a command against allow/deny lists and injection patterns. Returns…, Check if a command is auto-approved (no human approval needed). Auto-approve…, Validate a remote working-directory path. Must be absolute and shell-safe., Validate a structured /ssh/write_file request (host, path, content). Returns…, Write file content to a remote host via structured (non-shell-string)…, Result of a structured SSH file-write operation (SSHProxy.write_file()), SSHProxy (+43 more)

### Community 24 - "asyncio"
Cohesion: 0.04
Nodes (43): OutboundInfoFilter, Any, Compile all filter patterns into regex objects., Get filter statistics., Main outbound information filtering engine. Uses compiled regex patterns to…, Initialize the outbound information filter. Args: config: Configuration…, ScanResult, Integration tests with other security components. (+35 more)

### Community 25 - "AsyncMock"
Cohesion: 0.03
Nodes (73): Unknown recipient's body is PII-scrubbed before approval queue submission., Owner-allowlisted recipient receives body verbatim; pii_redacted=False., /email/send-owner delegates to email_send and also skips PII for the owner., TestOwnerEmailBypassesPii, TestClose, TestProcessToolResult, _make_proxy(), _pass_result() (+65 more)

### Community 26 - "PathIsolationManager"
Cohesion: 0.08
Nodes (18): PathIsolationManager, any, Get the isolated temp directory path for a user., Sanitize user ID to prevent path traversal attacks., Rewrite a path to isolate it to the user's namespace. Args: path: Original file…, Check if path is trying to access the base AgentShroud directory., Check if path is trying to access another user's isolated namespace. Returns:…, Apply path rewriting rules to isolate paths per user. (+10 more)

### Community 27 - "TrustManager"
Cohesion: 0.03
Nodes (61): BotIncidentSeverity, CrossBotTrustLedger, IncidentRecord, IntEnum, A single cross-bot incident recorded in the ledger., Shared trust decay channel for multi-bot deployments. Usage:: ledger =…, Register bot_b as a peer of bot_a. Args: bot_a: Source bot name. bot_b: Peer…, Attach a TrustManager instance to a bot name. (+53 more)

### Community 28 - "RedactionResult"
Cohesion: 0.03
Nodes (61): Set configuration and initialize tool result sanitizer, Individual redaction record, Result of PII sanitization, RedactionDetail, RedactionResult, _analyze_and_anonymize(), Return the effective confidence threshold for one call (raise-only). The…, Detect PII in content and apply the enforcement action Args: content: Text to… (+53 more)

### Community 29 - "get_trivy_summary"
Cohesion: 0.14
Nodes (11): get_trivy_summary(), _is_fresh(), _load_latest_json(), Path, Score domain 29: AI Model & Supply Chain Integrity (0-5). MITRE ATLAS, OWASP…, Return True if the most recent report file was written within max_age_hours., Load the most recent JSON report file from a directory. Args: directory:…, Return latest Trivy scan summary from saved reports. When Trivy is installed… (+3 more)

### Community 30 - "EnhancedApprovalQueue"
Cohesion: 0.02
Nodes (141): Draft202012Validator, EnhancedApprovalQueue, timeout_handler(), Any, WebSocket, Close the store and cancel timeout tasks., Get the risk tier for a tool., Get the policy for a risk tier. (+133 more)

### Community 31 - "test_e2e_proxy.py"
Cohesion: 0.03
Nodes (91): ForwarderConfig, ForwardResult, HTTPForwarder, Any, Check if the OpenClaw backend is healthy., Configuration for the HTTP forwarder., Result of forwarding a request., Forwards sanitized requests to the OpenClaw backend. In production, uses… (+83 more)

### Community 32 - "EdgeOAuthService"
Cohesion: 0.07
Nodes (20): EdgeOAuthService, OAuthFailure, Any, Exception, Maps onto an RFC 6749 / 7591 error code at the HTTP layer., _edge(), edge_rpc(), _methods() (+12 more)

### Community 33 - "lifespan.py"
Cohesion: 0.04
Nodes (62): # NOTE: Gateway-side Slack Socket Mode listener removed., Application lifespan management for the AgentShroud Gateway, FilterMatch, FilterResult, InfoCategory, Enum, Categories of information that may need filtering., Filter agent response for sensitive information disclosure. Args:… (+54 more)

### Community 34 - "asyncio"
Cohesion: 0.03
Nodes (65): _mock_ws(), _pcm_bytes(), asyncio, ?agent=direct must route to _call_llm (fast path), not /forward., ?agent=hermes must route to _call_agent (gateway /forward), not _call_llm., When split_for_speech returns multiple sentences, the pipelined TTS loop must…, If a device sends LISTEN but never sends END (crash / stuck firmware), the…, pcm_chunks must stop growing once _PCM_MAX_BYTES is reached. A device that… (+57 more)

### Community 35 - "load_config"
Cohesion: 0.04
Nodes (93): load_config(), Load and validate configuration from agentshroud.yaml Search order: 1. Explicit…, MCPPolicyAction, MCPPolicyConfig, MCPPolicyDecision, MCPPolicyEngine, _norm(), Any (+85 more)

### Community 36 - "TestParanoidConfig"
Cohesion: 0.05
Nodes (10): _parse_env_file(), fixture, Path, minimal.env should have reasonable defaults., recommended.env should balance security and usability., Parse a .env file into a dict (ignoring comments and blanks)., paranoid.env should enable ALL security features., TestMinimalConfig (+2 more)

### Community 37 - "PromptGuard"
Cohesion: 0.02
Nodes (56): detect_base64_payloads(), Detect potential base64-encoded payloads in text. Returns list of decoded…, PromptGuard, Detect and block prompt injection attempts., Return HMAC key: env var preferred, session-scoped random fallback., Compute and return an HMAC-SHA256 fingerprint for the system prompt., Return True if prompt_text matches the stored HMAC fingerprint., Strip injected fake delimiters and return sanitized message. Called when… (+48 more)

### Community 39 - "main.rs"
Cohesion: 0.08
Nodes (54): AddResource, ApprovalAction, build_url(), Cli, CollabMode, Commands, deploy_status_formats_version_and_services(), deploy_status_no_services() (+46 more)

### Community 40 - "test_web_api_coverage.py"
Cohesion: 0.03
Nodes (48): client(), _make_app(), asyncio, FastAPI, fixture, A revert task is created (and is an asyncio.Task)., Second PUT cancels the first revert task., Auto-revert task sets mode back to enforce after delay. (+40 more)

### Community 41 - "test_edge_service_routes.py"
Cohesion: 0.03
Nodes (93): AccessToken, AsyncBaseTransport, AuthorizationCode, AuthorizationParams, Ed25519PublicKey, build_manifest(), canonical_bytes(), descriptor_hash() (+85 more)

### Community 42 - "test_agent_cve_registry.py"
Cohesion: 0.03
Nodes (72): get_agent_cve_summary(), list_cve_agents(), Any, Return the list of registered agent bot IDs with CVE coverage. Returns: List of…, Return a summary of the advisory registry for the specified agent. Counts are…, Upstream Agent Advisory Registry — tracks known vulns in the wrapped agents.…, _all_entries(), _hermes_by_title() (+64 more)

### Community 43 - "verify-proxy.sh"
Cohesion: 0.25
Nodes (16): infra-check.sh script, check(), preflight-check.sh script, fail(), ok(), tailscale-check.sh script, warn(), fail() (+8 more)

### Community 45 - "AgentTarget"
Cohesion: 0.03
Nodes (88): AgentTarget, Downstream agent target, ForwardError, Any, Exception, Determine which agent should receive this content Args: request: Forward…, Build the outbound payload for `target`, shared by the blocking and streaming…, Forward sanitized content to agent via HTTP POST Args: target: Agent target to… (+80 more)

### Community 48 - "discover_upstream_versions.py"
Cohesion: 0.04
Nodes (40): Tests for scripts/discover_upstream_versions.py — latest-release discovery.…, Hermes publishes date-based image tags (vYYYY.M.D)., latest'/'main' float and would defeat the whole point of pinning., Upstream fetches must survive a transient blip. 2026-10-16, dev host marvin:…, A fetch that never returns must not hang the unattended run. 2026-10-16: the…, Every Docker Hub failure on marvin was on IPv6; curl -4 was 100% clean., discover() applies the retry to both sources, independently., The 2026-10-16 CLOSE_WAIT hang: attempt 1 never returns; the hard deadline must… (+32 more)

### Community 49 - "api.py"
Cohesion: 0.03
Nodes (106): Configuration for container runtime selection and behavior. Loaded from…, Load configuration from environment variables., Runtime configuration for multi-engine container support., Load from a config dictionary (e.g. from YAML)., Resolve rootless setting based on runtime., RuntimeConfig, get_missing_features(), get_security_comparison() (+98 more)

### Community 50 - "EdgeStore"
Cohesion: 0.08
Nodes (14): EdgeStore, _h(), Any, Path, Async SQLite store. One instance per gateway process., Mint a one-time code the owner types on the consent page. Returned once., True exactly once for an unexpired code bound to ``vendor``; else None., The vendor with an open (unused, unexpired) enrollment, if exactly one. (+6 more)

### Community 51 - "WebProxy"
Cohesion: 0.03
Nodes (42): # NOTE: api.telegram.org is intentionally NOT listed here. The bot is, HTTP CONNECT proxy server — intercepts all bot outbound traffic. Listens on…, DomainSettings, Check if a domain is on the allowlist (used when mode == 'allowlist'). Supports…, Get settings for a specific domain, falling back to defaults., Check if a domain is on the denylist., Per-domain configuration overrides., Configuration for the web traffic proxy. Default-allow: all URLs pass unless… (+34 more)

### Community 52 - "TestConfigValidation"
Cohesion: 0.02
Nodes (55): ForwardRequest, Request to forward content through the gateway Received from iOS Shortcuts,…, parametrize, GatewayConfig validation behavior., openclaw init patch script must quarantine malformed JSON instead of exiting., openclaw init patch script must remove unsupported gateway.model key., OpenClaw's bot Dockerfile must pin via the shared ARG OPENCLAW_VERSION (backed…, openclaw init patch script must seed control UI origins for non-loopback bind. (+47 more)

### Community 53 - "test_llm_proxy.py"
Cohesion: 0.04
Nodes (67): First item yielded by proxy_messages_streaming(with_head=True). Carries the…, StreamHead, _FakeSanitizer, _FakeToolACL, _HeadFakeResponse, _make_fake_urlopen(), _proxy_with_connect_refused(), mock_forward() (+59 more)

### Community 54 - "PermissionLevel"
Cohesion: 0.04
Nodes (20): MCPToolConfig, MCPTransport, PermissionLevel, Any, Enum, str, Configuration for a specific MCP tool., Parse config from a dictionary (e.g. loaded from YAML). (+12 more)

### Community 55 - "fake_urlopen"
Cohesion: 0.02
Nodes (33): Identity enumeration prompts should return privacy-safe guidance., Cross-user activity probes should return privacy-safe collaborator guidance., Blocked env-secret probes should return deterministic Protect secret wording., Conceptual file-purpose questions should get safe info without file data access., Mixed BOOTSTRAP/IDENTITY purpose+show phrasing should return safe guidance, not…, Collaborator tool/command inventory probes should return safe local guidance., Collaborator blocked-tool policy question should be answered safely and…, Conceptual auth workflow questions should be answered safely (not hard-blocked). (+25 more)

### Community 57 - "IntelReportStore"
Cohesion: 0.05
Nodes (30): CompetitiveIntelReport, CompetitorEntry, _compute_hash(), IntelReportStore, Exception, field_validator, Path, Derive content_hash from the canonical content fields. Only computed when… (+22 more)

### Community 58 - "openclaw/skills/i-cr/SKILL.md"
Cohesion: 0.05
Nodes (31): Skill: cd, Skill: ci, Feedback Guidelines, Output Format, Production-Specific Review Checks, Review Principles, Role, Skill: Code Review (CR) (+23 more)

### Community 59 - "EgressFilter"
Cohesion: 0.04
Nodes (68): EgressFilterConfig, get_egress_config(), Configuration for egress filtering enforcement., Get the effective allowlist for a specific agent., Check if a domain matches the denylist., Check if domain matches any pattern in the list (supports wildcards)., Get the global egress filter configuration., Set the global egress filter configuration. (+60 more)

### Community 60 - ".get_or_create_session"
Cohesion: 0.07
Nodes (18): ConversationMessage, Any, Path, Initialize session manager. Args: base_workspace: Base directory for user…, Return the cache key string for a (user_id, bot_id) pair., Load existing sessions from metadata file. Handles both the new…, Atomically persist current sessions to the metadata file. Writes are serialized…, Validate and sanitize bot_id to prevent path traversal. Allows alphanumeric… (+10 more)

### Community 62 - "ingest_api/main.py"
Cohesion: 0.01
Nodes (354): EventBus, GatewayEvent, make_event(), Any, Helper to create a GatewayEvent with current timestamp, A single gateway event, Simple in-process event bus with async support, Subscribe to all events (+346 more)

### Community 63 - "AuditChain"
Cohesion: 0.06
Nodes (22): AuditChain, AuditChainEntry, PipelineResult, Any, Process an outbound response through the security pipeline. Thin wrapper around…, Process an outbound response through the security pipeline., An entry in the SHA-256 hash chain audit ledger., SHA-256 hash chain for tamper-evident audit logging. (+14 more)

### Community 64 - "scanner_integration.py"
Cohesion: 0.04
Nodes (74): _app_state_has(), compute_scorecard(), _compute_weighted_subscore(), _determine_compliance_level(), _determine_iec_sl(), _evaluate_mandatory_gates(), _is_container_running(), _is_containerized() (+66 more)

### Community 65 - "test_voice_gateway.py"
Cohesion: 0.02
Nodes (83): _fake_kokoro_pipeline(), _fw_client(), fixture, Empty STT result: no LLM call, state goes directly to idle., transcribe() calls the model and returns joined segment text., /voice is the one endpoint reachable over the public internet (Tailscale…, synthesize() runs the Kokoro pipeline; when rates match no resampling occurs., When OUTPUT_SAMPLE_RATE (24000, Kokoro native) != TARGET_SAMPLE_RATE (16000),… (+75 more)

### Community 66 - "version_routes.py"
Cohesion: 0.05
Nodes (54): downgrade_version(), get_available_versions(), get_current_version(), get_version_history(), Any, BaseModel, get, post (+46 more)

### Community 67 - "test_scanner_integration.py"
Cohesion: 0.07
Nodes (35): Score domain 4: Container Hardening (0-5). Baseline of 3 because docker-…, Score domain 5: Runtime Protection (0-5). 1=module exists, 2=running with…, Score domain 9: Logging & Monitoring (0-5). 1=SOC exists, 2=Wazuh running,…, Score domain 10: Compliance Auditing (0-5). 0=not run, 2=has failures, 3=zero…, Score domain 12: Incident Response (0-5). 1=SOC exists, 2=Falco running,…, Score domain 1: Image Integrity (0-5). 1=SBOM exists, 2=Trivy ran, 3=zero…, _score_compliance_auditing(), _score_container_hardening() (+27 more)

### Community 68 - "UserSessionManager"
Cohesion: 0.03
Nodes (52): GroupSession, Represents a shared workspace + memory for a group., Manages per-user, per-bot session isolation. Sessions are keyed by (user_id,…, Validate and sanitize user_id to prevent path traversal. Only allows…, Check if a user can access another user's session., Get or create a shared workspace + MEMORY.md for a group., Session Manager - Per-User Session Isolation Implements per-user session…, UserSessionManager (+44 more)

### Community 69 - "test_security_audit.py"
Cohesion: 0.02
Nodes (37): fixture, Test supply chain security measures., Dockerfile should be present for reproducible builds., Every security module should import without error., No hardcoded secrets in Python source files., All security modules should have copyright header., Security modules should not *call* eval() or exec(). Uses AST analysis so the…, Test prompt injection detection with adversarial payloads. (+29 more)

### Community 70 - "A2APolicyEngine"
Cohesion: 0.06
Nodes (77): A2AMethod, A2APolicyAction, A2APolicyDecision, A2APolicyEngine, _address_is_public(), is_safe_a2a_callback_url(), _method_of(), _norm() (+69 more)

### Community 71 - "NetworkValidator"
Cohesion: 0.04
Nodes (43): NetworkConfiguration, NetworkSecurityFinding, NetworkValidator, Any, Parse network configuration for a service., Validate network definitions in compose file., Validate service network isolation., A network security finding. (+35 more)

### Community 72 - "AgentRegistry"
Cohesion: 0.05
Nodes (36): AgentRegistry, ContainerConfig, IsolationCheck, IsolationStatus, IsolationVerifier, Enum, str, Verify that each agent has its own volume (no shared filesystems). (+28 more)

### Community 73 - "test_soc_bots.py"
Cohesion: 0.06
Nodes (37): compute_bot_scorecard(), Per-bot scorecard scoped to a single bot's image scan and egress stats. Scoring…, get_agent_cves(), get_config(), list_bots(), Return the list of registered bots. Falls back to backward-compat OpenClaw…, Return the tracked advisory registry for the wrapped AI agent. When bot_id is…, _make_app_state() (+29 more)

### Community 74 - "sync-cve-registry.py"
Cohesion: 0.06
Nodes (59): expr, get_agent_ghsa_repo(), Return the resolved GitHub advisory repo slug for *bot_id*. Honors the per-…, append_ghsa_entries(), render(), _append_nvd_entries(), render(), append_to_hermes_registry() (+51 more)

### Community 76 - "SessionManager"
Cohesion: 0.06
Nodes (20): EventInjectionError, Any, Exception, RateLimitExceeded, Generate a single-use, time-bound nonce for an instruction. Format:…, Return True if the nonce is valid (not replayed, within 5-min window). Side-…, Session Security Module - Secure session management for MCP gateway. Provides…, SessionBindingError (+12 more)

### Community 77 - "test_voice_latency_guard.py"
Cohesion: 0.07
Nodes (42): A connection-level error (not a status/timeout) also falls back to the trouble-…, test_call_agent_stream_generic_http_error_falls_back(), _mock_stream_resp(), asyncio, DEFAULT OFF: no_memory=False → empty metadata (request unchanged)., ON: no_memory=True → {"no_memory": True} ephemeral tag., The module-level default flag is OFF unless VG_VOICE_NO_MEMORY is set., DEFAULT OFF: /forward/stream body carries NO metadata key — byte-for-byte… (+34 more)

### Community 79 - "DifferentialPIIDetector"
Cohesion: 0.04
Nodes (41): DifferentialPIIConfig, DifferentialPIIDetector, _normalize_adversarial(), PIIHit, PIIHitSeverity, IntEnum, Full scan result for a tool result or prompt., Strip common adversarial encoding tricks, return (normalized, count_removed). (+33 more)

### Community 80 - "test_edge_facades.py"
Cohesion: 0.14
Nodes (13): HermesDelegate, LabSearch, PkeStatus, Any, datetime, The signed descriptor says "freshness per feed" — a stale feed (e.g. a GitHub…, test_delegate_wraps_task_as_untrusted_and_targets_restricted_profile(), test_lab_search_queries_fixed_endpoint_and_trims() (+5 more)

### Community 81 - "test_http_proxy_coverage.py"
Cohesion: 0.04
Nodes (66): _allowlist_proxy(), _capture_scans(), _CloseRaisesTargetWriter, _CloseRaisesWriter, _DummyTargetWriter, _eof_target_connection(), _open_conn(), _HeaderTimeoutReader (+58 more)

### Community 82 - "soc.js"
Cohesion: 0.06
Nodes (76): _AGENT_STATUS_BADGE, _ago(), _allGroups, _api(), _appendLogLine(), _applyAndRenderSbom(), _botContainerName(), _botParam() (+68 more)

### Community 83 - ".from_source"
Cohesion: 0.11
Nodes (24): deploy_manifest(), plan_deploy(), PlannedAction, One unit of work in a deploy plan (canonical entry -> per-bot path). ``action``…, Compute the deploy plan without mutating the filesystem. Pure with respect to…, Copy all files in *manifest* from *source* to each per-bot destination.…, Return names of entries that are missing or hash-mismatched in *dest*. Returns…, Skills manifest — build, deploy, and validate the canonical skills/agents/MCP… (+16 more)

### Community 84 - "ToolResultSanitizer.sanitize_tool_result"
Cohesion: 0.33
Nodes (6): ToolResultSanitizer._extract_dict_content, ToolResultSanitizer._extract_scannable_content, ToolResultSanitizer._get_sanitizer_for_tool, ToolResultSanitizer._log_redaction_audit, ToolResultSanitizer._reconstruct_result, ToolResultSanitizer.sanitize_tool_result

### Community 85 - "HTTPConnectProxy"
Cohesion: 0.04
Nodes (62): HTTPConnectProxy, Start the CONNECT proxy server., Stop the CONNECT proxy server., Return proxy traffic statistics., Asyncio HTTP CONNECT proxy server. Intercepts CONNECT tunnel requests,…, start() binds a real loopback server; a client gets a parsed response; stop()…, clamscan runs must never share the default executor with LLM upstream calls…, test_clamav_scans_use_dedicated_single_thread_executor() (+54 more)

### Community 87 - "cli/main.py"
Cohesion: 0.07
Nodes (63): argument, command, add(), add_collaborator(), add_group_member(), approve(), deny(), edge() (+55 more)

### Community 88 - "_make_proxy"
Cohesion: 0.04
Nodes (68): _anthropic_ok(), _anthropic_tool_use_ok(), _FakeSanitizer, _make_proxy(), _openai_ok(), _openai_tool_use_ok(), asyncio, parametrize (+60 more)

### Community 89 - "TrustConfig"
Cohesion: 0.03
Nodes (33): Build a ledger where every bot in *bot_ids* is a mutual peer of every other…, TrustConfig, Depth-2 propagation: A → B → C but NOT C → D when max_depth=2., build_full_mesh: N-agent-scalable topology construction. Adding a 3rd/4th/Nth…, The exact scenario the user asked for: add a 4th bot and it just works., End-to-end: a real incident on bot A decays trust on bots B and C in a 3-bot…, TestBuildFullMesh, Verify you can't jump from UNTRUSTED to FULL in one step. (+25 more)

### Community 90 - "hermes/skills/i-bs/README.md"
Cohesion: 0.03
Nodes (48): AWS Cloud Management & FinOps, Purpose, Related Skills, Usage, Branding Specialist (BS), Purpose, Related Skills, Usage (+40 more)

### Community 91 - "AgentShroud v0.8.0 "Watchtower" Release Plan"
Cohesion: 0.12
Nodes (22): EgressFilter, Approval Queue, Audit Trail, Container Runtime, CVE-2026-22708 (Prompt Injection bypass), CVE-2026-25253 (DNS Tunneling), DNS Tunneling, Enforce Mode (+14 more)

### Community 92 - "KillSwitchConfig"
Cohesion: 0.09
Nodes (20): KillSwitchConfig, Any, Convert configuration to dictionary for serialization., Configuration for kill switch monitoring and verification., Load configuration from environment variables., config(), dispatcher(), fixture (+12 more)

### Community 93 - "A2AProxy"
Cohesion: 0.07
Nodes (64): A2AProxy, A2AProxyResult, ParsedA2ARequest, Any, Terminates inbound A2A HTTP requests, enforces policy, forwards. Usage:: proxy…, Resolve peer identity from the Authorization: Bearer token. Never falls back to…, Parse a JSON-RPC 2.0 A2A request body into method/task_id/ callback_url. Raises…, Flatten an A2A Message's `parts` array to plain text for PII scanning. Returns… (+56 more)

### Community 94 - "AgentShroud — System Overview"
Cohesion: 0.12
Nodes (16): AgentShroud — System Overview, Components, Key Design Decisions, Related Notes, Security Layers (in order), What It Is, Who Depends On It, Why It Exists (+8 more)

### Community 95 - "chatbot/main.py"
Cohesion: 0.23
Nodes (11): _get_auth_token(), lifespan(), load_persona_files(), FastAPI, HTTPAuthorizationCredentials, Isaiah Chat Service - Phase 3 MVP Minimal chat service with Isaiah's…, FastAPI lifespan - initialize OpenAI client and persona once., Load Isaiah's persona from IDENTITY, SOUL, and USER files. (+3 more)

### Community 96 - "._extract_first_egress_target"
Cohesion: 0.04
Nodes (21): Detect plain NO_REPLY sentinel with light punctuation wrapping., Best-effort check to avoid treating local file names as egress domains., Detect patterns that must redact for ALL non-owner chats, including…, Detect leakage patterns blocked for local_only/project_scoped collaborators.…, Detect internal approval/egress banner text that must remain owner-only., Detect legacy bracket-style block notices for collaborator normalization., Extract first outbound web target (URL or bare domain) for egress preflight., Unit tests for outbound target extraction helper used by egress preflight. (+13 more)

### Community 98 - "test_ws_e_rt2_inbound_encoding.py"
Cohesion: 0.05
Nodes (53): DecodedLayer, EncodingConfig, EncodingDetector, replacer(), replacer(), replacer(), EncodingResult, Decode rot13-obfuscated injection payloads. rot13 is self-inverse and applies… (+45 more)

### Community 99 - "DraftEntry"
Cohesion: 0.06
Nodes (34): CitationVerifier, DraftEntry, FetchOutcome, _fetch(), An unverified competitor claim submitted for citation checking., Verifies competitor claims against re-fetched, allowlisted sources., Re-fetch *url* and return a Citation iff it is allowlisted + live. SSRF…, Return a CompetitorEntry with only its valid citations, or None. None means the… (+26 more)

### Community 100 - "test_mfa_guard.py"
Cohesion: 0.06
Nodes (64): MFAGuard, MFAResult, Verify a TOTP second factor for high-risk operations (fail-closed). Args:…, Build an MFAGuard from environment variables / Docker secret file. Recognized…, Return True if ``action_type`` requires a second factor right now. Two classes…, Verify the second factor for a high-risk action. Args: action_type: The action…, Decode a base32 secret; return b"" on empty/invalid input., Compute the RFC 6238 TOTP value for a specific time-step counter. (+56 more)

### Community 101 - "app"
Cohesion: 0.03
Nodes (58): auth_dep(), Authentication dependency for protected endpoints, client(), fixture, Sync TestClient for WebSocket tests, sync_client(), client(), fixture (+50 more)

### Community 102 - "FalcoAlertWatcher"
Cohesion: 0.06
Nodes (32): categorize_alerts(), configure_rules(), FalcoAlertWatcher, generate_summary(), is_agentshroud_rule(), parse_alert(), Any, datetime (+24 more)

### Community 103 - "WebProxyResult"
Cohesion: 0.18
Nodes (7): Any, Check an outbound HTTP request before it's sent. This is the pre-flight check.…, Scan a response body for prompt injection, PII, and hidden content. This is…, Result of proxying a web request., Record an audit entry in the hash chain., Get proxy statistics., WebProxyResult

### Community 104 - "triage-cve-mitigations.py"
Cohesion: 0.05
Nodes (56): CVE Triage — Gaps & Development Plan (OpenClaw), 891 triaged, ASH-OCLAW-113 auth_bypass partially_mitigated (running 2026.9.8, fixed_in None), ASH-OCLAW-230 dos under_review (running 2026.9.8, fixed_in None), _AGENT_CVE_REGISTRIES, _HERMES_CVE_REGISTRY, _OPENCLAW_CVE_REGISTRY, test_no_entry_id_looks_like_a_cve, test_real_registry_plan_is_internally_consistent (+48 more)

### Community 105 - "MCPToolCall"
Cohesion: 0.06
Nodes (24): MCPToolCall, MCPToolResult, Represents an MCP tool_use request., Represents an MCP tool result., A policy-permitted call passes the policy gate (inspection/permission layers…, test_mcp_proxy_allows_policy_permitted_call(), _ok(), TestDataclasses (+16 more)

### Community 106 - "Added"
Cohesion: 0.13
Nodes (22): [0.2.0] - 2026-02-17, [0.4.0] - 2026-02-19, Added, Added, Added, Added, Added, Changed (+14 more)

### Community 107 - "TestEgressApprovalQueue"
Cohesion: 0.04
Nodes (42): ApprovalResult, EgressRequest, Enum, Result of an approval request., Risk assessment levels for egress requests., Represents a pending egress approval request., RiskLevel, asyncio (+34 more)

### Community 108 - "test_edge_network_isolation.py"
Cohesion: 0.07
Nodes (41): _add_env(), check_dmz_members(), check_dmz_subnet_unique(), check_edge_on_dmz_only(), check_forwarder_targets_edge(), check_gateway_edge_port_loopback_only(), check_gateway_keeps_dual_membership(), check_issuer_matches() (+33 more)

### Community 110 - "MCPPermissionManager"
Cohesion: 0.04
Nodes (30): MCPPermissionManager, _walk(), PermissionCheck, PrivateAccessAttempt, PrivateRedactionEvent, RateLimitEntry, Result of a permission check., Track rate limit state for a tool+agent combo. (+22 more)

### Community 111 - "_canonicalize_ip_literal"
Cohesion: 0.40
Nodes (5): _BaseAddress, _canonicalize_ip_literal(), _int_to_ipv4(), Best-effort canonicalization of alternate IPv4 encodings that…, IPv4Address

### Community 112 - "patch"
Cohesion: 0.05
Nodes (12): detect_runtime(), get_engine(), Auto-detect which container runtimes are available on this system., Return an appropriate container engine instance. Args: preference: Explicit…, patch, Test the management API endpoints with mocked runtime., TestAppleContainerEngine, TestDetectRuntime (+4 more)

### Community 113 - "CronStateMonitor"
Cohesion: 0.08
Nodes (23): CronStateMonitor, JobState, One poll pass over all stores. Never raises., Evaluate one job. Returns 1 if a NEW episode was alerted. Flood guard (review…, Start the poll loop as an asyncio task (idempotent)., Cron job failure monitor (SCRUM-61 part 2). Detection half of cron/job failure…, Normalized view of one bot cron job., Poll bot cron stores; dispatch AlertDispatcher alerts on failures. (+15 more)

### Community 114 - "test_collaborator_responses.py"
Cohesion: 0.04
Nodes (34): build_project_context_injection(), format_addtogroup_success(), format_already_member(), format_group_info(), format_groups_list(), format_no_permission(), format_not_member(), format_projects_list() (+26 more)

### Community 115 - "EncryptedStore"
Cohesion: 0.04
Nodes (26): EncryptedStore, Derive a 256-bit key from master secret using PBKDF2-HMAC-SHA256., Encrypt data using AES-256-GCM. Args: data: String, bytes, or dict (JSON-…, Decrypt an AES-256-GCM encrypted blob. Args: blob: The encrypted blob from…, Decrypt and return as UTF-8 string., Decrypt and return as parsed JSON dict., Encrypt and return as base64-encoded string., Decrypt a base64-encoded blob. (+18 more)

### Community 116 - "PrivacyPolicyEnforcer"
Cohesion: 0.05
Nodes (28): PrivacyPolicy, PrivacyPolicyEnforcer, Enum, str, Privacy policy configuration. Loaded from agentshroud.yaml `privacy:` section., Parse from a YAML/dict representation. Example YAML: privacy: services: gmail:…, Return a default policy with all known private services locked down., Evaluates access control and filters responses per privacy policy. (+20 more)

### Community 117 - ".agents/skills/i-cr/SKILL.md"
Cohesion: 0.04
Nodes (42): Skill: bdd, Feedback Guidelines, Output Format, Production-Specific Review Checks, Review Principles, Role, Skill: Code Review (CR), Data Validation (DATA-VAL) (+34 more)

### Community 118 - "upgrade-2026-09-21.md"
Cohesion: 0.10
Nodes (29): Colima docker-socket forward death under load, Dev/prod account split (agentshroud-bot vs ijefferson.admin), Host network filter blocking Homebrew Python/Node outbound, dev-result-<date>.json dev->prod handoff contract, Verify the executable line, not the commit message, Host memory pressure on marvin (near-OOM, 90%+ swap), Shared working-tree collision between concurrent sessions, Vendor supply-chain freshness gate (npm min-release-age / uv exclude-newer) (+21 more)

### Community 119 - "_make_proxy"
Cohesion: 0.06
Nodes (30): _make_proxy(), asyncio, _RaisingRedactionResult, Cached correlation for the channel → no Slack history call; outbound is…, Correlation ID with no ':' separator → outbound attributed to channel id., Thread reply with no cached corr → conversations.replies lookup recovers the…, Non-thread reply → conversations.history lookup; bot and subtype messages are…, History lookup returns ok=False → no inbound record; outbound still logged,… (+22 more)

### Community 121 - "URLAnalyzer"
Cohesion: 0.04
Nodes (32): _looks_like_base64(), Enum, str, Analyze URLs for SSRF, data exfiltration, and suspicious patterns., Args: resolve_dns: If True, resolve hostnames to IPs and check those too.…, Analyze a URL for security issues. Returns URLAnalysisResult with verdict and…, Check if hostname is a private/reserved address (SSRF attempt)., Check if an IP address is private/reserved/loopback. (+24 more)

### Community 122 - "KeyRotationManager"
Cohesion: 0.03
Nodes (80): CredentialRotationPolicy, KeyRotationConfig, Get rotation policy for a credential type, falling back to api_key default., Add or update a rotation policy for a specific credential type., Check if a specific emergency trigger is enabled., Build a complete op:// reference for a credential., Rotation policy for a specific credential type., Configuration for key rotation policies and schedules. (+72 more)

### Community 123 - "test_e2e_watchtower.py"
Cohesion: 0.04
Nodes (42): _BrokenOutputCanary, _BrokenSanitizer, pii_config(), pipeline(), asyncio, fixture, E2E-02: Social security numbers and email are redacted before forwarding., E2E-03: PII in agent responses is stripped before delivery. (+34 more)

### Community 124 - "ApprovalRequest"
Cohesion: 0.03
Nodes (101): GroupApprovalRouter, Any, Return True if agent_id represents a Telegram group workspace., Extract the raw chat_id from a group-{chat_id} agent_id. Returns None if the…, Build the owner DM notification text., Build the group thread reply notification text., No-op send stub — used when no transport is injected., Routes approval notifications to owner DM and (optionally) group thread. Args:… (+93 more)

### Community 126 - "sunday-upgrade-apply.sh"
Cohesion: 0.09
Nodes (66): Colima/Docker VM Storage Exhaustion, Sunday Upgrade Report 2026-09-06 (prod read-only, pre-crisis), Sunday Upgrade Report 2026-09-06 (prod, disk-exhaustion incident), asb clean-rebuild [full|hermes], COMPOSE (asb compose command string), Compose profile gating (voice/hermes/full), _PROFILE_FLAG, PROJECT (compose project name) (+58 more)

### Community 127 - "fake_owner_notice"
Cohesion: 0.03
Nodes (22): Owner /approve should fail closed when target has no pending request., Owner /deny with no target and NO pending collaborator request must not be…, Owner /deny without target, with 2+ pending collaborator requests, is genuinely…, Owner /deny with one pending request should deny that request., Owner /addcollab should add collaborator and clear revoked state., Owner /addcollab without target should return usage guidance., Owner /addcollab should accept known collaborator short-name aliases., Owner /restorecollabs should restore baseline collaborator IDs. (+14 more)

### Community 128 - "EgressPolicy"
Cohesion: 0.05
Nodes (40): EgressAction, EgressPolicy, Enum, str, Set a per-agent egress policy., Egress policy for an agent or global default., Check if domain matches any allowed domain (supports wildcards). Wildcards only…, Check if IP matches any allowed IP/CIDR. (+32 more)

### Community 129 - "LLMProxy.proxy_messages (non-streaming)"
Cohesion: 0.13
Nodes (30): LLMProxy._apply_filters, LLMProxy._build_timeout_fallback_response, LLMProxy._emit_failover_notice, LLMProxy._enforce_tool_acl, LLMProxy._failover_request, LLMProxy._filter_outbound, LLMProxy._filter_outbound_streaming, LLMProxy._filter_streaming_event (+22 more)

### Community 130 - "TestOutboundInfoFilter"
Cohesion: 0.03
Nodes (32): Test that sensitive MCP tool names are filtered., Test that common English words are not filtered., Test that Telegram user IDs are filtered., Test that security module references are filtered., AgentShroud brand name must pass through unredacted (Fix C)., Test that credential paths are filtered., Test that internal file paths are filtered., Test suite for the outbound information filter. (+24 more)

### Community 131 - "parse_trivy_output"
Cohesion: 0.09
Nodes (15): generate_summary(), parse_trivy_output(), Any, Path, Parse raw Trivy JSON output into a structured summary. Args: raw: Raw JSON…, Save a Trivy report to the log directory. Args: report: Parsed report dict.…, Generate a summary dict suitable for the health report. Args: report: Parsed…, save_report() (+7 more)

### Community 132 - "test_mcp_proxy_coverage.py"
Cohesion: 0.08
Nodes (15): FakeApprovalQueue, FakeConn, make_call(), make_config(), make_proxy(), Exception, Stand-in connection injected into the proxy's pool., Coverage tests for gateway/proxy/mcp_proxy.py. Targets the branches not… (+7 more)

### Community 135 - "test_anthropic_openai_translator.py"
Cohesion: 0.05
Nodes (55): _random_msg_id(), OpenAI-compat SSE stream → Anthropic SSE stream translator. Consumes an async…, Translate an OpenAI-compat SSE byte stream to Anthropic SSE byte events. Yields…, _sse(), translate_openai_sse_to_anthropic(), _anthropic_content_to_openai(), _anthropic_system_to_openai(), anthropic_to_openai_request() (+47 more)

### Community 138 - "GroupWorkspaceManager"
Cohesion: 0.05
Nodes (28): GroupAccessDenied, GroupWorkspaceManager, Canonical workspace id for a group chat_id: ``group-{chat_id}``., Canonical workspace id for a direct-message context: ``dm-{user_id}``., Return True if user_id may access the workspace for ``group_chat_id``. A DM…, Resolve the workspace/context for an inbound message, fail-closed. Returns:…, Read a group's shared memory, gated by member access (fail-closed)., Append to a group's shared memory, gated by member access (fail-closed). (+20 more)

### Community 139 - "upgrade-2026-10-12.md"
Cohesion: 0.04
Nodes (45): Base docker-compose stack, Marvin dev compose override (agentshroud-bot), Features: Prompt Injection Defense, PII Sanitization, Egress Filtering, Human-in-the-Loop, IEC 62443, Presidio PII detection deps (analyzer/anonymizer/spacy), python-jose removal (CVE-2024-33663/33664), Transitive-dependency security floors (pip-audit gate), websockets 16.1.1 -> 17.1 Sunday upgrade bump, 1. Summary line (+37 more)

### Community 142 - "test_llm_proxy_failover.py"
Cohesion: 0.07
Nodes (38): _call_proxy(), make_proxy(), asyncio, x-agentshroud-interactive: 1 → the first 429 returns immediately (no 2s/4s/8s…, Without the interactive flag the 3-retry loop is unchanged (guards the hermes-…, Updated 2026-06-15: a plain 429 that escaped the upstream retry loop NOW…, Tests for the cloud→local quota failover orchestrator in LLMProxy., HTTP 200 with an overloaded_error body must trigger local failover. (+30 more)

### Community 143 - "KeyVault"
Cohesion: 0.05
Nodes (19): KeyAuditEvent, KeyEntry, KeyInjector, KeyLeakDetector, KeyVault, KeyVaultConfig, LeakScanResult, Check if any stored key values appear in text. Returns matching key names. (+11 more)

### Community 144 - "AgentShroud v0.7.0 Enforcement Audit Results"
Cohesion: 0.11
Nodes (33): ContextGuard (context window poisoning defense), Egress Filter / SSRF Protection, FileSandbox (path isolation), GitGuard (supply-chain hook scanning), Kill Switch (FREEZE/SHUTDOWN/DISCONNECT), MCP Proxy Layer (tool-call interception), PII Sanitizer (Presidio + regex hybrid), PromptGuard (Prompt Injection Defense) (+25 more)

### Community 145 - "._run_and_read"
Cohesion: 0.06
Nodes (27): CompletedProcess, Path, local qwen3:14b: second run leaves env identical., local-coder target: second run leaves env identical., local-anchor target: second run leaves env identical., anthropic target: second run leaves env identical., Expected keys are present in docker/.env after a switch., --verify flag causes switch_model.sh to check both bots are healthy. (+19 more)

### Community 146 - "asyncio"
Cohesion: 0.05
Nodes (19): _make_error_report(), asyncio, OpenClaw and Hermes are processed on fully separate paths; one failing never…, The 06:05 check and the 07:00 GHSA ingest share one diff; an advisory still…, check_upstream_cves(agent_id=...) selects that agent's OWN repo + list., Owner wants to SEE a Hermes report even with 0 new advisories., If the per-agent source config is missing, the label falls back gracefully., A Telegram failure on the zero-report path never raises. (+11 more)

### Community 147 - "asyncio"
Cohesion: 0.03
Nodes (23): asyncio, Hypothetical execution policy questions should get safe info, not hard block., Rate-limit notice helper should report unsent when bot token is unavailable., Cross-tenant/workspace data probes should be blocked and quarantined., Plugin/tool auto-discovery inventory prompts should be blocked., Collaborator scheduler/autorun requests should be blocked and quarantined., Plain language model question should be answered by gateway directly., Owner /whoami should be handled locally and include owner role + user id. (+15 more)

### Community 148 - "test_security_regressions_v1_2.py"
Cohesion: 0.04
Nodes (39): fixture, BT-H4 (reverse): Writing to Hermes workspace does not bleed into OpenClaw., BT-H1: SharedMemoryManager.get_user_memory must accept a bot_id parameter. The…, Finding RT-N1/RT-N2: TrustManager uses shared in-memory DB keyed by agent_id.…, RT-N1: Recording a violation against openclaw MUST NOT change hermes trust., RT-N1 (reverse): Hermes violation must not demote OpenClaw., RT-N2: Bot agent IDs ('openclaw', 'hermes') are separate from user IDs. A…, RT-N3: lifespan.py seeds 'hermes' with STANDARD trust. Verifies the seeding… (+31 more)

### Community 149 - "llm-init.sh"
Cohesion: 0.08
Nodes (48): llm-init(), _llm_init_agent_reference_paths(), _llm_init_any_tool_enabled(), _llm_init_bounded(), _llm_init_check_sf(), _llm_init_check_twg(), _llm_init_convert_agent(), _llm_init_convert_for_copilot() (+40 more)

### Community 151 - "test_config_hot_reload.py"
Cohesion: 0.11
Nodes (34): apply_reloadable_config(), config_watcher(), _default_mtime(), Path, Copy only the reloadable-field subset from ``new`` onto ``current`` in place.…, Re-parse and validate ``config_path``; atomically swap in reloadable fields.…, Return the file mtime, or -1.0 if the file is missing (treated as no-op)., Background mtime-poll watcher: reload the config when the file changes. Polls… (+26 more)

### Community 153 - "2. Security Analysis"
Cohesion: 0.05
Nodes (42): 1. Changes in This Diff, 2. Security Analysis, 2a. Owner Bypass (`OWNER_USER_IDS`) — ⚠️ WARNING, 2b. Telegram SDK Patch Removal — ⚠️ WARNING, 2c. Telegram Proxy Auth Added — ✅ GOOD, 2d. Credential Reference Fixes — ✅ GOOD, 2e. Gateway Auth Simplification — ✅ GOOD, 3. Code Quality (+34 more)

### Community 154 - "test_forward_stream.py"
Cohesion: 0.08
Nodes (47): _filtered_sentence_stream(), _event_stream(), Resolve the outbound trust level for `request`, shared by the blocking and…, Buffer streamed text deltas and yield each complete sentence as soon as its…, 2-sentence sliding window over `sentences`: each window (previous + current,…, _resolve_user_trust_level(), _sentences_from_deltas(), _aiter() (+39 more)

### Community 155 - "ContainerSnapshot"
Cohesion: 0.06
Nodes (20): ContainerSnapshot, DriftAlert, DriftDetector, Retrieve baseline snapshot for a container., Compare current config against baseline, return any drift alerts., Retrieve stored drift alerts., Mark an alert as acknowledged., SHA-256 hash of the config for quick comparison. (+12 more)

### Community 156 - "_engine"
Cohesion: 0.05
Nodes (12): _engine(), _gitless_run(), fake_run(), Build a subprocess.run double that simulates the upgrade git flow., TestAgentshroudUpdates, TestBotUpdates, TestKillSwitch, TestLogs (+4 more)

### Community 157 - "SecurityPipeline"
Cohesion: 0.05
Nodes (44): AppState, Container for application-wide state, Set global observatory mode for all security modules. Args: mode: "monitor" or…, Main security pipeline that all messages pass through. Wires together:…, SecurityPipeline, CanaryCheck, CanaryResult, Any (+36 more)

### Community 159 - "mcp"
Cohesion: 0.05
Nodes (43): command, enabled, type, command, enabled, type, command, enabled (+35 more)

### Community 160 - "telegram_proxy.py"
Cohesion: 0.05
Nodes (33): _OutboundScan, Telegram API Reverse Proxy — intercepts all bot ↔ Telegram traffic. The gateway…, Result of the shared outbound text security scan. processed: a scan path…, DelegationPrivilege, str, Subset of privileges that can be delegated by the owner., _load_overrides(), persist_group_collab_mode() (+25 more)

### Community 161 - "test_telegram_proxy_inbound.py"
Cohesion: 0.05
Nodes (26): Return True if message originates from a group or supergroup chat., Return True if the bot is @mentioned or a bot_command targets this bot. Checks…, Normalize first command token so small obfuscations don't bypass local handlers., _no_owner_mirror(), _no_real_telegram_network(), fixture, Tests for TelegramAPIProxy inbound security pipeline integration. Proves that…, Stub the fire-and-forget owner activity mirror. The mirror runs via… (+18 more)

### Community 162 - "IEC 62443 Compliance Matrix — AgentShroud"
Cohesion: 0.07
Nodes (28): Current Assessment: **SL 2** (with SL 3 capabilities in FR 2, FR 3, FR 4, FR 6), FR 1: Identification and Authentication Control (IAC), FR 2: Use Control (UC), FR 3: System Integrity (SI), FR 4: Data Confidentiality (DC), FR 5: Restricted Data Flow (RDF), FR 6: Timely Response to Events (TRE), FR 7: Resource Availability (RA) (+20 more)

### Community 163 - "test_redteam_probes.py"
Cohesion: 0.06
Nodes (52): _make_approval_queue(), _make_full_pipeline(), pipeline(), asyncio, fixture, Probe 1.1c: admin_action must require approval or be trust-blocked., Probe 1.6: EgressFilter must block non-allowlisted domains., Probe 1.6b: EgressFilter must block direct IP exfiltration. (+44 more)

### Community 164 - "AgentShroud Security Architecture"
Cohesion: 0.05
Nodes (39): Defense-in-Depth, DNS Filtering, Audit Ledger (SQLite), Bot Identity Separation (Separate Accounts), AgentShroud Security Architecture, Executive Summary, Docker Network Isolation (agentshroud-isolated), PII Sanitization at Gateway Boundary (+31 more)

### Community 165 - "test_telegram_replay.py"
Cohesion: 0.06
Nodes (32): Any, Mark all updates with update_id < offset as delivered (normal getUpdates ack)., Return undelivered updates older than grace window (avoids replay storms)., Periodically prune rows older than retention window., Telegram update replay buffer — SQLite WAL, bot-agnostic. Records every…, SQLite-backed Telegram update store, safe for concurrent asyncio callers., Close the SQLite connection (idempotent)., Persist inbound updates so they can be replayed after a crash. (+24 more)

### Community 167 - "test_bots_ssh_exec_wrapper.py"
Cohesion: 0.06
Nodes (42): _bearer_from_argv(), _build_payload_via_shell(), _extract_payload_builder(), _fenced_code_blocks(), CompletedProcess, Wrapper is COPY'd into and chmod'd in BOTH bot Dockerfiles., Hermes' belt-and-suspenders tirith trust must be scoped, never blanket. It may…, The wrapper must NOT shell out to python3/python for JSON building. Regression:… (+34 more)

### Community 168 - "Colima & Docker Operations Guide — AgentShroud"
Cohesion: 0.05
Nodes (38): 10. Port Forwarding — Dual-Stack Bind Race (silently unreachable host port), 11. Common Errors — Quick Reference, 12. Dev Account (agentshroud-bot) Operations, 1. Environment Overview, 2. `asb` Helper — Primary Interface, 3. Colima VM Lifecycle, 4. Disk & Resource Monitoring, 5. Container Management (+30 more)

### Community 169 - "_stub_client"
Cohesion: 0.09
Nodes (13): cli(), AgentShroud SOC CLI — Shared Command Layer., _all_output(), _invoke(), parametrize, Replace SCLClient in main with a MagicMock factory; return the instance., stdout + stderr regardless of click version (mix_stderr removed in 8.2)., _stub_client() (+5 more)

### Community 170 - "SCLClient"
Cohesion: 0.12
Nodes (3): Any, Minimal synchronous httpx-free client for the SCL API., SCLClient

### Community 171 - "DNSFilterConfig"
Cohesion: 0.06
Nodes (24): t_dns(), DNSFilter, DNSFilterConfig, DNSQuery, DNSVerdict, Resolve domain to an IP and cache it for 5 minutes., Return True if the IP address is in a private / loopback range., TunnelingPattern (+16 more)

### Community 172 - "TokenValidator"
Cohesion: 0.07
Nodes (24): t_token(), AudienceMismatch, IssuerMismatch, Any, Exception, Close the audit-log database connection., Token Validation Module - Validates MCP token claims before passthrough.…, ScopeViolation (+16 more)

### Community 173 - "AgentShroud v0.9.0"
Cohesion: 0.05
Nodes (40): Adversarial Red-Team / Blue-Team Assessment, AgentShroud v1.3.0, Executive Summary, How to regenerate this report accurately, Test Coverage Report, 10.1 Test Metrics Dashboard, 10.2 Release Readiness Criteria, 10. Test Reporting (+32 more)

### Community 174 - "hermes/skills/i-cr/SKILL.md"
Cohesion: 0.05
Nodes (37): Skill: bdd, Skill: cd, Skill: ci, Feedback Guidelines, Output Format, Production-Specific Review Checks, Review Principles, Role (+29 more)

### Community 175 - "Skill: MCP AWS Profile Configuration (MCPM-AWS-PROFILE)"
Cohesion: 0.05
Nodes (39): MCP AWS Profile Configuration (MCPM-AWS-PROFILE), Purpose, Related Skills, Usage, "Access Denied", AWS Profile Basics, AWS SSO Configuration, Best Practices (+31 more)

### Community 176 - "_wrap_response"
Cohesion: 0.04
Nodes (21): Blocked collaborator commands should be retained in quarantine store., Mention + punctuation variants should still be blocked for collaborators., Uppercase collaborator blocked commands should still be quarantined., Zero-width + mention/punctuation blocked command variants should still be…, Direct secret/token value requests should be blocked and quarantined., Collaborator command-policy questions should get informative guidance, not hard…, Collaborator model/provider switching requests should be blocked., Allowlist/redirect-bypass prompts should be blocked and quarantined. (+13 more)

### Community 177 - "Quality Assurance (SKILL)"
Cohesion: 0.15
Nodes (16): Incident Response (SKILL), Production Safety Checklist (SKILL), Purpose, Quality Assurance (QA), Related Skills, Usage, Quality Assurance (README), Quality Assurance (SKILL) (+8 more)

### Community 178 - "AgentShroud Agentic OS"
Cohesion: 0.05
Nodes (38): 10. Infrastructure & Runtime, 12. MCP Integrations, 13. Compliance Alignment, 14. Gap Analysis & Recommendations, 1. System Overview, 2. Multi-Agent Hierarchy, 3. Agent Inventory, 5. Orchestration Flow (+30 more)

### Community 179 - "OpenClaw Workspace Usage Guide"
Cohesion: 0.05
Nodes (38): Configuration, Current Setup (Kept), Decision Summary, Files Created, Helper Script, Next Steps, Why This Matters for Read-Only Filesystem, Workspace Configuration Decision (+30 more)

### Community 181 - "test_hermes_model_resolver.py"
Cohesion: 0.06
Nodes (45): _apply_stale_alias_correction(), main(), provider_for_model(), Return the Hermes provider key for a bare model name. Local models…, Resolve (model, provider) for Hermes from the container environment.…, CLI: `resolve_model.py [model|provider]`. Defaults to 'model'., Resolve the model + provider Hermes should use, honouring local-model parity.…, Strip a known provider prefix from a model ref, leaving the bare model name.… (+37 more)

### Community 182 - "MCPServerConfig"
Cohesion: 0.07
Nodes (18): MCPServerConfig, Configuration for an MCP server., ConnectionPool, HttpSseConnection, Start the MCP server process., Send a JSON-RPC request and read the response., Stop the MCP server process., Manages an HTTP/SSE connection to an MCP server. (+10 more)

### Community 183 - "mcp_proxy.py"
Cohesion: 0.06
Nodes (27): ProxyResult, Result of proxying an MCP tool call., asyncio, Missing server_name or tool_name should return 422., Response should include processing_time_ms., x-agentshroud-user-id header must override spoofable body agent_id., Body agent_id is used only when trusted header is absent., Body-only owner identity must be rejected to prevent impersonation. (+19 more)

### Community 184 - "MCPAuditTrail"
Cohesion: 0.09
Nodes (13): MCPAuditEntry, MCPAuditTrail, Any, Log an outgoing MCP tool call., Log an incoming MCP tool result., Verify integrity of the retained MCP audit hash-chain window. Anchors at the…, A single MCP tool call audit entry., Generate an MCP audit report summary. (+5 more)

### Community 185 - "test_security_toolchain.py"
Cohesion: 0.08
Nodes (24): calculate_overall_score(), calculate_tool_score(), format_report(), generate_report(), get_trend(), init_db(), Any, Connection (+16 more)

### Community 186 - "check_benchmark_regression.py"
Cohesion: 0.36
Nodes (8): check(), _compare(), _is_number(), _load_json(), main(), Path, Benchmark regression checker (SCRUM-201). Reads the results JSON written by…, Return the parsed dict, or None after printing why it could not be loaded.

### Community 187 - "_token"
Cohesion: 0.08
Nodes (16): _pct(), test_edge_read_call_latency(), _profile(), Edge calls must not inherit the pipeline's owner exemption., throttle → writes disabled → token revoked → vendor disabled, each audited., TestAuditRecord, TestCommandCenterStats, TestMonitorMode (+8 more)

### Community 188 - "test_runtime_engines.py"
Cohesion: 0.06
Nodes (18): generate_apple_script(), generate_compose(), Generate a shell script to start services with Apple Containers. Apple…, Definition of a single service for compose generation., Generate a compose YAML file for Docker or Podman. Args: services: List of…, ServiceDef, get_features_for_runtime(), get_security_options() (+10 more)

### Community 189 - "Release Notes - AgentShroud v0.9.0"
Cohesion: 0.05
Nodes (39): Acknowledgments, 🔍 Advanced Audit Capabilities, 🤖 AI-Powered Security, ⚠️ Breaking Changes, Breaking Changes and Migration, 🤝 Community and Support, 📚 Comprehensive Documentation Suite, 👥 Contributors (+31 more)

### Community 190 - "EgressEvent"
Cohesion: 0.08
Nodes (25): AlertSeverity, AnomalyAlert, EgressChannel, EgressEvent, EgressMonitor, EgressMonitorConfig, EgressSummary, Enum (+17 more)

### Community 192 - "AgentShroud™ Brand Guidelines"
Cohesion: 0.10
Nodes (19): AgentShroud™ Brand Guidelines, Brand Identity, Colors, Communication Templates, Elevator pitch, Key Messaging, License, Logo Usage (+11 more)

### Community 193 - "SecureBrowser - Enterprise Secure Browser Automation"
Cohesion: 0.06
Nodes (31): 1. Always Specify Risk Level, 1Password Integration, 2. Use Allowlisting Liberally, 3. Take Screenshots for Audit Trail, 4. Handle CAPTCHAs Gracefully, 5. Never Extract Credentials, "Action requires approval but none granted", Approval Integration (+23 more)

### Community 195 - "AgentShroud™ README"
Cohesion: 0.07
Nodes (26): GitHub Pages Deploy Workflow, Acknowledgments, AgentShroud vs Unprotected Agent, Architecture, Control Centers, Core Objectives, Development, Development Resources (+18 more)

### Community 197 - "_make_multipart_body"
Cohesion: 0.05
Nodes (22): _make_multipart_body(), Build a multipart/form-data body with text fields and an optional binary part., Multipart captions must get the full pipeline scan, not just the XML filter.…, process_outbound must run on multipart caption text., Redacted caption replaces the original; binary part stays byte-identical., Pipeline-blocked captions to non-owners are replaced with a safe notice., If the pipeline crashes on a multipart body, non-owner captions are blocked., Owner multipart messages still pass through on pipeline crash (parity). (+14 more)

### Community 198 - "Any"
Cohesion: 0.10
Nodes (13): Any, Validate a credential. Returns: tuple: (is_valid, message), Get detailed status for a credential., Get status for all managed credentials., Calculate overall credential health score., [EXPERIMENTAL] Generate a new credential value. WARNING: This method generates…, Store a new credential in 1Password., Validate a credential using registered validator. (+5 more)

### Community 199 - "Telegram Formatting Rule (bold only, no headers or tables)"
Cohesion: 0.24
Nodes (11): OpenClaw cron: AgentShroud Weekly Summary, Prompt: AgentShroud Daily Check-in, Telegram Formatting Rule (bold only, no headers or tables), Hermes Failure Scenario Catalog (gateway crash, volume corruption, bot disconnect, dependency outage), Prompt: Monthly Chaos Engineering Drill, Restart Backoff Pause (5-minute sleep), gateway-exit-diag.log Restart/Exit Telemetry, Prompt: Weekly Hermes Stability Report (+3 more)

### Community 200 - "_make_cve"
Cohesion: 0.09
Nodes (15): _get_mod(), _make_cve(), Path, _build_heading returns correct H2 text and sentinel markers., When some advisories are under_review the heading is honest, NOT 'all…, _build_table returns correct sentinel markers and unique element ids., generate() rewrites index.html with correct sections for both agents., Write a fake index.html, invoke generate(), return updated HTML. (+7 more)

### Community 201 - "GatewayEmailService"
Cohesion: 0.07
Nodes (17): GatewayEmailService, Protocol, The subset of ``smtplib.SMTP_SSL`` the service uses., Sends owner-comms email over an injectable SMTP transport., Gateway owner-comms email service (SCRUM-77). Consolidates the SMTP transport…, Build the MIME message string (multipart/alternative). For HTML mail the plain…, Send one email synchronously. Blocking — call in an executor. Raises the…, SmtpLike (+9 more)

### Community 202 - "AgentShroud Dev Environment — Raspberry Pi 4 (8GB) Setup Checklist"
Cohesion: 0.04
Nodes (47): Additional Dev Tools, AgentShroud Dev Environment — Raspberry Pi 4 (8GB) Setup Checklist, Bot Account (Manual Setup Required), Bot Account (You Do This Manually), Clone Repo on Pi, Clone Repo on Pi, Cost Estimate, Cost Estimate (+39 more)

### Community 204 - "SubagentMonitor"
Cohesion: 0.07
Nodes (21): Enum, str, SubagentEvent, SubagentEventType, SubagentInfo, SubagentMonitor, SubagentMonitorConfig, ToolCheckResult (+13 more)

### Community 205 - "test_gemini_openai_translator.py"
Cohesion: 0.08
Nodes (44): gemini_failover_unsupported_reason(), gemini_to_openai_request(), gemini_to_openai_response(), _openai_content_to_parts(), openai_to_gemini_request(), openai_to_gemini_response(), _parts_to_text(), Flatten an OpenAI message's content (string or content-block list) to Gemini… (+36 more)

### Community 206 - "test_jira_dev_ticket.py"
Cohesion: 0.05
Nodes (14): _MockTransport, Records requests; serves op-proxy secrets then a scripted Jira response., Tests for the generalized Jira dev-ticket helper (create / comment /…, test_resolve_cloud_id_parses_response(), transport(), test_resolve_cloud_id_raises_on_non_200(), test_resolve_cloud_id_raises_when_field_missing(), test_run_comment_posts_to_correct_issue() (+6 more)

### Community 207 - "TestMultiTurnTracker"
Cohesion: 0.04
Nodes (24): Test detection of tool inventory queries., Test detection of credential-related queries., Test detection of system information queries., Test detection of file reference patterns., Test that scores accumulate across turns., Test threshold-based warning system., Test that sessions get blocked at high scores., Test detection of repeated queries with different phrasing. (+16 more)

### Community 208 - "mock_stream"
Cohesion: 0.06
Nodes (40): _mock_stream_resp(), Build a mock httpx.Response usable as the yield value of a mocked…, _call_agent_stream POSTs to /forward/stream and yields each sentence event as…, Agents with no streaming-compatible chat_path (OpenClaw) get a 400 from the…, A stream that goes straight to 'done' with no sentence events (e.g. everything…, _call_agent_stream must POST to /forward/stream with stream:true, not the old…, SSE keepalive comments (': ...') and blank lines are ignored, not treated as…, A single corrupted SSE line logs a warning and is skipped — it must not abort… (+32 more)

### Community 209 - "SecureBrowser"
Cohesion: 0.07
Nodes (28): main(), Enum, Exception, Validate URL against allowlist/blocklist Security: This is the primary URL…, Check if domain matches pattern (supports wildcards), Classify action risk level Security: Determines if approval is needed, Check if action requires approval Security: Approval queue integration, Log security-related events (+20 more)

### Community 210 - "CI/CD Pipeline Advisor (SKILL)"
Cohesion: 0.07
Nodes (32): Data Validation README, Data Validation (DATA-VAL) Skill, AWS Cloud Management & FinOps (README), AWS Cloud Management & FinOps Agent (SKILL), EBS Performance Analysis Pattern, GSDE&G Team (Global Services Digital Enablement & Governance), Branding Specialist (BS) (README), Brand System Components (Identity/Color/Typography/Voice/Layout/Components) (+24 more)

### Community 211 - "SecurityConfig"
Cohesion: 0.07
Nodes (25): dict, check_monitor_mode_warnings(), get_module_mode(), Security module configuration, Complete security configuration, Return module mode, respecting the global permissive override., Log warnings for any core modules running in monitor mode., SecurityConfig (+17 more)

### Community 212 - "Report Delivery Format Instructions"
Cohesion: 0.10
Nodes (21): AgentShroud Weekly Summary (Hermes Prompt), Collaborator Daily Digest Cron Prompt, Collaborator Report (Evening) Cron Prompt, Collaborator Report - Evening Job, Collaborator Report (Morning) Cron Prompt, Contributor Log Read Path (gateway-data primary, memory fallback), Dual-Surface Report Delivery (Email HTML / Telegram Markdown), Source Verification Policy (+13 more)

### Community 213 - "AgentShroud Docker Configuration"
Cohesion: 0.08
Nodes (29): AgentShroud Docker Configuration, Architecture, Container Runtime Support (SCRUM-92), Container Stack, Core Configuration, Cron Failure Alerting (SCRUM-61), Detection contract, Development (+21 more)

### Community 215 - "AgentShroud™ CVE Mitigation Matrix"
Cohesion: 0.05
Nodes (37): Agent CVE Registry (source of truth), Application CVE Domain (OpenClaw / Hermes), Fresh-DB vs Cached-DB Trivy Verification, Daily GHSA / NVD Registry Sync, Container-Image CVE Domain (our own images), slsa-verifier From-Source Dependency Override, Tier 1 Hand-Curated OpenClaw CVEs, Under Review Is Honest, Not Mitigated (+29 more)

### Community 216 - "ContextGuard"
Cohesion: 0.03
Nodes (49): check_message(), ContextAttack, ContextGuard, ContextSegment, get_context_guard(), Analyze a message for context poisoning attempts. Args: session_id: Session…, Detect instruction injection attempts., Detect repetition-based context stuffing attacks. (+41 more)

### Community 217 - "SecureBrowser"
Cohesion: 0.07
Nodes (28): main(), Enum, Exception, Validate URL against allowlist/blocklist Security: This is the primary URL…, Check if domain matches pattern (supports wildcards), Classify action risk level Security: Determines if approval is needed, Check if action requires approval Security: Approval queue integration, Log security-related events (+20 more)

### Community 218 - "OpenClaw Bot SSH Configuration"
Cohesion: 0.05
Nodes (37): 1. Add Public Key to Target Host, 2. Add Host Configuration (Optional but Recommended), 3. Test Connection, Adding Additional Hosts, Backup and Recovery, Backup SSH Keys, Configured Hosts, 🔐 Credentials in 1Password (+29 more)

### Community 219 - "SecureBrowser"
Cohesion: 0.07
Nodes (28): main(), Enum, Exception, Validate URL against allowlist/blocklist Security: This is the primary URL…, Check if domain matches pattern (supports wildcards), Classify action risk level Security: Determines if approval is needed, Check if action requires approval Security: Approval queue integration, Log security-related events (+20 more)

### Community 220 - "test_clamav_pipeline.py"
Cohesion: 0.05
Nodes (55): clamd_available(), generate_summary(), preferred_scan_binary(), Any, Path, Save a ClamAV report to the log directory., Stream bytes to clamdscan for inline malware scanning. Uses ``clamdscan…, Generate a summary dict suitable for the health report. Args: report: Parsed… (+47 more)

### Community 221 - "BrowserSecurityGuard"
Cohesion: 0.06
Nodes (14): BrowserSecurityGuard, CredentialEntryBlocked, Exception, IntEnum, Browser Security Module - Detects social engineering in web content. Provides…, ThreatAssessment, ThreatLevel, guard() (+6 more)

### Community 222 - "test_session_manager.py"
Cohesion: 0.05
Nodes (19): Represents an isolated session for a user within a specific bot workspace. Each…, Create session from dictionary., UserSession, mgr(), fixture, History should be capped at 1000 messages., Create a UserSessionManager with a temp base workspace and an owner., Re-anchoring prepends a security notice to the system prompt. (+11 more)

### Community 223 - "SecureBrowser"
Cohesion: 0.07
Nodes (28): main(), Enum, Exception, Validate URL against allowlist/blocklist Security: This is the primary URL…, Check if domain matches pattern (supports wildcards), Classify action risk level Security: Determines if approval is needed, Check if action requires approval Security: Approval queue integration, Log security-related events (+20 more)

### Community 224 - "ProxyDashboard"
Cohesion: 0.06
Nodes (32): ProxyDashboard, ProxyStatusReport, Complete proxy status report for the dashboard., Return human-readable dashboard strings., Collects status from all security components and generates reports., Dashboard should track uptime., Dashboard display should include all required fields., ProxyStatusReport.to_display should produce readable strings. (+24 more)

### Community 225 - "AppleContainerEngine"
Cohesion: 0.04
Nodes (24): ABC, AppleContainerEngine, Any, Container engine backed by Apple's `container` CLI., ContainerEngine, ContainerInfo, Any, CompletedProcess (+16 more)

### Community 226 - "TestNormalizeForSpeech"
Cohesion: 0.08
Nodes (7): Unit tests for voice_gateway.tts.normalize_for_speech., Reproduces the exact log pattern: http://gateway:[PORT], 🔒 [REDACTED: Credentials cannot be displayed via Telegram], [1], [possible], [note] — not uppercase-only, must not be touched., If a secret somehow reaches normalise (shouldn't — pipeline redacted it), the…, Reproduces the 2026-06-27 12:38 agent reply that triggered SCRUM-46., TestNormalizeForSpeech

### Community 227 - "check-vendor-compat.sh"
Cohesion: 0.07
Nodes (33): Wazuh-Agent Sidecar Split (SIDECAR-GAP-001 resolution), Sunday Upgrade Report 2026-08-30 (07:34 first-pass abort), Sunday Upgrade Report 2026-08-30 (local-llms upgrade requested), Sunday Upgrade Report 2026-08-30 (final), Sunday Upgrade Report 2026-09-06 (dev-only scoped run), Sunday Upgrade Report 2026-09-06 (dev-only, duplicate), Sunday Upgrade Report 2026-09-14 (dev account), 0. What happened before this session (reconstructed from git + JSON, not narrated) (+25 more)

### Community 228 - "test_playback_state.c (host-native unit tests, SCRUM-59)"
Cohesion: 0.67
Nodes (3): playback_logic.h (pure END-gate/resume math, extracted for host testing), stubs/audio.h (host-test stub replacing audio.h constants), test_playback_state.c (host-native unit tests, SCRUM-59)

### Community 229 - "lifespan"
Cohesion: 0.07
Nodes (21): _build_per_bot_telegram_tokens(), _DropInvalidHTTPRequestFilter, _install_uvicorn_warning_filter(), lifespan(), _op_authenticate(), _prewarm_op(), _run_hermes_api_forwarder(), _handle() (+13 more)

### Community 230 - "test_mcp_proxy.py"
Cohesion: 0.04
Nodes (37): AgentShroud Proxy — security pipeline for all OpenClaw traffic., FindingType, InspectionFinding, InspectionResult, MCPInspector, Any, Enum, Return the highest threat level from all findings. (+29 more)

### Community 231 - "Step-by-Step Deployment"
Cohesion: 0.05
Nodes (42): 1Password Integration (Optional), AgentShroud Deployment Procedure, Container Won't Start, Database Connection Issues, Deployment Modes, Functional Testing, Grafana Dashboard Configuration, Maintenance Procedures (+34 more)

### Community 232 - "_make_report"
Cohesion: 0.08
Nodes (19): format_cve_report(), Format a Trivy scan result into a Telegram-ready Markdown message. Args:…, _make_report(), The daily fs scan of / must exclude /var/log/security (trivy's own cache +…, Pin _running_image to the docker-unavailable fallback (same as…, run_and_send_cve_report calls run_trivy_scan with scan_type='image' for each…, Message sent via Telegram includes a Container Image Scans section., Return value includes image_scans list. (+11 more)

### Community 233 - "OutputCanary"
Cohesion: 0.04
Nodes (35): CanaryConfig, CanaryResult, OutputCanary, Any, Pattern, Create an invisible version of the canary using various techniques. Args:…, Create regex patterns to detect the canary in responses. Args: base_canary:…, Check if response contains the session's canary (prompt leakage detected).… (+27 more)

### Community 234 - "SecureBrowser Skill"
Cohesion: 0.05
Nodes (42): 1. Verify Installation, 2. Configure Allowlist, 3. Test Navigation, "Approval required but none granted", Approval Workflow, Audit Trail, "Browser timeout", "CAPTCHA detected" (+34 more)

### Community 235 - "Development Workflow: Read-Only Filesystem Strategy"
Cohesion: 0.05
Nodes (41): 1. What Needs to WRITE?, 2. What Needs to PERSIST?, 3. What's System-Level?, Current Configuration Status, Current Features: Write Requirements, Current Recommendation, Currently Documented, Development Mode Script (+33 more)

### Community 236 - "ADR-006: Multi-Runtime Container Support"
Cohesion: 0.07
Nodes (31): Cisco AnyConnect VPN Networking Fix (col0 vmnet route), Colima (primary macOS runtime), 1. Pre-cache the Lima disk image, 2. Start Colima, 3. Apply the VPN networking fix, 4. Verify, ADR-006: Multi-Runtime Container Support, Cisco AnyConnect VPN Networking Fix (+23 more)

### Community 237 - "What Does OpenClaw Actually Need to Write?"
Cohesion: 0.06
Nodes (33): 1. Skills Installation (`.openclaw/skills/`), 2. Conversation Memory (`.openclaw/MEMORY.md`), 3. Workspace Files (`workspace/`), 4. npm Cache (`.npm/`, `.cache/`), 5. Temporary Files (`/tmp/`), 6. Session Configuration (`.config/`, `.local/`), Answer to Your Question, Bind Mount vs Docker Volume (+25 more)

### Community 239 - "MetadataGuard"
Cohesion: 0.06
Nodes (18): t_metadata(), DocumentTag, MetadataGuard, Sanitize filename by removing unicode control characters and normalizing., Check if binary data contains EXIF metadata., Remove EXIF metadata from image data if present., Create and store a provenance tag for a document., Look up a document tag by its SHA-256 content hash. (+10 more)

### Community 241 - "ConfigIntegrityMonitor"
Cohesion: 0.10
Nodes (29): ConfigIntegrityMonitor, Path, Accept current file hashes as the new baseline (owner-acknowledged rebuild)., Format Telegram alert text for detected config changes., Computes and verifies SHA256 hashes of monitored bot config files. At gateway…, Config Integrity Monitor — detects tampering with bot configuration files.…, Return hex SHA256 of a file, or None if the file does not exist., Load the last known baseline from disk. Returns empty dict if not found. (+21 more)

### Community 242 - "SharedMemoryManager"
Cohesion: 0.07
Nodes (18): Return True if user_id is the system owner (oversight override)., Return member IDs of a group, or empty list if no teams config., Check if user is the owner (any platform)., Append a timestamped entry to the group shared memory file. Authorization…, Read raw private memory for a user. Args: user_id: The user whose memory to…, Append content to user's private memory file. Authorization (RT-5, WS-E HIGH):…, Build merged memory context for bot prompt injection. Includes: 1. User's own…, Return memory from groups whose focus_topics match the query text. For… (+10 more)

### Community 243 - "RateLimitGuard"
Cohesion: 0.09
Nodes (31): RateLimitConfig, RateLimitDecision, RateLimitGuard, Record one request for (agent_id, tool) and decide allow/block. Fail-closed: on…, Configuration for :class:`RateLimitGuard`. All windows are per (agent_id, tool)…, Structured verdict returned by :meth:`RateLimitGuard.check`., Adaptive per-agent / per-tool sliding-window rate limiter with burst detection., clock() (+23 more)

### Community 244 - "asyncio"
Cohesion: 0.06
Nodes (25): asyncio, Tamper detection at various chain positions., Can retrieve specific entry by ID for verification., Looking up nonexistent entry returns None., Deleted entry is gone (right to erasure)., Deleting nonexistent entry returns False., Export chain and re-verify., Paginated queries return correct subsets. (+17 more)

### Community 245 - "test_benchmark_regression.py"
Cohesion: 0.07
Nodes (26): assert_within_threshold(), load_baseline(), percentile(), fixture, Benchmark regression tests — ensure latency stays within 20% of baseline., Time each of N iterations; return mean/p50/p99 in ms., Single inbound request processing should stay within baseline., Single outbound request processing should stay within baseline. (+18 more)

### Community 246 - "Mac App Discovery Skill"
Cohesion: 0.07
Nodes (31): Error Handling, Future Extensions (for collaborative sharing), Mac App Discovery Skill, Performance Notes, When to Use This Skill, 10. Spotlight Catch-All, 1. System Profiler (most comprehensive single source), 2. Applications Folders (catch drag-and-drop installs) (+23 more)

### Community 247 - "S8 no raw ssh/agentshroud-bot@/real Tailscale FQDN in baked bot config"
Cohesion: 0.50
Nodes (4): OpenClaw Cron Jobs Configuration, S10 start-agentshroud.sh force-reconciles security-critical live cron jobs, S8 no raw ssh/agentshroud-bot@/real Tailscale FQDN in baked bot config, S9 init-openclaw-config.sh seeds agentshroud-ssh-exec.sh rules into live AGENTS.md

### Community 249 - "AgentShroud Documentation"
Cohesion: 0.06
Nodes (32): Active Protections, AgentShroud Documentation, [architecture/](./architecture/) - Architecture & Planning, 🗂️ Archive, Bot Development Team (Future), 📝 Contributing, 📋 Current Status, [deploy/](./deploy/) - Deployment Guides (+24 more)

### Community 250 - "PodmanEngine"
Cohesion: 0.12
Nodes (5): PodmanEngine, Any, Generate a systemd unit file for a container., Container engine backed by the Podman CLI., Detect podman compose or podman-compose.

### Community 251 - "_sleep"
Cohesion: 0.06
Nodes (13): First iteration ingests + records; second sees dedup and skips., If already ingested today, the loop bumps to tomorrow and never ingests., A raised per-agent check error is ISOLATED — the ingest still completes. Per-…, _already_ingested_ghsa_today returns False on a malformed sentinel., After sleeping, if the day is now marked done, the loop skips ingest., A disk-write failure on the sentinel is swallowed; in-memory guard set., Nothing to deliver is a legitimate 'done', not a failure to retry., TestGhsaIngestScheduler (+5 more)

### Community 252 - "TestPathIsolationManager"
Cohesion: 0.05
Nodes (23): fixture, patch, Test user session registration., Test ending user session., Test path rewriting for /tmp files., Test path rewriting for nested /tmp paths., Test paths that don't need rewriting., Test blocking direct access to base agentshroud directory. (+15 more)

### Community 253 - ".test_collaborator_web_access_imperative_with_url_queues_owner_approval"
Cohesion: 0.05
Nodes (13): Collaborator URL web-access prompts should queue owner approval and return…, Web access intent without explicit URL should remain restricted and not queue…, Domain-only web intent should queue owner approval and pending notice., Conceptual egress-policy questions should get safe info, not hard block., Conceptual policy questions that mention a URL should not be treated as fetch…, URL policy questions without collaborator keyword should still remain…, Bare-domain policy questions should be informational, not treated as web…, Imperative URL requests should queue owner approval and not expose command… (+5 more)

### Community 254 - "ingest_api/config.py"
Cohesion: 0.02
Nodes (167): ApprovalQueue, WebSocket, # NOTE: Called within _lock context, In-memory approval queue with WebSocket notifications Actions requiring…, Accept a WebSocket connection and add to connected set Args: websocket:…, Remove a WebSocket connection from connected set Args: websocket: WebSocket…, Initialize approval queue Args: config: Approval queue configuration mfa_guard:…, Load queue items from store file when present. (+159 more)

### Community 255 - "The 8D Investigation Process"
Cohesion: 0.06
Nodes (31): 8D Root Cause Analysis — Data-Driven Control System Investigation, Agent Interaction Protocol, Architecture Context, Confidence Scoring, Critical Rules, D0 — Planning & Scoping, D1 — Team & Expertise Identification, D2 — Problem Description (Data Collection & Characterization) (+23 more)

### Community 256 - "AWS Cloud Management & FinOps Agent"
Cohesion: 0.06
Nodes (31): AWS Cloud Management & FinOps Agent, Cost Optimization Priority, Cross-Account & Future Proofing, Decision Framework, Deliverables, EBS Performance Analysis (Critical Pattern), Expertise, FY26 Cost Reduction Context (+23 more)

### Community 257 - "The 8D Investigation Process"
Cohesion: 0.06
Nodes (31): 8D Root Cause Analysis — Data-Driven Control System Investigation, Agent Interaction Protocol, Architecture Context, Confidence Scoring, Critical Rules, D0 — Planning & Scoping, D1 — Team & Expertise Identification, D2 — Problem Description (Data Collection & Characterization) (+23 more)

### Community 258 - "AgentShroud Phase 3 - Quick Start Guide"
Cohesion: 0.06
Nodes (31): 1. Health Check (Gateway), 2. Get Auth Token (Gateway), 3. Send Test Message, 4. Verify Isaiah's Personality, AgentShroud Phase 3 - Quick Start Guide, API Key Error, Architecture Diagram, Check File Permissions (+23 more)

### Community 259 - "AgentShroud Audit Specification"
Cohesion: 0.05
Nodes (40): 1. Authentication Events (AUTH), 2. Authorization Events (AUTHZ), 3. Security Events (SEC), 4. Data Events (DATA), 5. System Events (SYS), A.12.4 Logging and Monitoring, Advanced Search Query, AgentShroud Audit Specification (+32 more)

### Community 260 - "get_wazuh_summary"
Cohesion: 0.07
Nodes (28): Return recent Wazuh HIDS alerts with FIM and rootkit summary., wazuh_alerts(), get_falco_summary(), get_wazuh_summary(), _is_falco_running(), _is_wazuh_agent_running(), Return True if a non-zombie falco process is running inside this container., Return True if wazuh-agentd is running as a local process inside this container. (+20 more)

### Community 263 - "_make_filter"
Cohesion: 0.07
Nodes (17): _make_filter(), IP allowlist and private-IP SSRF protection., CIDR in policy allowlist should match., Private IPs are blocked by default to prevent SSRF., Private IPs pass if explicitly in the EgressPolicy allowlist (SSRF check)., EgressFilter correctly parses URLs, host:port, and bare hostnames., EgressFilter records attempts and provides stats., Create an EgressFilter with a simple config. (+9 more)

### Community 264 - "Skill: UX Expert (UX)"
Cohesion: 0.06
Nodes (30): Alert Prioritization Display, Anti-Patterns to Flag, CLI / TUI UX, CLI UX Rules, Confirmation Patterns, Content Organization Patterns, Contextual Actions, Core Discipline: Discover → Define → Design → Validate (+22 more)

### Community 265 - "migrate-cve-registry-ghsa.py"
Cohesion: 0.12
Nodes (28): Counter, _advisory_text_tokens(), build_id_plan(), compute_stats(), fetch_advisories(), gather_advisories(), load_registry(), load_snapshot() (+20 more)

### Community 266 - "REQUIRED NOTES — PRODUCE EVERY ONE OF THESE"
Cohesion: 0.06
Nodes (30): `00 - START HERE/Home.md`, `00 - START HERE/Quick Reference.md`, `00 - START HERE/System Overview.md`, `01 - Architecture/Architecture Overview.md`, `01 - Architecture/Data Flow.md`, `01 - Architecture/Shutdown & Recovery.md`, `01 - Architecture/Startup Sequence.md`, `02 - Modules/[FileName].md` — ONE PER SOURCE FILE (+22 more)

### Community 267 - "Skill: UX Expert (UX)"
Cohesion: 0.06
Nodes (30): Alert Prioritization Display, Anti-Patterns to Flag, CLI / TUI UX, CLI UX Rules, Confirmation Patterns, Content Organization Patterns, Contextual Actions, Core Discipline: Discover → Define → Design → Validate (+22 more)

### Community 268 - "TestPIIDetection"
Cohesion: 0.07
Nodes (22): asyncio, Visa card: 4111-1111-1111-1111., Card without dashes: 4111111111111111., Amex card: 378282246310005 (15 digits starting with 37)., Multiple PII entities in one message., PII embedded in JSON., PII in code/markdown blocks., Dates should not be flagged as SSN/phone. (+14 more)

### Community 269 - "Security Architecture"
Cohesion: 0.05
Nodes (39): Application Security, Audit Logging, Best Practices, Build Process Security, Container Logs, Container Security Layers, Core Security Principle, Health Monitoring (+31 more)

### Community 270 - "CREDENTIAL-PROTECTION-IMPLEMENTED.md"
Cohesion: 0.09
Nodes (32): Credential Access Audit Logging (Layer 3), Console Access Only (Layer 2), Gateway Credential Filter (Layer 1), 🎓 Configuration, 📚 Created Documentation, Credential Protection - Implementation Complete ✅, 🔍 How It Works Internally, 🔐 How to Access Credentials Securely (+24 more)

### Community 271 - "AgentShroud Access Control Matrix"
Cohesion: 0.05
Nodes (39): Admin (admin), Administrative Roles, Agent Management, Agent Operational Permissions, Agent Trust Levels, AgentShroud Access Control Matrix, Approval Queue Management, Automatic Progression Criteria (+31 more)

### Community 272 - "CanaryTripwire"
Cohesion: 0.08
Nodes (8): CanaryConfig, CanaryResult, CanaryTripwire, Pipeline-compatible bridge: scan response text and return TripwireResponse., Bridge result returned by scan_response() for pipeline compatibility., Register a new canary value at runtime for dynamic tripwire testing., TripwireResponse, TestCanaryTripwire

### Community 273 - "DataExfilVolumeGuard"
Cohesion: 0.10
Nodes (33): DataExfilVolumeConfig, DataExfilVolumeGuard, Observe one outbound response and decide allow/block. A blocked response is NOT…, Clear cumulative + baseline state for a session (e.g. on new session)., Configuration for :class:`DataExfilVolumeGuard`., Structured verdict returned by :meth:`DataExfilVolumeGuard.observe`., Cumulative + adaptive outbound-volume anomaly detector, per session., _SessionState (+25 more)

### Community 274 - "SkillGuard"
Cohesion: 0.12
Nodes (14): Scan skill / MCP / agent-definition payloads for supply-chain risk. Usage::…, Ordered severity ladder (``IntEnum`` so comparisons work)., Severity, SkillGuard, _finding_categories(), TestCleanSkill, TestExecOfDownload, TestExfiltration (+6 more)

### Community 275 - "Job details"
Cohesion: 0.07
Nodes (30): AgentShroud Daily Check-in, AgentShroud Weekly Summary, Daily Component Health Digest, Daily Memory Journal, Email: Chat Front-Ends & Search Infra, Email: Coding-Agent CLIs, Email: Local Inference Engines, Email: Mac Clustering (+22 more)

### Community 276 - "Browser — Secure Browser Automation"
Cohesion: 0.07
Nodes (29): 1. Always Specify Risk Level, 2. Use Allowlisting Liberally, 3. Take Screenshots for Audit Trail, 4. Handle CAPTCHAs Gracefully, 5. Never Extract Credentials, "Action requires approval but none granted", Approval Integration, Audit Logging (+21 more)

### Community 277 - "Browser — Secure Browser Automation"
Cohesion: 0.07
Nodes (29): 1. Always Specify Risk Level, 2. Use Allowlisting Liberally, 3. Take Screenshots for Audit Trail, 4. Handle CAPTCHAs Gracefully, 5. Never Extract Credentials, "Action requires approval but none granted", Approval Integration, Audit Logging (+21 more)

### Community 278 - "TestEgressTelegramNotify"
Cohesion: 0.07
Nodes (21): asyncio, fixture, Test handling deny callback., Test handling invalid callback data., Test Telegram egress notification system., Test callback for non-existent request., Test cleanup removes expired pending requests., Test answering callback query. (+13 more)

### Community 279 - "_w"
Cohesion: 0.07
Nodes (11): Write a file under the sandbox root, creating parents., TestDaemonConfigReader, TestDockerDaemonConfig, TestImageSigningProvenance, TestMandatoryGates, TestNetworkSegmentation, TestOpenscapSummary, TestProcScans (+3 more)

### Community 280 - "AgentShroud Weekly Upgrade — 2026-09-22 (DEV run, account: agentshroud-bot)"
Cohesion: 0.06
Nodes (32): 0. Identity, timeline, and prior-run continuity (discovered, not assumed), 10. Time spent (03:00 run), 11.1 Duplicate/zombie-session forensics, 11.2 State inherited from the 03:00 run (re-verified, not assumed), 11.3 Attempt to deploy (`sunday-upgrade-apply.sh --env dev --phase all`), 11.4 Prune sequence failed — same socket death, now under prune load not build load, 11.5 Recovery — confirmed dev left healthy, not upgraded, 11. CONTINUATION RUN — started 08:00 ET, account agentshroud-bot (+24 more)

### Community 281 - "test_skill_guard.py"
Cohesion: 0.13
Nodes (15): guard(), CompletedProcess, fixture, Path, TestClient, Exercise ``gateway.skills.scan.main`` directly for exit-code coverage., Tests for SkillGuard — skill supply-chain scanning (SCRUM-97). Coverage: -…, The parallel bash sync path must invoke SkillGuard before copying. (+7 more)

### Community 283 - "Goal: Codex is a secondary/tertiary agent used for test augmentation, validation, and safe refactors AFTER tests pass."
Cohesion: 0.20
Nodes (10): 0) PRIME DIRECTIVE (CODEX ROLE - NON-NEGOTIABLE), 10) MCP SERVERS (EXTERNAL INTEGRATIONS), 3) DEFINITION OF DONE (DoD), 5) ENVIRONMENT SETUP, 6) SECURITY & SAFETY REQUIREMENTS, 9) CONFIGURATION FILES, Conda Environment, Goal: Codex is a secondary/tertiary agent used for test augmentation, validation, and safe refactors AFTER tests pass. (+2 more)

### Community 284 - "AgentShroud Device Pairing Management"
Cohesion: 0.07
Nodes (30): 1. Regular Audits, 2. Principle of Least Privilege, 3. Monitor Remote IPs, 4. Document Your Devices, 5. Rotate on Compromise, AgentShroud Device Pairing Management, Approve All Pending Requests, Approving Device Pairing Requests (+22 more)

### Community 285 - "sunday-scan.sh"
Cohesion: 0.08
Nodes (32): die(), err(), log(), sunday-scan.sh script, sunday_build_revision(), sunday_catchup_pending(), _sunday_commit(), _sunday_date_minus() (+24 more)

### Community 286 - "AgentShroud v0.9.0 — Human Interface Testing Guide"
Cohesion: 0.07
Nodes (29): 1. SOC Command Center (Web UI), 2. Telegram Command Testing, 3. Collaborator Experience Testing, 4. Shared Memory Testing, 5. Log Monitoring, 6. Security Scan, 7. Pre-Merge Checklist, Access and Login (+21 more)

### Community 287 - "prompt_guard.py"
Cohesion: 0.06
Nodes (14): PatternRule, Enum, str, Prompt Injection Defense — detect and block prompt injection attempts. Scoring…, HMAC-SHA256 fingerprint for a registered system prompt., Args: block_threshold: Score at or above which input is blocked.…, SystemPromptFingerprint, ThreatAction (+6 more)

### Community 288 - "10. Troubleshooting"
Cohesion: 0.09
Nodes (27): Atlassian: "OAuth flow failed", AWS: "Token expired" (SSO), AWS: "Unable to locate credentials", GitHub: "Bad credentials", GitHub: "Docker image not found", Troubleshooting, Authentication Issues, Common Errors (+19 more)

### Community 289 - "Local-Model Job Quality Matrix"
Cohesion: 0.07
Nodes (32): Env-split note (prod FYI, for init-config.sh work), Failure classes (prod investigation handover, 2026-08-31), Job Quality Matrix — local-model report/newsletter jobs (Mission 1), Per-job verdicts, Related delivery-layer defects (separate from model quality), Hard-Fail Rather Than Deliver an Empty Shell, Failure Class: Local Model Call Hangs, Local-Model Job Quality Matrix (+24 more)

### Community 290 - "start.sh"
Cohesion: 0.09
Nodes (29): Duplicate/overlapping Hermes cron jobs colliding at same minute — retired duplicate, Hermes cron garbled output — nemotron exhausted budget on monologue; pinned to gemma-4-26b-a4b-it, qwen3-coder silently routed to LM Studio instead of oMLX — generic prefix matched first, v1.5.2 Release — local-model routing and cron reliability, First-boot gateway-default s6 service auto-start, _hermes_cron_ids_names(), MCP servers reconciliation from mcp/servers.json into config.yaml, Env-split cron reconciliation (AGENTSHROUD_PROD_CRON_KEEP) (+21 more)

### Community 291 - "graphify reference: extra exports and benchmark"
Cohesion: 0.08
Nodes (20): For /graphify add, For --watch, graphify reference: add a URL and watch a folder, graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag) (+12 more)

### Community 292 - "Skills by Category"
Cohesion: 0.07
Nodes (28): 1. Branch Creation, 2. Development (TDD), 3. Production Testing (if needed), 4. Pull Request, 5. Pre-Merge, Cloud & FinOps, Common Commands Quick Reference, Content & Communication (+20 more)

### Community 293 - "graphify reference: extra exports and benchmark"
Cohesion: 0.07
Nodes (23): For /graphify add, For --watch, graphify reference: add a URL and watch a folder, graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag) (+15 more)

### Community 294 - "Skills by Category"
Cohesion: 0.07
Nodes (28): 1. Branch Creation, 2. Development (TDD), 3. Production Testing (if needed), 4. Pull Request, 5. Pre-Merge, Cloud & FinOps, Common Commands Quick Reference, Content & Communication (+20 more)

### Community 296 - "test_scorecard_integrity.py"
Cohesion: 0.09
Nodes (23): Score domain 6: Malware Defense (0-5). 1=module installed or not_run, 3=clamd…, Score domain 2: Vulnerability Management (0-5). 1=module installed but no…, _score_malware_defense(), _score_vulnerability_management(), TestScoreMalwareDefense, TestScoreVulnerabilityManagement, _clean_clamav(), _clean_trivy() (+15 more)

### Community 297 - "asyncio"
Cohesion: 0.06
Nodes (26): asyncio, Dashboard should set httpOnly cookie and redirect to clean URL, GET /dashboard?token=valid sets cookie and redirects to /dashboard, GET /dashboard with valid cookie serves HTML, GET /dashboard with invalid cookie returns 403, GET /dashboard with no auth returns 403, GET /dashboard?token=wrong returns 403, Dashboard ws-token endpoint returns token only for cookie-authed sessions (+18 more)

### Community 298 - "_run_4b"
Cohesion: 0.13
Nodes (10): _all(), Path, wazuh-manager daemon watchdog (docker/wazuh/services.d/wazuh-watchdog/run). The…, _run(), _run_4b(), _step_4b(), TestHealthCheckWazuhStep, TestWatchdogBehaviour (+2 more)

### Community 299 - "TestWebProxySecurityIntegration"
Cohesion: 0.08
Nodes (22): MockDNSVerdict, MockEgressChannel, MockEgressEvent, MockThreatLevel, MockURLResult, Enum, Test that DNS filter blocks suspicious domains., Test that DNS filter flags questionable domains but allows them through. (+14 more)

### Community 300 - "_t"
Cohesion: 0.09
Nodes (10): _startup_scanner(), parametrize, Regression guard for the 2026-07-29 staleness incident. RUNNING_VERSION was…, Tests for scripts/triage-cve-mitigations.py — Phase 2 mitigation-triage engine.…, _t(), TestClassify, TestConsumeFieldEdge, TestDriverIsolation (+2 more)

### Community 301 - "Security Module Inventory"
Cohesion: 0.07
Nodes (29): 10. AppArmor/SELinux Policies, 11. Linux Capability Dropping, 12. User Namespace Isolation, 13. Container Runtime Security, 14. Process Monitor, 15. File System Guard, 16. Resource Guard, 17. API Key Manager (+21 more)

### Community 302 - "test_module_stats.py"
Cohesion: 0.10
Nodes (24): Decision, get_collector(), ModuleStatsCollector, Enum, str, Thread-safe per-module allow/block/sanitize counters., Live per-module enforcement counters (SCRUM-80). Feeds the SOC dashboard's per-…, Record one enforcement decision for ``module``. Never raises: an… (+16 more)

### Community 303 - "TestMultilingualInjection"
Cohesion: 0.05
Nodes (20): Test Dutch injection detection., Set up PromptGuard with standard thresholds., Test Ukrainian injection detection (Tier 2)., Test Persian/Farsi injection detection (Tier 2)., Test Bengali injection detection (Tier 2)., Test Japanese injection detection., Test Tamil injection detection (Tier 2)., Test Tagalog injection detection (Tier 2). (+12 more)

### Community 304 - "TestPromptProtection"
Cohesion: 0.05
Nodes (20): Test redaction of targeted infrastructure details. Generic hostnames (e.g.…, Product name 'agentshroud' and 'agentshroud-openclaw' are public branding —…, Test that dynamically registered bot hostnames are redacted., Test redaction of user ID patterns., Test redaction of credential patterns., Test that normal content passes through without redaction., Test adding protected content., Test fuzzy matching against protected content. (+12 more)

### Community 305 - "GroupRoleResolver"
Cohesion: 0.08
Nodes (12): GroupRoleResolver, Return True if user_id is the owner in group_chat_id., Return True if user_id is at least a member (member or owner)., Return True if the tool is classified as high-risk. High-risk tools require…, Remove a user's role entry from a group (falls back to READ_ONLY)., Resolve per-group roles for Telegram group workspace members. Args:…, Return the GroupRole for user_id in group_chat_id. Returns GroupRole.READ_ONLY…, Test GroupRole.rank, can_use_high_risk, and GroupRoleResolver helpers. (+4 more)

### Community 306 - "ProgressiveLockdown"
Cohesion: 0.09
Nodes (10): ProgressiveLockdown, Tracks per-principal block counts and returns escalation actions. Thread-safe:…, Args: decay_window_seconds: When set, only blocks recorded within this many…, Return current lockdown state for a principal (for /collabs or owner…, Owner command: reset lockdown state for a principal. Returns True if existed., Return lockdown status for all tracked principals., TestConcurrency, TestEscalateTo (+2 more)

### Community 307 - "A2APeerTestDouble"
Cohesion: 0.25
Nodes (6): A2APeerTestDouble, fixture, Request, Response, Minimal JSON-RPC 2.0 responder standing in for a real A2A peer. Explicitly NOT…, test_double_peer()

### Community 308 - "Skill: MCP AWS Profile Configuration (MCPM-AWS-PROFILE)"
Cohesion: 0.06
Nodes (35): "Access Denied", AWS Profile Basics, AWS SSO Configuration, Best Practices, Check Current Profile, Configuration Files, Configure New Profile, Default Profile vs Named Profiles (+27 more)

### Community 309 - "test_collaborator_tracker.py"
Cohesion: 0.06
Nodes (14): log_file(), fixture, Unit tests for CollaboratorActivityTracker., record_activity with bot_id='hermes' stores bot_id in the entry., record_activity without bot_id stores bot_id=None in the entry., get_activity_summary returns a by_bot breakdown keyed by bot_id., Real Telegram UIDs (9-10 digits) must NOT be pruned., Owner messages are now recorded with is_owner=True (not silently dropped). (+6 more)

### Community 310 - "classify"
Cohesion: 0.31
Nodes (8): OpenClaw isHeartbeatContentEffectivelyEmpty benign skip, _is_benign_skip, classify(), _is_benign_skip(), main(), Any, Return (soaked, message) for the given cron job list. soaked=True only if at…, Classification logic for scripts/check-soak-status.sh. Separated from the shell…

### Community 311 - "get_trivy_image_summaries"
Cohesion: 0.18
Nodes (13): get_trivy_image_summaries(), Return per-image Trivy scan summaries from saved image reports. Reads reports…, _clean_trivy_report(), _critical_trivy_report(), Path, Write a fake image report file in the expected filename format., Files named trivy-*.json (fs scans) are not included., bot_id + config param restricts results to that bot's image. (+5 more)

### Community 312 - "GitGuard"
Cohesion: 0.08
Nodes (25): GitGuard, Enum, Path, str, Scan arbitrary text content for malicious git/supply-chain patterns. This is…, Scan a git repository for malicious hooks and scripts. Args: repo_path: Path to…, Scan git hooks directory for malicious content., Scan package.json for suspicious install scripts. (+17 more)

### Community 313 - "Skill: Mindmap Architect (MM)"
Cohesion: 0.07
Nodes (26): Anti-Patterns to Flag, Brainstorming Session Map, Core Discipline: Frame → Structure → Generate → Validate, Curriculum Design (with `/i-atlas`), Decision Tree Map, Dependencies, Example: FODL Pipeline Overview, Export and Sharing Conventions (+18 more)

### Community 314 - "Skill: UI Expert (UI)"
Cohesion: 0.07
Nodes (26): Accessibility Requirements, Anti-Patterns to Flag, BEM (Block Element Modifier), Breakpoints (mobile-first), Button, Component contract rules, Component file structure, Component Patterns (+18 more)

### Community 315 - "Mode A — Single task"
Cohesion: 0.07
Nodes (26): Guardrails, Invocation, Jira ticket — every development batch gets one, Mode A — Single task, Mode B — Comprehensive review sweep, Reviewers and fixer available to you, Role, Skill: Hermes Dev Workflow (HDEV) (+18 more)

### Community 316 - "iCloud Services"
Cohesion: 0.07
Nodes (26): "401 Unauthorized", Add Contact, "Calendar/Contacts not found", Calendar Operations, Configuration, "Connection timeout", Contact Operations, Create Event (+18 more)

### Community 317 - "TestProductionCompose"
Cohesion: 0.06
Nodes (15): _load_compose(), _load_compose_raw(), fixture, parametrize, Validate docker/docker-compose.yml (main compose)., All compose files should be valid YAML., Load a docker-compose YAML file., Load raw text of a compose file. (+7 more)

### Community 318 - "Skill: Mindmap Architect (MM)"
Cohesion: 0.07
Nodes (26): Anti-Patterns to Flag, Brainstorming Session Map, Core Discipline: Frame → Structure → Generate → Validate, Curriculum Design (with `/i-atlas`), Decision Tree Map, Dependencies, Example: FODL Pipeline Overview, Export and Sharing Conventions (+18 more)

### Community 319 - "test_env_guard_class.py"
Cohesion: 0.05
Nodes (9): guard(), fixture, Behavior tests for the EnvironmentGuard class (gateway/security/env_guard.py).…, TestCheckCommandExecution, TestCheckFileAccess, TestLooksLikeCredential, TestMonitorEnvironmentAccess, TestScrubCommandOutput (+1 more)

### Community 320 - "Skill: UI Expert (UI)"
Cohesion: 0.07
Nodes (26): Accessibility Requirements, Anti-Patterns to Flag, BEM (Block Element Modifier), Breakpoints (mobile-first), Button, Component contract rules, Component file structure, Component Patterns (+18 more)

### Community 321 - "iCloud Services"
Cohesion: 0.07
Nodes (26): "401 Unauthorized", Add Contact, "Calendar/Contacts not found", Calendar Operations, Configuration, "Connection timeout", Contact Operations, Create Event (+18 more)

### Community 322 - "test_forward_routing.py"
Cohesion: 0.08
Nodes (20): _BlockedOutboundPipeline, _make_mock_app_state(), _PipelineCaptor, Pipeline receives 'openclaw' as agent_id when routed to openclaw., Pipeline receives 'hermes' as agent_id when routed to hermes., Regression: 'default' must never appear in agent_id when a named target is…, process_inbound must receive metadata={'user_id': ...} from /forward so that…, Minimal pipeline mock that records which agent_id it was called with. (+12 more)

### Community 323 - "Skill: MCP AWS Profile Configuration (MCPM-AWS-PROFILE)"
Cohesion: 0.06
Nodes (35): "Access Denied", AWS Profile Basics, AWS SSO Configuration, Best Practices, Check Current Profile, Configuration Files, Configure New Profile, Default Profile vs Named Profiles (+27 more)

### Community 324 - "Slack Channel Setup"
Cohesion: 0.14
Nodes (13): Architecture, Sending Messages to the Bot, Slack Channel Setup, Step 10: Verify, Step 1: Create a Slack App, Step 2: Enable Socket Mode, Step 3: Add Bot Token Scopes, Step 4: Enable Event Subscriptions (+5 more)

### Community 326 - "Incident → Test Backfill Rule (R3 extension): every postmortem must add a regression test in the same PR as the fix, not deferred"
Cohesion: 0.09
Nodes (26): GitHub Branch Protection — main (docs/governance/BRANCH_PROTECTION.md), Local PreToolUse hook block_main_commits.sh (blocks commit/push/merge on main before GitHub is reached), Required status checks: test, lint, smoke-static, Monthly Chaos Drill cron job (1st of month, 9:00 AM ET), Sprint Cadence Decision (docs/governance/SPRINT_CADENCE.md), GSD (Get Shit Done) cadence — adopted in place of formal Scrum/SAFe sprints, GSD issue required before branching on gateway/security, docker/, secrets, hooks (production gating), Rationale: formal sprint ceremonies add overhead without proportional value for a solo developer + AI agents team (+18 more)

### Community 327 - "AgentShroud User Guide"
Cohesion: 0.07
Nodes (26): 1. Find the Bot, 2. Verify You're Authorized, 3. Start Chatting, AgentShroud User Guide, Commands, Dashboard Overview, FAQ, Getting Started (+18 more)

### Community 328 - "Skill: MCP AWS Profile Configuration (MCPM-AWS-PROFILE)"
Cohesion: 0.06
Nodes (35): "Access Denied", AWS Profile Basics, AWS SSO Configuration, Best Practices, Check Current Profile, Configuration Files, Configure New Profile, Default Profile vs Named Profiles (+27 more)

### Community 329 - "Skill: MCP AWS Profile Configuration (MCPM-AWS-PROFILE)"
Cohesion: 0.06
Nodes (35): "Access Denied", AWS Profile Basics, AWS SSO Configuration, Best Practices, Check Current Profile, Configuration Files, Configure New Profile, Default Profile vs Named Profiles (+27 more)

### Community 330 - "AgentShroud: A Transparent Proxy Framework for Enterprise Governance of Autonomous AI Agents"
Cohesion: 0.08
Nodes (26): Abstract, AgentShroud: A Transparent Proxy Framework for Enterprise Governance of Autonomous AI Agents, I. Introduction, II-A. AI Agent Security, II-B. STPA-Sec, II-C. Transparent Proxy Architectures, II. Related Work, III-A. Attacker Model (+18 more)

### Community 331 - "Phase Review: P0 - Core Pipeline Wiring"
Cohesion: 0.10
Nodes (24): 1. Accomplishments This Phase, 2. Security Value Audit, 3. Remaining Work — Prioritized by Value, 4. Risks & Gaps, 5. Merge Readiness Assessment, 🟡 AREAS REQUIRING VALIDATION, Basic Test Infrastructure (⚠️ PARTIAL), Conclusion (+16 more)

### Community 332 - "Telegram & Gmail Integration Guide"
Cohesion: 0.06
Nodes (35): 1. Backup Configuration, 2. Regular Health Checks, 3. Auto-Restart on Reboot, 4. Monitor Logs, 5. Test Regularly, Bot Not Responding, Bot Responds Slowly, "Bot was blocked by user" Error (+27 more)

### Community 333 - "test_cli_coverage.py"
Cohesion: 0.08
Nodes (17): client_from_env(), Build SCLClient from args or environment variables., HTTP client for the AgentShroud SCL REST API (/soc/v1/)., _default_format(), _is_tty(), main(), _tail_ws(), _FakeConnect (+9 more)

### Community 334 - "Skill: MCP AWS Profile Configuration (MCPM-AWS-PROFILE)"
Cohesion: 0.06
Nodes (35): "Access Denied", AWS Profile Basics, AWS SSO Configuration, Best Practices, Check Current Profile, Configuration Files, Configure New Profile, Default Profile vs Named Profiles (+27 more)

### Community 335 - "graphify reference: extra exports and benchmark"
Cohesion: 0.08
Nodes (21): For /graphify add, For --watch, graphify reference: add a URL and watch a folder, graphify reference: extra exports and benchmark, Step 6b - Wiki (only if --wiki flag), Step 7 - Neo4j export (only if --neo4j or --neo4j-push flag), Step 7b - SVG export (only if --svg flag), Step 7c - GraphML export (only if --graphml flag) (+13 more)

### Community 336 - "Coding Agent (bash-first)"
Cohesion: 0.10
Nodes (21): Auto-Notify on Completion, Bash Tool Parameters, Batch PR Reviews (parallel army!), Building/Creating, Claude Code, Codex CLI, Coding Agent (bash-first), Flags (+13 more)

### Community 337 - ".agents/skills/i-tw/SKILL.md"
Cohesion: 0.08
Nodes (25): Anti-Patterns to Flag, API / Function Reference, Architecture Decision Record (ADR), Changelog Entry, Core Discipline: Understand → Structure → Write → Validate, Dependencies, Document Structure, Document-Type Patterns (+17 more)

### Community 338 - "Prompt: Daily Component Health Digest"
Cohesion: 0.11
Nodes (20): Mandatory Daily Delivery (never [SILENT]), Prompt: Daily Component Health Digest, Script-Output-Only Constraint (no tools, no recomputation), Stale Trivy Scan Disclosure Requirement, agentshroud-email-send.sh Gateway Email Sender, Mandatory --html Flag Rule, Prompt: Hermes Competitive Intelligence Email (AM/PM), render_md_email.py Markdown-to-Inline-CSS Email Renderer (+12 more)

### Community 339 - "hermes/SOUL.md"
Cohesion: 0.13
Nodes (18): AgentShroud Hermes System Identity (agents/hermes-soul.md), Security Reviewer Agent, OpenClaw/AgentShroud Bot Identity, marvin (dev host, per openclaw-identity.md), raspberrypi (per openclaw-identity.md), trillian (per openclaw-identity.md), Agents Folder README, Hermes MCP Servers Config (+10 more)

### Community 340 - "Atlas — Curriculum Architect"
Cohesion: 0.08
Nodes (25): Athena — Knowledge Distiller (SKILL), cheatsheet.md Output Template, show_notes.md Output Template, Atlas — Curriculum Architect (README), Atlas — Curriculum Architect (SKILL), Bloom's Taxonomy, curriculum.md Output Template, Gleim CPA Review Study Unit Mapping (+17 more)

### Community 341 - "wakeword.c"
Cohesion: 0.13
Nodes (35): ws_client_handle_t, _send_status_beacon(), voice_task(), vt_agent_count(), vt_remote_log(), _touch_pressed(), _touch_start_only(), _agent_btn_pressed() (+27 more)

### Community 342 - "Skill: MCP AWS Profile Configuration (MCPM-AWS-PROFILE)"
Cohesion: 0.06
Nodes (35): "Access Denied", AWS Profile Basics, AWS SSO Configuration, Best Practices, Check Current Profile, Configuration Files, Configure New Profile, Default Profile vs Named Profiles (+27 more)

### Community 343 - "Skill: MCP AWS Profile Configuration (MCPM-AWS-PROFILE)"
Cohesion: 0.06
Nodes (35): "Access Denied", AWS Profile Basics, AWS SSO Configuration, Best Practices, Check Current Profile, Configuration Files, Configure New Profile, Default Profile vs Named Profiles (+27 more)

### Community 344 - "_ctx"
Cohesion: 0.09
Nodes (12): args_sha256(), Any, Hash of the canonical arguments, excluding the ticket itself., _ctx(), _principal(), T5: the owner sees raw arguments and their hash — never agent-written prose., There is no summary/justification input to render_card at all., TestApprovalCard (+4 more)

### Community 345 - "AgentShroud Project Terminology"
Cohesion: 0.08
Nodes (25): A, AgentShroud Project Terminology, B, C, D, E, F, Glossary (+17 more)

### Community 346 - "AgentShroud Prerequisites"
Cohesion: 0.08
Nodes (26): Accounts, 📚 Additional Resources, Additional Tools in Containers, AgentShroud Prerequisites, Annually, Base Images, Common Issues, Configuration (+18 more)

### Community 347 - "AgentShroud Weekly Upgrade Report — 2026-08-30"
Cohesion: 0.12
Nodes (26): 1. Summary, 2. Environment mapping, 3. Upgrade table, 4. Security findings, 5. Verification evidence, 6. Breaking changes / manual follow-ups, 7. Rollback instructions, 8. Time spent (+18 more)

### Community 348 - "test_daily_cve_report.py"
Cohesion: 0.07
Nodes (16): _build_image_targets(), Resolve the image tag a container is ACTUALLY running, via docker CLI. The…, Build the list of container image targets for Trivy image scanning. Prefers…, _running_image(), _isolated_alert_state(), fixture, Pin _running_image to the docker-unavailable fallback path so these tests…, Deployments that rename the gateway container (dev runs agentshroud-marvin-… (+8 more)

### Community 349 - "test_jira_weekly_review.py"
Cohesion: 0.07
Nodes (12): _get_fn_stub(), _MockTransport, Records POSTs; returns op-proxy secrets then a 201 for the comment., Tests for the SCRUM-81 Hermes weekly Jira review script. The script lives in…, test_resolve_cloud_id_parses_response(), get_fn(), test_resolve_cloud_id_raises_on_non_200(), test_resolve_cloud_id_raises_when_field_missing() (+4 more)

### Community 350 - "test_scanner_integration_coverage.py"
Cohesion: 0.06
Nodes (11): Coverage tests for gateway/security/scanner_integration.py. Exercises the…, TestAccessControl, TestAiModelSupplyChain, TestAppStateHas, TestClamavSummary, TestComputeScorecard, TestDataConfidentiality, TestIdentityAuth (+3 more)

### Community 351 - "test_soc_egress_endpoints.py"
Cohesion: 0.09
Nodes (30): client(), asyncio, fixture, Returns empty result when scanner_result_history is empty., Returns scanner events from app_state.scanner_result_history., Status query param filters by summary.status., Limit param caps the number of returned items., test_manage_egress_add_remove_rule_and_risk() (+22 more)

### Community 352 - "OpenClaw Setup Guide - agentshroud.ai Bot"
Cohesion: 0.06
Nodes (34): 1. Build and Start OpenClaw, 2. Access OpenClaw Control UI, ✅ Agents, Architecture Overview, Communication Channels, Control UI Not Accessible, Current Security Posture, Data Locations (+26 more)

### Community 353 - "TeamsConfig"
Cohesion: 0.07
Nodes (20): _apply_persisted_overrides(), Return all groups the user belongs to., Return all projects accessible to the user via group membership., Return deduplicated list of all user IDs across all groups., Return the safe_response_prefix for the first group that the user belongs to…, Return the effective collab_mode for a user. Resolution order: 1. Per-user…, Merge group_overrides.json additions into the in-memory TeamsConfig., Top-level teams configuration parsed from agentshroud.yaml `teams:` section. (+12 more)

### Community 354 - "OutputSchemaEnforcer"
Cohesion: 0.07
Nodes (21): OutputSchemaEnforcer, Definition for a named output schema., Result of validating output against a schema., Output Schema Enforcement — C25 Validates and sanitizes outbound agent…, Validates outbound responses against structural schemas. Usage:: enforcer =…, Register the built-in default schema., Register or replace a named schema., Validate output against the named schema. Args: output: The agent response text… (+13 more)

### Community 355 - "DELIVERABLE 1 — Domain-by-Domain Assessment"
Cohesion: 0.08
Nodes (26): DELIVERABLE 1 — Domain-by-Domain Assessment, Domain 10 — Human Approval Design, Domain 11 — Prompt and Policy Hardening, Domain 12 — Output Validation and Secondary Controls, Domain 13 — Sandboxing and Execution Isolation, Domain 14 — Browser and Document Ingestion Hardening, Domain 15 — Secret Management and Anti-Exfiltration Design, Domain 16 — Detection Engineering and Monitoring (+18 more)

### Community 356 - "Canvas Skill"
Cohesion: 0.08
Nodes (24): 1. Create HTML content, 2. Find your canvas host URL, 3. Find connected nodes, 4. Present content, 5. Navigate, snapshot, or hide, Actions, Architecture, Canvas Skill (+16 more)

### Community 358 - "ws_client.c"
Cohesion: 0.21
Nodes (19): _deliver_utterance(), rlog_task(), esp_err_t, esp_event_base_t, ws_client_handle_t, _on_event(), ws_client_connected(), ws_client_create() (+11 more)

### Community 359 - "GroupRegistry"
Cohesion: 0.10
Nodes (15): Group, GroupRegistry, _load_persisted_groups(), A named group of users., Manages user groups including auto-groups and custom groups., Derive and reset auto-groups from current RBAC user list, then load custom…, Return group by ID, or None., Create or replace a custom group and persist it. (+7 more)

### Community 361 - "_req"
Cohesion: 0.09
Nodes (7): _req(), TestBrowserSecurity, TestContextGuard, TestEnvGuard, TestGitGuard, TestMultiTurnTracker, TestProcessRequestIdentity

### Community 362 - "TestCollaboratorPersistence"
Cohesion: 0.11
Nodes (7): removed_collaborator_ids / paused_collaborator_ids share…, Bug 1: revoking a hardcoded default (never in approved_collaborators.json) must…, Bug 1: RBACConfig.__post_init__ must exclude persisted-removed IDs from the…, Pausing is access-gating only, not a role/removal change (constraint check)., Writes to one exclusion set must not clobber the other persisted keys., TestCollaboratorPersistence, boom()

### Community 363 - "apply-patches.js"
Cohesion: 0.06
Nodes (32): allAllowedOrigins, allowedOrigins, cIdx, COLLAB_LOCAL_INFO_ONLY, _COLLAB_TOOL_DENY, _COLLAB_TOOL_DENY_FULL_ACCESS, COLLABORATOR_IDS, config (+24 more)

### Community 364 - "AgentShroud Operations Runbook"
Cohesion: 0.06
Nodes (32): 1. Starting and Stopping AgentShroud, 2. Health Monitoring, 3. Viewing Audit Logs, 4. Handling Alerts, 5. API Key Rotation, 6. System Updates, 7. Backup and Restore Procedures, 8. Common Troubleshooting Scenarios (+24 more)

### Community 365 - "Google Services Setup - Calendar, Contacts, Keep"
Cohesion: 0.06
Nodes (32): Alternative: Google People API, CLI Tool: gcalcli, 📊 Comparison: CalDAV vs OAuth2, For Immediate Use: CalDAV/CardDAV, For Production: OAuth2 + Google APIs, 📧 Gmail Already Working, 📅 Google Calendar (CalDAV), 📞 Google Contacts (CardDAV) (+24 more)

### Community 366 - "hermes_dashboard_ws_proxy"
Cohesion: 0.09
Nodes (14): hermes_dashboard_ws_proxy(), Relay the Hermes dashboard's WebSocket channels (/api/ws, /api/pub) through the…, asyncio, hermes_dashboard_proxy must reject traversal sequences before forwarding., hermes_dashboard_proxy raises HTTPException(400) for traversal in path., hermes_dashboard_proxy raises HTTPException(400) for traversal in query string., hermes_dashboard_ws_proxy: WebSocket counterpart of hermes_dashboard_proxy.…, Upstream URL must be ws:// (not http://) at the bridge port, with the client's… (+6 more)

### Community 367 - "ESP32-S3-BOX-3 Voice Terminal — Manual Setup Runbook"
Cohesion: 0.10
Nodes (19): 11. Current status (v1.2.0), 12. OTA Wireless Firmware Updates, 2. Toolchain — install ESP-IDF v5.4, 3. Get the firmware, 4. Configure WiFi credentials, 5. Build · flash · monitor, 5a. IDF v5.4 auto-patches (applied automatically — for reference), 7. Voice Gateway — server-side ✅ LIVE (install/config/OTA: docs/integrations/voice-terminal-esp32-s3.md) (+11 more)

### Community 368 - "daily_cve_report.py"
Cohesion: 0.08
Nodes (33): get_agent_cve_source(), Return the CVE-pipeline config for *bot_id* (raises KeyError if unknown). Args:…, _already_checked_upstream_today(), _already_ingested_ghsa_today(), _already_sent_today(), cve_report_scheduler(), format_upstream_cve_alert(), ghsa_ingest_scheduler() (+25 more)

### Community 369 - "What You Must Do When Invoked"
Cohesion: 0.10
Nodes (20): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Step 0 - GitHub repos and multi-path merge (only if a URL or several paths) (+12 more)

### Community 370 - "Phase 3 Requirements: Working Chat Container"
Cohesion: 0.08
Nodes (23): Core Identity (from IDENTITY.md, SOUL.md, USER.md), Critical Constraint, Deferred Security Controls (Phase 5+), DEFERRED TO PHASE 4+ (Advanced Features), Files to Mount in Container, MUST HAVE (Phase 3 - Minimum Viable Chat), Must-Implement Security Controls (from 10_skills_to_harden_openclaw.txt), Notes (+15 more)

### Community 371 - "OpenClaw Cron Jobs Reference & Recreation Guide"
Cohesion: 0.20
Nodes (13): 2026-08-24 incident history (for context, not action items), Known drift from `docker/config/openclaw/cron/jobs.json`, OpenClaw Cron Jobs — Reference & Recreation Guide, Shared dependencies (must exist before dependent jobs run), Monthly Journal File (/opt/data/memories/journal-YYYY-MM.md), Prompt: Daily Memory Journal, CVE Triage 3-Job Pipeline, OpenClaw Cron Jobs Reference & Recreation Guide (+5 more)

### Community 372 - "DockerEngine"
Cohesion: 0.13
Nodes (3): DockerEngine, Any, Container engine backed by the Docker CLI.

### Community 373 - "Hermes Cron Jobs Reference & Recreation Guide"
Cohesion: 0.08
Nodes (35): Hermes Cron Jobs — Reference & Recreation Guide, Cron: Daily Competitive Landscape Update, Provider-Must-Be-Custom Rule, Hermes Cron Jobs Reference & Recreation Guide, How to recreate a job, Job index, trend-log.md Rolling One-Line Summary Log, Prompt: Newsletter — Chat Front-Ends & Search Infra (+27 more)

### Community 374 - "is_quota_exhausted"
Cohesion: 0.10
Nodes (29): _is_anthropic_quota(), _is_google_quota(), _is_openai_quota(), is_quota_exhausted(), is_rate_limited_post_retry(), Return (True, token) if the response indicates a billing/quota wall. The stable…, Quota-exhaustion detector for cloud LLM providers. Pure-function module — no…, Return (True, "anthropic_rate_limit"/"openai_rate_limit"/...) for a persistent… (+21 more)

### Community 375 - "What You Must Do When Invoked"
Cohesion: 0.08
Nodes (23): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+15 more)

### Community 376 - "System Instructions: Credential Security (Ultra-Conservative)"
Cohesion: 0.08
Nodes (26): 🔐 Core Security Principle, 🧪 Decision Examples, Example 1: User Asks for Password (Chat), Example 2: User Asks for Password (Console), Example 3: User Wants Service Configured, Example 4: User Insists on Seeing Password, 💬 Example Conversations, 📝 Implementation Checklist (+18 more)

### Community 377 - "AgentShroud Security Policy - Final Decision"
Cohesion: 0.10
Nodes (20): 1Password App, 📋 Access Methods, AgentShroud Security Policy - Final Decision, 📚 Authoritative Documentation, Console (Direct Command), 🎯 Final Security Policy, ✅ How to Access Credentials, 📊 How We Got Here (+12 more)

### Community 378 - "app_main.c"
Cohesion: 0.08
Nodes (32): face_emotion_t, app_main(), _build_ws_url(), esp_event_base_t, _lvgl_flush_wait_yield(), _on_tts_pcm(), _on_ws_ctrl(), ui_init() (+24 more)

### Community 379 - "HeuristicClassifier"
Cohesion: 0.13
Nodes (11): HeuristicClassifier, Pattern, [EXPERIMENTAL] Attempt to load a fine-tuned ML model. Returns True on success.…, Score a single signal pattern. Returns 0.0–1.0., Detect unusual Unicode patterns that suggest evasion., Classify text for injection probability. Args: text: Input text to classify…, Heuristic-based classification using multi-signal analysis., [EXPERIMENTAL] ML model classification placeholder. (+3 more)

### Community 380 - "archive_old_events"
Cohesion: 0.09
Nodes (23): Connection, archive_old_events(), _cli(), purge_low_value_events(), datetime, Path, Archive+delete ALL rows matching (event_type, severity), regardless of age. For…, Move audit_events older than cutoff_days into archive_path, then delete +… (+15 more)

### Community 381 - "asyncio"
Cohesion: 0.10
Nodes (9): _old_cred(), asyncio, TestCheckAndRotateDisabled, TestEmergencyAndRetire, TestGenerateAndValidate, TestReadFrom1Password, TestRotateGuardBranches, TestStatusHelpers (+1 more)

### Community 382 - "gen.py"
Cohesion: 0.36
Nodes (9): default_out_dir(), get_model_defaults(), main(), pick_prompts(), Path, Return (default_size, default_quality) for the given model., request_images(), slugify() (+1 more)

### Community 384 - "xurl — Agent Skill Reference"
Cohesion: 0.06
Nodes (32): Check your activity, Command Details, Common Workflows, Direct Messages, Engagement, Error Handling, Global Flags, Go (+24 more)

### Community 385 - "AWS Cloud Management & FinOps Agent"
Cohesion: 0.06
Nodes (31): AWS Cloud Management & FinOps Agent, Cost Optimization Priority, Cross-Account & Future Proofing, Decision Framework, Deliverables, EBS Performance Analysis (Critical Pattern), Expertise, FY26 Cost Reduction Context (+23 more)

### Community 386 - "AgentShroud Security Overview v0.8.0"
Cohesion: 0.10
Nodes (23): AgentShroud Security Overview v0.8.0, AgentShroud Security Overview — v0.8.0, Before & After: Security Finding Remediation, Memory Refresh Context, Test Coverage Summary (Post-Remediation), v0.9.0 — Production Hardening, v0.9.0 / v1.0.0 Roadmap, v1.0.0 — Zero-Trust Compute (+15 more)

### Community 387 - "Workstream D — Sync agents/skills/MCP from `~/.llm_settings` into both bots"
Cohesion: 0.22
Nodes (16): Workstream A: Groups and Teamwork in OpenClaw, Workstream C: Full Local-Model Parity (Both Bots), Workstream E: Blue and Red Team Security Scan (Both Bots), Acceptance, Acceptance, Intent, Intent, Module surface to extend (+8 more)

### Community 388 - "ESP32-S3-BOX-3 Voice Terminal for Hermes (behind AgentShroud)"
Cohesion: 0.08
Nodes (24): 10. Alternatives (only if needed), 11. Open decisions (confirm before server-side coding), 1. Why this differs from a generic ESP32+Hermes build, 2.1 New `voice_gateway/` service, 2.2 Close the governed-path schema gap for Hermes  ⚠️ required, 2.3 Compose + tailnet exposure, 2.4 Egress & governance — what does NOT change, 2.5 Tests (CLAUDE.md §4, coverage gate `fail_under=84`) (+16 more)

### Community 389 - "Skill: MCP Auth Reset (MCPM-AUTH-RESET)"
Cohesion: 0.06
Nodes (31): 1. GitHub MCP Authentication Reset, 2. Atlassian MCP Authentication Reset, 3. AWS API MCP Authentication Reset, Atlassian OAuth, Atlassian: "OAuth flow failed", Authentication Reset Procedures, AWS Credentials, AWS: "Token expired" (SSO) (+23 more)

### Community 390 - "Network Topology"
Cohesion: 0.25
Nodes (7): Container Network Diagram, Hostname Resolution, Network Security Notes, Network Topology, Related Notes, Traffic Routing, Bot Network Isolation Design

### Community 391 - "GIT-GUARD Skill Definition"
Cohesion: 0.19
Nodes (14): GSDE&G Development Master Checklist Skill, CI/CD Pipeline Advisor SKILL (OpenClaw), Code Review (CR) README (OpenClaw), Code Review (CR) SKILL (OpenClaw), Create PR with Pre-Flight Audit (CRPR) SKILL (OpenClaw), devsecops SKILL stub (OpenClaw), Branch Naming Convention (feat/fix/hotfix/chore/refactor/test/docs), Mandatory 10-Step Git Workflow (+6 more)

### Community 392 - "AWS Cloud Management & FinOps Agent"
Cohesion: 0.06
Nodes (31): AWS Cloud Management & FinOps Agent, Cost Optimization Priority, Cross-Account & Future Proofing, Decision Framework, Deliverables, EBS Performance Analysis (Critical Pattern), Expertise, FY26 Cost Reduction Context (+23 more)

### Community 393 - "PHASE_3A_3B_IMPLEMENTATION.md"
Cohesion: 0.07
Nodes (32): 3A.1: Re-enable seccomp profiles ✅, 3A.2: Make OpenClaw container read-only ✅, 3A.3: Remove NET_RAW capability ✅, 3A.4: Add mDNS/Bonjour disable ✅, 3A.5: Move gateway password to Docker secrets ✅, 3A.6: Create verify-security.sh ✅, 3A.7: Create scan.sh (OpenSCAP) ✅, 3A.8: Change DM policy to allowlist ✅ (+24 more)

### Community 394 - "AWS Cloud Management & FinOps Agent"
Cohesion: 0.06
Nodes (31): AWS Cloud Management & FinOps Agent, Cost Optimization Priority, Cross-Account & Future Proofing, Decision Framework, Deliverables, EBS Performance Analysis (Critical Pattern), Expertise, FY26 Cost Reduction Context (+23 more)

### Community 395 - "AgentShroud Color Palette"
Cohesion: 0.10
Nodes (20): Accessibility, AgentShroud Blue (Primary), AgentShroud Color Palette, Applications, Borders, Color Combinations, Dark Surface Hierarchy, Dark Theme (+12 more)

### Community 396 - "Credential Security Policy"
Cohesion: 0.11
Nodes (25): Implementation Status, Option 2: Approval Queue for Credential Ops, Option 1: Gateway-Level Filtering, Access Control Matrix, Audit Logging, Behavior Examples, Credential Security Policy, Emergency Override (+17 more)

### Community 397 - ".cursor/mcp.json"
Cohesion: 0.09
Nodes (22): autoOpenFile, outputPath, PATH, .llm_settings/mcp-servers/atlassian/agentshroud/mcp-atlassian.sh, .llm_settings/mcp-servers/atlassian/idallasj/mcp-atlassian.sh, .llm_settings/mcp-servers/devonthink/mcp-devonthink.sh, .llm_settings/mcp-servers/github/agentshroud/github-mcp-wrapper.sh, .llm_settings/mcp-servers/github/default/github-mcp-wrapper.sh (+14 more)

### Community 398 - "Skill: MCP Auth Reset (MCPM-AUTH-RESET)"
Cohesion: 0.06
Nodes (31): 1. GitHub MCP Authentication Reset, 2. Atlassian MCP Authentication Reset, 3. AWS API MCP Authentication Reset, Atlassian OAuth, Atlassian: "OAuth flow failed", Authentication Reset Procedures, AWS Credentials, AWS: "Token expired" (SSO) (+23 more)

### Community 399 - "generate-cve-page.py"
Cohesion: 0.22
Nodes (12): _agent_display_name(), _build_heading(), _build_table(), generate(), Return the human-readable display name for a bot_id., Build the H2 heading block for one agent's CVE section., Build the full paginated CVE table block for one agent's section. Args: cves:…, Return a mapping of bot_id → CVE list, using the new API when available. Falls… (+4 more)

### Community 400 - "agentshroud-ieee-paper.md"
Cohesion: 0.10
Nodes (22): CVE-2026-22708 (Indirect Prompt Injection via Web Browsing), CVE-2026-25253 (OpenClaw RCE), Debenedetti et al., The Attacker Moves Second (2025), DNS-Layer Enforcement, Leveson, Engineering a Safer World (2012), Log-To-Leak MCP Exfiltration Attack, MCP Proxy Layer, MiddlewareManager (35 Modules) (+14 more)

### Community 401 - "Skill: MCP Auth Reset (MCPM-AUTH-RESET)"
Cohesion: 0.06
Nodes (31): 1. GitHub MCP Authentication Reset, 2. Atlassian MCP Authentication Reset, 3. AWS API MCP Authentication Reset, Atlassian OAuth, Atlassian: "OAuth flow failed", Authentication Reset Procedures, AWS Credentials, AWS: "Token expired" (SSO) (+23 more)

### Community 402 - ".github/mcp.json"
Cohesion: 0.09
Nodes (22): autoOpenFile, outputPath, PATH, .llm_settings/mcp-servers/atlassian/agentshroud/mcp-atlassian.sh, .llm_settings/mcp-servers/atlassian/idallasj/mcp-atlassian.sh, .llm_settings/mcp-servers/devonthink/mcp-devonthink.sh, .llm_settings/mcp-servers/github/agentshroud/github-mcp-wrapper.sh, .llm_settings/mcp-servers/github/default/github-mcp-wrapper.sh (+14 more)

### Community 403 - ".mcp.json"
Cohesion: 0.09
Nodes (22): autoOpenFile, outputPath, PATH, .llm_settings/mcp-servers/atlassian/agentshroud/mcp-atlassian.sh, .llm_settings/mcp-servers/atlassian/idallasj/mcp-atlassian.sh, .llm_settings/mcp-servers/devonthink/mcp-devonthink.sh, .llm_settings/mcp-servers/github/agentshroud/github-mcp-wrapper.sh, .llm_settings/mcp-servers/github/default/github-mcp-wrapper.sh (+14 more)

### Community 404 - ".omp/mcp.json"
Cohesion: 0.09
Nodes (22): autoOpenFile, outputPath, PATH, .llm_settings/mcp-servers/atlassian/agentshroud/mcp-atlassian.sh, .llm_settings/mcp-servers/atlassian/idallasj/mcp-atlassian.sh, .llm_settings/mcp-servers/devonthink/mcp-devonthink.sh, .llm_settings/mcp-servers/github/agentshroud/github-mcp-wrapper.sh, .llm_settings/mcp-servers/github/default/github-mcp-wrapper.sh (+14 more)

### Community 405 - ".pi/mcp.json"
Cohesion: 0.09
Nodes (22): autoOpenFile, outputPath, PATH, .llm_settings/mcp-servers/atlassian/agentshroud/mcp-atlassian.sh, .llm_settings/mcp-servers/atlassian/idallasj/mcp-atlassian.sh, .llm_settings/mcp-servers/devonthink/mcp-devonthink.sh, .llm_settings/mcp-servers/github/agentshroud/github-mcp-wrapper.sh, .llm_settings/mcp-servers/github/default/github-mcp-wrapper.sh (+14 more)

### Community 406 - "🛡️ AgentShroud Release Plan"
Cohesion: 0.08
Nodes (27): 🛡️ AgentShroud Release Plan, Current Execution Tracker (2026-03-14), Current hard gate, Current status snapshot, Live tracker files, v1.1.0 "Groups" — Workspaces for Teams (6 items), v1.2.0 "Local LLMs" — Offline Model Support (4 items), 8. Comprehensive Multilingual Prompt Injection Defense (+19 more)

### Community 407 - "1. Accomplishments This Phase"
Cohesion: 0.06
Nodes (31): 1. Accomplishments This Phase, 2. Security Value Audit, 3. Remaining Work — Prioritized by Value, 4. Risks & Gaps, 5. Test Results, AgentShroud Phase Review — 2026-02-24, 📁 **AlertDispatcher Storage Fix**, ⚠️ **Areas Requiring Vigilance** (+23 more)

### Community 408 - "make_httpx_fetcher"
Cohesion: 0.11
Nodes (10): Fetcher, make_httpx_fetcher(), Production fetcher: stream the URL and hash the body as proof-of-source.…, _FakeStreamResponse, Stand-in for the object httpx.stream() yields as a context manager., Patch httpx.stream; return a list that records the call kwargs., TestMakeHttpxFetcher, Fake httpx.stream context manager yielding a body in chunks. (+2 more)

### Community 409 - "WebContentScanner"
Cohesion: 0.08
Nodes (16): FindingSeverity, Enum, str, Scan web content for prompt injection, PII, and hidden payloads. All findings…, WebContentScanner, Proves enforcement, not just detection., Gateway XML DTD/entity control — CLAUDE.md 0.05 arm 2. CVE-2026-6653 is a use-…, The '[' block inside DOCTYPE is what xmlParseInternalSubset parses. (+8 more)

### Community 411 - "AgentShroud Security Value Proposition"
Cohesion: 0.09
Nodes (23): AgentShroud Security Value Proposition, Comparison: Three Deployment Options, CRITICAL (Do First):, HIGH VALUE:, Is AgentShroud worth the effort?, LOW VALUE (Maybe Later):, MEDIUM VALUE:, My Recommendation (+15 more)

### Community 412 - "TestContributingMdAccuracy"
Cohesion: 0.07
Nodes (11): fixture, Verify CONTRIBUTING.md references are correct., The test command in CONTRIBUTING.md should be valid., Verify README.md claims match actual implementation., This representative sample of modules mentioned in README should exist as code., README claims Python 3.9+., Verify SECURITY.md content., _read_file() (+3 more)

### Community 413 - "AWS Cloud Management & FinOps Agent"
Cohesion: 0.06
Nodes (31): AWS Cloud Management & FinOps Agent, Cost Optimization Priority, Cross-Account & Future Proofing, Decision Framework, Deliverables, EBS Performance Analysis (Critical Pattern), Expertise, FY26 Cost Reduction Context (+23 more)

### Community 414 - "Skill: MCP Auth Reset (MCPM-AUTH-RESET)"
Cohesion: 0.06
Nodes (31): 1. GitHub MCP Authentication Reset, 2. Atlassian MCP Authentication Reset, 3. AWS API MCP Authentication Reset, Atlassian OAuth, Atlassian: "OAuth flow failed", Authentication Reset Procedures, AWS Credentials, AWS: "Token expired" (SSO) (+23 more)

### Community 415 - "AgentShroud Security Hardening Plan"
Cohesion: 0.09
Nodes (22): AgentShroud Security Hardening Plan, Architecture, Current State (2026-02-24), Current State (v0.7.0 → All Phases Complete), Endpoints, Execution Order, FINAL: Network Lockdown Activation ✅ DONE, GitHub Workflow (+14 more)

### Community 416 - "AWS Cloud Management & FinOps Agent"
Cohesion: 0.06
Nodes (31): AWS Cloud Management & FinOps Agent, Cost Optimization Priority, Cross-Account & Future Proofing, Decision Framework, Deliverables, EBS Performance Analysis (Critical Pattern), Expertise, FY26 Cost Reduction Context (+23 more)

### Community 417 - "Sunday Upgrade 2026-11-15 — DEV run (agentshroud-bot), 01:00–02:25 ET"
Cohesion: 0.06
Nodes (32): 1. Summary line, 2. Environment mapping, 3. Upgrade table (latest via scripts/discover_upstream_versions.py, 2026-11-15 ~01:05 ET), 3a. Per-component change report, 3a. Per-component change report, 3b. Not updated this run — plan, 3b. Not updated this run — plan for the week, 4. Security findings (+24 more)

### Community 418 - "AgentShroud Deployment Architecture"
Cohesion: 0.09
Nodes (21): ADR-007: Zero-Config Security, AgentShroud Deployment Architecture, Apple Containers (macOS), Cloud Provider Secrets, Default Port Allocation, Deployment Validation, DNS Routing Configuration, Docker Runtime (+13 more)

### Community 419 - "Skill: Technical Illustrator (TI)"
Cohesion: 0.09
Nodes (21): Anti-Patterns to Flag, Architecture (C4 / block) — System boundaries and components, ASCII Art (fallback — no renderer available), Brand Theme Block (Mermaid), Core Discipline: Understand → Diagram → Validate → Export, Data Flow — How data moves and transforms, Dependencies, Diagram Types and Data Lakehouse Examples (+13 more)

### Community 420 - "plan_remediation"
Cohesion: 0.06
Nodes (39): _entry(), test_auto_remediate_cves.py (CVE remediation planner tests), test_pin_revert_restores_the_exact_original_string, Tests for scripts/auto_remediate_cves.py — automated CVE remediation planning.…, Already-triaged entries are somebody's assessed verdict — a version bump…, An operator may cap how far forward an unattended job may jump., Reading and rewriting docker/versions.env., Silently appending a new key could create a pin nothing consumes. (+31 more)

### Community 421 - "1Password op-proxy (POST /credentials/op-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s)"
Cohesion: 0.11
Nodes (29): AgentShroud Gateway (Trust Zone 1): holds 1Password service account, enforces policy, signs ledger entries, controls approval queue, HMAC/JWT validation, HTTP CONNECT egress proxy (gateway:8181; domain allowlist via agentshroud.yaml proxy.allowed_domains; blocks RFC1918 + unlisted domains; logs connections), 1Password op-proxy (POST /credentials/op-proxy; validates GATEWAY_AUTH_TOKEN + allowed_op_paths; cascading retry 5s,10s,15s,30s,60s), Trust Boundary Diagram, Blocked/Untrusted (LAN RFC1918, unlisted domains), Trust Zone 2 — Bot (Supervised Agent: no direct credential/internet access), Trust Zone 3 — External Services (OpenAI, Anthropic, Telegram, GitHub, 1Password; allowlisted HTTPS only), Trust Zone 4 — Infrastructure Nodes (raspberrypi, marvin, trillian; SSH-gated) (+21 more)

### Community 422 - "Enterprise Security Feature Priorities"
Cohesion: 0.50
Nodes (4): Credential Isolation Planning, Enterprise Security Feature Priorities, Outbound Information Filter Planning, Separation of Privilege Planning

### Community 423 - "Skill: Technical Illustrator (TI)"
Cohesion: 0.09
Nodes (21): Anti-Patterns to Flag, Architecture (C4 / block) — System boundaries and components, ASCII Art (fallback — no renderer available), Brand Theme Block (Mermaid), Core Discipline: Understand → Diagram → Validate → Export, Data Flow — How data moves and transforms, Dependencies, Diagram Types and Data Lakehouse Examples (+13 more)

### Community 424 - "Phase 3: MITIGATE (Rollback First!)"
Cohesion: 0.12
Nodes (16): Follow-up (within 48 hours), Glue Job Rollback, Immediate (within 2 hours), Incident Response Workflow, Phase 1: ASSESS (Max 5 minutes), Phase 2: COMMUNICATE (Concurrent with assess), Phase 3: MITIGATE (Rollback First!), Post-Incident (+8 more)

### Community 425 - "Skill: Technical Illustrator (TI)"
Cohesion: 0.09
Nodes (21): Anti-Patterns to Flag, Architecture (C4 / block) — System boundaries and components, ASCII Art (fallback — no renderer available), Brand Theme Block (Mermaid), Core Discipline: Understand → Diagram → Validate → Export, Data Flow — How data moves and transforms, Dependencies, Diagram Types and Data Lakehouse Examples (+13 more)

### Community 426 - "Skill: MCP Auth Reset (MCPM-AUTH-RESET)"
Cohesion: 0.06
Nodes (31): 1. GitHub MCP Authentication Reset, 2. Atlassian MCP Authentication Reset, 3. AWS API MCP Authentication Reset, Atlassian OAuth, Atlassian: "OAuth flow failed", Authentication Reset Procedures, AWS Credentials, AWS: "Token expired" (SSO) (+23 more)

### Community 427 - "Voice Terminal — ESP32-S3-BOX-3 (Optional AgentShroud Add-On)"
Cohesion: 0.09
Nodes (21): 1. Generate the voice gateway token, 2. Create `wifi_credentials.h`, 3. Start the voice gateway, 4. Enable Tailscale Funnel, 5. Build and flash the firmware, Adding a future agent, Agent toggle (MUTE button — BSP_BUTTON_MUTE), Architecture (+13 more)

### Community 429 - "AgentShroud: Enterprise Governance for Autonomous AI Agents"
Cohesion: 0.08
Nodes (26): Architecture Overview, 11.1 Complete 26-Module Security Matrix, 11.2 Unique AgentShroud Modules (No Competitor Implementation), 11.3 Competitor Analysis Details, 11.4 Security Coverage Gap Analysis, 11.5 Security Score Evolution, 11.6 Industry Implications, 11. Competitive Security Comparison Matrix (+18 more)

### Community 430 - "v0.8.0 — "Watchtower" (Complete Security + Everything We Know Today)"
Cohesion: 0.09
Nodes (25): A. Steve Hay — ALL Tiers (14 features, 23 requirements), B. Wire ALL Modules Into Request Path, C. Bug Fixes, D. Interactive Egress Firewall ("Little Snitch for Agents"), E. Observatory Mode (Global Monitor/Enforce Switch), F. Prompt Injection Hardening, G. Encrypted Container-to-Container Communication, H. Pi-hole as Default Stack Component (+17 more)

### Community 431 - "agentshroud-blueteam/SKILL.md"
Cohesion: 0.08
Nodes (27): AgentShroud Module Inventory (Blue Team), AgentShroud Blue Team Security Auditor, Audit Procedure, Critical Rules, Heat Map Legend, Infrastructure, Loss Categories, Methodology (+19 more)

### Community 432 - "AWS Cloud Management & FinOps Agent"
Cohesion: 0.06
Nodes (31): AWS Cloud Management & FinOps Agent, Cost Optimization Priority, Cross-Account & Future Proofing, Decision Framework, Deliverables, EBS Performance Analysis (Critical Pattern), Expertise, FY26 Cost Reduction Context (+23 more)

### Community 433 - "Hermes Agent — Connection Setup"
Cohesion: 0.09
Nodes (22): API Key Setup, Authentication Flow, Chatbox, Frontend Client Setup, HCI (Hermes Control Interface), HCI Network Access, HCI Tailscale Serve Configuration, Hermes Agent — Connection Setup (+14 more)

### Community 435 - "Skill: MCP Auth Reset (MCPM-AUTH-RESET)"
Cohesion: 0.06
Nodes (31): 1. GitHub MCP Authentication Reset, 2. Atlassian MCP Authentication Reset, 3. AWS API MCP Authentication Reset, Atlassian OAuth, Atlassian: "OAuth flow failed", Authentication Reset Procedures, AWS Credentials, AWS: "Token expired" (SSO) (+23 more)

### Community 436 - "CollaboratorActivityTracker"
Cohesion: 0.09
Nodes (18): CollaboratorActivityTracker, Path, Return a health snapshot suitable for /status/detail., Best-effort float timestamp coercion for resilient log reads., Return activity entries sorted newest-first. Args: since: Unix timestamp — only…, Return aggregated statistics over all recorded activity. Returns: Dict with…, Tracks collaborator messages at the gateway level. Records every inbound…, Short numeric UIDs (< 7 digits) must be silently dropped before any write. (+10 more)

### Community 437 - "Skill: UX Expert (UX)"
Cohesion: 0.06
Nodes (30): Alert Prioritization Display, Anti-Patterns to Flag, CLI / TUI UX, CLI UX Rules, Confirmation Patterns, Content Organization Patterns, Contextual Actions, Core Discipline: Discover → Define → Design → Validate (+22 more)

### Community 438 - "Pre-Deployment Checklist"
Cohesion: 0.10
Nodes (20): 1. Change Documentation, 2. Testing Evidence, 3. Backups & Rollback, 4. Blast Radius, 5. Observability, 6. Security, 7. Communication, 8. Service Control Commands (+12 more)

### Community 439 - "ApprovalStore"
Cohesion: 0.03
Nodes (65): Process an approval decision. IEC 62443 FR1: approving a high-risk action…, Get all pending approval items., Fetch a single queue item by ID., Any, Process an approval decision Args: request_id: Request UUID approved: Whether…, Get all pending (not expired, not decided) items First expires any stale items.…, Fetch a single queue item by ID Args: request_id: Request UUID Returns:…, Remove decided (approved/rejected/expired) items older than max_age_seconds.… (+57 more)

### Community 440 - "browser-extension/manifest.json"
Cohesion: 0.10
Nodes (20): action, default_popup, default_title, background, service_worker, browser_specific_settings, gecko, description (+12 more)

### Community 441 - "AgentShroud Operations Cheat Sheet"
Cohesion: 0.10
Nodes (19): AgentShroud Operations Cheat Sheet, Colima VM, Container Basics, Hermes Control Interface (HCI), Hermes Agent Management, Host IPs (extra_hosts), Key Paths, Kill Switch (Emergency) (+11 more)

### Community 442 - "i-sec-defense SKILL (Blue Team Security Auditor, AgentShroud)"
Cohesion: 0.25
Nodes (8): i-sec-defense README (Blue Team Security Auditor), i-sec-defense SKILL (Blue Team Security Auditor, AgentShroud), STPA-Sec Methodology, i-sec-offense README (Red Team Adversarial Tester), i-sec-offense SKILL (Red Team Adversarial Tester, AgentShroud), Steve Hay's Phase 1 Probes (Red/Blue Team Assessment), i-sec README (Security Review, SecureClaw), i-sec SKILL (Security Review / SEC, SecureClaw)

### Community 443 - "Pre-Deployment Checklist"
Cohesion: 0.10
Nodes (20): 1. Change Documentation, 2. Testing Evidence, 3. Backups & Rollback, 4. Blast Radius, 5. Observability, 6. Security, 7. Communication, 8. Service Control Commands (+12 more)

### Community 444 - "Skill: UX Expert (UX)"
Cohesion: 0.06
Nodes (30): Alert Prioritization Display, Anti-Patterns to Flag, CLI / TUI UX, CLI UX Rules, Confirmation Patterns, Content Organization Patterns, Contextual Actions, Core Discipline: Discover → Define → Design → Validate (+22 more)

### Community 445 - "Pre-Purge Secret Rotation Checklist"
Cohesion: 0.11
Nodes (21): 1Password Item ID Vault-Structure Disclosure, Archive Directory Exposure Risk, Gateway Auth Token Reference Exposure, iCloud App-Specific Password Reference Exposure, Post-Purge Gitleaks Verification, Pre-Purge Secret Rotation Checklist, Telegram Bot Token Reference Exposure, Telegram Chat History Artifact Risk (+13 more)

### Community 446 - "generate_branding_assets.py"
Cohesion: 0.26
Nodes (20): FreeTypeFont, Image, ensure(), generate_email(), generate_favicons(), generate_feature_icons(), generate_icon_sizes(), generate_presentation() (+12 more)

### Community 449 - "jira_weekly_review.py"
Cohesion: 0.09
Nodes (30): _adf_paragraph(), build_basic_auth_header(), build_comment_payload(), build_comment_url(), build_op_proxy_request(), build_tenant_info_url(), build_weekly_summary(), extract_scrum_items() (+22 more)

### Community 450 - "Skill: UX Expert (UX)"
Cohesion: 0.06
Nodes (30): Alert Prioritization Display, Anti-Patterns to Flag, CLI / TUI UX, CLI UX Rules, Confirmation Patterns, Content Organization Patterns, Contextual Actions, Core Discipline: Discover → Define → Design → Validate (+22 more)

### Community 451 - "Deploying AgentShroud on Raspberry Pi (aarch64)"
Cohesion: 0.10
Nodes (21): 1. Clone the Repository, 2. Install Docker, 3. Set Up Secrets, 4. Configure AgentShroud, 5. Build and Start, 6. Verify, ARM64 Builds, Container Won't Start (+13 more)

### Community 452 - "iCloud Services Setup - Complete Guide"
Cohesion: 0.06
Nodes (30): "401 Unauthorized", "403 Forbidden", Access Notes via IMAP, Challenge, 🚀 Complete Setup Script, "Connection timeout", Discovery Process, Discovery Process (+22 more)

### Community 453 - "ContributorManager"
Cohesion: 0.13
Nodes (11): ContributorManager, Builds ContributorRecord instances from RBACConfig + TeamsConfig., _FakeRBAC, Constraint check: paused (owner-initiated) and lockdown_level (auto-escalation)…, _load_paused_ids must never crash record-building if the persisted store is…, Bug 2: contributors.py must call get_status(), not the nonexistent get_level()., SCRUM-203: the app-wide instance on app_state.progressive_lockdown wins., Tests for gateway/soc/contributors.py — ContributorManager record building. No… (+3 more)

### Community 454 - "Container Security Policy — AgentShroud"
Cohesion: 0.10
Nodes (21): 1.1 Capabilities, 1.2 Seccomp Profile, 1.3 Read-Only Filesystem (Planned), 1.4 Non-Root Execution, 1.5 Resource Limits, 1. Container Hardening, 3.1 Hierarchy, 3.2 Rules (+13 more)

### Community 455 - "test_file_sandbox_message_gate.py"
Cohesion: 0.10
Nodes (16): manager(), _plain_msg(), asyncio, fixture, Unit tests for the _is_tool_call_request helper (TDD RED phase)., FileSandbox must NOT block plain chat messages that mention file-like words., Owner (8096968754) must not be blocked by content-pattern scanning. They should…, TDD — FileSandbox message-gating and owner bypass. Root cause of the BLOCKED BY… (+8 more)

### Community 456 - "Skill: UX Expert (UX)"
Cohesion: 0.06
Nodes (30): Alert Prioritization Display, Anti-Patterns to Flag, CLI / TUI UX, CLI UX Rules, Confirmation Patterns, Content Organization Patterns, Contextual Actions, Core Discipline: Discover → Define → Design → Validate (+22 more)

### Community 457 - "Security Modules (58)"
Cohesion: 0.10
Nodes (20): 🛡️ AgentShroud Security Inventory (v0.8.0), Audit & Compliance (4), Collaborator Testing, Encryption & Key Management (3), External Integrations (4), Inbound Defense (6), Infrastructure Protection (8), MCP/Tool Security (6) (+12 more)

### Community 458 - "Skill: UX Expert (UX)"
Cohesion: 0.06
Nodes (30): Alert Prioritization Display, Anti-Patterns to Flag, CLI / TUI UX, CLI UX Rules, Confirmation Patterns, Content Organization Patterns, Contextual Actions, Core Discipline: Discover → Define → Design → Validate (+22 more)

### Community 459 - "AgentShroud v0.8.0 "Watchtower" — Comprehensive Wiring Audit"
Cohesion: 0.10
Nodes (20): 1. EgressTelegramNotifier — Little Snitch Inline Buttons, 2. Approval Queue — Missing Telegram Notifications, 3. OutputCanary — Not Passed to Pipeline, 4. EnhancedToolResultSanitizer — Not Passed to Pipeline, 5. LLMProxy — Never Instantiated, 6. Callback Query Handler for Inline Buttons, 7. KeyVault — Instantiated but Not Used, 8. SidecarScanner — External Tool Interface (+12 more)

### Community 460 - "Skill: UX Expert (UX)"
Cohesion: 0.06
Nodes (30): Alert Prioritization Display, Anti-Patterns to Flag, CLI / TUI UX, CLI UX Rules, Confirmation Patterns, Content Organization Patterns, Contextual Actions, Core Discipline: Discover → Define → Design → Validate (+22 more)

### Community 461 - "graphify Skill"
Cohesion: 0.13
Nodes (20): graphify Add & Watch Reference, graphify Exports & Benchmark Reference, graphify Extraction Subagent Prompt Spec, graphify GitHub Clone & Cross-Repo Merge Reference, graphify Commit Hook & CLAUDE.md Integration Reference, graphify Query/Path/Explain Reference, graphify Transcribe Reference, Whisper Transcription (+12 more)

### Community 462 - "Production Testing Procedures  ⚠️  NO SEPARATE DEV ENVIRONMENT"
Cohesion: 0.10
Nodes (19): A. AWS Glue Jobs, B. AWS Step Functions, C. AWS Athena, D. PostgreSQL — RDS (`fe-gsdl-poc-database`), E. MySQL — On-Site Zabbix Databases (200+ sites), F. IAM Policies, G. Tailscale / Network, General Rules (+11 more)

### Community 463 - "Distributed OpenClaw Node Architecture — Raspberry Pi 4"
Cohesion: 0.10
Nodes (19): Additional Costs (Option 2 vs Option 1), Architecture Comparison, Benefits Gained, Best Use Cases for Distributed Node Approach, Comparison Matrix, Concept Overview, Conclusion, Cost-Benefit Analysis (+11 more)

### Community 464 - "background.js"
Cohesion: 0.15
Nodes (15): clipPage(), extractPageContent(), forwardUrl(), loadConfig(), notify(), reportResult(), icon48.png — solid blue (#2b6cff) placeholder icon, no logo/text, save() (+7 more)

### Community 465 - "dashboard/README.md"
Cohesion: 0.14
Nodes (13): ActionFeed Component (Live Action Stream), DataLedger Component (Forwarded Content Viewer), KillSwitch Component (Emergency Halt), MemoryViewer Component (MEMORY.md Browser), NetworkInspector Component (Outbound Request Monitor), AgentShroud Dashboard, Components (to be implemented in Week 2), Implementation Status (+5 more)

### Community 466 - "Browser — Secure Browser Automation"
Cohesion: 0.07
Nodes (29): 1. Always Specify Risk Level, 2. Use Allowlisting Liberally, 3. Take Screenshots for Audit Trail, 4. Handle CAPTCHAs Gracefully, 5. Never Extract Credentials, "Action requires approval but none granted", Approval Integration, Audit Logging (+21 more)

### Community 467 - "Production Testing Procedures  ⚠️  NO SEPARATE DEV ENVIRONMENT"
Cohesion: 0.10
Nodes (19): A. AWS Glue Jobs, B. AWS Step Functions, C. AWS Athena, D. PostgreSQL — RDS (`fe-gsdl-poc-database`), E. MySQL — On-Site Zabbix Databases (200+ sites), F. IAM Policies, G. Tailscale / Network, General Rules (+11 more)

### Community 468 - "Production Testing Procedures  ⚠️  NO SEPARATE DEV ENVIRONMENT"
Cohesion: 0.10
Nodes (19): A. AWS Glue Jobs, B. AWS Step Functions, C. AWS Athena, D. PostgreSQL — RDS (`fe-gsdl-poc-database`), E. MySQL — On-Site Zabbix Databases (200+ sites), F. IAM Policies, G. Tailscale / Network, General Rules (+11 more)

### Community 469 - "OpenClaw Management Scripts"
Cohesion: 0.06
Nodes (30): drift-detector.sh (planned), memory-scrubber.py (planned), security-audit.sh (planned), skill-scanner.sh (planned), test-network-isolation.sh (planned), test-pii-sanitization.sh (planned), docker/scripts README.md, API Keys (+22 more)

### Community 470 - "AgentShroud v0.8.0 — Full Security & Functionality Audit"
Cohesion: 0.10
Nodes (19): 1. Code Audit, 2. Verify Open Findings, 3. Test Each Module, 4. Collaborator Isolation, 5. Update the Module Matrix, Additional Security Components, AgentShroud v0.8.0 — Full Security & Functionality Audit, Architecture (+11 more)

### Community 471 - "Multi-Agent Role Matrix"
Cohesion: 0.12
Nodes (18): Diagram 21: Team Structure, Diagram 23: Roadmap Gantt (2026), Multi-Agent Role Matrix (AGENT_ROLES.md), GSD Cadence — Get Shit Done Governance (doc), Rule 2 — Approval Tag (approved:isaiah) for High-Severity Changes, Authorization Matrix, Decision Tree for New Tasks, Escalation Path (+10 more)

### Community 472 - "AgentShroud Security Value Proposition - Revised"
Cohesion: 0.08
Nodes (29): AgentShroud Security Value Proposition - Revised, 1. Re-enable Seccomp Profiles, 2. Enable Read-Only Filesystem, 3. Remove NET_RAW Capability, 4. Disable mDNS/Bonjour Broadcasting, 5. Set DM Policy to Allowlist, AgentShroud Security Value Proposition - REVISED, Bottom Line (Corrected) (+21 more)

### Community 473 - "REQUIRED NOTES — PRODUCE EVERY ONE OF THESE"
Cohesion: 0.07
Nodes (30): `00 - START HERE/Home.md`, `00 - START HERE/Quick Reference.md`, `00 - START HERE/System Overview.md`, `01 - Architecture/Architecture Overview.md`, `01 - Architecture/Data Flow.md`, `01 - Architecture/Shutdown & Recovery.md`, `01 - Architecture/Startup Sequence.md`, `02 - Modules/[FileName].md` — ONE PER SOURCE FILE (+22 more)

### Community 475 - "Message Composition with MML (MIME Meta Language)"
Cohesion: 0.10
Nodes (20): Address Formats, Attachments, Basic Message Structure, Composing from CLI, Forward, Headers, Inline Images, Interactive compose (+12 more)

### Community 476 - "Browser — Secure Browser Automation"
Cohesion: 0.07
Nodes (29): 1. Always Specify Risk Level, 2. Use Allowlisting Liberally, 3. Take Screenshots for Audit Trail, 4. Handle CAPTCHAs Gracefully, 5. Never Extract Credentials, "Action requires approval but none granted", Approval Integration, Audit Logging (+21 more)

### Community 478 - "REQUIRED NOTES — PRODUCE EVERY ONE OF THESE"
Cohesion: 0.07
Nodes (30): `00 - START HERE/Home.md`, `00 - START HERE/Quick Reference.md`, `00 - START HERE/System Overview.md`, `01 - Architecture/Architecture Overview.md`, `01 - Architecture/Data Flow.md`, `01 - Architecture/Shutdown & Recovery.md`, `01 - Architecture/Startup Sequence.md`, `02 - Modules/[FileName].md` — ONE PER SOURCE FILE (+22 more)

### Community 479 - "Browser — Secure Browser Automation"
Cohesion: 0.07
Nodes (29): 1. Always Specify Risk Level, 2. Use Allowlisting Liberally, 3. Take Screenshots for Audit Trail, 4. Handle CAPTCHAs Gracefully, 5. Never Extract Credentials, "Action requires approval but none granted", Approval Integration, Audit Logging (+21 more)

### Community 480 - "REQUIRED NOTES — PRODUCE EVERY ONE OF THESE"
Cohesion: 0.07
Nodes (30): `00 - START HERE/Home.md`, `00 - START HERE/Quick Reference.md`, `00 - START HERE/System Overview.md`, `01 - Architecture/Architecture Overview.md`, `01 - Architecture/Data Flow.md`, `01 - Architecture/Shutdown & Recovery.md`, `01 - Architecture/Startup Sequence.md`, `02 - Modules/[FileName].md` — ONE PER SOURCE FILE (+22 more)

### Community 481 - "Plan: AgentShroud Security Hardening — Real Agent Containment"
Cohesion: 0.08
Nodes (37): Changes, Changes, Changes, Changes, Changes, Changes, Context, Execution Order & Parallelism (+29 more)

### Community 482 - "REQUIRED NOTES — PRODUCE EVERY ONE OF THESE"
Cohesion: 0.07
Nodes (30): `00 - START HERE/Home.md`, `00 - START HERE/Quick Reference.md`, `00 - START HERE/System Overview.md`, `01 - Architecture/Architecture Overview.md`, `01 - Architecture/Data Flow.md`, `01 - Architecture/Shutdown & Recovery.md`, `01 - Architecture/Startup Sequence.md`, `02 - Modules/[FileName].md` — ONE PER SOURCE FILE (+22 more)

### Community 483 - "Required: ≥ 4.5 for text, ≥ 3.0 for UI elements"
Cohesion: 0.11
Nodes (18): Anti-Patterns to Flag, Brand Audit Checklist, Brand System Components, Color Token Definition, Core Discipline: Audit → Define → Apply → Enforce, Deck / Slide Master Rules, Dependencies, Diagram Theme Block (Mermaid) (+10 more)

### Community 484 - "3. AWS API MCP Authentication Reset"
Cohesion: 0.14
Nodes (15): 1. GitHub MCP Authentication Reset, 2. Atlassian MCP Authentication Reset, 3. AWS API MCP Authentication Reset, Authentication Reset Procedures, If Using SSO, Manual Re-authentication, Option A: Default AWS Profile, Option B: Named Profile (+7 more)

### Community 485 - "Skill: MCP Doctor (MCPM-DOCTOR)"
Cohesion: 0.11
Nodes (18): 1. Check MCP Configuration, 2. Test GitHub MCP Server, 3. Test Atlassian MCP Server, 4. Test AWS API MCP Server, Common Issues & Fixes, Diagnostic Capabilities, Diagnostic Workflow, Issue: "Atlassian OAuth token expired" (+10 more)

### Community 486 - "Skill: Project Management (PM)"
Cohesion: 0.11
Nodes (18): Assigning Work, CHANGELOG.md Updates, Continuity Files, Definition of Done (from CLAUDE.md), Escalation, Known Risks, Project Roadmap, Quick Status (for chat/Telegram) (+10 more)

### Community 487 - "Audit Ledger (SHA-256 hash only)"
Cohesion: 0.11
Nodes (21): SSH Proxy, 1Password (op-proxy), agentshroud-config volume (openclaw.json), Anthropic API, Approval Queue (human gate), Audit Ledger (SHA-256 hash only), Cron Scheduler (8 scheduled jobs), Execute Action (tool call / reply) (+13 more)

### Community 488 - "setup-secrets.sh"
Cohesion: 0.17
Nodes (29): cmd_dump_op_refs(), cmd_edge_ensure(), cmd_edge_init(), cmd_extract(), cmd_help(), cmd_interactive(), cmd_migrate(), cmd_store() (+21 more)

### Community 489 - "ManifestEntry"
Cohesion: 0.23
Nodes (6): ManifestEntry, Path, A single item in the skills manifest., Build a ManifestEntry by reading *path* from disk., _sha256(), TestManifestEntry

### Community 490 - "AgentShroud Phase Review — 2026-02-24-final"
Cohesion: 0.07
Nodes (29): 1. Accomplishments This Phase — Delivered Security Infrastructure, 2. Security Value Audit — Real Protection vs. Theater Assessment, 3. Remaining Work — Prioritized by Security Value, 4. Risks & Gaps — Critical Security Concerns, 5. Strategic Recommendations, 6. Conclusion — Mission-Critical Security Infrastructure Delivered, AgentShroud Phase Review — 2026-02-24-final, 📋 **Architecture Evolution (Next Quarter)** (+21 more)

### Community 491 - "AgentShroud Data Dictionary"
Cohesion: 0.11
Nodes (17): AgentShroud Data Dictionary, ApprovalRequest, AuditEntry, Core Audit Entities, Data Classification, Data Retention Policies, DNSQuery, InspectionResult (+9 more)

### Community 492 - "model_usage.py"
Cohesion: 0.23
Nodes (19): date, aggregate_costs(), build_json_all(), build_json_current(), eprint(), filter_by_days(), latest_day_cost(), load_payload() (+11 more)

### Community 493 - "02-infrastructure.md"
Cohesion: 0.11
Nodes (17): 4. Infrastructure Diagram — Hosting & Servers, 5. Network Topology Diagram, 6. Deployment Diagram — What Runs Where, AgentShroud — Infrastructure & Network Diagrams, 21. Agile Team Diagram — Structure & Roles, 22. Dependency Graph — Component Dependencies, 23. Roadmap / Timeline — Development Phases, AgentShroud — Team, Planning & Dependency Diagrams (+9 more)

### Community 494 - "AWS Cloud Management & FinOps Agent"
Cohesion: 0.06
Nodes (35): AWS Cloud Management & FinOps Agent, Cost Optimization Priority, Cross-Account & Future Proofing, Decision Framework, Deliverables, EBS Performance Analysis (Critical Pattern), Expertise, FY26 Cost Reduction Context (+27 more)

### Community 495 - "Required: ≥ 4.5 for text, ≥ 3.0 for UI elements"
Cohesion: 0.11
Nodes (18): Anti-Patterns to Flag, Brand Audit Checklist, Brand System Components, Color Token Definition, Core Discipline: Audit → Define → Apply → Enforce, Deck / Slide Master Rules, Dependencies, Diagram Theme Block (Mermaid) (+10 more)

### Community 496 - "3. Brutally Honest Self-Assessment"
Cohesion: 0.07
Nodes (29): 1. Accomplishments This Phase (Feb 25 – Mar 3), 2. Security Value Audit, 3. Brutally Honest Self-Assessment, 4. Remaining Work — Prioritized by Value, 5. Risks & Gaps, 6. Go / No-Go Recommendation, AgentShroud Phase Review — 2026-03-03, Are we adding real value? (+21 more)

### Community 497 - "Skill: Project Management (PM)"
Cohesion: 0.11
Nodes (18): Assigning Work, CHANGELOG.md Updates, Continuity Files, Definition of Done (from CLAUDE.md), Escalation, Known Risks, Project Roadmap, Quick Status (for chat/Telegram) (+10 more)

### Community 498 - "Required: ≥ 4.5 for text, ≥ 3.0 for UI elements"
Cohesion: 0.11
Nodes (18): Anti-Patterns to Flag, Brand Audit Checklist, Brand System Components, Color Token Definition, Core Discipline: Audit → Define → Apply → Enforce, Deck / Slide Master Rules, Dependencies, Diagram Theme Block (Mermaid) (+10 more)

### Community 499 - "Skill: MCP Doctor (MCPM-DOCTOR)"
Cohesion: 0.11
Nodes (18): 1. Check MCP Configuration, 2. Test GitHub MCP Server, 3. Test Atlassian MCP Server, 4. Test AWS API MCP Server, Common Issues & Fixes, Diagnostic Capabilities, Diagnostic Workflow, Issue: "Atlassian OAuth token expired" (+10 more)

### Community 500 - "test_playback_state.c"
Cohesion: 0.15
Nodes (26): face_state_t, ws_vg_state_t, _on_vg_state(), tts_task(), delivery_resume_offset(), delivery_track_sent_ok(), playback_gate_should_open(), wakeword_set_tts_playing() (+18 more)

### Community 501 - "AgentShroud Consolidated Issues Report"
Cohesion: 0.13
Nodes (19): AgentShroud Consolidated Issues Report, 10. Colima VM Internet Connectivity Loss, 11. Missing Test Coverage for Core Modules, 12. PII Redaction Issues, 13. Duplicate Imports & Verbose Pydantic Init, 14. Hardcoded Database Paths, 15. Debug Artifacts in Production Code, 16. Missing Newlines (+11 more)

### Community 502 - "Any"
Cohesion: 0.11
Nodes (16): aggregate_results(), get_clamav_summary(), get_fluent_bit_summary(), get_openscap_summary(), _is_clamd_running(), _is_fluent_bit_running(), Any, Return True if clamd Unix socket /tmp/clamd.ctl is connectable. (+8 more)

### Community 503 - "AgentShroud Development Team — Agile Structure"
Cohesion: 0.11
Nodes (18): AgentShroud Development Team — Agile Structure, Collaborators (Advisory — Read-Only), Communication & Tooling, Container Architecture, Data Engineers / Analysts, Development Environment, Development Team, Development Workflow (+10 more)

### Community 504 - "test_group_isolation.py"
Cohesion: 0.08
Nodes (20): fixture, Content appended to group-B must not appear in group-A memory., Both groups store separate content with no cross-contamination., group-A and group-B memory files must be in separate directories., group-{chat_id} sessions must live under the 'groups' subdirectory., Group workspace content must not leak into any user's DM workspace., Content written to a group must not appear in any user's private DM memory., Content written to a user DM must not appear in any group memory. (+12 more)

### Community 505 - "test_security_integration.py"
Cohesion: 0.09
Nodes (28): approval_queue(), encrypted_store(), ledger(), prompt_guard(), asyncio, fixture, parametrize, Clean message flows through entire pipeline without issues. (+20 more)

### Community 506 - "pick_latest_stable"
Cohesion: 0.11
Nodes (14): 2026.7.1-2 is a patch published after 2026.7.1, so it must win., Pre-release builds must never be shipped to production automatically., 2026.7.1-2' is a real published OpenClaw release, not a prerelease marker — the…, Selecting the newest shippable npm release., The actual npm tail as of 2026-09-15., 2026.10.1' must beat '2026.9.4' — string compare gets this wrong., TestIsStable, TestPickLatestStable (+6 more)

### Community 508 - "TestToolResultSanitizer"
Cohesion: 0.07
Nodes (16): Test detection of blocked patterns in URLs., Test stripping of malicious markdown images., Test stripping of malicious markdown links., Test stripping of links to non-allowlisted domains., Test that legitimate links are preserved., Test that internal/relative links are preserved., Test that code blocks with URLs are preserved., Test handling of images with empty alt text. (+8 more)

### Community 509 - "Sunday Upgrade 2026-11-08 (DEV run, account `agentshroud-bot`)"
Cohesion: 0.09
Nodes (22): 1. Summary line, 1a. Upstream discovery (scripts/discover_upstream_versions.py --json, 2026-11-08 03:0x ET), 2. Environment mapping, 3. Upgrade table, 3a. Per-component change report, 3b. Not updated this run — plan for the week, 4. Security findings, 5. Verification evidence (+14 more)

### Community 510 - "Browser — Secure Browser Automation"
Cohesion: 0.07
Nodes (29): 1. Always Specify Risk Level, 2. Use Allowlisting Liberally, 3. Take Screenshots for Audit Trail, 4. Handle CAPTCHAs Gracefully, 5. Never Extract Credentials, "Action requires approval but none granted", Approval Integration, Audit Logging (+21 more)

### Community 511 - "REQUIRED NOTES — PRODUCE EVERY ONE OF THESE"
Cohesion: 0.07
Nodes (30): `00 - START HERE/Home.md`, `00 - START HERE/Quick Reference.md`, `00 - START HERE/System Overview.md`, `01 - Architecture/Architecture Overview.md`, `01 - Architecture/Data Flow.md`, `01 - Architecture/Shutdown & Recovery.md`, `01 - Architecture/Startup Sequence.md`, `02 - Modules/[FileName].md` — ONE PER SOURCE FILE (+22 more)

### Community 512 - "Browser — Secure Browser Automation"
Cohesion: 0.07
Nodes (29): 1. Always Specify Risk Level, 2. Use Allowlisting Liberally, 3. Take Screenshots for Audit Trail, 4. Handle CAPTCHAs Gracefully, 5. Never Extract Credentials, "Action requires approval but none granted", Approval Integration, Audit Logging (+21 more)

### Community 513 - "REQUIRED NOTES — PRODUCE EVERY ONE OF THESE"
Cohesion: 0.07
Nodes (30): `00 - START HERE/Home.md`, `00 - START HERE/Quick Reference.md`, `00 - START HERE/System Overview.md`, `01 - Architecture/Architecture Overview.md`, `01 - Architecture/Data Flow.md`, `01 - Architecture/Shutdown & Recovery.md`, `01 - Architecture/Startup Sequence.md`, `02 - Modules/[FileName].md` — ONE PER SOURCE FILE (+22 more)

### Community 514 - "Browser — Secure Browser Automation"
Cohesion: 0.07
Nodes (29): 1. Always Specify Risk Level, 2. Use Allowlisting Liberally, 3. Take Screenshots for Audit Trail, 4. Handle CAPTCHAs Gracefully, 5. Never Extract Credentials, "Action requires approval but none granted", Approval Integration, Audit Logging (+21 more)

### Community 515 - "REQUIRED NOTES — PRODUCE EVERY ONE OF THESE"
Cohesion: 0.07
Nodes (30): `00 - START HERE/Home.md`, `00 - START HERE/Quick Reference.md`, `00 - START HERE/System Overview.md`, `01 - Architecture/Architecture Overview.md`, `01 - Architecture/Data Flow.md`, `01 - Architecture/Shutdown & Recovery.md`, `01 - Architecture/Startup Sequence.md`, `02 - Modules/[FileName].md` — ONE PER SOURCE FILE (+22 more)

### Community 516 - "AgentShroud™ — Project Knowledge Base"
Cohesion: 0.07
Nodes (28): About the Creator, AgentShroud™ — Project Knowledge Base, Architecture, Architecture Review, Current Status, Design Philosophy, Development Phases, Documentation & Ideas (+20 more)

### Community 517 - "API Keys Setup Guide"
Cohesion: 0.07
Nodes (28): API Keys Setup Guide, Bot not responding on Telegram, Change Default Model, Check Telegram Channel Status, Container won't start after adding Anthropic secret, Create the Anthropic OAuth Token File, List Available Models, "Missing auth" for a provider (+20 more)

### Community 518 - "Test-Driven Development README"
Cohesion: 0.16
Nodes (17): Branding Specialist Skill (i-bs, external), Test-Driven Development README, Purpose, Related Skills, Test-Driven Development (TDD), Usage, Test-Driven Development (TDD) Coach, Technical Illustrator README (+9 more)

### Community 519 - "test_memory_lifecycle.py"
Cohesion: 0.10
Nodes (19): MemoryIntegrityConfig, MemorySecurityConfig, Create configuration from environment variables., Configuration for memory file integrity monitoring., Combined memory security configuration., ModificationSource, Enum, Source of a file modification. (+11 more)

### Community 520 - "Route map (by router)"
Cohesion: 0.18
Nodes (11): Agent-facing proxy endpoints (not control-plane), Audit / ledger, DNS, Egress control, Health & status, Quarantine, RBAC, Route map (by router) (+3 more)

### Community 521 - "v0.9.0 — "Sentinel" (Blue Team Remediation + Data Isolation + SOC)"
Cohesion: 0.20
Nodes (10): A. Private Service Data Isolation, B. Security Operations Center (SOC), C. Steve Hay Remediation, D. Apple Messages Integration, E. Security Tools (Full Integration, Not Stubs), F. Infrastructure, G. Multi-Agent Architecture, H. Development Infrastructure (+2 more)

### Community 522 - "competitive-report-*.md dated reports"
Cohesion: 0.40
Nodes (11): competitive-analysis.md artifact, competitive-report-*.md dated reports, trend-log.md artifact, OpenClaw cron: Competitive Analysis Email (Afternoon), OpenClaw cron: Competitive Landscape Update (Afternoon), OpenClaw cron: Daily Competitive Analysis Email (AM), OpenClaw cron: Daily Competitive Landscape Update (zero-hallucination sourcing rules), Hermes Competitive Intelligence Email (AM/PM) (+3 more)

### Community 523 - "Approval Queue (human-in-the-loop)"
Cohesion: 0.10
Nodes (34): Approval Queue (human-in-the-loop), SHA-256 content hashing (original_content_hash + sanitized content_hash), OpenClaw auto-compaction (reserveTokensFloor=4000; triggers at ~196K of 200K tokens; hard overflow >200K after 3 failed retries → session reset), ledger.db — audit ledger (Layer 3 persistence; hash-only, 90-day retention, auto-purge at expires_at), MCP Inspector (injection scan, PII scan, sensitive-op scan; ThreatLevel NONE/LOW/MEDIUM/HIGH), PII Redaction (Presidio-style pattern matching: PHONE_NUMBER, EMAIL_ADDRESS, SSN, etc.), Layer 5 — Consumption (auto-delete at expires_at, audit query, user response), Data Lineage Diagram (5-Layer Pipeline) (+26 more)

### Community 524 - "AgentShroud Schema Documentation"
Cohesion: 0.11
Nodes (17): AgentShroud Schema Documentation, Approval Queue Schema, Audit Chain State, Configuration File Schemas, Database Connection Configuration, Docker Secrets Structure, Egress Configuration (egress-config.yml), In-Memory Data Structures (+9 more)

### Community 525 - "Phase 1 — Raw Collection"
Cohesion: 0.11
Nodes (18): 10. Spotlight Catch-All, 1. System Profiler (most comprehensive single source), 2. Applications Folders (catch drag-and-drop installs), 3. Homebrew (formulae + casks), 4. Mac App Store (via `mas` CLI), 5. Setapp Detection, 6. Package Receipts (direct .pkg installs), 7. CLI Tools & Utilities (non-.app installs) (+10 more)

### Community 526 - "AgentShroud Red Team Adversarial Tester"
Cohesion: 0.11
Nodes (17): Adversary Model, AgentShroud Red Team Adversarial Tester, Attack Phases, Attack Techniques Reference, Coverage Requirements, Critical Rules, Infrastructure, Key Principle (+9 more)

### Community 527 - "Socrates — Dialogue Architect"
Cohesion: 0.11
Nodes (17): Dialogue Adaptations, Dialogue Techniques, ElevenLabs v3 Audio Tags, Episode Closing (Mandatory for OKE), EXPERT, Expert Persona, HOST, Input Requirements (+9 more)

### Community 528 - "AgentShroud Red Team Adversarial Tester"
Cohesion: 0.11
Nodes (17): Adversary Model, AgentShroud Red Team Adversarial Tester, Attack Phases, Attack Techniques Reference, Coverage Requirements, Critical Rules, Infrastructure, Key Principle (+9 more)

### Community 529 - "_run_asgi"
Cohesion: 0.12
Nodes (9): _FakeUpstreamWS, _http_scope(), Drive the canvas ASGI app with scripted receive events; collect sends., Fake upstream WebSocket: yields scripted messages, records sends., _run_asgi(), receive(), TestCanvasHTTP, TestCanvasWebSocket (+1 more)

### Community 530 - "asyncio"
Cohesion: 0.08
Nodes (10): FakeAuditStore, asyncio, Only DENY decisions are persisted to the tamper-evident audit store. ALLOW…, EgressFilter must call notifier when blocking an unknown domain., EgressFilter must NOT notify when domain is allowed., flush_notifications with no notifier set should not crash., test_egress_filter_flush_without_notifier(), test_egress_filter_no_notification_on_allow() (+2 more)

### Community 531 - "TestNewPatternsV080"
Cohesion: 0.12
Nodes (3): Regression guard — fail if patterns drop below 43., Unit tests for the 20 patterns added in v0.8.0 (total: 43)., TestNewPatternsV080

### Community 532 - "read_secret"
Cohesion: 0.10
Nodes (15): Unit tests for gateway.utils.secrets — secret-file reading and normalization.…, Normal single-line value is returned unchanged (modulo outer whitespace)., Single-line value with trailing newline is stripped., CRLF line endings are handled correctly., The exact garbled blob from the marvin-dev bug returns only the real token., When the value has interior blank lines, the last non-empty line is returned., An all-whitespace / blank file returns an empty string., Label + masked preview lines before the real token are discarded. (+7 more)

### Community 533 - "gh-issues — Auto-fix GitHub Issues with Parallel Sub-agents"
Cohesion: 0.11
Nodes (18): gh-issues — Auto-fix GitHub Issues with Parallel Sub-agents, Phase 1 — Parse Arguments, Phase 2 — Fetch Issues, Phase 3 — Present & Confirm, Phase 4 — Pre-flight Checks, Phase 5 — Spawn Sub-agents (Parallel), Phase 6 — PR Review Handler, Results Collection (+10 more)

### Community 534 - "AgentShroud Weekly Upgrade — 2026-09-06"
Cohesion: 0.11
Nodes (18): AgentShroud Weekly Upgrade — 2026-09-06, Application CVE registry (OpenClaw / Hermes agents, per `docs/security/cve-mitigation-matrix.md`), Breaking changes / manual follow-ups, CRITICAL: Docker storage exhausted (live fault, found this run), Environment Mapping, Fresh Trivy scans (run today, CRITICAL+HIGH only, `--scanners vuln`), GitHub-hosted findings, Language dependencies (+10 more)

### Community 535 - "Known Log Messages"
Cohesion: 0.06
Nodes (32): ContextGuard False Positive Collaborator Block, Kill Switch Won't Deactivate Troubleshooting, `[agent/embedded] embedded run agent end: isError=true error=Ollama API stream ended without a final response`, Bot Not Responding to Telegram Messages, ClamAV: `SelfCheck: Database status OK.`, ClamAV: `Socket for clamd not found yet, retrying (N/1800)...`, ClamAV: `WARNING: Can't query current.cvd.clamav.net` / `ERROR: Database update process failed`, Common Issues (+24 more)

### Community 536 - "SecureBrowser Security Policies"
Cohesion: 0.07
Nodes (28): 1. Least Privilege, 2. Defense in Depth, 3. Explicit Over Implicit, 4. Fail Secure, Approval Decision Criteria, Approval Request Format, Approval Workflows, Audit Access (+20 more)

### Community 537 - "Skill Creation Process"
Cohesion: 0.07
Nodes (28): About Skills, Anatomy of a Skill, Assets (`assets/`), Body, Bundled Resources (optional), Concise is Key, Core Principles, Frontmatter (+20 more)

### Community 538 - "Inbound MCP Edge — Agent Coverage and Vendor Onboarding"
Cohesion: 0.07
Nodes (26): 1. First-time enablement (dev first, then prod on the owner's word), 1. Sign the tool descriptors (owner only, interactive terminal), 1a. Claude Duet pilot (prod, owner's Claude account), 2. Create the edge secrets, 2. Killswitch, 3. Rotating keys, 3. Turn the edge on, 4. Enable one vendor (+18 more)

### Community 539 - "AgentShroud Incident Response Plan"
Cohesion: 0.07
Nodes (27): AgentShroud Incident Response Plan, Audit Chain Tampering, Configuration Drift, Contact Information, Container Escape Attempt, Data Exfiltration Detected, Emergency Contacts, Escalation Chain (+19 more)

### Community 540 - "AlertTelegramRelay"
Cohesion: 0.24
Nodes (23): AlertTelegramRelay, Alert → owner Telegram relay (SCRUM-61). Event-bus subscriber that forwards…, Subscribe to the gateway EventBus; relay security alerts to Telegram., _alert_event(), asyncio, Tests for AlertTelegramRelay (SCRUM-61) — security_alert events → owner…, _SendSpy, test_async_sanitizer_supported() (+15 more)

### Community 541 - "_is_op_reference_allowed"
Cohesion: 0.10
Nodes (12): _is_op_reference_allowed(), Return True if the op:// reference matches an allowed path pattern., client(), fixture, Endpoint returns 401 without auth override., Real functional check, not a boot-time smoke test: every op:// reference…, Tests for POST /credentials/op-proxy endpoint (P2: credential isolation)., The vault has no item literally titled "Brave Search API Key" — the real item… (+4 more)

### Community 542 - "AgentShroud Typography Guidelines"
Cohesion: 0.15
Nodes (12): Inter Typeface (Primary), JetBrains Mono Typeface (Monospace), AgentShroud Typography Guidelines, Do's, Don'ts, Font Families, Font Weights, Letter Spacing (+4 more)

### Community 543 - "ToolACLEnforcer"
Cohesion: 0.11
Nodes (13): Enforces tool-level access control based on user role and group membership.…, Public entry — records the decision for the SOC heat-map (SCRUM-80), then…, Check whether user_id may invoke the named tool. Returns: (allowed: bool,…, Check whether user_id may invoke tool_name when acting inside a group…, Authorize a tool call, refusing owner elevation over an unverified origin. WHY…, Return the list of tools the user is allowed to use (union of all sets)., Return tools explicitly denied for this user., Return per-user tool denial counts since last restart (V9-2: SOC correlation). (+5 more)

### Community 544 - "Project Management (SKILL)"
Cohesion: 0.14
Nodes (16): Code Review (i-cr), Production-Ready PR (i-crpr), GitHub Workflow Standards (i-gg), Project Management (PM), Purpose, Related Skills, Usage, Project Management (README) (+8 more)

### Community 545 - "Phase 3: MITIGATE (Rollback First!)"
Cohesion: 0.12
Nodes (16): Follow-up (within 48 hours), Glue Job Rollback, Immediate (within 2 hours), Incident Response Workflow, Phase 1: ASSESS (Max 5 minutes), Phase 2: COMMUNICATE (Concurrent with assess), Phase 3: MITIGATE (Rollback First!), Post-Incident (+8 more)

### Community 546 - "Integration Guide"
Cohesion: 0.08
Nodes (23): AgentShroud v1.3.0, API Reference, Authentication, Error responses, Example: `GET /manage/health`, Example: `POST /manage/egress/{request_id}/approve`, Overview, Source of truth (+15 more)

### Community 547 - "deployment-mode.sh"
Cohesion: 0.23
Nodes (11): deployment_mode_resolve(), deployment_profile_flags(), deployment_runs_edge(), deployment_runs_local_agents(), deployment_up_flags(), deployment-mode.sh script, check(), post-deploy-check.sh script (+3 more)

### Community 548 - "10. Security Supply Chain Analysis"
Cohesion: 0.12
Nodes (18): Cost & timeline (indicative), Readiness assessment — existing controls vs SOC 2 Common Criteria, Recommendation, SOC 2 Type II — Attestation Path & Go/No-Go Scoping, Tracking, What SOC 2 Type II actually requires, Why this is on the board, 10.1 Core Runtime Dependencies (+10 more)

### Community 549 - "Browser — Secure Browser Automation (SKILL)"
Cohesion: 0.19
Nodes (12): SecureBrowser Security Configuration (config.yaml), Browser — Secure Browser Automation (README), SecureBrowser.click(), SecureBrowser.extract(), SecureBrowser.fill_field(), SecureBrowser._log_action(), SecureBrowser._log_security_event(), SecureBrowser.navigate() (+4 more)

### Community 550 - "ServiceManager"
Cohesion: 0.13
Nodes (8): Thin wrapper around the container engine that produces ServiceDescriptors., ServiceManager, _full_inspect_info(), TestDescribeService, TestGetEngine, TestLifecycleActions, Verify ServiceManager can be imported without a running container engine., TestServiceManagerImport

### Community 551 - "Phase 3: MITIGATE (Rollback First!)"
Cohesion: 0.12
Nodes (16): Follow-up (within 48 hours), Glue Job Rollback, Immediate (within 2 hours), Incident Response Workflow, Phase 1: ASSESS (Max 5 minutes), Phase 2: COMMUNICATE (Concurrent with assess), Phase 3: MITIGATE (Rollback First!), Post-Incident (+8 more)

### Community 552 - "Atlas — Curriculum Architect"
Cohesion: 0.12
Nodes (16): Atlas — Curriculum Architect, Coverage Types, CPA Curriculum Frontmatter Addition, Episode Closing, Exam Weight Integration, Gleim Unit Mapping, Input Requirements, Mandatory Acronym Expansion (+8 more)

### Community 553 - "Skill: MCP Auth Reset (MCPM-AUTH-RESET)"
Cohesion: 0.06
Nodes (31): 1. GitHub MCP Authentication Reset, 2. Atlassian MCP Authentication Reset, 3. AWS API MCP Authentication Reset, Atlassian OAuth, Atlassian: "OAuth flow failed", Authentication Reset Procedures, AWS Credentials, AWS: "Token expired" (SSO) (+23 more)

### Community 554 - "TestManifest"
Cohesion: 0.10
Nodes (8): _keypair(), The signed manifest in config/ must describe exactly the shipped descriptors., Owner workflow: keygen | <keychain>; <keychain> | sign — key never in argv or…, _sign(), TestDescriptorShape, TestManifest, TestPublicView, TestSigningCli

### Community 555 - "Currently Unmitigable Residual Class"
Cohesion: 0.14
Nodes (14): Base-Image Change Flagged For Decision, Not Attempted, Currently Unmitigable Residual Class, Hermes Vendored-Base Residual (upstream-owned), Two-Terminal-State Finding Taxonomy, Zeroed .trivyignore (no suppressions), Dev-Side Copy of the 2026-09-06 Report, Sunday Upgrade 2026-09-06 (dev-only scoped run), Dev/Prod Mapping Keyed Off $USER via scripts/asb (+6 more)

### Community 556 - "TestRejected"
Cohesion: 0.10
Nodes (8): _forge(), Algorithm confusion: HMAC 'signed' with the published public key., A correctly signed token the issuer has no record of (e.g. from another…, Sign arbitrary claims with the real key (as if minted outside the issuer)., TestRejected, TestRevocationAndKill, TestValidToken, _token()

### Community 557 - "AlertDispatcher"
Cohesion: 0.05
Nodes (27): AlertDispatcher, Any, Path, Check if alert was already seen within dedup window., Check if we've exceeded the rate limit., Append alert to JSONL log file., POST alert to /api/alerts with bounded retry + backoff. Returns True on first…, Format alert as human-readable message. (+19 more)

### Community 558 - "_make_proxy"
Cohesion: 0.14
Nodes (12): _make_proxy(), _make_update(), Verify suspended users get a drop notice (rate-limited to avoid spam)., Owner messages must never be blocked by the suspension logic., Drive a single owner command through the proxy and capture admin notices., Return a TelegramAPIProxy wired with fake deps (no real HTTP)., capture(), TestLockedCommand (+4 more)

### Community 559 - "ControlCenter"
Cohesion: 0.13
Nodes (15): ANSI, ControlCenter, main(), Clear screen and position cursor at home, Draw main dashboard screen, AgentShroud Text Control Center - Full Terminal TUI Dashboard Usage: python3…, Draw approval queue screen, Draw kill switch screen (+7 more)

### Community 560 - "AgentShroud — Master Feature List (Everything Ever Mentioned)"
Cohesion: 0.12
Nodes (16): A. One-Click Install & Updates, AgentShroud — Master Feature List (Everything Ever Mentioned), AgentShroud Shared Tasks:, AgentShroud Tasks (all overdue, added to v0.8.0):, Apple Reminders — Items Recovered, B. Professional Branded Web Command Center, C. Text/CLI Command Center, Collaborators (+8 more)

### Community 561 - "Skill: Mindmap Architect (MM)"
Cohesion: 0.07
Nodes (26): Anti-Patterns to Flag, Brainstorming Session Map, Core Discipline: Frame → Structure → Generate → Validate, Curriculum Design (with `/i-atlas`), Decision Tree Map, Dependencies, Example: FODL Pipeline Overview, Export and Sharing Conventions (+18 more)

### Community 562 - "Skill: UI Expert (UI)"
Cohesion: 0.07
Nodes (26): Accessibility Requirements, Anti-Patterns to Flag, BEM (Block Element Modifier), Breakpoints (mobile-first), Button, Component contract rules, Component file structure, Component Patterns (+18 more)

### Community 563 - "Implement gateway-level outbound information filtering module"
Cohesion: 0.12
Nodes (16): Constraints, Evidence, Implement gateway-level outbound information filtering module, Problem, Relationship to chunk 00-information-disclosure.md, Remediation, Root Cause, Severity (+8 more)

### Community 564 - "package_skill"
Cohesion: 0.16
Nodes (10): main(), package_skill(), Skill Packager - Creates a distributable .skill file of a skill folder Usage:…, Package a skill folder into a .skill file. Args: skill_path: Path to the skill…, Basic validation of a skill, Quick validation script for skills - minimal version, validate_skill(), Regression tests for skill packaging security behavior. (+2 more)

### Community 565 - "iCloud Services"
Cohesion: 0.07
Nodes (26): "401 Unauthorized", Add Contact, "Calendar/Contacts not found", Calendar Operations, Configuration, "Connection timeout", Contact Operations, Create Event (+18 more)

### Community 566 - "iCloud Services"
Cohesion: 0.07
Nodes (26): "401 Unauthorized", Add Contact, "Calendar/Contacts not found", Calendar Operations, Configuration, "Connection timeout", Contact Operations, Create Event (+18 more)

### Community 567 - "Function Details"
Cohesion: 0.12
Nodes (16): Configuration / Environment Variables, Function Details, Key Classes / Functions, oauth_security.py, OAuthSecurityValidator.create_consent_cookie(client_id, scopes, user_id), OAuthSecurityValidator.__init__(allowed_redirect_uris, require_pkce), OAuthSecurityValidator.record_state_used(state) / check_state_reuse(state), OAuthSecurityValidator.register_known_shared_ids(ids) (+8 more)

### Community 568 - "Function Details"
Cohesion: 0.12
Nodes (15): Configuration / Environment Variables, Function Details, Key Classes / Functions, Purpose, Related, Responsibilities, session_security.py, SessionManager.create_session(ip, user_agent) (+7 more)

### Community 569 - "Skill: Mindmap Architect (MM)"
Cohesion: 0.07
Nodes (26): Anti-Patterns to Flag, Brainstorming Session Map, Core Discipline: Frame → Structure → Generate → Validate, Curriculum Design (with `/i-atlas`), Decision Tree Map, Dependencies, Example: FODL Pipeline Overview, Export and Sharing Conventions (+18 more)

### Community 570 - "Detailed Profiles"
Cohesion: 0.15
Nodes (13): ClamAV — Malware Detection, cryptography (Python) — Encryption Library, Detailed Profiles, Docker Engine, Falco — Runtime Security Monitoring, FastAPI / Starlette / Uvicorn — Web Framework, OpenSCAP — Compliance Scanning, Podman (+5 more)

### Community 571 - "Skill: UI Expert (UI)"
Cohesion: 0.07
Nodes (26): Accessibility Requirements, Anti-Patterns to Flag, BEM (Block Element Modifier), Breakpoints (mobile-first), Button, Component contract rules, Component file structure, Component Patterns (+18 more)

### Community 572 - "iCloud Services"
Cohesion: 0.07
Nodes (26): "401 Unauthorized", Add Contact, "Calendar/Contacts not found", Calendar Operations, Configuration, "Connection timeout", Contact Operations, Create Event (+18 more)

### Community 573 - "Mode A — Single task"
Cohesion: 0.07
Nodes (26): Guardrails, Invocation, Jira ticket — every development batch gets one, Mode A — Single task, Mode B — Comprehensive review sweep, Reviewers and fixer available to you, Role, Skill: OpenClaw Dev Workflow (ODEV) (+18 more)

### Community 574 - "Mode A — Single task"
Cohesion: 0.07
Nodes (26): Guardrails, Invocation, Jira ticket — every development batch gets one, Mode A — Single task, Mode B — Comprehensive review sweep, Reviewers and fixer available to you, Role, Skill: Hermes Dev Workflow (HDEV) (+18 more)

### Community 575 - "LogBuffer"
Cohesion: 0.22
Nodes (5): test_log_buffer_ring(), test_log_buffer_tail(), LogBuffer, Any, Ring buffer for recent log/audit entries.

### Community 576 - "Skill: Mindmap Architect (MM)"
Cohesion: 0.07
Nodes (26): Anti-Patterns to Flag, Brainstorming Session Map, Core Discipline: Frame → Structure → Generate → Validate, Curriculum Design (with `/i-atlas`), Decision Tree Map, Dependencies, Example: FODL Pipeline Overview, Export and Sharing Conventions (+18 more)

### Community 577 - "Mode A — Single task"
Cohesion: 0.07
Nodes (26): Guardrails, Invocation, Jira ticket — every development batch gets one, Mode A — Single task, Mode B — Comprehensive review sweep, Reviewers and fixer available to you, Role, Skill: OpenClaw Dev Workflow (ODEV) (+18 more)

### Community 578 - "Skill: UI Expert (UI)"
Cohesion: 0.07
Nodes (26): Accessibility Requirements, Anti-Patterns to Flag, BEM (Block Element Modifier), Breakpoints (mobile-first), Button, Component contract rules, Component file structure, Component Patterns (+18 more)

### Community 579 - "LOW — Informational"
Cohesion: 0.07
Nodes (26): AgentShroud v0.8.0 — Blue Team Security Assessment (Final), C4: Root Endpoint `/` Exposes System Metrics Without Authentication, C5: `/status` Endpoint Exposes Security Posture Without Authentication, CRITICAL — Must Fix Before Release, Fixes Applied, H4: Docker Network `agentshroud-isolated` Not Actually Isolated, H5: `/dashboard/ws-token` Returns Master Auth Token to Browser, H6: Session Manager Path Traversal via Crafted User ID (+18 more)

### Community 580 - "Apple Services Setup Guide"
Cohesion: 0.07
Nodes (26): Access Pattern, App-Specific Password (if 2FA enabled), 🔐 App-Specific Passwords, Apple ID Creation, 📧 Apple Mail (IMAP/SMTP), Apple Services Setup Guide, 🤖 Bot Integration Plan, CalDAV Server (+18 more)

### Community 581 - "Enterprise Governance Proxy System (invention)"
Cohesion: 0.29
Nodes (7): Competitive Positioning — Proxy-Layer Inversion Differentiator, Human-in-the-Loop Approval Queue, Delegated Authority Model (time-bounded privilege delegation), Enterprise Governance Proxy System (invention), Collaborative Multi-Agent Governance, PII Detection and Redaction Engine, Transparent Interception Architecture

### Community 582 - "MCP AWS Profile Configuration README"
Cohesion: 0.43
Nodes (6): MCP AWS Profile Configuration README, MCP AWS Profile Configuration (MCPM-AWS-PROFILE), Purpose, Related Skills, Usage, MCP AWS Profile Configuration Skill

### Community 583 - "Skill: MCP Auth Reset (MCPM-AUTH-RESET)"
Cohesion: 0.12
Nodes (14): MCP Auth Reset (MCPM-AUTH-RESET), Purpose, Related Skills, Usage, Atlassian OAuth, AWS Credentials, GitHub PAT, Related Skills (+6 more)

### Community 584 - "Patch 1b — _send_to_platform Telegram call site (fixes cron Deliver:telegram bypass)"
Cohesion: 0.17
Nodes (12): Cron Telegram delivery bypassed v1.5.2 base_url patch — fixed via third patch anchor on _send_to_platform, Daily Check-in dumped raw ssh-exec JSON verbatim — rewritten to parse stdout/stderr, dash echo XSI backslash-escape bug — fixed with printf '%s\n', ssh-exec.sh / ssh-write-file.sh fixed-filename race — moved to PID-suffixed files, v1.5.3 Release — Telegram/cron delivery fixes, Patch 1 — _send_telegram signature + Bot() construction (version-tolerant anchors), Patch 1b — _send_to_platform Telegram call site (fixes cron Deliver:telegram bypass), Patch 2 — adapter.py _standalone_send passthrough (+4 more)

### Community 585 - "AgentShroud Branding Assets Index"
Cohesion: 0.17
Nodes (12): AgentShroud Branding Assets Index, 📊 Asset Summary, Assets Needed, 📞 Contact, 📁 Directory Overview, Documentation Needed, Documentation Status, Icon Sets (+4 more)

### Community 586 - "AgentShroud Brand Quick Reference"
Cohesion: 0.12
Nodes (16): Accessibility Checklist, AgentShroud Brand Quick Reference, Common Use Cases, CSS Variables, Dark Mode, ✅ Do, ❌ Don't, Favicon (+8 more)

### Community 587 - "Browser Extension"
Cohesion: 0.12
Nodes (15): browser-extension package.json (Jest test harness), 1. URL Forwarder, 2. Page Clipper, 3. Form Fill Request (Reverse Flow), 4. Tab Session Exporter, 5. Reading List Queue, Browser Extension, Browser Support (+7 more)

### Community 588 - "Contributing to AgentShroud™"
Cohesion: 0.12
Nodes (16): Code of Conduct, Code Style, Contributing to AgentShroud™, Development Setup, Pull Request Process, Questions?, Requirements, Response SLA (+8 more)

### Community 589 - "03-data.md"
Cohesion: 0.11
Nodes (20): 10. Data Dictionary / Catalog Map, 7. Data Flow Diagram — How Data Moves Through the System, 8. Entity Relationship Diagram (ERD), 9. Data Lineage Diagram, AgentShroud — Data Diagrams, 14. Logic Flow / Flowchart — Request Execution, 15. Sequence Diagram — Telegram Message to Response, 16. State Machine Diagram — Approval Queue Item Lifecycle (+12 more)

### Community 590 - "test_dns_canvas_coverage.py"
Cohesion: 0.10
Nodes (18): DatagramTransport, AgentShroud DNS Blocklist — Pi-hole-compatible domain blocking for the gateway.…, main(), parse_domain_name(), AgentShroud DNS Forwarder — Lightweight DNS proxy for gateway container. Routes…, Start the DNS forwarding server with optional blocklist. Returns the transport…, Parse a DNS domain name from wire format, handling compression pointers., start_dns_forwarder() (+10 more)

### Community 591 - "_handle"
Cohesion: 0.31
Nodes (10): _handle(), main(), _pipe(), StreamReader, StreamWriter, Rewrite the Host header to `new_host` and normalize Connection framing.…, Relays 0.0.0.0:HERMES_DASHBOARD_BRIDGE_PORT -> 127.0.0.1:HERMES_DASHBOARD_PORT.…, Read up to the end of the request's header block (\\r\\n\\r\\n). Returns… (+2 more)

### Community 592 - "test_soc_edge.py"
Cohesion: 0.09
Nodes (15): In-memory counters for the Command Center (reset on restart)., VendorStats, client(), edge(), holder(), _no_rows(), _profile(), fixture (+7 more)

### Community 593 - "is_overloaded"
Cohesion: 0.13
Nodes (5): is_overloaded(), Return (True, "<provider>_overloaded") for a provider capacity-error envelope…, SCRUM-60: in-body overload envelopes from OpenAI and Gemini must fail over…, TestIsOverloaded, TestOverloadedMultiProvider

### Community 594 - "AuditStore"
Cohesion: 0.09
Nodes (14): AuditStore, Path, SQLite-backed audit event store with tamper-evident hash chain., Open the database, create the schema, and run column migrations. Initialization…, Close the database connection., Log a new audit event with hash chain integrity. Args: bot_id: Identifier of…, Query audit events with optional filters. Args: bot_id: When set, restricts…, Return the most recent audit entries (alias for query_events with limit). (+6 more)

### Community 595 - "canvas_proxy.py"
Cohesion: 0.14
Nodes (17): _build_proxy_headers(), canvas_proxy_app(), _check_basic_auth(), _check_token_auth(), _handle_http(), _handle_websocket(), Any, Build headers to forward upstream, stripping hop-by-hop and Authorization. (+9 more)

### Community 596 - "TestOAuthInjection"
Cohesion: 0.17
Nodes (9): Path, Verify gateway-side OAuth-token translation for the Anthropic path. Root cause…, inject_headers sets anthropic-beta: oauth-2025-04-20 when Bearer is injected., inject_headers does NOT overwrite an existing Authorization: Bearer token, but…, x-api-key is stripped; Authorization: Bearer and anthropic-beta are added., anthropic-version is required on every /v1/messages call; the gateway adds it…, Caller-supplied anthropic-version (e.g. a newer beta date) must not be…, Existing anthropic-beta values are kept; oauth-2025-04-20 is appended once. (+1 more)

### Community 597 - "test_cron_jobs_prompts.py"
Cohesion: 0.18
Nodes (16): _collab_jobs(), _load_jobs(), Path, SSH config must have a Host *.tail240ea8.ts.net block BEFORE Host * block., Tailnet Host block must route through the gateway CONNECT proxy., Regression tests for cron job prompt content and SSH config. These tests guard…, Every collaborator report prompt must instruct the LLM to avoid 'denied' —…, Every collaborator report prompt must instruct LLM to exclude short UIDs. (+8 more)

### Community 598 - "_get_gmail_app_password"
Cohesion: 0.13
Nodes (15): _get_gmail_app_password(), Read Gmail app password from 1Password using the gateway's cached session., _completed(), CompletedProcess, OP_SESSION is set — primary op read path., Tests for _get_gmail_app_password in gateway/ingest_api/routes/forward.py.…, OP_SESSION absent — must fall back to mounted secrets., Core regression test: empty OP_SESSION must NOT short-circuit the secrets path. (+7 more)

### Community 599 - "check_command"
Cohesion: 0.13
Nodes (10): check_command(), get_env_guard(), Get the global environment guard instance., Check if command execution should be allowed. Args: cmd: Command to check…, Scrub API keys and sensitive patterns from text output. Args: text: Text to…, Environment Leakage Guard - Security Hardening Module Block agent access to…, scrub_output(), Test Environment Leakage Guard. (+2 more)

### Community 600 - "test_edge_profiles.py"
Cohesion: 0.11
Nodes (10): parametrize, A vendor whose custom-MCP support is not confirmed ships with no redirect URI…, Duet, chat and Cowork share one Claude account and client identity, so the edge…, TestDlpFloor, TestFailClosed, TestMonitorMode, TestShippedProfiles, TestValidProfile (+2 more)

### Community 601 - "Deploying AgentShroud on Linux (x86_64 / aarch64)"
Cohesion: 0.12
Nodes (15): 1. Clone the Repository, 2. Install Docker, 3. Set Up Secrets, 4. Configure AgentShroud, 5. Build and Start, 6. Verify, Architecture Notes, Deploying AgentShroud on Linux (x86_64 / aarch64) (+7 more)

### Community 602 - "3. Security Controls"
Cohesion: 0.12
Nodes (16): 3.10 Egress Filtering — Phase 7, 3.11 Drift Detection — Phase 7, 3.12 Container Hardening, 3.13 MCP Proxy Layer — Phase 9, 3.14 Web Traffic Proxy — Phase 10, 3.15 Full Egress Control — Phase 11, 3.1 PII Sanitizer, 3.2 Audit Ledger (+8 more)

### Community 603 - "classify"
Cohesion: 0.13
Nodes (12): TestClassify, _job(), The benign skip alone proves nothing — still need a real success., A benign heartbeat skip must not hide an actual failing job., A job that last succeeded before this boot proves nothing about THIS deploy —…, Tests for scripts/soak_status.py's classify() — the soak-period gate. This gate…, An actively-failing job since redeploy must block soak even if other jobs…, A skip for any OTHER reason (not the known-benign empty-heartbeat- file case… (+4 more)

### Community 604 - "AgentShroud System Status Report"
Cohesion: 0.12
Nodes (16): AgentShroud System Status Report, 📊 Container Status, Critical Issues, 🎯 Current Focus, 📁 Documentation, Features Confirmed Working, iMessage Fix Required, Immediate (Required for Bot to Work) (+8 more)

### Community 605 - "TestFabricatedSecurityNotice"
Cohesion: 0.11
Nodes (13): Test cases for the widened fabricated_security_notice pattern., Original pattern: exact past-tense form., blocking' continuous form., continues blocking' — adverb + gerund form., flagging' gerund form., Possessive form: AGENTSHROUD's behavioral analysis flagging., Standalone 'blocked unauthorized command execution' without AGENTSHROUD prefix., blocking suspicious code execution' variant. (+5 more)

### Community 606 - "AgentShroud Recovery Plan v0.4.0"
Cohesion: 0.12
Nodes (16): 0.1 Code Inventory ✅, 0.2 Current State ✅, 2.1 Top Up Anthropic API Credits, 2.2 Grant iMessage Automation Permission, 2.3 Verify Both Working, 4.1 Remove Obsolete Code/Docs, 4.2 Update README, 4.3 Create CHANGELOG (+8 more)

### Community 607 - "Remediation"
Cohesion: 0.12
Nodes (15): Constraints, Evidence, Problem, Remediation, Root Cause, Severity, Step 1: Define MCP tool risk tiers, Step 2: Configure approval requirements per tier (+7 more)

### Community 608 - "Implement per-user session isolation using Telegram user ID"
Cohesion: 0.12
Nodes (15): Constraints, Evidence, Implement per-user session isolation using Telegram user ID, Problem, Remediation, Root Cause, Severity, Step 1: Add user session registry to the gateway (+7 more)

### Community 609 - "Remediation"
Cohesion: 0.12
Nodes (15): Constraints, Evidence, Problem, Remediation, Remove secret mounts from agent container and implement transparent credential injection, Severity, Step 1: Audit current secret mounts, Step 2: Move all secrets to gateway-only Docker Secrets (+7 more)

### Community 610 - "test_telegram_pipeline.py"
Cohesion: 0.17
Nodes (16): _getUpdates_response(), _make_pipeline_result(), _make_proxy(), _make_update(), asyncio, sendMessageDraft must be suppressed to prevent draft flicker leaks., Integration tests: SecurityPipeline wired into TelegramAPIProxy message paths.…, Build a TelegramAPIProxy with mocked RBAC and rate limiter. RBACConfig and… (+8 more)

### Community 611 - "AgentShroud Sunday Upgrade — 2026-09-14 (dev account, agentshroud-bot@marvin)"
Cohesion: 0.14
Nodes (13): 0. Session context, 1. Bugs found and fixed in the Sunday-upgrade tooling itself, 2. Baseline (captured before any change), 3. Vendor version bumps, 4.1 OpenClaw 2026.9.4 — BLOCKED, root cause fully diagnosed, 4.2 Hermes v0.20.6 — BLOCKED after two real fixes landed, 5. CVE matrix updates, 6. Incident during apply: exit 50, manual recovery required (+5 more)

### Community 612 - "_call_llm_stream"
Cohesion: 0.10
Nodes (25): _mock_llm_stream_resp(), _aiter_lines(), _openai_delta_lines(), Build OpenAI-shaped streaming SSE lines for a sequence of content deltas., Build a mock httpx.Response usable as the yield value of a mocked…, _call_llm_stream posts to /v1/chat/completions with stream:true and yields each…, A final delta with no terminal punctuation is flushed once the SSE stream ends,…, A malformed/unexpected-shape SSE chunk is skipped, not fatal — a good sentence… (+17 more)

### Community 613 - "iCloud Services"
Cohesion: 0.07
Nodes (26): "401 Unauthorized", Add Contact, "Calendar/Contacts not found", Calendar Operations, Configuration, "Connection timeout", Contact Operations, Create Event (+18 more)

### Community 614 - "soc/models.py"
Cohesion: 0.03
Nodes (75): Highest severity across all findings (``NONE`` when clean)., SOC Contributor Manager — wraps RBACConfig + TeamsConfig → ContributorRecord., _role_enum(), collect_recent_events(), from_anomaly_alert(), from_audit_chain_entry(), from_dict(), from_egress_attempt() (+67 more)

### Community 615 - "Skill: Mindmap Architect (MM)"
Cohesion: 0.07
Nodes (26): Anti-Patterns to Flag, Brainstorming Session Map, Core Discipline: Frame → Structure → Generate → Validate, Curriculum Design (with `/i-atlas`), Decision Tree Map, Dependencies, Example: FODL Pipeline Overview, Export and Sharing Conventions (+18 more)

### Community 616 - "Skill: UI Expert (UI)"
Cohesion: 0.07
Nodes (26): Accessibility Requirements, Anti-Patterns to Flag, BEM (Block Element Modifier), Breakpoints (mobile-first), Button, Component contract rules, Component file structure, Component Patterns (+18 more)

### Community 617 - "Skill: Mindmap Architect (MM)"
Cohesion: 0.07
Nodes (26): Anti-Patterns to Flag, Brainstorming Session Map, Core Discipline: Frame → Structure → Generate → Validate, Curriculum Design (with `/i-atlas`), Decision Tree Map, Dependencies, Example: FODL Pipeline Overview, Export and Sharing Conventions (+18 more)

### Community 618 - "Skill: UI Expert (UI)"
Cohesion: 0.07
Nodes (26): Accessibility Requirements, Anti-Patterns to Flag, BEM (Block Element Modifier), Breakpoints (mobile-first), Button, Component contract rules, Component file structure, Component Patterns (+18 more)

### Community 619 - "Security Implementation Verification"
Cohesion: 0.09
Nodes (23): 1. Defense in Depth, 2. Simple Rules Are Secure, 3. Bot's Superior Reasoning, 🏗️ Architecture Overview, ✅ Authoritative Files (Active), 📋 Compliance Checklist, 🔍 Container Status, 📁 Current File Status (+15 more)

### Community 620 - "iCloud Services"
Cohesion: 0.07
Nodes (26): "401 Unauthorized", Add Contact, "Calendar/Contacts not found", Calendar Operations, Configuration, "Connection timeout", Contact Operations, Create Event (+18 more)

### Community 621 - "Security Verification Report"
Cohesion: 0.12
Nodes (16): Conclusion, docker/.gitignore, Emergency Procedures, Gitignore Protection (Multi-Layer), Root .gitignore, Security Guarantees, Security Verification Report, Summary (+8 more)

### Community 622 - "iOS / macOS Shortcuts — Relay to AgentShroud"
Cohesion: 0.12
Nodes (15): Canonical request (copy-paste `curl` to validate before building Shortcuts), Content-type quick reference, Contract verification (automated), iOS / macOS Shortcuts — Relay to AgentShroud, One-time setup (do this first), Recipe A — Share Sheet: text / URL, Recipe B — Siri voice capture ("Hey Siri, send to AgentShroud"), Recipe C — Screenshot relay (OCR text) (+7 more)

### Community 623 - "Skill: Mindmap Architect (MM)"
Cohesion: 0.07
Nodes (26): Anti-Patterns to Flag, Brainstorming Session Map, Core Discipline: Frame → Structure → Generate → Validate, Curriculum Design (with `/i-atlas`), Decision Tree Map, Dependencies, Example: FODL Pipeline Overview, Export and Sharing Conventions (+18 more)

### Community 624 - "Skill: UI Expert (UI)"
Cohesion: 0.07
Nodes (26): Accessibility Requirements, Anti-Patterns to Flag, BEM (Block Element Modifier), Breakpoints (mobile-first), Button, Component contract rules, Component file structure, Component Patterns (+18 more)

### Community 625 - "iCloud Services"
Cohesion: 0.07
Nodes (26): "401 Unauthorized", Add Contact, "Calendar/Contacts not found", Calendar Operations, Configuration, "Connection timeout", Contact Operations, Create Event (+18 more)

### Community 626 - "AgentShroud macOS App Icon (1024x1024, Rounded Squircle)"
Cohesion: 0.10
Nodes (21): AgentShroud App Icon (64x64), AgentShroud macOS App Icon (1024x1024, Rounded Squircle), Agent Isolation Module Badge Icon, Approval Queue Module Badge Icon, Audit Ledger Module Badge Icon, Credential Isolation Module Badge Icon, Drift Detector Module Badge Icon, Egress Filter Module Badge Icon (+13 more)

### Community 627 - "AgentShroud Security Assessment — v0.8.0"
Cohesion: 0.12
Nodes (15): AgentShroud Security Assessment — v0.8.0, CRITICAL-1: `history.env` committed to git with live Telegram credentials, CRITICAL-2: No request body size limits on API models, Critical Findings, Executive Summary, HIGH-1: ML injection classifier is entirely a stub, HIGH-2: Approval queue Telegram notifications unimplemented, HIGH-3: Credential generation in key rotation is a placeholder (+7 more)

### Community 629 - "test-sunday-upgrade-scan.sh"
Cohesion: 0.13
Nodes (18): check(), dev_gate(), lib30(), lib_call(), make_apply_bin(), make_fake_repo(), notify(), restore() (+10 more)

### Community 630 - "ADR-005: SHA-256 Hash Chain Audit Integrity"
Cohesion: 0.17
Nodes (15): ADR-005: SHA-256 Hash Chain Audit Integrity, ADR-005: SHA-256 Hash Chain for Audit Integrity, Consequences, Context, Decision, Hash Chain Structure, Implementation Details, Negative Consequences (+7 more)

### Community 631 - "ADR-001: Transparent Proxy vs Agent Modification"
Cohesion: 0.12
Nodes (15): ADR-001: Transparent Proxy vs Agent Modification, Agent Modification Cons:, Agent Modification Pros:, Consequences, Context, Decision, Implementation Strategy, Key Considerations (+7 more)

### Community 632 - "Skill: Audit Branch (AB) — Merge Regression Detection"
Cohesion: 0.13
Nodes (14): Check A — Substantive change on the losing side?, Check B — Tied to a real ticket?, Check C — Still broken at HEAD (not self-healed)?, Guardrails, Invocation Forms, Jira / PR Comment Format, Role, Skill: Audit Branch (AB) — Merge Regression Detection (+6 more)

### Community 633 - "Skill: Create PR with Pre-Flight Audit (CRPR)"
Cohesion: 0.13
Nodes (14): Guardrails, Invocation, Role, Skill: Create PR with Pre-Flight Audit (CRPR), Step 0 — Pre-flight checks, Step 1 — Check for an in-progress merge, Step 2 — Merge without committing, Step 3 — Audit the pending merge (+6 more)

### Community 634 - "Mode A — Single task"
Cohesion: 0.04
Nodes (46): Guardrails, Invocation, Jira ticket — every development batch gets one, Mode A — Single task, Mode B — Comprehensive review sweep, Reviewers and fixer available to you, Role, Skill: Hermes Dev Workflow (HDEV) (+38 more)

### Community 635 - ".agents/agents/i-tw.md"
Cohesion: 0.08
Nodes (25): Anti-Patterns to Flag, API / Function Reference, Architecture Decision Record (ADR), Changelog Entry, Core Discipline: Understand → Structure → Write → Validate, Dependencies, Document Structure, Document-Type Patterns (+17 more)

### Community 636 - "internal network (isolated, internal:true)"
Cohesion: 0.67
Nodes (3): internal network (isolated, internal:true), openclaw service (proxy mode, internal-only network), wazuh service (proxy-mode HIDS sidecar)

### Community 637 - "Gateway Management/Control-Plane API (v1.3.0)"
Cohesion: 0.11
Nodes (18): ADR-002: Default-Allow with Comprehensive Logging, Gateway Management/Control-Plane API (v1.3.0), gateway/soc/router.py (SOC Shared Command Layer), gateway/web/api.py (Web control center), OpenClaw Integration Guide (v0.9.0), 11. Automated Operations, 11 Cron Jobs, SOC Dashboard (+10 more)

### Community 638 - "Apple Reminders CLI (remindctl)"
Cohesion: 0.13
Nodes (14): Apple Reminders CLI (remindctl), Common Commands, Complete/Delete, Create Reminders, Date Formats, Example: Clarifying User Intent, Manage Lists, Output Formats (+6 more)

### Community 639 - "8. Governance Model"
Cohesion: 0.20
Nodes (10): 8. Governance Model, Branch Protection (belt-and-suspenders), "Get Shit Done" (GSD) Cadence, No Security Theater Rules, Recurring Governance Rituals, No Security Theater (Rule A-E), AgentShroud CLAUDE.md operating rules, Prove the Outcome, Never the Steps (+2 more)

### Community 640 - "1.4 Implementation Plan"
Cohesion: 0.29
Nodes (10): Implementation Plan, Phase 1: Pi Preparation (Prerequisites), Phase 2: Node Pairing, Phase 3: Security Configuration, Phase 4: Skill Development, Phase 5: Distributed Workflows, Workflow 1: Automated Testing on Pi, Workflow 2: Continuous Development (+2 more)

### Community 641 - ".cursor/agents/i-tw.md"
Cohesion: 0.08
Nodes (25): Anti-Patterns to Flag, API / Function Reference, Architecture Decision Record (ADR), Changelog Entry, Core Discipline: Understand → Structure → Write → Validate, Dependencies, Document Structure, Document-Type Patterns (+17 more)

### Community 642 - "Skill: Audit Branch (AB) — Merge Regression Detection"
Cohesion: 0.13
Nodes (14): Check A — Substantive change on the losing side?, Check B — Tied to a real ticket?, Check C — Still broken at HEAD (not self-healed)?, Guardrails, Invocation Forms, Jira / PR Comment Format, Role, Skill: Audit Branch (AB) — Merge Regression Detection (+6 more)

### Community 643 - "Skill: Create PR with Pre-Flight Audit (CRPR)"
Cohesion: 0.13
Nodes (14): Guardrails, Invocation, Role, Skill: Create PR with Pre-Flight Audit (CRPR), Step 0 — Pre-flight checks, Step 1 — Check for an in-progress merge, Step 2 — Merge without committing, Step 3 — Audit the pending merge (+6 more)

### Community 644 - "update-bot-agents.sh"
Cohesion: 0.40
Nodes (4): BOT_CONTAINER, BOT_DEFAULTS_DIR, BOT_LIVE_SKILLS_DIR, update-bot-agents.sh script

### Community 645 - "openclaw/skills/i-tw/SKILL.md"
Cohesion: 0.08
Nodes (25): Anti-Patterns to Flag, API / Function Reference, Architecture Decision Record (ADR), Changelog Entry, Core Discipline: Understand → Structure → Write → Validate, Dependencies, Document Structure, Document-Type Patterns (+17 more)

### Community 646 - "AgentShroud Blue Team Security Auditor"
Cohesion: 0.13
Nodes (14): AgentShroud Blue Team Security Auditor, Audit Procedure, Critical Rules, Heat Map Legend, Infrastructure, Loss Categories, Methodology, Output Format (+6 more)

### Community 647 - "Future Features & Roadmap"
Cohesion: 0.08
Nodes (26): 1.1 Apple Shortcuts Integration (iOS & macOS), 1.2 Gmail Integration with Smart Filtering, 1.3 Telegram Quick Forwarding, 2.1 Hardware Security Key Support, 2.2 Automatic Security Updates, 2.3 Intrusion Detection & Honeypots, 5.1 Calendar Integration (Google Calendar), 5.2 Task Management (Todoist, Things, TickTick) (+18 more)

### Community 648 - "Skill: Audit Branch (AB) — Merge Regression Detection"
Cohesion: 0.13
Nodes (14): Check A — Substantive change on the losing side?, Check B — Tied to a real ticket?, Check C — Still broken at HEAD (not self-healed)?, Guardrails, Invocation Forms, Jira / PR Comment Format, Role, Skill: Audit Branch (AB) — Merge Regression Detection (+6 more)

### Community 649 - "Skill: Create PR with Pre-Flight Audit (CRPR)"
Cohesion: 0.13
Nodes (14): Guardrails, Invocation, Role, Skill: Create PR with Pre-Flight Audit (CRPR), Step 0 — Pre-flight checks, Step 1 — Check for an in-progress merge, Step 2 — Merge without committing, Step 3 — Audit the pending merge (+6 more)

### Community 650 - "AgentShroud Phase Review — 2026-03-05 (Round 2)"
Cohesion: 0.08
Nodes (25): 1. Prior Review Verification, 2. New Blue Team Changes Since Round 1, 3. Round 2 Findings, 4. Security Analysis, 4a. Blue Team Fixes — ✅ EXCELLENT, 4b. Remaining Risk: Tailscale Networking (E1), 4c. Test Coverage Improvements, 5. Summary (+17 more)

### Community 651 - "WebhookReceiver"
Cohesion: 0.13
Nodes (12): Any, Path, Process an incoming webhook through the security pipeline., Prepare payload with session context injection., Extract display name from webhook payload., Receives webhooks and routes them through the security pipeline. In production,…, Extract user ID from webhook payload based on source platform., Extract message text from webhook payload (Telegram format). (+4 more)

### Community 652 - "AuditExporter"
Cohesion: 0.10
Nodes (15): AuditExporter, Export events in Common Event Format (CEF). CEF Format: CEF:Version|Device…, Export events in JSON-LD format with security ontology., Export events in standard JSON format., Exports audit events in various compliance formats., Export audit events in the specified format. Args: start_time: ISO timestamp to…, Test AuditExporter functionality., Test JSON export format. (+7 more)

### Community 653 - "AgentShroud Blue Team Security Auditor"
Cohesion: 0.13
Nodes (14): AgentShroud Blue Team Security Auditor, Audit Procedure, Critical Rules, Heat Map Legend, Infrastructure, Loss Categories, Methodology, Output Format (+6 more)

### Community 654 - "Backup & Restore Runbook — AgentShroud"
Cohesion: 0.13
Nodes (13): Tamper-Evident Audit (SHA-256 Hash Chain), Disaster Recovery Full Rebuild Procedure, Daily Audit Ledger Review, Backup Procedure, Backup & Restore Runbook — AgentShroud, Backup Retention, Daily Automated Backup, Disaster Recovery (Full Rebuild) (+5 more)

### Community 655 - "test_shared_memory.py"
Cohesion: 0.09
Nodes (10): fixture, Tests for gateway/security/shared_memory.py — V9-T1: Group shared memory +…, rbac(), session_mgr(), smm(), TestGroupMemoryReadWrite, TestMergedMemory, TestTopicScopedMemory (+2 more)

### Community 656 - "Docker Commands Reference"
Cohesion: 0.13
Nodes (14): Container management, Container status, Debugging read-only filesystem errors, Docker Commands Reference, Exec into containers, Logs, Networking, OpenClaw CLI commands (run inside agentshroud-bot) (+6 more)

### Community 657 - "i-tw.agent.md"
Cohesion: 0.08
Nodes (25): Anti-Patterns to Flag, API / Function Reference, Architecture Decision Record (ADR), Changelog Entry, Core Discipline: Understand → Structure → Write → Validate, Dependencies, Document Structure, Document-Type Patterns (+17 more)

### Community 659 - "Features"
Cohesion: 0.09
Nodes (21): Dependency Graph, Gateway Module Dependencies, Key Initialization Order (main.py lifespan), Python Package Dependencies, Related Notes, Gateway Startup Initialization Order, 1. Install Dependencies, 2. Configure (+13 more)

### Community 660 - ".omp/agents/i-tw.md"
Cohesion: 0.08
Nodes (25): Anti-Patterns to Flag, API / Function Reference, Architecture Decision Record (ADR), Changelog Entry, Core Discipline: Understand → Structure → Write → Validate, Dependencies, Document Structure, Document-Type Patterns (+17 more)

### Community 662 - ".opencode/agents/i-tw.md"
Cohesion: 0.08
Nodes (25): Anti-Patterns to Flag, API / Function Reference, Architecture Decision Record (ADR), Changelog Entry, Core Discipline: Understand → Structure → Write → Validate, Dependencies, Document Structure, Document-Type Patterns (+17 more)

### Community 663 - "v1.3.0 — Platform Expansion (53 items)"
Cohesion: 0.13
Nodes (15): Advanced Integrations, Browser Extension, Command Center — CLI/TUI (moved from v1.0.0 on 2026-03-20), Full Configuration System, Infrastructure (moved from v0.9.0 on 2026-03-04), Integration Hub, iOS/macOS Shortcuts, Mac Mini Onboarding (+7 more)

### Community 664 - "The 8D Investigation Process"
Cohesion: 0.08
Nodes (24): 8D Root Cause Analysis — Data-Driven Control System Investigation, Agent Interaction Protocol, Architecture Context, Critical Rules, D0 — Planning & Scoping, D1 — Team & Expertise Identification, D2 — Problem Description (Data Collection & Characterization), D3 — Interim Containment Assessment (+16 more)

### Community 665 - "The 8D Investigation Process"
Cohesion: 0.08
Nodes (24): 8D Root Cause Analysis — Data-Driven Control System Investigation, Agent Interaction Protocol, Architecture Context, Critical Rules, D0 — Planning & Scoping, D1 — Team & Expertise Identification, D2 — Problem Description (Data Collection & Characterization), D3 — Interim Containment Assessment (+16 more)

### Community 666 - ".new"
Cohesion: 0.17
Nodes (22): approvals_list_empty(), approvals_list_errors_on_401(), approvals_list_formats_rows(), approve_sends_correct_body_and_path(), cves_counts_array_when_no_total(), cves_formats_summary(), cves_reads_nested_summary(), cves_reads_summary_total_fallback() (+14 more)

### Community 667 - "The 8D Investigation Process"
Cohesion: 0.08
Nodes (24): 8D Root Cause Analysis — Data-Driven Control System Investigation, Agent Interaction Protocol, Architecture Context, Critical Rules, D0 — Planning & Scoping, D1 — Team & Expertise Identification, D2 — Problem Description (Data Collection & Characterization), D3 — Interim Containment Assessment (+16 more)

### Community 668 - "AgentShroud v0.8.0 "Watchtower" — Execution Summary (Draft)"
Cohesion: 0.08
Nodes (24): 1) v0.8.0 Baseline Delivery (Documented), 2) Additional v0.8.0 Stabilization Work (Current Execution Cycle), 3) Verification Evidence (Current Cycle), 4) v0.8.0 Done Gate — 2026-03-14 Status, 5) Items Still Remaining (Tracked Separately), 5) Notes, 6) Owner Readout — Daily Telegram Validation Checklist, A. Startup + baseline (+16 more)

### Community 669 - "Phase 3A/3B Implementation Verification Results"
Cohesion: 0.08
Nodes (24): After Phase 3A/3B, Before Phase 3A, Container Status, Created (4 files), Deployment Readiness, Development Environment, Disconnect Mode, Files Modified/Created (+16 more)

### Community 670 - "Make gateway source code, config, and security policies read-only to the agent"
Cohesion: 0.13
Nodes (14): Constraints, Evidence, Make gateway source code, config, and security policies read-only to the agent, Problem, Remediation, Root Cause, Severity, Step 1: Mount gateway source as read-only Docker volumes (+6 more)

### Community 671 - "AgentShroud Sunday Upgrade Report — 2026-09-20 (PROD run)"
Cohesion: 0.07
Nodes (27): 10. Jira tracking, 11. Verification evidence, 12. Breaking changes / manual follow-ups, 13. Rollback instructions, 14. Time spent, 1. Summary line, 0. Dev handoff check (BLOCKING), AgentShroud Sunday Upgrade — 2026-09-20 (PROD run) (+19 more)

### Community 672 - "parse_clamscan_output"
Cohesion: 0.11
Nodes (6): parse_clamscan_output(), Parse clamscan output into structured results. Args: output: Raw stdout from…, Test container hardening and runtime security., TestContainerSecurity, TestClamAVParser, TestClamAVSummary

### Community 673 - "ServerConfig"
Cohesion: 0.14
Nodes (7): ServerConfig, framework(), fixture, Tests for consent_framework module - MCP server config validation. TDD: Written…, TestEnvironmentValidation, TestServerConfigValidation, TestWhitelistBlacklist

### Community 674 - "LockdownLevel"
Cohesion: 0.16
Nodes (15): _level_for_count(), LockdownAction, LockdownLevel, _max_level(), Enum, str, Apply decay (if enabled) and recompute the principal's level., Return True the first time `level` is reached; mark it as notified. (+7 more)

### Community 675 - "browser_security.py"
Cohesion: 0.13
Nodes (14): browser_security.py, BrowserSecurityGuard.analyze_content(content), BrowserSecurityGuard.analyze_screenshot(image_data), BrowserSecurityGuard.can_enter_credentials(url), BrowserSecurityGuard.check_url_reputation(url), BrowserSecurityGuard.register_screenshot_hook(hook), Function Details, Key Classes / Functions (+6 more)

### Community 676 - "test_tool_acl.py"
Cohesion: 0.12
Nodes (11): Policy configuration for tool ACL enforcement. Loaded from agentshroud.yaml…, ToolACLConfig, enforcer(), _make_rbac(), fixture, Tests for gateway/security/tool_acl.py — V9-T2: Tool-level access control., rbac(), TestClassificationSets (+3 more)

### Community 677 - "SSHResult"
Cohesion: 0.09
Nodes (10): Result of an SSH command execution, Execute a command on a remote host via SSH., SSHResult, cwd is validated and passed to proxy.execute()., cwd with shell metacharacters is rejected before execution., cwd must be an absolute path., Omitting cwd passes cwd=None to proxy.execute()., When require_approval=false, non-auto-approved commands execute directly. (+2 more)

### Community 678 - "._run_proxy"
Cohesion: 0.09
Nodes (7): TestSendTelegramTruncation, _fake_urlopen(), _fake_urlopen(), hermes_dashboard_proxy must relay upstream headers header-by-header. Found on…, TestHermesDashboardProxyHeaders, request(), _FakeResp

### Community 679 - "test_hermes_cron_seed.py"
Cohesion: 0.12
Nodes (24): _injectable_providers(), _parse_cron_names_from_sh(), _parse_job_names_from_yaml(), _parse_seed_cron_calls_from_sh(), SCRUM-81: weekly Jira review cron must exist in both sh and yaml, Sun 09:00., The schedule must be '0 9 * * 0' (Sunday 09:00) in both files., Map job name -> the full '_seed_cron "Name" ...' call text (all lines, since…, Validate that init-config.sh cron jobs and jobs.yaml stay in sync. Prevents… (+16 more)

### Community 680 - "TestMetadataGuard"
Cohesion: 0.08
Nodes (12): Test that header sanitization stops at size limit., Test that EXIF metadata is removed from image data., Test that non-EXIF data is preserved., Test comprehensive internal IP pattern matching., Test that all specified unicode control characters are stripped., Test that sensitive headers are stripped., Test that internal IPs are redacted from headers., Test that unicode control characters are stripped. (+4 more)

### Community 681 - "The 8D Investigation Process"
Cohesion: 0.08
Nodes (24): 8D Root Cause Analysis — Data-Driven Control System Investigation, Agent Interaction Protocol, Architecture Context, Critical Rules, D0 — Planning & Scoping, D1 — Team & Expertise Identification, D2 — Problem Description (Data Collection & Characterization), D3 — Interim Containment Assessment (+16 more)

### Community 682 - "The 8D Investigation Process"
Cohesion: 0.08
Nodes (24): 8D Root Cause Analysis — Data-Driven Control System Investigation, Agent Interaction Protocol, Architecture Context, Critical Rules, D0 — Planning & Scoping, D1 — Team & Expertise Identification, D2 — Problem Description (Data Collection & Characterization), D3 — Interim Containment Assessment (+16 more)

### Community 683 - "The 8D Investigation Process"
Cohesion: 0.08
Nodes (24): 8D Root Cause Analysis — Data-Driven Control System Investigation, Agent Interaction Protocol, Architecture Context, Critical Rules, D0 — Planning & Scoping, D1 — Team & Expertise Identification, D2 — Problem Description (Data Collection & Characterization), D3 — Interim Containment Assessment (+16 more)

### Community 685 - "Mode A — Single task"
Cohesion: 0.08
Nodes (23): Guardrails, Invocation, Jira ticket — every development batch gets one, Mode A — Single task, Mode B — Comprehensive review sweep, Reviewers and fixer available to you, Role, Skill: Hermes Dev Workflow (HDEV) (+15 more)

### Community 686 - "Mode A — Single task"
Cohesion: 0.08
Nodes (23): Guardrails, Invocation, Jira ticket — every development batch gets one, Mode A — Single task, Mode B — Comprehensive review sweep, Reviewers and fixer available to you, Role, Skill: OpenClaw Dev Workflow (ODEV) (+15 more)

### Community 687 - "Phase 1 — Raw Collection"
Cohesion: 0.08
Nodes (23): 10. Spotlight Catch-All, 1. System Profiler (most comprehensive single source), 2. Applications Folders (catch drag-and-drop installs), 3. Homebrew (formulae + casks), 4. Mac App Store (via `mas` CLI), 5. Setapp Detection, 6. Package Receipts (direct .pkg installs), 7. CLI Tools & Utilities (non-.app installs) (+15 more)

### Community 688 - "tts.py"
Cohesion: 0.15
Nodes (16): Kaiser-windowed sinc anti-aliasing filter suppresses content above the output…, Frequencies well below the Nyquist (≤3 kHz) must pass through with minimal…, test_resample_antialias_attenuates_above_nyquist(), test_resample_passband_preserved(), test_tts_empty_text_returns_empty(), _get_pipeline(), normalize_for_speech(), Any (+8 more)

### Community 689 - "Feature: Global Monitor-Only Mode ("Observatory Mode")"
Cohesion: 0.13
Nodes (15): API Response, Architecture (high-level), Concept, Concept, Console Management, Design, Estimated Effort, Feature: Global Monitor-Only Mode ("Observatory Mode") (+7 more)

### Community 690 - "OpenSCAP"
Cohesion: 0.17
Nodes (11): Installation in Gateway, Integration Point, Key Commands, OpenSCAP, Purpose, Related Notes, Relationship to Other Security Tools, What It Checks (+3 more)

### Community 691 - "AgentShroud Security Verification (13-check driver)"
Cohesion: 0.43
Nodes (7): toggle-readonly.sh mode switcher, AgentShroud Security Verification (13-check driver), AgentShroud Seccomp Profile (default-deny syscall allowlist), Read-Only Root FS Constraint — what breaks without proper mounts, OpenClaw Volume Architecture (persistent volumes vs tmpfs), Phase 3 Container Security Hardening Baseline, Phase 3 Success Criteria

### Community 692 - "Phase 1 — Raw Collection"
Cohesion: 0.08
Nodes (23): 10. Spotlight Catch-All, 1. System Profiler (most comprehensive single source), 2. Applications Folders (catch drag-and-drop installs), 3. Homebrew (formulae + casks), 4. Mac App Store (via `mas` CLI), 5. Setapp Detection, 6. Package Receipts (direct .pkg installs), 7. CLI Tools & Utilities (non-.app installs) (+15 more)

### Community 693 - "browser-extension/package.json"
Cohesion: 0.13
Nodes (14): description, devDependencies, jest, jest, collectCoverageFrom, testEnvironment, license, name (+6 more)

### Community 694 - "Mode A — Single task"
Cohesion: 0.08
Nodes (23): Guardrails, Invocation, Jira ticket — every development batch gets one, Mode A — Single task, Mode B — Comprehensive review sweep, Reviewers and fixer available to you, Role, Skill: Hermes Dev Workflow (HDEV) (+15 more)

### Community 695 - "Applies to: Claude Code (primary) · Gemini CLI (secondary) · Codex CLI (tertiary)"
Cohesion: 0.04
Nodes (44): 0.05) WEEKLY UPGRADES — UNATTENDED, AND ON DEMAND, 0.0) PROVE THE OUTCOME, NEVER THE STEPS (NON-NEGOTIABLE), 0.1) MULTI-AGENT HIERARCHY, 0) PRIME DIRECTIVE (NON-NEGOTIABLE), 10) CLAUDE CODE OPERATIONAL RULES, 1) PROJECT IDENTITY, 2) ⚠️ NO SECURITY THEATER (NON-NEGOTIABLE), 3) SDLC — HOW TO WORK IN THIS REPO (+36 more)

### Community 697 - "Technical Specification"
Cohesion: 0.14
Nodes (13): API Call Structure, Apollo — Audio Systems Producer, Audio Quality Settings, Error Handling, Input Requirements, Output, Primary API: Text-to-Dialogue, Quality Checklist (+5 more)

### Community 698 - "Technical Specification"
Cohesion: 0.14
Nodes (13): API Call Structure, Apollo — Audio Systems Producer, Audio Quality Settings, Error Handling, Input Requirements, Output, Primary API: Text-to-Dialogue, Quality Checklist (+5 more)

### Community 699 - "Mode A — Single task"
Cohesion: 0.08
Nodes (23): Guardrails, Invocation, Jira ticket — every development batch gets one, Mode A — Single task, Mode B — Comprehensive review sweep, Reviewers and fixer available to you, Role, Skill: OpenClaw Dev Workflow (ODEV) (+15 more)

### Community 701 - "Phase 1 — Raw Collection"
Cohesion: 0.08
Nodes (23): 10. Spotlight Catch-All, 1. System Profiler (most comprehensive single source), 2. Applications Folders (catch drag-and-drop installs), 3. Homebrew (formulae + casks), 4. Mac App Store (via `mas` CLI), 5. Setapp Detection, 6. Package Receipts (direct .pkg installs), 7. CLI Tools & Utilities (non-.app installs) (+15 more)

### Community 702 - "TELEGRAM_ISSUES.md"
Cohesion: 0.09
Nodes (21): agentshroud.yaml Configuration File, ARM64 Seccomp Profile Requirement, Secrets Setup Script (docker/secrets/setup-secrets.sh), Tailscale Remote Access (Pi), Anthropic API Credits Exhausted Blocker, iMessage Automation Permission Blocker, 1Password Session Expiry (op-proxy), Anthropic API Credits & Rate Limits Issue (+13 more)

### Community 703 - "SSH Capability Architecture Document"
Cohesion: 0.18
Nodes (15): API Endpoints (`gateway/ingest_api/main.py`), Approval-Required Commands, Architecture, Auto-Approved Commands, Components, Denied Commands, SSH Capability Architecture Document, Overview (+7 more)

### Community 704 - "AgentShroud -- USPTO Trademark Application"
Cohesion: 0.14
Nodes (13): 1.1 Owner / Applicant, 1.2 Attorney Information, AgentShroud -- USPTO Trademark Application, Filing Reference, Option A: Section 1(a) — Use in Commerce (if mark is already in use), Option B: Section 1(b) — Intent to Use (if not yet in commerce), Recommended Searches, SECTION 10: ESTIMATED COSTS (+5 more)

### Community 705 - "What You Must Do When Invoked"
Cohesion: 0.08
Nodes (23): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Part A - Structural extraction for code files (+15 more)

### Community 706 - "http_proxy.py"
Cohesion: 0.08
Nodes (23): Configuration / Environment Variables, CONNECT Retry Logic, Constructor Parameters, Domain Policy Decision Tree, Function Details, http_proxy.py, `HTTPConnectProxy._agent_id_for_peer(peer)`, `HTTPConnectProxy._clamav_scan_bytes(data: bytes, host: str)` (+15 more)

### Community 707 - "fastapi.md"
Cohesion: 0.03
Nodes (84): FastAPI, Key FastAPI Features Used, Purpose, Related Notes, Where Used, create_auth_dependency(), dependency(), get_auth_dependency() (+76 more)

### Community 708 - "DNSBlocklist"
Cohesion: 0.04
Nodes (26): DNSBlocklist, Path, Parse a single line from a hosts-format or domain-only blocklist. Supports: -…, Parse blocklist text and add domains. Returns count of new domains., Download a blocklist URL. Uses the gateway's own HTTP client., Download all blocklists and rebuild the blocked domains set., Start background task for periodic blocklist updates., Background loop: update blocklists every UPDATE_INTERVAL_SECONDS. (+18 more)

### Community 709 - "._relay"
Cohesion: 0.20
Nodes (9): StreamReader, StreamWriter, Handle a single incoming client connection., Resolve source IP to a bot_id; lazily extends registry via DNS. The startup…, Parse CONNECT request, check allowlist, relay or block., Copy bytes from reader to writer until EOF. ``idle_timeout`` (default 120 s)…, Copy bytes from reader to writer, sampling the first scan_limit bytes for…, Write data to a temp file and scan with ClamAV. Runs in a thread executor so it… (+1 more)

### Community 710 - "sync-llm-settings.sh"
Cohesion: 0.80
Nodes (4): _python(), sync-llm-settings.sh script, _sha256(), _write_manifest()

### Community 711 - "iCloud Services"
Cohesion: 0.07
Nodes (26): "401 Unauthorized", Add Contact, "Calendar/Contacts not found", Calendar Operations, Configuration, "Connection timeout", Contact Operations, Create Event (+18 more)

### Community 712 - "TestAuth"
Cohesion: 0.09
Nodes (10): t_session(), Session, Test authentication and authorization enforcement., Reject JWTs with alg=none (classic attack)., Session must bind to user identity., Different fingerprints should create different sessions., Low-trust agents should be blocked from high-risk actions., Trust should recover after good behavior. (+2 more)

### Community 713 - "GitHub Skill"
Cohesion: 0.14
Nodes (14): API Queries, CI/Workflow Runs, Common Commands, GitHub Skill, Issue Triage, Issues, JSON Output, Notes (+6 more)

### Community 714 - "DNSForwarderProtocol"
Cohesion: 0.15
Nodes (9): DNSForwarderProtocol, UDP protocol handler for DNS forwarding with optional blocklist., _BlockAll, _BlockNone, build_dns_query(), Build a minimal DNS query packet in wire format., Blocklist stub that blocks every domain., Blocklist stub that blocks nothing. (+1 more)

### Community 715 - "Deploying AgentShroud on macOS (Apple Silicon / Intel)"
Cohesion: 0.14
Nodes (13): 1. Clone the Repository, 2. Install Docker Desktop, 3. Set Up Secrets, 4. Configure AgentShroud, 5. Build and Start, 6. Verify, Apple Silicon vs Intel, Deploying AgentShroud on macOS (Apple Silicon / Intel) (+5 more)

### Community 716 - "4. Compliance & Standards Alignment"
Cohesion: 0.22
Nodes (11): 4.1 IEC 62443 (Industrial Automation Security), 4.2 EU AI Act, 4.3 NIST AI Risk Management Framework (AI RMF), 5. Compliance & Standards Alignment, 4. Compliance & Standards Alignment, 4a. OT / Industrial Security (P1 — Critical), 4b. Enterprise IT (P2 — High), 4c. Container & Cloud Security (P2 — High) (+3 more)

### Community 717 - "v1.0.0 "Fortress" — Ship-Ready Public Release (116 items)"
Cohesion: 0.14
Nodes (14): Phase 10: Community & GitHub Setup (10 items), Phase 11: Command Center — Web (11 items), Phase 12: One-Click Install (5 items), Phase 13: Final Hardening + Release (10 items), Phase 1: Security & Secrets (14 items), Phase 2: Repo Hygiene (10 items), Phase 3: Container & Runtime Hardening (11 items), Phase 4: Dependencies (7 items) (+6 more)

### Community 718 - "🟠 HIGH: Security & Logic Issues"
Cohesion: 0.10
Nodes (24): 4. Function Call Exposure (XML Leak), 5. `main.py` Async Bug in Email Module, 6. SSH Bypass in `is_auto_approved`, 7. CI Safety Issue: Pytest Exit Codes Swallowed, 8. ForwardResponse Type Mismatch, 🟠 HIGH: Security & Core Logic Issues, 10. Seccomp Profile Conflicts (x86_64), 11. Bot Token Migration Confusion (+16 more)

### Community 719 - "._looks_like_safe_collaborator_info_query"
Cohesion: 0.14
Nodes (4): Allow conceptual security/process questions that don't request execution/data…, Probes containing 'how does' should be caught by…, Classifier for conceptual collaborator questions., TestLooksLikeSafeCollaboratorInfoQuery

### Community 720 - "._check_impl"
Cohesion: 0.10
Nodes (12): EgressAttempt, Get effective policy for an agent., Public entry — records the decision for the SOC heat-map (SCRUM-80), then…, Check if an outbound connection is allowed. Args: agent_id: The agent making…, Async egress check with interactive approval for unknown domains., Check if domain matches any domain in the allowlist (supports wildcards)., Check if IP matches any IP/CIDR in the list., Check if host looks like an IPv6 address. (+4 more)

### Community 721 - "Flip core security modules from monitor to enforce mode"
Cohesion: 0.14
Nodes (13): Constraints, Evidence, Flip core security modules from monitor to enforce mode, Problem, Remediation, Root Cause, Severity, Step 1: Change default mode in gateway configuration (+5 more)

### Community 722 - "Publish SecureBrowser to ClawHub - Step-by-Step Guide"
Cohesion: 0.14
Nodes (14): Immediate (Day 1), 🎯 Marketing Checklist, Monitor Installations, Month 1, Publish SecureBrowser to ClawHub - Step-by-Step Guide, 🚀 Quick Publish (3 Commands), 💬 Skill Listing Template, ✅ Success Indicators (+6 more)

### Community 723 - "test_soc_services_coverage.py"
Cohesion: 0.15
Nodes (9): _FakeResponse, _frame(), _patch_http_connection(), Build one Docker multiplexed-log frame (stdout)., Coverage tests for gateway/soc/services.py — ServiceManager, socket fallbacks,…, Replace http.client.HTTPConnection so the in-function _UnixHTTP subclass…, TestInspectViaSocket, TestLogsViaSocket (+1 more)

### Community 724 - "TestMultiBotContextvarRouting"
Cohesion: 0.12
Nodes (13): Tests for per-request bot token routing via contextvars. Regression suite for…, Outside a proxy_request call, _active_send_token() returns self._bot_token., When _inbound_bot_token is set, _active_send_token() returns it., Outside a proxy_request call, _active_bot_id() returns 'openclaw'., When _inbound_bot_id is set, _active_bot_id() returns it., _send_telegram_text uses the inbound contextvar token, not self._bot_token., Without contextvar, _send_telegram_text uses self._bot_token., After proxy_request returns, _inbound_bot_token is reset to its prior value. (+5 more)

### Community 725 - "Mode A — Single task"
Cohesion: 0.08
Nodes (23): Guardrails, Invocation, Jira ticket — every development batch gets one, Mode A — Single task, Mode B — Comprehensive review sweep, Reviewers and fixer available to you, Role, Skill: Hermes Dev Workflow (HDEV) (+15 more)

### Community 726 - "AgentShroud Deployment & Troubleshooting Runbook"
Cohesion: 0.14
Nodes (14): AgentShroud Deployment & Troubleshooting Runbook, Architecture Notes, Check Gateway Health, Colima won't start, Container starts but unhealthy, Deploy Latest Code (Any Host), Deploy to Production, Docker says "Cannot connect to Docker daemon" (+6 more)

### Community 727 - "Phase 1 — Raw Collection"
Cohesion: 0.08
Nodes (23): 10. Spotlight Catch-All, 1. System Profiler (most comprehensive single source), 2. Applications Folders (catch drag-and-drop installs), 3. Homebrew (formulae + casks), 4. Mac App Store (via `mas` CLI), 5. Setapp Detection, 6. Package Receipts (direct .pkg installs), 7. CLI Tools & Utilities (non-.app installs) (+15 more)

### Community 729 - "Mode A — Single task"
Cohesion: 0.08
Nodes (23): Guardrails, Invocation, Jira ticket — every development batch gets one, Mode A — Single task, Mode B — Comprehensive review sweep, Reviewers and fixer available to you, Role, Skill: OpenClaw Dev Workflow (ODEV) (+15 more)

### Community 730 - "Mode A — Single task"
Cohesion: 0.08
Nodes (23): Guardrails, Invocation, Jira ticket — every development batch gets one, Mode A — Single task, Mode B — Comprehensive review sweep, Reviewers and fixer available to you, Role, Skill: Hermes Dev Workflow (HDEV) (+15 more)

### Community 731 - "consent_framework.py"
Cohesion: 0.13
Nodes (13): consent_framework.py, ConsentFramework.add_to_blacklist(command) / remove_from_blacklist(command), ConsentFramework.add_to_whitelist(command) / remove_from_whitelist(command), ConsentFramework.validate_config(config), ConsentFramework.validate_configs(configs), Function Details, Key Classes / Functions, Purpose (+5 more)

### Community 732 - "Mode A — Single task"
Cohesion: 0.08
Nodes (23): Guardrails, Invocation, Jira ticket — every development batch gets one, Mode A — Single task, Mode B — Comprehensive review sweep, Reviewers and fixer available to you, Role, Skill: OpenClaw Dev Workflow (ODEV) (+15 more)

### Community 733 - "Phase 1 — Raw Collection"
Cohesion: 0.08
Nodes (23): 10. Spotlight Catch-All, 1. System Profiler (most comprehensive single source), 2. Applications Folders (catch drag-and-drop installs), 3. Homebrew (formulae + casks), 4. Mac App Store (via `mas` CLI), 5. Setapp Detection, 6. Package Receipts (direct .pkg installs), 7. CLI Tools & Utilities (non-.app installs) (+15 more)

### Community 734 - "WS-E Security Audit — AgentShroud v1.2 (Gateway + OpenClaw + Hermes)"
Cohesion: 0.12
Nodes (15): Trust Level, rbac.py (5-level RBAC hierarchy), gateway/proxy/pipeline.py (inbound/outbound guard chain), RT-2 — Inbound Encoding Bypass (FIX-RECOMMENDED), RT-5 — Shared-Memory Write Poisoning (FIX-RECOMMENDED), RT-6 — Owner-Identity Spoofing via /forward body (FIXED), Dead-code / unwired security modules surfaced (No-Security-Theater flags), Executive Summary (+7 more)

### Community 735 - "Mode A — Single task"
Cohesion: 0.08
Nodes (23): Guardrails, Invocation, Jira ticket — every development batch gets one, Mode A — Single task, Mode B — Comprehensive review sweep, Reviewers and fixer available to you, Role, Skill: Hermes Dev Workflow (HDEV) (+15 more)

### Community 736 - "Mode A — Single task"
Cohesion: 0.08
Nodes (23): Guardrails, Invocation, Jira ticket — every development batch gets one, Mode A — Single task, Mode B — Comprehensive review sweep, Reviewers and fixer available to you, Role, Skill: OpenClaw Dev Workflow (ODEV) (+15 more)

### Community 737 - "Phase 1 — Raw Collection"
Cohesion: 0.08
Nodes (23): 10. Spotlight Catch-All, 1. System Profiler (most comprehensive single source), 2. Applications Folders (catch drag-and-drop installs), 3. Homebrew (formulae + casks), 4. Mac App Store (via `mas` CLI), 5. Setapp Detection, 6. Package Receipts (direct .pkg installs), 7. CLI Tools & Utilities (non-.app installs) (+15 more)

### Community 738 - "mcp_oauth_preflight.py"
Cohesion: 0.16
Nodes (20): BaseHTTPRequestHandler, HTTPServer, _CallbackHandler, cmd_oauth(), cmd_reachability(), _dns_lookup(), getenv_required(), _http_request() (+12 more)

### Community 739 - "All Environment Variables"
Cohesion: 0.16
Nodes (15): All Environment Variables, Bot Container (`agentshroud-bot`), Derived (set at runtime by `config.py`), Environment Variable Index, Gateway Container (`agentshroud-gateway`), Loaded at Startup via 1Password op-proxy, Optional / Runtime, Related Notes (+7 more)

### Community 740 - "AgentShroud Documentation"
Cohesion: 0.09
Nodes (23): AgentShroud Documentation, ANNOUNCEMENT.md, Common Issues, CONNECTION-GUIDE.md, Contributing to Documentation, Document Summaries, Documentation Status, Essential Commands (+15 more)

### Community 741 - "Security Audit - One Shroud Over Every Wire"
Cohesion: 0.09
Nodes (22): 1. Filesystem Isolation (EXCEEDS REQUIREMENTS), 2. Network Isolation (EXCEEDS REQUIREMENTS), 3. Process Isolation (EXCEEDS REQUIREMENTS), 4. Resource Limits (PREVENTS DOS), 5. Secrets Management (BEST PRACTICES), 6. Zero-Trust Build (PARANOID MODE), 7. Audit & Monitoring (COMPLIANCE-GRADE), 8. Application Security (DEFENSE IN DEPTH) (+14 more)

### Community 742 - "Claude Code skill catalog (59 skills)"
Cohesion: 0.07
Nodes (30): Agent layer (skills, subagents, orchestration), Nine-stage AI-augmented lifecycle, CDAS — Central Data Acquisition Systems, FODL — Fluence Operational Data Lakehouse, FY26 Cost Reduction Plan (40% target), Claude Code (PRIMARY developer configuration), Codex CLI (TERTIARY agent, TOML config), Configure each tool natively (no config copying) (+22 more)

### Community 743 - "docs/README.md"
Cohesion: 0.09
Nodes (17): Access Points, AI Models, API Keys, Container Management, Files, Most Common Commands, Quick Reference Card, Telegram Bot (+9 more)

### Community 744 - "Skill: Security Review (SEC)"
Cohesion: 0.15
Nodes (12): Anti-Patterns to Flag, Core Principle, Layer 1: Application Security, Layer 2: Container Security, Layer 3: Network Security, Layer 4: Data Flow Security, Output Format, Review Layers (+4 more)

### Community 745 - "Workflow: Survey → Draft → Inject → Confirm"
Cohesion: 0.15
Nodes (12): Re-injection Command (for reference), Role, Rules, Skill: Session Prompt Generator (SESSION-PROMPT), Step 1 — Survey the Repo, Step 2 — Answer Six Questions, Step 3 — Write SESSION_PROMPT.md, Step 4 — Write the File (+4 more)

### Community 746 - "Skill: Test-Driven Development (TDD)"
Cohesion: 0.15
Nodes (12): Anti-Patterns to Flag, Core Discipline: Red → Green → Refactor, Glue Job Logic  →  test transformations outside Spark, PostgreSQL  →  `SAVEPOINT` + `ROLLBACK`, Python / Boto3 / AWS  →  `moto`, Role, Rules, Skill: Test-Driven Development (TDD) (+4 more)

### Community 747 - "AgentShroud (system, C4 context)"
Cohesion: 0.21
Nodes (13): 1Password Integration (service account), AgentShroud (system, C4 context), Anthropic API (external system), Brave Search API (external system), External Collaborators, GitHub (external system), Isaiah Jefferson (Architect/Owner), 1Password (credential vault) (+5 more)

### Community 748 - "AgentShroud System Architecture Document (SAD)"
Cohesion: 0.14
Nodes (13): Metrics to Track, Monitoring & Observability, AgentShroud System Architecture Document (SAD), Component Architecture, Core Technologies, Executive Overview, Monitoring and Observability, Network Isolation Benefits: (+5 more)

### Community 749 - "Per-Agent Container Isolation Architecture"
Cohesion: 0.15
Nodes (12): Architecture, Container Configuration, Design Principles, Docker Compose Template, Future Enhancements, Overview, Per-Agent Audit Trails, Per-Agent Container Isolation Architecture (+4 more)

### Community 750 - "Core Components"
Cohesion: 0.15
Nodes (13): 10. Dashboard (WebSocket), 11. Trust Manager, 12. Egress Monitor, 1. Gateway (FastAPI), 2. PII Sanitizer (Presidio + Regex), 3. Audit Ledger (SHA-256 Hash Chain), 4. Approval Queue (SQLite), 5. Kill Switch (3 Modes) (+5 more)

### Community 751 - "main.py"
Cohesion: 0.09
Nodes (23): Approval Router — `gateway/ingest_api/routes/approval.py` (no prefix), Core / Root — main.py, Dashboard API Router — `gateway/web/dashboard_endpoints.py` (prefix `/api`), Dashboard Router — `gateway/ingest_api/routes/dashboard.py` (no prefix), Endpoints, Environment Variables Used, Forward Router — `gateway/ingest_api/routes/forward.py` (no prefix), Health Router — `gateway/ingest_api/routes/health.py` (no prefix) (+15 more)

### Community 753 - "llm_proxy.py"
Cohesion: 0.09
Nodes (22): Buffered streaming filter (`_filter_outbound_streaming`), Claude Opus intercept, Configuration, Constructor dependencies (dependency injection), Environment variables, Failover chain, Failover controls, Failover notifications (+14 more)

### Community 754 - "Mnemosyne — Retention Engineer"
Cohesion: 0.25
Nodes (7): Input Requirements, Mnemosyne — Retention Engineer, Output Format, Persona, Quality Checklist, Role, System Prompt

### Community 755 - "Skill: Security Review (SEC)"
Cohesion: 0.15
Nodes (12): Anti-Patterns to Flag, Core Principle, Layer 1: Application Security, Layer 2: Container Security, Layer 3: Network Security, Layer 4: Data Flow Security, Output Format, Review Layers (+4 more)

### Community 756 - "Workflow: Survey → Draft → Inject → Confirm"
Cohesion: 0.15
Nodes (12): Re-injection Command (for reference), Role, Rules, Skill: Session Prompt Generator (SESSION-PROMPT), Step 1 — Survey the Repo, Step 2 — Answer Six Questions, Step 3 — Write SESSION_PROMPT.md, Step 4 — Write the File (+4 more)

### Community 757 - "Skill: Test-Driven Development (TDD)"
Cohesion: 0.15
Nodes (12): Anti-Patterns to Flag, Core Discipline: Red → Green → Refactor, Glue Job Logic  →  test transformations outside Spark, PostgreSQL  →  `SAVEPOINT` + `ROLLBACK`, Python / Boto3 / AWS  →  `moto`, Role, Rules, Skill: Test-Driven Development (TDD) (+4 more)

### Community 758 - "pipeline.py — Security Pipeline"
Cohesion: 0.09
Nodes (23): `AuditChain`, `AuditChain.append_block()` — Guaranteed Persistence Guarantee, Configuration, CVE Mitigations, Early Return on Block, Fail-Open ClamAV, Guard Presence and Startup Behavior, Important Behaviors (+15 more)

### Community 759 - "EgressTelegramNotifier"
Cohesion: 0.11
Nodes (11): EgressTelegramNotifier, Return the Telegram bot token to use for a given agent_id. If the agent maps to…, Send a request to Telegram Bot API (sync, run in executor)., Async wrapper around sync Telegram API call., Send a plain text message — public transport for other gateway components (e.g.…, Send Telegram message with time-limited approve/deny buttons. Buttons: Allow 1h…, Process inline button callback. Returns action result. Actions: allow_1h,…, Send answerCallbackQuery to dismiss the button loading state. Pass ``token``… (+3 more)

### Community 760 - "TestKillSwitchScript"
Cohesion: 0.09
Nodes (6): fixture, Verify the kill switch script structure and modes., Kill Switch Tests — verify freeze, shutdown, disconnect modes., Kill switch configuration in example configs., TestKillSwitchConfig, TestKillSwitchScript

### Community 761 - "Skill: Test-Driven Development (TDD)"
Cohesion: 0.15
Nodes (12): Anti-Patterns to Flag, Core Discipline: Red → Green → Refactor, Glue Job Logic  →  test transformations outside Spark, PostgreSQL  →  `SAVEPOINT` + `ROLLBACK`, Python / Boto3 / AWS  →  `moto`, Role, Rules, Skill: Test-Driven Development (TDD) (+4 more)

### Community 762 - "Skill: Technical Illustrator (TI)"
Cohesion: 0.09
Nodes (21): Anti-Patterns to Flag, Architecture (C4 / block) — System boundaries and components, ASCII Art (fallback — no renderer available), Brand Theme Block (Mermaid), Core Discipline: Understand → Diagram → Validate → Export, Data Flow — How data moves and transforms, Dependencies, Diagram Types and Data Lakehouse Examples (+13 more)

### Community 764 - "STPA-Sec Analysis of AgentShroud"
Cohesion: 0.12
Nodes (17): Credential Isolation Architecture, Enforce-by-Default Semantics (R-02, R-03), Hay, Enterprise Security Feature Priorities Assessment (2026), Human-in-the-Loop Approval Gating (R-08, R-09), Outbound Information Filter (R-01), Per-User Session Isolation (R-04, R-05), Separation of Privilege (R-06, R-07), STPA-Sec Analysis of AgentShroud (+9 more)

### Community 765 - "Skill: Technical Illustrator (TI)"
Cohesion: 0.09
Nodes (21): Anti-Patterns to Flag, Architecture (C4 / block) — System boundaries and components, ASCII Art (fallback — no renderer available), Brand Theme Block (Mermaid), Core Discipline: Understand → Diagram → Validate → Export, Data Flow — How data moves and transforms, Dependencies, Diagram Types and Data Lakehouse Examples (+13 more)

### Community 766 - "IDENTITY.md - Who I Am"
Cohesion: 0.17
Nodes (10): Competitive Intelligence Protocol, IDENTITY.md - Who I Am, My Owner, My Responsibilities, My Role, Competitive Intelligence Protocol, IDENTITY.md - Who I Am, My Owner (+2 more)

### Community 767 - "AgentShroud Security Scripts Reference"
Cohesion: 0.09
Nodes (21): AgentShroud Security Scripts Reference, Alerting, Automation Examples, Best Practices, CI/CD Integration, Daily Security Check (cron), killswitch.sh, killswitch.sh doesn't confirm (+13 more)

### Community 768 - "SlackAPIProxy"
Cohesion: 0.12
Nodes (11): Return True if channel is a DM with the configured owner. In Slack, DM channels…, Proxy a bot Slack Web API call through the security pipeline. For message-…, POST to https://slack.com/api/<method> with the bot token., Intercept apps.connections.open: rewrite the returned WSS URL to route the…, Pop and return the real WSS URL for a relay token (one-time use). Returns None…, Handle an inbound Slack event payload received via Socket Mode. Called by…, Create a Slack channel for a group. Returns channel_id or None on failure.…, Invite a Slack user to a channel. Returns True on success. (+3 more)

### Community 769 - "AuditEvent"
Cohesion: 0.13
Nodes (11): AuditEvent, Compute SHA-256 hash of event content (excluding hashes)., Compute entry hash including previous hash (chain)., Represents a single audit event. The ``bot_id`` field identifies which bot…, Generate a unique event ID based on timestamp + random., Convert to dictionary representation., Test AuditEvent functionality., Test basic audit event creation. (+3 more)

### Community 770 - "Steps"
Cohesion: 0.15
Nodes (12): 1. Verify CI and update the PR, 2. Merge, 3. Update graphify, 4. Tag and release, 5. Documentation and version visibility, 6. Close Jira, 7. Rebuild/restart prod and dev from main, Guardrails (+4 more)

### Community 771 - "test_image_verifier.py"
Cohesion: 0.17
Nodes (19): Verify an image signature using cosign keyless OIDC verification. Args:…, Verify multiple image signatures concurrently. Returns: Dict mapping image_ref…, verify_image(), verify_images(), _instant_wait_for(), asyncio, verify_images: exception from one task is caught, others continue., Tests for gateway/security/image_verifier.py. Covers: - verify_image: cosign… (+11 more)

### Community 772 - "TestLogSanitizer"
Cohesion: 0.15
Nodes (5): install_log_sanitizer(), Install the log sanitizer on all existing loggers., Log Sanitizer - Security Hardening Module Scrubs PII, credentials, and…, Test Log Sanitizer - verify PII and credential scrubbing from log output., TestLogSanitizer

### Community 773 - "Fixed"
Cohesion: 0.14
Nodes (15): [0.5.0] - 2026-02-21, [1.2.0] — feat/esp32-s3-hermes-voice (2026-06-24), [1.6.0] (2026-08-28), Added, Added, Added, Agent Routing (P0), Fixed (+7 more)

### Community 774 - "OAuthSecurityValidator"
Cohesion: 0.14
Nodes (8): ConfusedDeputyError, OAuthError, OAuthSecurityValidator, PKCEViolation, Exception, OAuth Security Module - Prevents confused deputy attacks on MCP OAuth proxy…, RedirectMismatch, TestRedirectURI

### Community 775 - "test_adversarial_injection.py"
Cohesion: 0.13
Nodes (15): _any_detector_fires(), _heuristic_detects(), _normalizer_transforms(), _prompt_guard_detects(), Return True if PromptGuard assigns a non-zero score or blocks., Return True if HeuristicClassifier flags as injection or uncertain., Return True if InputNormalizer changes the text (encoding detected)., Combined: detected if ANY defense layer triggers. (+7 more)

### Community 776 - "TestAgentsRegistry"
Cohesion: 0.13
Nodes (3): _bot(), _rows(), TestAgentsRegistry

### Community 777 - "export-bot-conversations.py"
Cohesion: 0.15
Nodes (22): Why exec cat replaced docker cp for reading container files, _docker_read_file(), export_hermes(), export_openclaw(), _extract_text(), main(), _parse_since(), datetime (+14 more)

### Community 778 - "TestSSRFDetection"
Cohesion: 0.09
Nodes (4): SSRF blocking — the one hard block., 2130706433 = 127.0.0.1 in decimal., 0x7f000001 = 127.0.0.1 in hex., TestSSRFDetection

### Community 779 - "Skill: Technical Illustrator (TI)"
Cohesion: 0.09
Nodes (21): Anti-Patterns to Flag, Architecture (C4 / block) — System boundaries and components, ASCII Art (fallback — no renderer available), Brand Theme Block (Mermaid), Core Discipline: Understand → Diagram → Validate → Export, Data Flow — How data moves and transforms, Dependencies, Diagram Types and Data Lakehouse Examples (+13 more)

### Community 780 - "Skill: Technical Illustrator (TI)"
Cohesion: 0.09
Nodes (21): Anti-Patterns to Flag, Architecture (C4 / block) — System boundaries and components, ASCII Art (fallback — no renderer available), Brand Theme Block (Mermaid), Core Discipline: Understand → Diagram → Validate → Export, Data Flow — How data moves and transforms, Dependencies, Diagram Types and Data Lakehouse Examples (+13 more)

### Community 781 - "AgentShroud v0.8.0 — Peer Review Round 3 (FINAL)"
Cohesion: 0.17
Nodes (14): AgentShroud v0.8.0 — Peer Review Round 3 (FINAL), Architecture Review (Positive Observations), Prior Findings — Verification, R1 Findings (all verified fixed in R2), R2 Findings (all verified fixed), R3 Findings (NEW — this round), R3-W1 — WARNING: Stale version string in control page HTML, R3-W2 — WARNING: Stale OCI label version in Dockerfile (+6 more)

### Community 782 - "Critical Findings"
Cohesion: 0.12
Nodes (16): 1. ContextGuard NEVER BLOCKS (Severity: HIGH), 2. Regex-Only Detection (Severity: MEDIUM-HIGH), 3. No Cross-Turn Analysis (Severity: HIGH), 4. No Semantic Understanding (Severity: MEDIUM), Critical Findings, Current Defenses (3 Layers), Layer 1: PromptGuard (11 regex patterns) — P0, ACTIVE, Layer 2: ContextGuard (23 patterns + session tracking) — P1, ACTIVE (+8 more)

### Community 783 - "Skill: Technical Illustrator (TI)"
Cohesion: 0.09
Nodes (21): Anti-Patterns to Flag, Architecture (C4 / block) — System boundaries and components, ASCII Art (fallback — no renderer available), Brand Theme Block (Mermaid), Core Discipline: Understand → Diagram → Validate → Export, Data Flow — How data moves and transforms, Dependencies, Diagram Types and Data Lakehouse Examples (+13 more)

### Community 784 - "What You Must Do When Invoked"
Cohesion: 0.10
Nodes (20): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Step 0 - GitHub repos and multi-path merge (only if a URL or several paths) (+12 more)

### Community 786 - "Pre-Deployment Checklist"
Cohesion: 0.10
Nodes (20): 1. Change Documentation, 2. Testing Evidence, 3. Backups & Rollback, 4. Blast Radius, 5. Observability, 6. Security, 7. Communication, 8. Service Control Commands (+12 more)

### Community 787 - "update-conduit-push.sh"
Cohesion: 0.32
Nodes (12): die(), install_ref(), installed_ref(), installed_status(), installed_version(), own_plugin_files(), pin(), pulse_state() (+4 more)

### Community 788 - "What You Must Do When Invoked"
Cohesion: 0.10
Nodes (20): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Step 0 - GitHub repos and multi-path merge (only if a URL or several paths) (+12 more)

### Community 789 - "Pre-Deployment Checklist"
Cohesion: 0.10
Nodes (20): 1. Change Documentation, 2. Testing Evidence, 3. Backups & Rollback, 4. Blast Radius, 5. Observability, 6. Security, 7. Communication, 8. Service Control Commands (+12 more)

### Community 790 - "Pre-Deployment Checklist"
Cohesion: 0.10
Nodes (20): 1. Change Documentation, 2. Testing Evidence, 3. Backups & Rollback, 4. Blast Radius, 5. Observability, 6. Security, 7. Communication, 8. Service Control Commands (+12 more)

### Community 791 - "1. Accomplishments This Phase"
Cohesion: 0.10
Nodes (20): 1. Accomplishments This Phase, 2. Security Value Audit — Genuine Protection vs. Security Theater, 3. Remaining Work — Prioritized by Value, 4. Risks & Gaps, AgentShroud Phase Review — 2026-02-24-b, 🎯 **Binary Detection & Graceful Degradation**, 📊 **Complete Security Module Integration**, **🚨 Critical Risks** (+12 more)

### Community 792 - "Findings"
Cohesion: 0.10
Nodes (20): AgentShroud v0.8.0 — Blue Team Security Assessment, C1: Hardcoded Owner User ID in middleware.py:94, C2: Hardcoded Owner User ID in webhook_receiver.py:45, C3: Bot Tokens Partially Exposed in Chat History, CRITICAL — Must Fix Before Release, Findings, H1: Telegram Proxy middleware_manager Never Initialized, H2: FileSandbox _extract_file_paths Regex Too Broad (+12 more)

### Community 793 - "Blue Team Security Assessment — AgentShroud v0.8.0 Round 3 (Final)"
Cohesion: 0.10
Nodes (20): Blue Team Security Assessment — AgentShroud v0.8.0 Round 3 (Final), Executive Summary, "Final" Assessment Findings, Fixes Applied, LOW Findings, MEDIUM Findings, Overall Security Posture: **STRONG** 🟢, R3-L1: No Global Security Headers Middleware (Reopened from R2-L1) (+12 more)

### Community 794 - "jira_dev_ticket.py"
Cohesion: 0.08
Nodes (39): add_comment(), _adf_doc(), _auth_headers(), _build_arg_parser(), build_basic_auth_header(), build_comment_payload(), build_comment_url(), build_create_issue_payload() (+31 more)

### Community 795 - "env_guard.py"
Cohesion: 0.10
Nodes (20): Blocked Command Patterns (via `_contains_env_access_patterns`), Blocked Commands, Blocked Paths, check_command(cmd), env_guard.py, Environment Variables, EnvironmentGuard.check_command_execution(command, agent_id), EnvironmentGuard.check_file_access(file_path, agent_id) (+12 more)

### Community 796 - "._is_valid_domain_name"
Cohesion: 0.17
Nodes (3): Validate normalized domain labels to avoid malformed allowlist entries., Unit tests for domain validator used by egress approval flow., TestDomainValidationHelper

### Community 797 - "AgentShroud™ v0.8.0 "Watchtower" — Complete Feature List"
Cohesion: 0.08
Nodes (26): A. Steve Hay Requirements — ALL Tiers (14 features), AgentShroud™ v0.8.0 "Watchtower" — Complete Feature List, B. Wire ALL Modules Into Request Path (14 features), C. Bug Fixes (9 items), D. Interactive Egress Firewall (7 features), E. Observatory Mode (6 features), F. Prompt Injection Hardening (8 features), G. Pi-hole DNS Stack (9 features) (+18 more)

### Community 798 - "Local LLM Support — Implementation Review"
Cohesion: 0.14
Nodes (13): 10. Known Gaps / Open Items, 11. Quick Reference — Switching to Local Mode, 1. Architecture Overview, 2. Source Files, 3. How Provider Detection Works (`llm_proxy.py:95-153`), 5. Model Switching CLI (`scripts/switch_model.sh`), 6. Three Local Backends, 7. Test Coverage (`gateway/tests/test_llm_proxy.py`) (+5 more)

### Community 799 - "ConsentFramework"
Cohesion: 0.13
Nodes (8): ConfigValidationError, ConsentDecision, ConsentFramework, Exception, Consent Framework Module - Pre-configuration consent for MCP server…, Validate a server configuration before execution., ShellInjectionDetected, TestConsentDecision

### Community 800 - "CredentialInjector"
Cohesion: 0.11
Nodes (10): CredentialInjector, Register default domain → credential mappings., Load credential values from Docker Secrets directory., Inject credentials into request headers based on destination domain. Args:…, Check if we have a loaded credential for a domain., Scan outbound content for credential patterns. Returns description of detected…, Return all loaded credential values for use in outbound scrubbing…, Return status for /manage/modules endpoint. (+2 more)

### Community 801 - "asyncio"
Cohesion: 0.15
Nodes (8): asyncio, Verify per-bot filtering in AuditStore (v1.1.0 multi-bot support)., Opening a pre-migration DB (no bot_id column) should auto-migrate., verify_hash_chain(start_id=X) anchors on X's predecessor (SCRUM-204)., Rewriting the first examined row's prev_hash must not be self-anchoring., After the head is archived, the archived predecessor's entry_hash is the anchor., TestAuditStoreAnchoredVerify, TestAuditStoreBotId

### Community 802 - "TestEmailSend"
Cohesion: 0.10
Nodes (11): Missing 'subject' or 'body' returns 422., Missing 'to' field returns 422., Endpoint returns 401 without auth override., Email to an allowed recipient returns 200 with status=approved., Approved response includes sanitized_body field., Allowed (owner) recipient receives the body verbatim — PII scan is skipped. The…, PII in email body IS redacted before queuing for unknown recipients., Unknown recipient triggers approval queue and returns 202. (+3 more)

### Community 803 - "Technical Illustrator (i-ti)"
Cohesion: 0.22
Nodes (11): Mindmap Architect (MM), Purpose, Related Skills, Technical Illustrator (TI), Usage, Technical Illustrator (i-ti), Technical Writing (i-tw), Purpose (+3 more)

### Community 804 - "iMessage Integration Status"
Cohesion: 0.17
Nodes (11): BlueBubbles (native macOS iMessage relay), Current Configuration, Current State: Partially Working, Current Status Summary, iMessage Integration Status, Next Steps, Option 1: Grant Permissions (NOT RECOMMENDED - Won't Work from Container), Option 2: Use BlueBubbles (RECOMMENDED ✅) (+3 more)

### Community 805 - "Trademark Statements"
Cohesion: 0.20
Nodes (10): AgentShroud Bot Capabilities, Option 1 — Professional (email, formal), Option 2 — Compact (Telegram, Slack — default), Option 3 — Full Collaborator Notice (first contact only), Rules, Trademark Statements, Which statement to use, Docker Compose Override — Raspberry Pi Bot Host (+2 more)

### Community 806 - "Credential Management - 1Password Integration"
Cohesion: 0.17
Nodes (12): Advanced 1Password Access, Available Commands, 🔴 Chat Interfaces (NEVER display credentials), 🟢 Console Commands (ALWAYS display), Credential Management - 1Password Integration, 🟢 Internal Use (ALWAYS allowed), Security Decision Tree, Security Rules (Ultra-Conservative) (+4 more)

### Community 807 - "Credential Isolation — Gateway op-proxy (ACTIVE)"
Cohesion: 0.15
Nodes (13): Allowlist, Already in your environment at startup, Credential flow, Credential Isolation — Gateway op-proxy (ACTIVE), How to retrieve a credential, Known working credentials, What NEVER to do, 🏗️ Credential Architecture — How Secrets Are Retrieved (+5 more)

### Community 809 - "test_check_benchmark_regression.py"
Cohesion: 0.21
Nodes (19): _current(), parametrize, The shipped baseline must carry every mean key the checker gates on., Tests for scripts/check_benchmark_regression.py (SCRUM-201). The checker used…, _run(), test_baseline_missing_mean_key_exits_nonzero(), test_batch_metric_regression_exits_nonzero(), test_empty_current_file_exits_nonzero() (+11 more)

### Community 810 - "Athena — Knowledge Distiller"
Cohesion: 0.17
Nodes (11): Athena — Knowledge Distiller, cheatsheet.md, <description of what this does>, Input Requirements, Output Format, Persona, Quality Checklist, Role (+3 more)

### Community 811 - "GSDE&G Development Master Checklist"
Cohesion: 0.17
Nodes (11): Emergency Hotfix, GSDE&G Development Master Checklist, Phase 1 · Plan & Branch  → `gg/SKILL.md`, Phase 2 · TDD  → `tdd/SKILL.md`, Phase 3 · QA  → `qa/SKILL.md`, Phase 4 · Code Review  → `cr/SKILL.md`, Phase 5 · Pull Request  → `pr/SKILL.md`, Phase 6 · CI  → `cicd/SKILL.md` (+3 more)

### Community 812 - "Athena — Knowledge Distiller"
Cohesion: 0.17
Nodes (11): Athena — Knowledge Distiller, cheatsheet.md, <description of what this does>, Input Requirements, Output Format, Persona, Quality Checklist, Role (+3 more)

### Community 813 - ".test_gives_up_and_marks_sent_after_max_retries"
Cohesion: 0.11
Nodes (5): A failed send retries (bounded) within the same day, not next-day., After the retry cap, the day IS marked done so the loop moves on., TestCveReportSchedulerRetry, _fake_run(), TestTrivySkipDirs

### Community 815 - "ledger row (id, timestamp, source, hashes, sanitized flag, expires_at)"
Cohesion: 0.20
Nodes (12): Audit query GET /ledger (hashes only), content_hash = SHA-256(sanitized), ledger row (id, timestamp, source, hashes, sanitized flag, expires_at), LLM API call (sanitized text only), original_content_hash = SHA-256(raw), PII Redaction ([PHONE_NUMBER], [EMAIL_ADDRESS], [SSN]), Response to user (Telegram / iMessage), Auto-delete at expires_at (+4 more)

### Community 816 - "test_dashboard_endpoints.py"
Cohesion: 0.16
Nodes (20): auth_headers(), client(), asyncio, fixture, tail parameter is clamped to 1-100., Tests for dashboard API endpoints: proxy/status, alerts/summary, ssh/hosts,…, When pipeline exists, stats should reflect its data., test_alerts_summary_empty() (+12 more)

### Community 817 - "Red Team Assessment v1.2.0"
Cohesion: 0.26
Nodes (12): AgentShroud Security Inventory v0.8.0 (58 Modules), KeyVault: Zero-Exposure In-Memory Secret Storage, PromptGuard: Prompt Injection Defense (49 Patterns, 35+ Languages), SecurityPipeline: Central Inbound/Outbound Module Orchestrator, TrustManager: Progressive Trust Scoring (5 Levels), Competitive Security Matrix (28 Modules vs 11 Platforms), Security Module 27: Cross-Bot Trust Ledger (v1.2.0), Security Module 28: Differential PII Detector on Tool Results 0.7-floor (v1.2.0) (+4 more)

### Community 818 - "SSH Configuration Guide"
Cohesion: 0.15
Nodes (13): Configuration File, Example: Production Server with Strict Restrictions, Field Reference, Full Annotated Example, How Allow/Deny Lists Work, How Auto-Approve Works, How to Add a New Trusted Host, SSH Configuration Guide (+5 more)

### Community 819 - "MultiHostResult"
Cohesion: 0.14
Nodes (10): TestHostResult, TestMultiHostResultProperties, HostResult, MultiHostResult, Aggregated outcome across all hosts., True only if every host passed (none failed or unreachable)., 0 iff all hosts passed; 1 otherwise (incl. empty / any unreachable)., Render an aligned PASS/FAIL table plus a totals line. (+2 more)

### Community 820 - "TestEdgeKill"
Cohesion: 0.10
Nodes (4): FakeCaller, RBAC is recorded, not enforced; owner is switchable., TestEdgeKill, _lost_write()

### Community 821 - "BlockingPipeline"
Cohesion: 0.10
Nodes (12): BlockingPipeline, EncodingDetectingPipeline, FakePipelineResult, Pipeline that detects base64-encoded injections., Prompt injection via getUpdates must be blocked by the pipeline., Base64-encoded injection via getUpdates must be caught., Normal messages must pass through the pipeline unmodified., Owner messages must pass even if the pipeline would block them. (+4 more)

### Community 822 - "What You Must Do When Invoked"
Cohesion: 0.10
Nodes (20): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Step 0 - GitHub repos and multi-path merge (only if a URL or several paths) (+12 more)

### Community 823 - "Pre-Deployment Checklist"
Cohesion: 0.10
Nodes (20): 1. Change Documentation, 2. Testing Evidence, 3. Backups & Rollback, 4. Blast Radius, 5. Observability, 6. Security, 7. Communication, 8. Service Control Commands (+12 more)

### Community 824 - "2026-03-08 — AI Engineering OS v1.0 Integration"
Cohesion: 0.10
Nodes (20): 2026-03-08 — AI Engineering OS v1.0 Integration, 2026-05-05 (Part 2) — Agent Cleanup, Gemini Recursion Fix, `.env.example` Fixes, 2026-05-05 — Skills `i-` Prefix, MCP Expansion, `--mcp` Flag, Agent Cleanup, Counts After Upgrade, `.env.example` Variable Name Fix, Files Added, Files Modified (path reference updates) (+12 more)

### Community 826 - "What You Must Do When Invoked"
Cohesion: 0.10
Nodes (20): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Step 0 - GitHub repos and multi-path merge (only if a URL or several paths) (+12 more)

### Community 827 - "AgentShroud™ — Trademark Prior Use Record"
Cohesion: 0.08
Nodes (24): First Use in Commerce (Feb 20, 2026), AgentShroud Mission Statement (Timestamped), USPTO Class 009 Filing (Downloadable Software), USPTO Class 042 Filing (Scientific/Technological Services), TEAS Plus Filing Process, AgentShroud™ — Trademark Prior Use Record, Asset Creation Timeline, First Use in Commerce (+16 more)

### Community 828 - "Pre-Deployment Checklist"
Cohesion: 0.10
Nodes (20): 1. Change Documentation, 2. Testing Evidence, 3. Backups & Rollback, 4. Blast Radius, 5. Observability, 6. Security, 7. Communication, 8. Service Control Commands (+12 more)

### Community 829 - "What You Must Do When Invoked"
Cohesion: 0.10
Nodes (20): For /graphify add and --watch, For /graphify query, For the commit hook and native CLAUDE.md integration, For --update and --cluster-only, /graphify, Honesty Rules, Interpreter guard for subcommands, Step 0 - GitHub repos and multi-path merge (only if a URL or several paths) (+12 more)

### Community 830 - "Pre-Deployment Checklist"
Cohesion: 0.10
Nodes (20): 1. Change Documentation, 2. Testing Evidence, 3. Backups & Rollback, 4. Blast Radius, 5. Observability, 6. Security, 7. Communication, 8. Service Control Commands (+12 more)

### Community 831 - "Post-v1.0.0 — Deferred"
Cohesion: 0.17
Nodes (12): Advanced Integrations (Phase 19), Browser Extension, Full Configuration System (Phase 18), Infrastructure — Deferred (moved from v0.9.0 → post-v1.0.0 on 2026-03-04), Integration Hub (Phase 13), iOS/macOS Shortcuts, Mac Mini Onboarding (Phase 14), Multi-Host Deployment (+4 more)

### Community 832 - "Production Testing Procedures  ⚠️  NO SEPARATE DEV ENVIRONMENT"
Cohesion: 0.10
Nodes (19): A. AWS Glue Jobs, B. AWS Step Functions, C. AWS Athena, D. PostgreSQL — RDS (`fe-gsdl-poc-database`), E. MySQL — On-Site Zabbix Databases (200+ sites), F. IAM Policies, G. Tailscale / Network, General Rules (+11 more)

### Community 833 - "Production Testing Procedures  ⚠️  NO SEPARATE DEV ENVIRONMENT"
Cohesion: 0.10
Nodes (19): A. AWS Glue Jobs, B. AWS Step Functions, C. AWS Athena, D. PostgreSQL — RDS (`fe-gsdl-poc-database`), E. MySQL — On-Site Zabbix Databases (200+ sites), F. IAM Policies, G. Tailscale / Network, General Rules (+11 more)

### Community 834 - "AgentShroud Security Analysis & Hardening"
Cohesion: 0.10
Nodes (20): AgentShroud Security Analysis & Hardening, Comparison: Traditional Setup vs. Our Approach, Conclusion, Daily Monitoring, Docker Hardening Measures, Future Security Enhancements, Incident Response Plan, Monitoring & Incident Response (+12 more)

### Community 836 - "Add information filtering to prevent agent self-disclosure"
Cohesion: 0.17
Nodes (11): Add information filtering to prevent agent self-disclosure, Constraints, Evidence, Option A: System prompt restriction (fast, partial), Option B: Outbound content filter (robust), Option C: Both (recommended), Problem, Remediation (+3 more)

### Community 837 - "Browser-Fetch Skill for 1Password Share Links"
Cohesion: 0.17
Nodes (12): AgentShroud Method ✅, Audit Log Format, Browser-Fetch Skill for 1Password Share Links, Future: Telegram Integration (When Auto-Discovered), Installation Status, Integration with AgentShroud Workflow, Overview, Performance (+4 more)

### Community 838 - "AgentShroud Weekly Upgrade Report — 2026-08-30"
Cohesion: 0.08
Nodes (22): 1. Summary, 1. Summary, 2. Environment mapping, 3. Upgrade table, 4. Security findings, 5. Verification evidence, 6. Breaking changes / manual follow-ups, 7. Rollback instructions (+14 more)

### Community 839 - "AgentShroud Sunday Upgrade — 2026-09-06 (dev-only, read-only inventory → scoped fixes)"
Cohesion: 0.17
Nodes (11): 0. Pre-existing session context worth recording, 1. Environment mapping, 2. Upgrade table, 3. Security findings, 4. Verification evidence, 5. Breaking changes / manual follow-ups (human review needed), 6. Rollback instructions, 7. Time spent (+3 more)

### Community 840 - "Session Summary - February 14, 2026"
Cohesion: 0.10
Nodes (19): Appendix: Commands Run This Session, Appendix: Gateway Credentials, Conclusion, Documentation, Immediate (This Session), Key Metrics, Lessons Learned, Long-Term (3-12 Months) (+11 more)

### Community 841 - "1. Accomplishments This Phase"
Cohesion: 0.10
Nodes (19): 1. Accomplishments This Phase, 2. Security Value Audit, 3. Remaining Work — Prioritized by Value, 4. Risks & Gaps, AgentShroud Phase Review — 2026-02-23, Critical, Design Decisions to Reconsider, feature/terminal-control-center (1 commit) (+11 more)

### Community 842 - "AgentShroud v0.9.0"
Cohesion: 0.10
Nodes (19): 1.1 Purpose, 1.2 Scope, 1.3 Intended Audience, 1. Purpose and Scope, 2.1 Core Security Modules, 2. Functional Requirements, 3. Non-Functional Requirements, 4.1 Technical Constraints (+11 more)

### Community 843 - "Incident Response Playbook — AgentShroud"
Cohesion: 0.10
Nodes (19): 1. Detection — What Triggers an Incident, 2. Severity Classification, 3. Response Procedures, 4. Kill Switch Usage Guide, 5. Evidence Preservation, 6. Post-Incident Review Template, 7. Communication Templates, 8. Contacts and Escalation (+11 more)

### Community 844 - "TestExfiltrationDetection"
Cohesion: 0.12
Nodes (10): EntropyCalculator, TestEntropyCalculator, Test detection of data exfiltration patterns., High-entropy DNS queries indicate tunneling., Egress monitoring should be available., Environment guard should monitor data access patterns., Git guard should catch credential patterns., TestExfiltrationDetection (+2 more)

### Community 845 - "TestEgressFilterConfig"
Cohesion: 0.11
Nodes (11): Create config from environment variables and AGENTSHROUD_MODE., Test denylist wildcard matching., Test EgressFilterConfig functionality., Test default configuration values., Test config creation from environment in enforce mode., Test config creation from environment in monitor mode., Test specific egress mode environment variable., Test basic allowlist functionality. (+3 more)

### Community 846 - "EnvelopeSigner"
Cohesion: 0.19
Nodes (16): _defang(), EnvelopeSigner, Return ``content`` wrapped and signed as untrusted third-party input., Return ``(content, source)`` if ``wrapped`` is intact and correctly signed., Signs and verifies InstructionEnvelopes. Usage:: signer = EnvelopeSigner() env…, Signed Instruction Envelopes — C46 Wraps instructions and tool results in HMAC-…, unwrap_untrusted(), wrap_untrusted() (+8 more)

### Community 847 - "ToolResultSanitizerConfig"
Cohesion: 0.15
Nodes (13): Configuration for tool result markdown sanitization., Convenience function to sanitize tool result content. Args: content: Content to…, sanitize_tool_result(), ToolResultSanitizerConfig, Test ToolResultSanitizerConfig., Test default configuration values., Test the convenience sanitize_tool_result function., Integration tests for the sanitizer. (+5 more)

### Community 848 - "_patch_urlopen"
Cohesion: 0.13
Nodes (8): _FakeHTTPResponse, _patch_urlopen(), fake_urlopen(), Exception, Context-manager stand-in for the object urlopen() yields., Patch gateway.cli.client.urlopen; return list of captured Request objects., test_convenience_methods_hit_expected_endpoints(), TestSCLClientRequest

### Community 849 - "Incident: Conduit/Hermes instability, 2026-10-16 (overnight)"
Cohesion: 0.08
Nodes (24): 2026-10-17 afternoon: drift audit of both hosts, and the drift PR, Afternoon (12:00–12:15 EDT): prod's evidence arrived, two more fixes committed, Afternoon (14:00–14:30 EDT): two more gateway findings from prod, fixed on dev, Changes committed for Sunday (this commit), Complete commit list, 2026-10-10 through tonight (`main`, this repo), Dev bring-up failures 06:32-06:57 EDT: compose-version network hash + stale endpoints, Dev Hermes was polling prod's Hermes Telegram bot (found 07:12 EDT), Dev-side changes made tonight (this repo, this session) (+16 more)

### Community 850 - "AgentShroud v0.8.0 — 25-Domain Prompt Injection Defense Assessment & Roadmap"
Cohesion: 0.22
Nodes (8): Additional Controls Checklist, AgentShroud v0.8.0 — 25-Domain Prompt Injection Defense Assessment & Roadmap, Context, Critical Files (v0.8.0 Changes), DELIVERABLE 2 — Maturity Scorecard, Implementation Sequence (v0.8.0 Execution Order), Top-10 Gaps by Exploitability x Impact (Post v0.8.0), Verification Plan

### Community 851 - "test_voice_stt_model_ab.py"
Cohesion: 0.06
Nodes (42): test_stt_transcribe_empty_bytes_returns_empty(), The record is emitted through the module logger for A/B comparison., With WHISPER_MODEL_SIZE unset, the resolved size stays small.en., Setting WHISPER_MODEL_SIZE=base.en flips the resolved model (A/B)., A garbage WHISPER_MODEL_SIZE env value does not break startup., The A/B measurement fires on the real transcribe path (model mocked). Proves…, No requested value → the default is used (behaviour unchanged)., SCRUM-57 — STT model A/B (Whisper small.en ↔ base.en). Covers the config-driven… (+34 more)

### Community 852 - "dashboard_endpoints.py"
Cohesion: 0.13
Nodes (17): test_alert_store_push_and_summary(), Alert, alerts_summary(), AlertStore, _check_host(), logs_recent(), proxy_status(), get (+9 more)

### Community 853 - "_TrustCaptor"
Cohesion: 0.15
Nodes (11): _make_trust_app_state(), Pipeline mock that records the user_trust_level passed to process_outbound.…, Minimal app_state for owner-trust tests., SCRUM-46: verify forward.py elevates trust to FULL for the owner's user_id. The…, When request.user_id matches _owner_user_id (with the trusted header),…, A collaborator's user_id must NOT trigger the owner elevation., Requests with no user_id must not be elevated to FULL., An empty string user_id must not match the owner. (+3 more)

### Community 855 - "TestVersionRoutes"
Cohesion: 0.11
Nodes (6): client(), fixture, Use a temporary DB for all tests., Tests for Version Manager API Routes., TestVersionRoutes, tmp_version_db()

### Community 856 - "ADR-002: Default-Allow Security Philosophy"
Cohesion: 0.18
Nodes (10): ADR-002: Default-Allow Security Philosophy, Consequences, Context, Decision, Evaluation Criteria, Implementation Approach, Mitigation Strategies, Negative Consequences (+2 more)

### Community 858 - "ADR-007: Zero-Config Security (docker-compose up = fully secured)"
Cohesion: 0.18
Nodes (10): ADR-007: Zero-Config Security (docker-compose up = fully secured), Auto-Configuration Features, Configuration Hierarchy, Consequences, Context, Decision, Mitigation, Negative Consequences (+2 more)

### Community 859 - "ADR-008-progressive-trust-levels.md"
Cohesion: 0.23
Nodes (11): ADR-008: Progressive Trust Levels for Agents, Consequences, Context, Decision, Mitigation, Negative Consequences, Positive Consequences, Progressive Controls (+3 more)

### Community 860 - "Bear Notes"
Cohesion: 0.18
Nodes (9): Apple Notes CLI, Bear Notes, Common Commands, Configuration, Getting a Bear Token, Notes, Options, memo CLI (antoniorodr/memo) (+1 more)

### Community 862 - "SecurityFinding"
Cohesion: 0.12
Nodes (22): SecurityFinding, AgentShroud Weekly Upgrade — 2026-09-06, Application CVE registry (OpenClaw / Hermes agents, per `docs/security/cve-mitigation-matrix.md`), Breaking changes / manual follow-ups, Environment Mapping, Fresh Trivy scans (run today, CRITICAL+HIGH only, `--scanners vuln`), GitHub-hosted findings, Language dependencies (+14 more)

### Community 863 - "Daedalus — Concept Illustrator"
Cohesion: 0.18
Nodes (10): architecture.puml (PlantUML), Daedalus — Concept Illustrator, diagrams/README.md, flow.mmd (Mermaid), Input Requirements, Output Format, Persona, Quality Checklist (+2 more)

### Community 864 - "Daedalus — Concept Illustrator"
Cohesion: 0.18
Nodes (10): architecture.puml (PlantUML), Daedalus — Concept Illustrator, diagrams/README.md, flow.mmd (Mermaid), Input Requirements, Output Format, Persona, Quality Checklist (+2 more)

### Community 866 - "Recommendations for Production Deployment"
Cohesion: 0.18
Nodes (10): 1. Pre-populate known_hosts, 2. Network Segmentation, 3. Key Rotation, 4. Rate Limiting, 5. Output Sanitization, 6. Least-Privilege SSH Users, Comparison: Direct SSH vs. AgentShroud SSH Proxy, Recommendations for Production Deployment (+2 more)

### Community 867 - "AgentShroud -- USPTO Provisional Patent Application"
Cohesion: 0.24
Nodes (10): AgentShroud -- USPTO Provisional Patent Application, Combined Filing Costs (Patent + Trademark), Filing Reference, Patent Center Filing Steps, Post-Filing, Pre-Filing Preparation, SECTION 2: WRITTEN DESCRIPTION OF THE INVENTION, SECTION 4: FILING CHECKLIST (+2 more)

### Community 868 - "ENTERPRISE GOVERNANCE PROXY SYSTEM AND METHOD FOR POLICY-ENFORCED INTERCEPTION, INSPECTION, AND MEDIATION OF AUTONOMOUS AI AGENT COMMUNICATIONS WITH EXTERNAL SYSTEMS"
Cohesion: 0.18
Nodes (11): ABSTRACT, BACKGROUND OF THE INVENTION, CROSS-REFERENCE TO RELATED APPLICATIONS, DETAILED DESCRIPTION — INTERCEPTION MECHANISMS, DETAILED DESCRIPTION — SECURITY MODULE PIPELINE, DETAILED DESCRIPTION — SYSTEM ARCHITECTURE, ENTERPRISE GOVERNANCE PROXY SYSTEM AND METHOD FOR POLICY-ENFORCED INTERCEPTION, INSPECTION, AND MEDIATION OF AUTONOMOUS AI AGENT COMMUNICATIONS WITH EXTERNAL SYSTEMS, FIELD OF THE INVENTION (+3 more)

### Community 869 - "Production Testing Procedures  ⚠️  NO SEPARATE DEV ENVIRONMENT"
Cohesion: 0.10
Nodes (19): A. AWS Glue Jobs, B. AWS Step Functions, C. AWS Athena, D. PostgreSQL — RDS (`fe-gsdl-poc-database`), E. MySQL — On-Site Zabbix Databases (200+ sites), F. IAM Policies, G. Tailscale / Network, General Rules (+11 more)

### Community 870 - "Production Testing Procedures  ⚠️  NO SEPARATE DEV ENVIRONMENT"
Cohesion: 0.10
Nodes (19): A. AWS Glue Jobs, B. AWS Step Functions, C. AWS Athena, D. PostgreSQL — RDS (`fe-gsdl-poc-database`), E. MySQL — On-Site Zabbix Databases (200+ sites), F. IAM Policies, G. Tailscale / Network, General Rules (+11 more)

### Community 871 - "Production Testing Procedures  ⚠️  NO SEPARATE DEV ENVIRONMENT"
Cohesion: 0.10
Nodes (19): A. AWS Glue Jobs, B. AWS Step Functions, C. AWS Athena, D. PostgreSQL — RDS (`fe-gsdl-poc-database`), E. MySQL — On-Site Zabbix Databases (200+ sites), F. IAM Policies, G. Tailscale / Network, General Rules (+11 more)

### Community 872 - "Required: ≥ 4.5 for text, ≥ 3.0 for UI elements"
Cohesion: 0.11
Nodes (18): Anti-Patterns to Flag, Brand Audit Checklist, Brand System Components, Color Token Definition, Core Discipline: Audit → Define → Apply → Enforce, Deck / Slide Master Rules, Dependencies, Diagram Theme Block (Mermaid) (+10 more)

### Community 873 - "Skill: MCP Doctor (MCPM-DOCTOR)"
Cohesion: 0.11
Nodes (18): 1. Check MCP Configuration, 2. Test GitHub MCP Server, 3. Test Atlassian MCP Server, 4. Test AWS API MCP Server, Common Issues & Fixes, Diagnostic Capabilities, Diagnostic Workflow, Issue: "Atlassian OAuth token expired" (+10 more)

### Community 874 - "Common Operations"
Cohesion: 0.18
Nodes (11): Common Operations, Delete an Email, Forward an Email, List Emails, List Folders, Manage Flags, Move/Copy Emails, Read an Email (+3 more)

### Community 875 - "tailscale-serve.sh"
Cohesion: 0.29
Nodes (14): Gateway /hermes-dashboard/ reverse proxy 502 from host/Tailscale, hermes-dashboard-relay container (:9119 Tailscale bypass of gateway), cmd_persist(), cmd_start(), cmd_status(), cmd_stop(), edge_funnel_off(), edge_funnel_on() (+6 more)

### Community 876 - "Plan: Proxying HexStrike AI MCP Agents via AgentShroud"
Cohesion: 0.18
Nodes (10): Context, Deliverable & branch, Known integration gaps to document (not fix in this planning branch), Out of scope (explicitly), Plan: Proxying HexStrike AI MCP Agents via AgentShroud, Policy levers to configure (per engagement), Proposed architecture, The core tension (and its resolution) (+2 more)

### Community 877 - "Skill: Project Management (PM)"
Cohesion: 0.11
Nodes (18): Assigning Work, CHANGELOG.md Updates, Continuity Files, Definition of Done (from CLAUDE.md), Escalation, Known Risks, Project Roadmap, Quick Status (for chat/Telegram) (+10 more)

### Community 878 - "Required: ≥ 4.5 for text, ≥ 3.0 for UI elements"
Cohesion: 0.11
Nodes (18): Anti-Patterns to Flag, Brand Audit Checklist, Brand System Components, Color Token Definition, Core Discipline: Audit → Define → Apply → Enforce, Deck / Slide Master Rules, Dependencies, Diagram Theme Block (Mermaid) (+10 more)

### Community 879 - "AgentShroud Recovery Plan v0.4.0"
Cohesion: 0.18
Nodes (10): 0.1 Code Inventory ✅, 0.2 Current State ✅, 1.1 The Problem, 1.2 Fix Shipped ✅, AgentShroud Recovery Plan v0.4.0, EXECUTIVE SUMMARY, PHASE 0: STABILIZATION ✅ COMPLETE, PHASE 1: SECURITY FIX ✅ COMPLETE (v0.4.0) (+2 more)

### Community 880 - "Skill: MCP Doctor (MCPM-DOCTOR)"
Cohesion: 0.11
Nodes (18): 1. Check MCP Configuration, 2. Test GitHub MCP Server, 3. Test Atlassian MCP Server, 4. Test AWS API MCP Server, Common Issues & Fixes, Diagnostic Capabilities, Diagnostic Workflow, Issue: "Atlassian OAuth token expired" (+10 more)

### Community 881 - "Skill: Project Management (PM)"
Cohesion: 0.11
Nodes (18): Assigning Work, CHANGELOG.md Updates, Continuity Files, Definition of Done (from CLAUDE.md), Escalation, Known Risks, Project Roadmap, Quick Status (for chat/Telegram) (+10 more)

### Community 882 - "Skill: MCP Doctor (MCPM-DOCTOR)"
Cohesion: 0.11
Nodes (18): 1. Check MCP Configuration, 2. Test GitHub MCP Server, 3. Test Atlassian MCP Server, 4. Test AWS API MCP Server, Common Issues & Fixes, Diagnostic Capabilities, Diagnostic Workflow, Issue: "Atlassian OAuth token expired" (+10 more)

### Community 883 - "Skill: Project Management (PM)"
Cohesion: 0.11
Nodes (18): Assigning Work, CHANGELOG.md Updates, Continuity Files, Definition of Done (from CLAUDE.md), Escalation, Known Risks, Project Roadmap, Quick Status (for chat/Telegram) (+10 more)

### Community 884 - "start-agentshroud.sh"
Cohesion: 0.22
Nodes (18): _container_age_seconds(), _dns_warmup_probe(), _enforce_sandbox_cap(), _model_runtime_ready(), op_proxy_read_with_retry(), _poll_openclaw_ready(), _read_hc_secret(), _read_secret_file() (+10 more)

### Community 885 - "Work Completed"
Cohesion: 0.11
Nodes (19): 1. Security Research & Analysis, 2. Documentation Created, 3. Files Modified/Created, 4. Security Verification, 5. Tasks Completed, 6. Testing Performed, 7. Current Issues, Additional Vulnerabilities (+11 more)

### Community 886 - "Updating AgentShroud"
Cohesion: 0.12
Nodes (18): Deploying AgentShroud on Linux (docs/operations/linux.md), Docker Buildx multi-arch build (linux/amd64, linux/arm64), systemd service /etc/systemd/system/agentshroud.service for auto-start, Deploying AgentShroud on macOS (docs/operations/macos.md), Docker Desktop (Apple Silicon / Intel transparent arch handling; resource allocation guidance), Native Python gateway dev run: uvicorn gateway.ingest_api.main:app --host 127.0.0.1 --port 8080, Check Current Version, Checking the Changelog (+10 more)

### Community 887 - "Crash Recovery"
Cohesion: 0.11
Nodes (19): Auto-Restart, Crash Diagnosis, Crash Recovery, Data Recovery, Immediate Assessment, Ledger Database, OOM Kill (Exit Code 137), Option 1: Simple Restart (most common fix) (+11 more)

### Community 888 - "_age"
Cohesion: 0.11
Nodes (6): _age(), Path, Set a file's mtime to `hours` hours in the past., TestComplianceAuditing, TestIsFresh, TestVulnerabilityManagement

### Community 889 - "Telegram Channel Setup"
Cohesion: 0.17
Nodes (11): Step 8: Configure Environment, Prerequisites, Step 1: Create a Bot, Step 2: Write the Token to Secrets, Step 3: Find Your Telegram User ID, Step 4: Configure Environment, Step 5: Configure agentshroud.yaml, Step 6: Rebuild and Start (+3 more)

### Community 890 - "test_edge_fuzz.py"
Cohesion: 0.21
Nodes (14): FUZZ, parametrize, test_control_characters_rejected_in_single_line_fields(), test_control_characters_rejected_in_task(), test_edge_guard_never_500s_or_passes_batches(), test_enums_and_types(), test_gateway_rpc_parser_rejects_junk_without_500(), __getattr__() (+6 more)

### Community 891 - "ScanResult"
Cohesion: 0.17
Nodes (11): ContentFinding, Scan content for security issues. Args: content: The web content to scan.…, Scan for prompt injection patterns., Scan HTML for hidden instructions in comments, invisible elements, meta tags., A single finding from content scanning., Scan for base64-encoded or otherwise obfuscated payloads., Detect zero-width character sequences (steganographic attacks)., Detect DTD/entity constructs that drive XML parser memory-safety bugs. Flags… (+3 more)

### Community 892 - "test_lifespan_prune.py"
Cohesion: 0.17
Nodes (17): _is_fixture_uid(), Return True when uid looks like a test fixture that should be silently dropped.…, Gateway-level collaborator activity tracker. Logs every non-owner message from…, _make_md(), _prune_fixture_markdown(), parametrize, Path, Run the same markdown-prune logic as lifespan.py and return pruned count. (+9 more)

### Community 893 - "OAuthRequest"
Cohesion: 0.18
Nodes (7): OAuthRequest, fixture, Tests for oauth_security module - MCP OAuth proxy security. TDD: Written before…, TestClientValidation, TestPKCE, TestStateValidation, validator()

### Community 894 - "ADR-004: API Keys Never in Agent Container"
Cohesion: 0.20
Nodes (9): ADR-004: API Keys Never in Agent Container, Consequences, Context, Decision, Implementation, Mitigation, Negative Consequences, Positive Consequences (+1 more)

### Community 895 - "TestOpenAPIContract"
Cohesion: 0.11
Nodes (11): fixture, API contract tests. Validates the FastAPI OpenAPI schema and ensures: - Version…, OpenAPI schema and version consistency tests., Create a FastAPI test client., OpenAPI schema endpoint returns valid JSON schema., API version in OpenAPI schema matches gateway package version., Health/status endpoint must be accessible without authentication., Protected API endpoints must reject requests without auth tokens. (+3 more)

### Community 896 - "Skill: Data Validation (DATA-VAL)"
Cohesion: 0.20
Nodes (9): 1. Schema Validation, 2. Partition Coverage, 3. Data Quality Checks, 4. Cross-Site Comparison, Critical: Cost Control, Role, Skill: Data Validation (DATA-VAL), Test Data Validation Pattern (+1 more)

### Community 897 - "TestGroupRoleResolver"
Cohesion: 0.11
Nodes (9): GroupRoleResolver correctly maps Telegram user IDs to per-group roles., owner_in_group resolves to GroupRole.OWNER., Regular member resolves to GroupRole.MEMBER., Read-only user resolves to GroupRole.READ_ONLY., User not in role map defaults to GroupRole.READ_ONLY (deny-by-default)., Unknown group_chat_id defaults to GroupRole.READ_ONLY., email_sending is recognized as a high-risk tool., web_search is NOT a high-risk tool. (+1 more)

### Community 898 - "test_hermes_forwarder_drops_non_http"
Cohesion: 0.11
Nodes (9): asyncio, lifespan startup must install ThreadPoolExecutor(max_workers=64)., Regression guards for gateway lifespan startup fixes. Covers: -…, Hermes API forwarder must include an HTTP-method peek to drop non-HTTP…, Non-HTTP bytes (e.g. TLS ClientHello) must be dropped without proxying., test_hermes_forwarder_drops_non_http(), _fake_open_connection(), test_lifespan_hermes_forwarder_has_http_peek() (+1 more)

### Community 899 - "Identity Reference - AgentShroud System"
Cohesion: 0.20
Nodes (9): 🎯 Bot Identity Configuration, 💬 Communication Flow, 📱 How It Works, Identity Reference - AgentShroud System, 🔐 Security, Via Control UI:, Via Telegram:, 👤 You (The Real Person) (+1 more)

### Community 900 - "Required: ≥ 4.5 for text, ≥ 3.0 for UI elements"
Cohesion: 0.11
Nodes (18): Anti-Patterns to Flag, Brand Audit Checklist, Brand System Components, Color Token Definition, Core Discipline: Audit → Define → Apply → Enforce, Deck / Slide Master Rules, Dependencies, Diagram Theme Block (Mermaid) (+10 more)

### Community 901 - "AgentShroud Changelog"
Cohesion: 0.15
Nodes (16): A2A Governance (A2APolicyEngine / A2AProxy), AgentShroud Changelog, ESP32-S3-BOX-3 Voice Terminal, Hermes Bot, OpenClaw Bot, TrustManager Progressive-Trust Ladder, Voice Gateway, Reachability Context (cap_drop ALL, isolated network) (+8 more)

### Community 902 - "AgentShroud Sunday Upgrade — 2026-09-23 14:00 ET (DEV run, afternoon continuation)"
Cohesion: 0.09
Nodes (22): 0. Preflight, 10. openclaw build FAILED — genuine disk exhaustion, not policy or code, 11. Rollback triggered automatically, got stuck, manually completed, 12. Live incident discovered at handoff: ENOSPC crash-looping containers, 13. Security findings — unresolved from prior sessions, one new live incident, 14. Verification evidence, 15. Jira tracking (§6 of mission), 16. Breaking changes / manual follow-ups (for Isaiah) (+14 more)

### Community 903 - "01-architecture.md"
Cohesion: 0.27
Nodes (9): 1. C4 Level 0 — Context Diagram (Executive View), 2. C4 Level 1 — Container Diagram, 3. Architecture Component Diagram — Gateway internals, AgentShroud — Architecture Diagrams, C4 Level 1 — Container Diagram, C4 Level 0 — System Context Diagram, Gateway Internals Component Diagram, Rendered C4 Context Diagram (PNG) (+1 more)

### Community 904 - "Skill: MCP Doctor (MCPM-DOCTOR)"
Cohesion: 0.11
Nodes (18): 1. Check MCP Configuration, 2. Test GitHub MCP Server, 3. Test Atlassian MCP Server, 4. Test AWS API MCP Server, Common Issues & Fixes, Diagnostic Capabilities, Diagnostic Workflow, Issue: "Atlassian OAuth token expired" (+10 more)

### Community 905 - "Skill: Project Management (PM)"
Cohesion: 0.11
Nodes (18): Assigning Work, CHANGELOG.md Updates, Continuity Files, Definition of Done (from CLAUDE.md), Escalation, Known Risks, Project Roadmap, Quick Status (for chat/Telegram) (+10 more)

### Community 906 - "Skill: Data Validation (DATA-VAL)"
Cohesion: 0.20
Nodes (9): 1. Schema Validation, 2. Partition Coverage, 3. Data Quality Checks, 4. Cross-Site Comparison, Critical: Cost Control, Role, Skill: Data Validation (DATA-VAL), Test Data Validation Pattern (+1 more)

### Community 907 - "Required: ≥ 4.5 for text, ≥ 3.0 for UI elements"
Cohesion: 0.11
Nodes (18): Anti-Patterns to Flag, Brand Audit Checklist, Brand System Components, Color Token Definition, Core Discipline: Audit → Define → Apply → Enforce, Deck / Slide Master Rules, Dependencies, Diagram Theme Block (Mermaid) (+10 more)

### Community 908 - "REPORT STRUCTURE"
Cohesion: 0.20
Nodes (9): ANTI-HALLUCINATION CHECKLIST, CRITICAL RULES — READ BEFORE DOING ANYTHING, OUTPUT REQUIREMENTS, REPORT STRUCTURE, SECTION 1: MARKET ANALYSIS, SECTION 2: COMPETITIVE ANALYSIS — AGENT SECURITY TOOLS, SECTION 3: AUTONOMOUS AGENT ECOSYSTEM UPDATE, SECTION 4: NEXT STEPS TO STAY AHEAD (+1 more)

### Community 909 - "Skill: MCP Doctor (MCPM-DOCTOR)"
Cohesion: 0.11
Nodes (18): 1. Check MCP Configuration, 2. Test GitHub MCP Server, 3. Test Atlassian MCP Server, 4. Test AWS API MCP Server, Common Issues & Fixes, Diagnostic Capabilities, Diagnostic Workflow, Issue: "Atlassian OAuth token expired" (+10 more)

### Community 910 - "Skill: Data Validation (DATA-VAL)"
Cohesion: 0.20
Nodes (9): 1. Schema Validation, 2. Partition Coverage, 3. Data Quality Checks, 4. Cross-Site Comparison, Critical: Cost Control, Role, Skill: Data Validation (DATA-VAL), Test Data Validation Pattern (+1 more)

### Community 911 - "Skill: Project Management (PM)"
Cohesion: 0.11
Nodes (18): Assigning Work, CHANGELOG.md Updates, Continuity Files, Definition of Done (from CLAUDE.md), Escalation, Known Risks, Project Roadmap, Quick Status (for chat/Telegram) (+10 more)

### Community 912 - "Skill: MCP Tools Usage (MCP-TOOLS)"
Cohesion: 0.20
Nodes (9): 1. GitHub MCP, 2. Atlassian MCP (Jira + Confluence), 3. AWS API MCP, Authentication Issues, Available MCP Servers, Common Errors, MCP Troubleshooting, Role (+1 more)

### Community 913 - "REPORT STRUCTURE"
Cohesion: 0.20
Nodes (9): ANTI-HALLUCINATION CHECKLIST, CRITICAL RULES — READ BEFORE DOING ANYTHING, OUTPUT REQUIREMENTS, REPORT STRUCTURE, SECTION 1: MARKET ANALYSIS, SECTION 2: COMPETITIVE ANALYSIS — AGENT SECURITY TOOLS, SECTION 3: AUTONOMOUS AGENT ECOSYSTEM UPDATE, SECTION 4: NEXT STEPS TO STAY AHEAD (+1 more)

### Community 914 - "Required: ≥ 4.5 for text, ≥ 3.0 for UI elements"
Cohesion: 0.11
Nodes (18): Anti-Patterns to Flag, Brand Audit Checklist, Brand System Components, Color Token Definition, Core Discipline: Audit → Define → Apply → Enforce, Deck / Slide Master Rules, Dependencies, Diagram Theme Block (Mermaid) (+10 more)

### Community 915 - "34 Security Modules Pipeline (P0-P3)"
Cohesion: 0.29
Nodes (8): 25-Domain Prompt Injection Defense Framework, egress_filter module, pii_sanitizer module (disabled — false positives), prompt_guard module (observatory mode — too aggressive for enforce), 34 Security Modules Pipeline (P0-P3), Steve Hay's External Reviewer Findings, PII Sanitizer (user-facing description), Multi-Stage Security Pipeline (P0-P3 tiers)

### Community 916 - "Approval queue (notify Isaiah via Telegram, wait up to 1 hour)"
Cohesion: 0.20
Nodes (10): Approval queue (notify Isaiah via Telegram, wait up to 1 hour), Execute action via HTTP CONNECT proxy, Isaiah decides (approved / rejected / timeout), Write audit entry to ledger.db (SHA-256 hash only), LLM inference (OpenAI GPT-4o or Anthropic Claude), Main agent (agentshroud_bot), MCP Inspector (injection scan, PII scan, sensitive op scan), Response delivered to user (+2 more)

### Community 917 - "Skill: MCP Doctor (MCPM-DOCTOR)"
Cohesion: 0.11
Nodes (18): 1. Check MCP Configuration, 2. Test GitHub MCP Server, 3. Test Atlassian MCP Server, 4. Test AWS API MCP Server, Common Issues & Fixes, Diagnostic Capabilities, Diagnostic Workflow, Issue: "Atlassian OAuth token expired" (+10 more)

### Community 918 - "installer.py"
Cohesion: 0.17
Nodes (15): check_prerequisites(), get_runtimes(), InstallConfig, installer_page(), PrerequisiteCheck, BaseModel, get, post (+7 more)

### Community 919 - "Skill: Project Management (PM)"
Cohesion: 0.11
Nodes (18): Assigning Work, CHANGELOG.md Updates, Continuity Files, Definition of Done (from CLAUDE.md), Escalation, Known Risks, Project Roadmap, Quick Status (for chat/Telegram) (+10 more)

### Community 920 - "AgentShroud Red Team Adversarial Tester"
Cohesion: 0.11
Nodes (17): Adversary Model, AgentShroud Red Team Adversarial Tester, Attack Phases, Attack Techniques Reference, Coverage Requirements, Critical Rules, Infrastructure, Key Principle (+9 more)

### Community 921 - "Socrates — Dialogue Architect"
Cohesion: 0.11
Nodes (17): Dialogue Adaptations, Dialogue Techniques, ElevenLabs v3 Audio Tags, Episode Closing (Mandatory for OKE), EXPERT, Expert Persona, HOST, Input Requirements (+9 more)

### Community 922 - "AgentShroud Red Team Adversarial Tester"
Cohesion: 0.11
Nodes (17): Adversary Model, AgentShroud Red Team Adversarial Tester, Attack Phases, Attack Techniques Reference, Coverage Requirements, Critical Rules, Infrastructure, Key Principle (+9 more)

### Community 923 - "Workflow (follow in order)"
Cohesion: 0.11
Nodes (19): 0) Model self-check (non-blocking), 1) Establish context (read-only), 2) Run OpenClaw security audits (read-only), 3) Check OpenClaw version/update status (read-only), 4) Determine risk tolerance (after system context), 5) Produce a remediation plan, 6) Offer execution options, 7) Execute with confirmations (+11 more)

### Community 924 - "ScanResult"
Cohesion: 0.07
Nodes (23): Finding, IntEnum, ValueError, Aggregated result of scanning a skill file or an entire skill tree., ALLOW below MEDIUM, FLAG at MEDIUM/HIGH, BLOCK at CRITICAL., Scan one skill artefact (``name`` = relative path, ``content`` = text)., Flag long opaque base64/hex runs as probable obfuscated payloads., Scan every file in a skill/MCP/agent tree and aggregate findings. ``files``… (+15 more)

### Community 925 - "Socrates — Dialogue Architect"
Cohesion: 0.11
Nodes (17): Dialogue Adaptations, Dialogue Techniques, ElevenLabs v3 Audio Tags, Episode Closing (Mandatory for OKE), EXPERT, Expert Persona, HOST, Input Requirements (+9 more)

### Community 926 - "AgentShroud Red Team Adversarial Tester"
Cohesion: 0.11
Nodes (17): Adversary Model, AgentShroud Red Team Adversarial Tester, Attack Phases, Attack Techniques Reference, Coverage Requirements, Critical Rules, Infrastructure, Key Principle (+9 more)

### Community 927 - "9. Deep Security Hardening (v0.9.0)"
Cohesion: 0.20
Nodes (10): 9.1 Log Sanitizer (gateway/security/log_sanitizer.py), 9.2 Environment Leakage Guard (gateway/security/env_guard.py), 9.3 Context Window Poisoning Defense (gateway/security/context_guard.py), 9.4 Git Hook Guard (gateway/security/git_guard.py), 9.5 Metadata Channel Guard (gateway/security/metadata_guard.py), 9.6 Network Isolation Validator (gateway/security/network_validator.py), 9.7 Resource Exhaustion Guard (gateway/security/resource_guard.py), 9.8 Tool Result Injection Scanning (MCP Inspector Enhancement) (+2 more)

### Community 928 - "Socrates — Dialogue Architect"
Cohesion: 0.11
Nodes (17): Dialogue Adaptations, Dialogue Techniques, ElevenLabs v3 Audio Tags, Episode Closing (Mandatory for OKE), EXPERT, Expert Persona, HOST, Input Requirements (+9 more)

### Community 929 - "Socrates — Dialogue Architect"
Cohesion: 0.11
Nodes (17): Dialogue Adaptations, Dialogue Techniques, ElevenLabs v3 Audio Tags, Episode Closing (Mandatory for OKE), EXPERT, Expert Persona, HOST, Input Requirements (+9 more)

### Community 930 - "Required Software"
Cohesion: 0.20
Nodes (10): 1. Docker Desktop, 2. Python 3.11+, 3. Python Packages, 4. Node.js 22+ (for OpenClaw), 5. Git, 6. Tailscale (Optional but Recommended), Hardware, Operating System (+2 more)

### Community 931 - "One Shroud Over Every Wire: A Story About Trust, Isolation, and AI Assistants"
Cohesion: 0.11
Nodes (18): Call for Collaborators, Daily Workflow, FAQ, Get Involved, How You Actually Use It, Long-Term (6-12 months), Mid-Term (3-6 months), Near-Term (1-3 months) (+10 more)

### Community 932 - "AgentShroud v0.7.0 — Red Team Remediation Plan"
Cohesion: 0.11
Nodes (17): 4 Architectural Gaps (No Existing Module), AgentShroud v0.7.0 — Red Team Remediation Plan, Critical Finding, Implementation Notes, Loss Categories, Red Team Engagement Plan (Pending), Source, Sprint 1: Enforce-by-Default (R-02, R-03) (+9 more)

### Community 933 - "Blue Team Security Assessment — AgentShroud v0.8.0 Round 2"
Cohesion: 0.11
Nodes (17): Blue Team Security Assessment — AgentShroud v0.8.0 Round 2, CRITICAL Findings, Executive Summary, HIGH Findings, LOW Findings, MEDIUM Findings, R2-C1: RBAC Management Endpoints Missing Authentication, R2-H1: 1Password CLI Download Without Checksum Verification (Bot Dockerfile) (+9 more)

### Community 934 - "Findings & Mitigations"
Cohesion: 0.11
Nodes (17): Architecture, Audit Methodology, 🔴 C1: SSH Config Bypass (`-F /dev/null`), 🔴 C2: Raw TCP to Host Port 22, 🔴 C3: PID1 Environment Readable (`/proc/1/environ`), Colima VM Networking, Container Security Audit — AgentShroud v0.8.0, Controls Summary (+9 more)

### Community 935 - "AgentShroud Threat Model (STRIDE Analysis)"
Cohesion: 0.20
Nodes (9): AgentShroud Threat Model (STRIDE Analysis), Assets Under Protection, Executive Summary, Mitigation Coverage Matrix, System Components in Scope, Threat Feeds, Threat Intelligence Integration, Threat Modeling Scope (+1 more)

### Community 936 - "AgentShroud Web Control Center - Implementation Summary"
Cohesion: 0.11
Nodes (17): 1. Enhanced Management Dashboard Routes (`gateway/web/management.py`), 2. Responsive CSS Framework (`gateway/web/static/agentshroud-dashboard.css`), 3. Main Dashboard Template (`gateway/web/templates/dashboard.html`), 🌐 Access Points, AgentShroud Web Control Center - Implementation Summary, 🔧 Architecture, 🎨 Branding Compliance, ✅ Dashboard Pages Created (+9 more)

### Community 937 - "AgentShroud Module Inventory"
Cohesion: 0.20
Nodes (8): AgentShroud Module Inventory, Original 33 Modules (v0.6.0), Pipeline Integration Points, v0.7.0 New Modules (Tier 2+3 + Hardening), AgentShroud Module Inventory, Original 33 Modules (v0.6.0), Pipeline Integration Points, v0.7.0 New Modules (Tier 2+3 + Hardening)

### Community 938 - "Google Calendar & Contacts - Quick Setup"
Cohesion: 0.11
Nodes (17): 📊 Comparison, Create Test Script, ⚡ Fastest Path Forward, Google Calendar & Contacts - Quick Setup, Install Node CalDAV Client, 🎯 My Recommendation, ✅ Next Steps, Option A: Simple (App Password + CalDAV) - RECOMMENDED FOR NOW (+9 more)

### Community 939 - "alert_dispatcher.py"
Cohesion: 0.11
Nodes (16): alert_dispatcher.py, Alert JSONL Format, AlertDispatcher.dispatch(alert), AlertDispatcher.get_digest(clear), AlertDispatcher._send_notification(alert), Configuration, Environment Variables, Function Details (+8 more)

### Community 940 - "drift_detector.py"
Cohesion: 0.11
Nodes (16): Configuration, Database Schema, Drift Categories and Severity, drift_detector.py, DriftDetector.acknowledge_alert(alert_id), DriftDetector.check_drift(current), DriftDetector.get_alerts(container_id, unacknowledged_only, limit), DriftDetector.set_baseline(snapshot) (+8 more)

### Community 941 - "encrypted_store.py"
Cohesion: 0.11
Nodes (17): Blob Wire Format, Configuration, encrypted_store.py, EncryptedStore.decrypt(blob), EncryptedStore.encrypt(data), EncryptedStore.__init__(master_secret, secret_path, iterations, key_id), EncryptedStore.rotate(blobs, new_secret, new_key_id), Environment Variables (+9 more)

### Community 942 - "Function Details"
Cohesion: 0.11
Nodes (16): Configuration / Environment Variables, Function Details, Generic Key Patterns Detected, Key Classes / Functions, key_vault.py, KeyInjector.inject_for_request(url, headers, agent_id, key_name), KeyLeakDetector.scan_outbound(text), KeyVault.check_value_match(text) (+8 more)

### Community 944 - "Function Details"
Cohesion: 0.11
Nodes (17): Configuration / Environment Variables, Default Limits, Function Details, Key Classes / Functions, Purpose, Related, resource_guard.py, ResourceGuard.add_alert_callback(callback) (+9 more)

### Community 945 - "trust_manager.py"
Cohesion: 0.11
Nodes (17): Configuration (TrustConfig), Database Schema, Default Action Trust Requirements, Environment Variables, Function Details, Key Classes / Functions, Mode: Enforce vs Monitor, Purpose (+9 more)

### Community 946 - "test_channel_ownership.py"
Cohesion: 0.12
Nodes (11): bypass_auth(), client(), fixture, Standard Telegram message payload is accepted., Tests for P3: Channel Ownership — Telegram webhook + email send. TDD red phase:…, Empty payload is handled gracefully (skipped, not error)., Response always includes a 'status' field., Without a pipeline configured, status is passthrough (not error). (+3 more)

### Community 947 - "A2APolicyConfig"
Cohesion: 0.08
Nodes (35): HermesA2AForwarder, Real HTTP forwarder to Hermes's internal A2A JSON-RPC listener. Matches the…, A2APolicyConfig, Any, Declarative A2A security policy. Loaded from the ``a2a_policy:`` section of…, Parse a policy config from a plain dict (e.g. loaded from YAML)., _jsonrpc(), asyncio (+27 more)

### Community 948 - "TestMemoryLifecycleManager"
Cohesion: 0.11
Nodes (10): Test memory lifecycle management., Clean up test environment., Test PII detection in memory content., Test prompt injection detection., Test content sanitization removes threats., Test validation before writing to memory files., Test retention policy for daily notes., Test MEMORY.md size limit enforcement. (+2 more)

### Community 949 - "Skill: Git Workflow Guardian (GIT-GUARD)"
Cohesion: 0.22
Nodes (8): Branch Naming, Commit Messages  (Conventional Commits), Emergency Hotfix, Mandatory Workflow  (10 steps), Protected Branch, REFUSE These, Role, Skill: Git Workflow Guardian (GIT-GUARD)

### Community 950 - "Output Sections (ALL required)"
Cohesion: 0.20
Nodes (10): 1. Scope of Change, 2. What Changes and Why, 3. Scalability Gate, 4. Blast Radius, 5. Known Limits and Assumptions, 6. Alternatives Considered, 7. Open Questions, 8. Verification Plan (+2 more)

### Community 951 - "Skill: Pull Request (PR) Generator"
Cohesion: 0.22
Nodes (8): Constraints, Content Requirements, Header, Objective, Role, Safety, Skill: Pull Request (PR) Generator, Technical Detail

### Community 952 - "Management Dashboard"
Cohesion: 0.22
Nodes (9): /api/config, /api/killswitch/{mode}, /api/logs, /api/rebuild, /api/security/report, /api/services/{name}/{action}, /api/status, /api/updates/bot/openclaw (+1 more)

### Community 953 - "test_middleware_coverage.py"
Cohesion: 0.12
Nodes (9): mm(), fixture, Coverage tests for gateway/ingest_api/middleware.py (MiddlewareManager).…, MiddlewareManager built via __new__ — every module attr explicitly None so each…, temp_workspace(), TestExtractUserId, TestInit, TestMetadataGuard (+1 more)

### Community 954 - "Socrates — Dialogue Architect"
Cohesion: 0.25
Nodes (9): Apollo — Audio Systems Producer, Athena — Knowledge Distiller, Atlas — Curriculum Architect, Daedalus — Concept Illustrator, Hermes — Reference Verifier (podcast agent), Mnemosyne — Retention Engineer, Oracle — Feedback Analyst, Socrates — Dialogue Architect (+1 more)

### Community 955 - "TestObservatoryMode"
Cohesion: 0.11
Nodes (10): Test Observatory Mode configuration and endpoints., Test that get_module_mode respects AGENTSHROUD_MODE env var., Test that pinned modules always return enforce even in monitor mode., Test SecurityPipeline.set_global_mode method., Test set_global_mode handles missing components gracefully., Test that observatory mode state is properly initialized., Test module mode resolution with pinned modules., Test validation of observatory mode parameters. (+2 more)

### Community 956 - "test_progressive_lockdown.py"
Cohesion: 0.16
Nodes (7): FakePipelineResult, FakeRBAC, PassthroughPipeline, asyncio, Tests for progressive lockdown UX fixes. Covers: 1. ProgressiveLockdown unit…, TestLifespanWiring, TestTelegramProxyInjection

### Community 957 - "TestMultiBotIsolation"
Cohesion: 0.11
Nodes (5): Verify that different bots get independent workspaces per user., openclaw and hermes sessions for the same user must not share a directory., Existing plain user_id keys (no separator) are promoted to user::openclaw., If legacy users/{uid}/MEMORY.md exists, first openclaw session copies it., TestMultiBotIsolation

### Community 958 - "Turbo Fieldfare (MLX inference backend)"
Cohesion: 0.31
Nodes (9): MoE (Mixture-of-Experts) Streaming Inference, oMLX (local model backend), Turbo Fieldfare (MLX inference backend), Turbo Fieldfare GitHub Issue #84 (decoder_consume bug), Newsletter: Local Inference Engines, Newsletter: MoE Streaming / SSD Offload, oMLX MoE Streaming Health Check, Today in AI (Daily Newsletter) (+1 more)

### Community 959 - "Discord (Via `message`)"
Cohesion: 0.22
Nodes (8): Common Actions (Examples), Discord (Via `message`), Guidelines, Musts, Targets, Writing Style (Discord), Discord Components v2 preferred over legacy embeds, message tool (channel=discord)

### Community 960 - "Skill: Git Workflow Guardian (GIT-GUARD)"
Cohesion: 0.22
Nodes (8): Branch Naming, Commit Messages  (Conventional Commits), Emergency Hotfix, Mandatory Workflow  (10 steps), Protected Branch, REFUSE These, Role, Skill: Git Workflow Guardian (GIT-GUARD)

### Community 961 - "_patch_open"
Cohesion: 0.16
Nodes (7): _patch_open(), EPERM means the process exists but is owned by another user., Stale PID (ESRCH) is not EPERM — falls through to /proc scan, then standby., Intercept builtins.open for specific paths; delegate everything else., TestCheckFluentBit, TestCheckWazuhAgent, _kill()

### Community 962 - ".test_fetch_paginates_via_link_cursor"
Cohesion: 0.14
Nodes (4): aquasecurity/trivy 403s the Actions token but serves the public feed., TestFetch, _fake_urlopen(), _fake_urlopen()

### Community 963 - "Vulcan — Subject Matter Auditor"
Cohesion: 0.22
Nodes (8): Input Requirements, Output Format, Persona, Quality Checklist, Role, System Prompt, User Prompt Template, Vulcan — Subject Matter Auditor

### Community 964 - "Skill: Git Workflow Guardian (GIT-GUARD)"
Cohesion: 0.22
Nodes (8): Branch Naming, Commit Messages  (Conventional Commits), Emergency Hotfix, Mandatory Workflow  (10 steps), Protected Branch, REFUSE These, Role, Skill: Git Workflow Guardian (GIT-GUARD)

### Community 965 - "MCPProxy"
Cohesion: 0.06
Nodes (27): MCPProxyConfig, Top-level MCP proxy configuration., MCPProxy, _add(), _walk(), _scrub(), Any, Send an HTTP request to the MCP server. (+19 more)

### Community 966 - "Skill: Pull Request (PR) Generator"
Cohesion: 0.22
Nodes (8): Constraints, Content Requirements, Header, Objective, Role, Safety, Skill: Pull Request (PR) Generator, Technical Detail

### Community 967 - "TestReplayBufferOffsetParsing"
Cohesion: 0.15
Nodes (10): Tests that _forward_to_telegram uses correct urlopen timeouts. Regression guard…, Return a urlopen mock that records the timeout kwarg and succeeds., sendMessage and similar calls must use a 15s urlopen timeout., getUpdates must use a 60s urlopen timeout so the long-poll is not aborted early., Verify URL-encoded and JSON getUpdates bodies both trigger mark_delivered…, URL-encoded getUpdates body must call mark_delivered with the correct int…, JSON getUpdates body must still call mark_delivered (existing behaviour…, TestForwardToTelegramTimeouts (+2 more)

### Community 968 - "AgentShroud Gateway (holds 1Password service account)"
Cohesion: 0.22
Nodes (9): 1Password (trusted for secrets, gateway-only access), AgentShroud Bot (no direct credential/internet access), AgentShroud Gateway (holds 1Password service account), Isaiah Jefferson (full control), Trust Zone 0 — Owner (Highest Trust), Trust Zone 1 — Gateway (Trusted Enforcer), Trust Zone 2 — Bot (Supervised Agent), Trust Zone 3 — External Services (Conditional) (+1 more)

### Community 969 - "AgentShroud Data Flow Diagrams (doc)"
Cohesion: 0.22
Nodes (9): Diagram 11: Trust Boundary, Diagram 13: Network Security Egress, Diagram 14: Logic Flow, Audit Ledger (blockchain-style chain), AgentShroud Data Flow Diagrams (doc), Kill Switch (Level 1 security component), MCP Proxy Detailed Flow (tool call inspection, permission check, rate limit, forward, result inspection), PII Sanitizer (Level 1 security component) (+1 more)

### Community 970 - "Claude Code (claude-sonnet-4-6) — Lead Engineer / Primary Developer"
Cohesion: 0.39
Nodes (9): AgentShroud Bot (@agentshroud_bot) — Autonomous Agent (Prod), ChatGPT Codex — QA / Support Engineer / Tertiary Developer, Claude Code (claude-sonnet-4-6) — Lead Engineer / Primary Developer, ChatGPT/Codex — Tertiary/QA Support Engineer (cannot direct Claude), Team/Agent Role Structure Diagram, Gemini CLI — Secondary/Test Engineer (cannot direct Claude), Gemini CLI — Test Engineer / Secondary Developer, Isaiah Jefferson — Product Owner/Architect/PM/Operator (+1 more)

### Community 971 - "Threat Model"
Cohesion: 0.20
Nodes (10): 1. Command Injection, 2. Host Spoofing / Man-in-the-Middle, 3. Credential Theft, 4. Privilege Escalation, 5. Denial of Service, 6. Audit Log Tampering / PII Leakage, Threat Model, D - Denial of Service (+2 more)

### Community 972 - "Voice Terminal Main IDF Component Manifest"
Cohesion: 0.50
Nodes (4): Voice Terminal Main Component CMakeLists (app_main, audio, ota, ui_face), Voice Terminal Main IDF Component Manifest, esp-box-3 BSP v3.2.0 (Board Support Package), esp-sr Speech Recognition Library (WakeNet WN9)

### Community 973 - "test_multi_host_test.py"
Cohesion: 0.24
Nodes (8): Path, Tests for multi_host_test — host parsing + result aggregation (no real SSH)., _run_wrapper(), TestParserAndCommandResolution, TestWrapperSubprocess, _write_exec(), build_parser(), ArgumentParser

### Community 974 - "AgentShroud Red Team Adversarial Tester"
Cohesion: 0.11
Nodes (17): Adversary Model, AgentShroud Red Team Adversarial Tester, Attack Phases, Attack Techniques Reference, Coverage Requirements, Critical Rules, Infrastructure, Key Principle (+9 more)

### Community 975 - "Socrates — Dialogue Architect"
Cohesion: 0.11
Nodes (17): Dialogue Adaptations, Dialogue Techniques, ElevenLabs v3 Audio Tags, Episode Closing (Mandatory for OKE), EXPERT, Expert Persona, HOST, Input Requirements (+9 more)

### Community 976 - "session-prompt-setup.sh"
Cohesion: 0.27
Nodes (17): _fail(), _hdr(), _info(), _inject_all(), _inject_block(), main(), _ok(), _parse_args() (+9 more)

### Community 977 - "AgentShroud™ Communication Templates"
Cohesion: 0.20
Nodes (10): AgentShroud™ Communication Templates, Claude Code (primary developer), For Agents and Bots, Gemini CLI / ChatGPT Codex (secondary agents), OpenClaw Bot (agentshroud-bot), Option 1 — Clean & Professional, Option 2 — Compact, Option 3 — Full Collaborator Notice (+2 more)

### Community 978 - "AgentShroud Red Team Adversarial Tester"
Cohesion: 0.11
Nodes (17): Adversary Model, AgentShroud Red Team Adversarial Tester, Attack Phases, Attack Techniques Reference, Coverage Requirements, Critical Rules, Infrastructure, Key Principle (+9 more)

### Community 979 - "Socrates — Dialogue Architect"
Cohesion: 0.11
Nodes (17): Dialogue Adaptations, Dialogue Techniques, ElevenLabs v3 Audio Tags, Episode Closing (Mandatory for OKE), EXPERT, Expert Persona, HOST, Input Requirements (+9 more)

### Community 980 - "AgentShroud Red Team Adversarial Tester"
Cohesion: 0.11
Nodes (17): Adversary Model, AgentShroud Red Team Adversarial Tester, Attack Phases, Attack Techniques Reference, Coverage Requirements, Critical Rules, Infrastructure, Key Principle (+9 more)

### Community 981 - "4. Defense-in-Depth Container Security"
Cohesion: 0.22
Nodes (9): 4.1 Build-Time Image Scanning (Trivy), 4.2 Runtime Malware Detection (ClamAV), 4.3 Runtime Syscall Monitoring (Falco), 4.4 Host Integrity Monitoring (Wazuh), 4.5 Compliance Scanning (OpenSCAP), 4.6 Daily Security Health Report, 4.7 Zero-Configuration Security, 4.8 Container Security — Competitive Comparison (+1 more)

### Community 982 - "v0.9.0 "Sentinel" — Data Isolation + SOC + Remediation (37 items)"
Cohesion: 0.22
Nodes (9): 🟡 Apple Messages Integration (4 items), 🟢 Development Infrastructure (4 items), 🟢 Infrastructure (5 items), 🟢 Multi-Agent Architecture (3 items), 🔴 Private Service Data Isolation (6 items), 🔴 Security Operations Center (SOC) (6 items), 🟡 Security Tools — Full Integration (5 items), 🟡 Steve Hay Remediation (4 items) (+1 more)

### Community 983 - "v0.8.0 "Watchtower" — Security Fixes + Module Wiring (104 items)"
Cohesion: 0.22
Nodes (9): 🔧 Code Quality (2 items), 📊 Exit Criteria (5 items), Gateway Pipeline, Module Enforcement, 🔴 P0 — Security Fixes (17 items), 🟡 P1 — High Priority (8 items), 🟢 P2 — Quick Wins (11 items), Prompt Injection Hardening (+1 more)

### Community 984 - "AgentShroud Sunday Upgrade — 2026-09-23 (DEV run)"
Cohesion: 0.12
Nodes (16): 0. Concurrency finding (read this first), 10. Security findings — unresolved from prior sessions, not newly regressed, 11. Breaking changes / manual follow-ups (for Isaiah), 12. Rollback instructions, 13. Time spent, 1. Preflight / environment mapping, 2. Inventory / upstream discovery (mechanical, read-only), 3. Colima socket-forward death — recurred live, during this session (+8 more)

### Community 985 - "Socrates — Dialogue Architect"
Cohesion: 0.11
Nodes (17): Dialogue Adaptations, Dialogue Techniques, ElevenLabs v3 Audio Tags, Episode Closing (Mandatory for OKE), EXPERT, Expert Persona, HOST, Input Requirements (+9 more)

### Community 986 - "test_deployment_mode.py"
Cohesion: 0.16
Nodes (15): _asb_setup(), _bash(), CompletedProcess, parametrize, Run scripts/asb's real _deployment_setup and report the variables it leaves., Deployment mode (AGENTSHROUD_DEPLOYMENT): local agents, hosted (cloud) agents,…, test_asb_cloud_mode_drops_local_agents_even_for_full(), test_asb_hybrid_mode_adds_edge_to_full_stack() (+7 more)

### Community 987 - "AgentShroud Red Team Adversarial Tester"
Cohesion: 0.11
Nodes (17): Adversary Model, AgentShroud Red Team Adversarial Tester, Attack Phases, Attack Techniques Reference, Coverage Requirements, Critical Rules, Infrastructure, Key Principle (+9 more)

### Community 988 - "Actions"
Cohesion: 0.11
Nodes (17): Action groups, Actions, Delete a message, Edit a message, Emoji list, Ideas to try, Inputs to collect, List pinned items (+9 more)

### Community 989 - "generate-job-schedule.py"
Cohesion: 0.36
Nodes (9): describe_cron(), docker_exec(), fmt_ts(), load_hermes_jobs(), load_openclaw_jobs(), main(), Generate docs/job-schedule.html from Hermes + OpenClaw's live cron state. Reads…, Best-effort plain-language gloss of a 5-field cron expression. (+1 more)

### Community 990 - "tmux Session Control"
Cohesion: 0.11
Nodes (17): Approve Claude Code Prompt, Capture Output, Check All Sessions Status, Check if Session Needs Input, Claude Code Session Patterns, Common Commands, Example Sessions, List Sessions (+9 more)

### Community 991 - "switch_model.sh"
Cohesion: 0.42
Nodes (8): ensure_local_model_available(), normalize_cloud_ref(), preflight_local(), switch_model.sh script, upsert_env_value(), usage(), verify_both_bots_healthy(), wait_for_local_model()

### Community 992 - "STRIDE Threat Analysis"
Cohesion: 0.22
Nodes (9): R - Repudiation, S - Spoofing Identity, STRIDE Threat Analysis, T - Tampering with Data, Threat: Agent Identity Spoofing, Threat: API Key Impersonation, Threat: Audit Log Tampering, Threat: Configuration Drift (+1 more)

### Community 993 - "Atlas — Curriculum Architect"
Cohesion: 0.12
Nodes (16): Atlas — Curriculum Architect, Coverage Types, CPA Curriculum Frontmatter Addition, Episode Closing, Exam Weight Integration, Gleim Unit Mapping, Input Requirements, Mandatory Acronym Expansion (+8 more)

### Community 994 - "Phase 3: MITIGATE (Rollback First!)"
Cohesion: 0.12
Nodes (16): Follow-up (within 48 hours), Glue Job Rollback, Immediate (within 2 hours), Incident Response Workflow, Phase 1: ASSESS (Max 5 minutes), Phase 2: COMMUNICATE (Concurrent with assess), Phase 3: MITIGATE (Rollback First!), Post-Incident (+8 more)

### Community 995 - "Atlas — Curriculum Architect"
Cohesion: 0.12
Nodes (16): Atlas — Curriculum Architect, Coverage Types, CPA Curriculum Frontmatter Addition, Episode Closing, Exam Weight Integration, Gleim Unit Mapping, Input Requirements, Mandatory Acronym Expansion (+8 more)

### Community 996 - "properties"
Cohesion: 0.12
Nodes (17): maximum, minimum, type, maximum, minimum, type, additionalProperties, properties (+9 more)

### Community 997 - "Atlas — Curriculum Architect"
Cohesion: 0.12
Nodes (16): Atlas — Curriculum Architect, Coverage Types, CPA Curriculum Frontmatter Addition, Episode Closing, Exam Weight Integration, Gleim Unit Mapping, Input Requirements, Mandatory Acronym Expansion (+8 more)

### Community 998 - "Phase 3: MITIGATE (Rollback First!)"
Cohesion: 0.12
Nodes (16): Follow-up (within 48 hours), Glue Job Rollback, Immediate (within 2 hours), Incident Response Workflow, Phase 1: ASSESS (Max 5 minutes), Phase 2: COMMUNICATE (Concurrent with assess), Phase 3: MITIGATE (Rollback First!), Post-Incident (+8 more)

### Community 999 - "Layer-by-Layer Breakdown"
Cohesion: 0.12
Nodes (17): 10. Approval Queue, 11. Ledger Recording, 1. MCP Proxy Wrapper (Bot Side), 2. Authentication (Gateway Entry), 3. Middleware Manager, 4. Input Normalization, 5. PII Sanitization, 6. Prompt Injection Defense (+9 more)

### Community 1000 - "middleware.py"
Cohesion: 0.12
Nodes (16): Config Keys Read, Environment Variables Used, Extended v0.8.0 Modules, FileSandbox Configuration (hardcoded in __init__), Imports From / Exports To, Key Classes / Functions, Known Issues / Notes, Memory Security (+8 more)

### Community 1001 - "models.py"
Cohesion: 0.12
Nodes (16): AgentTarget, Config Keys Read, EmailSendRequest, Environment Variables Used, ForwardRequest, ForwardResponse, Imports From / Exports To, Key Classes / Functions (+8 more)

### Community 1002 - "clamav_scanner.py"
Cohesion: 0.12
Nodes (16): clamav_scanner.py, Configuration, Environment Variables, Error Handling, Function Details, generate_summary(report), Key Classes / Functions, Mode: Enforce vs Monitor (+8 more)

### Community 1003 - "7. Pi-hole DNS Security Layer (Built-In)"
Cohesion: 0.29
Nodes (7): 7. Pi-hole DNS Security Layer (Built-In), AgentShroud Web Console Integration, Architecture, Configuration, Default Blocklists (Auto-Updated), Deliverables, Design Philosophy

### Community 1004 - "AgentShroud v1.2.0 — Blue Team Security Assessment"
Cohesion: 0.20
Nodes (9): §1 — Re-audit of v0.8.0 Prior Findings, §2 — New v1.2.0 Findings (OpenClaw-specific), §6 — SAST (Semgrep) Status, §7 — Summary Table, §8 — Regression Tests, AgentShroud v1.2.0 — Blue Team Security Assessment, Method, Previously FIXED findings — verification (+1 more)

### Community 1005 - "AgentShroud v1.2.0 — Red Team Assessment"
Cohesion: 0.22
Nodes (8): §3 — SAST Scan Summary, §4 — Findings Summary, §5 — Acceptance Rationales (Signed Off), §6 — Regression Test Index, AgentShroud v1.2.0 — Red Team Assessment, Methodology note, RT-00 — Tool inventory disclosure, RT-MB4 — Hermes cron job injection via jobs.yaml

### Community 1006 - "server.py"
Cohesion: 0.08
Nodes (37): switch_model.sh main flow, _answer_volume_query(), _effective_voice_model(), firmware_bin(), _get_firmware_etag(), health(), _is_volume_query(), _keepalive() (+29 more)

### Community 1007 - "Function Details"
Cohesion: 0.12
Nodes (16): calculate_overall_score(summaries), calculate_tool_score(summary), Configuration / Environment Variables, format_report(report), Function Details, generate_report(summaries, db_path, save_history), get_trend(days, db_path), health_report.py (+8 more)

### Community 1008 - "prompt_guard.py"
Cohesion: 0.12
Nodes (16): Configuration, Dependencies, Environment Variables, Function Details, Key Classes / Functions, Mode: Enforce vs Monitor, Pattern Categories and Weights, prompt_guard.py (+8 more)

### Community 1009 - "Function Details"
Cohesion: 0.12
Nodes (16): Configuration / Environment Variables, Function Details, Key Classes / Functions, Purpose, Related, Responsibilities, subagent_monitor.py, SubagentMonitor.check_tool_usage(session_id, agent_id, tool_name, required_trust) (+8 more)

### Community 1010 - "Gateway Python Dependencies (`gateway/requirements.txt`)"
Cohesion: 0.12
Nodes (16): All Dependencies, Authentication, Bot / Docker Container Dependencies, Configuration, Core Framework, Data Storage, Dependency Notes, Gateway Python Dependencies (`gateway/requirements.txt`) (+8 more)

### Community 1011 - "CredentialInjectorConfig"
Cohesion: 0.16
Nodes (8): CredentialInjectorConfig, CredentialMapping, Credential Injector — transparent credential injection for outbound requests.…, Maps a destination domain to its credential injection config., Configuration for the credential injector., Default Anthropic mapping must strip x-api-key (regression guard)., strip_headers must remove x-api-key before injecting Authorization: Bearer., TestCredentialInjection

### Community 1012 - "TestRewriteRequestHeaders"
Cohesion: 0.12
Nodes (9): bridge_module(), fixture, Tests for the Hermes dashboard bridge's HTTP header rewrite (2026-07 502/400…, Forcing Connection: close makes every request single-shot per TCP connection,…, A WebSocket upgrade MUST keep Connection: Upgrade (not close) or the handshake…, relay_module(), TestDockerProxyRelayHalfClose, scenario() (+1 more)

### Community 1013 - "TestStartupScannerKeying"
Cohesion: 0.23
Nodes (8): Simulate the _store_result keying logic from lifespan._startup_scanner. The…, Reproduce the _store_result closure from lifespan.py., trivy' key is always stored for backward compat (SOC /scanners endpoint)., trivy:fs:/app' key is stored for per-target access., Per-image compound keys are independent — last image doesn't clobber first., Summary status is derived correctly for compound 'trivy:image:...' keys., Each _store_result call appends an entry to scanner_result_history., TestStartupScannerKeying

### Community 1014 - "TestAtomicRegistryWrites"
Cohesion: 0.12
Nodes (8): Registry writes must be atomic (os.replace) and serialized (lock). The session…, _save_sessions must go through os.replace(tmp, final), never a partial in-place…, A successful save leaves only the final registry file, no *.tmp., A corrupt/partial registry file must not crash construction., An empty registry file must not crash construction., If the write to the temp file fails mid-flight, the existing registry on disk…, Concurrent add_conversation_message calls (each of which saves) must not drop…, TestAtomicRegistryWrites

### Community 1015 - "Atlas — Curriculum Architect"
Cohesion: 0.12
Nodes (16): Atlas — Curriculum Architect, Coverage Types, CPA Curriculum Frontmatter Addition, Episode Closing, Exam Weight Integration, Gleim Unit Mapping, Input Requirements, Mandatory Acronym Expansion (+8 more)

### Community 1016 - "Features"
Cohesion: 0.13
Nodes (13): Action Feed, Data Ledger Viewer, Features, Kill Switch, Memory Browser, Network Inspector, Read-Only Filesystem (Planned), Secret Management Hierarchy (1Password → Docker Secrets → Env) (+5 more)

### Community 1017 - "Phase 3: MITIGATE (Rollback First!)"
Cohesion: 0.12
Nodes (16): Follow-up (within 48 hours), Glue Job Rollback, Immediate (within 2 hours), Incident Response Workflow, Phase 1: ASSESS (Max 5 minutes), Phase 2: COMMUNICATE (Concurrent with assess), Phase 3: MITIGATE (Rollback First!), Post-Incident (+8 more)

### Community 1018 - "Hermes Dev Workflow (HDEV) Skill"
Cohesion: 0.17
Nodes (13): Git Workflow Guardian (GIT-GUARD) README, GIT-GUARD Skill, gitops Skill (stub), Hermes Dev Workflow (HDEV) Skill, OpenClaw Dev Workflow (ODEV), agentshroud-ssh-exec.sh (gateway SSH wrapper), agentshroud-ssh-write-file.sh (gateway SSH wrapper), Codex CLI (codex exec / Codex -p) (+5 more)

### Community 1019 - "Atlas — Curriculum Architect"
Cohesion: 0.12
Nodes (16): Atlas — Curriculum Architect, Coverage Types, CPA Curriculum Frontmatter Addition, Episode Closing, Exam Weight Integration, Gleim Unit Mapping, Input Requirements, Mandatory Acronym Expansion (+8 more)

### Community 1020 - "Phase 3: MITIGATE (Rollback First!)"
Cohesion: 0.12
Nodes (16): Follow-up (within 48 hours), Glue Job Rollback, Immediate (within 2 hours), Incident Response Workflow, Phase 1: ASSESS (Max 5 minutes), Phase 2: COMMUNICATE (Concurrent with assess), Phase 3: MITIGATE (Rollback First!), Post-Incident (+8 more)

### Community 1021 - "Security Review (SEC)"
Cohesion: 0.22
Nodes (6): Purpose, Related Skills, Security Review (SEC), Usage, security-reviewer, security-reviewer

### Community 1022 - "Key Skills in Detail"
Cohesion: 0.25
Nodes (8): 4. Skill System, 59 Skills by Category, `/cr` — Code Review, `/gg` — Git Workflow Guardian, Key Skills in Detail, `/sec-defense` — Blue Team STPA-Sec Auditor, `/sec-offense` — Red Team Adversarial Tester, `/tdd` — Test-Driven Development Coach

### Community 1023 - "Atlas — Curriculum Architect"
Cohesion: 0.12
Nodes (16): Atlas — Curriculum Architect, Coverage Types, CPA Curriculum Frontmatter Addition, Episode Closing, Exam Weight Integration, Gleim Unit Mapping, Input Requirements, Mandatory Acronym Expansion (+8 more)

### Community 1024 - "EU AI Act & NIST Alignment Matrix — AgentShroud™"
Cohesion: 0.25
Nodes (7): 1. EU AI Act — high-risk operational requirements, 2. NIST AI RMF 1.0 mapping, 3. NIST AI Agent Standards Initiative (2026) — identity & authorization themes, 4. Honest gap list (with tracking), 5. Evidence trail — where an auditor looks, EU AI Act & NIST Alignment Matrix — AgentShroud™, Positioning

### Community 1025 - "AgentShroud Hermes — System Identity"
Cohesion: 0.25
Nodes (7): AgentShroud Hermes — System Identity, Capabilities, Core Behaviors, Owner, Remote Hosts (SSH via gateway), Trademark Notice, Your Role

### Community 1026 - "Sunday Upgrade 2026-11-01 (DEV run, account agentshroud-bot)"
Cohesion: 0.14
Nodes (13): 1. Summary line, 2. Environment mapping, 3. Upgrade table, 3a. Per-component change report, 3b. Not updated this run — plan for the week, 4. Security findings, 5. Verification evidence, 6. Breaking changes / needs human (+5 more)

### Community 1027 - "Oracle — Feedback Analyst"
Cohesion: 0.25
Nodes (7): Input Requirements, Oracle — Feedback Analyst, Output Format, Persona, Quality Checklist, Role, System Prompt

### Community 1028 - "AgentShroud Hermes — System Identity"
Cohesion: 0.25
Nodes (7): AgentShroud Hermes — System Identity, Capabilities, Core Behaviors, Owner, Remote Hosts (SSH via gateway), Trademark Notice, Your Role

### Community 1030 - "Phase 3: MITIGATE (Rollback First!)"
Cohesion: 0.12
Nodes (16): Follow-up (within 48 hours), Glue Job Rollback, Immediate (within 2 hours), Incident Response Workflow, Phase 1: ASSESS (Max 5 minutes), Phase 2: COMMUNICATE (Concurrent with assess), Phase 3: MITIGATE (Rollback First!), Post-Incident (+8 more)

### Community 1031 - "Himalaya Configuration Reference"
Cohesion: 0.12
Nodes (16): Additional Options, Downloads directory, Editor for composing, Folder Aliases, Gmail Configuration, Himalaya Configuration Reference, iCloud Configuration, Minimal IMAP + SMTP Setup (+8 more)

### Community 1032 - "Common Queries"
Cohesion: 0.12
Nodes (16): Common Queries, Count messages and tokens in a session, Daily cost summary, Extract user messages from a session, Fast text-only hint (low noise), Find sessions from a specific day, Get total cost for a session, List all sessions by date and size (+8 more)

### Community 1033 - "test_colima_and_sdk_patch_fallback_resolution.sh"
Cohesion: 0.17
Nodes (8): _bounce(), check(), _hc(), hc_run(), _mk(), _render_build(), test_colima_and_sdk_patch_fallback_resolution.sh script, _wait_result()

### Community 1034 - "Output Sections (ALL required)"
Cohesion: 0.12
Nodes (15): 1. Scope of Change, 2. What Changes and Why, 3. Scalability Gate, 4. Blast Radius, 5. Known Limits and Assumptions, 6. Alternatives Considered, 7. Open Questions, 8. Verification Plan (+7 more)

### Community 1035 - "properties"
Cohesion: 0.12
Nodes (16): enum, maxLength, minLength, type, type, type, properties, connection (+8 more)

### Community 1036 - "Planning Docs Index (redteam, reviews, recovery, version buckets)"
Cohesion: 0.22
Nodes (10): AgentShroud Blue #1583f0, Master Feature List (historical index), Planning Docs Index (redteam, reviews, recovery, version buckets), Recovery Plan v0.4.0 — Systematic Stabilization, XML Function-Call Block Filter (filter_xml_blocks) — Response Sanitization, Credential Isolation via op-proxy — Gateway as Sole 1Password Broker, Security Hardening Plan Reset — Real Agent Containment v0.8, Network Lockdown FINAL Phase — agentshroud-isolated internal:true + HTTP_PROXY (+2 more)

### Community 1037 - "SECTION 1: COVER SHEET (Form PTO/SB/16)"
Cohesion: 0.25
Nodes (8): 1.1 Application Type, 1.2 Inventor(s), 1.3 Title of Invention, 1.4 Correspondence Address, 1.5 Attorney/Agent (if applicable), 1.6 U.S. Government Interest, 1.7 Entity Status, SECTION 1: COVER SHEET (Form PTO/SB/16)

### Community 1038 - "SECTION 3: DRAWINGS"
Cohesion: 0.25
Nodes (8): Drawing Preparation Checklist, FIGURE 1 — System Context Diagram, FIGURE 2 — Security Pipeline Flow Diagram, FIGURE 3 — Approval Queue Flow Diagram, FIGURE 4 — Trust-Differentiated Processing, FIGURE 5 — Multi-Agent Governance with Isolation, FIGURE 6 — Delegated Authority Model, SECTION 3: DRAWINGS

### Community 1039 - "ota.c"
Cohesion: 0.33
Nodes (7): esp_http_client_event_t, esp_err_t, _http_event_handler(), _nvs_get_etag(), _nvs_set_etag(), ota_check(), _ws_to_https_base()

### Community 1040 - "Output Sections (ALL required)"
Cohesion: 0.12
Nodes (15): 1. Scope of Change, 2. What Changes and Why, 3. Scalability Gate, 4. Blast Radius, 5. Known Limits and Assumptions, 6. Alternatives Considered, 7. Open Questions, 8. Verification Plan (+7 more)

### Community 1041 - "Himalaya Email CLI"
Cohesion: 0.12
Nodes (13): Configuration Entities, ConfigurationSetting, Attachments, Configuration Setup, Debugging, Himalaya Email CLI, Multiple Accounts, Output Formats (+5 more)

### Community 1042 - "_run"
Cohesion: 0.16
Nodes (9): parametrize, Path, scripts/update-conduit-push.sh — pinned installer for Hermes's conduit_push…, _run(), TestPinIsValidated, TestProvesTheOutcome, TestRepoPin, TestUpgrade (+1 more)

### Community 1043 - "auth.py"
Cohesion: 0.12
Nodes (15): auth.py, Config Keys Read, create_auth_dependency(config), Environment Variables Used, Function Details, get_auth_dependency(config), HTTP Responses, Imports From / Exports To (+7 more)

### Community 1044 - "TestAggregateResults"
Cohesion: 0.39
Nodes (3): Any, _stub_summary(), TestAggregateResults

### Community 1045 - "ledger.py"
Cohesion: 0.12
Nodes (13): Config Keys Read, Database Schema, Environment Variables Used, Function Details, Imports From / Exports To, Key Classes / Functions, Known Issues / Notes, ledger.py (+5 more)

### Community 1046 - "sanitizer.py"
Cohesion: 0.12
Nodes (15): block_credentials(content, source), Config Keys Read, Environment Variables Used, filter_xml_blocks(content), Function Details, Imports From / Exports To, Key Classes / Functions, Known Issues / Notes (+7 more)

### Community 1047 - "version_routes.py"
Cohesion: 0.12
Nodes (14): Config Keys Read, downgrade_version(request), Environment Variables Used, Function Details, Imports From / Exports To, Key Classes / Functions, Known Issues / Notes, Purpose (+6 more)

### Community 1048 - "Function Details"
Cohesion: 0.12
Nodes (15): Configuration / Environment Variables, Function Details, Key Classes / Functions, mcp_permissions.py, MCPPermissionManager.check_agent_server_access(agent_id, server_name), MCPPermissionManager.check_all(agent_id, server_name, tool_name), MCPPermissionManager.check_rate_limit(agent_id, server_name, tool_name), MCPPermissionManager.check_tool_permission(agent_id, server_name, tool_name) (+7 more)

### Community 1049 - "apple_engine.py"
Cohesion: 0.12
Nodes (14): Apple Containers vs Docker/Podman, apple_engine.py, AppleContainerEngine.compose_up(file, detach) / compose_down(file), AppleContainerEngine.inspect(name), AppleContainerEngine.network_create / network_rm / volume_create / volume_rm, AppleContainerEngine.pause(name) / unpause(name), AppleContainerEngine.ps(all), AppleContainerEngine.run(image, name, *, ports, volumes, env, privileged, caps, seccomp, detach, ...) (+6 more)

### Community 1050 - "Function Details"
Cohesion: 0.12
Nodes (13): Configuration / Environment Variables, Function Details, Key Classes / Functions, Key Differences from DockerEngine, podman_engine.py, PodmanEngine.compose_up(file, detach) / compose_down(file), PodmanEngine.generate_systemd(name), PodmanEngine.__init__(cli) (+5 more)

### Community 1051 - "agent_isolation.py"
Cohesion: 0.12
Nodes (11): agent_isolation.py, ContainerConfig Defaults, Environment Variables, Function Details, Integration Notes, Key Classes / Functions, Mode: Enforce vs Monitor, Purpose (+3 more)

### Community 1052 - "dns_filter.py"
Cohesion: 0.12
Nodes (15): Allowlist Behavior, Audit Log, Configuration (DNSFilterConfig), dns_filter.py, DNSFilter.check(domain, agent_id), DNSFilter._detect_tunneling(domain), EntropyCalculator.shannon_entropy(s), Environment Variables (+7 more)

### Community 1053 - "wazuh_client.py"
Cohesion: 0.12
Nodes (15): Configuration / Environment Variables, Function Details, generate_summary(alerts), get_fim_events(alerts) / get_rootkit_events(alerts), Key Classes / Functions, Key Rule ID Sets, level_to_severity(level), parse_alert(raw) (+7 more)

### Community 1054 - "ANTHROPIC_BASE_URL"
Cohesion: 0.12
Nodes (14): ANTHROPIC_BASE_URL, Description, How It Works, Related Notes, SDK Patch, Set In, Value, Why It's Critical (+6 more)

### Community 1055 - "Attack Teardowns: How AgentShroud Stops RovoBlast and Cross-Turn Coordination Attacks"
Cohesion: 0.25
Nodes (7): Attack Teardowns: How AgentShroud Stops RovoBlast and Cross-Turn Coordination Attacks, Honest gap, Part 1 — RovoBlast: how AgentShroud's pipeline would have stopped it, Part 2 — Cross-turn correlation: the differentiator, made concrete, What actually happened, What this document does NOT cover (explicitly out of scope here), Where AgentShroud's pipeline breaks each stage

### Community 1056 - "agentshroud-bot"
Cohesion: 0.12
Nodes (15): agentshroud-bot, Container Properties, Extra Hosts, Health Check, Key Environment Variables, Logs, Network, Ports (+7 more)

### Community 1057 - "agentshroud-gateway"
Cohesion: 0.12
Nodes (15): agentshroud-gateway, Container Properties, Environment Variables, Health Check, Key Endpoints, Logs, Networks, Ports (+7 more)

### Community 1058 - "PathRewriteResult"
Cohesion: 0.16
Nodes (10): PathRewriteResult, Result of path rewriting operation., Test path isolation configuration., Test default configuration values., Test PathRewriteResult dataclass., Test basic result creation., Test blocked result creation., Test custom configuration values. (+2 more)

### Community 1059 - "TestMemoryIntegrityMonitor"
Cohesion: 0.12
Nodes (9): Test monitoring a new file., Test detection of unauthorized modifications., Test write grace window prevents false alerts., Test integrity database saves and loads correctly., Test memory integrity monitoring., Set up test environment., Clean up test environment., Test file hash computation. (+1 more)

### Community 1060 - "_FakeRBAC"
Cohesion: 0.17
Nodes (4): _FakeRBAC, Deterministic stand-in for RBACManager., TestIsOwner, TestProcessRequestRBAC

### Community 1061 - "TestWebSocketHandshakeAuth"
Cohesion: 0.12
Nodes (9): WebSocket endpoints must validate token during handshake, not first message, WS /ws/approvals closes immediately without token, WS /ws/approvals closes with bad token, WS /ws/approvals rejects the master auth token -- R3-L4 removed the master-…, WS /ws/approvals accepts valid scoped WS token, WS /ws/activity closes immediately without token, WS /ws/activity closes with bad token, WS /ws/activity accepts valid scoped WS token (+1 more)

### Community 1062 - "_audit_entry"
Cohesion: 0.19
Nodes (4): _audit_entry(), SimpleNamespace, TestCollectRecentEvents, TestFromAuditChainEntry

### Community 1063 - "Output Sections (ALL required)"
Cohesion: 0.12
Nodes (15): 1. Scope of Change, 2. What Changes and Why, 3. Scalability Gate, 4. Blast Radius, 5. Known Limits and Assumptions, 6. Alternatives Considered, 7. Open Questions, 8. Verification Plan (+7 more)

### Community 1064 - "Output Sections (ALL required)"
Cohesion: 0.12
Nodes (15): 1. Scope of Change, 2. What Changes and Why, 3. Scalability Gate, 4. Blast Radius, 5. Known Limits and Assumptions, 6. Alternatives Considered, 7. Open Questions, 8. Verification Plan (+7 more)

### Community 1065 - "A2A (Agent-to-Agent) Protocol Threat Analysis"
Cohesion: 0.25
Nodes (8): A2A (Agent-to-Agent) Protocol Threat Analysis, E — Elevation of Privilege: Cross-Process Isolation Break, I — Information Disclosure / Elevation of Privilege: Unsandboxed Live-Session Injection, I — Information Disclosure: SSRF via Push-Notification Callback URLs, Not Yet Mitigated (Explicitly Deferred), R — Repudiation: Rejected Auth Attempts Not Audited, S — Spoofing: Peer Identity Collapse Behind a Reverse Proxy, T — Tampering: Cross-Tenant Task Ownership via `contextId` Collision

### Community 1066 - "ADR-001: Transparent Proxy Decision"
Cohesion: 0.25
Nodes (9): Agent Modification Approach (rejected alternative), ADR-001: Transparent Proxy Decision, ADR-004: Proxy-Side API Key Management, Deployment Modes, Proxy Mode (Recommended), Sidecar Mode (Performance Optimized), Gateway (FastAPI), PII Sanitizer (Presidio + Regex) (+1 more)

### Community 1067 - "Output Sections (ALL required)"
Cohesion: 0.12
Nodes (15): 1. Scope of Change, 2. What Changes and Why, 3. Scalability Gate, 4. Blast Radius, 5. Known Limits and Assumptions, 6. Alternatives Considered, 7. Open Questions, 8. Verification Plan (+7 more)

### Community 1068 - "Examples"
Cohesion: 0.12
Nodes (15): App + window management, Capture screenshots + analyze, Common capture parameters, Common motion/typing parameters, Common targeting parameters (most interaction commands), Examples, Features (all CLI capabilities, excluding agent/MCP), Keyboard input (+7 more)

### Community 1069 - "Skill: Audit Branch (AB) — Merge Regression Detection"
Cohesion: 0.13
Nodes (14): Check A — Substantive change on the losing side?, Check B — Tied to a real ticket?, Check C — Still broken at HEAD (not self-healed)?, Guardrails, Invocation Forms, Jira / PR Comment Format, Role, Skill: Audit Branch (AB) — Merge Regression Detection (+6 more)

### Community 1070 - "Skill: Create PR with Pre-Flight Audit (CRPR)"
Cohesion: 0.13
Nodes (14): Guardrails, Invocation, Role, Skill: Create PR with Pre-Flight Audit (CRPR), Step 0 — Pre-flight checks, Step 1 — Check for an in-progress merge, Step 2 — Merge without committing, Step 3 — Audit the pending merge (+6 more)

### Community 1071 - "System Audit & Documentation"
Cohesion: 0.13
Nodes (14): SECTION 10 — SHUTDOWN & RECOVERY SEQUENCE, SECTION 11 — KNOWN FAILURE MODES & TROUBLESHOOTING MATRIX, SECTION 12 — MERMAID FLOWCHART (Complete System Map), SECTION 13 — QUICK REFERENCE CARD, SECTION 1 — SYSTEM OVERVIEW (Plain English), SECTION 2 — COMPLETE FILE & DIRECTORY MAP, SECTION 3 — EVERY ENVIRONMENT VARIABLE, SECTION 4 — ALL EXTERNAL DEPENDENCIES (+6 more)

### Community 1072 - "AgentShroud Blue Team Security Auditor"
Cohesion: 0.13
Nodes (14): AgentShroud Blue Team Security Auditor, Audit Procedure, Critical Rules, Heat Map Legend, Infrastructure, Loss Categories, Methodology, Output Format (+6 more)

### Community 1073 - "System Audit & Documentation"
Cohesion: 0.13
Nodes (14): SECTION 10 — SHUTDOWN & RECOVERY SEQUENCE, SECTION 11 — KNOWN FAILURE MODES & TROUBLESHOOTING MATRIX, SECTION 12 — MERMAID FLOWCHART (Complete System Map), SECTION 13 — QUICK REFERENCE CARD, SECTION 1 — SYSTEM OVERVIEW (Plain English), SECTION 2 — COMPLETE FILE & DIRECTORY MAP, SECTION 3 — EVERY ENVIRONMENT VARIABLE, SECTION 4 — ALL EXTERNAL DEPENDENCIES (+6 more)

### Community 1074 - "SSH Proxy Threat Model (6 threats)"
Cohesion: 0.22
Nodes (10): Option 1: Direct SSH (current approach), Open Findings (C3-C5, H4-H7, M1-M5), SSH Allow/Deny List Evaluation Order, SSH Auto-Approve Commands, SSH Proxy Config Schema (agentshroud.yaml ssh: section), Command Injection Threat — regex + no-shell exec mitigation, Host Spoofing/MITM Threat — TOFU model residual risk, Production Deployment Recommendations (+2 more)

### Community 1075 - "AgentShroud Blue Team Security Auditor"
Cohesion: 0.13
Nodes (14): AgentShroud Blue Team Security Auditor, Audit Procedure, Critical Rules, Heat Map Legend, Infrastructure, Loss Categories, Methodology, Output Format (+6 more)

### Community 1076 - "Skill: Audit Branch (AB) — Merge Regression Detection"
Cohesion: 0.13
Nodes (14): Check A — Substantive change on the losing side?, Check B — Tied to a real ticket?, Check C — Still broken at HEAD (not self-healed)?, Guardrails, Invocation Forms, Jira / PR Comment Format, Role, Skill: Audit Branch (AB) — Merge Regression Detection (+6 more)

### Community 1077 - "Skill: Create PR with Pre-Flight Audit (CRPR)"
Cohesion: 0.13
Nodes (14): Guardrails, Invocation, Role, Skill: Create PR with Pre-Flight Audit (CRPR), Step 0 — Pre-flight checks, Step 1 — Check for an in-progress merge, Step 2 — Merge without committing, Step 3 — Audit the pending merge (+6 more)

### Community 1078 - "§3 — Bot Pipeline Integrity Checks"
Cohesion: 0.25
Nodes (8): 3.1 PII Sanitizer — confidence floor, 3.2 Egress filter — enforce mode, 3.3 form-urlencoded outbound bypass (PR#158 regression check), 3.4 KeyVault seeding includes Hermes secrets, 3.5 Telegram proxy multi-bot token validation, 3.6 CONNECT proxy force-blocks api.telegram.org, 3.7 agentshroud-isolated network isolation, §3 — Bot Pipeline Integrity Checks

### Community 1079 - "§1 — Re-run of Prior Scenarios"
Cohesion: 0.25
Nodes (8): §1 — Re-run of Prior Scenarios, Scenario 00 — Information Disclosure (Phase 0 finding), Scenario 01 — Enforce-by-Default, Scenario 02 — Human-in-the-Loop Bypass, Scenario 03 — Session Isolation, Scenario 04 — Separation of Privilege, Scenario 05 — Credential Isolation, Scenario 06 — Outbound Information Filter

### Community 1080 - "System Audit & Documentation"
Cohesion: 0.13
Nodes (14): SECTION 10 — SHUTDOWN & RECOVERY SEQUENCE, SECTION 11 — KNOWN FAILURE MODES & TROUBLESHOOTING MATRIX, SECTION 12 — MERMAID FLOWCHART (Complete System Map), SECTION 13 — QUICK REFERENCE CARD, SECTION 1 — SYSTEM OVERVIEW (Plain English), SECTION 2 — COMPLETE FILE & DIRECTORY MAP, SECTION 3 — EVERY ENVIRONMENT VARIABLE, SECTION 4 — ALL EXTERNAL DEPENDENCIES (+6 more)

### Community 1081 - "AgentShroud Blue Team Security Auditor"
Cohesion: 0.13
Nodes (14): AgentShroud Blue Team Security Auditor, Audit Procedure, Critical Rules, Heat Map Legend, Infrastructure, Loss Categories, Methodology, Output Format (+6 more)

### Community 1082 - "System Audit & Documentation"
Cohesion: 0.13
Nodes (14): SECTION 10 — SHUTDOWN & RECOVERY SEQUENCE, SECTION 11 — KNOWN FAILURE MODES & TROUBLESHOOTING MATRIX, SECTION 12 — MERMAID FLOWCHART (Complete System Map), SECTION 13 — QUICK REFERENCE CARD, SECTION 1 — SYSTEM OVERVIEW (Plain English), SECTION 2 — COMPLETE FILE & DIRECTORY MAP, SECTION 3 — EVERY ENVIRONMENT VARIABLE, SECTION 4 — ALL EXTERNAL DEPENDENCIES (+6 more)

### Community 1083 - "System Audit & Documentation"
Cohesion: 0.13
Nodes (14): SECTION 10 — SHUTDOWN & RECOVERY SEQUENCE, SECTION 11 — KNOWN FAILURE MODES & TROUBLESHOOTING MATRIX, SECTION 12 — MERMAID FLOWCHART (Complete System Map), SECTION 13 — QUICK REFERENCE CARD, SECTION 1 — SYSTEM OVERVIEW (Plain English), SECTION 2 — COMPLETE FILE & DIRECTORY MAP, SECTION 3 — EVERY ENVIRONMENT VARIABLE, SECTION 4 — ALL EXTERNAL DEPENDENCIES (+6 more)

### Community 1084 - "Deployment Runbook — AgentShroud"
Cohesion: 0.13
Nodes (14): 1. Pull Latest Code, 2. Run Tests, 3. Update Dependencies (if changed), 4. Build Containers, 5. Deploy, 6. Verify, Deployment Runbook — AgentShroud, Environment Variables (+6 more)

### Community 1085 - "Available MCP Servers"
Cohesion: 0.50
Nodes (4): 1. GitHub MCP, 2. Atlassian MCP (Jira + Confluence), 3. AWS API MCP, Available MCP Servers

### Community 1086 - "CI/CD Quality Gates (14 jobs, 6 workflows)"
Cohesion: 0.29
Nodes (7): CI/CD Pipeline Integration Guide, CI/CD Quality Gates (14 jobs, 6 workflows), Gap Analysis & Recommendations, "Get Shit Done" (GSD) Governance Cadence, Pre/Post Tool Hook Enforcement Layer, GitHub Actions CI (test + lint + security-scan), Git Worktrees (../agentshroud-worktrees/)

### Community 1087 - "Docker Compose (infra diagram)"
Cohesion: 0.29
Nodes (7): Docker Secrets Management (deployment doc), Docker Secrets Structure (/run/secrets/), Docker Compose (infra diagram), Docker Secrets (infra diagram), Named Docker Volumes, agentshroud-internal network (172.20.0.0/16), agentshroud-isolated network (172.21.0.0/16)

### Community 1088 - "Migration Path (SSH → Distributed Node)"
Cohesion: 0.29
Nodes (7): Migration Path (SSH → Distributed Node), Step 1: Verify Option 1 Working, Step 2: Install OpenClaw on Pi, Step 3: Pair Nodes, Step 4: Test Basic Communication, Step 5: Migrate Workflows, Step 6: Deprecate SSH (Optional)

### Community 1089 - "OpenClaw Control UI Pairing Instructions"
Cohesion: 0.13
Nodes (14): After Pairing, Alternative: Auto-Pairing URL, Cannot save token, Get Token Again, OpenClaw Control UI Pairing Instructions, Security Note, Step 1: Open the Control UI, Step 2: Open Settings (+6 more)

### Community 1090 - "Telegram Bot Setup for OpenClaw"
Cohesion: 0.13
Nodes (15): Advanced: Telegram Commands, Bot doesn't respond, Cannot find bot, How Messages Flow, Important Notes, Messages delayed, Multi-Device Access, Next Steps (+7 more)

### Community 1091 - "i-gg SKILL — Git Workflow Guardian (GIT-GUARD)"
Cohesion: 0.29
Nodes (7): i-crpr: Create PR with Pre-Flight Audit (CRPR), i-gg README — Git Workflow Guardian (GIT-GUARD), i-gg SKILL — Git Workflow Guardian (GIT-GUARD), /i-ab merge regression audit skill, cr/SKILL.md code review skill, /i-pr PR description skill, tdd/SKILL.md test-driven development skill

### Community 1092 - "i-icloud SKILL — iCloud Services"
Cohesion: 0.33
Nodes (6): i-icloud README — iCloud Data Manager (ICLOUD), i-icloud SKILL — iCloud Services, scripts/contacts.js, scripts/mail.js, scripts/notes.js, 1Password credential store

### Community 1093 - "Skill: CI/CD Pipeline Advisor (CICD)"
Cohesion: 0.29
Nodes (6): Deployment Matrix  (Direct to Prod), GitHub Actions Best Practices, Quality Gates  (execution order), Review Flags  (block the merge), Role, Skill: CI/CD Pipeline Advisor (CICD)

### Community 1094 - "Domain allowlisted? (agentshroud.yaml proxy.allowed_domains)"
Cohesion: 0.29
Nodes (7): Allowlisted domains (api.openai.com, api.anthropic.com, api.telegram.org, *.github.com, etc), Blocked (403 Forbidden) — all other domains + RFC1918, Bot makes outbound request (any HTTPS connection), Connection logged (timestamp, domain, allowed/blocked, count), Domain allowlisted? (agentshroud.yaml proxy.allowed_domains), HTTP CONNECT tunnel to gateway:8181, HTTP_PROXY set? (http://gateway:8181)

### Community 1095 - "Bot Container (agent decides: reply + tool call)"
Cohesion: 0.29
Nodes (7): Bot Container (agent decides: reply + tool call), Gateway (HMAC auth check, PII redaction via Presidio, route to agent), Isaiah (Telegram), ledger.db (INSERT INTO ledger), MCP inspection (injection scan NONE, PII scan NONE, sensitive op NONE), OpenAI API (POST /v1/chat/completions), Telegram API

### Community 1096 - "What is the symptom?"
Cohesion: 0.29
Nodes (7): Alert / Issue Detected, Bot not responding on Telegram, Bot container not healthy or crash-looping, Context limit exceeded, bot resets mid-conversation, Kill switch: gateway kill_switch_enabled=true (freeze/shutdown/disconnect), Security alert (blocked domain, HIGH MCP threat, canary token triggered), What is the symptom?

### Community 1097 - "Phase 2 — Security Core (HMAC Auth + PII Sanitizer, HTTP CONNECT Proxy, Approval Queue)"
Cohesion: 0.29
Nodes (7): Phase 1 — Foundation (Bot Container + Telegram, Gateway API + Ledger), Phase 2 — Security Core (HMAC Auth + PII Sanitizer, HTTP CONNECT Proxy, Approval Queue), Phase 3 — Credential Isolation (Op-Proxy, 1Password service account), Phase 4 — Channels (iMessage MCP, iCloud Email, MCP Proxy Inspector), Phase 5 — Stability (context limit fix, cascading retry + startup), Phase 6 — Observability (Prometheus + Grafana, log aggregation), Phase 7 — Enterprise Hardening (multi-tenant isolation, IEC 62443 policy docs, external contributor access)

### Community 1098 - "1Password Vault Sharing Instructions"
Cohesion: 0.13
Nodes (14): 1Password Vault Sharing Instructions, Current Files Status, Current Situation, How to Share the Vault, Next Steps, Option 1: Share Existing Vault, Option 2: Create and Share New Vault, Option 3: Use the Bot's Private Vault (+6 more)

### Community 1099 - "BROWSER_FETCH_SKILL.md"
Cohesion: 0.33
Nodes (5): Browser-Fetch Approval Queue Integration, Browser-Fetch Audit Logging, Browser-Fetch ClawHub Auto-Discovery Plan, Playwright Headless Chromium Decryption, SecureBrowser Skill

### Community 1100 - "AgentShroud Sequence Diagrams"
Cohesion: 0.29
Nodes (6): 1. Normal Message Flow, 2. MCP Tool Call Flow, 3. Kill Switch Activation Flow, 4. SSH Command Flow, 5. Web Fetch Flow, AgentShroud Sequence Diagrams

### Community 1101 - "Shutdown & Recovery"
Cohesion: 0.13
Nodes (15): Approval Queue, Auto-Restart, Crash Recovery, Data Integrity After Crash, Detecting a Crash, Graceful Shutdown, Kill Switch (Emergency Stop), Ledger Database (+7 more)

### Community 1102 - "mcp_audit.py"
Cohesion: 0.13
Nodes (12): Configuration / Environment Variables, Function Details, Hash Chain Structure, Key Classes / Functions, mcp_audit.py, MCPAuditTrail.log_tool_call(agent_id, server_name, tool_name, parameters, findings_count, threat_level, blocked, block_reason, pii_redacted, call_id), MCPAuditTrail.log_tool_result(call_id, agent_id, server_name, tool_name, success, error_message, result_summary, findings_count, threat_level, pii_redacted), MCPAuditTrail.start_call(call_id) (+4 more)

### Community 1103 - "gh-issues/SKILL.md"
Cohesion: 0.24
Nodes (8): gh-issues Claims File (dedup tracking), gh-issues Cursor File (cron sequential tracking), gh-issues PR Review Handler (Phase 6), gh-issues Sub-agent Spawn (Phase 5), gh CLI (GitHub), Stable-named cron scheduling for periodic audits, Conditional memory writes (memory/YYYY-MM-DD.md, MEMORY.md), openclaw security audit command family

### Community 1104 - "Sprint Cadence Decision"
Cohesion: 0.29
Nodes (6): Decision, GSD Issue Requirements, Skills Available (if needed), Sprint Cadence Decision, What We Do Instead, When to Revisit

### Community 1105 - "mcp_inspector.py"
Cohesion: 0.13
Nodes (14): Configuration / Environment Variables, Detection Patterns, Function Details, Key Classes / Functions, mcp_inspector.py, MCPInspector.inspect_tool_call(tool_name, params, check_injection, check_pii, check_encoding, check_sensitive), MCPInspector.inspect_tool_result(tool_name, result_content, check_pii, check_encoding), MCPInspector._redact_pii(value) (+6 more)

### Community 1106 - "i-ti SKILL.md (Technical Illustrator, Mermaid diagrams)"
Cohesion: 0.48
Nodes (7): i-bs SKILL.md (Brand Systems, referenced dependency), i-ti README.md, i-ti SKILL.md (Technical Illustrator, Mermaid diagrams), i-tw README.md, i-tw SKILL.md (Technical Writer), i-ui SKILL.md (UI Engineer, CSS architecture, WCAG AA), i-ux SKILL.md (UX Designer, IA, Nielsen heuristics)

### Community 1107 - "telegram_proxy.py"
Cohesion: 0.13
Nodes (13): Configuration / Environment Variables, Function Details, Key Classes / Functions, Methods Filtered (Inbound), Methods Filtered (Outbound), Purpose, Related, Responsibilities (+5 more)

### Community 1108 - "web_content_scanner.py"
Cohesion: 0.13
Nodes (14): Configuration / Environment Variables, Function Details, Injection Pattern Weights, Key Classes / Functions, Purpose, Related, Responsibilities, web_content_scanner.py (+6 more)

### Community 1109 - "MCP Auth Reset Skill"
Cohesion: 0.43
Nodes (7): i-mcpm-auth-reset README, MCP Auth Reset Skill, i-mcpm-aws-profile README, MCP AWS Profile Configuration Skill, mcpm-doctor Skill (referenced, sibling dir), i-mcpm README (MCP Tools Usage), MCP Tools Usage Skill

### Community 1110 - "`docs/planning/` — Index"
Cohesion: 0.29
Nodes (6): Active, `docs/planning/` — Index, Historic / archive, How to add a plan, Layout, What does NOT live here

### Community 1111 - "docker_engine.py"
Cohesion: 0.13
Nodes (13): Configuration / Environment Variables, docker_engine.py, Docker Security Options Used, DockerEngine._cmd(*args, **kwargs), DockerEngine.compose_up(file, detach), DockerEngine.inspect(name), DockerEngine.ps(all), DockerEngine.run(image, name, *, ports, volumes, networks, env, privileged, caps, seccomp, detach, read_only, no_new_privileges) (+5 more)

### Community 1113 - "📋 Detailed Step-by-Step"
Cohesion: 0.29
Nodes (7): 📋 Detailed Step-by-Step, Step 1: Install ClawHub CLI, Step 2: Create ClawHub Account, Step 3: Verify Skill Ready, Step 4: Publish to ClawHub, Step 5: Verify Publication, Step 6: Test Installation (Optional)

### Community 1114 - "egress_config.py"
Cohesion: 0.13
Nodes (13): Configuration / Environment Variables, Default Allowlist, Default Denylist Categories, egress_config.py, EgressFilterConfig.get_effective_allowlist(agent_id), EgressFilterConfig.is_denylisted(domain), EgressFilterConfig._matches_any_pattern(domain, patterns), Function Details (+5 more)

### Community 1115 - "egress_filter.py"
Cohesion: 0.13
Nodes (14): Configuration, egress_filter.py, EgressFilter.check(agent_id, destination, port), EgressFilter._is_private_ip(host), EgressFilter._record(agent_id, dest, port, action, rule), EgressPolicy.matches_domain(domain), Environment Variables, Function Details (+6 more)

### Community 1116 - "canary-deploy.sh"
Cohesion: 0.57
Nodes (6): deploy_ref(), die(), log(), run(), run_in_repo(), canary-deploy.sh script

### Community 1117 - "egress_monitor.py"
Cohesion: 0.13
Nodes (14): Alert Actions, Configuration / Environment Variables, Default Thresholds, egress_monitor.py, EgressMonitor.check_anomalies(agent_id), EgressMonitor.daily_summary(agent_id), EgressMonitor.get_events(agent_id, channel), EgressMonitor.record(event) (+6 more)

### Community 1118 - "gemini-review.py"
Cohesion: 0.29
Nodes (6): call_gemini(), main(), Lightweight Gemini API reviewer — no heavy CLI, just REST calls. Usage: echo…, Call Gemini API and return the review text and exit code. Returns: tuple:…, PATH, peer-review.sh script

### Community 1119 - "falco_monitor.py"
Cohesion: 0.13
Nodes (14): categorize_alerts(alerts), Configuration / Environment Variables, falco_monitor.py, Function Details, generate_summary(alerts), is_agentshroud_rule(rule_name), Key Classes / Functions, parse_alert(raw) (+6 more)

### Community 1120 - "input_normalizer.py"
Cohesion: 0.13
Nodes (14): detect_base64_payloads(text), Environment Variables, Function Details, input_normalizer.py, Invisible Characters Stripped, Key Classes / Functions, Mode: Enforce vs Monitor, normalize_input(text) (+6 more)

### Community 1121 - "scripts/security-scan.sh"
Cohesion: 0.57
Nodes (6): error(), info(), require_tool(), security-scan.sh script, success(), warn()

### Community 1122 - "Competitive Security Matrix — AgentShroud vs AI Agent Platforms"
Cohesion: 0.29
Nodes (6): Competitive Security Matrix — AgentShroud vs AI Agent Platforms, Container Security Toolchain Comparison, Key Takeaways, Module Comparison, Security Score (out of 28), Updated Magic Quadrant Position

### Community 1123 - "OPENCLAW_SANDBOX_MODE"
Cohesion: 0.13
Nodes (13): Description, Effect, OPENCLAW_DISABLE_HOST_FILESYSTEM, Related Notes, Set In, Value, Combination with Other Settings, Description (+5 more)

### Community 1124 - "check_upstream_cves"
Cohesion: 0.27
Nodes (6): check_upstream_cves(), Fetch one agent's GitHub Security Advisories and return advisories we don't…, _make_github_advisory(), Build a minimal GitHub Security Advisory payload keyed on GHSA id. ``ghsa_id``…, Stub urllib.request.urlopen to return a list of advisories., TestCheckUpstreamCves

### Community 1125 - "DelegationManager"
Cohesion: 0.23
Nodes (6): DelegationManager, Create a time-bounded delegation. Args: owner_id: Must match configured…, Revoke an active delegation. Returns True if a matching active delegation was…, Revoke all delegations for a specific user. Returns count removed., Remove expired delegations, persist result. Returns count removed., Manages owner-away privilege delegations. Thread-safe via file locking for…

### Community 1126 - "ReportStore"
Cohesion: 0.22
Nodes (5): Persist a report awaiting an async sanitizer (presidio) if injected. Sanitizes…, Prune oldest reports so the shared volume can't be filled., Filesystem-backed shared report store on the gateway-data volume., Persist a report (sync sanitizer path); return its id. Sanitizes ALL free-text…, ReportStore

### Community 1127 - "run_trivy_scan"
Cohesion: 0.27
Nodes (7): Run a Trivy scan and return parsed results. Args: target: Scan target…, run_trivy_scan(), patch, A 0-byte/empty stdout means the scan failed to produce output -- it must never…, returncode 0 = clean, 1 = vulns found (both expected); anything else means…, scan_type='image' is passed correctly to the trivy binary., TestTrivyRun

### Community 1128 - "TestEnvelopeSigner"
Cohesion: 0.13
Nodes (8): sign() + verify() should return True for unmodified content., Modifying content after signing should fail verification., Modifying the signature directly should fail verification., wrap_system_prompt() sets issuer='system' and passes verification., wrap_tool_result() sets issuer='tool:<name>' and passes verification., Two signers sharing the same key can cross-verify envelopes., Envelopes signed with one key should not verify with a different key., TestEnvelopeSigner

### Community 1129 - "_tool_req"
Cohesion: 0.21
Nodes (4): TestFileSandboxStep, TestPathIsolationStep, TestToolChainAnalyzer, _tool_req()

### Community 1130 - "multi_host_test.py"
Cohesion: 0.16
Nodes (12): TestBuildSshArgv, build_ssh_argv(), _dry_run_report(), HostStatus, Enum, str, Build the ssh argv for a host. Non-interactive, fail-fast on connect.…, Describe exactly what would run, without executing anything. (+4 more)

### Community 1131 - "patch"
Cohesion: 0.21
Nodes (3): patch, TestCpuMemoryDiskLimits, TestUsageStatsAndTracking

### Community 1132 - "DELIVERABLE 3 — v0.8.0 Implementation Items"
Cohesion: 0.29
Nodes (7): DELIVERABLE 3 — v0.8.0 Implementation Items, Item 1: Streaming Response Outbound Filtering — **DONE (v0.8.0)**, Item 2: Wire MemoryIntegrity/Lifecycle at Startup — **DONE (v0.8.0)**, Item 3: LLM Proxy User Identity Propagation — **DONE (v0.8.0)**, Item 4: Adversarial Prompt Injection Test Suite — **DONE (v0.8.0)**, Item 5: Audit Chain Guaranteed Persistence for BLOCK Events — **DONE (v0.8.0)**, Item 6: Update ADR-002 to Reflect Enforce-by-Default — **DONE (v0.8.0)**

### Community 1133 - "_mock_dir_with_files"
Cohesion: 0.20
Nodes (5): _mock_dir_with_files(), _mock_missing_dir(), Return a mock Path that exists and whose glob() returns named mock files., TestScoreImageIntegrity, TestScoreSupplyChain

### Community 1134 - "§4 — Hermes-Specific Section (NEW — first assessment)"
Cohesion: 0.29
Nodes (7): 4.1 Per-bot egress allowlist completeness, 4.2 Per-bot trust seeding, 4.3 Per-bot CVE triage cron health, 4.4 Hermes SOUL.md information disclosure posture, 4.5 Hermes dashboard TCP forwarder — binding address, 4.6 Cross-bot session isolation (FINDING BT-H1 — FIXED IN THIS PR), §4 — Hermes-Specific Section (NEW — first assessment)

### Community 1135 - "§2 — New Multi-Bot Attack Scenarios (v1.1+ Surface)"
Cohesion: 0.29
Nodes (7): §2 — New Multi-Bot Attack Scenarios (v1.1+ Surface), RT-MB1 — Cross-Bot Trust Pivot, RT-MB2 — Shared-Memory Leak Between Bots, RT-MB3 — Group-Context Escalation (Anticipating Workstream A), RT-MB4 — Hermes Cron Job Injection (NEW — Hermes-specific), RT-MB5 — Hermes-Initiated Exfiltration via Competitive Intel Cron, RT-MB6 — Cross-Bot Telegram Token Confusion

### Community 1137 - "Docker Desktop Network Settings — Cisco AnyConnect VPN Compatibility"
Cohesion: 0.15
Nodes (13): Docker Desktop Network Settings — Cisco AnyConnect VPN Compatibility, How to Apply, If It Stops Working After a VPN Reconnect, Network Architecture (unchanged), Primary: gVisor networking mode, Problem, Related Files, Root Cause (+5 more)

### Community 1138 - "_sync"
Cohesion: 0.22
Nodes (6): _exec_registry(), parametrize, CI runs black on gateway/; an appended registry block must already be clean., _sync(), TestListLocator, TestSerialization

### Community 1139 - "TestOriginAwareAuthorization"
Cohesion: 0.13
Nodes (8): AgentShroud-side mitigation for the 'channel skips the check' CVE class.…, The legitimate path must not regress., The core of the CVE class: a side channel claiming to be the owner.…, Refusing ELEVATION is not the same as blanket denial — an unverified origin…, A non-owner gains nothing and loses nothing from origin checking., Fail closed: an origin nobody vouched for is not trusted. A caller that forgets…, The control is agent-agnostic by construction: it takes an origin and an…, TestOriginAwareAuthorization

### Community 1140 - "AGENTS.md — Codex CLI Guidance"
Cohesion: 0.25
Nodes (7): Codex Configuration (.codex/config.toml), Data Lakehouse Platform (GSDL), AGENTS.md — Codex CLI Guidance, Guidance for ChatGPT Codex CLI when working in this repository., Codex Safe Refactor Role, Codex Test Augmenter Role, Codex Validation Runner Role

### Community 1141 - "Claude Code — Primary development agent"
Cohesion: 0.33
Nodes (6): Codex Prime Directive: Not Primary Developer, Claude Code — Primary development agent, Gemini CLI + Codex — Embedded QA/Test Engineers, Git Worktrees — parallel branch development, Product Owner — Isaiah Jefferson, Scrum Master / Agile Coach — AgentShroud Bot (OpenClaw)

### Community 1142 - "Skill: Audit Branch (AB) — Merge Regression Detection"
Cohesion: 0.13
Nodes (14): Check A — Substantive change on the losing side?, Check B — Tied to a real ticket?, Check C — Still broken at HEAD (not self-healed)?, Guardrails, Invocation Forms, Jira / PR Comment Format, Role, Skill: Audit Branch (AB) — Merge Regression Detection (+6 more)

### Community 1143 - "Skill: Create PR with Pre-Flight Audit (CRPR)"
Cohesion: 0.13
Nodes (14): Guardrails, Invocation, Role, Skill: Create PR with Pre-Flight Audit (CRPR), Step 0 — Pre-flight checks, Step 1 — Check for an in-progress merge, Step 2 — Merge without committing, Step 3 — Audit the pending merge (+6 more)

### Community 1144 - "i-eightd SKILL — 8D Root Cause Analysis"
Cohesion: 0.33
Nodes (6): AWS Agent (Athena data retrieval layer), AWS Athena / Data Lake, i-data README — Data Validation (DATA-VAL), i-data SKILL — Data Validation (DATA-VAL), i-eightd README — 8D Root Cause Analysis, i-eightd SKILL — 8D Root Cause Analysis

### Community 1145 - "System Audit & Documentation"
Cohesion: 0.13
Nodes (14): SECTION 10 — SHUTDOWN & RECOVERY SEQUENCE, SECTION 11 — KNOWN FAILURE MODES & TROUBLESHOOTING MATRIX, SECTION 12 — MERMAID FLOWCHART (Complete System Map), SECTION 13 — QUICK REFERENCE CARD, SECTION 1 — SYSTEM OVERVIEW (Plain English), SECTION 2 — COMPLETE FILE & DIRECTORY MAP, SECTION 3 — EVERY ENVIRONMENT VARIABLE, SECTION 4 — ALL EXTERNAL DEPENDENCIES (+6 more)

### Community 1146 - "AgentShroud Blue Team Security Auditor"
Cohesion: 0.13
Nodes (14): AgentShroud Blue Team Security Auditor, Audit Procedure, Critical Rules, Heat Map Legend, Infrastructure, Loss Categories, Methodology, Output Format (+6 more)

### Community 1147 - "Test Coverage Report (AgentShroud v1.3.0)"
Cohesion: 0.33
Nodes (6): NO SECURITY THEATER Policy (CLAUDE.md §2), STPA-Sec Methodology (Nancy Leveson, MIT), Agentic OS Architecture Doc (91 security-dir files / 75 wired), Red-Team Assessment Plan, Test Coverage Report (AgentShroud v1.3.0), Test Plan (AgentShroud v0.9.0)

### Community 1148 - "Skill: Audit Branch (AB) — Merge Regression Detection"
Cohesion: 0.13
Nodes (14): Check A — Substantive change on the losing side?, Check B — Tied to a real ticket?, Check C — Still broken at HEAD (not self-healed)?, Guardrails, Invocation Forms, Jira / PR Comment Format, Role, Skill: Audit Branch (AB) — Merge Regression Detection (+6 more)

### Community 1149 - "Skill: Create PR with Pre-Flight Audit (CRPR)"
Cohesion: 0.13
Nodes (14): Guardrails, Invocation, Role, Skill: Create PR with Pre-Flight Audit (CRPR), Step 0 — Pre-flight checks, Step 1 — Check for an in-progress merge, Step 2 — Merge without committing, Step 3 — Audit the pending merge (+6 more)

### Community 1150 - "System Audit & Documentation"
Cohesion: 0.13
Nodes (14): SECTION 10 — SHUTDOWN & RECOVERY SEQUENCE, SECTION 11 — KNOWN FAILURE MODES & TROUBLESHOOTING MATRIX, SECTION 12 — MERMAID FLOWCHART (Complete System Map), SECTION 13 — QUICK REFERENCE CARD, SECTION 1 — SYSTEM OVERVIEW (Plain English), SECTION 2 — COMPLETE FILE & DIRECTORY MAP, SECTION 3 — EVERY ENVIRONMENT VARIABLE, SECTION 4 — ALL EXTERNAL DEPENDENCIES (+6 more)

### Community 1151 - "AgentShroud Blue Team Security Auditor"
Cohesion: 0.13
Nodes (14): AgentShroud Blue Team Security Auditor, Audit Procedure, Critical Rules, Heat Map Legend, Infrastructure, Loss Categories, Methodology, Output Format (+6 more)

### Community 1152 - "Skill: Audit Branch (AB) — Merge Regression Detection"
Cohesion: 0.13
Nodes (14): Check A — Substantive change on the losing side?, Check B — Tied to a real ticket?, Check C — Still broken at HEAD (not self-healed)?, Guardrails, Invocation Forms, Jira / PR Comment Format, Role, Skill: Audit Branch (AB) — Merge Regression Detection (+6 more)

### Community 1153 - "Tailscale mesh VPN (tail240ea8.ts.net)"
Cohesion: 0.33
Nodes (6): Distributed OpenClaw Node Architecture (Pi peer-to-peer agent), Cryptographic Node Pairing Process, Marvin (Mac Studio) — Primary dev/build server, Pi (Raspberry Pi 4B) — Edge/test node, Tailscale mesh VPN (tail240ea8.ts.net), Trillian (Mac Mini) — Secondary build/CI

### Community 1154 - "AgentShroud Sequence Diagrams (doc)"
Cohesion: 0.33
Nodes (6): Diagram 15: Sequence — Telegram, AgentShroud Sequence Diagrams (doc), Kill Switch Activation Flow (SOFT_KILL, HARD_KILL, PANIC), Normal Message Flow (User -> Gateway -> Sanitizer -> Audit -> OpenClaw -> Audit -> User), SSH Command Flow (injection check, approval queue, executor, audit), Web Fetch Flow (URL analysis, SSRF protection, content scanning)

### Community 1155 - "AgentShroud State Diagrams (doc)"
Cohesion: 0.33
Nodes (6): Diagram 16: State — Approval Queue, Agent Trust Levels (UNTRUSTED, BASIC, STANDARD, TRUSTED, ADMIN), Approval Queue States (PENDING, APPROVED, DENIED, TIMED_OUT, EXECUTED, ARCHIVED), AgentShroud State Diagrams (doc), Gateway Operational Modes (MONITOR, ENFORCE, LOCKDOWN, EMERGENCY, RECOVERY), Kill Switch States (ACTIVE, SOFT_KILL, HARD_KILL, PANIC, RECOVERY)

### Community 1156 - "Assess severity"
Cohesion: 0.33
Nodes (6): Assess severity, Incident detected, P1 — Critical (respond immediately; owner Isaiah Jefferson; kill switch / revoke / rotate), P2 — High (respond within 1 hour; restart containers, rebuild image), P3 — Medium (respond within 4 hours; review logs, apply config fix), P4 — Low (resolve in next session; fix branch + PR)

### Community 1157 - "agentshroud-gateway container (starts first)"
Cohesion: 0.33
Nodes (6): 1password_service_account Docker secret, agentshroud-bot container (starts after gateway healthy), docker-agentshroud image (FROM node:22-bookworm-slim), docker-gateway image (FROM python:3.11-slim, gateway/Dockerfile), agentshroud-gateway container (starts first), gateway_password.txt Docker secret

### Community 1158 - "SECTION 2: MARK INFORMATION"
Cohesion: 0.33
Nodes (6): 2.1 Mark Type, 2.2 The Mark, 2.3 Mark Literal Element, 2.4 Translation / Transliteration, 2.5 Mark Description (for standard character mark), SECTION 2: MARK INFORMATION

### Community 1159 - "AGENTSHROUD standard character mark"
Cohesion: 0.33
Nodes (6): Class 9 — Downloadable Computer Software, Class 42 — Software as a Service (SaaS), Class 9 — Computer Software, Filing Basis (Section 1(a) Use in Commerce / 1(b) Intent to Use), AGENTSHROUD standard character mark, SECTION 3: GOODS AND SERVICES

### Community 1160 - "iot_button_register_cb"
Cohesion: 0.22
Nodes (8): bsp_iot_button_create(), button_handle_t, esp_err_t, button_cb_t, button_event_t, button_handle_t, iot_button_delete(), iot_button_register_cb()

### Community 1161 - "iot_button_register_cb"
Cohesion: 0.22
Nodes (8): bsp_iot_button_create(), button_handle_t, esp_err_t, button_cb_t, button_event_t, button_handle_t, iot_button_delete(), iot_button_register_cb()

### Community 1162 - "AgentShroud State Diagrams"
Cohesion: 0.33
Nodes (5): 1. Agent Trust Levels, 2. Kill Switch States, 3. Approval Queue States, 4. Gateway Operational Modes, AgentShroud State Diagrams

### Community 1163 - "telegram_egress_notify.py"
Cohesion: 0.33
Nodes (7): _err_text(), _is_stale_callback_error(), _is_stale_edit_error(), BaseException, Egress Firewall Telegram Inline Button Notifications. Sends inline keyboard…, urllib HTTPError carries the response body on .read(); fall back to str., Tests for Egress Firewall Telegram inline button notifications.

### Community 1164 - "SubagentMonitor._log_event"
Cohesion: 0.33
Nodes (6): SubagentMonitor.check_tool_usage, SubagentMonitor.deregister, SubagentMonitor.kill_agent, SubagentMonitor.kill_all, SubagentMonitor._log_event, SubagentMonitor.register_spawn

### Community 1165 - "ToolChainAnalyzer.analyze_tool_call"
Cohesion: 0.33
Nodes (6): ToolChainAnalyzer.analyze_tool_call, ToolChainAnalyzer._calculate_risk_score, ToolChainAnalyzer._cleanup_old_sessions, ToolChainAnalyzer._detect_chain_patterns, ToolChainAnalyzer._matches_source_pattern, ToolChainAnalyzer._trigger_alert

### Community 1166 - "🎯 High-Value Features (Justify the Effort)"
Cohesion: 0.15
Nodes (13): 1. **Approval Queue** (Gateway), 2. **PII Sanitization** (Gateway), 3. **Audit Ledger** (Gateway), 4. **Persona System** (Gateway), 5. **Docker Isolation**, 6. **Separate Bot Accounts** (iCloud, Gmail), 7. **Ultra-Conservative Credential Policy**, 8. **Seccomp Profiles** (Currently Disabled) (+5 more)

### Community 1167 - "Skill: Create PR with Pre-Flight Audit (CRPR)"
Cohesion: 0.13
Nodes (14): Guardrails, Invocation, Role, Skill: Create PR with Pre-Flight Audit (CRPR), Step 0 — Pre-flight checks, Step 1 — Check for an in-progress merge, Step 2 — Merge without committing, Step 3 — Audit the pending merge (+6 more)

### Community 1168 - "System Audit & Documentation"
Cohesion: 0.13
Nodes (14): SECTION 10 — SHUTDOWN & RECOVERY SEQUENCE, SECTION 11 — KNOWN FAILURE MODES & TROUBLESHOOTING MATRIX, SECTION 12 — MERMAID FLOWCHART (Complete System Map), SECTION 13 — QUICK REFERENCE CARD, SECTION 1 — SYSTEM OVERVIEW (Plain English), SECTION 2 — COMPLETE FILE & DIRECTORY MAP, SECTION 3 — EVERY ENVIRONMENT VARIABLE, SECTION 4 — ALL EXTERNAL DEPENDENCIES (+6 more)

### Community 1169 - "AgentShroud Blue Team Security Auditor"
Cohesion: 0.13
Nodes (14): AgentShroud Blue Team Security Auditor, Audit Procedure, Critical Rules, Heat Map Legend, Infrastructure, Loss Categories, Methodology, Output Format (+6 more)

### Community 1170 - "sync-version.sh"
Cohesion: 0.40
Nodes (5): Release Docker build & tag job, Release GitHub Release job (CHANGELOG notes extraction), Release test job (py3.13, tag/version sync checks), check_or_fix(), sync-version.sh script

### Community 1171 - "GitHub Branch Protection — `main`"
Cohesion: 0.33
Nodes (5): GitHub Branch Protection — `main`, Local Enforcement (already active), Required Settings, Required Status Checks, Verification

### Community 1172 - "main"
Cohesion: 0.15
Nodes (7): TestMain, TestSshRunner, main(), Return a HostRunner that executes the command on the host over SSH. SSH…, CLI entry point. Returns the aggregated exit code (0 = all passed)., ssh_runner(), HostRunner

### Community 1173 - "75 Security Modules"
Cohesion: 0.19
Nodes (15): TABLE I: Security Module Inventory (52 Modules), V-A. PII Sanitizer, V-B. Prompt Injection Defense, V-C. Credential Isolation, V-D. Encrypted Container Communication, V-E. DNS-Layer Enforcement, V-F. Tamper-Evident Audit, V. Security Modules (+7 more)

### Community 1174 - "skill.json"
Cohesion: 0.13
Nodes (14): playwright, author, dependencies, playwright, description, security, keywords, name (+6 more)

### Community 1175 - "test_wire_llm_settings.js"
Cohesion: 0.17
Nodes (13): fs, HERMES_INIT, OC_INIT, os, path, read(), readHermesMcpServers(), REPO (+5 more)

### Community 1177 - "Technical Specification"
Cohesion: 0.14
Nodes (13): API Call Structure, Apollo — Audio Systems Producer, Audio Quality Settings, Error Handling, Input Requirements, Output, Primary API: Text-to-Dialogue, Quality Checklist (+5 more)

### Community 1178 - "Technical Specification"
Cohesion: 0.14
Nodes (13): API Call Structure, Apollo — Audio Systems Producer, Audio Quality Settings, Error Handling, Input Requirements, Output, Primary API: Text-to-Dialogue, Quality Checklist (+5 more)

### Community 1179 - "AgentShroud Brand Guidelines"
Cohesion: 0.14
Nodes (14): AgentShroud Brand Guidelines, Available Formats, Brand Colors, Color Palette, Directory Structure, Do's, Don'ts, File Formats (+6 more)

### Community 1180 - "allowed_hours"
Cohesion: 0.14
Nodes (14): additionalProperties, properties, required, type, pattern, type, allowed_hours, end (+6 more)

### Community 1181 - "Future Enhancements"
Cohesion: 0.33
Nodes (6): Future Enhancements, Priority 1: Auto-Discovery, Priority 2: Enhanced Extraction, Priority 3: Screenshot Capture, Priority 4: Multi-Page Support, Priority 5: Direct Gmail Configuration

### Community 1182 - "properties"
Cohesion: 0.14
Nodes (14): additionalProperties, properties, required, type, type, type, auth, dynamic_registration (+6 more)

### Community 1183 - "Technical Specification"
Cohesion: 0.14
Nodes (13): API Call Structure, Apollo — Audio Systems Producer, Audio Quality Settings, Error Handling, Input Requirements, Output, Primary API: Text-to-Dialogue, Quality Checklist (+5 more)

### Community 1184 - "Output Sections (ALL required)"
Cohesion: 0.14
Nodes (13): 1. Scope of Change, 2. What Changes and Why, 3. Scalability Gate, 4. Blast Radius, 5. Known Limits and Assumptions, 6. Alternatives Considered, 7. Open Questions, 8. Verification Plan (+5 more)

### Community 1185 - "Output Sections (ALL required)"
Cohesion: 0.14
Nodes (13): 1. Scope of Change, 2. What Changes and Why, 3. Scalability Gate, 4. Blast Radius, 5. Known Limits and Assumptions, 6. Alternatives Considered, 7. Open Questions, 8. Verification Plan (+5 more)

### Community 1186 - "AgentShroud™ Brand Guidelines"
Cohesion: 0.14
Nodes (13): AgentShroud™ Brand Guidelines, Brand Identity, Colors, Communication Templates, Elevator pitch, Key Messaging, License, Logo Usage (+5 more)

### Community 1187 - "1password-skill.sh"
Cohesion: 0.29
Nodes (10): get_field(), get_totp(), list_items(), list_vaults(), 1password-skill.sh script, _validate_arg(), get-credential.sh script, op_authenticate() (+2 more)

### Community 1188 - "mcp-proxy-wrapper.js"
Cohesion: 0.16
Nodes (13): auditResult(), child, [command, ...commandArgs], dashDash, gatewayPost(), http, https, inboundRl (+5 more)

### Community 1189 - "AgentShroud Control UI Connection Guide"
Cohesion: 0.14
Nodes (14): AgentShroud Control UI Connection Guide, Alternative: Use Built-In Control UI (If Available), "Cannot connect to gateway", "Connection timeout", "Disconnected (1006): no reason", Getting Help, Manual Connection Test, Quick Fix: Connect to Gateway (+6 more)

### Community 1190 - "Use Cases"
Cohesion: 0.14
Nodes (13): AgentShroud Security Proxy, Overview, UC-001: User Sends Message to Agent (PII Sanitization Flow), UC-002: Agent Calls MCP Tool (Inspection + Permission Check), UC-003: Agent Fetches Web Content (SSRF Check + Content Scan), UC-004: Admin Activates Kill Switch, UC-005: Agent Requests SSH Access (Approval Queue), UC-006: Security Alert Triggers Notification (+5 more)

### Community 1191 - "event_bus.py"
Cohesion: 0.14
Nodes (13): Config Keys Read, Environment Variables Used, event_bus.py, Event Types Emitted by main.py, EventBus.emit(event), Function Details, Imports From / Exports To, Key Classes / Functions (+5 more)

### Community 1192 - "mcp-proxy-wrapper.js"
Cohesion: 0.14
Nodes (13): Environment Variables, Fail-Closed Design, Fail-Closed Patch, Gateway Communication, Gateway Endpoints Called, How It Works, Key Behavior, mcp-proxy-wrapper.js (+5 more)

### Community 1193 - "Function Details"
Cohesion: 0.14
Nodes (13): Configuration / Environment Variables, ConnectionPool.get_or_create(server_name, config), Function Details, Key Classes / Functions, mcp_proxy.py, MCPProxy.check_approval_required(tool_call), MCPProxy._execute_tool_call(tool_call, sanitized_params), MCPProxy.process_tool_call(tool_call, execute) (+5 more)

### Community 1194 - "url_analyzer.py"
Cohesion: 0.14
Nodes (13): Configuration / Environment Variables, Function Details, Key Classes / Functions, Purpose, Related, Responsibilities, SSRF Detection Coverage, url_analyzer.py (+5 more)

### Community 1195 - "security.py"
Cohesion: 0.14
Nodes (13): Configuration / Environment Variables, Function Details, get_features_for_runtime(runtime), get_missing_features(runtime), get_security_options(runtime), Key Classes / Functions, Purpose, Related (+5 more)

### Community 1196 - "Procedure"
Cohesion: 0.11
Nodes (18): 0. Preflight (both environments), 1. Inventory, 2. Security findings, 2b. AgentShroud-side remediation — the vendor's fix is NOT the finish line, 3. Upgrade DEV, 4. Promote to PROD, 5. Cleanup, 6. Jira tracking (standard procedure, owner directive 2026-08-30) (+10 more)

### Community 1197 - "Voice Gateway Service (STT/TTS WebSocket Bridge to Governed Path)"
Cohesion: 0.47
Nodes (6): MicroLink Native Tailscale Client for ESP32 (Requires PSRAM), ESP32-S3-BOX-3 Hermes Voice Terminal Planning Doc, Voice Gateway Service (STT/TTS WebSocket Bridge to Governed Path), Voice Gateway Python Requirements (faster-whisper, kokoro), faster-whisper STT Engine (Local, CPU-friendly), Kokoro TTS Engine

### Community 1198 - "Skill: Pre-Change Analysis (PCA)"
Cohesion: 0.33
Nodes (5): Closing Gate, Output Format Rules, Role, Skill: Pre-Change Analysis (PCA), Persisted Artifact Mode (opt-in repos only)

### Community 1199 - "v1.6.0 Release — Voice Terminal"
Cohesion: 0.40
Nodes (5): Audio clicking fix — TTS resume dedup + dither + voice-gateway cpuset widen, ESP32 live model label fix — server-authoritative label push, Firmware TLS connect reliability — timeout 5s to 10s (DERP handshake race), Streaming direct voice path (_call_llm_stream) — avoids blocking full-reply wait, v1.6.0 Release — Voice Terminal

### Community 1200 - "canary.py"
Cohesion: 0.14
Nodes (12): Canary Checks, canary.py, Environment Variables, Function Details, Key Classes / Functions, Mode: Enforce vs Monitor, Operational Notes, Purpose (+4 more)

### Community 1201 - "Key Benefits"
Cohesion: 0.40
Nodes (5): 1. True Distributed AI, 2. Enhanced Security, 3. Advanced Capabilities, 4. Better Development Workflow, Key Benefits

### Community 1202 - "log_sanitizer.py"
Cohesion: 0.14
Nodes (11): Configuration / Environment Variables, Function Details, Key Classes / Functions, log_sanitizer.py, LogSanitizer.filter(record), LogSanitizer._sanitize_text(text), Pattern Taxonomy, Purpose (+3 more)

### Community 1203 - "trivy_report.py"
Cohesion: 0.14
Nodes (13): Configuration / Environment Variables, Function Details, generate_summary(report), Key Classes / Functions, parse_trivy_output(raw), Purpose, Related, Responsibilities (+5 more)

### Community 1204 - "Gateway Container Startup Failures"
Cohesion: 0.14
Nodes (13): Bot Container Startup Failures, Bot Exits Before Gateway Is Healthy, `Could not load Claude OAuth token after retries`, `FileNotFoundError: No agentshroud.yaml found`, Gateway Container Startup Failures, Gateway Health Check Never Passes, `No auth_token found in secret file`, OpenClaw Not Starting (+5 more)

### Community 1207 - "Browser — Secure Browser Automation"
Cohesion: 0.40
Nodes (4): Browser — Secure Browser Automation, Purpose, Related Skills, Usage

### Community 1208 - "Daedalus — Concept Illustrator"
Cohesion: 0.40
Nodes (4): Daedalus — Concept Illustrator, Purpose, Related Skills, Usage

### Community 1209 - "_output"
Cohesion: 0.24
Nodes (4): _output(), _print_table(), Print data in the requested format., TestOutputHelpers

### Community 1210 - "._rewrite_known_runtime_errors"
Cohesion: 0.24
Nodes (3): Map recurring runtime/provider failures to deterministic operator guidance., Unit tests for deterministic runtime error rewrite helper behavior., TestRuntimeRewriteHelpers

### Community 1211 - "iCloud Data Manager (ICLOUD)"
Cohesion: 0.40
Nodes (4): iCloud Data Manager (ICLOUD), Purpose, Related Skills, Usage

### Community 1212 - "GroupRole"
Cohesion: 0.15
Nodes (9): GroupRole, Enum, str, Set or update the role for a user in a specific group., Return all user→role mappings for a group., Group-context RBAC — per-member role resolution for Telegram group workspaces.…, Per-group roles for Telegram group workspace members. Hierarchy (highest to…, Numeric rank for comparison — higher is more privileged. (+1 more)

### Community 1213 - "ToolResultSanitizer"
Cohesion: 0.18
Nodes (7): Extract code blocks to preserve them during sanitization., Restore code blocks after sanitization., Remove or warn about markdown links pointing to non-allowlisted domains., Sanitize tool result content by filtering markdown links and images. Args:…, Enhanced markdown sanitizer with configurable domain allowlist., ToolResultSanitizer, Test warn mode that marks but preserves external content.

### Community 1214 - "_run"
Cohesion: 0.22
Nodes (5): Tests for scripts/canary-deploy.sh (SCRUM-62 blue/green canary). Exercised via…, _run(), test_help_prints_usage(), TestDryRun, TestGuard

### Community 1215 - "TestDeterministicPresidioInit"
Cohesion: 0.14
Nodes (4): When the pinned model loads, Presidio is built with an explicit ``nlp_engine``…, Presidio init must be deterministic and must NEVER trigger a runtime model…, The default-model auto-download path must never be taken. If Presidio is ever…, TestDeterministicPresidioInit

### Community 1217 - "test_group_rbac.py"
Cohesion: 0.19
Nodes (11): acl_config(), enforcer(), group_role_resolver(), fixture, Owner must have unrestricted access even in group context., Owner is allowed ALL tools in group context., Owner group-context check must match standard can_use_tool result., TDD — Workstream A (v1.2.0): Per-member RBAC in group context. Tests that: -… (+3 more)

### Community 1218 - "Incident Response (INCIDENT)"
Cohesion: 0.40
Nodes (4): Incident Response (INCIDENT), Purpose, Related Skills, Usage

### Community 1219 - "Security Controls"
Cohesion: 0.11
Nodes (18): 2.1 Docker Networks, 2.2 Exposed Ports, 2.3 Tailscale Network, 2. Network Isolation, 1. Container Isolation, 2. Capability Dropping, 3. Resource Limits, 4. Network Isolation (+10 more)

### Community 1220 - "TestReadOnlyMemberGroupContext"
Cohesion: 0.14
Nodes (8): Read-only members must be denied high-risk tools in any group context., Read-only member denied email_sending even when called from group context., Read-only member denied file_deletion in group context., Read-only member denied external_api_calls in group context., Read-only member denied skill_installation in group context., Read-only member IS allowed web_search (low-risk) in group context., Read-only member IS allowed read tool in group context., TestReadOnlyMemberGroupContext

### Community 1222 - "Socrates — Dialogue Architect"
Cohesion: 0.40
Nodes (4): Purpose, Related Skills, Socrates — Dialogue Architect, Usage

### Community 1223 - "TestInfoLeakage"
Cohesion: 0.14
Nodes (8): Test that errors don't leak sensitive information., Decryption errors shouldn't expose the encryption key., Token validation errors shouldn't expose signing keys., Git guard errors shouldn't expose full file paths., Environment guard should scrub sensitive output., Stack traces containing secrets should be sanitized., Internal infrastructure headers should be stripped., TestInfoLeakage

### Community 1225 - "_patch_exists"
Cohesion: 0.18
Nodes (4): _patch_exists(), os.path.exists override for specific paths only., TestCheckOpenscap, TestGetLogs

### Community 1226 - "TestWebSearchLog"
Cohesion: 0.14
Nodes (7): Tests for _trigger_web_search_log and raw web_search JSON outbound handling., _trigger_web_search_log calls log_external_decision with Brave domain and query., _trigger_web_search_log returns silently when egress_filter is None., Queries longer than 200 chars are truncated in the SOC log reason., Owner chat: raw web_search JSON produces 'Switch to tool-capable model' message., Collaborator chat: raw web_search JSON produces a safe notice., TestWebSearchLog

### Community 1227 - "_entry"
Cohesion: 0.29
Nodes (4): _entry(), _not_yet_fixed(), A version guaranteed newer than the real pinned RUNNING_VERSION, for tests that…, TestTriageEntry

### Community 1228 - "Technical Specification"
Cohesion: 0.14
Nodes (13): API Call Structure, Apollo — Audio Systems Producer, Audio Quality Settings, Error Handling, Input Requirements, Output, Primary API: Text-to-Dialogue, Quality Checklist (+5 more)

### Community 1229 - "Daedalus — Concept Illustrator"
Cohesion: 0.40
Nodes (4): Daedalus — Concept Illustrator, Purpose, Related Skills, Usage

### Community 1230 - "Data Validation (DATA-VAL)"
Cohesion: 0.40
Nodes (4): Data Validation (DATA-VAL), Purpose, Related Skills, Usage

### Community 1231 - "8D Root Cause Analysis"
Cohesion: 0.40
Nodes (4): 8D Root Cause Analysis, Purpose, Related Skills, Usage

### Community 1232 - "Hermes — Podcast Production Orchestrator"
Cohesion: 0.40
Nodes (4): Hermes — Podcast Production Orchestrator, Purpose, Related Skills, Usage

### Community 1233 - "iCloud Data Manager (ICLOUD)"
Cohesion: 0.40
Nodes (4): iCloud Data Manager (ICLOUD), Purpose, Related Skills, Usage

### Community 1234 - "Technical Specification"
Cohesion: 0.14
Nodes (13): API Call Structure, Apollo — Audio Systems Producer, Audio Quality Settings, Error Handling, Input Requirements, Output, Primary API: Text-to-Dialogue, Quality Checklist (+5 more)

### Community 1235 - "MCP Auth Reset (MCPM-AUTH-RESET)"
Cohesion: 0.40
Nodes (4): MCP Auth Reset (MCPM-AUTH-RESET), Purpose, Related Skills, Usage

### Community 1236 - "Technical Specification"
Cohesion: 0.14
Nodes (13): API Call Structure, Apollo — Audio Systems Producer, Audio Quality Settings, Error Handling, Input Requirements, Output, Primary API: Text-to-Dialogue, Quality Checklist (+5 more)

### Community 1237 - "Sunday Upgrade 2026-11-22 (DEV run, account `agentshroud-bot`)"
Cohesion: 0.14
Nodes (13): 1. Summary line, 2. Environment mapping, 3b. Not updated this run — plan for the week, 7. Rollback, Attempt 1 of dev apply (01:18-01:42) — exit 30, rolled back automatically, Attempt 3 of dev apply (04:00-04:49) — exit 40, rolled back — ROOT CAUSE: self-inflicted state downgrade, Attempt 4 of dev apply (05:04-06:00) — exit 0, PASS, Conduit plugin (conduit_push) — HELD BACK (stays 0.58.0 @ f56bbb963f01, wanted 0.193.2 @ ff7734190d44) (+5 more)

### Community 1238 - "Morning Checklist (5 minutes)"
Cohesion: 0.14
Nodes (14): 1. Dependency Updates, 1. Service Health, 2. Backup Verification, 2. Tailscale Connectivity, 3. Audit Ledger Review, 3. Tailscale ACL Review, 4. Log Review, 4. Test Suite (+6 more)

### Community 1239 - "asb"
Cohesion: 0.26
Nodes (13): asb script, _asb_banner(), _deployment_setup(), DOCKER_API_VERSION, _ensure_sandbox_image(), _fstrim_colima_datadisk(), _hermes_down(), _hermes_up() (+5 more)

### Community 1240 - "Part 2 — Red-Team Attack Run (SCRUM-73)"
Cohesion: 0.14
Nodes (14): Part 2 — Red-Team Attack Run (SCRUM-73), RT-10 · Subagent / delegation privilege escalation — **BLOCKED**, RT-11 · MCP-server compromise — **BLOCKED-if-configured / dormant-by-default**, RT-12 · Skill supply-chain — **PARTIALLY BLOCKED**, RT-1 · Prompt injection — **PARTIALLY BLOCKED**, RT-2 · Inbound encoding bypass — **EXPLOITABLE**, RT-3 · Cross-collaborator data access — **BLOCKED (isolation) / gated by RT-6**, RT-4 · Cross-group access — **data BLOCKED / group tool-ACL UNWIRED** (+6 more)

### Community 1241 - "Skill: Security Review (SEC)"
Cohesion: 0.15
Nodes (12): Anti-Patterns to Flag, Core Principle, Layer 1: Application Security, Layer 2: Container Security, Layer 3: Network Security, Layer 4: Data Flow Security, Output Format, Review Layers (+4 more)

### Community 1242 - "Workflow: Survey → Draft → Inject → Confirm"
Cohesion: 0.15
Nodes (12): Re-injection Command (for reference), Role, Rules, Skill: Session Prompt Generator (SESSION-PROMPT), Step 1 — Survey the Repo, Step 2 — Answer Six Questions, Step 3 — Write SESSION_PROMPT.md, Step 4 — Write the File (+4 more)

### Community 1243 - "Skill: Test-Driven Development (TDD)"
Cohesion: 0.15
Nodes (12): Anti-Patterns to Flag, Core Discipline: Red → Green → Refactor, Glue Job Logic  →  test transformations outside Spark, PostgreSQL  →  `SAVEPOINT` + `ROLLBACK`, Python / Boto3 / AWS  →  `moto`, Role, Rules, Skill: Test-Driven Development (TDD) (+4 more)

### Community 1244 - "Salesforce CLI (`sf`) Agent"
Cohesion: 0.15
Nodes (12): Auth Preflight (run FIRST, before any other `sf` command), Command Map, Data investigation, Failed deploy triage, Identity, Operating Rules (non-negotiable), Output Format, Risks (+4 more)

### Community 1245 - "Salesforce CLI (`sf`) Agent"
Cohesion: 0.15
Nodes (12): Auth Preflight (run FIRST, before any other `sf` command), Command Map, Data investigation, Failed deploy triage, Identity, Operating Rules (non-negotiable), Output Format, Risks (+4 more)

### Community 1246 - "forwarder.js"
Cohesion: 0.21
Nodes (8): buildClipPayload(), cleanExtractedText(), normalizeGatewayUrl(), postForward(), F, GOOD_CONFIG, truncateContent(), validateConfig()

### Community 1247 - "Summary"
Cohesion: 0.15
Nodes (13): [0.6.0] - 2026-02-23, [0.7.0] - 2026-02-25, [1.2.4] — release/v1.2.4 (2026-06-29), Added, Added, Fixed, Fixed, Fixed (+5 more)

### Community 1248 - "test_collaborator_greeter.py"
Cohesion: 0.10
Nodes (35): AsyncClient, CollaboratorGreeter, Sends a branded greeting photo to each (bot, user) pair once per 24 h., Collaborator daily greeting — fires on the first inbound Telegram message from…, Greet user if cooldown has expired. Returns True when greeting was sent., _err_response(), _make_greeter(), _ok_response() (+27 more)

### Community 1249 - "SOC Command Center — Five Pillars"
Cohesion: 0.40
Nodes (5): Collaborator System (multi-user agentic workspace), OpenClaw — primary integration target agent, SOC Command Center — Five Pillars, Dashboard Overview (request volume, security events, audit trail), Kill Switch (freeze/shutdown/disconnect)

### Community 1250 - "active"
Cohesion: 0.50
Nodes (5): active, compacting (token count approaches reserveTokensFloor, 196K of 200K), fresh (container starts, new session created), idle (health monitor 300s interval), reset (new session UUID created, previous archived)

### Community 1251 - "COMMUNICATION-TEMPLATES.md"
Cohesion: 0.40
Nodes (4): Option 1 — Clean & Professional Trademark Notice, Option 2 — Compact Trademark Notice, Option 3 — Full Collaborator Trademark Notice, Option 4 — Documentation Footer Trademark Notice

### Community 1252 - "SECTION 9: IMPORTANT NOTES"
Cohesion: 0.40
Nodes (5): SECTION 9: IMPORTANT NOTES, TEAS Plus vs. TEAS Standard, The TM Symbol, Trademark vs. Patent, Why Standard Character Mark First

### Community 1253 - "Default Monitor-Mode Egress Rationale"
Cohesion: 0.60
Nodes (5): AgentShroud Egress Control Configuration, AgentShroud MCP Proxy Configuration, Default Monitor-Mode Egress Rationale, MCP Proxy Default-Allow Philosophy, Default-Allow Web Proxy Design Rationale

### Community 1254 - "AgentShroud Data Flow Diagrams"
Cohesion: 0.40
Nodes (4): AgentShroud Data Flow Diagrams, Level 0: Context Diagram, Level 1: Security Components, Level 2: MCP Proxy Detail

### Community 1255 - "Changelog — AgentShroud™"
Cohesion: 0.15
Nodes (12): [1.5.1] "A2A Governance" (2026-08-22), [1.5.3] (2026-08-23), Added, Changelog — AgentShroud™, Fixed, Fixed, Migration Notes, Recommended Steps (+4 more)

### Community 1256 - "Skill: Security Review (SEC)"
Cohesion: 0.15
Nodes (12): Anti-Patterns to Flag, Core Principle, Layer 1: Application Security, Layer 2: Container Security, Layer 3: Network Security, Layer 4: Data Flow Security, Output Format, Review Layers (+4 more)

### Community 1257 - "Workflow: Survey → Draft → Inject → Confirm"
Cohesion: 0.15
Nodes (12): Re-injection Command (for reference), Role, Rules, Skill: Session Prompt Generator (SESSION-PROMPT), Step 1 — Survey the Repo, Step 2 — Answer Six Questions, Step 3 — Write SESSION_PROMPT.md, Step 4 — Write the File (+4 more)

### Community 1258 - "Skill: Test-Driven Development (TDD)"
Cohesion: 0.15
Nodes (12): Anti-Patterns to Flag, Core Discipline: Red → Green → Refactor, Glue Job Logic  →  test transformations outside Spark, PostgreSQL  →  `SAVEPOINT` + `ROLLBACK`, Python / Boto3 / AWS  →  `moto`, Role, Rules, Skill: Test-Driven Development (TDD) (+4 more)

### Community 1259 - "Salesforce CLI (`sf`) Agent"
Cohesion: 0.15
Nodes (12): Auth Preflight (run FIRST, before any other `sf` command), Command Map, Data investigation, Failed deploy triage, Identity, Operating Rules (non-negotiable), Output Format, Risks (+4 more)

### Community 1260 - "AgentShroud™ Security Policy"
Cohesion: 0.09
Nodes (22): Kill Switch Operations, Daily CVE Sync + Page Update Workflow, AgentShroud™ Security Policy, Compliance Alignment, Emergency Response, Layer 1 — Core Pipeline (P0), Layer 2 — Middleware (P1), Layer 3 — Output Protection (+14 more)

### Community 1261 - "AgentShroud Weekly Upgrade — 2026-09-21 (DEV run, account: agentshroud-bot)"
Cohesion: 0.12
Nodes (16): 0. Identity, timeline, and environment reality (discovered, not assumed), 10. Verification evidence, 11. Rollback instructions, 12. Time spent, 1. Summary line, 2. Environment mapping (discovered), 3. Preflight, 4. Inventory — wrapped agents (mandatory script, cited) (+8 more)

### Community 1262 - "Skill: Security Review (SEC)"
Cohesion: 0.15
Nodes (12): Anti-Patterns to Flag, Core Principle, Layer 1: Application Security, Layer 2: Container Security, Layer 3: Network Security, Layer 4: Data Flow Security, Output Format, Review Layers (+4 more)

### Community 1264 - "browse.py — SecureBrowser CLI (OpenClaw)"
Cohesion: 0.50
Nodes (5): browse.py — SecureBrowser CLI (OpenClaw), SecureBrowser Security Configuration (config.yaml, OpenClaw), browser-fetch package.json, Browser Skill README (OpenClaw), Browser — Secure Browser Automation SKILL (OpenClaw)

### Community 1265 - "Workflow: Survey → Draft → Inject → Confirm"
Cohesion: 0.15
Nodes (12): Re-injection Command (for reference), Role, Rules, Skill: Session Prompt Generator (SESSION-PROMPT), Step 1 — Survey the Repo, Step 2 — Answer Six Questions, Step 3 — Write SESSION_PROMPT.md, Step 4 — Write the File (+4 more)

### Community 1266 - "Troubleshooting"
Cohesion: 0.40
Nodes (5): Problem: 1Password link shows only page shell, Problem: Browser binaries not found, Problem: Permission denied executing browser, Problem: Skill not auto-discovered by bot, Troubleshooting

### Community 1267 - "🆘 Troubleshooting"
Cohesion: 0.40
Nodes (5): "Authentication required", "clawhub: command not found", "Permission denied", "Skill validation failed", 🆘 Troubleshooting

### Community 1268 - "AgentShroud v0.7.0 - Blue Team Security Audit Report"
Cohesion: 0.05
Nodes (37): 10. Steve Hay Assessment Alignment, 1.1 Module Integration Status, 1.2 Critical Security Pipeline Flow, 1. Security Module Analysis, 2.1 Loss Categories, 2.2 Heat Map Matrix, 2.3 Coverage Analysis, 2. Steve Hay Heat Map Assessment (+29 more)

### Community 1269 - "v0.6.0 Baseline Results"
Cohesion: 0.15
Nodes (12): AgentShroud Red Team Assessment — Live Results, CIS Docker Benchmark: 12/12 (100%), Container Security Profile: 12/12 (100%), Deep Integration Test: 36/37 (97%), Expected v0.7.0 Results, Identified Gaps (Steve Hay's Assessment), Module Status: 33/33 Active, Sprint Status (+4 more)

### Community 1270 - "agentshroud-manage.sh"
Cohesion: 0.70
Nodes (4): api_call(), agentshroud-manage.sh script, usage(), validate_input()

### Community 1271 - "launch-instance.sh"
Cohesion: 0.50
Nodes (4): DOCKER_HOST, find_port(), PATH, launch-instance.sh script

### Community 1272 - "openclaw_triage.sh"
Cohesion: 0.70
Nodes (4): log(), save_cmd(), save_shell(), openclaw_triage.sh script

### Community 1273 - "Step-by-Step Installation"
Cohesion: 0.15
Nodes (13): Dashboard Access, Development (local testing), Health Check, Production (background daemon), Production with Restart Policy, Proxy Mode (Default), Sidecar Mode, Step 1: Clone the Repository (+5 more)

### Community 1274 - "I - Information Disclosure"
Cohesion: 0.40
Nodes (5): I - Information Disclosure, Threat: DNS Data Exfiltration, Threat: Environment Variable Leakage, Threat: PII Leakage in Logs, Threat: SSRF (Server-Side Request Forgery)

### Community 1275 - "router.py"
Cohesion: 0.15
Nodes (13): Config Keys Read, Environment Variables Used, forward_to_agent(target, sanitized_content, ledger_id, metadata), Function Details, health_check(target), Imports From / Exports To, Key Classes / Functions, Known Issues / Notes (+5 more)

### Community 1276 - "mcp_config.py"
Cohesion: 0.15
Nodes (12): Configuration / Environment Variables, Function Details, Key Classes / Functions, mcp_config.py, MCPProxyConfig Fields, MCPProxyConfig.from_dict(data), MCPServerConfig Fields, PermissionLevel comparison operators (+4 more)

### Community 1277 - "web_proxy.py"
Cohesion: 0.15
Nodes (12): Configuration / Environment Variables, Function Details, Key Classes / Functions, Purpose, RateLimiter.check(domain, rpm_limit), Related, Responsibilities, Security Check Order (check_request) (+4 more)

### Community 1278 - "compose_generator.py"
Cohesion: 0.15
Nodes (12): compose_generator.py, Configuration / Environment Variables, Default Service Configuration, Function Details, gateway service, generate_apple_script(services), generate_compose(services, runtime), Key Classes / Functions (+4 more)

### Community 1279 - "config.py"
Cohesion: 0.15
Nodes (11): config.py, Configuration / Environment Variables, Environment Variables, Function Details, Key Classes / Functions, Purpose, Related, Responsibilities (+3 more)

### Community 1280 - "agentshroud.yaml"
Cohesion: 0.15
Nodes (12): agentshroud.yaml, channels section, Config Search Order, gateway section, mcp_proxy section, proxy section, Purpose, Related Notes (+4 more)

### Community 1281 - "test_all_modules_enforce.py"
Cohesion: 0.04
Nodes (48): AlertLevel, ConsistencyScore, DisclosureCategory, DisclosureEvent, MultiTurnTracker, Any, callable, Enum (+40 more)

### Community 1282 - "Docker Volumes"
Cohesion: 0.15
Nodes (12): agentshroud-browsers, agentshroud-config, agentshroud-ssh, agentshroud-workspace, Backup, Cleanup Warning, Docker Volumes, gateway-data (+4 more)

### Community 1283 - "Troubleshooting Matrix"
Cohesion: 0.15
Nodes (12): Approval Queue Issues, Connectivity Issues, Container Stability Issues, Debugging Commands, Egress / Network Issues, PII / Sanitization Issues, Prompt Injection Issues, Quick Diagnosis Flow (+4 more)

### Community 1284 - "Health Checks"
Cohesion: 0.15
Nodes (12): Approval Queue Health, Basic Status (No Auth), Bot Health Check, Container Health Check, Full Health Report (Auth Required), Gateway Health Endpoints, Health Check Intervals (Docker), Health Checks (+4 more)

### Community 1285 - "Kill Switch Procedure"
Cohesion: 0.15
Nodes (13): After Disconnect, After Freeze, After Shutdown, Kill Switch Actions, Kill Switch Monitoring, Kill Switch Procedure, Method 1: Dashboard (Recommended), Method 2: API (+5 more)

### Community 1286 - "parse_query"
Cohesion: 0.22
Nodes (5): parse_query(), Extract domain name and query type from a DNS query packet. Returns: (domain,…, Handle incoming DNS query., Process a single DNS query: log, forward, respond., TestParseQuery

### Community 1287 - "EnvironmentGuard"
Cohesion: 0.07
Nodes (19): t_env(), EnvironmentGuard, EnvironmentLeakage, Any, Check if command execution should be blocked to prevent environment leakage.…, Check if command contains patterns that could access environment., Scrub environment variables and API keys from command output. Args: output:…, Detected environment variable leakage. (+11 more)

### Community 1288 - "make_fake_socket_module"
Cohesion: 0.21
Nodes (5): forward_query(), Forward a DNS query to upstream resolvers with failover., make_fake_socket_module(), Build a fake `socket` module namespace driving forward_query without I/O. Each…, TestForwardQuery

### Community 1289 - "._suppress_qwen3_thinking"
Cohesion: 0.32
Nodes (11): Append '/no_think' to the last user message, in place, if not already present.…, Regression tests for LLMProxy._suppress_qwen3_thinking. 2026-10-16 incident:…, _req(), test_missing_model_treated_as_non_qwen(), test_nemotron_alias_gets_reasoning_effort_none_and_text_untouched(), test_nemotron_normalized_full_path_gets_reasoning_effort_none(), test_non_qwen_caller_supplied_effort_is_overridden_to_none(), test_non_qwen_reasoning_effort_already_none_is_noop() (+3 more)

### Community 1290 - "test_delegation.py"
Cohesion: 0.15
Nodes (4): Tests for gateway/security/delegation.py — V9-T1: Owner-away privilege…, TestIsDelegated, TestRedelegation, TestRevoke

### Community 1292 - "test_integration.py"
Cohesion: 0.21
Nodes (12): asyncio, Test that /status endpoint works without authentication, Test /forward endpoint with proper authentication, Test /forward endpoint rejects requests without auth, Test ledger query endpoint, Test WebSocket authentication flow, Integration tests for the full gateway stack, test_forward_with_auth() (+4 more)

### Community 1293 - "run_multi_host"
Cohesion: 0.27
Nodes (5): _fake_runner(), Return a runner that looks up (exit_code, output) by host name., TestRunMultiHost, Run ``command`` on each host via ``runner`` and aggregate the results. A runner…, run_multi_host()

### Community 1294 - "TestGroupMemoryWriteACL"
Cohesion: 0.15
Nodes (7): A member of group B cannot write into group A's memory., A legitimate group member's write lands., The owner may write into any group's memory., Writing to a group that does not exist in the RBAC config is denied., Back-compat: with no RBAC context supplied, the namespace-isolation callers…, A user who is NOT a member of the target group cannot poison its memory., TestGroupMemoryWriteACL

### Community 1295 - "TestTelegramTokenRegistry"
Cohesion: 0.15
Nodes (5): Validate the token → bot_id registry logic extracted from the route handler., Token matching must be exact — case-sensitive., Registry maps two distinct tokens to two distinct bot_ids., Tokens are the registry keys — no two bots share a token., TestTelegramTokenRegistry

### Community 1296 - "TestParseModeStrippedAfterPIIRedaction"
Cohesion: 0.21
Nodes (7): Regression tests for Telegram HTML parse error caused by PII placeholders. When…, Return a TelegramAPIProxy configured with a mock owner RBAC., PII redaction must not strip parse_mode for the whole message (owner, fallback…, PII redaction must not strip parse_mode for the whole message (owner, fallback…, parse_mode=HTML must be preserved for owner when text contains no PII., PII redaction via the pipeline path must not strip parse_mode either (owner,…, TestParseModeStrippedAfterPIIRedaction

### Community 1297 - "API Documentation"
Cohesion: 0.50
Nodes (3): API Documentation, Current Status, Planned Documents

### Community 1298 - "Resources"
Cohesion: 0.50
Nodes (4): Community, Documentation, Related AgentShroud Docs, Resources

### Community 1299 - "camsnap/SKILL.md"
Cohesion: 0.50
Nodes (3): camsnap, camsnap CLI, ffmpeg dependency

### Community 1301 - "test_us_ssn_regex_tightened.py"
Cohesion: 0.21
Nodes (12): asyncio, CVE identifiers must NOT be treated as US_SSN., CVE IDs with 5-digit suffix must also be excluded., Real SSNs (not preceded by uppercase) must still be detected., Regression tests for the tightened US_SSN regex. CVE-2024-NNNN identifiers…, SSN at the very start of a string (no preceding character) is still flagged., A competitive-intel body with multiple CVEs is not collapsed into redaction…, test_cve_dense_report_body_preserved() (+4 more)

### Community 1302 - "Fail-Closed Outbound: pipeline exception blocks delivery to non-owner"
Cohesion: 0.50
Nodes (4): Fail-Closed Outbound: pipeline exception blocks delivery to non-owner, SharedMemoryManager Private Content Detection/Filtering, SlackAPIProxy Multi-Field Outbound Scanning (blocks, attachments), SlackAPIProxy Owner vs Collaborator Channel Filtering Tests

### Community 1303 - "Skill: Security Review (SEC)"
Cohesion: 0.15
Nodes (12): Anti-Patterns to Flag, Core Principle, Layer 1: Application Security, Layer 2: Container Security, Layer 3: Network Security, Layer 4: Data Flow Security, Output Format, Review Layers (+4 more)

### Community 1304 - "GSDL-715 (silent regression incident)"
Cohesion: 0.50
Nodes (4): Discrete confidence-score rubric, scripts/audit_merge_regression.py, GSDL-715 (silent regression incident), Finding Triage Classes (CONFIRMED/PROBABLE/SELF_HEALED/FALSE_POSITIVE/GOOD_DIRECTION)

### Community 1306 - "Workflow: Survey → Draft → Inject → Confirm"
Cohesion: 0.15
Nodes (12): Re-injection Command (for reference), Role, Rules, Skill: Session Prompt Generator (SESSION-PROMPT), Step 1 — Survey the Repo, Step 2 — Answer Six Questions, Step 3 — Write SESSION_PROMPT.md, Step 4 — Write the File (+4 more)

### Community 1307 - "Salesforce CLI (`sf`) Agent"
Cohesion: 0.15
Nodes (12): Auth Preflight (run FIRST, before any other `sf` command), Command Map, Data investigation, Failed deploy triage, Identity, Operating Rules (non-negotiable), Output Format, Risks (+4 more)

### Community 1308 - "Skill: Test-Driven Development (TDD)"
Cohesion: 0.15
Nodes (12): Anti-Patterns to Flag, Core Discipline: Red → Green → Refactor, Glue Job Logic  →  test transformations outside Spark, PostgreSQL  →  `SAVEPOINT` + `ROLLBACK`, Python / Boto3 / AWS  →  `moto`, Role, Rules, Skill: Test-Driven Development (TDD) (+4 more)

### Community 1309 - "pending (bot submits action requiring approval)"
Cohesion: 0.50
Nodes (4): approved (action executed, ledger entry written), expired (1-hour TTL exceeded, auto-transition on load), pending (bot submits action requiring approval), rejected (action blocked, bot notified)

### Community 1310 - "Outbound Infrastructure Content Filter (deny-list for hostnames, tool names, user IDs)"
Cohesion: 0.50
Nodes (4): Red Team Finding 00: Agent Self-Disclosure of Internal Architecture, Outbound Infrastructure Content Filter (deny-list for hostnames, tool names, user IDs), Red Team Finding 01: Security Modules Default to Monitor Mode — Zero Active Defense, Monitor-First Design Rationale: Observe → Tune → Enforce (operator must flip before production)

### Community 1311 - "Red Team Finding 02: No Human Approval for High-Risk Tool Calls"
Cohesion: 0.50
Nodes (4): Red Team Finding 02: No Human Approval for High-Risk Tool Calls, MCP Tool Risk Tier Classification (critical/high/medium/low) with Approval Policy, Red Team Finding 03: All Users Share Agent Context and File System, SessionManager — Telegram User ID as Partition Key for Workspaces and Memory

### Community 1312 - "Skill: Security Review (SEC)"
Cohesion: 0.15
Nodes (12): Anti-Patterns to Flag, Core Principle, Layer 1: Application Security, Layer 2: Container Security, Layer 3: Network Security, Layer 4: Data Flow Security, Output Format, Review Layers (+4 more)

### Community 1313 - "Workflow: Survey → Draft → Inject → Confirm"
Cohesion: 0.15
Nodes (12): Re-injection Command (for reference), Role, Rules, Skill: Session Prompt Generator (SESSION-PROMPT), Step 1 — Survey the Repo, Step 2 — Answer Six Questions, Step 3 — Write SESSION_PROMPT.md, Step 4 — Write the File (+4 more)

### Community 1314 - "Skill: Test-Driven Development (TDD)"
Cohesion: 0.15
Nodes (12): Anti-Patterns to Flag, Core Discipline: Red → Green → Refactor, Glue Job Logic  →  test transformations outside Spark, PostgreSQL  →  `SAVEPOINT` + `ROLLBACK`, Python / Boto3 / AWS  →  `moto`, Role, Rules, Skill: Test-Driven Development (TDD) (+4 more)

### Community 1315 - "SECURITY_VALUE_PROPOSITION.md"
Cohesion: 0.17
Nodes (8): Approval Queue Control, Defense in Depth (Bot Instructions + Gateway + Audit Log), Ultra-Conservative Credential Display Policy, Approval Queue — Core Security Value, MVP Recommendation (Option A), Multi-User/Multi-Tenant Threat Model (Reversal Driver), Multi-Layer .gitignore Secret Protection, Four-Layer Access Security Model (Password / Pairing / Allowlist / Approval)

### Community 1316 - "test_container_dns_check.py"
Cohesion: 0.23
Nodes (8): _block(), Path, Gateway DNS-server check in colima-health-check.sh (4c) and post-deploy-…, _run(), _run_hc(), _run_pd(), TestHealthCheckDnsServers, TestPostDeployDnsServers

### Community 1317 - "Incident Log — Conduit connectivity + prod stability, 2026-10-15/16"
Cohesion: 0.13
Nodes (14): Context, Daily Brief backfill — in progress, not complete, Fixes (all verified live), Fixes applied (live/runtime, working as of 05:50 EDT), For dev / prod sync, Incident Log — Conduit connectivity + prod stability, 2026-10-15/16, OpenClaw rebuild (makes the sandbox stopgap durable) — and what it dragged in, Other state (+6 more)

### Community 1318 - "Salesforce CLI (`sf`) Agent"
Cohesion: 0.15
Nodes (12): Auth Preflight (run FIRST, before any other `sf` command), Command Map, Data investigation, Failed deploy triage, Identity, Operating Rules (non-negotiable), Output Format, Risks (+4 more)

### Community 1319 - "Skill: Security Review (SEC)"
Cohesion: 0.15
Nodes (12): Anti-Patterns to Flag, Core Principle, Layer 1: Application Security, Layer 2: Container Security, Layer 3: Network Security, Layer 4: Data Flow Security, Output Format, Review Layers (+4 more)

### Community 1320 - "i-vulcan SKILL.md (Subject Matter Auditor, podcast QA gate)"
Cohesion: 0.50
Nodes (4): i-atlas SKILL.md (Curriculum Architect, referenced dependency), i-socrates SKILL.md (Dialogue Architect, referenced dependency), i-vulcan README.md, i-vulcan SKILL.md (Subject Matter Auditor, podcast QA gate)

### Community 1321 - "MCP OAuth preflight checker (mcp_oauth_preflight.py)"
Cohesion: 0.50
Nodes (4): MCP OAuth preflight checker (mcp_oauth_preflight.py), Atlassian OAuth 2.0 (3LO) config, GitHub OAuth device authorization flow config, Secrets stay in .env, never in the repo

### Community 1323 - "Workflow: Survey → Draft → Inject → Confirm"
Cohesion: 0.15
Nodes (12): Re-injection Command (for reference), Role, Rules, Skill: Session Prompt Generator (SESSION-PROMPT), Step 1 — Survey the Repo, Step 2 — Answer Six Questions, Step 3 — Write SESSION_PROMPT.md, Step 4 — Write the File (+4 more)

### Community 1324 - "8D Root Cause Analysis SKILL (OpenClaw)"
Cohesion: 0.50
Nodes (4): Data Validation (DATA-VAL) README (OpenClaw), Data Validation (DATA-VAL) SKILL (OpenClaw), 8D Root Cause Analysis README (OpenClaw), 8D Root Cause Analysis SKILL (OpenClaw)

### Community 1325 - "iCloud Services Skill"
Cohesion: 0.67
Nodes (4): 1Password item "Apple ID - therealidallasj", i-icloud README (ICLOUD Data Manager), iCloud Services Skill, calendar.js (iCloud CalDAV script)

### Community 1326 - "Skill: Test-Driven Development (TDD)"
Cohesion: 0.15
Nodes (12): Anti-Patterns to Flag, Core Discipline: Red → Green → Refactor, Glue Job Logic  →  test transformations outside Spark, PostgreSQL  →  `SAVEPOINT` + `ROLLBACK`, Python / Boto3 / AWS  →  `moto`, Role, Rules, Skill: Test-Driven Development (TDD) (+4 more)

### Community 1327 - "Salesforce CLI (`sf`) Agent"
Cohesion: 0.15
Nodes (12): Auth Preflight (run FIRST, before any other `sf` command), Command Map, Data investigation, Failed deploy triage, Identity, Operating Rules (non-negotiable), Output Format, Risks (+4 more)

### Community 1328 - "lib.sh"
Cohesion: 0.24
Nodes (11): lib.sh script, t_die(), t_finish(), t_have(), t_help(), t_init(), t_parse(), t_record() (+3 more)

### Community 1329 - "Technical Details"
Cohesion: 0.50
Nodes (4): Architecture, Files, Security Features, Technical Details

### Community 1330 - "Manual Usage (Current Method)"
Cohesion: 0.50
Nodes (4): Manual Usage (Current Method), Step 1: Create 1Password Share Link, Step 2: Fetch with Browser-Fetch Skill, Step 3: Parse Output

### Community 1331 - "🎨 Customize Skill Page (Optional)"
Cohesion: 0.50
Nodes (4): Add Long Description, Add Screenshots, Add Security Badge, 🎨 Customize Skill Page (Optional)

### Community 1332 - "Usage"
Cohesion: 0.15
Nodes (12): Add a comment to a card, Archive a card, Create a card, Examples, List boards, List cards in a list, List lists in a board, Move a card to another list (+4 more)

### Community 1333 - "Dockerfile — Gateway"
Cohesion: 0.17
Nodes (11): Build Stages, Dockerfile — Gateway, Environment Variables Set, Image Labels (OCI), Pre-installed Tools, Related Notes, Runtime Command, Security Hardening (+3 more)

### Community 1334 - "Athena — Knowledge Distiller"
Cohesion: 0.17
Nodes (11): Athena — Knowledge Distiller, cheatsheet.md, <description of what this does>, Input Requirements, Output Format, Persona, Quality Checklist, Role (+3 more)

### Community 1335 - "GSDE&G Development Master Checklist"
Cohesion: 0.17
Nodes (11): Emergency Hotfix, GSDE&G Development Master Checklist, Phase 1 · Plan & Branch  → `gg/SKILL.md`, Phase 2 · TDD  → `tdd/SKILL.md`, Phase 3 · QA  → `qa/SKILL.md`, Phase 4 · Code Review  → `cr/SKILL.md`, Phase 5 · Pull Request  → `pr/SKILL.md`, Phase 6 · CI  → `cicd/SKILL.md` (+3 more)

### Community 1336 - "Athena — Knowledge Distiller"
Cohesion: 0.17
Nodes (11): Athena — Knowledge Distiller, cheatsheet.md, <description of what this does>, Input Requirements, Output Format, Persona, Quality Checklist, Role (+3 more)

### Community 1337 - "Salesforce CLI (`sf`) Agent"
Cohesion: 0.17
Nodes (11): Command Map, Data investigation, Failed deploy triage, Identity, Operating Rules (non-negotiable), Output Format, Risks, Safe deploy (+3 more)

### Community 1338 - "TestLifespan"
Cohesion: 0.18
Nodes (5): When the Docker secret file exists, it wins over the env var., When the Docker secret file for the OpenAI key exists, it wins over the env var…, fake_exists(), fake_read_text(), TestLifespan

### Community 1339 - "Athena — Knowledge Distiller"
Cohesion: 0.17
Nodes (11): Athena — Knowledge Distiller, cheatsheet.md, <description of what this does>, Input Requirements, Output Format, Persona, Quality Checklist, Role (+3 more)

### Community 1340 - "GSDE&G Development Master Checklist"
Cohesion: 0.17
Nodes (11): Emergency Hotfix, GSDE&G Development Master Checklist, Phase 1 · Plan & Branch  → `gg/SKILL.md`, Phase 2 · TDD  → `tdd/SKILL.md`, Phase 3 · QA  → `qa/SKILL.md`, Phase 4 · Code Review  → `cr/SKILL.md`, Phase 5 · Pull Request  → `pr/SKILL.md`, Phase 6 · CI  → `cicd/SKILL.md` (+3 more)

### Community 1341 - "AgentShroud™ — OpenClaw Local-Model Tool-Use Instructions"
Cohesion: 0.17
Nodes (11): AgentShroud™ — OpenClaw Local-Model Tool-Use Instructions, Approved Tools and Their Arguments, bash, Critical Rules for Local Models, Example: Multi-Step Tool Use, Failover Behaviour (Local Mode), file_read, file_write (+3 more)

### Community 1342 - "setup-https-proxy.js"
Cohesion: 0.21
Nodes (9): ConnectProxyAgent, http, https, net, NO_PROXY_HOSTS, PatchedWebSocket, proxyCreateConnection(), shouldBypass() (+1 more)

### Community 1343 - "GSDE&G Development Master Checklist"
Cohesion: 0.17
Nodes (11): Emergency Hotfix, GSDE&G Development Master Checklist, Phase 1 · Plan & Branch  → `gg/SKILL.md`, Phase 2 · TDD  → `tdd/SKILL.md`, Phase 3 · QA  → `qa/SKILL.md`, Phase 4 · Code Review  → `cr/SKILL.md`, Phase 5 · Pull Request  → `pr/SKILL.md`, Phase 6 · CI  → `cicd/SKILL.md` (+3 more)

### Community 1344 - "DEVELOPER.md — Development Context for AgentShroud"
Cohesion: 0.17
Nodes (11): 1. Owner & Governance Context, 2. Project, 3. Prime Directive, 4. Development Rules (TDD), 5. Language & Tooling Standards, 6. Runtime Environment (CRITICAL), 7. SSH Development Workflow, 8. Agent Orchestration (+3 more)

### Community 1345 - "colima-health-check.sh"
Cohesion: 0.32
Nodes (11): _colima_vm_flags(), _dead_dns_servers(), log(), notify(), PATH, read_state(), resolve_docker_host(), colima-health-check.sh script (+3 more)

### Community 1346 - "CVE Registry — Manual Review List"
Cohesion: 0.40
Nodes (4): CVE Registry — Manual Review List, Hermes — 7 entries, Openclaw — 168 entries, Summary

### Community 1347 - "workspace.sh"
Cohesion: 0.42
Nodes (11): check_container(), cmd_cat(), cmd_cp_from(), cmd_cp_to(), cmd_ls(), cmd_mkdir(), cmd_rm(), cmd_shell() (+3 more)

### Community 1348 - "ADR-009: Enforce-by-Default Security Philosophy"
Cohesion: 0.17
Nodes (11): ADR-009: Enforce-by-Default Security Philosophy, Configuration, Consequences, Context, Decision, Migration from ADR-002, Negative Consequences, Policy Table (+3 more)

### Community 1349 - "Inbound MCP Edge — Plan (awaiting owner approval)"
Cohesion: 0.17
Nodes (11): 10. Open questions (decisions I need), 1. Architecture decision: a thin edge in front of a gateway that enforces policy, 2. Command Center (owner addendum 2026-11-09), 3. Prerequisite fixes the edge depends on (separate commits, RED first), 4. Modules and files, 5. Request pipeline order (FR5), 6. Test plan (RED first; each threat has a test that fails when its control is removed), 7. Commit sequence (branch `feat/inbound-mcp-edge`; no push or PR until you ask) (+3 more)

### Community 1350 - "Inbound MCP Edge — Design"
Cohesion: 0.17
Nodes (11): 1. Targets, 2. Architecture, 3. Pipeline order (gateway, every `tools/call`), 4. Sequences, 5. OAuth and enrollment, 6. Command Center (tailnet only), 7. Known limits, Delegation to Hermes (+3 more)

### Community 1351 - "Collaborator Setup Checklist"
Cohesion: 0.17
Nodes (11): Collaborator Setup Checklist, Executive Summary, Files intentionally not for collaborators, Optional local tooling, Required for local model-profile persistence, Required for standard Docker runtime, Required if using 1Password-backed secret retrieval, Required if using external LLM providers (+3 more)

### Community 1352 - "Startup Sequence"
Cohesion: 0.17
Nodes (12): Boot Sequence (Numbered), Common Startup Failures, First-Boot Notes, Overview, Related Notes, Stage 1: Gateway Container Startup, Stage 2: Gateway Application Initialization (main.py lifespan), Stage 3: Health Check (+4 more)

### Community 1353 - "E - Elevation of Privilege"
Cohesion: 0.50
Nodes (4): E - Elevation of Privilege, Threat: Container Escape, Threat: Docker Socket Access, Threat: Prompt Injection Attacks

### Community 1354 - "ssh_config.py"
Cohesion: 0.17
Nodes (11): Config Keys Read, Environment Variables Used, Imports From / Exports To, Key Classes / Functions, Known Issues / Notes, Purpose, Related, Responsibilities (+3 more)

### Community 1355 - "apply-patches.js"
Cohesion: 0.17
Nodes (11): Additional Patches, apply-patches.js, Behavior, Patch 1: Main Agent as Default, Patch 2: Telegram Binding, Patch 3: Telegram Bot Token (if $TELEGRAM_BOT_TOKEN is set), Patches Applied, Purpose (+3 more)

### Community 1356 - "forwarder.py"
Cohesion: 0.17
Nodes (9): Configuration / Environment Variables, forwarder.py, Function Details, HTTPForwarder.forward(path, body, headers, method), HTTPForwarder.set_response_handler(handler), Key Classes / Functions, Purpose, Related (+1 more)

### Community 1357 - "web_config.py"
Cohesion: 0.17
Nodes (11): Configuration / Environment Variables, Function Details, Key Classes / Functions, Purpose, Related, Responsibilities, web_config.py, WebProxyConfig Fields (+3 more)

### Community 1358 - "First Time Setup"
Cohesion: 0.17
Nodes (12): First Time Setup, Prerequisites, Related Notes, Step 1: Create Secret Files, Step 2: Configure agentshroud.yaml, Step 3: Configure 1Password Items, Step 4: Build Container Images, Step 5: Start Containers (+4 more)

### Community 1359 - "_FakeWSConnect"
Cohesion: 0.17
Nodes (7): websocket, WebSocket relay for Slack Socket Mode inbound traffic. Bot connects here…, slack_ws_relay(), _FakeWSConnect, Async context manager mimicking websockets.connect()., fake_connect(), upstream()

### Community 1360 - "compute_backoff"
Cohesion: 0.21
Nodes (8): compute_backoff(), Capped exponential backoff with jitter for reconnect attempts. Returns a wait…, Unit tests for the reconnect backoff calculation., With jitter pinned to max, backoff doubles per attempt until the cap., Backoff never exceeds the cap, even for huge attempt counts., Jitter scales the wait between 50% and 100% of the ceiling., Attempt 0 waits at most the base interval (1s default)., TestComputeBackoff

### Community 1361 - "get_sbom"
Cohesion: 0.23
Nodes (6): get_sbom(), Score domain 3: Supply Chain (0-5). 0=no SBOM, 2=SBOM exists, 3=SBOM has…, Return the latest SBOM (Software Bill of Materials) as parsed JSON., _score_supply_chain(), TestGetSbom, TestScoreSupplyChain

### Community 1362 - "._is_domain_allowed"
Cohesion: 0.20
Nodes (7): Check if a URL's domain is in the allowlist., Check if domain matches pattern (supports wildcards)., Check if URL contains any blocked patterns., Check if this is an internal link (relative, anchor, etc.)., Remove or warn about markdown images pointing to non-allowlisted domains., replace_image(), replace_link()

### Community 1363 - "TestMemberGroupContext"
Cohesion: 0.17
Nodes (7): Regular members can use medium-risk tools but not private/admin tools., Regular member IS allowed web_search in group context., Regular member IS allowed read/write in group context., Regular member denied gmail (private tool) even in group context., Regular member denied ssh (private tool) in group context., Regular member (non-owner group role) is denied high-risk tools that require…, TestMemberGroupContext

### Community 1364 - "§5 — Trivy Container Scan Results"
Cohesion: 0.50
Nodes (4): §5 — Trivy Container Scan Results, Gateway container (8 CRITICAL CVEs), Hermes container — Not scanned, OpenClaw container (17 CRITICAL CVEs)

### Community 1365 - "_fake_stats"
Cohesion: 0.26
Nodes (3): _fake_stats(), TestAnomalyDetection, TestHeartbeat

### Community 1370 - "Audit Branch (Merge Regression Detection)"
Cohesion: 0.67
Nodes (3): Audit Branch (Merge Regression Detection), GSDL-715 (Merge Regression Ticket), i-crpr — Production-Ready PR Skill

### Community 1371 - "kaizen Skill (stub)"
Cohesion: 0.67
Nodes (3): incident-response Skill (stub), kaizen Skill (stub), kanban Skill (stub)

### Community 1372 - "75 Active Security Modules — no stubs, fully wired"
Cohesion: 0.67
Nodes (3): 75 Active Security Modules — no stubs, fully wired, OpenClaw cron: AI Security Standards Watch (OWASP/NIST/ISO/MAESTRO/ATLAS), OpenClaw cron: Daily CVE Triage & Remediation Scan (cites agent_cve_registry.py)

### Community 1373 - "MCP tools available — GitHub (repos/PRs/issues), Atlassian (Jira/Confluence)"
Cohesion: 0.67
Nodes (3): MCP tools available — GitHub (repos/PRs/issues), Atlassian (Jira/Confluence), MCP Server: atlassian-agentshroud, MCP Server: github-agentshroud

### Community 1374 - "shared network (sidecar mode bridge)"
Cohesion: 0.67
Nodes (3): agentshroud-gateway service (sidecar mode, optional scan), openclaw service (sidecar mode, exposed normally), shared network (sidecar mode bridge)

### Community 1375 - "Claude Code (PRIMARY agent)"
Cohesion: 0.67
Nodes (3): Claude Code (PRIMARY agent), Codex CLI (TERTIARY agent), Gemini CLI (SECONDARY agent)

### Community 1379 - "TestKillSwitchVerification"
Cohesion: 0.26
Nodes (5): Path, Automated verification that verify_killswitch() returns required fields., dry_run=True must never trigger actual kill switch execution., verify_killswitch() must write a log entry for auditability., TestKillSwitchVerification

### Community 1380 - "[1.3.0] "Reliability" (2026-07-21)"
Cohesion: 0.14
Nodes (14): [0.1.0] - 2026-02-16, [1.2.3] — release/v1.2.3 (2026-06-29), [1.3.0] "Reliability" (2026-07-21), Added, Changed, Changed, Fixed, Fixed (+6 more)

### Community 1381 - "TestSetMode"
Cohesion: 0.17
Nodes (3): revert_after_minutes below 1 is clamped to 1., revert_after_minutes above 480 is clamped to 480., TestSetMode

### Community 1383 - "EU AI Act & NIST Alignment Matrix"
Cohesion: 0.67
Nodes (3): Governance Proxy Positioning (deployer compliance enabler), EU AI Act & NIST Alignment Matrix, SOC 2 Type II Attestation Path (SCRUM-99)

### Community 1385 - "AgentShroud Config with Tool Risk Tiers (example)"
Cohesion: 0.67
Nodes (3): PII confidence 0.8 (example) vs 0.9 floor (CLAUDE.md §7) discrepancy, Tool Risk Tier Policy (critical/high/medium/low), AgentShroud Config with Tool Risk Tiers (example)

### Community 1386 - "Changed"
Cohesion: 0.18
Nodes (11): [1.1.0] — feat-v1.4.0-shroud-another-bot — "Hermes" (2026-05-29), [1.2.2] — release/v1.2.2 (2026-06-28), Added, Changed, Changed, Changed, Fixed, Security (+3 more)

### Community 1387 - "OpenClaw cron: Collaborator Report - Morning (Telegram HTML, PII filter rules)"
Cohesion: 0.67
Nodes (3): OpenClaw cron: Collaborator Daily Digest, OpenClaw cron: Collaborator Report - Evening, OpenClaw cron: Collaborator Report - Morning (Telegram HTML, PII filter rules)

### Community 1390 - "openclaw-identity.md (OpenClaw bot identity)"
Cohesion: 0.67
Nodes (3): competitive-analysis.md (bot workspace competitive-intel source of truth), hermes-soul.md (Hermes system identity), openclaw-identity.md (OpenClaw bot identity)

### Community 1392 - "Diagram 08: Entity Relationship Diagram"
Cohesion: 0.67
Nodes (3): Diagram 08: Entity Relationship Diagram, Diagram 09: Data Lineage, Diagram 10: Data Dictionary (Mindmap)

### Community 1393 - "Gateway observability (GET /status, GET /ledger, MCP audit log, HTTP CONNECT proxy stats)"
Cohesion: 0.67
Nodes (3): Gateway observability (GET /status, GET /ledger, MCP audit log, HTTP CONNECT proxy stats), GET /ledger audit query API, Observability Gaps (Future Work): no log aggregation, no metrics export, no uptime monitor, Zabbix uninstalled

### Community 1395 - "test_playback_state/stubs/freertos/FreeRTOS.h"
Cohesion: 0.33
Nodes (4): TickType_t, xTaskGetTickCount(), TickType_t, vTaskDelay()

### Community 1397 - "test_wakeword_state/stubs/freertos/FreeRTOS.h"
Cohesion: 0.33
Nodes (4): TickType_t, xTaskGetTickCount(), TickType_t, vTaskDelay()

### Community 1398 - "TestRBACConfig"
Cohesion: 0.17
Nodes (7): Env overrides should drive runtime owner/collaborator identity., Test RBAC configuration., Test default RBAC configuration initialization., Test role hierarchy helper methods., Test dynamic role assignment., Test getting users by role., TestRBACConfig

### Community 1399 - "agentshroud-gateway pyproject config"
Cohesion: 0.67
Nodes (3): AgentShroud Gateway Package (__init__.py), Gateway OpenAPI Spec, agentshroud-gateway pyproject config

### Community 1400 - "Agent CVE Registry module (_AGENT_CVE_REGISTRIES etc.)"
Cohesion: 0.67
Nodes (3): Registry-integrity fix: fabricated CVE ids replaced with synthetic ASH refs, Agent CVE Registry module (_AGENT_CVE_REGISTRIES etc.), test_security_tool_entries_start_as_under_review_never_pre_claimed_mitigated

### Community 1401 - "MemoryIntegrityMonitor"
Cohesion: 0.13
Nodes (13): MemoryIntegrityMonitor, Path, Save integrity database to disk., Load active write windows from disk., Save active write windows to disk., Register an expected write to a file to prevent false alerts., Check if a file is currently in a write grace window., Attempt to detect the source of a file modification. Detection strategy (in… (+5 more)

### Community 1402 - "TrustManager._update_score"
Cohesion: 0.67
Nodes (3): TrustManager._promotion_allowed, TrustManager.record_violation, TrustManager._update_score

### Community 1403 - "Test Kill Switch Monitor"
Cohesion: 0.67
Nodes (3): Test Kill Switch Script Modes, Test Kill Switch Monitor, Test Observatory Mode API and Kill Switch Verification

### Community 1404 - "TestIsContainerRunning"
Cohesion: 0.21
Nodes (3): TestHostOsHardening, TestIsContainerRunning, boom()

### Community 1405 - "TestWebSecurity"
Cohesion: 0.17
Nodes (7): Test web dashboard and API security headers., Dashboard should have an HTML file., Dashboard should not contain hardcoded secrets., Dashboard should have Content-Security-Policy or mention it., Dashboard should not load HTTP resources., Dashboard should escape user inputs (no raw innerHTML from API)., TestWebSecurity

### Community 1406 - ".test_full_access_collaborator_passes_despite_multi_turn_middleware_block_without_interrogative"
Cohesion: 0.17
Nodes (7): Middleware block must be bypassed for full_access collaborators., full_access bypass applies even when the message has no interrogative marker.…, project_scoped collaborators are still blocked when middleware blocks (non-…, fake_notify_blocked(), process_request(), process_request(), process_request()

### Community 1407 - "AgentShroud Weekly Upgrade — 2026-09-20 (DEV run, account: agentshroud-bot)"
Cohesion: 0.14
Nodes (14): 1. Summary line, 2. Environment mapping, 3. Upgrade table, 4. Security findings, 5. Verification evidence, 6. Breaking changes / manual follow-ups, 7. Rollback instructions, 8. Time spent (+6 more)

### Community 1411 - ".test_activity_command_renders_entries"
Cohesion: 0.18
Nodes (7): _send_owner_pending_notice must append Pending Egress Requests when queue non-…, _send_owner_activity_notice must render tracker entries or honest error., When tracker has entries, /activity renders them., When tracker is None, /activity returns honest error, not silent empty., TestOwnerActivityNotice, TestPendingNoticeIncludesEgressSection, _capture()

### Community 1413 - "Athena — Knowledge Distiller"
Cohesion: 0.17
Nodes (11): Athena — Knowledge Distiller, cheatsheet.md, <description of what this does>, Input Requirements, Output Format, Persona, Quality Checklist, Role (+3 more)

### Community 1414 - "GSDE&G Development Master Checklist"
Cohesion: 0.17
Nodes (11): Emergency Hotfix, GSDE&G Development Master Checklist, Phase 1 · Plan & Branch  → `gg/SKILL.md`, Phase 2 · TDD  → `tdd/SKILL.md`, Phase 3 · QA  → `qa/SKILL.md`, Phase 4 · Code Review  → `cr/SKILL.md`, Phase 5 · Pull Request  → `pr/SKILL.md`, Phase 6 · CI  → `cicd/SKILL.md` (+3 more)

### Community 1415 - "i-hermes README (Podcast Production Orchestrator)"
Cohesion: 1.00
Nodes (3): i-hermes README (Podcast Production Orchestrator), Hermes — Reference Verifier Skill, Podcast Production Pipeline (multi-agent)

### Community 1416 - "kaizen Skill (stub)"
Cohesion: 0.67
Nodes (3): incident-response Skill (stub), kaizen Skill (stub), kanban Skill (stub)

### Community 1417 - "pre-commit as single owner of .git/hooks/pre-commit"
Cohesion: 0.67
Nodes (3): pre-commit detect-secrets hook (v1.5.0, .secrets.baseline), pre-commit git-secrets local hook (AWS credential patterns), pre-commit as single owner of .git/hooks/pre-commit

### Community 1420 - "Athena — Knowledge Distiller"
Cohesion: 0.17
Nodes (11): Athena — Knowledge Distiller, cheatsheet.md, <description of what this does>, Input Requirements, Output Format, Persona, Quality Checklist, Role (+3 more)

### Community 1421 - "GSDE&G Development Master Checklist"
Cohesion: 0.17
Nodes (11): Emergency Hotfix, GSDE&G Development Master Checklist, Phase 1 · Plan & Branch  → `gg/SKILL.md`, Phase 2 · TDD  → `tdd/SKILL.md`, Phase 3 · QA  → `qa/SKILL.md`, Phase 4 · Code Review  → `cr/SKILL.md`, Phase 5 · Pull Request  → `pr/SKILL.md`, Phase 6 · CI  → `cicd/SKILL.md` (+3 more)

### Community 1422 - "Athena — Knowledge Distiller"
Cohesion: 0.17
Nodes (11): Athena — Knowledge Distiller, cheatsheet.md, <description of what this does>, Input Requirements, Output Format, Persona, Quality Checklist, Role (+3 more)

### Community 1423 - "GSDE&G Development Master Checklist"
Cohesion: 0.17
Nodes (11): Emergency Hotfix, GSDE&G Development Master Checklist, Phase 1 · Plan & Branch  → `gg/SKILL.md`, Phase 2 · TDD  → `tdd/SKILL.md`, Phase 3 · QA  → `qa/SKILL.md`, Phase 4 · Code Review  → `cr/SKILL.md`, Phase 5 · Pull Request  → `pr/SKILL.md`, Phase 6 · CI  → `cicd/SKILL.md` (+3 more)

### Community 1424 - "init_skill.py"
Cohesion: 0.24
Nodes (11): create_resource_dirs(), init_skill(), main(), normalize_skill_name(), parse_resources(), # TODO: Add actual script logic here, Normalize a skill name to lowercase hyphen-case., Skill Initializer - Creates a new skill from template Usage: init_skill.py… (+3 more)

### Community 1425 - "Weather Skill"
Cohesion: 0.17
Nodes (11): Commands, Current Weather, Forecasts, Format Codes, Format Options, Location, Notes, Quick Responses (+3 more)

### Community 1426 - "chat_console.py"
Cohesion: 0.23
Nodes (11): check_status(), main(), print_banner(), print_help(), Read gateway password from secrets file or environment., AgentShroud Text Chat Console - Chat with OpenClaw as Admin Usage: python3…, Display chat console banner, Check gateway and bot status (+3 more)

### Community 1427 - "Daedalus — Concept Illustrator"
Cohesion: 0.18
Nodes (10): architecture.puml (PlantUML), Daedalus — Concept Illustrator, diagrams/README.md, flow.mmd (Mermaid), Input Requirements, Output Format, Persona, Quality Checklist (+2 more)

### Community 1428 - "Daedalus — Concept Illustrator"
Cohesion: 0.18
Nodes (10): architecture.puml (PlantUML), Daedalus — Concept Illustrator, diagrams/README.md, flow.mmd (Mermaid), Input Requirements, Output Format, Persona, Quality Checklist (+2 more)

### Community 1429 - "docs"
Cohesion: 0.22
Nodes (11): items, maxItems, type, maxLength, type, docs, source_cidrs, items (+3 more)

### Community 1444 - "Daedalus — Concept Illustrator"
Cohesion: 0.18
Nodes (10): architecture.puml (PlantUML), Daedalus — Concept Illustrator, diagrams/README.md, flow.mmd (Mermaid), Input Requirements, Output Format, Persona, Quality Checklist (+2 more)

### Community 1445 - "run-standalone.sh"
Cohesion: 0.29
Nodes (7): cmd_down(), cmd_logs(), cmd_status(), cmd_up(), _dashboard_host_default(), run-standalone.sh script, _wait_for_gateway_healthy()

### Community 1446 - "Inbound MCP Edge — Phase 0 Discovery"
Cohesion: 0.18
Nodes (10): 1. Repo layout, build and test, 2. Baseline measurements (run now), 3. Defense layers and reusable interfaces, 4. Mechanisms the edge depends on, 5. Hermes, local agents and networking, 6. Pre-existing findings (not caused by this work), 7. External specs verified (2026-11-09), 8. Gaps this feature needs filled (+2 more)

### Community 1447 - "Tailscale Remote Access Setup"
Cohesion: 0.18
Nodes (10): Access OpenClaw Dashboard Remotely, Current Status, Next Steps, Option 1: OpenClaw Control UI on Port 18790, Option 2: Gateway Dashboard on Port 8080, Option 3: Both Services, Security: Tailscale ACLs, Stop Tailscale Serve (+2 more)

### Community 1456 - "Git History Purge Plan"
Cohesion: 0.18
Nodes (10): Claude (Codex on Marvin), Git History Purge Plan, GitHub Cache Warning, Pi, Post-Purge — Other Instances, Post-Rotation Verification, Pre-Purge Checklist, Procedure (+2 more)

### Community 1466 - "Quick Reference — AgentShroud"
Cohesion: 0.18
Nodes (11): Common Issues, Configuration Files, Environment Variables (required), Health Checks, Key Ports, Kill Switch, Logs, Quick Reference — AgentShroud (+3 more)

### Community 1472 - "EnhancedApprovalQueue (`enhanced_queue.py`)"
Cohesion: 0.18
Nodes (10): EnhancedApprovalQueue (`enhanced_queue.py`), Environment Variables Used, Key Class: `EnhancedApprovalQueue`, Persistence, Purpose, Related Notes, Responsibilities, Timeout Behavior (+2 more)

### Community 1473 - "sidecar.py"
Cohesion: 0.18
Nodes (9): Configuration / Environment Variables, Function Details, Key Classes / Functions, Purpose, Related, Responsibilities, Security Limitation Warning, sidecar.py (+1 more)

### Community 1477 - "Dockerfile — Bot (OpenClaw)"
Cohesion: 0.18
Nodes (10): Build Process, Config Defaults (Baked In), Directory Structure, Dockerfile — Bot (OpenClaw), Image Labels (OCI), Pre-installed Tools, Related Notes, Scripts Copied to `/usr/local/bin` (+2 more)

### Community 1483 - "Architecture Overview.md"
Cohesion: 0.17
Nodes (7): i-sav README (System Audit Vault), i-sav SKILL (System Audit Vault, Obsidian), Complete System Diagram, Full System Flowchart, Legend, Related Notes, Startup Flow Diagram (vault note)

### Community 1484 - "SlackSocketClient"
Cohesion: 0.22
Nodes (6): Open the WebSocket and process events until Slack requests disconnect., Maintains a persistent Socket Mode WebSocket connection to Slack. Call run() as…, Main reconnect loop. Runs until stop() is called., Signal the run loop to exit., Call apps.connections.open to get a fresh WSS URL., SlackSocketClient

### Community 1487 - "deep_security_test"
Cohesion: 0.06
Nodes (20): deep_security_test(), t_context(), t_drift(), t_egress(), t_encrypt(), t_git(), t_log(), t_prompt() (+12 more)

### Community 1494 - "InstructionEnvelope"
Cohesion: 0.24
Nodes (6): InstructionEnvelope, A signed instruction or tool result., Return a signed envelope for content., Return True if the envelope's signature is valid., Convenience: sign a system prompt as issuer='system'., Convenience: sign a tool result as issuer='tool:<tool_name>'.

### Community 1495 - "FileIntegrityRecord"
Cohesion: 0.22
Nodes (7): FileIntegrityRecord, Any, Get alerts from the last N hours., Get current integrity monitoring status., Record of a file's integrity state., Convert to dictionary for JSON serialization., Create from dictionary for JSON deserialization.

### Community 1496 - "ContentThreat"
Cohesion: 0.22
Nodes (6): ContentThreat, Scan memory file content for security threats., Sanitize content by removing/redacting threats., Validate content before writing to memory file., Detected threat in memory file content., Test cleanup of old threat records.

### Community 1497 - "._get_engine"
Cohesion: 0.18
Nodes (3): Return the container engine from app_state if not injected., Pull the latest image then restart the container., Read container logs via Docker Unix socket — fallback when engine unavailable.…

### Community 1498 - "TestClassicOverride"
Cohesion: 0.18
Nodes (7): parametrize, Classic instruction-override payloads — should have near-100% detection., PromptGuard scans high-confidence classic payloads with non-zero score., HeuristicClassifier returns injection or uncertain on known bad payloads., TestClassicOverride, TestHeuristicClassifierDirectly, TestPromptGuardDirectly

### Community 1499 - "test_api_contract_fuzz.py"
Cohesion: 0.18
Nodes (7): client(), _fuzzable_endpoints(), fixture, parametrize, (method, path) for every non-destructive route declaring a requestBody., Schema-driven contract fuzzing for the ingest/data-plane API (SCRUM-76).…, test_endpoint_survives_adversarial_body()

### Community 1500 - "test_credential_injector.py"
Cohesion: 0.20
Nodes (8): injector(), fixture, Verify that raw credential values never appear in log output., Create a temp secrets directory with a test credential., CredentialInjector with a custom mapping pointing at the temp secrets., Tests for gateway/security/credential_injector.py — verify secrets never leak., secrets_dir(), TestStatus

### Community 1504 - "test_egress_callback_stale.py"
Cohesion: 0.36
Nodes (10): asyncio, Stale-callback handling for EgressTelegramNotifier (kaizen fix). Telegram…, _real_err(), _stale_callback_err(), _stale_edit_err(), test_answer_callback_real_error_still_logs_error(), test_answer_callback_stale_logs_debug_not_error(), test_edit_decision_message_real_error_still_logs_error() (+2 more)

### Community 1512 - "test_proxy_gemini_translation_failure_falls_through_gracefully"
Cohesion: 0.22
Nodes (7): asyncio, If openai_to_gemini_request raises, the request must still be forwarded…, The combined path: /v1/chat/completions with model=gemini-* must end up POSTing…, Gemini-model-via-OpenAI-path translation. Mirrors…, test_proxy_gemini_translation_failure_falls_through_gracefully(), test_proxy_rewrites_gemini_via_openai_path(), mock_forward()

### Community 1526 - "parse_hosts"
Cohesion: 0.31
Nodes (3): TestParseHosts, parse_hosts(), Parse a comma/whitespace-separated host list into a de-duplicated list.…

### Community 1528 - "TestCollabLockdownNotifications"
Cohesion: 0.29
Nodes (4): Verify _quarantine_blocked_message sends threshold warnings to the collaborator., The 4th block stays at ALERT but must NOT fire a second notification., Owner should receive an escalation notice on the 3rd block., TestCollabLockdownNotifications

### Community 1529 - "TestResourceGuardAlertBridge"
Cohesion: 0.25
Nodes (5): Any, End-to-end: register the bridge on a real ResourceGuard, trigger its alert path…, The lifespan bridges ResourceGuard's native callback payload to…, Recreate the lifespan bridge closure verbatim from…, TestResourceGuardAlertBridge

### Community 1530 - "test_scorecard_scoring.py"
Cohesion: 0.31
Nodes (10): clean_clamav(), clean_falco(), clean_openscap_with_zero_fails(), clean_trivy(), not_run_clamav(), not_run_falco(), not_run_openscap(), not_run_trivy() (+2 more)

### Community 1533 - "TestListServices"
Cohesion: 0.18
Nodes (4): _known_services() must resolve each bot's real container name — not a hardcoded…, _boom(), TestKnownServices, TestListServices

### Community 1534 - "TestServiceManagerGetLogs"
Cohesion: 0.27
Nodes (4): asyncio, fixture, Unit tests for ServiceManager.get_logs — including module_filter behaviour., TestServiceManagerGetLogs

### Community 1536 - "TestTelegramProxyRouteMultiBot"
Cohesion: 0.18
Nodes (6): An unregistered token must not be matched — fail-closed., If no tokens are registered, any token must be rejected., Integration tests for the /telegram-api/{path} route with multi-bot registry., A request bearing the OpenClaw token resolves to 'openclaw' bot_id., A request bearing the Hermes token resolves to 'hermes' bot_id., TestTelegramProxyRouteMultiBot

### Community 1537 - "TestTrustProgression"
Cohesion: 0.18
Nodes (5): Test earning and losing trust., Agent should be promoted when score crosses threshold., Agent should be demoted on violations., Score should not go below 0., TestTrustProgression

### Community 1538 - "Daedalus — Concept Illustrator"
Cohesion: 0.18
Nodes (10): architecture.puml (PlantUML), Daedalus — Concept Illustrator, diagrams/README.md, flow.mmd (Mermaid), Input Requirements, Output Format, Persona, Quality Checklist (+2 more)

### Community 1539 - "Daedalus — Concept Illustrator"
Cohesion: 0.18
Nodes (10): architecture.puml (PlantUML), Daedalus — Concept Illustrator, diagrams/README.md, flow.mmd (Mermaid), Input Requirements, Output Format, Persona, Quality Checklist (+2 more)

### Community 1540 - "Daedalus — Concept Illustrator"
Cohesion: 0.18
Nodes (10): architecture.puml (PlantUML), Daedalus — Concept Illustrator, diagrams/README.md, flow.mmd (Mermaid), Input Requirements, Output Format, Persona, Quality Checklist (+2 more)

### Community 1541 - "export-email-reports.py"
Cohesion: 0.31
Nodes (10): Why report .md source files stand in for a missing sent-mail ledger, export_bot(), _list_report_files(), main(), _parse_since(), datetime, Path, Export dated competitive-report .md files (the source content actually emailed… (+2 more)

### Community 1542 - "oracle — best use"
Cohesion: 0.18
Nodes (10): Attaching files (`--file`), Commands (preferred), Engines (API vs browser), “Exhaustive prompt” restoration pattern, Golden path, Main use case (browser, GPT‑5.2 Pro), oracle — best use, Prompt template (high signal) (+2 more)

### Community 1543 - "Skill: Data Validation (DATA-VAL)"
Cohesion: 0.20
Nodes (9): 1. Schema Validation, 2. Partition Coverage, 3. Data Quality Checks, 4. Cross-Site Comparison, Critical: Cost Control, Role, Skill: Data Validation (DATA-VAL), Test Data Validation Pattern (+1 more)

### Community 1544 - "Available MCP Servers"
Cohesion: 0.20
Nodes (9): 1. GitHub MCP, 2. Atlassian MCP (Jira + Confluence), 3. AWS API MCP, Authentication Issues, Available MCP Servers, Common Errors, MCP Troubleshooting, Role (+1 more)

### Community 1547 - "browser/package.json"
Cohesion: 0.20
Nodes (9): author, description, keywords, license, main, name, scripts, test (+1 more)

### Community 1551 - "AgentShroud Sunday Upgrade — 2026-09-26 (DEV run)"
Cohesion: 0.15
Nodes (13): §0 Preflight, §1 Environment mapping, §2 Inventory & versions checked, §3 Bugs found and fixed this run (code changes, per owner directive — a needed fix is not grounds to skip), §4 Build / apply / verify (dev), §5 Security findings, §6 Breaking changes / manual follow-ups, §7 Rollback instructions (+5 more)

### Community 1552 - "skills/icloud/scripts/calendar.js"
Cohesion: 0.29
Nodes (9): args, CONFIG, createEvent(), { execSync }, getCredentials(), https, listEvents(), makeRequest() (+1 more)

### Community 1553 - "dlp"
Cohesion: 0.20
Nodes (10): additionalProperties, properties, required, type, maximum, type, enum, dlp (+2 more)

### Community 1554 - "Skill: Data Validation (DATA-VAL)"
Cohesion: 0.20
Nodes (9): 1. Schema Validation, 2. Partition Coverage, 3. Data Quality Checks, 4. Cross-Site Comparison, Critical: Cost Control, Role, Skill: Data Validation (DATA-VAL), Test Data Validation Pattern (+1 more)

### Community 1555 - "Available MCP Servers"
Cohesion: 0.20
Nodes (9): 1. GitHub MCP, 2. Atlassian MCP (Jira + Confluence), 3. AWS API MCP, Authentication Issues, Available MCP Servers, Common Errors, MCP Troubleshooting, Role (+1 more)

### Community 1556 - "Security Pipeline Flow"
Cohesion: 0.29
Nodes (6): Layer Reference, Monitor Mode, Overview, Related Notes, Security Pipeline Flow, Security Pipeline Layer Order

### Community 1557 - "hermes/skills/i-browser/package.json"
Cohesion: 0.20
Nodes (9): author, description, keywords, license, main, name, scripts, test (+1 more)

### Community 1558 - "hermes/skills/i-icloud/scripts/calendar.js"
Cohesion: 0.29
Nodes (9): args, CONFIG, createEvent(), { execSync }, getCredentials(), https, listEvents(), makeRequest() (+1 more)

### Community 1559 - "openclaw/skills/i-browser/package.json"
Cohesion: 0.20
Nodes (9): author, description, keywords, license, main, name, scripts, test (+1 more)

### Community 1560 - "Owner-elevation-over-unverified-origin refusal (owner directive 2026-09-15)"
Cohesion: 0.17
Nodes (12): ToolACLEnforcer.can_use_tool, can_use_tool_from_origin, ToolACLEnforcer._can_use_tool_impl, ToolACLEnforcer.can_use_tool_in_group_context, Owner-elevation-over-unverified-origin refusal (owner directive 2026-09-15), TrustManager.get_trust, TrustManager.is_tool_allowed, GHSA-58qx-6m8p-wh2j — Slack group DMs skip sender allowlists (+4 more)

### Community 1561 - "openclaw/skills/i-icloud/scripts/calendar.js"
Cohesion: 0.29
Nodes (9): args, CONFIG, createEvent(), { execSync }, getCredentials(), https, listEvents(), makeRequest() (+1 more)

### Community 1562 - "container-net-diag.sh"
Cohesion: 0.51
Nodes (9): fail(), has(), header(), http_test(), info(), pass(), container-net-diag.sh script, tcp_test() (+1 more)

### Community 1563 - "Cross-Turn Correlation Capability"
Cohesion: 0.22
Nodes (10): PromptArmor: Atlassian Rovo Content-Borne Injection Disclosure, Varonis: "RovoBlast: How One Click Triggered Atlassian's AI Assistant to Leak Data", context_guard.py Provenance Tagging (ContextSegment), Cross-Turn Correlation Capability, EgressFilter.check(), multi_turn_tracker.py / SubagentMonitor, OpenAI Agent Message-Board Coordination Attack, RovoBlast Attack (Atlassian Rovo AI) (+2 more)

### Community 1564 - "ADR-003: Two-Network Container Isolation"
Cohesion: 0.20
Nodes (9): ADR-003: Two-Network Container Isolation, Consequences, Context, Decision, Mitigation, Negative Consequences, Network Configuration, Positive Consequences (+1 more)

### Community 1565 - "iMessage Integration Fix - Using imsg + imessage-exporter"
Cohesion: 0.20
Nodes (9): Current Setup (CORRECT), iMessage Integration Fix - Using imsg + imessage-exporter, Next Steps, Option 1: Grant Automation Permission (REQUIRED), Option 2: Check if Messages.app is Signed In, Status, The Fix, The Problem (+1 more)

### Community 1566 - "How to Fix (5 Minutes)"
Cohesion: 0.20
Nodes (9): Current Status, How to Fix (5 Minutes), If It Still Doesn't Work, iMessage Permission Fix - Step by Step, Step 1: Switch to agentshroud-bot User, Step 2: Grant Automation Permission, Step 3: Test It, Step 4: Verify from Docker (+1 more)

### Community 1567 - "AgentShroud™ LLM Provider Setup & Switching Guide"
Cohesion: 0.20
Nodes (9): 1. Provision Your Secrets (API Keys & Tokens), 2. Apply Configuration & Restart, 3. Switching Models in OpenClaw, 4. Local Ollama Integration, 5. Verification & Troubleshooting, AgentShroud™ LLM Provider Setup & Switching Guide, How to Switch via Telegram:, Provider Model Strings: (+1 more)

### Community 1568 - "engine.py"
Cohesion: 0.20
Nodes (9): Abstract Method Reference, Configuration / Environment Variables, ContainerEngine._run(cmd, check, capture, timeout), engine.py, Function Details, Key Classes / Functions, Purpose, Related (+1 more)

### Community 1569 - "docker-compose.yml"
Cohesion: 0.20
Nodes (9): agentshroud (agentshroud-bot), Alternate Compose Files, docker-compose.yml, gateway (agentshroud-gateway), Networks, Related Notes, Secrets Files, Services (+1 more)

### Community 1615 - "Seccomp Profiles"
Cohesion: 0.20
Nodes (9): Allowed Syscall Categories, Applied By, Architecture Support, Blocked Syscalls (Notable), Default Action, Gateway vs Bot Profile Differences, Purpose, Related Notes (+1 more)

### Community 1652 - "HTTP 401 — Unauthorized"
Cohesion: 0.20
Nodes (9): 1Password Auth Failures, Auth Errors, Common Causes, Diagnosis, HTTP 401 — Unauthorized, `op read` Failing, Related Notes, Token Reset (+1 more)

### Community 1653 - "Egress Filter Errors"
Cohesion: 0.20
Nodes (9): Common Missing Domains, Diagnosis, Egress Filter Errors, Egress Filter Not Initialized, Fix: Add Domain to Allowlist, HTTP 403 — Egress Blocked, Monitor Mode — Egress Not Enforced, Related Notes (+1 more)

### Community 1654 - "LLM Operating Context — Isaiah Jefferson"
Cohesion: 0.17
Nodes (12): 0) PRIME DIRECTIVE (NON-NEGOTIABLE), 10. Glossary (Normalized), 1. Executive Summary, 2. Core Identity Model, 3) TEST-DRIVEN DEVELOPMENT, 5) SECURITY & SAFETY REQUIREMENTS, 6) OPERATIONAL CONSTRAINTS, 7) CLAUDE CODE OPERATIONAL RULES (+4 more)

### Community 1657 - "Error Index"
Cohesion: 0.20
Nodes (10): Auth Errors, Container Errors, Egress Filter Errors, Error Index, HTTP Status Codes, MCP Proxy Errors, PII Pipeline Errors, Prompt Injection Blocks (+2 more)

### Community 1658 - "Restart Procedure"
Cohesion: 0.20
Nodes (10): After Config Change, After Secret Rotation, Bot Only Restart, Full Stack Restart, Gateway Only Restart, Related Notes, Restart Procedure, Restart Verification (+2 more)

### Community 1659 - "TestAuditStore"
Cohesion: 0.20
Nodes (6): Test querying events with filters., Test audit store statistics., Test AuditStore functionality., Test logging audit events., Test hash chain maintains integrity., TestAuditStore

### Community 1661 - "TestCredentialInjector"
Cohesion: 0.20
Nodes (3): Test the CredentialInjector module., Agent container should have no secrets., TestCredentialInjector

### Community 1671 - "TestSecurityPolicyProtection"
Cohesion: 0.20
Nodes (6): Agent cannot modify SOUL.md behavioral instructions., Agent cannot modify SOUL.md even in workspace path., Agent cannot modify system prompt files., Agent cannot modify gateway configuration., Agent cannot modify security policies and behavioral instructions., TestSecurityPolicyProtection

### Community 1672 - "TestReadAccess"
Cohesion: 0.20
Nodes (6): Test read access controls., Agent can read its own workspace., Agent can read basic system info., Agent cannot read sensitive configuration., Reading gateway source should be flagged/blocked., TestReadAccess

### Community 1751 - "TestAgentShroudSourceCodeProtection"
Cohesion: 0.20
Nodes (6): Agent cannot modify AgentShroud's own source code., Agent cannot write to gateway Python source files., Agent cannot write to security module source files., Agent cannot write to security framework files., Any .py file in gateway directory should be blocked., TestAgentShroudSourceCodeProtection

### Community 1752 - "TestReportAPI"
Cohesion: 0.20
Nodes (4): fixture, Route-level: POST/GET /api/reports through the FastAPI app (SCRUM-79)., store(), TestReportAPI

### Community 1753 - "_mock_dir_with_fresh_files"
Cohesion: 0.20
Nodes (3): _mock_dir_with_fresh_files(), Like _mock_dir_with_files but mtime is now (fresh)., TestScoreComplianceAuditing

### Community 1754 - "TestDependencySecurity"
Cohesion: 0.20
Nodes (6): Test dependency and supply chain security., Security modules should not use pickle (deserialization attack)., No yaml.load() without Loader (arbitrary code execution)., Subprocess calls should not pass shell=True. Uses AST analysis to flag only a…, Requirements should have pinned versions., TestDependencySecurity

### Community 1755 - "TestManagementWSTokenScoping"
Cohesion: 0.20
Nodes (6): Management WebSocket endpoints should use scoped tokens, not master auth., WS /ws/activity should reject master auth token (R3-L4), WS /ws/activity should reject empty token, WS /ws/activity should accept scoped ws_ token, Scoped WS token should be consumed after first use (single-use), TestManagementWSTokenScoping

### Community 1757 - "_make_client"
Cohesion: 0.22
Nodes (5): _make_client(), stop() signals the run loop to exit., _get_wss_url raises RuntimeError when apps.connections.open fails., Unit tests for SlackSocketClient., TestSlackSocketClient

### Community 1758 - "TestFailsLoudly"
Cohesion: 0.22
Nodes (3): An unreachable feed must fail the run, not print '0 new' and exit 0., TestFailsLoudly, _boom()

### Community 1763 - ".test_proxy_request_returns_ack_only_updates_when_all_dropped"
Cohesion: 0.20
Nodes (6): proxy_request should increment inbound getUpdates stats when messages pass…, When all getUpdates items are locally handled/dropped, return ack-only…, proxy_request should track dropped updates (e.g. collaborator blocked command)., fake_forward(), fake_forward(), fake_forward()

### Community 1766 - ".test_collaborator_rate_limit_resets_after_window"
Cohesion: 0.20
Nodes (4): Once stranger exhausts rate limit, they get a rate-limit notice; owner is NOT…, Repeated rate-limited messages within the cooldown window send at most one…, Messages within the window are blocked; after the window passes they succeed., fake_rl_notice()

### Community 1771 - "_skills_reload_impl"
Cohesion: 0.20
Nodes (8): Exception, Path, Raised when SkillGuard blocks a dangerous skill tree before deploy., Resolve the source (``~/.llm_settings/``) and bot-config destinations.…, Re-read ``~/.llm_settings/``, scan for supply-chain risk, deploy to both bots.…, SkillGuardBlocked, _skills_reload_impl(), _skills_reload_paths()

### Community 1772 - "Skill: Data Validation (DATA-VAL)"
Cohesion: 0.20
Nodes (9): 1. Schema Validation, 2. Partition Coverage, 3. Data Quality Checks, 4. Cross-Site Comparison, Critical: Cost Control, Role, Skill: Data Validation (DATA-VAL), Test Data Validation Pattern (+1 more)

### Community 1774 - "Available MCP Servers"
Cohesion: 0.20
Nodes (9): 1. GitHub MCP, 2. Atlassian MCP (Jira + Confluence), 3. AWS API MCP, Authentication Issues, Available MCP Servers, Common Errors, MCP Troubleshooting, Role (+1 more)

### Community 1775 - "Skill: Data Validation (DATA-VAL)"
Cohesion: 0.20
Nodes (9): 1. Schema Validation, 2. Partition Coverage, 3. Data Quality Checks, 4. Cross-Site Comparison, Critical: Cost Control, Role, Skill: Data Validation (DATA-VAL), Test Data Validation Pattern (+1 more)

### Community 1776 - "Available MCP Servers"
Cohesion: 0.20
Nodes (9): 1. GitHub MCP, 2. Atlassian MCP (Jira + Confluence), 3. AWS API MCP, Authentication Issues, Available MCP Servers, Common Errors, MCP Troubleshooting, Role (+1 more)

### Community 1777 - "Skill: Data Validation (DATA-VAL)"
Cohesion: 0.20
Nodes (9): 1. Schema Validation, 2. Partition Coverage, 3. Data Quality Checks, 4. Cross-Site Comparison, Critical: Cost Control, Role, Skill: Data Validation (DATA-VAL), Test Data Validation Pattern (+1 more)

### Community 1778 - "Available MCP Servers"
Cohesion: 0.20
Nodes (9): 1. GitHub MCP, 2. Atlassian MCP (Jira + Confluence), 3. AWS API MCP, Authentication Issues, Available MCP Servers, Common Errors, MCP Troubleshooting, Role (+1 more)

### Community 1779 - "browser-fetch/package.json"
Cohesion: 0.20
Nodes (9): author, description, keywords, license, main, name, scripts, test (+1 more)

### Community 1780 - "AgentShroud Sunday Upgrade — 2026-09-06 (dev-only, read-only inventory → scoped fixes)"
Cohesion: 0.18
Nodes (10): 0. Pre-existing session context worth recording, 2. Upgrade table, 3. Security findings, 4. Verification evidence, 5. Breaking changes / manual follow-ups (human review needed), 6. Rollback instructions, 7. Time spent, 8. Branch / commits (+2 more)

### Community 1781 - "Sunday Upgrade 2026-10-11 — DEV run (agentshroud-bot, 03:00 ET)"
Cohesion: 0.17
Nodes (12): 1. Summary line, 2. Environment mapping, 3. Upgrade table (discovery 2026-10-11 ~03:01 EDT, `scripts/discover_upstream_versions.py --json`), 4. Security findings, 5. Verification evidence, 6. Breaking changes / manual follow-ups, 7. Rollback, 8. Time (+4 more)

### Community 1782 - "custom/icloud/scripts/calendar.js"
Cohesion: 0.29
Nodes (9): args, CONFIG, createEvent(), { execSync }, getCredentials(), https, listEvents(), makeRequest() (+1 more)

### Community 1783 - "test_apply_patches.js"
Cohesion: 0.20
Nodes (6): fs, os, PATCHES_FILE, path, ROSTER_ENV, { spawnSync }

### Community 1787 - "LLMProxy"
Cohesion: 0.03
Nodes (98): Compute the bot's internal base URL from hostname and port., LLMProxy, _bytes_only(), _stream(), Any, BaseException, Proxy a streaming LLM API request, yielding SSE chunks as they arrive. Used…, Scan request data for PII and injection across different provider formats. (+90 more)

### Community 1790 - "Skill: Git Workflow Guardian (GIT-GUARD)"
Cohesion: 0.22
Nodes (8): Branch Naming, Commit Messages  (Conventional Commits), Emergency Hotfix, Mandatory Workflow  (10 steps), Protected Branch, REFUSE These, Role, Skill: Git Workflow Guardian (GIT-GUARD)

### Community 1808 - "Skill: Pull Request (PR) Generator"
Cohesion: 0.22
Nodes (8): Constraints, Content Requirements, Header, Objective, Role, Safety, Skill: Pull Request (PR) Generator, Technical Detail

### Community 1840 - "Vulcan — Subject Matter Auditor"
Cohesion: 0.22
Nodes (8): Input Requirements, Output Format, Persona, Quality Checklist, Role, System Prompt, User Prompt Template, Vulcan — Subject Matter Auditor

### Community 1852 - "Learning System (Continuous Improvement)"
Cohesion: 0.22
Nodes (8): Confidence Scoring, Device Hierarchy, Knowledge Base Schema, Learning System (Continuous Improvement), Pattern Matching for New Incidents, What to Extract:, Why This Matters:, XML Configuration File Parsing

### Community 1858 - "Vulcan — Subject Matter Auditor"
Cohesion: 0.22
Nodes (8): Input Requirements, Output Format, Persona, Quality Checklist, Role, System Prompt, User Prompt Template, Vulcan — Subject Matter Auditor

### Community 1869 - "Proxy Layer"
Cohesion: 0.22
Nodes (9): MCP Server Integration Guide, MCP Proxy, Web Proxy, mcp-config.yml, http_proxy.py (HTTP CONNECT :8181, domain allowlist), mcp_proxy.py (MCP tool call gate), Op-Proxy (Credential Gateway), Proxy Layer (+1 more)

### Community 1876 - "AgentShroud Brand Guidelines"
Cohesion: 0.22
Nodes (8): AgentShroud Brand Guidelines, Brand Personality, Color Profiles, Contact, File Formats & Deliverables, Logo Files, Voice & Tone, Writing Style

### Community 1877 - "Quickstart"
Cohesion: 0.22
Nodes (9): asb Wrapper Script, 1. Clone, 2. Store credentials, 3. Start the stack, 4. Verify, 5. (Optional) Voice Terminal — ESP32-S3-BOX-3, `asb` reference, Prerequisites (+1 more)

### Community 1878 - "Skill: Git Workflow Guardian (GIT-GUARD)"
Cohesion: 0.22
Nodes (8): Branch Naming, Commit Messages  (Conventional Commits), Emergency Hotfix, Mandatory Workflow  (10 steps), Protected Branch, REFUSE These, Role, Skill: Git Workflow Guardian (GIT-GUARD)

### Community 1888 - "Skill: Pull Request (PR) Generator"
Cohesion: 0.22
Nodes (8): Constraints, Content Requirements, Header, Objective, Role, Safety, Skill: Pull Request (PR) Generator, Technical Detail

### Community 1891 - "Vulcan — Subject Matter Auditor"
Cohesion: 0.22
Nodes (8): Input Requirements, Output Format, Persona, Quality Checklist, Role, System Prompt, User Prompt Template, Vulcan — Subject Matter Auditor

### Community 1895 - "render_md_email.py"
Cohesion: 0.39
Nodes (8): _esc(), _inline(), main(), Markdown → HTML email renderer (Python stdlib only, no pip installs). Pre-…, Apply inline Markdown spans to plain text (no recursive nesting)., render(), _save_fence(), _render_table()

### Community 1900 - "Skill: Pull Request (PR) Generator"
Cohesion: 0.22
Nodes (8): Constraints, Content Requirements, Header, Objective, Role, Safety, Skill: Pull Request (PR) Generator, Technical Detail

### Community 1906 - "Vulcan — Subject Matter Auditor"
Cohesion: 0.22
Nodes (8): Input Requirements, Output Format, Persona, Quality Checklist, Role, System Prompt, User Prompt Template, Vulcan — Subject Matter Auditor

### Community 1907 - "Starting a Development Task via Hermes / OpenClaw"
Cohesion: 0.22
Nodes (8): How to start a task, Monitoring progress, Source of truth, Starting a Development Task via Hermes / OpenClaw, Status: ready to use, with 4 known gaps (see below), Things that will make a task halt and ask you, not fail silently, What happens automatically (confirmed real, in, What is **not** currently automated (the 4 gaps)

### Community 1912 - "AgentShroud Setup Guide"
Cohesion: 0.22
Nodes (8): AgentShroud Setup Guide, Environment Variables, Mac Studio Example, Multi-Instance Setup, Port Auto-Detection, Quick Start (5 minutes), What is AgentShroud?, What's Next?

### Community 1915 - "Architecture Overview"
Cohesion: 0.22
Nodes (9): Architecture Overview, Bot Container (`agentshroud-bot`), Container Architecture, Full System Diagram, Gateway Container (`agentshroud-gateway`), Gateway Internal Layer Order, Network Topology, Related Notes (+1 more)

### Community 1916 - "[1.5.0] "A2A Governance" (2026-08-14)"
Cohesion: 0.17
Nodes (12): [1.0.0] — feat/v1.0.0 — "Fortress" (2026-03-31), [1.5.0] "A2A Governance" (2026-08-14), Added, Changed, Compliance, Fixed, Hardened, Known issues (+4 more)

### Community 1917 - "ssh_proxy.py"
Cohesion: 0.22
Nodes (8): Configured Hosts, `execute(host: str, command: str, session_id: str) → SSHExecResult`, Key Class: `SSHProxy`, Purpose, Related Notes, Responsibilities, Security Notes, ssh_proxy.py

### Community 1918 - "api.py"
Cohesion: 0.22
Nodes (8): api.py, Key Endpoints, Purpose, Pydantic Models, Related Notes, Responsibilities, Runtime Engine Integration, Security

### Community 1919 - "falco-rules.yaml"
Cohesion: 0.22
Nodes (8): falco-rules.yaml, Integration, Network Enforcement, Priority Levels, Purpose, Related Notes, Rules Defined, Shell Spawning Exceptions

### Community 1920 - "pytest.ini"
Cohesion: 0.22
Nodes (8): Contents, Coverage Requirements, Purpose, pytest.ini, Related Notes, Test Execution, Test Locations, Why `/tmp/pytest_cache`

### Community 1921 - "wazuh-ossec.conf"
Cohesion: 0.22
Nodes (8): Alert Levels, Integration with Gateway, Key OSSEC Config Sections (Inferred), Purpose, Related Notes, Relationship to Other Security Modules, wazuh-ossec.conf, What Wazuh Monitors in AgentShroud

### Community 1922 - "AgentShroud Sunday Upgrade — 2026-09-25 (DEV run)"
Cohesion: 0.18
Nodes (11): §0 Preflight notes (in progress), §0b Session handoff — 03:00 attempt died, resuming at 05:01 ET, §1 Root-cause: dev run was crashing instantly, every attempt, on a real bug, §1b Inventory delta — Hermes vendor image, §1c `--phase all` run #2 — baseline+scan clean, gateway build FAILED, auto-rollback OK, §2 `--phase all` run #3 (05:28:31–06:28:34 ET) — PASS, §3 Mandated OpenClaw soak-status check — NOT_SOAKED (pre-existing, unrelated to this run), §4 CVE arm-2 triage (`triage-cve-mitigations.py`) — not run this session (+3 more)

### Community 1923 - "Final report"
Cohesion: 0.18
Nodes (11): §0c Follow-up session — 11:00 ET, closing the §3/§4/§5 gaps, Breaking changes / manual follow-ups, Environment mapping (discovered this session), Final report, Rollback instructions (dev), Security findings, Summary line, Time spent (+3 more)

### Community 1924 - "sunday-upgrade.sh"
Cohesion: 0.05
Nodes (42): Jira MCP writes blocked in unattended sessions (don't-ask mode / allowedTools), Soak status: boot-proof is not work-proof, sync-cve-registry NVD append writes to wrong registry constant, Wrapper 180-min timeout vs session cannot self-terminate, §0 Preflight, §1 Environment mapping, AgentShroud Sunday Upgrade — 2026-09-27, 08:00 ET verification pass (DEV run, session #2), Decision: no rebuild performed (+34 more)

### Community 1925 - "AGENTSHROUD_MODE"
Cohesion: 0.22
Nodes (8): Affected Modules, AGENTSHROUD_MODE, Behavior, Description, Related Notes, Startup Warnings, Usage, Values

### Community 1926 - "Presidio Analyzer"
Cohesion: 0.22
Nodes (8): Architecture, Confidence Threshold, Configured Entities, NLP Backend, Presidio Analyzer, Purpose, Related Notes, Where Used

### Community 1927 - "Container Errors"
Cohesion: 0.22
Nodes (8): Container Errors, Container Won't Stop (Stuck in Stopping), Exit Code Reference, `no-new-privileges` Security Denial, OOM Kill (Exit Code 137), Port Already in Use, Read-Only Filesystem Errors, Related Notes

### Community 1928 - "PII Pipeline Errors"
Cohesion: 0.22
Nodes (8): Excessive False Positives, PII Engine Not Initialized, PII Not Being Detected, PII Pipeline Errors, Redaction Breaking JSON/Structured Data, Related Notes, spaCy Model Issues, Tool Result PII Not Scanned

### Community 1929 - "load_all_secret_file_values"
Cohesion: 0.28
Nodes (5): load_all_secret_file_values(), Return all non-empty values from Docker secret files (CVE-2026-9352). Reads…, load_all_secret_file_values reads all Docker secret files for scrubbing., CredentialInjector.get_all_loaded_values returns all loaded credential values., TestLoadAllSecretFileValues

### Community 1930 - "ClassificationResult"
Cohesion: 0.25
Nodes (4): ClassificationResult, Result of injection classification., Heuristic Injection Classifier — multi-signal scoring for injection detection.…, Tests for heuristic injection classifier.

### Community 1931 - "test_chat_completions_alias.py"
Cohesion: 0.22
Nodes (5): client(), fixture, Alias for hermes v0.16.0's OpenAI client. POST /chat/completions (no /v1…, Regression: don't break the existing /v1/messages path., test_root_v1_messages_still_works_unchanged()

### Community 1932 - "test_clamav_scan_unavailable_degrades_silently"
Cohesion: 0.22
Nodes (6): clamscan binary missing (sidecar down) -> no exception, temp file removed., test_clamav_scan_clean_records_nothing(), test_clamav_scan_infected_records_stats(), _fake_clamscan(), test_clamav_scan_unavailable_degrades_silently(), test_clamav_scan_unlink_failure_swallowed()

### Community 1933 - "_script"
Cohesion: 0.33
Nodes (4): Tests for scripts/list_registry_ghsa_ids.py. Exists so the daily CVE triage job…, Smoke test against the actual committed registry — every real ghsa_id currently…, _script(), TestListRegistryGhsaIds

### Community 1936 - "TestInstructionNonce"
Cohesion: 0.22
Nodes (5): Each call generates a distinct nonce., A freshly generated nonce validates on first use., Replaying the same nonce is rejected., A nonce with a timestamp outside the 5-min window is rejected., TestInstructionNonce

### Community 1937 - "TestUserMemoryWriteACL"
Cohesion: 0.22
Nodes (5): A non-owner author cannot write into another user's private memory., A user may write into their own private memory., The owner may write into any user's private memory., Back-compat: existing callers that pass no author_id/rbac_config keep working., TestUserMemoryWriteACL

### Community 1939 - ".test_collaborator_rate_limit_notice_is_sent_for_each_limited_message"
Cohesion: 0.22
Nodes (4): Rate-limit notice path should key retry window by user_id, not chat_id., Repeated rate-limited messages should each receive a deterministic notice., If notice send fails, cooldown should not suppress the next retry attempt., fake_rate_notice()

### Community 1940 - "TestTelegram400Retry"
Cohesion: 0.31
Nodes (5): B1: one-shot 400-retry for unbalanced HTML parse errors., First sendMessage returns 400 'can't parse entities'; retry with plain text…, Persistent 400 returns the error after exactly one retry (no infinite loop)., TestTelegram400Retry, _fake_urlopen()

### Community 1941 - "TestToolRateLimiting"
Cohesion: 0.22
Nodes (5): Calls within limits should pass., Exceeding per-minute limit should return False., Rate limits are tracked independently per user., Tools not in the rate-limit map should always pass., TestToolRateLimiting

### Community 1943 - "test_v1_models_synthetic.py"
Cohesion: 0.22
Nodes (6): client(), fixture, parametrize, TestClient with a stubbed proxy IP that passes the network allowlist., Synthetic /v1/models/<id> response so hermes v0.16.0 preflight succeeds. The…, test_v1_models_get_returns_synthetic_200()

### Community 1944 - "TrustManager"
Cohesion: 0.13
Nodes (17): ADR-008: Progressive Trust Level System, Monitoring System Integration (Webhooks/Prometheus), Approval Queue (SQLite), Dashboard (WebSocket), Kill Switch (Monitor/Block/Isolate), ApprovalRequest (data entity), RateLimitBucket (data entity), TrustLevel (data entity) (+9 more)

### Community 1945 - "Skill: Git Workflow Guardian (GIT-GUARD)"
Cohesion: 0.22
Nodes (8): Branch Naming, Commit Messages  (Conventional Commits), Emergency Hotfix, Mandatory Workflow  (10 steps), Protected Branch, REFUSE These, Role, Skill: Git Workflow Guardian (GIT-GUARD)

### Community 1946 - "Skill: Pull Request (PR) Generator"
Cohesion: 0.22
Nodes (8): Constraints, Content Requirements, Header, Objective, Role, Safety, Skill: Pull Request (PR) Generator, Technical Detail

### Community 1947 - "Vulcan — Subject Matter Auditor"
Cohesion: 0.22
Nodes (8): Input Requirements, Output Format, Persona, Quality Checklist, Role, System Prompt, User Prompt Template, Vulcan — Subject Matter Auditor

### Community 1948 - "Skill: Git Workflow Guardian (GIT-GUARD)"
Cohesion: 0.22
Nodes (8): Branch Naming, Commit Messages  (Conventional Commits), Emergency Hotfix, Mandatory Workflow  (10 steps), Protected Branch, REFUSE These, Role, Skill: Git Workflow Guardian (GIT-GUARD)

### Community 1949 - "Skill: Pull Request (PR) Generator"
Cohesion: 0.22
Nodes (8): Constraints, Content Requirements, Header, Objective, Role, Safety, Skill: Pull Request (PR) Generator, Technical Detail

### Community 1950 - "Vulcan — Subject Matter Auditor"
Cohesion: 0.22
Nodes (8): Input Requirements, Output Format, Persona, Quality Checklist, Role, System Prompt, User Prompt Template, Vulcan — Subject Matter Auditor

### Community 1951 - "Skill: Git Workflow Guardian (GIT-GUARD)"
Cohesion: 0.22
Nodes (8): Branch Naming, Commit Messages  (Conventional Commits), Emergency Hotfix, Mandatory Workflow  (10 steps), Protected Branch, REFUSE These, Role, Skill: Git Workflow Guardian (GIT-GUARD)

### Community 1952 - "Skill: Pull Request (PR) Generator"
Cohesion: 0.22
Nodes (8): Constraints, Content Requirements, Header, Objective, Role, Safety, Skill: Pull Request (PR) Generator, Technical Detail

### Community 1953 - "Vulcan — Subject Matter Auditor"
Cohesion: 0.22
Nodes (8): Input Requirements, Output Format, Persona, Quality Checklist, Role, System Prompt, User Prompt Template, Vulcan — Subject Matter Auditor

### Community 1954 - "VIII. Evaluation"
Cohesion: 0.22
Nodes (9): TABLE IV: Test Coverage by Defense Layer, TABLE V: Phase 8.5 E2E Verification Scenarios, TABLE VI: Post-Remediation Coverage Summary, TABLE VII: Security Module Comparison, VIII-A. Test Coverage, VIII-B. Enforcement Verification, VIII-C. Module Coverage Matrix, VIII-D. Competitive Analysis (+1 more)

### Community 1955 - "SOUL"
Cohesion: 0.22
Nodes (8): Current Focus (AgentShroud v1.7.x), Decision-Making Style, How to Represent Isaiah, Identity, Long-Term Goals, SOUL, Thinking Style, Values

### Community 1956 - "📱 Required Accounts & Services"
Cohesion: 0.22
Nodes (9): 1. Phone Number (Separate from Main), 1Password (Optional — Teams / Shared Credentials), 2. Gmail Account (Dedicated for Bot), 3. Telegram Account (Bot Communication), 4. Secrets Backend (Credential Management), 5. OpenAI Account (LLM API), 6. Anthropic Account (Claude API), macOS Keychain (Default) (+1 more)

### Community 1957 - "Sunday Upgrade 2026-10-04 — DEV run (agentshroud-bot, 03:00 ET)"
Cohesion: 0.22
Nodes (9): 1. Summary line, 2. Environment mapping, 3. Upgrade table (discovery 2026-10-04 03:0x EDT, `scripts/discover_upstream_versions.py --json`), 4. Security findings (in progress), 5. Verification evidence, 6. Breaking changes / manual follow-ups, 7. Rollback, 8. Time (+1 more)

### Community 1958 - "Hermes — Reference Verifier"
Cohesion: 0.25
Nodes (7): Hermes — Reference Verifier, Input Requirements, Output Format, Persona, Quality Checklist, Role, System Prompt

### Community 1959 - "Mnemosyne — Retention Engineer"
Cohesion: 0.25
Nodes (7): Input Requirements, Mnemosyne — Retention Engineer, Output Format, Persona, Quality Checklist, Role, System Prompt

### Community 1960 - "Oracle — Feedback Analyst"
Cohesion: 0.25
Nodes (7): Input Requirements, Oracle — Feedback Analyst, Output Format, Persona, Quality Checklist, Role, System Prompt

### Community 1961 - "Hermes — Reference Verifier"
Cohesion: 0.25
Nodes (7): Hermes — Reference Verifier, Input Requirements, Output Format, Persona, Quality Checklist, Role, System Prompt

### Community 1962 - "Mnemosyne — Retention Engineer"
Cohesion: 0.25
Nodes (7): Input Requirements, Mnemosyne — Retention Engineer, Output Format, Persona, Quality Checklist, Role, System Prompt

### Community 1963 - "Oracle — Feedback Analyst"
Cohesion: 0.25
Nodes (7): Input Requirements, Oracle — Feedback Analyst, Output Format, Persona, Quality Checklist, Role, System Prompt

### Community 1964 - "AgentShroud Primary Logo"
Cohesion: 0.39
Nodes (5): AgentShroud Blue — #1583f0, AgentShroud Logo — Dark Background Variant, AgentShroud Merchandise/Stationery Mockup, AgentShroud Email Banner (600x150), AgentShroud Primary Logo

### Community 1965 - "[0.9.0] — feat/v0.9.0-soc-team-collab — "Sentinel" (2026-03-18)"
Cohesion: 0.25
Nodes (8): [0.9.0] — feat/v0.9.0-soc-team-collab — "Sentinel" (2026-03-18), Added — Tranche 1: True Collaboration Architecture, Added — Tranche 2: Private Service Data Isolation, Added — Tranche 3: Security Tools (IEC 62443 Alignment), Container Security Scorecard — Baseline Scores, Deferred to post-v1.0.0, Summary, Tests

### Community 1966 - "Owner vs Bot Telegram Identity Separation"
Cohesion: 0.40
Nodes (5): Owner vs Bot Telegram Identity Separation, Isaiah's Persona Package (IDENTITY.md/SOUL.md/USER.md), Slack Socket Mode Integration Architecture, Telegram Bot Setup (BotFather token + gateway config), Trust-Differentiated Processing (RBAC tiers)

### Community 1967 - "health_check"
Cohesion: 0.25
Nodes (6): health_check(), get, Health check endpoint for Docker. Reports degraded status when the OpenAI…, Health endpoint reports degraded when OpenAI client is not available., Health endpoint reports healthy when OpenAI client is available., TestHealthCheck

### Community 1968 - "test_main.py"
Cohesion: 0.29
Nodes (6): app(), client(), fixture, Tests for chatbot/main.py. Covers the four SCRUM-109 fixes: 1. Auth enforcement…, Import chatbot.main with a fresh module state (no real OpenAI)., TestAuthTokenSource

### Community 1969 - "Hermes — Reference Verifier"
Cohesion: 0.25
Nodes (7): Hermes — Reference Verifier, Input Requirements, Output Format, Persona, Quality Checklist, Role, System Prompt

### Community 1970 - "Collaborators"
Cohesion: 0.40
Nodes (5): Collaborator Session Isolation (blocked functions/skills), Collaborators, Collaborators, Advisory Collaborators (Brett, Chris, Gabriel, TJ), Steve Hay — Collaborator (Telegram ID 8279589982)

### Community 1971 - "Mnemosyne — Retention Engineer"
Cohesion: 0.25
Nodes (7): Input Requirements, Mnemosyne — Retention Engineer, Output Format, Persona, Quality Checklist, Role, System Prompt

### Community 1972 - "Hermes — Reference Verifier"
Cohesion: 0.25
Nodes (7): Hermes — Reference Verifier, Input Requirements, Output Format, Persona, Quality Checklist, Role, System Prompt

### Community 1973 - "AgentShroud v1.2.0 Master Plan"
Cohesion: 0.36
Nodes (8): AgentShroud v1.2.0 Master Plan, Workstream D: Sync Skills/MCP from ~/.llm_settings, AgentShroud v1.2.0 — Master Plan, Cross-cutting: branches + PR train, Open clarifications before coding starts, Out of scope for v1.2.0, Tracking + cadence, Why v1.2.0

### Community 1974 - "Oracle — Feedback Analyst"
Cohesion: 0.25
Nodes (7): Input Requirements, Oracle — Feedback Analyst, Output Format, Persona, Quality Checklist, Role, System Prompt

### Community 1975 - "AgentShroud — Collaborator Knowledge Base"
Cohesion: 0.25
Nodes (7): AgentShroud — Collaborator Knowledge Base, Collaboration Guidelines, Contact, Project Goals, What Does It Do?, What is AgentShroud?, Who Can Use It?

### Community 1976 - "Mnemosyne — Retention Engineer"
Cohesion: 0.25
Nodes (7): Input Requirements, Mnemosyne — Retention Engineer, Output Format, Persona, Quality Checklist, Role, System Prompt

### Community 1977 - "Oracle — Feedback Analyst"
Cohesion: 0.25
Nodes (7): Input Requirements, Oracle — Feedback Analyst, Output Format, Persona, Quality Checklist, Role, System Prompt

### Community 1978 - "Usage"
Cohesion: 0.25
Nodes (8): Check Status, Hermes / HCI, Port Reference, Start the Stack, Stop the Stack, Test Chat, Usage, View Logs

### Community 1979 - "docker-cleanup.sh"
Cohesion: 0.46
Nodes (7): cmd_buildkit(), cmd_diagnose(), cmd_nuclear(), cmd_restart(), cmd_safe_prune(), docker-cleanup.sh script, usage()

### Community 1980 - "docker/scripts/security-scan.sh"
Cohesion: 0.68
Nodes (7): alert_if_critical(), log(), run_clamav(), run_oscap(), run_sbom(), run_trivy(), security-scan.sh script

### Community 1981 - "port_manager.py"
Cohesion: 0.25
Nodes (7): Default Ports, Environment Variables, Key Class: `PortManager`, port_manager.py, Purpose, Related Notes, `resolve_ports(desired: dict[str, int]) → dict[str, int]`

### Community 1982 - "GATEWAY_OP_PROXY_URL"
Cohesion: 0.25
Nodes (7): Description, GATEWAY_OP_PROXY_URL, Related Notes, Security, Set In, Usage Flow, Value

### Community 1983 - "HTTP_PROXY / HTTPS_PROXY"
Cohesion: 0.25
Nodes (7): Current Status, Description, Gateway Proxy Port, HTTP_PROXY / HTTPS_PROXY, Related Notes, Value, When Enabled

### Community 1984 - "[Unreleased] — feat/v0.8.0-enforcement-hardening (session 3 — 2026-03-15)"
Cohesion: 0.20
Nodes (10): [1.2.1] — release/v1.2.1-quality-sweep (2026-06-27), Added, Fixed, Fixed, Summary, Summary, Tests, Tests (+2 more)

### Community 1985 - "TELEGRAM_API_BASE_URL"
Cohesion: 0.25
Nodes (7): Description, Effect, Related Notes, SDK Patch, Set In, TELEGRAM_API_BASE_URL, Value

### Community 1986 - "OpenClaw"
Cohesion: 0.25
Nodes (7): Config Location, Key Intercepted Paths, OpenClaw, Purpose, Related Notes, Role in AgentShroud, Version Note

### Community 1987 - "python-jose"
Cohesion: 0.25
Nodes (7): Auth Methods, Current Usage, Key Features, Purpose, python-jose, Related Notes, Security Note

### Community 1988 - "spaCy"
Cohesion: 0.25
Nodes (7): Fallback Behavior, First-Boot Performance, Model, Purpose, Related Notes, spaCy, Where Used

### Community 1989 - "06-operations.md"
Cohesion: 0.29
Nodes (7): 18. Runbook / Decision Tree — On-Call Logic, 19. Incident Response Flow — Severity & Escalation, 20. Monitoring & Observability Map, AgentShroud — Operations & Reliability Diagrams, Incident Response Flow — Severity & Escalation, Monitoring & Observability Map, Runbook / Decision Tree — On-Call Logic

### Community 1990 - "MCP Proxy Errors"
Cohesion: 0.25
Nodes (7): HTTP 400 — Unknown MCP Server, HTTP 403 — MCP Tool Permission Denied, HTTP 429 — MCP Rate Limit Exceeded, HTTP 502 — MCP Server Unreachable, MCP Proxy Errors, MCP Proxy Wrapper Issues (Bot Side), Related Notes

### Community 1992 - "GitHub Copilot CLI Setup Guide"
Cohesion: 0.25
Nodes (7): Agent Files Location, Built-in Default Agents, GitHub Copilot CLI Setup Guide, MCP Server Integration, Overview, Questions?, References

### Community 1993 - "Prompt Injection Blocks"
Cohesion: 0.25
Nodes (7): Common Injection Signatures Detected, False Positive (Legitimate Content Blocked), HTTP 400 — Prompt Injection Detected, Prompt Injection Blocks, Prompt Injection in Monitor Mode, Related Notes, Tool Result Injections

### Community 1994 - "SSH Proxy Errors"
Cohesion: 0.25
Nodes (7): Globally Denied Command, HTTP 403 — SSH Host Not Allowed, Related Notes, Session Duration Exceeded, SSH Connection Timeout, SSH Key Not Found, SSH Proxy Errors

### Community 1995 - "._sanitize_reason"
Cohesion: 0.32
Nodes (3): Strip internal paths and module names from block reasons before user display., TestNotifyUserBlockedSanitization, User-facing block reasons should not expose modules or file paths.

### Community 1996 - "AuditExportConfig"
Cohesion: 0.29
Nodes (4): AuditExportConfig, Configuration for audit export functionality., Default JSON-LD context for security ontology., Create test export configuration.

### Community 1997 - ".record_activity"
Cohesion: 0.25
Nodes (4): Append one activity entry for any tracked collaborator or the owner. Args:…, Mirror activity into workspace contributor logs used by daily digests., Normalize previews to single-line safe text for JSONL + markdown mirrors., Normalize username for safe contributor-log tokenization.

### Community 1998 - "MemoryLifecycleConfig"
Cohesion: 0.29
Nodes (6): MemoryLifecycleConfig, Configuration for memory lifecycle management., ContentThreatType, Enum, Types of content threats detected in memory files., Set up test environment.

### Community 2000 - "test_credential_isolation.py"
Cohesion: 0.25
Nodes (5): Verify Docker Compose configuration isolates secrets correctly., Gateway service should have secrets configured., Agent (agentshroud) service should not have credential secrets., Tests for credential isolation — R-10, R-11, R-12. Verifies: - Gateway is the…, TestDockerSecretIsolation

### Community 2001 - "TestRunningImageResolution"
Cohesion: 0.25
Nodes (3): Regression guard (2026-08-30): the report scanned :latest tags while deploys…, _raise(), TestRunningImageResolution

### Community 2006 - "tail"
Cohesion: 0.39
Nodes (3): TestTail, Return the last ``lines`` non-trailing-empty lines of ``text``., tail()

### Community 2007 - "TestConfigurationProtection"
Cohesion: 0.25
Nodes (5): Agent cannot modify AgentShroud configuration files., Agent cannot write to gateway config directory., Agent cannot modify Docker Compose configuration., Agent cannot modify Dockerfile., TestConfigurationProtection

### Community 2008 - "TestSystemPathProtection"
Cohesion: 0.25
Nodes (5): Agent cannot modify system paths., Agent cannot write to /etc/ system configuration., Agent cannot write to /usr/bin/ system binaries., Agent cannot write to /var/log/ system logs., TestSystemPathProtection

### Community 2009 - "TestWorkspaceAccessPreserved"
Cohesion: 0.25
Nodes (5): Agent can still write to its own workspace., Agent can write to its own workspace directory., Agent can write to /tmp for temporary files., Agent can write to subdirectories in workspace., TestWorkspaceAccessPreserved

### Community 2010 - "TestSecurityViolationLogging"
Cohesion: 0.25
Nodes (5): Test that security violations are properly logged and tracked., Security violations should be recorded in audit log., Multiple violations should all be tracked., Normal workspace operations should not be flagged as violations., TestSecurityViolationLogging

### Community 2011 - "TestEdgeCases"
Cohesion: 0.25
Nodes (5): Test edge cases and potential bypass attempts., Path traversal attempts should be blocked., Relative paths should be resolved properly., Case variations should not bypass protection., TestEdgeCases

### Community 2012 - "TestAsyncSave"
Cohesion: 0.36
Nodes (3): asyncio, TestAsyncSave, _san()

### Community 2014 - "fs"
Cohesion: 0.25
Nodes (7): flags(), fs(), fixture, Redirect every Path(...) constructed inside the module into a sandbox. Absolute…, Replace _app_state_has with a controllable membership set., Replace shutil.which with a controllable name → path mapping., tools()

### Community 2016 - "[Unreleased] — feat/http-connect-proxy + feat/credential-isolation"
Cohesion: 0.29
Nodes (7): Added, Changed, Fixed, Security, Summary, Tests, [Unreleased] — feat/http-connect-proxy + feat/credential-isolation

### Community 2020 - "Available MCP Servers"
Cohesion: 0.50
Nodes (4): 1. GitHub MCP, 2. Atlassian MCP (Jira + Confluence), 3. AWS API MCP, Available MCP Servers

### Community 2021 - "Sunday upgrade 2026-10-25 (DEV run, account agentshroud-bot)"
Cohesion: 0.40
Nodes (4): 2. Environment mapping, 3. Upgrade table (in progress), Progress log (appended as work completes), Sunday upgrade 2026-10-25 (DEV run, account agentshroud-bot)

### Community 2022 - "copilot-instructions.md"
Cohesion: 0.29
Nodes (6): CLAUDE.md, Guidance for Claude Code (claude.ai/code) when working in this repository., Keep actions deterministic, minimal, and aligned with how this repo is actually run., KNOWLEDGE MAP — READ THIS FIRST, LLM OPERATING CONTEXT (llm-init), These instructions are authoritative. Follow them strictly.

### Community 2023 - "4. Technical Environment Baseline"
Cohesion: 0.29
Nodes (7): 4. Technical Environment Baseline, AI Workflow, BESS Systems, Cloud Infrastructure (AWS), Data Architecture, Local Development Environment, Programming Languages

### Community 2024 - "test_sync_cve_registry_ghsa.py"
Cohesion: 0.25
Nodes (5): Runs against the REAL gateway/security/agent_cve_registry.py. Every registered…, Tests for scripts/sync-cve-registry.py — Phase 1 GHSA under_review auto-…, An OpenClaw advisory diffed against the Hermes list yields it as 'new'. Proves…, TestLiveRegistryLayout, TestPerAgentIsolation

### Community 2025 - "TestNvdAppend"
Cohesion: 0.32
Nodes (3): fixture, The NVD source appends to the OpenClaw / Hermes lists through the same locator., TestNvdAppend

### Community 2028 - "TestTriageClassLevelCoverage"
Cohesion: 0.36
Nodes (4): The durable statement is at the CLASS level, not per-CVE. A register entry…, It calls itself DoS; the generic DOS profile is containment-only. Left as DOS…, The new rule runs first, so prove it does not swallow neighbours., TestTriageClassLevelCoverage

### Community 2029 - "Hermes — Reference Verifier"
Cohesion: 0.25
Nodes (7): Hermes — Reference Verifier, Input Requirements, Output Format, Persona, Quality Checklist, Role, System Prompt

### Community 2030 - "Mnemosyne — Retention Engineer"
Cohesion: 0.25
Nodes (7): Input Requirements, Mnemosyne — Retention Engineer, Output Format, Persona, Quality Checklist, Role, System Prompt

### Community 2031 - "Oracle — Feedback Analyst"
Cohesion: 0.25
Nodes (7): Input Requirements, Oracle — Feedback Analyst, Output Format, Persona, Quality Checklist, Role, System Prompt

### Community 2032 - "postmortem.md"
Cohesion: 0.25
Nodes (7): Contributing Factors, Follow-Up Actions, Incident Summary, Remediation, Root Cause, Test Added to Prevent Recurrence (MANDATORY), Timeline

### Community 2033 - "quick-setup.sh script"
Cohesion: 0.25
Nodes (4): quick-setup.sh script, security-audit.sh script, setup-direnv.sh script, setup-pgpass.sh script

### Community 2034 - "Workstream B: Security Features from Competitive Intel"
Cohesion: 0.38
Nodes (7): Workstream B: Security Features from Competitive Intel, Acceptance, B.1 — Lock the lead: 26+ modules, B.2 — Strengthen the report pipeline itself, Source of truth, Tests to add, Workstream B — Security features from competitive intel

### Community 2035 - "Hermes — Reference Verifier"
Cohesion: 0.25
Nodes (7): Hermes — Reference Verifier, Input Requirements, Output Format, Persona, Quality Checklist, Role, System Prompt

### Community 2036 - "Mnemosyne — Retention Engineer"
Cohesion: 0.25
Nodes (7): Input Requirements, Mnemosyne — Retention Engineer, Output Format, Persona, Quality Checklist, Role, System Prompt

### Community 2037 - "Oracle — Feedback Analyst"
Cohesion: 0.25
Nodes (7): Input Requirements, Oracle — Feedback Analyst, Output Format, Persona, Quality Checklist, Role, System Prompt

### Community 2038 - "Hermes — Reference Verifier"
Cohesion: 0.25
Nodes (7): Hermes — Reference Verifier, Input Requirements, Output Format, Persona, Quality Checklist, Role, System Prompt

### Community 2039 - "[1.1.1] — fix/guard-wiring-and-ops-hardening (2026-06-10)"
Cohesion: 0.33
Nodes (6): [1.1.1] — fix/guard-wiring-and-ops-hardening (2026-06-10), Added, Fixed, Removed, Security, Summary

### Community 2040 - "AgentShroud Data Assets (root)"
Cohesion: 0.33
Nodes (6): approval_items table (pending, approved, rejected, expired; 1h TTL), AgentShroud Data Assets (root), External Credentials (1Password vault), ledger table (indexed on timestamp, source, forwarded_to), OpenClaw Volume (openclaw.json, cron/jobs.json, sessions), SQLite DBs (Backed by SQLite)

### Community 2041 - "Mnemosyne — Retention Engineer"
Cohesion: 0.25
Nodes (7): Input Requirements, Mnemosyne — Retention Engineer, Output Format, Persona, Quality Checklist, Role, System Prompt

### Community 2042 - "VII. v0.8.0 Remediation"
Cohesion: 0.29
Nodes (7): VII-A. Enforce-by-Default (R-02, R-03), VII-B. Outbound Information Filter (R-01), VII-C. Per-User Session Isolation (R-04, R-05), VII-D. Separation of Privilege (R-06, R-07), VII-E. Human-in-the-Loop (R-08, R-09), VII-F. Credential Isolation (R-10, R-11, R-12), VII. v0.8.0 Remediation

### Community 2043 - "Oracle — Feedback Analyst"
Cohesion: 0.25
Nodes (7): Input Requirements, Oracle — Feedback Analyst, Output Format, Persona, Quality Checklist, Role, System Prompt

### Community 2044 - "PHASE 1: SECURITY FIX (CURRENT PRIORITY)"
Cohesion: 0.33
Nodes (6): 1.1 The Problem, 1.2 Root Cause Analysis, 1.3 Solution Options, 1.5 Testing Strategy, 1.6 Success Criteria, PHASE 1: SECURITY FIX (CURRENT PRIORITY)

### Community 2045 - "test-edge-isolation.sh"
Cohesion: 0.54
Nodes (7): _assert_blocked(), check(), _connect_probe(), _container_ips(), _http_probe(), test-edge-isolation.sh script, _tcp_probe()

### Community 2046 - "run_sourced"
Cohesion: 0.32
Nodes (3): check(), run_sourced(), test-edge-keygen.sh script

### Community 2047 - "Model usage"
Cohesion: 0.25
Nodes (7): Current model logic, Inputs, Model usage, Output, Overview, Quick start, References

### Community 2048 - "notion"
Cohesion: 0.25
Nodes (7): API Basics, Common Operations, Key Differences in 2025-09-03, Notes, notion, Property Types, Setup

### Community 2049 - "Model-Specific Parameters"
Cohesion: 0.25
Nodes (7): Model-Specific Parameters, OpenAI Image Gen, Other Notable Differences, Output, Quality, Run, Size

### Community 2050 - "Summarize"
Cohesion: 0.25
Nodes (7): Config, Model + keys, Quick start, Summarize, Useful flags, When to use (trigger phrases), YouTube: summary vs transcript

### Community 2051 - "Skill: CI/CD Pipeline Advisor (CICD)"
Cohesion: 0.29
Nodes (6): Deployment Matrix  (Direct to Prod), GitHub Actions Best Practices, Quality Gates  (execution order), Review Flags  (block the merge), Role, Skill: CI/CD Pipeline Advisor (CICD)

### Community 2052 - "Skill: Code Review (CR)"
Cohesion: 0.29
Nodes (6): Feedback Guidelines, Output Format, Production-Specific Review Checks, Review Principles, Role, Skill: Code Review (CR)

### Community 2053 - "Skill: CI/CD Pipeline Advisor (CICD)"
Cohesion: 0.29
Nodes (6): Deployment Matrix  (Direct to Prod), GitHub Actions Best Practices, Quality Gates  (execution order), Review Flags  (block the merge), Role, Skill: CI/CD Pipeline Advisor (CICD)

### Community 2054 - "Animation Guidelines"
Cohesion: 0.29
Nodes (7): Accessibility, Animation Guidelines, CSS Reference, Logo Animation Constraints, Motion Principles, Status & Feedback Animations, Timing & Easing

### Community 2055 - "chat"
Cohesion: 0.33
Nodes (7): chat(), ChatRequest, ChatResponse, BaseModel, post, Request, Process chat message with Isaiah's personality.

### Community 2056 - "TestAsyncClient"
Cohesion: 0.29
Nodes (4): Verify the module uses AsyncOpenAI, not sync OpenAI., A successful OpenAI completion returns 200 with the parsed fields via the…, OpenAI's own RateLimitError is translated to a 429 for the caller., TestAsyncClient

### Community 2057 - "Workstream E — Blue + red team security scan, both bots"
Cohesion: 0.33
Nodes (6): Acceptance, Intent, Phases, Source of truth, Tests to add, Workstream E — Blue + red team security scan, both bots

### Community 2058 - "TestAuth"
Cohesion: 0.29
Nodes (4): When CHATBOT_AUTH_TOKEN is set, /chat without a token returns 401., When CHATBOT_AUTH_TOKEN is set and correct token given, request proceeds., When CHATBOT_AUTH_TOKEN is not set, /chat is open (backward compat)., TestAuth

### Community 2059 - "schema.json"
Cohesion: 0.29
Nodes (6): additionalProperties, $id, required, $schema, title, type

### Community 2060 - "Skill: CI/CD Pipeline Advisor (CICD)"
Cohesion: 0.29
Nodes (6): Deployment Matrix  (Direct to Prod), GitHub Actions Best Practices, Quality Gates  (execution order), Review Flags  (block the merge), Role, Skill: CI/CD Pipeline Advisor (CICD)

### Community 2061 - "Skill: Code Review (CR)"
Cohesion: 0.29
Nodes (6): Feedback Guidelines, Output Format, Production-Specific Review Checks, Review Principles, Role, Skill: Code Review (CR)

### Community 2062 - "crashwatch.sh"
Cohesion: 0.52
Nodes (6): _count_recent_restarts(), _log(), _read_last_alert_epoch(), crashwatch.sh script, _telegram_alert(), _write_last_alert_epoch()

### Community 2063 - "_handle"
Cohesion: 0.48
Nodes (6): _handle(), main(), _pump(), StreamReader, StreamWriter, Relays 127.0.0.1:HERMES_DOCKER_RELAY_PORT -> docker-socket-proxy:2375. Hermes's…

### Community 2064 - "Quick Navigation"
Cohesion: 0.29
Nodes (7): Contributing, Getting Started, Quick Navigation, Security, Technical Documentation, Understanding the Project, Usage Guides

### Community 2065 - "Inbound MCP Edge — Threat Model"
Cohesion: 0.29
Nodes (6): 1. Trust boundaries, 2. Threats, controls, tests and residual risk, 3. Taxonomy corrections versus the brief, 4. Mutation evidence (2026-11-09), 5. Defects found while building, Inbound MCP Edge — Threat Model

### Community 2066 - "Apple Platform Integration"
Cohesion: 0.29
Nodes (6): AgentShroud Post-v1.0.0 Roadmap, Apple Platform Integration, Apple Watch Support, Control Center Widget (iPhone + macOS), Implementation Notes, Push Notifications (iPhone + Mac + Apple Watch)

### Community 2067 - "cve-mitigation-matrix.md"
Cohesion: 0.29
Nodes (6): CVE-2026-22172 — WebSocket Scope Self-Declaration, CVE-2026-22708 — AI Agent Container Escape via Prompt Injection, CVE-2026-30741 — RCE via Request-Side Prompt Injection, CVE-2026-32922 — Token Scope Expansion via device.token.rotate, CVE-2026-34425 — Preflight Validation Bypass (Shell-Bleed), CVE-2026-3690 — Canvas Authentication Bypass

### Community 2069 - "Important Notes"
Cohesion: 0.29
Nodes (7): Add Swap File, Backup Strategy, Cooling Recommendations, Important Notes, Optional: Automated Security Updates, Power Supply, Security Hardening Checklist

### Community 2070 - "Troubleshooting"
Cohesion: 0.29
Nodes (7): 1Password Authentication Failed, Container Unhealthy, Gmail Connection Issues, Performance Issues, Port Already in Use, Tests Failing, Troubleshooting

### Community 2071 - "installer.py"
Cohesion: 0.29
Nodes (6): Endpoints (Inferred), installer.py, Key Features, Purpose, Related Notes, When Used

### Community 2072 - "CI Workflows"
Cohesion: 0.29
Nodes (6): CI Workflows, Coverage Threshold, Expected Pipeline (Inferred), Key Test Command, Purpose, Related Notes

### Community 2073 - "gitleaks.toml"
Cohesion: 0.29
Nodes (6): gitleaks.toml, Integration, Purpose, Related Notes, Usage, What It Checks

### Community 2074 - "SSH Config"
Cohesion: 0.29
Nodes (6): Applied By, Key Configuration, Purpose, Related Notes, Relationship to agentshroud.yaml, SSH Config

### Community 2075 - "SECTION 5: IMPORTANT NOTES"
Cohesion: 0.40
Nodes (5): Employment IP Considerations, Entity Status: Small Entity (Confirmed), SECTION 5: IMPORTANT NOTES, What is NOT in this application (by design), What you MUST file within 12 months

### Community 2076 - "AGENTSHROUD_CONFIG"
Cohesion: 0.29
Nodes (6): AGENTSHROUD_CONFIG, Default Search Order (when NOT set), Description, Related Notes, Usage, When to Set

### Community 2077 - "Troubleshooting"
Cohesion: 0.40
Nodes (5): Agent Not Found, Authentication Issues, Configuration Not Loading, Path Permission Denied, Troubleshooting

### Community 2078 - "Basic Usage"
Cohesion: 0.40
Nodes (5): Basic Usage, Check Context Usage, Run with Specific Agent, Select Model, Start Interactive Session

### Community 2079 - "Installation"
Cohesion: 0.40
Nodes (5): Install Script, Installation, macOS / Linux, npm (Cross-platform), Windows

### Community 2080 - "Security & Permissions"
Cohesion: 0.40
Nodes (5): Path Permissions, Security & Permissions, Tool Approval, Trusted Folders, URL Access Control

### Community 2081 - "11. Hard Guardrails (Non-Negotiables)"
Cohesion: 0.40
Nodes (5): 11. Hard Guardrails (Non-Negotiables), Code Quality, Data Engineering, Documentation, Operations

### Community 2082 - "LOG_LEVEL"
Cohesion: 0.29
Nodes (6): Debug Mode, Description, LOG_LEVEL, Related Notes, Set In, Values

### Community 2083 - "ClamAV"
Cohesion: 0.29
Nodes (6): ClamAV, First Boot, Gateway Usage, Installation, Purpose, Related Notes

### Community 2084 - "Playwright"
Cohesion: 0.29
Nodes (6): Container Integration, Playwright, Purpose, Related Notes, Security Controls, Volume

### Community 2085 - "Pydantic"
Cohesion: 0.29
Nodes (7): Field Validators, Key Configuration Models, Purpose, Pydantic, Related Notes, v2 vs v1, Where Used

### Community 2086 - "Trivy"
Cohesion: 0.29
Nodes (6): ARM64 Support, Gateway Usage, Purpose, Related Notes, Script Usage, Trivy

### Community 2087 - "Docker Networks"
Cohesion: 0.29
Nodes (6): agentshroud-internal, agentshroud-isolated, DNS Resolution, Docker Networks, Network Architecture, Related Notes

### Community 2088 - "Delegation"
Cohesion: 0.33
Nodes (3): Delegation, A single time-bounded privilege delegation record., TestSerialization

### Community 2089 - "._cleanup_expired"
Cohesion: 0.29
Nodes (3): Return True if the user currently holds the delegated privilege., Return all currently active (non-expired) delegations., Return all active delegations held by a specific user.

### Community 2090 - "test_report_store.py"
Cohesion: 0.29
Nodes (3): Gateway-managed multi-bot report store (SCRUM-79). Both OpenClaw and Hermes…, Tests for ReportStore (SCRUM-79) — gateway-managed multi-bot report store., TestPersistence

### Community 2091 - "PHASE 3: iMESSAGE INTEGRATION TEST"
Cohesion: 0.40
Nodes (5): 3.1 Test Manual Send from Host, 3.2 Test from Container, 3.3 Test via OpenClaw /chat Endpoint, 3.4 Verify End-to-End Message Flow, PHASE 3: iMESSAGE INTEGRATION TEST

### Community 2092 - "TestOverallDetectionRate"
Cohesion: 0.29
Nodes (4): End-to-end: all 110+ payloads against combined defense layer., Ensure the payload library stays above 100 entries (CI regression gate)., Report per-category detection rates for observability (not a gate)., TestOverallDetectionRate

### Community 2093 - "TestModuleConfigDefaults"
Cohesion: 0.29
Nodes (3): Verify individual module configs default to enforce mode., Kill switch dry_run must be False — real termination on anomaly., TestModuleConfigDefaults

### Community 2094 - ".test_concurrent_log_event_two_connections_keeps_linear_chain"
Cohesion: 0.38
Nodes (5): _assert_linear_chain(), _chain_rows(), Concurrent log_event calls must not fork the SHA-256 chain (SCRUM-204)., Two stores sharing one SQLite file (e.g. two workers) must not fork the chain., TestAuditStoreConcurrentAppend

### Community 2097 - "CVE Triage — Gaps & Development Plan (OpenClaw)"
Cohesion: 0.40
Nodes (4): CVE Triage — Gaps & Development Plan (OpenClaw), Gap detail (development plan), Gap themes, Resulting status breakdown

### Community 2100 - "Workstream C — Full local-model parity for both bots"
Cohesion: 0.40
Nodes (5): Acceptance, Intent, Source of truth, Tests to add, Workstream C — Full local-model parity for both bots

### Community 2105 - "TestLLMProxyEndpoints"
Cohesion: 0.29
Nodes (4): The /v1/{path} endpoint must exist (enabled in v0.9.0)., The /llm-proxy/stats endpoint must exist., Proxy endpoint must not crash if upstream returns non-JSON body., TestLLMProxyEndpoints

### Community 2107 - "TestSkillsReloadEndpoint"
Cohesion: 0.38
Nodes (3): fixture, TestClient, TestSkillsReloadEndpoint

### Community 2108 - "_FakeUnixSocket"
Cohesion: 0.29
Nodes (3): _FakeUnixSocket, request(), Stand-in for socket.socket — records calls, never opens a real fd.

### Community 2112 - "Skill: CI/CD Pipeline Advisor (CICD)"
Cohesion: 0.29
Nodes (6): Deployment Matrix  (Direct to Prod), GitHub Actions Best Practices, Quality Gates  (execution order), Review Flags  (block the merge), Role, Skill: CI/CD Pipeline Advisor (CICD)

### Community 2113 - "Skill: Code Review (CR)"
Cohesion: 0.29
Nodes (6): Feedback Guidelines, Output Format, Production-Specific Review Checks, Review Principles, Role, Skill: Code Review (CR)

### Community 2114 - "AgentShroud Hermes — System Identity"
Cohesion: 0.29
Nodes (7): AgentShroud Hermes — System Identity, Capabilities, Core Behaviors, Owner, Remote Hosts (SSH via gateway), Trademark Notice, Your Role

### Community 2115 - "Skill: CI/CD Pipeline Advisor (CICD)"
Cohesion: 0.29
Nodes (6): Deployment Matrix  (Direct to Prod), GitHub Actions Best Practices, Quality Gates  (execution order), Review Flags  (block the merge), Role, Skill: CI/CD Pipeline Advisor (CICD)

### Community 2116 - "Skill: Code Review (CR)"
Cohesion: 0.29
Nodes (6): Feedback Guidelines, Output Format, Production-Specific Review Checks, Review Principles, Role, Skill: Code Review (CR)

### Community 2117 - "Skill: CI/CD Pipeline Advisor (CICD)"
Cohesion: 0.29
Nodes (6): Deployment Matrix  (Direct to Prod), GitHub Actions Best Practices, Quality Gates  (execution order), Review Flags  (block the merge), Role, Skill: CI/CD Pipeline Advisor (CICD)

### Community 2118 - "Skill: Code Review (CR)"
Cohesion: 0.29
Nodes (6): Feedback Guidelines, Output Format, Production-Specific Review Checks, Review Principles, Role, Skill: Code Review (CR)

### Community 2119 - "launchd/install.sh"
Cohesion: 0.67
Nodes (6): act(), install_agent(), install_dev_crontab(), plist_label(), say(), install.sh script

### Community 2120 - "Control Center"
Cohesion: 0.29
Nodes (6): AgentShroud Text Interfaces, Control Center, Controls, Future Interfaces, Usage, What it Shows

### Community 2121 - "browser/browse.js"
Cohesion: 0.40
Nodes (5): appendLog(), browserFetch(), { chromium }, fs, path

### Community 2122 - "Co-Branding Guidelines"
Cohesion: 0.33
Nodes (6): Approval Process, Co-Branding Guidelines, Color Constraints, Placement Rules, Principles, Prohibited Uses

### Community 2123 - "Brand Applications"
Cohesion: 0.33
Nodes (6): Brand Applications, Documentation, Presentations, Print Materials, Social Media, Website

### Community 2124 - "hermes/skills/i-browser/browse.js"
Cohesion: 0.40
Nodes (5): appendLog(), browserFetch(), { chromium }, fs, path

### Community 2125 - "i-ps SKILL (Production Safety Checklist / PROD-SAFETY)"
Cohesion: 0.33
Nodes (6): i-production README (Incident Response), i-production SKILL (Incident Response / INCIDENT), i-ps README (Production Safety Checklist), i-ps SKILL (Production Safety Checklist / PROD-SAFETY), i-qa README (Quality Assurance), i-qa SKILL (Quality Assurance / QA)

### Community 2126 - "openclaw/skills/i-browser/browse.js"
Cohesion: 0.40
Nodes (5): appendLog(), browserFetch(), { chromium }, fs, path

### Community 2127 - "IDENTITY.md - Who I Am"
Cohesion: 0.33
Nodes (5): Competitive Intelligence Protocol, IDENTITY.md - Who I Am, My Owner, My Responsibilities, My Role

### Community 2128 - "Critical Vulnerabilities Identified in OpenClaw (2026)"
Cohesion: 0.33
Nodes (6): 512 Total Vulnerabilities, 8 Critical, Critical Vulnerabilities Identified in OpenClaw (2026), CVE-2026-25253: WebSocket Origin Hijacking → Remote Code Execution, Malicious Skills on ClawHub: The Supply Chain Attack, Mass Exposure: 42,900+ Publicly Accessible Instances, The "Lethal Trifecta" - Enterprise Insider Threat

### Community 2129 - "Technical Decisions"
Cohesion: 0.33
Nodes (6): Technical Decisions, Why Internet-Only Access?, Why Localhost-Only Binding?, Why Manual Skill Approval?, Why Separate Digital Environment?, Why Separate Documentation Folder?

### Community 2130 - "AgentShroud Session Issue Register — 2026-03-14"
Cohesion: 0.33
Nodes (5): AgentShroud Session Issue Register — 2026-03-14, Issue Register, Linked Artifacts, Recommended Next Closure Sequence, Summary

### Community 2131 - "Phase 2: Development Tools"
Cohesion: 0.33
Nodes (6): Additional Dev Tools, Docker & Docker Compose, Git Configuration, Node.js (for OpenClaw & AgentShroud), Phase 2: Development Tools, Python (for testing tools)

### Community 2132 - "Performance Considerations"
Cohesion: 0.33
Nodes (6): CPU Throttling, Disk I/O, Memory Management, Network, Performance Considerations, Temperature Management

### Community 2133 - "Troubleshooting"
Cohesion: 0.33
Nodes (6): Docker Permission Denied, High Temperature, Out of Memory, Slow Builds, SSH Connection Refused, Troubleshooting

### Community 2134 - "Security Verification"
Cohesion: 0.33
Nodes (6): Audit Trail Verification, Dashboard Security Events, Health Check Verification, Production Checklist, Security Testing, Security Verification

### Community 2135 - "Common Workflows"
Cohesion: 0.50
Nodes (4): 1. Add Test Coverage, 2. Run Validation Suite, 3. Safe Refactor, Common Workflows

### Community 2136 - "Custom Agents"
Cohesion: 0.50
Nodes (4): 1. test-augmenter, 2. validation-runner, 3. safe-refactor, Custom Agents

### Community 2137 - "Repository Context"
Cohesion: 0.50
Nodes (4): Environment, Key Testing Requirements, Primary Focus, Repository Context

### Community 2138 - "0.1) MULTI-AGENT HIERARCHY (CLAUDE CODE IS PRIMARY)"
Cohesion: 0.50
Nodes (4): 0.1) MULTI-AGENT HIERARCHY (CLAUDE CODE IS PRIMARY), PRIMARY Developer: Claude Code (You), SECONDARY/TERTIARY Developers: Gemini CLI & ChatGPT Codex, When to Use Each Agent

### Community 2139 - "13. Anti-Patterns to Avoid"
Cohesion: 0.50
Nodes (4): 13. Anti-Patterns to Avoid, Communication, Process, Technical

### Community 2140 - "14. Decision-Making Hierarchy"
Cohesion: 0.50
Nodes (4): 14. Decision-Making Hierarchy, When to Act, When to Clarify, When to Defer

### Community 2141 - "3. Strategic Operating Model"
Cohesion: 0.50
Nodes (4): 3. Strategic Operating Model, Active Projects (Q1 2026), FY26 Strategic Objectives, Major Risks

### Community 2142 - "5. Governance & Risk Doctrine"
Cohesion: 0.50
Nodes (4): 5. Governance & Risk Doctrine, Governance Principles, Security Posture, Standards Alignment

### Community 2143 - "6. Working Style Contract"
Cohesion: 0.50
Nodes (4): 6. Working Style Contract, Avoid, Expectations, Optimize For

### Community 2144 - "7. Output Formatting Contract"
Cohesion: 0.50
Nodes (4): 7. Output Formatting Contract, Anti-Patterns, Preferred Formats, Required Components

### Community 2145 - "8. Automation Doctrine"
Cohesion: 0.50
Nodes (4): 8. Automation Doctrine, Deployment Pattern, Provisioning Philosophy, Tool Compatibility

### Community 2146 - "Step 3: Configure Secrets Management"
Cohesion: 0.33
Nodes (6): Option A: macOS Keychain (Default — no software required), Option B: Linux (secret-tool / GNOME Keyring — Default on Linux), Option C: 1Password Service Account (Optional — Teams / Shared Credentials), Option D: Docker Secrets (Swarm Mode), Option E: Environment Variables (Development Only), Step 3: Configure Secrets Management

### Community 2147 - "AgentShroud — Vault Home"
Cohesion: 0.33
Nodes (6): AgentShroud — Vault Home, Configuration & Infrastructure, Diagrams, Module Index, Navigate This Vault, Operations

### Community 2148 - "browser-fetch.js"
Cohesion: 0.33
Nodes (5): browser-fetch.js, Expected Behavior, Purpose, Related Notes, Security Controls

### Community 2149 - "text_control_center.py / agentshroud_manager.py"
Cohesion: 0.33
Nodes (5): Key Operations (Inferred), Purpose, Related Notes, Relationship to Web API, text_control_center.py / agentshroud_manager.py

### Community 2150 - "proxy_status.py"
Cohesion: 0.33
Nodes (5): Key Output, proxy_status.py, Purpose, Related Notes, Responsibilities

### Community 2151 - "aiosqlite"
Cohesion: 0.33
Nodes (6): aiosqlite, Database Files, Purpose, Related Notes, WAL Mode, Where Used

### Community 2152 - "httpx"
Cohesion: 0.33
Nodes (6): httpx, Key Features Used, Purpose, Related Notes, Security Note, Where Used

### Community 2153 - ".verify_export_integrity"
Cohesion: 0.33
Nodes (3): Parse CEF lines and extract entryHash/previousHash for chain verification.…, Verify the integrity of an exported audit log. Args: export_content: The…, timestamp()

### Community 2154 - "ingest_api/models.py"
Cohesion: 0.03
Nodes (87): exception_handler, global_exception_handler(), limit_request_body(), Exception, Reject request bodies larger than 1MB before parsing. Checks Content-Length…, Catch-all error handler Never leaks stack traces or internal details to client.…, ApprovalDecision, EmailSendRequest (+79 more)

### Community 2155 - "delegation.py"
Cohesion: 0.33
Nodes (5): DelegationError, Enum, ValueError, Owner-Away Privilege Delegation (v0.9.0 Tranche 1) Owner can delegate specific…, Raised when a delegation operation is invalid.

### Community 2156 - "_score_secure_development"
Cohesion: 0.40
Nodes (3): Score domain 11: Secure Development (0-5). 1=Trivy in build, 2=semgrep config,…, _score_secure_development(), TestScoreSecureDevelopment

### Community 2171 - "TestSnapshotSmoke"
Cohesion: 0.33
Nodes (3): The committed snapshot yields a real backlog, all honest under_review. Diffs…, Re-running against the LIVE registry adds nothing (backlog already synced)., TestSnapshotSmoke

### Community 2173 - ".test_forward_to_telegram_handles_http_error_non_json"
Cohesion: 0.33
Nodes (3): HTTPError JSON payloads should be returned as structured API responses., Non-JSON HTTPError payloads should still produce a safe fallback dict., _raise_http_error()

### Community 2174 - "TestOwnerMirrorCoalescing"
Cohesion: 0.40
Nodes (3): _mirror_to_owner_if_collaborator must coalesce within the window., TestOwnerMirrorCoalescing, _fake_admin_notice()

### Community 2178 - "gsd.md"
Cohesion: 0.33
Nodes (5): Approval Required By, Blast Radius, Effort, Outcome, Problem

### Community 2179 - "8. Docker System Pruning"
Cohesion: 0.33
Nodes (6): 8. Docker System Pruning, Check what would be removed (dry run), Nuclear prune (removes everything including volumes), Prune from inside Colima VM (use when host-side prune hangs), Reclaim space from dangling layers in overlay2, Safe prune (removes only stopped containers + unused images + build cache)

### Community 2180 - "Common Scenarios"
Cohesion: 0.33
Nodes (6): Common Scenarios, Scenario 1: New Browser/Computer, Scenario 2: Safari Private Window, Scenario 3: Multiple Computers, Scenario 4: Lost/Stolen Device, Scenario 5: Clear All Devices (Nuclear Option)

### Community 2181 - "browser-fetch.js"
Cohesion: 0.40
Nodes (5): appendLog(), browserFetch(), { chromium }, fs, path

### Community 2182 - "Browser Fetch Skill"
Cohesion: 0.33
Nodes (5): Browser Fetch Skill, Features, Security, Usage, Use Cases

### Community 2183 - "CodexBar CLI quick ref (usage + cost)"
Cohesion: 0.33
Nodes (5): CodexBar CLI quick ref (usage + cost), Commands, Cost JSON fields, Install, Notes

### Community 2184 - "6. Tailscale — secure ESP→Hermes link ✅ LIVE (see docs/integrations/voice-terminal-esp32-s3.md)"
Cohesion: 0.33
Nodes (6): 6. Tailscale — secure ESP→Hermes link ✅ LIVE (see docs/integrations/voice-terminal-esp32-s3.md), 6a. marvin is your tailnet host, 6b. Generate an auth key for the device, 6c. Add MicroLink to the firmware (SUPERSEDED — production uses Tailscale Funnel, no on-device client), 6d. Expose the Voice Gateway on marvin ✅ LIVE (`tailscale serve --bg 8765`), 6e. ACL lock-down (recommended)

### Community 2185 - "7) CODEX CLI OPERATIONAL RULES"
Cohesion: 0.40
Nodes (5): 7) CODEX CLI OPERATIONAL RULES, Network-looking failures on marvin are NOT DNS until proven (owner rule, 2026-10-24), What You Can Own, When to Defer to Claude Code, Your Role in the Multi-Agent System

### Community 2186 - "Apollo — Audio Systems Producer"
Cohesion: 0.40
Nodes (4): Apollo — Audio Systems Producer, Purpose, Related Skills, Usage

### Community 2187 - "Athena — Knowledge Distiller"
Cohesion: 0.40
Nodes (4): Athena — Knowledge Distiller, Purpose, Related Skills, Usage

### Community 2188 - "Atlas — Curriculum Architect"
Cohesion: 0.40
Nodes (4): Atlas — Curriculum Architect, Purpose, Related Skills, Usage

### Community 2189 - "Agentic AI Threat Intelligence Cron Prompt"
Cohesion: 0.67
Nodes (3): Agentic AI Threat Intelligence Cron Prompt, AI Security Standards Watch Cron Prompt, AI Security Standards Watch Job (OWASP / NIST AI RMF / MITRE ATLAS)

### Community 2190 - "Authentication"
Cohesion: 0.67
Nodes (3): Authentication, Option 1: GitHub Login, Option 2: Personal Access Token

### Community 2191 - "Context Management"
Cohesion: 0.67
Nodes (3): Auto-Compaction, Context Management, Manual Controls

### Community 2192 - "Configuration Files"
Cohesion: 0.67
Nodes (3): Configuration Files, MCP Servers, User-Level Config

### Community 2193 - "Role & Restrictions"
Cohesion: 0.67
Nodes (3): Role & Restrictions, What Copilot CLI CAN Do (in this repo), What Copilot CLI CANNOT Do (in this repo)

### Community 2194 - "12. Quality Threshold Definition"
Cohesion: 0.67
Nodes (3): 12. Quality Threshold Definition, Definition of Done (DoD), Validation Hierarchy (Priority Order)

### Community 2195 - "1) PROJECT IDENTITY"
Cohesion: 0.67
Nodes (3): 1) PROJECT IDENTITY, Key Files, Usage

### Community 2196 - "2) HOW TO WORK IN THIS REPO (SDLC EXPECTATIONS)"
Cohesion: 0.67
Nodes (3): 2) HOW TO WORK IN THIS REPO (SDLC EXPECTATIONS), Definition of Done, Preferred Workflow

### Community 2197 - "4) LANGUAGE & TOOLING STANDARDS"
Cohesion: 0.67
Nodes (3): 4) LANGUAGE & TOOLING STANDARDS, Bash Standards, Config Validation

### Community 2198 - "9. Multi-Agent Orchestration Rules"
Cohesion: 0.67
Nodes (3): 9. Multi-Agent Orchestration Rules, Decision Authority, Role Hierarchy

### Community 2199 - "AWS Cloud Management & FinOps"
Cohesion: 0.40
Nodes (4): AWS Cloud Management & FinOps, Purpose, Related Skills, Usage

### Community 2200 - "Browser — Secure Browser Automation"
Cohesion: 0.40
Nodes (4): Browser — Secure Browser Automation, Purpose, Related Skills, Usage

### Community 2201 - "Daedalus — Concept Illustrator"
Cohesion: 0.40
Nodes (4): Daedalus — Concept Illustrator, Purpose, Related Skills, Usage

### Community 2202 - "8D Root Cause Analysis"
Cohesion: 0.40
Nodes (4): 8D Root Cause Analysis, Purpose, Related Skills, Usage

### Community 2203 - "graphify Step 3 - Parts A, B and C"
Cohesion: 0.40
Nodes (4): graphify Step 3 - Parts A, B and C, Part A - Structural extraction for code files, Part B - Semantic extraction (parallel subagents), Part C - Merge AST + semantic into final extraction

### Community 2204 - "Hermes — Podcast Production Orchestrator"
Cohesion: 0.40
Nodes (4): Hermes — Podcast Production Orchestrator, Purpose, Related Skills, Usage

### Community 2205 - "Branding Specialist (BS)"
Cohesion: 0.40
Nodes (4): Branding Specialist (BS), Purpose, Related Skills, Usage

### Community 2206 - "CI/CD Pipeline Advisor (CICD)"
Cohesion: 0.40
Nodes (4): CI/CD Pipeline Advisor (CICD), Purpose, Related Skills, Usage

### Community 2207 - "Code Review (CR)"
Cohesion: 0.40
Nodes (4): Code Review (CR), Purpose, Related Skills, Usage

### Community 2208 - "Mode B — Comprehensive review sweep"
Cohesion: 0.40
Nodes (4): Mode B — Comprehensive review sweep, Step 1 — One branch + worktree for the whole sweep, Step 2 — Work through directories one at a time, Step 3 — After the last directory (or a natural stopping point)

### Community 2209 - "GSDE&G Development Master Checklist (MC)"
Cohesion: 0.40
Nodes (4): GSDE&G Development Master Checklist (MC), Purpose, Related Skills, Usage

### Community 2210 - "Mode B — Comprehensive review sweep"
Cohesion: 0.40
Nodes (4): Mode B — Comprehensive review sweep, Step 1 — One branch + worktree for the whole sweep, Step 2 — Work through directories one at a time, Step 3 — After the last directory (or a natural stopping point)

### Community 2211 - "Pull Request Generator (PR)"
Cohesion: 0.40
Nodes (4): Pull Request Generator (PR), Purpose, Related Skills, Usage

### Community 2212 - "Incident Response (INCIDENT)"
Cohesion: 0.40
Nodes (4): Incident Response (INCIDENT), Purpose, Related Skills, Usage

### Community 2213 - "Production Safety Checklist (PROD-SAFETY)"
Cohesion: 0.40
Nodes (4): Production Safety Checklist (PROD-SAFETY), Purpose, Related Skills, Usage

### Community 2214 - "iCloud Data Manager (ICLOUD)"
Cohesion: 0.40
Nodes (4): iCloud Data Manager (ICLOUD), Purpose, Related Skills, Usage

### Community 2215 - "macOS System Administrator (MAC)"
Cohesion: 0.40
Nodes (4): macOS System Administrator (MAC), Purpose, Related Skills, Usage

### Community 2216 - "Mnemosyne — Retention Engineer"
Cohesion: 0.40
Nodes (4): Mnemosyne — Retention Engineer, Purpose, Related Skills, Usage

### Community 2217 - "Oracle — Feedback Analyst"
Cohesion: 0.40
Nodes (4): Oracle — Feedback Analyst, Purpose, Related Skills, Usage

### Community 2218 - "System Audit Documentation"
Cohesion: 0.40
Nodes (4): Purpose, Related Skills, System Audit Documentation, Usage

### Community 2219 - "System Audit Vault"
Cohesion: 0.40
Nodes (4): Purpose, Related Skills, System Audit Vault, Usage

### Community 2220 - "Blue Team Security Auditor (SEC-DEFENSE)"
Cohesion: 0.40
Nodes (4): Blue Team Security Auditor (SEC-DEFENSE), Purpose, Related Skills, Usage

### Community 2221 - "Red Team Adversarial Tester (SEC-OFFENSE)"
Cohesion: 0.40
Nodes (4): Purpose, Red Team Adversarial Tester (SEC-OFFENSE), Related Skills, Usage

### Community 2222 - "Socrates — Dialogue Architect"
Cohesion: 0.40
Nodes (4): Purpose, Related Skills, Socrates — Dialogue Architect, Usage

### Community 2223 - "Vulcan — Subject Matter Auditor"
Cohesion: 0.40
Nodes (4): Purpose, Related Skills, Usage, Vulcan — Subject Matter Auditor

### Community 2224 - "7. CI/CD Quality Gates"
Cohesion: 0.40
Nodes (5): 6 CI Workflows, 14 Jobs, 7. CI/CD Quality Gates, Pipeline Overview, Pre-commit Hook Chain, Semgrep SAST Rules

### Community 2225 - "Press Kit"
Cohesion: 0.40
Nodes (5): About AgentShroud™, Approved Logo Assets for Media, Key Facts, Media Contact, Press Kit

### Community 2226 - "Logo Usage"
Cohesion: 0.40
Nodes (5): Backgrounds, Clear Space, Logo Usage, Minimum Size, Prohibited Uses

### Community 2227 - "_check_rate_limit"
Cohesion: 0.40
Nodes (4): _check_rate_limit(), Raise 429 if the client has exceeded the rate limit., Exceeding the rate limit returns 429., TestRateLimit

### Community 2228 - "TestErrorSanitization"
Cohesion: 0.40
Nodes (3): OpenAI exceptions should not leak internal details to the client., OpenAI AuthenticationError returns 503 without leaking the key., TestErrorSanitization

### Community 2230 - "tools"
Cohesion: 0.40
Nodes (5): enum, tools, additionalProperties, maxProperties, type

### Community 2231 - "Apollo — Audio Systems Producer"
Cohesion: 0.40
Nodes (4): Apollo — Audio Systems Producer, Purpose, Related Skills, Usage

### Community 2232 - "Athena — Knowledge Distiller"
Cohesion: 0.40
Nodes (4): Athena — Knowledge Distiller, Purpose, Related Skills, Usage

### Community 2233 - "Atlas — Curriculum Architect"
Cohesion: 0.40
Nodes (4): Atlas — Curriculum Architect, Purpose, Related Skills, Usage

### Community 2234 - "GSDE&G Development Master Checklist (MC)"
Cohesion: 0.40
Nodes (4): GSDE&G Development Master Checklist (MC), Purpose, Related Skills, Usage

### Community 2235 - "MCP Auth Reset (MCPM-AUTH-RESET)"
Cohesion: 0.40
Nodes (4): MCP Auth Reset (MCPM-AUTH-RESET), Purpose, Related Skills, Usage

### Community 2236 - "MCP AWS Profile Configuration (MCPM-AWS-PROFILE)"
Cohesion: 0.40
Nodes (4): MCP AWS Profile Configuration (MCPM-AWS-PROFILE), Purpose, Related Skills, Usage

### Community 2237 - "MCP Doctor (MCPM-DOCTOR)"
Cohesion: 0.40
Nodes (4): MCP Doctor (MCPM-DOCTOR), Purpose, Related Skills, Usage

### Community 2238 - "MCP Tools Usage (MCPM)"
Cohesion: 0.40
Nodes (4): MCP Tools Usage (MCPM), Purpose, Related Skills, Usage

### Community 2239 - "Mnemosyne — Retention Engineer"
Cohesion: 0.40
Nodes (4): Mnemosyne — Retention Engineer, Purpose, Related Skills, Usage

### Community 2240 - "Oracle — Feedback Analyst"
Cohesion: 0.40
Nodes (4): Oracle — Feedback Analyst, Purpose, Related Skills, Usage

### Community 2241 - "Project Management (PM)"
Cohesion: 0.40
Nodes (4): Project Management (PM), Purpose, Related Skills, Usage

### Community 2242 - "Pull Request Generator (PR)"
Cohesion: 0.40
Nodes (4): Pull Request Generator (PR), Purpose, Related Skills, Usage

### Community 2243 - "System Audit Documentation"
Cohesion: 0.40
Nodes (4): Purpose, Related Skills, System Audit Documentation, Usage

### Community 2244 - "Blue Team Security Auditor (SEC-DEFENSE)"
Cohesion: 0.40
Nodes (4): Blue Team Security Auditor (SEC-DEFENSE), Purpose, Related Skills, Usage

### Community 2245 - "cve_prefetch.py"
Cohesion: 0.60
Nodes (4): curl_json(), known_ghsa_ids(), main(), Deterministic prefetch for the CVE Triage cron job. Fetches both GitHub…

### Community 2246 - "Apollo — Audio Systems Producer"
Cohesion: 0.40
Nodes (4): Apollo — Audio Systems Producer, Purpose, Related Skills, Usage

### Community 2247 - "Athena — Knowledge Distiller"
Cohesion: 0.40
Nodes (4): Athena — Knowledge Distiller, Purpose, Related Skills, Usage

### Community 2248 - "Atlas — Curriculum Architect"
Cohesion: 0.40
Nodes (4): Atlas — Curriculum Architect, Purpose, Related Skills, Usage

### Community 2249 - "AWS Cloud Management & FinOps"
Cohesion: 0.40
Nodes (4): AWS Cloud Management & FinOps, Purpose, Related Skills, Usage

### Community 2250 - "Browser — Secure Browser Automation"
Cohesion: 0.40
Nodes (4): Browser — Secure Browser Automation, Purpose, Related Skills, Usage

### Community 2251 - "Branding Specialist (BS)"
Cohesion: 0.40
Nodes (4): Branding Specialist (BS), Purpose, Related Skills, Usage

### Community 2252 - "CI/CD Pipeline Advisor (CICD)"
Cohesion: 0.40
Nodes (4): CI/CD Pipeline Advisor (CICD), Purpose, Related Skills, Usage

### Community 2253 - "Code Review (CR)"
Cohesion: 0.40
Nodes (4): Code Review (CR), Purpose, Related Skills, Usage

### Community 2254 - "Git Workflow Guardian (GIT-GUARD)"
Cohesion: 0.40
Nodes (4): Git Workflow Guardian (GIT-GUARD), Purpose, Related Skills, Usage

### Community 2255 - "MCP Doctor (MCPM-DOCTOR)"
Cohesion: 0.40
Nodes (4): MCP Doctor (MCPM-DOCTOR), Purpose, Related Skills, Usage

### Community 2256 - "Mnemosyne — Retention Engineer"
Cohesion: 0.40
Nodes (4): Mnemosyne — Retention Engineer, Purpose, Related Skills, Usage

### Community 2257 - "Oracle — Feedback Analyst"
Cohesion: 0.40
Nodes (4): Oracle — Feedback Analyst, Purpose, Related Skills, Usage

### Community 2258 - "Project Management (PM)"
Cohesion: 0.40
Nodes (4): Project Management (PM), Purpose, Related Skills, Usage

### Community 2259 - "Pull Request Generator (PR)"
Cohesion: 0.40
Nodes (4): Pull Request Generator (PR), Purpose, Related Skills, Usage

### Community 2260 - "Incident Response (INCIDENT)"
Cohesion: 0.40
Nodes (4): Incident Response (INCIDENT), Purpose, Related Skills, Usage

### Community 2261 - "Production Safety Checklist (PROD-SAFETY)"
Cohesion: 0.40
Nodes (4): Production Safety Checklist (PROD-SAFETY), Purpose, Related Skills, Usage

### Community 2262 - "Quality Assurance (QA)"
Cohesion: 0.40
Nodes (4): Purpose, Quality Assurance (QA), Related Skills, Usage

### Community 2263 - "System Audit Documentation"
Cohesion: 0.40
Nodes (4): Purpose, Related Skills, System Audit Documentation, Usage

### Community 2266 - "System Audit Vault"
Cohesion: 0.40
Nodes (4): Purpose, Related Skills, System Audit Vault, Usage

### Community 2268 - "Blue Team Security Auditor (SEC-DEFENSE)"
Cohesion: 0.40
Nodes (4): Blue Team Security Auditor (SEC-DEFENSE), Purpose, Related Skills, Usage

### Community 2269 - "Red Team Adversarial Tester (SEC-OFFENSE)"
Cohesion: 0.40
Nodes (4): Purpose, Red Team Adversarial Tester (SEC-OFFENSE), Related Skills, Usage

### Community 2270 - "Security Review (SEC)"
Cohesion: 0.40
Nodes (4): Purpose, Related Skills, Security Review (SEC), Usage

### Community 2271 - "Socrates — Dialogue Architect"
Cohesion: 0.40
Nodes (4): Purpose, Related Skills, Socrates — Dialogue Architect, Usage

### Community 2272 - "Test-Driven Development (TDD)"
Cohesion: 0.40
Nodes (4): Purpose, Related Skills, Test-Driven Development (TDD), Usage

### Community 2273 - "Technical Illustrator (TI)"
Cohesion: 0.40
Nodes (4): Purpose, Related Skills, Technical Illustrator (TI), Usage

### Community 2274 - "Technical Writer (TW)"
Cohesion: 0.40
Nodes (4): Purpose, Related Skills, Technical Writer (TW), Usage

### Community 2275 - "Vulcan — Subject Matter Auditor"
Cohesion: 0.40
Nodes (4): Purpose, Related Skills, Usage, Vulcan — Subject Matter Auditor

### Community 2276 - "security-scheduler.sh"
Cohesion: 0.70
Nodes (4): log(), security-scheduler.sh script, _stamp_read(), _stamp_write()

### Community 2277 - "verify-security.sh"
Cohesion: 0.70
Nodes (4): check_fail(), check_pass(), check_warn(), verify-security.sh script

### Community 2278 - "run"
Cohesion: 0.70
Nodes (4): run script, log(), missing(), restart()

### Community 2279 - "ADR-001: Proxy-layer inversion model"
Cohesion: 0.40
Nodes (4): ADR-001: Proxy-layer inversion model, Alternatives rejected, Decision, Rationale

### Community 2281 - "AgentShroud — Diagram Library"
Cohesion: 0.40
Nodes (4): AgentShroud — Diagram Library, Diagrams Not Yet Implemented, Index, Priority Reading Order

### Community 2282 - "1Password Integration"
Cohesion: 0.40
Nodes (5): 1Password Integration, Configure AgentShroud, Create a Service Account, Important Notes, Set Up Vault Access

### Community 2283 - "Configuration Reference"
Cohesion: 0.40
Nodes (5): agentshroud.yaml - Main Configuration, Configuration Reference, egress-config.yml - Egress Filtering, Example Configurations, mcp-config.yml - MCP Server Registry

### Community 2284 - "Updating"
Cohesion: 0.40
Nodes (5): Manual Update Process, Rollback If Needed, Update AgentShroud, Update OpenClaw, Updating

### Community 2285 - "test_slack_socket_client.py"
Cohesion: 0.40
Nodes (3): Slack Socket Mode client — receives Slack events via outbound WebSocket. No…, asyncio, Tests for SlackSocketClient — gateway-side Slack Socket Mode listener. Verifies…

### Community 2308 - "TestDefenseLayerVocabulary"
Cohesion: 0.40
Nodes (3): Every layer the engine can emit must already be used by a mitigated entry in…, Every name in _PROACTIVE_ONLY_LAYERS must be independently proven wired into…, TestDefenseLayerVocabulary

### Community 2309 - "container-runtime.sh"
Cohesion: 0.50
Nodes (3): _cr_plugin_works(), detect_container_runtime(), container-runtime.sh script

### Community 2310 - "test-container-runtime.sh"
Cohesion: 0.70
Nodes (4): check(), make_fake_bin(), run_detect(), test-container-runtime.sh script

### Community 2311 - "test-skills-sync.sh"
Cohesion: 0.50
Nodes (4): check(), PYTHONPATH, test-skills-sync.sh script, SKILLGUARD_TEST_DEST_ROOT

### Community 2312 - "Multi-Layer Detection Strategy"
Cohesion: 0.40
Nodes (5): Layer 1: Pattern Matching, Layer 2: Unicode Normalization, Layer 3: Multi-Layer Decoding, Multi-Layer Detection Strategy, Prompt Injection Defense

### Community 2313 - "generate_image.py"
Cohesion: 0.50
Nodes (4): get_api_key(), main(), Get API key from argument first, then environment., Generate images using Google's Nano Banana Pro (Gemini 3 Pro Image) API. Usage:…

### Community 2314 - "OpenAI Whisper API (curl)"
Cohesion: 0.40
Nodes (4): API key, OpenAI Whisper API (curl), Quick start, Useful flags

### Community 2315 - "test_hermes_edge_delegate_profile.sh"
Cohesion: 0.60
Nodes (3): check(), run_block(), test_hermes_edge_delegate_profile.sh script

### Community 2316 - "test_hermes_mcp_reconciliation.sh"
Cohesion: 0.60
Nodes (3): check(), reconcile_noyaml(), test_hermes_mcp_reconciliation.sh script

### Community 2317 - "test_launchd_install.sh"
Cohesion: 0.70
Nodes (4): bad(), ok(), run_install(), test_launchd_install.sh script

### Community 2319 - "test_sunday_prompt_unattended.sh"
Cohesion: 0.70
Nodes (4): fail(), pass(), rc_ctx(), test_sunday_prompt_unattended.sh script

### Community 2321 - "2) WHAT YOU SHOULD DO (YOUR JOBS)"
Cohesion: 0.50
Nodes (4): 2) WHAT YOU SHOULD DO (YOUR JOBS), A) Test Augmenter (Primary Job), B) Validation Runner (Primary Job), C) Safe Refactor (Secondary Job)

### Community 2322 - "i-code-reviewer — Code reviewer and change-impact analyst (pre-commit)"
Cohesion: 0.50
Nodes (3): i-code-reviewer — Code reviewer and change-impact analyst (pre-commit), Playbook, Testing types owned (priority order)

### Community 2323 - "i-data-ai-ot — Data, AI/LLM and OT/BESS tester (any stage)"
Cohesion: 0.50
Nodes (3): i-data-ai-ot — Data, AI/LLM and OT/BESS tester (any stage), Playbook, Testing types owned (priority order)

### Community 2324 - "i-integration-qa — Integration and regression QA (PR/CI)"
Cohesion: 0.50
Nodes (3): i-integration-qa — Integration and regression QA (PR/CI), Playbook, Testing types owned (priority order)

### Community 2325 - "i-release-gate — Release gate and operational readiness (release / post-deploy)"
Cohesion: 0.50
Nodes (3): i-release-gate — Release gate and operational readiness (release / post-deploy), Playbook, Testing types owned (priority order)

### Community 2326 - "i-security-scanner — Security scanner (pre-commit)"
Cohesion: 0.50
Nodes (3): i-security-scanner — Security scanner (pre-commit), Playbook, Testing types owned (priority order)

### Community 2327 - "i-system-nfr — System and non-functional tester (pre-release)"
Cohesion: 0.50
Nodes (3): i-system-nfr — System and non-functional tester (pre-release), Playbook, Testing types owned (priority order)

### Community 2328 - "i-test-architect — Test architect (planning)"
Cohesion: 0.50
Nodes (3): i-test-architect — Test architect (planning), Playbook, Testing types owned (priority order)

### Community 2329 - "i-unit-tdd — Unit-level TDD owner (implement)"
Cohesion: 0.50
Nodes (3): i-unit-tdd — Unit-level TDD owner (implement), Playbook, Testing types owned (priority order)

### Community 2330 - "Skill: Code review and impact analysis (Pre-commit)"
Cohesion: 0.50
Nodes (3): Owned testing types, Skill: Code review and impact analysis (Pre-commit), Steps

### Community 2331 - "Skill: Data, AI/LLM and OT/BESS testing (any stage)"
Cohesion: 0.50
Nodes (3): Owned testing types, Skill: Data, AI/LLM and OT/BESS testing (any stage), Steps

### Community 2332 - "Skill: Integration and regression QA (PR/CI)"
Cohesion: 0.50
Nodes (3): Owned testing types, Skill: Integration and regression QA (PR/CI), Steps

### Community 2333 - "Skill: Release gate (Release / post-deploy)"
Cohesion: 0.50
Nodes (3): Owned testing types, Skill: Release gate (Release / post-deploy), Steps

### Community 2334 - "Skill: Security scanning (Pre-commit)"
Cohesion: 0.50
Nodes (3): Owned testing types, Skill: Security scanning (Pre-commit), Steps

### Community 2335 - "Skill: System and non-functional testing (Pre-release)"
Cohesion: 0.50
Nodes (3): Owned testing types, Skill: System and non-functional testing (Pre-release), Steps

### Community 2336 - "Skill: Test architecture (Plan stage)"
Cohesion: 0.50
Nodes (3): Owned testing types, Skill: Test architecture (Plan stage), Steps

### Community 2337 - "Skill: Unit-level TDD (Implement stage)"
Cohesion: 0.50
Nodes (3): Owned testing types, Skill: Unit-level TDD (Implement stage), Steps

### Community 2338 - "Brand Approval Process"
Cohesion: 0.50
Nodes (4): Brand Approval Process, External/Partnership Use, Internal Use, Prohibited Uses

### Community 2339 - "Brand Identity"
Cohesion: 0.50
Nodes (4): Brand Identity, Mission, Values, Vision

### Community 2340 - "🎨 Quick Access"
Cohesion: 0.50
Nodes (4): Brand Color, Documentation, Logo Files, 🎨 Quick Access

### Community 2341 - "claude_repo_setup.sh"
Cohesion: 0.83
Nodes (3): append_ignore_line(), claude_repo_setup.sh script, stage_if_exists()

### Community 2342 - "max_concurrency"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, max_concurrency

### Community 2343 - "max_response_bytes"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, max_response_bytes

### Community 2344 - "per_vendor_per_minute"
Cohesion: 0.50
Nodes (4): maximum, minimum, type, per_vendor_per_minute

### Community 2345 - "i-code-reviewer — Code reviewer and change-impact analyst (pre-commit)"
Cohesion: 0.50
Nodes (3): i-code-reviewer — Code reviewer and change-impact analyst (pre-commit), Playbook, Testing types owned (priority order)

### Community 2346 - "i-data-ai-ot — Data, AI/LLM and OT/BESS tester (any stage)"
Cohesion: 0.50
Nodes (3): i-data-ai-ot — Data, AI/LLM and OT/BESS tester (any stage), Playbook, Testing types owned (priority order)

### Community 2347 - "i-integration-qa — Integration and regression QA (PR/CI)"
Cohesion: 0.50
Nodes (3): i-integration-qa — Integration and regression QA (PR/CI), Playbook, Testing types owned (priority order)

### Community 2348 - "i-release-gate — Release gate and operational readiness (release / post-deploy)"
Cohesion: 0.50
Nodes (3): i-release-gate — Release gate and operational readiness (release / post-deploy), Playbook, Testing types owned (priority order)

### Community 2349 - "i-security-scanner — Security scanner (pre-commit)"
Cohesion: 0.50
Nodes (3): i-security-scanner — Security scanner (pre-commit), Playbook, Testing types owned (priority order)

### Community 2350 - "i-system-nfr — System and non-functional tester (pre-release)"
Cohesion: 0.50
Nodes (3): i-system-nfr — System and non-functional tester (pre-release), Playbook, Testing types owned (priority order)

### Community 2351 - "i-test-architect — Test architect (planning)"
Cohesion: 0.50
Nodes (3): i-test-architect — Test architect (planning), Playbook, Testing types owned (priority order)

### Community 2352 - "i-unit-tdd — Unit-level TDD owner (implement)"
Cohesion: 0.50
Nodes (3): i-unit-tdd — Unit-level TDD owner (implement), Playbook, Testing types owned (priority order)

### Community 2353 - "hermes/manifest.json"
Cohesion: 0.50
Nodes (3): entries, generated_at, version

### Community 2354 - "graphify reference: commit hook and native CLAUDE.md integration"
Cohesion: 0.50
Nodes (3): For git commit hook, For native CLAUDE.md integration, graphify reference: commit hook and native CLAUDE.md integration

### Community 2355 - "openclaw/manifest.json"
Cohesion: 0.50
Nodes (3): entries, generated_at, version

### Community 2356 - "context.md"
Cohesion: 0.50
Nodes (3): Active Projects, Key Facts, Pending Tasks

### Community 2359 - "health-check.sh"
Cohesion: 0.83
Nodes (3): check_fail(), check_pass(), health-check.sh script

### Community 2360 - "init-openclaw-config.sh"
Cohesion: 0.83
Nodes (3): _oc_config_set(), init-openclaw-config.sh script, _sha256()

### Community 2361 - "killswitch.sh"
Cohesion: 0.83
Nodes (3): confirm(), killswitch.sh script, usage()

### Community 2362 - "security-entrypoint.sh"
Cohesion: 1.00
Nodes (3): alert_critical(), log(), security-entrypoint.sh script

### Community 2363 - "test-get-credential.sh"
Cohesion: 0.83
Nodes (3): fail(), pass(), test-get-credential.sh script

### Community 2364 - "test-op-auth.sh"
Cohesion: 0.83
Nodes (3): fail(), pass(), test-op-auth.sh script

### Community 2365 - "Priority 3: User Experience Improvements"
Cohesion: 0.50
Nodes (4): 3.1 One-Click Setup Wizard (Web-Based), 3.2 Mobile App (iOS/Android), 3.3 Desktop App (Electron), Priority 3: User Experience Improvements

### Community 2366 - "Priority 4: Advanced Agent Capabilities"
Cohesion: 0.50
Nodes (4): 4.1 Multi-Agent Orchestration, 4.2 Scheduled Actions & Automation, 4.3 Voice Interface, Priority 4: Advanced Agent Capabilities

### Community 2367 - "Data Documentation"
Cohesion: 0.50
Nodes (3): Current Status, Data Documentation, Planned Documents

### Community 2368 - "Flows Documentation"
Cohesion: 0.50
Nodes (3): Current Status, Flows Documentation, Planned Documents

### Community 2369 - "Integrations Documentation"
Cohesion: 0.50
Nodes (3): Current Status, Integrations Documentation, Planned Documents

### Community 2370 - "Post-fable-5 Task Delegation"
Cohesion: 0.50
Nodes (3): Notes, Post-fable-5 Task Delegation, Task list

### Community 2371 - "Project Documentation"
Cohesion: 0.50
Nodes (3): Current Status, Planned Documents, Project Documentation

### Community 2372 - "Requirements Documentation"
Cohesion: 0.50
Nodes (3): Current Status, Planned Documents, Requirements Documentation

### Community 2373 - "Competitive Analysis Reports Archive"
Cohesion: 0.50
Nodes (3): Competitive Analysis Reports Archive, Default Selection Notes, Reports

### Community 2374 - "Step 5: Configure Ports"
Cohesion: 0.50
Nodes (4): Auto-Detection, Default Configuration, Multi-Instance Setup, Step 5: Configure Ports

### Community 2375 - "Step 2: Choose Your Container Runtime"
Cohesion: 0.50
Nodes (4): Option A: Docker (Most Common), Option B: Podman (Red Hat/Enterprise), Option C: Apple Containers (macOS 26+), Step 2: Choose Your Container Runtime

### Community 2376 - "Prerequisites"
Cohesion: 0.50
Nodes (4): Optional Requirements, Prerequisites, Supported Platforms, System Requirements

### Community 2377 - "Testing Documentation"
Cohesion: 0.50
Nodes (3): Current Status, Planned Documents, Testing Documentation

### Community 2381 - ".test_mcp_proxy_endpoint"
Cohesion: 0.50
Nodes (3): Test /mcp/proxy endpoint., Test MCP proxy endpoint basic functionality., TestMCPProxyEndpoint

### Community 2395 - "BufferHandler"
Cohesion: 0.50
Nodes (3): BufferHandler, LogRecord, Logging handler that pushes records into the LogBuffer.

### Community 2396 - "i-code-reviewer — Code reviewer and change-impact analyst (pre-commit)"
Cohesion: 0.50
Nodes (3): i-code-reviewer — Code reviewer and change-impact analyst (pre-commit), Playbook, Testing types owned (priority order)

### Community 2397 - "i-data-ai-ot — Data, AI/LLM and OT/BESS tester (any stage)"
Cohesion: 0.50
Nodes (3): i-data-ai-ot — Data, AI/LLM and OT/BESS tester (any stage), Playbook, Testing types owned (priority order)

### Community 2398 - "i-integration-qa — Integration and regression QA (PR/CI)"
Cohesion: 0.50
Nodes (3): i-integration-qa — Integration and regression QA (PR/CI), Playbook, Testing types owned (priority order)

### Community 2399 - "i-release-gate — Release gate and operational readiness (release / post-deploy)"
Cohesion: 0.50
Nodes (3): i-release-gate — Release gate and operational readiness (release / post-deploy), Playbook, Testing types owned (priority order)

### Community 2400 - "i-security-scanner — Security scanner (pre-commit)"
Cohesion: 0.50
Nodes (3): i-security-scanner — Security scanner (pre-commit), Playbook, Testing types owned (priority order)

### Community 2401 - "i-system-nfr — System and non-functional tester (pre-release)"
Cohesion: 0.50
Nodes (3): i-system-nfr — System and non-functional tester (pre-release), Playbook, Testing types owned (priority order)

### Community 2402 - "i-test-architect — Test architect (planning)"
Cohesion: 0.50
Nodes (3): i-test-architect — Test architect (planning), Playbook, Testing types owned (priority order)

### Community 2403 - "i-unit-tdd — Unit-level TDD owner (implement)"
Cohesion: 0.50
Nodes (3): i-unit-tdd — Unit-level TDD owner (implement), Playbook, Testing types owned (priority order)

### Community 2404 - "git-hooks/install.sh"
Cohesion: 0.83
Nodes (3): backup_path(), hook_is_pre_commit(), install.sh script

### Community 2405 - "i-code-reviewer — Code reviewer and change-impact analyst (pre-commit)"
Cohesion: 0.50
Nodes (3): i-code-reviewer — Code reviewer and change-impact analyst (pre-commit), Playbook, Testing types owned (priority order)

### Community 2406 - "[Unreleased] — feat/v0.8.0-enforcement-hardening (session 2 — 2026-03-14)"
Cohesion: 0.33
Nodes (6): Added, Changed, Fixed, Summary, Tests, [Unreleased] — feat/v0.8.0-enforcement-hardening (session 2 — 2026-03-14)

### Community 2407 - "i-data-ai-ot — Data, AI/LLM and OT/BESS tester (any stage)"
Cohesion: 0.50
Nodes (3): i-data-ai-ot — Data, AI/LLM and OT/BESS tester (any stage), Playbook, Testing types owned (priority order)

### Community 2408 - "i-integration-qa — Integration and regression QA (PR/CI)"
Cohesion: 0.50
Nodes (3): i-integration-qa — Integration and regression QA (PR/CI), Playbook, Testing types owned (priority order)

### Community 2409 - "[1.5.2] (2026-08-23)"
Cohesion: 0.40
Nodes (5): [1.5.2] (2026-08-23), Added, Fixed, Known gaps (not yet closed), Summary

### Community 2410 - "i-release-gate — Release gate and operational readiness (release / post-deploy)"
Cohesion: 0.50
Nodes (3): i-release-gate — Release gate and operational readiness (release / post-deploy), Playbook, Testing types owned (priority order)

### Community 2411 - "i-security-scanner — Security scanner (pre-commit)"
Cohesion: 0.50
Nodes (3): i-security-scanner — Security scanner (pre-commit), Playbook, Testing types owned (priority order)

### Community 2412 - "i-system-nfr — System and non-functional tester (pre-release)"
Cohesion: 0.50
Nodes (3): i-system-nfr — System and non-functional tester (pre-release), Playbook, Testing types owned (priority order)

### Community 2413 - "i-test-architect — Test architect (planning)"
Cohesion: 0.50
Nodes (3): i-test-architect — Test architect (planning), Playbook, Testing types owned (priority order)

### Community 2414 - "i-unit-tdd — Unit-level TDD owner (implement)"
Cohesion: 0.50
Nodes (3): i-unit-tdd — Unit-level TDD owner (implement), Playbook, Testing types owned (priority order)

### Community 2415 - "i-code-reviewer — Code reviewer and change-impact analyst (pre-commit)"
Cohesion: 0.50
Nodes (3): i-code-reviewer — Code reviewer and change-impact analyst (pre-commit), Playbook, Testing types owned (priority order)

### Community 2416 - "i-data-ai-ot — Data, AI/LLM and OT/BESS tester (any stage)"
Cohesion: 0.50
Nodes (3): i-data-ai-ot — Data, AI/LLM and OT/BESS tester (any stage), Playbook, Testing types owned (priority order)

### Community 2417 - "i-integration-qa — Integration and regression QA (PR/CI)"
Cohesion: 0.50
Nodes (3): i-integration-qa — Integration and regression QA (PR/CI), Playbook, Testing types owned (priority order)

### Community 2418 - "i-release-gate — Release gate and operational readiness (release / post-deploy)"
Cohesion: 0.50
Nodes (3): i-release-gate — Release gate and operational readiness (release / post-deploy), Playbook, Testing types owned (priority order)

### Community 2419 - "i-security-scanner — Security scanner (pre-commit)"
Cohesion: 0.50
Nodes (3): i-security-scanner — Security scanner (pre-commit), Playbook, Testing types owned (priority order)

### Community 2420 - "i-system-nfr — System and non-functional tester (pre-release)"
Cohesion: 0.50
Nodes (3): i-system-nfr — System and non-functional tester (pre-release), Playbook, Testing types owned (priority order)

### Community 2421 - "i-test-architect — Test architect (planning)"
Cohesion: 0.50
Nodes (3): i-test-architect — Test architect (planning), Playbook, Testing types owned (priority order)

### Community 2422 - "i-unit-tdd — Unit-level TDD owner (implement)"
Cohesion: 0.50
Nodes (3): i-unit-tdd — Unit-level TDD owner (implement), Playbook, Testing types owned (priority order)

### Community 2423 - "1. The Problem: Unsecured AI Agents"
Cohesion: 0.50
Nodes (4): 1.1 The New Attack Surface, 1.2 The Industry Gap, 1.3 Threat Model, 1. The Problem: Unsecured AI Agents

### Community 2424 - "6. Competitive Landscape"
Cohesion: 0.50
Nodes (4): 6.1 Market Overview, 6.2 Comparison Table, 6.3 Key Differentiators, 6. Competitive Landscape

### Community 2425 - "Summary"
Cohesion: 0.50
Nodes (4): Key Changes (2026-03-04 12:16 UTC), Key Changes (2026-03-20), Key Changes (2026-04-08), Summary

### Community 2427 - "Authentication and Authorization Framework"
Cohesion: 0.50
Nodes (4): API Key Security, Approval Queue Workflow, Authentication and Authorization Framework, Trust Level Progression

### Community 2428 - "Obsidian"
Cohesion: 0.50
Nodes (3): Find the active vault(s), Obsidian, obsidian-cli quick start

### Community 2429 - "find-sessions.sh"
Cohesion: 0.83
Nodes (3): list_sessions(), find-sessions.sh script, usage()

### Community 2430 - "Video Frames (ffmpeg)"
Cohesion: 0.50
Nodes (3): Notes, Quick start, Video Frames (ffmpeg)

### Community 2431 - "Voice Call"
Cohesion: 0.50
Nodes (3): CLI, Tool, Voice Call

### Community 2432 - "Type Scale"
Cohesion: 0.50
Nodes (4): Body Text, Code/Monospace, Headings, Type Scale

### Community 2433 - "Platform-Specific"
Cohesion: 0.50
Nodes (4): Mobile, Platform-Specific, Print, Web

### Community 2434 - "DELIVERABLE 4 — v1.0 Roadmap"
Cohesion: 0.50
Nodes (4): DELIVERABLE 4 — v1.0 Roadmap, Phase 1: Foundation Hardening (v0.8.0, completed), Phase 2: Detection Enhancement (v0.9.3–v0.9.5, Weeks 5-10), Phase 3: Operational Maturity (v0.9.6–v1.0.0, Weeks 11-16)

### Community 2435 - "1) REPOSITORY OVERVIEW"
Cohesion: 0.67
Nodes (3): 1) REPOSITORY OVERVIEW, Primary Focus, Supporting Integrations

### Community 2436 - "4) LANGUAGE & TOOLING STANDARDS"
Cohesion: 0.67
Nodes (3): 4) LANGUAGE & TOOLING STANDARDS, Next.js / UI Standards, Python Standards

### Community 2437 - "8) CODEX CLI CONFIGURATION"
Cohesion: 0.67
Nodes (3): 8) CODEX CLI CONFIGURATION, What You Don't Have, What You Have

### Community 2438 - "Color Usage"
Cohesion: 0.67
Nodes (3): Accessibility, Color Usage, Primary Color Application

### Community 2439 - "Typography in Practice"
Cohesion: 0.67
Nodes (3): Hierarchy, Readability, Typography in Practice

### Community 2444 - "AgentShroud Falco Rules"
Cohesion: 0.67
Nodes (3): Falco Configuration, AgentShroud Falco Rules, Falco Rule: Unexpected Outbound Connection

### Community 2472 - "BotConfig"
Cohesion: 0.08
Nodes (24): BotConfig, BaseModel, Declaration for a single bot encapsulated by AgentShroud. Required bot HTTP…, The real docker container name for this bot — see container_name field., _build_telegram_token_registry(), Build the Telegram bot-token → bot_id registry from configured secrets., Proxy Telegram Bot API calls through security pipeline., telegram_api_proxy() (+16 more)

### Community 2474 - "test_webhook_receiver_passes_agent_id_as_bot_id"
Cohesion: 0.67
Nodes (3): asyncio, process_webhook passes agent_id as bot_id to record_activity., test_webhook_receiver_passes_agent_id_as_bot_id()

### Community 2475 - "mgr"
Cohesion: 0.67
Nodes (3): mgr(), fixture, In-memory delegation manager (no disk I/O).

## Ambiguous Edges - Review These
- `gen-code-graph.sh` → `Obsidian code-architecture vault (.obsidian-vaults/code-architecture)`  [AMBIGUOUS]
  scripts/gen-code-graph.sh · relation: references
- `op-to-keychain.sh` → `Sunday Upgrade Report 2026-08-30 (local-llms upgrade requested)`  [AMBIGUOUS]
  reports/upgrade-2026-08-30-20260830-2010.md · relation: conceptually_related_to
- `branding/README.md` → `AgentShroud Merchandise/Stationery Mockup`  [AMBIGUOUS]
  branding/README.md · relation: references
- `gateway/README.md` → `Dependency Graph.md`  [AMBIGUOUS]
  gateway/README.md · relation: conceptually_related_to
- `CLAUDE.md` → `Stale Repository-Context Description in COPILOT_CLI_SETUP.md`  [AMBIGUOUS]
  .github/COPILOT_CLI_SETUP.md · relation: conceptually_related_to
- `raspberry-pi.md` → `Disaster Recovery Full Rebuild Procedure`  [AMBIGUOUS]
  docs/runbooks/backup-restore.md · relation: references
- `SECURITY-IMPLEMENTATION-VERIFICATION.md` → `SECURITY_VERIFICATION.md`  [AMBIGUOUS]
  docs/security/SECURITY-IMPLEMENTATION-VERIFICATION.md · relation: conceptually_related_to
- `AgentShroud Security Architecture` → `NFKC Normalization`  [AMBIGUOUS]
  docs/security/security-architecture.md · relation: conceptually_related_to
- `SecurityPipeline (75 modules, 7 layers)` → `ADR-002: Default-Allow with Comprehensive Logging`  [AMBIGUOUS]
  docs/architecture/adr/ADR-002-default-allow-security-philosophy.md · relation: conceptually_related_to
- `browse.py — SecureBrowser CLI (OpenClaw)` → `browser-fetch package.json`  [AMBIGUOUS]
  docker/config/openclaw/skills/i-browser/package.json · relation: semantically_similar_to
- `8D Root Cause Analysis SKILL (OpenClaw)` → `Code Review (CR) SKILL (OpenClaw)`  [AMBIGUOUS]
  docker/config/openclaw/skills/i-eightd/SKILL.md · relation: semantically_similar_to
- `AgentShroud Config with Tool Risk Tiers (example)` → `PII confidence 0.8 (example) vs 0.9 floor (CLAUDE.md §7) discrepancy`  [AMBIGUOUS]
  examples/agentshroud-with-tool-risk.yaml · relation: rationale_for
- `i-hermes README (Podcast Production Orchestrator)` → `Hermes — Reference Verifier Skill`  [AMBIGUOUS]
  docker/config/openclaw/skills/i-hermes/README.md · relation: references
- `Scrum Ceremony Facilitation` → `SDLC Governance`  [AMBIGUOUS]
  .agents/skills/i-scrum/SKILL.md · relation: conceptually_related_to
- `DM Policy Allowlist Configuration` → `Runbook / Decision Tree — On-Call Logic`  [AMBIGUOUS]
  docs/diagrams/06-operations.md · relation: conceptually_related_to
- `GSDE&G Skills Reference Guide` → `i-session-prompt SKILL (Session Prompt Generator)`  [AMBIGUOUS]
  docker/config/hermes/skills/i-session-prompt/SKILL.md · relation: conceptually_related_to
- `i-sec-defense SKILL (Blue Team Security Auditor, AgentShroud)` → `i-sec SKILL (Security Review / SEC, SecureClaw)`  [AMBIGUOUS]
  docker/config/hermes/skills/i-sec/SKILL.md · relation: semantically_similar_to
- `1Password Desktop App Integration Flow` → `Currently Unmitigable Residual Class`  [AMBIGUOUS]
  skills/openclaw/1password/references/get-started.md · relation: conceptually_related_to
- `Gateway Management/Control-Plane API (v1.3.0)` → `OpenClaw Integration Guide (v0.9.0)`  [AMBIGUOUS]
  docs/api/integration-guide.md · relation: conceptually_related_to

## Knowledge Gaps
- **13727 isolated node(s):** `{ chromium }`, `fs`, `path`, `name`, `version` (+13722 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 24102 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **975 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `gen-code-graph.sh` and `Obsidian code-architecture vault (.obsidian-vaults/code-architecture)`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `op-to-keychain.sh` and `Sunday Upgrade Report 2026-08-30 (local-llms upgrade requested)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `branding/README.md` and `AgentShroud Merchandise/Stationery Mockup`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `gateway/README.md` and `Dependency Graph.md`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `CLAUDE.md` and `Stale Repository-Context Description in COPILOT_CLI_SETUP.md`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `raspberry-pi.md` and `Disaster Recovery Full Rebuild Procedure`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `SECURITY-IMPLEMENTATION-VERIFICATION.md` and `SECURITY_VERIFICATION.md`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
