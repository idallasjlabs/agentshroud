---
source_file: "gateway/security/image_verifier.py"
type: "code"
community: "Image Verifier"
location: "L30"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Image_Verifier
---

# verify_image()

## Connections
- [[Cosign signature verification of container images (fail-closed on missing binarytimeoutbad signature)]] - `rationale_for` [INFERRED]
- [[Verify an image signature using cosign keyless OIDC verification.      Args]] - `rationale_for` [EXTRACTED]
- [[image_verifier.py]] - `contains` [EXTRACTED]
- [[test_cosign_fails_bad_signature()]] - `calls` [EXTRACTED]
- [[test_cosign_not_found()]] - `calls` [EXTRACTED]
- [[test_cosign_success()]] - `calls` [EXTRACTED]
- [[test_cosign_timeout()]] - `calls` [EXTRACTED]
- [[test_image_verifier.py]] - `imports` [EXTRACTED]
- [[verify_images()]] - `calls` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Image_Verifier