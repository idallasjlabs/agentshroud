---
source_file: "scripts/asb"
type: "code"
community: "setup-secrets.sh"
location: "L475-L486"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/setup-secretssh
---

# _prune_docker

## Connections
- [[_fstrim_colima_datadisk]] - `calls` [EXTRACTED]
- [[_prune_superseded_images]] - `calls` [EXTRACTED]
- [[asb]] - `defines` [EXTRACTED]
- [[asb rebuild  clean-rebuild subcommands]] - `calls` [EXTRACTED]
- [[asb script]] - `calls` [EXTRACTED]
- [[asb up subcommand]] - `calls` [EXTRACTED]
- [[lazydocker docker.sock connection leak]] - `conceptually_related_to` [INFERRED]

#graphify/code #graphify/EXTRACTED #community/setup-secretssh
