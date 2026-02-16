# Workspace Configuration Decision

**Date**: 2026-02-16
**Decision**: Use Docker Volume (Option 1)

---

## Decision Summary

**Question**: Should workspace use Docker volume or bind mount?

**Answer**: **Docker Volume** (current configuration)

**Rationale**:
- ✅ Better performance on Mac
- ✅ More secure (isolated from host filesystem)
- ✅ No permission issues
- ✅ Portable and Docker-managed
- ✅ Helper script makes it easy to use

---

## Configuration

### Current Setup (Kept)

```yaml
# docker/docker-compose.yml
volumes:
  - openclaw-workspace:/home/node/openclaw/workspace
```

**Location**: Docker volume `openclaw-workspace`
**Mount point**: `/home/node/openclaw/workspace/` inside container
**Access**: Via helper script `docker/scripts/workspace.sh`

---

## Helper Script

**Created**: `docker/scripts/workspace.sh`

**Usage**:
```bash
./docker/scripts/workspace.sh ls              # List files
./docker/scripts/workspace.sh cp-to FILE      # Copy to workspace
./docker/scripts/workspace.sh cp-from FILE    # Copy from workspace
./docker/scripts/workspace.sh cat FILE        # View file
./docker/scripts/workspace.sh shell           # Interactive shell
```

**Full documentation**: `WORKSPACE_USAGE.md`

---

## Why This Matters for Read-Only Filesystem

When we enable `read_only: true`, the workspace will remain writable:

```yaml
services:
  openclaw:
    read_only: true  # System files read-only
    volumes:
      - openclaw-workspace:/home/node/openclaw/workspace:rw  # Workspace still writable
```

**Bot can**:
- ✅ Write to `/home/node/openclaw/workspace/` (your shared folder)
- ✅ Write to `/home/node/.openclaw/` (skills, memory)
- ✅ Write to tmpfs (cache, temp files)

**Bot cannot**:
- ❌ Write to `/usr/bin/`, `/etc/`, `/lib/` (system files)
- ❌ Modify container OS
- ❌ Install system packages at runtime

This gives us **security** (immutable OS) AND **functionality** (bot can work).

---

## Files Created

1. `docker/scripts/workspace.sh` - Helper script for workspace operations
2. `WORKSPACE_USAGE.md` - Complete usage guide
3. `OPENCLAW_WRITE_REQUIREMENTS.md` - Technical explanation of write requirements
4. `DEVELOPMENT_WORKFLOW_READ_ONLY.md` - Development workflow for read-only mode
5. `WORKSPACE_DECISION.md` - This file

---

## Next Steps

With workspace configuration decided, we can now:

1. ✅ Keep current Docker volume setup
2. ✅ Add missing tmpfs mounts for read-only compatibility
3. ✅ Continue with Phase 3A security implementation
4. ✅ Test read-only mode when features are complete

---

**Status**: Configuration finalized, ready to proceed with Phase 3A
