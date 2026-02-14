# Gateway Layer

The gateway layer is the core of SecureClaw's proxy architecture. It sits between user-forwarded content and the OpenClaw agent.

## Structure (to be implemented in Week 1, Days 3-4)

```
gateway/
├── ingest-api/
│   ├── main.py           # FastAPI application
│   ├── sanitizer.py      # PII redaction engine
│   ├── router.py         # Multi-agent routing
│   └── ledger.py         # Data inventory tracking
├── approval-queue/
│   └── queue.py          # Action approval service
├── requirements.txt      # Python dependencies
└── Dockerfile           # Gateway container image
```

## Features

### Ingest API
- `/forward` endpoint - Accepts forwarded content
- Authentication via shared secret
- Returns ledger ID and sanitization report
- Supports: text, URLs, photos, files

### PII Sanitizer
- Microsoft Presidio or spaCy NER
- Detects: SSN, credit cards, phone, email, addresses
- Configurable redaction rules
- Audit log of all redactions

### Data Ledger
- SQLite database
- Tracks all forwarded content
- Schema: id, timestamp, source, content_hash, sanitized, size
- Search, filter, "forget this" deletion

### Approval Queue
- WebSocket server for real-time approvals
- Queue system for agent-requested actions
- Push notifications via Tailscale

## Tech Stack

- Python 3.11+
- FastAPI
- Microsoft Presidio (PII detection)
- SQLite
- WebSocket

## Implementation Status

🚧 **Not yet implemented** - Scheduled for Week 1, Days 3-4
