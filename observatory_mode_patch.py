#!/usr/bin/env python3
import re
import os
from datetime import datetime, timezone

# Read the main.py file
with open('gateway/ingest_api/main.py', 'r') as f:
    content = f.read()

# 1. Add observatory mode and auto_revert_task to AppState class
content = re.sub(
    r'(http_proxy: Optional\[HTTPConnectProxy\])',
    r'\1\n    observatory_mode: dict\n    auto_revert_task: Optional[object]',
    content
)

# 2. Add observatory mode initialization after event bus initialization
observatory_init = '''
    # Initialize observatory mode state
    app_state.observatory_mode = {
        "global_mode": os.getenv("AGENTSHROUD_MODE", "enforce"),
        "effective_since": datetime.now(tz=timezone.utc).isoformat(),
        "auto_revert_at": None,
        "pinned_modules": [],
    }
    app_state.auto_revert_task = None
    logger.info(f"Observatory mode initialized: global_mode={app_state.observatory_mode['global_mode']}")
'''

content = re.sub(
    r'(app_state\.event_bus = EventBus\(\)\n    logger\.info\("Event bus initialized"\))',
    r'\1' + observatory_init,
    content
)

# Write the modified content back
with open('gateway/ingest_api/main.py', 'w') as f:
    f.write(content)

print('Observatory mode state initialization added to main.py')
