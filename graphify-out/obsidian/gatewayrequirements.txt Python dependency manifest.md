---
source_file: "gateway/requirements.txt"
type: "code"
community: "Collaborator Setup Checklist"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Collaborator_Setup_Checklist
---

# gateway/requirements.txt Python dependency manifest

## Connections
- [[Dockerfile.gateway vault note]] - `references` [EXTRACTED]
- [[cryptography=50.0.1 pin (CVE-2026-692476924869249, GHSA-537c-gmf6-5ccf)]] - `references` [EXTRACTED]
- [[gateway service (prod, sole egress point, 75-module pipeline)]] - `shares_data_with` [INFERRED]
- [[pip-audit gap — gateway Python deps not scanned]] - `references` [AMBIGUOUS]
- [[setuptools=83.0.0 pin (PYSEC-2026-3447)]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Collaborator_Setup_Checklist