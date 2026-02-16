# Container Security: IEC 62443 Compliance Framework

## Overview

This document outlines the comprehensive container security strategy aligned with IEC 62443 standards for the OneClaw project. IEC 62443 is the international standard for securing Industrial Automation and Control Systems (IACS), which is critical for Battery Energy Storage System (BESS) environments and OT/energy infrastructure.

## Executive Summary

**Objective**: Implement defense-in-depth container security controls that meet IEC 62443 security requirements across all containerized services in the OneClaw platform.

**Target Security Levels**:
- **SL 2** minimum: Management and analytics containers (data lake services)
- **SL 3** recommended: Containers handling OT data, protocol gateways (Modbus/DNP3), or with pathways to site controllers
- **SL 4**: Any containers in the direct control path of energy storage assets

**Primary Standards**:
- **IEC 62443-3-3**: System security requirements and security levels
- **IEC 62443-4-1**: Secure product development lifecycle (SDL) requirements
- **IEC 62443-4-2**: Technical security requirements for IACS components

---

## IEC 62443 Foundational Requirements (FR) Mapping

The technical security requirements in IEC 62443-3-3 are organized into seven foundational requirements. Each maps to specific container security controls:

### FR1 — Identification & Authentication Control

**Purpose**: Ensure all users, services, and components are uniquely identified and authenticated before access is granted.

**Container Security Controls**:

1. **Mutual TLS (mTLS) Between Services**
   - Implement certificate-based authentication for all inter-service communication
   - No plaintext service-to-service communication allowed
   - Certificate rotation automated through orchestration platform

2. **SPIFFE/SPIRE Workload Identity**
   - Every container receives a cryptographic identity (SPIFFE Verifiable Identity Document)
   - Replaces static credentials with dynamic, short-lived certificates
   - Workload attestation based on container properties (image hash, namespace, labels)

3. **Cloud IAM Integration**
   - AWS IAM Roles for Service Accounts (IRSA) for EKS deployments
   - Service accounts mapped to specific IAM roles with minimal permissions
   - No long-lived credentials stored in containers

4. **Container Registry Authentication**
   - All registry pulls require authentication (no anonymous access)
   - Amazon ECR private repositories with IAM-based pull permissions
   - Image pull secrets automatically injected into namespaces

**Compliance Mapping**: IEC 62443-4-2 CR 1.1, CR 1.2, CR 1.3

**Implementation Priority**: Phase 1 (Critical)

---

### FR2 — Use Control (Authorization)

**Purpose**: Enforce least-privilege access control to prevent unauthorized actions.

**Container Security Controls**:

1. **Role-Based Access Control (RBAC)**
   - Kubernetes RBAC policies defining who can deploy, modify, or delete resources
   - Separate roles for developers, operators, and administrators
   - Service accounts with minimal required permissions

2. **Policy Enforcement with OPA/Gatekeeper**
   - Admission control policies written in Rego
   - Enforce mandatory security requirements (non-root users, resource limits, etc.)
   - Block deployments that violate security policies
   - Alternative: Kyverno for Kubernetes-native policy management

3. **Non-Root Container Execution**
   - All containers run as non-root users by default
   - `runAsNonRoot: true` enforced via admission controllers
   - User ID (UID) explicitly set in container specifications
   - No privilege escalation allowed (`allowPrivilegeEscalation: false`)

4. **Linux Capabilities Management**
   - Drop all capabilities by default
   - Add back only required capabilities on case-by-case basis
   - Common approved capabilities: `NET_BIND_SERVICE` for services binding to ports <1024
   - Document and justify any capability additions

5. **Security Context Enforcement**
   - Seccomp profiles applied to restrict syscalls
   - AppArmor or SELinux policies for additional MAC (Mandatory Access Control)
   - Read-only root filesystem where possible
   - Prevent host filesystem access unless explicitly required

**Compliance Mapping**: IEC 62443-4-2 CR 2.1, CR 2.2, CR 2.3

