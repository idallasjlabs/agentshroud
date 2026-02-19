# ADR-005: SHA-256 Hash Chain for Audit Integrity

## Status
**Accepted** - December 2025

## Context

AgentShroud requires tamper-evident audit logging to ensure security event integrity. Options evaluated:

1. **Traditional Logging**: Standard log files with optional encryption
2. **Database Audit Tables**: Structured logging with database integrity constraints  
3. **Cryptographic Hash Chain**: Blockchain-inspired immutable audit trail
4. **Digital Signatures**: Sign each audit entry with private key

## Decision

Implement **SHA-256 Hash Chain** audit system:

```
Genesis Block: hash(timestamp + "GENESIS" + random_seed)
Block N: hash(previous_hash + timestamp + event_data + sequence_number)
Verification: Validate entire chain from genesis to current block
```

### Hash Chain Structure
```json
{
  "sequence": 1,
  "timestamp": "2025-12-19T10:30:00Z",
  "event_type": "request_filtered",
  "event_data": {...},
  "content_hash": "sha256(event_data)",
  "previous_hash": "a1b2c3...",
  "chain_hash": "sha256(previous_hash + content_hash + sequence + timestamp)"
}
```

## Consequences

### Positive Consequences
- **Tamper Detection**: Any modification breaks the cryptographic chain
- **Non-Repudiation**: Cryptographically proves event sequence and integrity
- **Forensic Analysis**: Complete audit trail reconstruction from any point
- **Compliance**: Meets requirements for immutable audit logs (IEC 62443)

### Negative Consequences
- **Storage Overhead**: Each entry requires additional hash fields
- **Performance Impact**: Hash calculation adds computational cost
- **Chain Recovery**: Broken chains require full re-validation

### Implementation Details
- Use SHA-256 for cryptographic hashing (FIPS 140-2 approved)
- Periodic chain validation every 1000 entries
- Automated backup and integrity verification
- Chain splitting for performance optimization at scale