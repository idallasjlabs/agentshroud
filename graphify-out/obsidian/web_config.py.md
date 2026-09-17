---
source_file: "gateway/proxy/web_config.py"
type: "code"
community: "Egress Filter & HTTP Proxy"
location: "L1"
tags:
  - graphify/code
  - graphify/EXTRACTED
  - community/Egress_Filter__HTTP_Proxy
---

# web_config.py

## Connections
- [[DomainSettings]] - `contains` [EXTRACTED]
- [[WebProxyConfig]] - `contains` [EXTRACTED]
- [[http_proxy.py]] - `imports_from` [EXTRACTED]
- [[lifespan.py]] - `imports_from` [EXTRACTED]
- [[url_analyzer.py]] - `references` [EXTRACTED]
- [[web_content_scanner.py]] - `references` [EXTRACTED]
- [[web_proxy.py]] - `imports_from` [EXTRACTED]

#graphify/code #graphify/EXTRACTED #community/Egress_Filter__HTTP_Proxy