**Implementation Priority**: Phase 1 (Critical)

---

### FR3 — System Integrity

**Purpose**: Ensure the authenticity and integrity of systems and prevent unauthorized changes.

**Container Security Controls**:

1. **Image Signing and Verification**
   - All production images signed with Cosign using keyless signing (Sigstore)
   - Admission controller verifies signatures before deployment
   - Reject unsigned or invalidly signed images
   - Supply chain security through transparent cryptographic verification

2. **Compliance Scanning with OpenSCAP**
   - Scan container images against CIS Benchmarks and DSTG STIG profiles
   - Automated scans in CI/CD pipeline before image promotion
   - Runtime compliance checks on running containers
   - Generate compliance reports for audit purposes
   - Integration with container-setup repository for centralized scanning

3. **Vulnerability Scanning**
   - Trivy or Grype for comprehensive CVE scanning
   - Scan at multiple stages: build time, registry storage, runtime
   - AWS ECR native scanning for images stored in ECR
   - Automated alerts for critical/high severity vulnerabilities
   - Vulnerability management workflow with SLA for patching

4. **Software Bill of Materials (SBOM)**
   - Generate SBOM with Syft for every container image
   - SBOM format: SPDX and CycloneDX
   - Store SBOMs alongside images in registry
   - Supply chain transparency and component tracking
   - Critical for IEC 62443-4-1 SDL requirements

5. **File Integrity Monitoring**
   - Runtime file integrity monitoring with Falco or AIDE
   - Detect unauthorized file modifications in containers
   - Alert on unexpected file system changes
   - Baseline integrity state established at deployment

6. **Immutable Infrastructure**
   - Read-only root filesystem (`readOnlyRootFilesystem: true`)
   - Use emptyDir or tmpfs volumes for temporary writes
   - No in-place updates; replace containers instead
   - Infrastructure as Code for all configurations

**Compliance Mapping**: IEC 62443-4-2 CR 3.1, CR 3.2, CR 3.4, IEC 62443-4-1 SDL

**Implementation Priority**: Phase 1-2

---

### FR4 — Data Confidentiality

**Purpose**: Protect sensitive data from unauthorized disclosure.

**Container Security Controls**:

1. **Encryption in Transit**
   - mTLS for all inter-service communication
   - TLS 1.3 minimum for external endpoints
   - No plaintext protocols (HTTP, unencrypted gRPC, etc.)
   - Certificate management automated through cert-manager

2. **Encryption at Rest**
   - AWS KMS-backed encryption for persistent volumes
   - Encrypted EBS volumes for stateful services
   - Database encryption enabled for all data stores
   - Encryption key rotation policies

3. **Secrets Management**
   - AWS Secrets Manager or HashiCorp Vault for runtime secret injection
   - No secrets baked into container images or environment variables
   - Secrets mounted as volumes or fetched at runtime
   - Automatic secret rotation where supported
   - Audit logging for all secret access

4. **Application-Layer Encryption**
   - Sensitive OT telemetry data encrypted at application layer
   - End-to-end encryption for critical data flows through the data lake pipeline
   - Encryption for data at rest in S3 buckets
   - Field-level encryption for PII or sensitive operational data

5. **Memory Protection**
   - Secure memory handling practices in application code
   - Clear sensitive data from memory after use
   - Prevent memory dumps from exposing secrets

**Compliance Mapping**: IEC 62443-4-2 CR 4.1, CR 4.2, CR 4.3

**Implementation Priority**: Phase 1-2

---

### FR5 — Restricted Data Flow

**Purpose**: Implement network segmentation (zones and conduits model) to control and monitor data flows.

**Container Security Controls**:

1. **Zones and Conduits Architecture**
   - Map container workloads to IEC 62443 security zones
   - Example zone structure:
     - **Zone 1**: Data ingestion containers (edge data collection)
     - **Zone 2**: Analytics and processing containers
     - **Zone 3**: Management plane and admin interfaces
     - **Zone 4**: OT/SCADA integration services (highest security)
   - Conduits define allowed communication paths between zones

