# AgentShroud Text Interfaces

## Control Center

Simple text-based control center for monitoring AgentShroud.

### Usage

```bash
# From repo root
./scripts/start-control-center

# Or directly
python3 src/interfaces/text_control_center.py
```

### Controls

- **Press Enter**: Refresh the dashboard
- **Type 'q' + Enter**: Quit

### What it Shows

- Current timestamp
- System status (ACTIVE)
- Version number

## Future Interfaces

This directory will contain additional text-based interfaces for:
- Log monitoring
- Message queue inspection
- Security event viewing
- Container health checks

All interfaces are designed to work in tmux for split-pane monitoring.
