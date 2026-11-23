---
source_file: "tests/startup_smoke/test_sunday_upgrade_head_guard.sh"
type: "code"
community: "sunday-upgrade-apply.sh"
location: "L116-L130"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/sunday-upgrade-applysh
---

# phase_apply build loop calls the guard every iteration

## Connections
- [[S16 asb rebuildclean-rebuild build with $_PROFILE_FLAG]] - `semantically_similar_to` [INFERRED]
- [[_assert_head_unchanged()]] - `references` [EXTRACTED]
- [[phase_apply()]] - `references` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/sunday-upgrade-applysh