2. **Kubernetes Network Policies**
   - Default-deny ingress and egress for all namespaces
   - Explicit allow rules for required communication paths
   - Label-based selectors for fine-grained control
   - Separate network policies per zone

3. **eBPF-Based Network Segmentation**
   - Cilium or Calico for advanced network security
   - Layer 7 (application-layer) network policies
   - Identity-based security (not IP-based)
   - Network flow visibility and monitoring
   - DNS-aware policies

4. **API Gateways as Conduits**
   - API gateways at zone boundaries
   - Traffic inspection and validation at gateways
   - Rate limiting and DDoS protection
   - Authentication and authorization at zone entry points

5. **Security Level Per Zone**
   - Different foundational requirement levels per zone
   - Example: SL 3 for FR1/FR3 in OT zone, SL 1 for FR4 in analytics zone
   - Document security level decisions and rationale

**Compliance Mapping**: IEC 62443-3-3 zones and conduits, IEC 62443-4-2 CR 5.1

**Implementation Priority**: Phase 2 (High)

---

### FR6 — Timely Response to Events

**Purpose**: Detect, report, and respond to security events in a timely manner.

**Container Security Controls**:

1. **Runtime Anomaly Detection with Falco**
   - Real-time syscall monitoring for unexpected behavior
   - Detection rules for:
     - Container escape attempts
     - Unexpected process execution in containers
     - File system modifications in read-only containers
     - Privilege escalation attempts
     - Network connections to unexpected destinations
   - Custom rules for application-specific threats

2. **Centralized Logging**
   - Fluent Bit as lightweight log collector in containers
   - Forward logs to centralized data lake or SIEM
   - Structured logging format (JSON) for easier parsing
   - Log retention policies compliant with regulations
   - Correlation of logs across multiple containers/services

3. **Security Information and Event Management (SIEM)**
   - Integration with existing Zabbix monitoring (if applicable)
   - Dedicated SIEM for security event correlation
   - Automated alerting on security policy violations
   - Examples:
     - Container attempting writes to read-only filesystem
     - Network policy violations
     - Failed authentication attempts
     - Abnormal resource consumption

4. **Incident Response**
   - Documented runbooks for container compromise scenarios
   - Automated containment actions (pod isolation, termination)
   - Forensic data collection procedures
   - Communication protocols for security incidents
   - Regular incident response drills

5. **Audit Logging**
   - Kubernetes audit logging enabled for API server
   - Container registry access logs
   - Identity and access management logs
   - Secrets access audit trail

**Compliance Mapping**: IEC 62443-4-2 CR 6.1, CR 6.2

**Implementation Priority**: Phase 2 (High)

---

### FR7 — Resource Availability

**Purpose**: Ensure system availability and resilience against resource exhaustion.

**Container Security Controls**:

1. **Resource Limits and Requests**
   - CPU and memory limits defined for all containers
   - Requests set based on actual usage metrics
   - Prevent noisy neighbor problems
   - Quality of Service (QoS) classes appropriately assigned

2. **Pod Disruption Budgets (PDB)**
   - Ensure minimum number of replicas during maintenance
   - Prevent voluntary disruptions from affecting availability
   - Especially critical for stateful services

3. **Health Checks**
   - Liveness probes: Detect and restart unhealthy containers
   - Readiness probes: Remove unhealthy containers from service endpoints
   - Startup probes: Handle slow-starting containers
   - Appropriate timeout and failure threshold settings

4. **DoS Protection**
   - Rate limiting at ingress controllers
   - Connection limits and request timeouts
   - Horizontal Pod Autoscaling (HPA) for traffic spikes
   - Cluster autoscaling for infrastructure capacity

5. **Backup and Recovery**
   - Automated backups for stateful container services
   - Disaster recovery procedures documented
   - Regular restore testing
   - RTO (Recovery Time Objective) and RPO (Recovery Point Objective) defined

