#!/usr/bin/env python3
"""
Fix generic agent descriptions in template agent files.

Replaces "Execute specialized tasks within the AI engineering OS" with specific
responsibilities derived from the agent name.
"""

import re
from pathlib import Path
from typing import Dict

# Agent name to responsibilities mapping
AGENT_RESPONSIBILITIES: Dict[str, list[str]] = {
    "ai-training-agent": [
        "Design and implement AI model training pipelines",
        "Optimize hyperparameters and model architecture",
        "Monitor training metrics and convergence",
        "Implement data augmentation strategies"
    ],
    "analytics-agent": [
        "Analyze system metrics and operational data",
        "Generate reports and visualizations",
        "Identify trends and anomalies",
        "Provide data-driven recommendations"
    ],
    "architecture-agent": [
        "Design system architecture and component interactions",
        "Evaluate architectural trade-offs",
        "Document architectural decisions (ADRs)",
        "Ensure scalability and maintainability"
    ],
    "backlog-agent": [
        "Prioritize and organize product backlog items",
        "Estimate effort and complexity",
        "Break down epics into user stories",
        "Maintain backlog refinement"
    ],
    "bluegreen-release-agent": [
        "Implement blue-green deployment strategies",
        "Manage traffic routing between environments",
        "Validate new releases before cutover",
        "Execute rollback procedures if needed"
    ],
    "canary-release-agent": [
        "Implement canary deployment strategies",
        "Monitor canary release metrics",
        "Gradually increase traffic to new version",
        "Execute automated rollback on failure"
    ],
    "chaos-engineering-agent": [
        "Design and execute chaos experiments",
        "Test system resilience and fault tolerance",
        "Inject controlled failures (network, latency, resources)",
        "Document failure scenarios and recovery procedures"
    ],
    "ci-agent": [
        "Configure and maintain CI/CD pipelines",
        "Optimize build and test execution",
        "Integrate quality gates (tests, linting, security scans)",
        "Debug pipeline failures"
    ],
    "code-reviewer": [
        "Review code changes for quality and correctness",
        "Check for security vulnerabilities and anti-patterns",
        "Ensure adherence to coding standards",
        "Provide actionable feedback on pull requests"
    ],
    "compliance-agent": [
        "Verify compliance with regulatory requirements (ITIL, ISO, SOC2)",
        "Audit configurations and access controls",
        "Generate compliance reports",
        "Track remediation of compliance violations"
    ],
    "data-engineer": [
        "Design and implement data pipelines",
        "Optimize data transformations and ETL processes",
        "Ensure schema consistency and data quality",
        "Manage data partitioning and storage"
    ],
    "database-agent": [
        "Design database schemas and indexes",
        "Optimize query performance",
        "Manage database migrations",
        "Monitor database health and capacity"
    ],
    "debugging-agent": [
        "Diagnose and isolate bugs",
        "Analyze stack traces and error logs",
        "Reproduce issues with minimal test cases",
        "Suggest root cause and fixes"
    ],
    "dependency-agent": [
        "Manage project dependencies and versions",
        "Check for security vulnerabilities in dependencies",
        "Update dependencies and test for compatibility",
        "Resolve dependency conflicts"
    ],
    "deploy-agent": [
        "Execute deployment procedures",
        "Validate pre-deployment checklist",
        "Monitor deployment health",
        "Execute rollback if deployment fails"
    ],
    "devsecops-agent": [
        "Integrate security into CI/CD pipelines",
        "Automate security scanning (SAST, DAST, dependency checks)",
        "Manage secrets and credentials securely",
        "Implement least-privilege access controls"
    ],
    "diagnostics-agent": [
        "Diagnose system and application issues",
        "Collect and analyze logs, metrics, and traces",
        "Identify root causes of failures",
        "Suggest remediation steps"
    ],
    "documentation-agent": [
        "Write clear, concise technical documentation",
        "Generate API documentation from code",
        "Maintain runbooks and troubleshooting guides",
        "Ensure documentation stays current with code changes"
    ],
    "feature-flag-agent": [
        "Manage feature flags and toggles",
        "Implement gradual feature rollouts",
        "A/B test feature variations",
        "Remove obsolete feature flags"
    ],
    "incident-commander": [
        "Coordinate incident response efforts",
        "Triage and prioritize incidents",
        "Facilitate communication between teams",
        "Document incident timeline and post-mortem"
    ],
    "infrastructure-agent": [
        "Provision and manage cloud infrastructure",
        "Implement infrastructure as code (Terraform, CloudFormation)",
        "Optimize resource utilization and cost",
        "Ensure high availability and disaster recovery"
    ],
    "integration-testing-agent": [
        "Design and execute integration tests",
        "Test API contracts and service interactions",
        "Validate end-to-end workflows",
        "Identify integration points and failure modes"
    ],
    "knowledge-engineer": [
        "Build and maintain knowledge bases",
        "Extract knowledge from documentation and code",
        "Create structured ontologies and taxonomies",
        "Facilitate knowledge sharing"
    ],
    "load-testing-agent": [
        "Design and execute load tests",
        "Simulate realistic traffic patterns",
        "Identify performance bottlenecks",
        "Generate performance reports and recommendations"
    ],
    "log-analysis-agent": [
        "Aggregate and parse logs from multiple sources",
        "Identify patterns and anomalies in logs",
        "Correlate logs with incidents",
        "Generate log-based alerts"
    ],
    "monitoring-agent": [
        "Configure monitoring dashboards and alerts",
        "Track key metrics (SLIs, SLOs, SLAs)",
        "Detect anomalies and degraded performance",
        "Integrate with incident management systems"
    ],
    "observability-agent": [
        "Implement observability across services (logs, metrics, traces)",
        "Correlate signals for root cause analysis",
        "Design distributed tracing strategies",
        "Optimize observability costs"
    ],
    "onboarding-agent": [
        "Guide new team members through onboarding",
        "Provide codebase tours and architecture overviews",
        "Assign starter tasks and pair programming sessions",
        "Track onboarding progress"
    ],
    "performance-agent": [
        "Profile and optimize application performance",
        "Identify CPU, memory, and I/O bottlenecks",
        "Implement caching and lazy loading strategies",
        "Benchmark before and after optimizations"
    ],
    "pm": [
        "Manage project scope, timeline, and resources",
        "Facilitate sprint planning and retrospectives",
        "Track progress and remove blockers",
        "Communicate status to stakeholders"
    ],
    "quality-assurance-agent": [
        "Design and execute test plans",
        "Automate regression testing",
        "Verify bug fixes and new features",
        "Track quality metrics and defect trends"
    ],
    "refactoring-agent": [
        "Identify code smells and technical debt",
        "Propose safe refactoring strategies",
        "Ensure tests pass before and after refactoring",
        "Improve code readability and maintainability"
    ],
    "release-notes-agent": [
        "Generate release notes from commits and PRs",
        "Categorize changes (features, fixes, breaking changes)",
        "Write user-facing change descriptions",
        "Format for different audiences (developers, operators, customers)"
    ],
    "rollback-agent": [
        "Execute rollback procedures",
        "Restore previous known-good state",
        "Validate rollback success",
        "Document rollback reasons and lessons learned"
    ],
    "scaling-agent": [
        "Implement horizontal and vertical scaling strategies",
        "Configure auto-scaling policies",
        "Monitor scaling events and resource utilization",
        "Optimize for cost and performance"
    ],
    "security-auditor": [
        "Audit systems for security vulnerabilities",
        "Verify security controls are in place",
        "Test for common vulnerabilities (OWASP Top 10)",
        "Generate security audit reports"
    ],
    "smoke-testing-agent": [
        "Execute smoke tests after deployments",
        "Verify critical paths work end-to-end",
        "Quickly detect major regressions",
        "Trigger alerts if smoke tests fail"
    ],
    "sre-agent": [
        "Ensure service reliability and availability",
        "Implement SRE best practices (SLOs, error budgets, toil reduction)",
        "Automate operational tasks",
        "Conduct post-incident reviews"
    ],
    "test-data-generator": [
        "Generate realistic test data",
        "Anonymize production data for testing",
        "Create fixtures and mock responses",
        "Validate test data quality"
    ],
    "troubleshooting-agent": [
        "Diagnose and resolve operational issues",
        "Analyze symptoms and hypothesize causes",
        "Execute troubleshooting runbooks",
        "Escalate when necessary"
    ],
    "ui-testing-agent": [
        "Automate UI testing (Selenium, Playwright, Cypress)",
        "Test cross-browser compatibility",
        "Validate accessibility (WCAG compliance)",
        "Capture screenshots and videos of failures"
    ],
    "version-control-agent": [
        "Manage branching and merging strategies",
        "Review and enforce commit message conventions",
        "Resolve merge conflicts",
        "Maintain clean Git history"
    ],
}


