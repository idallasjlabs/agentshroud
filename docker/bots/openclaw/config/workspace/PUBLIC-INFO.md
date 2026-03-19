# AgentShroud — Collaborator Knowledge Base

## What is AgentShroud?

AgentShroud is a security gateway that wraps autonomous AI agents (Claude Code and
similar tools) running on the owner's personal infrastructure. It intercepts all
traffic between the AI agent and its communication channels, applying multi-layer
security controls before any message reaches the agent or leaves it.

## What Does It Do?

AgentShroud provides:

- **Inbound security**: Scans messages from users for prompt injection attempts
  before they reach the AI agent
- **Outbound filtering**: Reviews agent responses for sensitive information before
  delivery to users
- **Collaborator isolation**: Collaborators interact with a restricted agent profile
  that has read-only access and no access to privileged tools
- **Audit trail**: All interactions are logged for review

## Who Can Use It?

- **Owner (Isaiah)**: Full access to all tools, credentials, and capabilities
- **Collaborators**: Read-only advisory access — can discuss projects, review
  documents, and get technical advice

## Collaboration Guidelines

As a collaborator, you can:
- Ask questions about software engineering, security, and technical topics
- Request code review or analysis of files in the shared workspace
- Discuss AgentShroud's public features and design philosophy

As a collaborator, you cannot:
- Access owner credentials, secrets, or 1Password
- Execute system commands or scripts
- Access the internet directly
- Modify files outside the shared workspace
- Access agent memory, session history, or owner conversations

## Project Goals

AgentShroud's primary goal is to allow autonomous AI agents to be safely shared
with collaborators while protecting the owner's infrastructure, credentials, and
operational data. It is designed for production use with multiple trusted collaborators.

## Contact

For questions about access, capabilities, or the project itself, contact Isaiah directly.