6. **Degraded Operation Modes**
   - Define acceptable degraded performance under failures
   - Graceful degradation strategies
   - Circuit breakers for failing dependencies
   - Failover procedures for critical services

**Compliance Mapping**: IEC 62443-4-2 CR 7.1, CR 7.2

**Implementation Priority**: Phase 2-3

---

## IEC 62443-4-1: Secure Development Lifecycle (SDL)

This standard focuses on the development process itself, ensuring security is built-in from the start.

### Required Practices

1. **Secure Coding Guidelines**
   - Documented secure coding standards for all container applications
   - Language-specific guidelines (Python, Go, etc.)
   - Regular security training for development team
   - Code review checklists including security items

2. **Threat Modeling**
   - Threat model created for each containerized service before deployment
   - Use frameworks like STRIDE or PASTA
   - Document attack surfaces and trust boundaries
   - Update threat models when architecture changes

3. **Static Application Security Testing (SAST)**
   - Integrate tools like Semgrep, SonarQube, or Bandit into CI/CD
   - Scan code for security vulnerabilities before building images
   - Enforce quality gates for critical/high findings
   - Track remediation of identified issues

4. **Dynamic Application Security Testing (DAST)**
   - Runtime security testing against deployed containers
   - Tools like OWASP ZAP for web application testing
   - API fuzzing for microservices
   - Regular penetration testing schedule

5. **Patch Management**
   - Documented lifecycle for updating base images
   - Automated alerts for upstream security patches
   - SLA for applying critical security updates
   - Track container image versions and update status
   - Maps to IEC TR 62443-2-3 patch management

6. **Vulnerability Disclosure**
   - Process for handling security vulnerabilities
   - Security contact information published
   - Coordinated disclosure timeline
   - CVE assignment for significant vulnerabilities

7. **Defect Management**
   - Security defects tracked separately with higher priority
   - Root cause analysis for security incidents
   - Lessons learned documentation

8. **End-of-Life Procedures**
   - Defined EOL policy for container images
   - Decommissioning procedures for services
   - Data retention and deletion policies
   - Communication plan for deprecations

**Compliance Mapping**: IEC 62443-4-1 entire standard

**Implementation Priority**: Phase 1 (foundational)

---

## Implementation Roadmap

### Phase 1: Foundation (Months 1-2)
- [ ] Implement non-root container execution across all services
- [ ] Establish RBAC policies for Kubernetes cluster
- [ ] Set up container registry authentication (ECR with IAM)
- [ ] Integrate Trivy CVE scanning into CI/CD pipeline
- [ ] Implement basic network policies (default deny)
- [ ] Establish secure coding guidelines
- [ ] Set up admission controller (OPA Gatekeeper or Kyverno)

### Phase 2: Enhanced Security (Months 3-4)
- [ ] Deploy SPIFFE/SPIRE for workload identity
- [ ] Implement mTLS between all services
- [ ] Set up OpenSCAP compliance scanning
- [ ] Integrate Cosign for image signing
- [ ] Configure AWS Secrets Manager integration
- [ ] Deploy Falco for runtime anomaly detection
- [ ] Establish centralized logging with Fluent Bit
- [ ] Create zone-based network architecture
- [ ] Implement advanced network policies with Cilium/Calico

### Phase 3: Operations & Monitoring (Months 5-6)
- [ ] SIEM integration for security event correlation
- [ ] Automated incident response playbooks
- [ ] Generate and store SBOMs for all images
- [ ] Implement file integrity monitoring
- [ ] Create compliance dashboards
- [ ] Conduct first threat modeling sessions
- [ ] Establish patch management process
- [ ] Configure resource limits and PDBs across all services

### Phase 4: Continuous Improvement (Ongoing)
- [ ] Regular security assessments and audits
- [ ] Update threat models quarterly
- [ ] Penetration testing (annual or after major changes)
- [ ] Security metrics tracking and reporting
- [ ] Team security training programs
- [ ] Review and update policies based on lessons learned

