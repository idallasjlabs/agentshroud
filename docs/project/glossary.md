# Glossary
## AgentShroud Project Terminology

### A

**AI Agent**  
An artificial intelligence system that autonomously performs tasks, makes decisions, and interacts with external systems on behalf of users. In the context of AgentShroud, these are the systems being protected by the security proxy layer.

**Approval Queue**  
A security control mechanism that requires human authorization before executing high-risk operations. Requests are queued for review by security operators with configurable timeouts and escalation procedures.

**Audit Trail**  
A chronological record of system activities, security events, and user actions maintained for compliance, forensic analysis, and security monitoring. AgentShroud implements tamper-evident audit trails using cryptographic hash chains.

### B

**Behavioral Pattern Analysis**  
The process of analyzing AI agent actions over time to identify anomalous or potentially malicious behavior patterns. Used by the trust management system to adjust agent trust scores.

### C

**Container Runtime**  
Software that executes and manages containers. AgentShroud supports Docker, Podman, and Apple Containers for cross-platform deployment flexibility.

**CVE-2026-22708**  
A theoretical vulnerability identifier representing prompt injection attacks that bypass traditional input validation. AgentShroud's prompt injection defense specifically addresses this class of vulnerabilities.

**CVE-2026-25253**  
A theoretical vulnerability identifier for DNS tunneling attacks used to exfiltrate data through DNS queries. AgentShroud's DNS filtering module detects and blocks these attacks.

### D

**Defense-in-Depth**  
A security strategy that employs multiple layers of security controls to protect against various attack vectors. AgentShroud implements this through 26 integrated security modules working in concert.

**DNS Filtering**  
Security control that monitors and filters Domain Name System queries to block access to malicious domains, detect DNS tunneling attempts, and prevent data exfiltration through DNS channels.

**DNS Tunneling**  
A technique where data is encoded and transmitted through DNS queries and responses, often used to bypass network security controls or exfiltrate sensitive information.

### E

**Egress Filter**  
Network security control that monitors and restricts outbound network traffic from AI agents to prevent data exfiltration, unauthorized communications, and access to restricted resources.

**Enforce Mode**  
Operational mode where AgentShroud actively blocks violations and enforces security policies. Contrasts with Monitor Mode where violations are logged but not blocked.

### F

**False Positive**  
A security alert or detection that incorrectly identifies legitimate activity as malicious. AgentShroud includes mechanisms to tune detection algorithms and reduce false positive rates.

### H

**Hash Chain**  
Cryptographic technique where each audit log entry includes the hash of the previous entry, creating an immutable chain that detects tampering. If any entry is modified, the chain breaks and tamper evidence is preserved.

### I

**Injection Attack**  
Security attack where malicious code or commands are inserted into application inputs to manipulate system behavior. AgentShroud defends against various injection types including prompt injection and SQL injection.

### K

**Kill Switch**  
Emergency control mechanism that immediately terminates all or specific AI agent operations when security threats are detected or during emergency situations. Provides rapid threat containment.

### M

**MCP (Model Context Protocol)**  
A protocol that enables AI agents to interact with external tools and services in a structured manner. AgentShroud provides secure proxy functionality for MCP communications with permission validation and audit logging.

**Monitor Mode**  
Operational mode where AgentShroud observes and logs security events without blocking them. Used for baseline establishment, testing, and gradual deployment scenarios.

### N

**NFKC Normalization**  
Unicode normalization form that converts text to a canonical representation. AgentShroud uses NFKC normalization to prevent bypass attempts using Unicode variations of malicious patterns.

### O

**OpenClaw**  
The primary AI agent platform that AgentShroud is designed to protect. OpenClaw provides the core AI agent runtime and tool ecosystem that AgentShroud secures through proxy functionality.

### P

**PII (Personally Identifiable Information)**  
Any information that can be used to identify, contact, or locate a specific individual. AgentShroud automatically detects and sanitizes PII in communications to prevent privacy violations and compliance issues.

**Prompt Injection**  
Attack technique where malicious instructions are embedded in user inputs to manipulate AI agent behavior, potentially causing the agent to ignore safety instructions or perform unauthorized actions.

**Proxy Mode**  
Operational configuration where AgentShroud sits between clients and AI agents, intercepting and securing all communications. Enables transparent security without requiring agent modifications.

### R

**Redaction**  
The process of removing or obscuring sensitive information from data while preserving the overall structure and meaning. AgentShroud redacts PII while maintaining message coherence for AI processing.

### S

**AgentShroud**  
The comprehensive security proxy layer designed to protect AI agents from various security threats through 26 integrated security modules, providing defense-in-depth protection with comprehensive audit capabilities.

**Sidecar Mode**  
Deployment pattern where AgentShroud runs alongside AI agents as a companion service, providing security services without requiring direct integration into the agent codebase.

**SSRF (Server-Side Request Forgery)**  
Attack where an attacker causes a server to make unauthorized requests to internal or external systems. AgentShroud's web proxy prevents SSRF attacks through URL validation and request filtering.

### T

**Threat Intelligence**  
Information about current and potential security threats, including malicious domains, IP addresses, and attack patterns. AgentShroud integrates threat intelligence feeds to enhance detection capabilities.

