# Import/Export Feature: Data Portability & System Migration

## Overview

This feature enables comprehensive data portability for the OneClaw platform, allowing users to export all settings, configurations, historical data, and activity logs, then reimport them into a clean installation. This is critical for system migrations, disaster recovery, container OS updates, and maintaining business continuity.

## Business Justification

### Problem Statement

Users need the ability to:
1. **Migrate to new infrastructure** without data loss when upgrading container OS or moving to new hardware
2. **Recover from disasters** by restoring complete system state from exports
3. **Clone environments** for testing, development, or multi-site deployments
4. **Maintain data sovereignty** by having full control over their data
5. **Perform clean reinstalls** while preserving years of historical data and configurations

### User Stories

**As a system administrator**, I want to export all system configurations and data so that I can migrate to a new container infrastructure without manual reconfiguration.

**As a compliance officer**, I want to maintain complete historical records even when updating underlying systems so that I can meet regulatory retention requirements.

**As a DevOps engineer**, I want to clone production environments to staging so that I can test upgrades safely before applying them to production.

**As a security professional**, I want to back up the complete system state regularly so that I can recover from ransomware or system compromise.

**As an early adopter**, I want to preserve my data when upgrading to new OneClaw versions so that I don't lose valuable historical insights.

---

## Functional Requirements

### FR1: Export Capabilities

The system shall export the following data categories:

#### 1. System Configuration
- User accounts and authentication settings
- Role-based access control (RBAC) policies
- API keys and service tokens (encrypted)
- System preferences and global settings
- Integration configurations (third-party services, webhooks)
- Network and security policies
- Resource quotas and limits

#### 2. Application Data
- All conversational history and agent interactions
- User-generated content (documents, code, analyses)
- Uploaded files and attachments
- Knowledge base articles and documentation
- Custom persona definitions
- Workflow and automation configurations

#### 3. Metadata and Activity Logs
- Audit logs (all user and system actions)
- Performance metrics and telemetry
- Error logs and debugging information
- Security event logs
- Usage statistics and analytics
- Timestamps and version information

#### 4. Operational State
- Running job queues and pending tasks
- Scheduled operations and cron jobs
- Cache contents (optional, for performance)
- Session state (optional, for continuity)

### FR2: Export Formats

The system shall support multiple export formats:

1. **Complete Archive** (recommended)
   - Single compressed file (`.tar.gz` or `.zip`)
   - Includes all data, configurations, and metadata
   - Self-contained with manifest file
   - Cryptographically signed for integrity verification

2. **Selective Export**
   - User can choose specific data categories
   - Useful for partial migrations or targeted backups
   - Individual JSON files per category

3. **Incremental Export**
   - Only export changes since last export
   - Significantly smaller file sizes
   - Faster export for regular backups
   - Requires base export reference

### FR3: Import Capabilities

The system shall support:

1. **Full System Restore**
   - Complete replacement of all system data
   - Wipe existing data before import (with confirmation)
   - Verify export integrity before import
   - Rollback on import failure

2. **Selective Import**
   - Import specific data categories only
   - Merge with existing data (conflict resolution strategies)
   - Preview import contents before applying

3. **Migration Mode**
   - Import from older OneClaw versions
   - Automatic schema migrations
   - Data transformation for compatibility
   - Validation and error reporting

### FR4: Data Integrity and Security

1. **Encryption**
   - Export files encrypted at rest using AES-256
   - User-provided passphrase or key-based encryption
   - Support for AWS KMS or HashiCorp Vault key management

2. **Integrity Verification**
   - SHA-256 checksums for all exported files
   - Digital signatures for tamper detection
   - Manifest file with file listing and checksums

3. **Sensitive Data Handling**
   - API keys and secrets encrypted separately
   - Option to exclude sensitive data from export
   - Audit log of export/import operations

4. **Access Control**
   - Only administrators can perform exports/imports
   - Multi-factor authentication required for production exports
   - IP whitelisting for export operations (optional)

### FR5: User Experience

1. **Progress Tracking**
   - Real-time progress indicators for long-running exports
   - Estimated time remaining
   - Cancellation support with cleanup

2. **Validation**
   - Pre-export validation checks
   - Post-import verification tests
   - Dry-run mode for import (preview without applying)

3. **Notifications**
   - Email/webhook notifications on export completion
   - Alerts for failed exports/imports
   - Summary report with statistics

---

## Technical Specification

### Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    OneClaw Platform                     │
├─────────────────────────────────────────────────────────┤
│  ┌───────────────────────────────────────────────────┐  │
│  │         Export/Import Orchestrator                │  │
│  │  - Manages export/import workflows                │  │
│  │  - Coordinates data extraction/restoration        │  │
│  │  - Progress tracking & error handling             │  │
│  └───────────────────────────────────────────────────┘  │
│           │                          │                   │
│           ▼                          ▼                   │
│  ┌─────────────────┐       ┌──────────────────┐         │
│  │  Data Exporters │       │  Data Importers  │         │
│  │  - DB Exporter  │       │  - DB Importer   │         │
│  │  - File Export  │       │  - File Import   │         │
│  │  - Config Exp.  │       │  - Config Import │         │
│  │  - Log Exporter │       │  - Log Importer  │         │
│  └─────────────────┘       └──────────────────┘         │
│           │                          │                   │
│           ▼                          ▼                   │
│  ┌─────────────────────────────────────────────────┐    │
│  │         Encryption & Compression Layer          │    │
│  │  - AES-256 encryption                           │    │
│  │  - gzip/zstd compression                        │    │
│  │  - Checksum generation                          │    │
│  └─────────────────────────────────────────────────┘    │
│           │                          │                   │
│           ▼                          ▼                   │
│  ┌─────────────────────────────────────────────────┐    │
│  │             Storage Layer                       │    │
│  │  - Local filesystem                             │    │
│  │  - S3-compatible storage                        │    │
│  │  - Azure Blob Storage                           │    │
│  └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

### Export File Structure

```
oneclaw-export-2026-02-14-173045.tar.gz
│
├── manifest.json              # Export metadata, file listing, checksums
├── version.json               # OneClaw version, schema version
│
├── config/
│   ├── system.json           # Global system settings
│   ├── users.json            # User accounts (passwords hashed)
│   ├── rbac.json             # RBAC policies and permissions
│   ├── integrations.json     # Third-party integrations
│   └── secrets.enc           # Encrypted secrets bundle
│
├── data/
│   ├── conversations/        # All conversation history
│   │   ├── 2026-01/
│   │   ├── 2026-02/
│   │   └── ...
│   ├── documents/            # User-uploaded files
│   ├── personas/             # Custom persona definitions
│   └── knowledge-base/       # KB articles and embeddings
│
├── logs/
│   ├── audit.jsonl           # Audit logs (JSON Lines format)
│   ├── security.jsonl        # Security event logs
│   ├── application.jsonl     # Application logs
│   └── metrics.jsonl         # Performance metrics
│
└── database/
    ├── postgresql_dump.sql   # PostgreSQL database dump
    ├── redis_dump.rdb        # Redis snapshot (if applicable)
    └── vector_store/         # Vector embeddings export
```

### Manifest File Schema

```json
{
  "export_metadata": {
    "export_id": "exp_2026-02-14-173045_a3f8e2c",
    "created_at": "2026-02-14T17:30:45Z",
    "oneclaw_version": "0.1.0",
    "schema_version": "1.0",
    "export_type": "full",
    "exported_by": "admin@example.com",
    "encryption": {
      "algorithm": "AES-256-GCM",
      "key_derivation": "PBKDF2-SHA256",
      "iterations": 100000
    },
    "compression": "gzip"
  },
  "system_info": {
    "hostname": "oneclaw-prod-01",
    "container_runtime": "docker",
    "database_version": "PostgreSQL 15.4",
    "total_users": 42,
    "total_conversations": 1523,
    "total_size_bytes": 2147483648
  },
  "files": [
    {
      "path": "config/system.json",
      "size_bytes": 4096,
      "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "encrypted": true
    },
    {
      "path": "data/conversations/2026-02/conv_123.json",
      "size_bytes": 16384,
      "sha256": "d7a8fbb307d7809469ca9abcb0082e4f8d5651e46d3cdb762d02d0bf37c9e592",
      "encrypted": true
    }
    // ... additional files
  ],
  "data_categories": [
    {
      "category": "conversations",
      "record_count": 1523,
      "size_bytes": 524288000,
      "date_range": {
        "earliest": "2025-06-01T00:00:00Z",
        "latest": "2026-02-14T17:30:00Z"
      }
    },
    {
      "category": "audit_logs",
      "record_count": 45231,
      "size_bytes": 104857600,
      "date_range": {
        "earliest": "2025-06-01T00:00:00Z",
        "latest": "2026-02-14T17:30:00Z"
      }
    }
    // ... additional categories
  ]
}
```

### API Endpoints

#### Export API