---

## Security Tool Stack

| Layer | Tool | Purpose | IEC 62443 FR | Priority |
|-------|------|---------|-------------|----------|
| Compliance Scanning | OpenSCAP | CIS/STIG profile validation | FR3 | Phase 2 |
| Image Vulnerability | Trivy + AWS ECR | CVE detection and tracking | FR3 | Phase 1 |
| Supply Chain | Cosign + Syft | Image signing & SBOM generation | FR3, 4-1 SDL | Phase 2 |
| Runtime Detection | Falco | Anomaly detection & threat response | FR3, FR6 | Phase 2 |
| Network Segmentation | Cilium/Calico | eBPF-based network policies | FR5 | Phase 2 |
| Workload Identity | SPIFFE/SPIRE | Cryptographic service identity | FR1 | Phase 2 |
| Secrets Management | AWS Secrets Manager / Vault | Runtime secret injection | FR4 | Phase 2 |
| Policy Enforcement | OPA Gatekeeper / Kyverno | Admission control & compliance | FR2 | Phase 1 |
| Logging/Monitoring | Fluent Bit + SIEM | Centralized logging & alerting | FR6 | Phase 2 |
| Secure Development | Semgrep + Threat Modeling | SAST & security design | 4-1 SDL | Phase 1 |
| Certificate Management | cert-manager | TLS certificate automation | FR1, FR4 | Phase 2 |

---

## Integration with Container-Setup Repository

The `/Users/ijefferson.admin/Development/container-setup` repository should be reviewed and enhanced to support this security framework:

1. **Centralized Security Scanning**: OpenSCAP scanning templates and profiles
2. **Base Image Hardening**: Secure base images with security tools pre-installed
3. **Security Configuration Management**: Standardized security configurations
4. **Compliance Reporting**: Automated compliance report generation
5. **CI/CD Integration**: Security scanning hooks for build pipelines

---

## Deliverables

### Documentation
1. **Container Security Policy Document**: Formal policy defining security requirements
2. **Compliance Matrix**: Mapping of OneClaw services to IEC 62443 requirements
3. **Hardening Checklist**: CI/CD pipeline integration checklist
4. **Incident Response Runbooks**: Container-specific security incident procedures
5. **Threat Models**: Per-service threat analysis documents
6. **Security Architecture Diagram**: Zones, conduits, and data flows

### Technical Artifacts
1. **Network Policy Templates**: Reusable Kubernetes NetworkPolicy manifests
2. **OPA/Gatekeeper Policies**: Security constraint policies
3. **Falco Rules**: Custom runtime detection rules
4. **Image Signing Workflow**: Automated signing in CI/CD
5. **SBOM Generation**: Integrated into build process
6. **Compliance Scan Reports**: Automated reporting dashboard

---

## Success Metrics

1. **Coverage**: 100% of container images scanned for vulnerabilities
2. **Compliance**: 0 critical/high vulnerabilities in production within SLA
3. **Image Signing**: 100% of production images cryptographically signed
4. **Network Segmentation**: All namespaces with default-deny policies
5. **Runtime Detection**: Falco deployed to 100% of clusters
6. **Audit**: All security events logged and retained per policy
7. **SDL Adherence**: 100% of new services threat modeled before deployment
8. **Incident Response**: Mean time to detect (MTTD) < 15 minutes for critical events

---

## References

- IEC 62443-3-3: Industrial communication networks - Network and system security - System security requirements and security levels
- IEC 62443-4-1: Security for industrial automation and control systems - Secure product development lifecycle requirements
- IEC 62443-4-2: Technical security requirements for IACS components
- IEC TR 62443-2-3: Patch management in the IACS environment
- CIS Benchmarks for Container Security
- NIST SP 800-190: Application Container Security Guide

---

## Document Control

**Version**: 1.0
**Created**: 2026-02-14
**Owner**: OneClaw Security Team
**Review Cycle**: Quarterly
**Next Review**: 2026-05-14