**Trust Level**  
Numerical score (typically 0-10) representing the trustworthiness of an AI agent based on behavior patterns, validation history, and security assessments. Higher trust levels receive fewer restrictions.

**Trust Management**  
System for calculating, maintaining, and applying trust scores to AI agents. Trust levels influence security policy enforcement, with lower trust agents receiving stricter controls.

### U

**Unicode Bypass**  
Attack technique using Unicode characters that appear similar to ASCII characters to bypass text-based security filters. AgentShroud prevents this through NFKC normalization and comprehensive pattern matching.

### V

**Vulnerability Assessment**  
Systematic evaluation of security weaknesses in systems and applications. AgentShroud undergoes regular vulnerability assessments and implements controls to address identified risks.

### W

**Webhook**  
HTTP callback mechanism that allows AgentShroud to send real-time notifications to external monitoring and alerting systems when security events occur.

### Z

**Zero-Config Deployment**  
Installation and deployment approach requiring minimal or no manual configuration. AgentShroud provides zero-config deployment with secure defaults and automatic service discovery.

**Zero-Trust Architecture**  
Security model that assumes no implicit trust and continuously validates every access request regardless of the user's location or previous authentication. AgentShroud implements zero-trust principles for AI agent security.

---

## Technical Abbreviations

**API** - Application Programming Interface  
**CI/CD** - Continuous Integration/Continuous Deployment  
**CPU** - Central Processing Unit  
**DAST** - Dynamic Application Security Testing  
**DNS** - Domain Name System  
**DoH** - DNS over HTTPS  
**HTTP/HTTPS** - HyperText Transfer Protocol (Secure)  
**IP** - Internet Protocol  
**IPv4/IPv6** - Internet Protocol version 4/6  
**JSON** - JavaScript Object Notation  
**JWT** - JSON Web Token  
**ML** - Machine Learning  
**NIST** - National Institute of Standards and Technology  
**OWASP** - Open Web Application Security Project  
**PII** - Personally Identifiable Information  
**RAM** - Random Access Memory  
**RBAC** - Role-Based Access Control  
**REST** - Representational State Transfer  
**SAST** - Static Application Security Testing  
**SQL** - Structured Query Language  
**SSH** - Secure Shell  
**SSL/TLS** - Secure Sockets Layer/Transport Layer Security  
**SSRF** - Server-Side Request Forgery  
**TTY** - Teletypewriter (Terminal)  
**UUID** - Universally Unique Identifier  
**WebSocket** - Full-duplex communication protocol  
**YAML** - YAML Ain't Markup Language

---

## Security Terms

**Attack Vector**  
The path or method used by an attacker to gain unauthorized access to a system or network.

**Cryptographic Hash**  
One-way mathematical function that converts input data into a fixed-size string of characters, used for integrity verification and tamper detection.

**Defense Evasion**  
Techniques used by attackers to avoid detection by security systems, often through encoding, obfuscation, or legitimate tool abuse.

**Exploit**  
Code or technique that takes advantage of a vulnerability to cause unintended behavior in a system.

**Forensics**  
The application of scientific methods to investigate and establish facts about security incidents and cyber crimes.

**Honeypot**  
Decoy system designed to attract attackers and gather intelligence about attack methods and patterns.

**Incident Response**  
Systematic approach to handling security breaches, including preparation, detection, containment, eradication, and recovery phases.

**Malware**  
Malicious software designed to damage, disrupt, or gain unauthorized access to systems.

**Penetration Testing**  
Authorized simulated cyber attack against systems to evaluate security effectiveness and identify vulnerabilities.

**Risk Assessment**  
Process of identifying, analyzing, and evaluating potential security risks to determine appropriate mitigation strategies.

**Security Baseline**  
Minimum security requirements and configurations that must be implemented across all systems and applications.

**Threat Model**  
Structured representation of potential threats to a system, including threat actors, attack vectors, and potential impacts.

**Vulnerability**  
Weakness in a system that could be exploited by threats to gain unauthorized access or cause harm.

---

## Operational Terms

**Availability**  
The degree to which a system is operational and accessible when required, typically measured as uptime percentage.

**Compliance**  
Adherence to laws, regulations, standards, and policies relevant to information security and data protection.

**Configuration Management**  
Process of maintaining system settings and configurations in a consistent, secure, and documented manner.

**Escalation**  
Process of forwarding security incidents or approval requests to higher authority levels when standard procedures are insufficient.

**Graceful Degradation**  
System design principle where functionality is reduced rather than completely failing when components or resources become unavailable.

**Health Check**  
Automated test that verifies system components are functioning correctly, used for monitoring and load balancer configuration.

**Load Balancing**  
Distribution of workload across multiple system components to ensure optimal resource utilization and performance.

**Monitoring**  
Continuous observation of system performance, security events, and operational metrics to ensure proper functioning.

**Scalability**  
System's ability to handle increased workload by adding resources or optimizing existing capacity.

**Service Level Agreement (SLA)**  
Formal agreement defining expected service performance levels, availability targets, and response times.

This glossary provides comprehensive definitions for terms used throughout the AgentShroud project documentation, enabling clear communication and understanding across technical and non-technical stakeholders.