---
source_file: "gateway/security/egress_filter.py"
type: "rationale"
community: "First iteration ingests + records; second sees dedup and skips. (2)"
location: "L78"
tags:
  - graphify/rationale
  - graphify/EXTRACTED
  - community/First_iteration_ingests__records_second_sees_dedup_and_skips_2
---

# Check if IP matches any allowed IP/CIDR.

## Connections
- [[dot-matches_ip()]] - `rationale_for` [EXTRACTED]

#graphify/rationale #graphify/EXTRACTED #community/First_iteration_ingests__records_second_sees_dedup_and_skips_2