```
POST /api/v1/export
Content-Type: application/json
Authorization: Bearer <admin_token>

Request Body:
{
  "export_type": "full" | "selective" | "incremental",
  "categories": ["config", "data", "logs", "database"],  // if selective
  "encryption": {
    "enabled": true,
    "passphrase": "user-provided-passphrase"  // or use KMS
  },
  "compression": "gzip" | "zstd",
  "destination": {
    "type": "local" | "s3" | "azure",
    "path": "/exports/",  // or S3 bucket URL
    "credentials": { ... }  // if remote storage
  },
  "include_options": {
    "include_secrets": false,  // exclude sensitive data
    "include_cache": false,
    "include_temp_data": false
  },
  "notification": {
    "email": "admin@example.com",
    "webhook": "https://example.com/webhook"
  }
}

Response:
{
  "export_id": "exp_2026-02-14-173045_a3f8e2c",
  "status": "initiated",
  "estimated_duration_seconds": 300,
  "status_url": "/api/v1/export/exp_2026-02-14-173045_a3f8e2c"
}
```

#### Export Status

```
GET /api/v1/export/{export_id}
Authorization: Bearer <admin_token>

Response:
{
  "export_id": "exp_2026-02-14-173045_a3f8e2c",
  "status": "in_progress" | "completed" | "failed",
  "progress_percent": 65,
  "current_phase": "exporting_database",
  "started_at": "2026-02-14T17:30:45Z",
  "estimated_completion": "2026-02-14T17:35:45Z",
  "exported_size_bytes": 1073741824,
  "download_url": "/api/v1/export/exp_2026-02-14-173045_a3f8e2c/download",
  "expires_at": "2026-02-21T17:30:45Z"  // 7-day retention
}
```

#### Import API

```
POST /api/v1/import
Content-Type: multipart/form-data
Authorization: Bearer <admin_token>

Form Data:
- file: <export_file.tar.gz>
- passphrase: <decryption_passphrase>
- import_mode: "replace" | "merge"
- dry_run: true | false
- conflict_resolution: "skip" | "overwrite" | "rename"

Response:
{
  "import_id": "imp_2026-02-14-180000_b4g9f3d",
  "status": "validating",
  "validation_results": {
    "manifest_valid": true,
    "checksums_valid": true,
    "version_compatible": true,
    "warnings": []
  },
  "status_url": "/api/v1/import/imp_2026-02-14-180000_b4g9f3d"
}
```

### Database Considerations

1. **PostgreSQL**
   - Use `pg_dump` with custom format for flexibility
   - Include schema and data
   - Handle large object (LOB) exports

2. **Vector Store** (if using Qdrant, Weaviate, etc.)
   - Export collections and embeddings
   - Preserve metadata and indexes
   - Include collection configurations

3. **Redis** (if used for caching/sessions)
   - Optional RDB snapshot export
   - Typically not critical for migration

### File Storage Considerations

1. **Large File Handling**
   - Stream large files to avoid memory issues
   - Chunked upload/download for reliability
   - Resume support for interrupted transfers

2. **External References**
   - Handle S3 object references in database
   - Options: export actual files or maintain references
   - Document external dependencies

---

## Implementation Plan

### Phase 1: Core Export (Weeks 1-2)
- [ ] Design export file format and manifest schema
- [ ] Implement database export (PostgreSQL dump)
- [ ] Implement configuration export (JSON serialization)
- [ ] Basic encryption and compression
- [ ] Local filesystem storage
- [ ] CLI tool for export

### Phase 2: Core Import (Weeks 3-4)
- [ ] Import validation and verification
- [ ] Database restoration
- [ ] Configuration restoration
- [ ] Basic conflict resolution
- [ ] CLI tool for import
- [ ] Rollback on import failure

### Phase 3: Enhanced Features (Weeks 5-6)
- [ ] Web UI for export/import
- [ ] Selective export/import
- [ ] Incremental export
- [ ] S3 storage backend
- [ ] Progress tracking and notifications
- [ ] Dry-run mode for imports

### Phase 4: Security & Compliance (Weeks 7-8)
- [ ] AWS KMS integration
- [ ] Digital signatures
- [ ] Audit logging for export/import operations
- [ ] MFA requirement for production exports
- [ ] Export retention policies
- [ ] Automated backup scheduling

### Phase 5: Testing & Documentation (Weeks 9-10)
- [ ] Integration tests for export/import workflows
- [ ] Migration testing between versions
- [ ] Large-scale export testing (multi-GB)
- [ ] User documentation and runbooks
- [ ] Disaster recovery procedures
- [ ] Performance benchmarking

---

## User Interface Mockups

### Export Dialog