def derive_responsibilities(agent_name: str) -> list[str]:
    """Derive responsibilities from agent name if not in mapping."""
    # Check exact match
    if agent_name in AGENT_RESPONSIBILITIES:
        return AGENT_RESPONSIBILITIES[agent_name]

    # Derive generic responsibilities based on name patterns
    name_clean = agent_name.replace("-", " ").replace("_", " ")
    return [
        f"Perform {name_clean}-specific tasks",
        f"Support {name_clean} workflows",
        f"Provide expertise in {name_clean} domain"
    ]


def fix_agent_file(file_path: Path) -> bool:
    """Fix a single agent file. Returns True if modified."""
    content = file_path.read_text()

    # Check if file needs fixing
    if "Execute specialized tasks within the AI engineering OS" not in content:
        return False

    # Extract agent name from filename
    agent_name = file_path.stem

    # Get responsibilities
    responsibilities = derive_responsibilities(agent_name)

    # Format new responsibilities
    resp_text = "\n".join(f"- {r}" for r in responsibilities)

    # Replace generic text with specific responsibilities
    new_content = content.replace(
        "- Execute specialized tasks within the AI engineering OS.",
        resp_text
    )

    # Write back
    file_path.write_text(new_content)
    print(f"✓ Fixed {file_path}")
    return True


def main():
    """Fix all agent files in mcp-servers/github subdirectories and main .llm_settings/agents."""
    agent_dirs = [
        Path(".llm_settings/mcp-servers/github/.codex/agents"),
        Path(".llm_settings/mcp-servers/github/.gemini/agents"),
        Path(".llm_settings/mcp-servers/github/.claude/agents"),
        Path(".llm_settings/agents"),
    ]

    total_fixed = 0
    for agent_dir in agent_dirs:
        if not agent_dir.exists():
            print(f"⚠ Skipping {agent_dir} (not found)")
            continue

        for agent_file in sorted(agent_dir.glob("*.md")):
            if fix_agent_file(agent_file):
                total_fixed += 1

    print(f"\n✅ Fixed {total_fixed} agent files")


if __name__ == "__main__":
    main()
