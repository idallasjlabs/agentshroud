---
source_file: "gateway/runtime/__init__.py"
type: "code"
community: "patch"
location: "L48"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/patch
---

# get_engine()

## Connections
- [[dot-_get_engine()]] - `calls` [INFERRED]
- [[dot-test_auto_detect_priority()]] - `calls` [EXTRACTED]
- [[dot-test_explicit_apple()]] - `calls` [EXTRACTED]
- [[dot-test_explicit_docker()]] - `calls` [EXTRACTED]
- [[dot-test_explicit_podman()]] - `calls` [EXTRACTED]
- [[dot-test_invalid_runtime()]] - `calls` [EXTRACTED]
- [[dot-test_no_runtime_available()]] - `calls` [EXTRACTED]
- [[AppleContainerEngine]] - `uses` [INFERRED]
- [[ContainerEngine]] - `uses` [INFERRED]
- [[DockerEngine]] - `uses` [INFERRED]
- [[PodmanEngine]] - `uses` [INFERRED]
- [[Return an appropriate container engine instance. Args preference Explicit…]] - `rationale_for` [EXTRACTED]
- [[_get_engine()]] - `calls` [EXTRACTED]
- [[api.py_2]] - `imports` [EXTRACTED]
- [[detect_runtime()]] - `calls` [EXTRACTED]
- [[get_status()]] - `calls` [EXTRACTED]
- [[health.py]] - `imports` [EXTRACTED]
- [[runtime__init__.py]] - `contains` [EXTRACTED]
- [[test_runtime_engines.py]] - `imports` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/patch