```
┌────────────────────────────────────────────────────────┐
│  Export OneClaw Data                              [X]  │
├────────────────────────────────────────────────────────┤
│                                                        │
│  Export Type:                                          │
│   ◉ Full System Export (Recommended)                  │
│   ○ Selective Export                                   │
│   ○ Incremental Export (since last backup)            │
│                                                        │
│  Include:                                              │
│   ☑ System Configuration                              │
│   ☑ User Accounts & Permissions                       │
│   ☑ Conversation History                              │
│   ☑ Uploaded Documents                                │
│   ☑ Audit Logs                                         │
│   ☐ Cache Data (not recommended)                      │
│                                                        │
│  Security:                                             │
│   ☑ Encrypt export file                               │
│   Passphrase: [•••••••••••••••••]                     │
│   ☐ Exclude API keys and secrets                      │
│                                                        │
│  Destination:                                          │
│   ◉ Download to local computer                        │
│   ○ Save to S3 bucket: [___________________]          │
│                                                        │
│  Estimated export size: 2.1 GB                         │
│  Estimated time: 5-10 minutes                          │
│                                                        │
│           [Cancel]              [Start Export]         │
└────────────────────────────────────────────────────────┘
```

### Import Dialog

```
┌────────────────────────────────────────────────────────┐
│  Import OneClaw Data                              [X]  │
├────────────────────────────────────────────────────────┤
│                                                        │
│  Export File:                                          │
│   [oneclaw-export-2026-02-14.tar.gz] [Browse...]      │
│                                                        │
│  Decryption Passphrase:                               │
│   [•••••••••••••••••]                                 │
│                                                        │
│  ✓ Export file validated successfully                 │
│  ✓ Version compatible (0.1.0)                         │
│  ✓ Checksums verified                                 │
│                                                        │
│  Export Contents:                                      │
│   • 42 user accounts                                   │
│   • 1,523 conversations                                │
│   • 45,231 audit log entries                          │
│   • 2.1 GB total data                                  │
│                                                        │
│  Import Mode:                                          │
│   ○ Replace all data (WARNING: deletes existing)      │
│   ◉ Merge with existing data                          │
│                                                        │
│  Conflict Resolution:                                  │
│   ◉ Keep existing data                                │
│   ○ Overwrite with imported data                      │
│   ○ Rename imported data                              │
│                                                        │
│  ☑ Perform dry run first (preview changes)            │
│                                                        │
│           [Cancel]              [Start Import]         │
└────────────────────────────────────────────────────────┘
```

---

## Security Considerations

1. **Export Access Control**
   - Only system administrators can initiate exports
   - Exports of production systems require MFA
   - Rate limiting to prevent abuse

2. **Data in Transit**
   - HTTPS for all API communications
   - Signed URLs for download with expiration

3. **Data at Rest**
   - Export files encrypted by default
   - Secure passphrase requirements (min 16 chars, complexity)
   - Key rotation for KMS-managed exports

4. **Audit Trail**
   - Log all export/import operations
   - Include user identity, timestamp, IP address
   - Alert security team for production exports

5. **Sensitive Data**
   - Option to exclude secrets from export
   - API keys re-generated on import (not imported)
   - Password hashes included but salted

---

## Testing Strategy

### Unit Tests
- Export/import individual data categories
- Encryption/decryption functions
- Checksum validation
- Manifest generation and parsing

### Integration Tests
- Full export workflow
- Full import workflow
- Selective export/import
- Migration between versions
- Conflict resolution scenarios

### Performance Tests
- Large dataset export (10GB+)
- Import performance benchmarks
- Concurrent export operations
- Network interruption recovery

### Security Tests
- Encryption strength validation
- Tamper detection
- Access control enforcement
- Sensitive data handling

---

## Success Metrics

1. **Reliability**: 99.9% success rate for export/import operations
2. **Performance**: Export 1GB of data in < 2 minutes
3. **Integrity**: 100% data integrity verification on import
4. **Usability**: Average time to complete export/import < 15 minutes for 10GB dataset
5. **Recovery**: Full system restore from export in < 30 minutes

---

## Documentation Requirements

1. **User Guide**: Step-by-step export/import procedures
2. **Admin Guide**: Backup strategies and disaster recovery
3. **API Reference**: Complete API documentation
4. **Migration Guide**: Version-to-version migration procedures
5. **Troubleshooting**: Common issues and resolutions
6. **Security Guide**: Best practices for handling exports

---

## Future Enhancements

1. **Cloud-native Backups**: Integration with cloud backup services (AWS Backup, Azure Backup)
2. **Automated Scheduling**: Cron-based automated exports
3. **Incremental Backups**: More sophisticated change tracking
4. **Multi-region Replication**: Automatic export to multiple regions
5. **Compliance Reporting**: Export audit reports for compliance
6. **Data Anonymization**: Export with PII removed for testing environments

---

## Document Control

**Version**: 1.0
**Created**: 2026-02-14
**Owner**: OneClaw Product Team
**Review Cycle**: Quarterly
**Next Review**: 2026-05-14
**Priority**: High (Pre-v0.1.0 Release)
