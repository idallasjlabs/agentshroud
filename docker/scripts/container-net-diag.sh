#!/bin/bash
# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
# container-net-diag.sh — Comprehensive container network diagnostic
#
# Run inside any Docker container to diagnose connectivity issues.
# Tests every layer of the network stack and reports pass/fail at each level.
#
# Usage: docker exec <container> bash /path/to/container-net-diag.sh
#        docker exec <container> bash /path/to/container-net-diag.sh --json
#
# Exit codes:
#   0 = all tests passed
#   1 = one or more tests failed
#
# Dependencies: None required. Uses whatever tools are available in the container
# (ip/ifconfig, ping, nc/ncat, curl/wget, nslookup/dig/getent, traceroute/mtr).

set -o pipefail

# ── Configuration ────────────────────────────────────────────────────────────
PING_TARGET_IP="8.8.8.8"
PING_TARGET_HOST="google.com"
DNS_SERVERS="8.8.8.8 1.1.1.1"
DNS_TEST_DOMAIN="google.com"
TCP_TARGETS="8.8.8.8:443 8.8.8.8:53 1.1.1.1:443"
HTTP_TEST_URL="http://detectportal.firefox.com/canonical.html"
HTTPS_TEST_URL="https://api.anthropic.com"
PING_COUNT=2
PING_TIMEOUT=3
TCP_TIMEOUT=5
HTTP_TIMEOUT=10
TRACEROUTE_HOPS=15

JSON_MODE=false
[[ "${1:-}" == "--json" ]] && JSON_MODE=true

# ── State tracking ───────────────────────────────────────────────────────────
PASS=0
FAIL=0
WARN=0
RESULTS=()

# ── Output helpers ───────────────────────────────────────────────────────────
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
BOLD='\033[1m'
NC='\033[0m'

header() {
  if ! $JSON_MODE; then
    echo ""
    echo -e "${BOLD}${BLUE}═══ $1 ═══${NC}"
  fi
}

pass() {
  ((PASS++))
  RESULTS+=("{\"test\":\"$1\",\"status\":\"pass\",\"detail\":\"$2\"}")
  if ! $JSON_MODE; then
    echo -e "  ${GREEN}✅ PASS${NC} $1 — $2"
  fi
}

fail() {
  ((FAIL++))
  RESULTS+=("{\"test\":\"$1\",\"status\":\"fail\",\"detail\":\"$2\"}")
  if ! $JSON_MODE; then
    echo -e "  ${RED}❌ FAIL${NC} $1 — $2"
  fi
}

warn() {
  ((WARN++))
  RESULTS+=("{\"test\":\"$1\",\"status\":\"warn\",\"detail\":\"$2\"}")
  if ! $JSON_MODE; then
    echo -e "  ${YELLOW}⚠️  WARN${NC} $1 — $2"
  fi
}

info() {
  if ! $JSON_MODE; then
    echo -e "  ${BLUE}ℹ${NC}  $1"
  fi
}

# ── Tool detection ───────────────────────────────────────────────────────────
has() { command -v "$1" >/dev/null 2>&1; }

# ── Start ────────────────────────────────────────────────────────────────────
if ! $JSON_MODE; then
  echo -e "${BOLD}╔════════════════════════════════════════════════════════╗${NC}"
  echo -e "${BOLD}║   Container Network Diagnostic — AgentShroud v0.8.0   ║${NC}"
  echo -e "${BOLD}╚════════════════════════════════════════════════════════╝${NC}"
  echo ""
  echo "  Container: $(hostname 2>/dev/null || echo unknown)"
  echo "  Date:      $(date -u '+%Y-%m-%d %H:%M:%S UTC' 2>/dev/null || date)"
  echo "  Kernel:    $(uname -r 2>/dev/null || echo unknown)"
fi

# ══════════════════════════════════════════════════════════════════════════════
# 1. NETWORK INTERFACES
# ══════════════════════════════════════════════════════════════════════════════
# Initialize variables that may not get set if tools are missing
DEFAULT_GW=""
DEFAULT_IF=""

header "1. Network Interfaces"

if has ip; then
  IFACES=$(ip -br addr show 2>/dev/null)
  if [ -n "$IFACES" ]; then
    DEFAULT_IF=$(ip route show default 2>/dev/null | awk '{print $5}' | head -1)
    while IFS= read -r line; do
      IFNAME=$(echo "$line" | awk '{print $1}')
      STATE=$(echo "$line" | awk '{print $2}')
      ADDRS=$(echo "$line" | awk '{$1=$2=""; print $0}' | xargs)
      info "$IFNAME  state=$STATE  addrs=$ADDRS"
    done <<< "$IFACES"

    if [ -n "$DEFAULT_IF" ]; then
      DEFAULT_STATE=$(echo "$IFACES" | grep "^$DEFAULT_IF" | awk '{print $2}')
      if [[ "$DEFAULT_STATE" == "UP" ]]; then
        pass "Default interface" "$DEFAULT_IF is UP"
      else
        fail "Default interface" "$DEFAULT_IF is $DEFAULT_STATE (expected UP)"
      fi
    else
      fail "Default interface" "No default interface found"
    fi
  else
    fail "Network interfaces" "No interfaces found"
  fi
elif has ifconfig; then
  ifconfig 2>/dev/null | head -20
  warn "Interface check" "Using ifconfig (ip not available)"
elif has node; then
  # Node.js fallback for minimal containers
  RESULT=$(node -e "const os=require('os');const n=os.networkInterfaces();Object.entries(n).forEach(([k,v])=>{v.forEach(i=>{if(!i.internal)console.log(k+' '+i.address+' '+i.family)})})" 2>/dev/null)
  if [ -n "$RESULT" ]; then
    echo "$RESULT" | while IFS= read -r line; do info "$line"; done
    pass "Interface check" "Detected via Node.js (ip/ifconfig not available)"
  else
    fail "Interface check" "No external interfaces found"
  fi
else
  fail "Interface check" "Neither ip, ifconfig, nor node available"
fi

# Check for eth0 IP
CONTAINER_IP=""
if has ip; then
  CONTAINER_IP=$(ip -4 addr show scope global 2>/dev/null | grep inet | awk '{print $2}' | head -1)
elif has hostname; then
  CONTAINER_IP=$(hostname -I 2>/dev/null | awk '{print $1}')
fi
if [ -n "$CONTAINER_IP" ]; then
  pass "Container IP" "$CONTAINER_IP"
else
  fail "Container IP" "No global IP address assigned"
fi

# MTU check (VPN/overlay issues often caused by MTU mismatch)
if has ip && [ -n "$DEFAULT_IF" ]; then
  MTU=$(ip link show "$DEFAULT_IF" 2>/dev/null | grep -oP 'mtu \K[0-9]+')
  if [ -n "$MTU" ]; then
    if [ "$MTU" -ge 1400 ]; then
      pass "MTU" "$DEFAULT_IF MTU=$MTU"
    else
      warn "MTU" "$DEFAULT_IF MTU=$MTU (low — may cause fragmentation with VPN/overlay)"
    fi
  fi
fi

# ══════════════════════════════════════════════════════════════════════════════
# 2. ROUTING TABLE
# ══════════════════════════════════════════════════════════════════════════════
header "2. Routing Table"

if has ip; then
  ROUTES=$(ip route show 2>/dev/null)
  info "$(echo "$ROUTES" | head -10)"

  DEFAULT_GW=$(echo "$ROUTES" | grep "^default" | awk '{print $3}' | head -1)
  if [ -n "$DEFAULT_GW" ]; then
    pass "Default gateway" "$DEFAULT_GW via $DEFAULT_IF"
  else
    fail "Default gateway" "No default route — internet traffic has no next-hop"
  fi
elif has route; then
  route -n 2>/dev/null | head -10
  DEFAULT_GW=$(route -n 2>/dev/null | grep "^0.0.0.0" | awk '{print $2}' | head -1)
  if [ -n "$DEFAULT_GW" ]; then
    pass "Default gateway" "$DEFAULT_GW"
  else
    fail "Default gateway" "No default route found"
  fi
elif has node; then
  # Node.js can't read routing table, but we can infer gateway from /proc
  if [ -f /proc/net/route ]; then
    DEFAULT_GW=$(awk '$2=="00000000"{split($3,a,"");printf "%d.%d.%d.%d",strtonum("0x"a[7]a[8]),strtonum("0x"a[5]a[6]),strtonum("0x"a[3]a[4]),strtonum("0x"a[1]a[2])}' /proc/net/route 2>/dev/null)
    DEFAULT_IF=$(awk '$2=="00000000"{print $1}' /proc/net/route 2>/dev/null | head -1)
    if [ -n "$DEFAULT_GW" ]; then
      pass "Default gateway" "$DEFAULT_GW via $DEFAULT_IF (from /proc/net/route)"
    else
      warn "Routing" "Could not parse /proc/net/route"
    fi
  else
    warn "Routing" "Neither ip, route, nor /proc/net/route available"
  fi
else
  warn "Routing" "No routing tools available"
fi

# ══════════════════════════════════════════════════════════════════════════════
# 3. GATEWAY REACHABILITY (ICMP)
# ══════════════════════════════════════════════════════════════════════════════
header "3. Gateway Reachability"

if [ -n "$DEFAULT_GW" ] && has ping; then
  if ping -c "$PING_COUNT" -W "$PING_TIMEOUT" "$DEFAULT_GW" >/dev/null 2>&1; then
    LATENCY=$(ping -c 1 -W "$PING_TIMEOUT" "$DEFAULT_GW" 2>/dev/null | grep -oP 'time=\K[0-9.]+' || echo "?")
    pass "Gateway ping" "$DEFAULT_GW reachable (${LATENCY}ms)"
  else
    fail "Gateway ping" "$DEFAULT_GW unreachable — issue is within Docker network"
  fi
elif [ -z "$DEFAULT_GW" ]; then
  fail "Gateway ping" "Skipped — no gateway to test"
elif ! has ping; then
  # Try TCP to gateway instead
  if has nc; then
    if nc -z -w "$TCP_TIMEOUT" "$DEFAULT_GW" 80 2>/dev/null; then
      pass "Gateway TCP" "$DEFAULT_GW:80 reachable"
    else
      warn "Gateway test" "ping not available, nc to gateway:80 failed"
    fi
  else
    warn "Gateway test" "Neither ping nor nc available"
  fi
fi

# ══════════════════════════════════════════════════════════════════════════════
# 4. DNS RESOLUTION
# ══════════════════════════════════════════════════════════════════════════════
header "4. DNS Resolution"

# 4a. DNS server port reachability
for DNS in $DNS_SERVERS; do
  if has nc; then
    if nc -z -w "$TCP_TIMEOUT" -u "$DNS" 53 2>/dev/null || nc -z -w "$TCP_TIMEOUT" "$DNS" 53 2>/dev/null; then
      pass "DNS port" "$DNS:53 reachable"
    else
      fail "DNS port" "$DNS:53 unreachable — DNS traffic may be blocked"
    fi
  else
    info "nc not available — skipping DNS port test for $DNS"
  fi
done

# 4b. Check configured nameservers
info "resolv.conf nameservers:"
grep "^nameserver" /etc/resolv.conf 2>/dev/null | while read -r line; do
  info "  $line"
done

# 4c. Actual hostname resolution
DNS_RESOLVED=false
if has nslookup; then
  RESULT=$(nslookup "$DNS_TEST_DOMAIN" 2>/dev/null | grep -A1 "Name:" | grep "Address" | head -1)
  if [ -n "$RESULT" ]; then
    pass "DNS resolution" "$DNS_TEST_DOMAIN → $(echo "$RESULT" | awk '{print $NF}')"
    DNS_RESOLVED=true
  fi
fi

if ! $DNS_RESOLVED && has dig; then
  RESULT=$(dig +short "$DNS_TEST_DOMAIN" 2>/dev/null | head -1)
  if [ -n "$RESULT" ]; then
    pass "DNS resolution" "$DNS_TEST_DOMAIN → $RESULT"
    DNS_RESOLVED=true
  fi
fi

if ! $DNS_RESOLVED && has getent; then
  RESULT=$(getent hosts "$DNS_TEST_DOMAIN" 2>/dev/null | awk '{print $1}' | head -1)
  if [ -n "$RESULT" ]; then
    pass "DNS resolution" "$DNS_TEST_DOMAIN → $RESULT"
    DNS_RESOLVED=true
  fi
fi

if ! $DNS_RESOLVED; then
  # Try Node.js as last resort (common in Node containers)
  if has node; then
    RESULT=$(node -e "require('dns').resolve4('$DNS_TEST_DOMAIN',(e,a)=>console.log(e?'FAIL':a[0]))" 2>/dev/null)
    if [ -n "$RESULT" ] && [ "$RESULT" != "FAIL" ]; then
      pass "DNS resolution" "$DNS_TEST_DOMAIN → $RESULT (via node)"
      DNS_RESOLVED=true
    fi
  fi
fi

if ! $DNS_RESOLVED; then
  fail "DNS resolution" "Cannot resolve $DNS_TEST_DOMAIN — no working resolver"
fi

# ══════════════════════════════════════════════════════════════════════════════
# 5. ICMP PING TO INTERNET
# ══════════════════════════════════════════════════════════════════════════════
header "5. Internet Ping (ICMP)"

if has ping; then
  # Raw IP ping
  if ping -c "$PING_COUNT" -W "$PING_TIMEOUT" "$PING_TARGET_IP" >/dev/null 2>&1; then
    LATENCY=$(ping -c 1 -W "$PING_TIMEOUT" "$PING_TARGET_IP" 2>/dev/null | grep -oP 'time=\K[0-9.]+' || echo "?")
    pass "Ping (IP)" "$PING_TARGET_IP reachable (${LATENCY}ms)"
    IP_PING=true
  else
    fail "Ping (IP)" "$PING_TARGET_IP unreachable — routing or firewall issue"
    IP_PING=false
  fi

  # Hostname ping (tests DNS + routing together)
  if ping -c "$PING_COUNT" -W "$PING_TIMEOUT" "$PING_TARGET_HOST" >/dev/null 2>&1; then
    pass "Ping (hostname)" "$PING_TARGET_HOST reachable"
  else
    if $IP_PING; then
      fail "Ping (hostname)" "$PING_TARGET_HOST unreachable but IP works — DNS issue"
    else
      fail "Ping (hostname)" "$PING_TARGET_HOST unreachable — routing issue"
    fi
  fi
else
  warn "Ping test" "ping not available in container"
fi

# ══════════════════════════════════════════════════════════════════════════════
# 6. TCP CONNECTIVITY
# ══════════════════════════════════════════════════════════════════════════════
header "6. TCP Connectivity"

tcp_test() {
  local HOST="$1"
  local PORT="$2"
  local LABEL="$3"

  if has nc; then
    if nc -z -w "$TCP_TIMEOUT" "$HOST" "$PORT" 2>/dev/null; then
      pass "TCP $LABEL" "$HOST:$PORT open"
      return 0
    fi
  fi

  # Fallback: bash /dev/tcp
  if (echo >/dev/tcp/"$HOST"/"$PORT") 2>/dev/null; then
    pass "TCP $LABEL" "$HOST:$PORT open (bash)"
    return 0
  fi

  # Fallback: node
  if has node; then
    RESULT=$(timeout "$TCP_TIMEOUT" node -e "
      const s = new (require('net').Socket)();
      s.setTimeout(${TCP_TIMEOUT}000);
      s.connect($PORT, '$HOST', () => { console.log('OK'); s.destroy(); });
      s.on('error', () => console.log('FAIL'));
      s.on('timeout', () => { console.log('TIMEOUT'); s.destroy(); });
    " 2>/dev/null)
    if [ "$RESULT" = "OK" ]; then
      pass "TCP $LABEL" "$HOST:$PORT open (node)"
      return 0
    fi
  fi

  fail "TCP $LABEL" "$HOST:$PORT closed/blocked"
  return 1
}

for TARGET in $TCP_TARGETS; do
  HOST="${TARGET%:*}"
  PORT="${TARGET#*:}"
  tcp_test "$HOST" "$PORT" "$HOST:$PORT"
done

# Test proxy endpoint if HTTP_PROXY is set
if [ -n "${HTTP_PROXY:-}" ]; then
  PROXY_HOST=$(echo "$HTTP_PROXY" | sed 's|http://||' | cut -d: -f1)
  PROXY_PORT=$(echo "$HTTP_PROXY" | sed 's|http://||' | cut -d: -f2)
  info "HTTP_PROXY=$HTTP_PROXY"
  tcp_test "$PROXY_HOST" "$PROXY_PORT" "proxy"
fi

# ══════════════════════════════════════════════════════════════════════════════
# 7. HTTP/HTTPS CONNECTIVITY
# ══════════════════════════════════════════════════════════════════════════════
header "7. HTTP/HTTPS Connectivity"

http_test() {
  local URL="$1"
  local LABEL="$2"
  local PROXY_FLAG=""

  # Use proxy if configured
  if [ -n "${HTTP_PROXY:-}" ]; then
    PROXY_FLAG="-x $HTTP_PROXY"
  fi

  if has curl; then
    CODE=$(curl $PROXY_FLAG -sf --connect-timeout "$HTTP_TIMEOUT" --max-time "$HTTP_TIMEOUT" -o /dev/null -w "%{http_code}" "$URL" 2>/dev/null)
    if [ -n "$CODE" ] && [ "$CODE" != "000" ]; then
      pass "$LABEL" "$URL → HTTP $CODE"
      return 0
    fi
  fi

  if has wget; then
    if wget $PROXY_FLAG --timeout="$HTTP_TIMEOUT" --spider -q "$URL" 2>/dev/null; then
      pass "$LABEL" "$URL → reachable"
      return 0
    fi
  fi

  if has node; then
    RESULT=$(timeout "$HTTP_TIMEOUT" node -e "
      const u = new URL('$URL');
      const mod = u.protocol === 'https:' ? require('https') : require('http');
      const opts = {hostname: u.hostname, port: u.port || (u.protocol === 'https:' ? 443 : 80), path: u.pathname, method: 'HEAD', timeout: ${HTTP_TIMEOUT}000};
      const req = mod.request(opts, (res) => { console.log(res.statusCode); });
      req.on('error', (e) => console.log('ERR:' + e.code));
      req.on('timeout', () => { console.log('TIMEOUT'); req.destroy(); });
      req.end();
    " 2>/dev/null)
    if [ -n "$RESULT" ] && [[ "$RESULT" =~ ^[0-9]+$ ]]; then
      pass "$LABEL" "$URL → HTTP $RESULT (node)"
      return 0
    fi
  fi

  fail "$LABEL" "$URL → unreachable"
  return 1
}

http_test "$HTTP_TEST_URL" "HTTP"
http_test "$HTTPS_TEST_URL" "HTTPS"

# Direct vs proxy comparison (if proxy is configured)
if [ -n "${HTTP_PROXY:-}" ]; then
  info "Testing direct (no proxy) for comparison..."
  CODE=$(curl -sf --noproxy "*" --connect-timeout 5 -o /dev/null -w "%{http_code}" "https://google.com" 2>/dev/null)
  if [ -n "$CODE" ] && [ "$CODE" != "000" ]; then
    warn "Direct HTTPS" "google.com reachable WITHOUT proxy (HTTP $CODE) — proxy bypass possible"
  else
    pass "Direct blocked" "Direct HTTPS fails without proxy — egress enforcement working"
  fi
fi

# ══════════════════════════════════════════════════════════════════════════════
# 8. TRACEROUTE
# ══════════════════════════════════════════════════════════════════════════════
header "8. Traceroute"

if has traceroute; then
  info "Tracing to $PING_TARGET_IP (max $TRACEROUTE_HOPS hops)..."
  TRACE=$(traceroute -m "$TRACEROUTE_HOPS" -w 2 "$PING_TARGET_IP" 2>/dev/null | head -20)
  echo "$TRACE" | while IFS= read -r line; do
    info "$line"
  done

  HOP_COUNT=$(echo "$TRACE" | grep -c "^ " 2>/dev/null || echo 0)
  LAST_RESPONDING=$(echo "$TRACE" | grep -v "\* \* \*" | tail -1)
  if echo "$TRACE" | grep -q "$PING_TARGET_IP"; then
    pass "Traceroute" "Reached $PING_TARGET_IP in $HOP_COUNT hops"
  elif [ "$HOP_COUNT" -le 1 ]; then
    fail "Traceroute" "Stuck at hop 1 — traffic not leaving container network namespace"
  else
    warn "Traceroute" "Reached hop $HOP_COUNT but not target — upstream issue"
  fi
elif has mtr; then
  info "Running mtr report to $PING_TARGET_IP..."
  mtr -r -c 3 -n "$PING_TARGET_IP" 2>/dev/null | while IFS= read -r line; do
    info "$line"
  done
  pass "MTR" "Report complete (review above)"
else
  warn "Traceroute" "Neither traceroute nor mtr available"
fi

# ══════════════════════════════════════════════════════════════════════════════
# 9. TCP TRACEROUTE (Port 443)
# ══════════════════════════════════════════════════════════════════════════════
header "9. TCP Traceroute (Port 443)"

# TCP traceroute bypasses ICMP-blocking environments and traces the actual
# path HTTPS traffic takes — useful for identifying where TLS is being dropped.

if has tcptraceroute; then
  info "TCP traceroute to $PING_TARGET_IP:443..."
  TRACE=$(tcptraceroute -m "$TRACEROUTE_HOPS" -w 2 "$PING_TARGET_IP" 443 2>/dev/null | head -20)
  echo "$TRACE" | while IFS= read -r line; do info "$line"; done
  if echo "$TRACE" | grep -q "\[open\]"; then
    pass "TCP traceroute" "Reached $PING_TARGET_IP:443 — port open"
  else
    HOP_COUNT=$(echo "$TRACE" | grep -c "^ " 2>/dev/null || echo 0)
    if [ "$HOP_COUNT" -le 1 ]; then
      fail "TCP traceroute" "Stuck at hop 1 — TCP egress blocked at container boundary"
    else
      warn "TCP traceroute" "Reached hop $HOP_COUNT but port 443 not open at destination"
    fi
  fi
elif has traceroute; then
  # Some traceroute implementations support -T for TCP mode
  if traceroute --help 2>&1 | grep -q "\-T"; then
    info "TCP traceroute (traceroute -T) to $PING_TARGET_IP:443..."
    TRACE=$(traceroute -T -m "$TRACEROUTE_HOPS" -w 2 -p 443 "$PING_TARGET_IP" 2>/dev/null | head -20)
    if [ -n "$TRACE" ]; then
      echo "$TRACE" | while IFS= read -r line; do info "$line"; done
      if echo "$TRACE" | grep -q "$PING_TARGET_IP"; then
        pass "TCP traceroute" "Reached $PING_TARGET_IP:443"
      else
        warn "TCP traceroute" "Did not reach destination"
      fi
    else
      warn "TCP traceroute" "traceroute -T failed (may need root)"
    fi
  else
    warn "TCP traceroute" "traceroute does not support -T flag"
  fi
elif has node; then
  # Node.js TCP hop estimation: connect and measure latency tiers
  info "TCP traceroute not available — testing TCP reachability via Node.js..."
  RESULT=$(timeout "$TCP_TIMEOUT" node -e "
    const start = Date.now();
    const s = new (require('net').Socket)();
    s.setTimeout(${TCP_TIMEOUT}000);
    s.connect(443, '$PING_TARGET_IP', () => {
      console.log('OPEN ' + (Date.now()-start) + 'ms');
      s.destroy();
    });
    s.on('error', (e) => console.log('FAIL ' + e.code + ' ' + (Date.now()-start) + 'ms'));
    s.on('timeout', () => { console.log('TIMEOUT ' + (Date.now()-start) + 'ms'); s.destroy(); });
  " 2>/dev/null)
  if echo "$RESULT" | grep -q "^OPEN"; then
    pass "TCP 443 reachability" "$PING_TARGET_IP:443 $RESULT"
  elif echo "$RESULT" | grep -q "^FAIL"; then
    fail "TCP 443 reachability" "$PING_TARGET_IP:443 $RESULT"
  else
    fail "TCP 443 reachability" "$PING_TARGET_IP:443 timeout"
  fi
else
  warn "TCP traceroute" "No TCP traceroute tools available"
fi

# ══════════════════════════════════════════════════════════════════════════════
# 10. MTU / FRAGMENTATION CHECK
# ══════════════════════════════════════════════════════════════════════════════
header "10. MTU / Fragmentation Check"

# MTU mismatches are a silent but common failure mode in containerized environments
# using overlay networks (Docker Swarm, K8s Flannel/Calico, WireGuard, VPNs).
# Large packets get silently dropped while small ones succeed, making connections
# appear intermittent or broken only for certain traffic types.

# Read interface MTU
IFACE_MTU=""
if has ip && [ -n "${DEFAULT_IF:-}" ]; then
  IFACE_MTU=$(ip link show "$DEFAULT_IF" 2>/dev/null | grep -oP 'mtu \K[0-9]+')
elif [ -f /sys/class/net/eth0/mtu ]; then
  IFACE_MTU=$(cat /sys/class/net/eth0/mtu 2>/dev/null)
  DEFAULT_IF="${DEFAULT_IF:-eth0}"
fi

if [ -n "$IFACE_MTU" ]; then
  info "Interface ${DEFAULT_IF:-unknown} MTU: $IFACE_MTU"

  if [ "$IFACE_MTU" -lt 1280 ]; then
    fail "MTU" "MTU $IFACE_MTU is below IPv6 minimum (1280) — will cause failures"
  elif [ "$IFACE_MTU" -lt 1400 ]; then
    warn "MTU" "MTU $IFACE_MTU is low — may cause fragmentation with VPN/overlay"
  else
    pass "MTU value" "MTU $IFACE_MTU is standard"
  fi

  # Fragmentation test: send large packet with DF (don't fragment) flag
  if has ping && [ -n "${DEFAULT_GW:-}" ]; then
    # Payload size = MTU - IP header (20) - ICMP header (8)
    PAYLOAD_SIZE=$((IFACE_MTU - 28))
    if [ "$PAYLOAD_SIZE" -gt 0 ]; then
      # -M do = don't fragment (Linux), -D = don't fragment (BSD/macOS)
      if ping -c 1 -W "$PING_TIMEOUT" -s "$PAYLOAD_SIZE" -M do "$DEFAULT_GW" >/dev/null 2>&1 ||
         ping -c 1 -W "$PING_TIMEOUT" -s "$PAYLOAD_SIZE" -D "$DEFAULT_GW" >/dev/null 2>&1; then
        pass "MTU path" "Full MTU packet ($PAYLOAD_SIZE + 28 = $IFACE_MTU) delivered to gateway"
      else
        fail "MTU path" "Full MTU packet dropped at gateway — MTU mismatch in path"
      fi
    fi

    # Also test a typical HTTPS-sized payload (1400 bytes)
    if [ "$IFACE_MTU" -gt 1400 ]; then
      if ping -c 1 -W "$PING_TIMEOUT" -s 1372 -M do "$DEFAULT_GW" >/dev/null 2>&1 ||
         ping -c 1 -W "$PING_TIMEOUT" -s 1372 -D "$DEFAULT_GW" >/dev/null 2>&1; then
        pass "MTU HTTPS" "1400-byte packet delivered (typical HTTPS payload size)"
      else
        warn "MTU HTTPS" "1400-byte packet dropped — HTTPS traffic may fail intermittently"
      fi
    fi
  elif has node && [ -n "${DEFAULT_GW:-}" ]; then
    info "ping not available — MTU path test requires ping with DF flag"
  else
    info "Cannot test MTU path (no ping or no gateway)"
  fi
else
  warn "MTU" "Could not determine interface MTU"
  # Try /proc fallback
  if [ -d /sys/class/net ]; then
    for iface in /sys/class/net/*/mtu; do
      IFNAME=$(echo "$iface" | cut -d/ -f5)
      [ "$IFNAME" = "lo" ] && continue
      MTU_VAL=$(cat "$iface" 2>/dev/null)
      if [ -n "$MTU_VAL" ]; then
        info "$IFNAME MTU: $MTU_VAL"
      fi
    done
  fi
fi

# ══════════════════════════════════════════════════════════════════════════════
# 11. FIREWALL RULES
# ══════════════════════════════════════════════════════════════════════════════
header "11. Firewall Rules (iptables)"

# Docker relies on iptables NAT and FORWARD rules to route container traffic.
# If these are misconfigured or flushed, containers lose outbound connectivity
# even though their internal configuration looks correct.

if has iptables; then
  # Try reading rules (usually needs root)
  RULES=$(iptables -L -n 2>/dev/null)
  if [ -n "$RULES" ]; then
    info "iptables FORWARD chain:"
    iptables -L FORWARD -n -v 2>/dev/null | head -10 | while IFS= read -r line; do
      info "  $line"
    done
    info ""
    info "iptables NAT POSTROUTING:"
    iptables -t nat -L POSTROUTING -n -v 2>/dev/null | head -10 | while IFS= read -r line; do
      info "  $line"
    done

    # Check for DROP-all in FORWARD
    if iptables -L FORWARD -n 2>/dev/null | grep -q "DROP.*0.0.0.0/0.*0.0.0.0/0"; then
      warn "Firewall" "FORWARD chain has blanket DROP rule — may block container traffic"
    else
      pass "Firewall" "No blanket DROP in FORWARD chain"
    fi

    # Check DOCKER-USER chain exists
    if iptables -L DOCKER-USER -n >/dev/null 2>&1; then
      DOCKER_USER_RULES=$(iptables -L DOCKER-USER -n 2>/dev/null | grep -c "DROP\|REJECT")
      info "DOCKER-USER chain: $DOCKER_USER_RULES blocking rules"
      pass "DOCKER-USER" "Chain exists ($DOCKER_USER_RULES blocking rules)"
    fi
  else
    info "iptables requires root — run from host:"
    info "  docker exec --user root <container> iptables -L -n"
    info "  iptables -L FORWARD -n -v  (on host)"
    info "  iptables -t nat -L POSTROUTING -n -v  (on host)"
    warn "Firewall" "Cannot read iptables (not root)"
  fi
elif has nft; then
  NFT_RULES=$(nft list ruleset 2>/dev/null | head -20)
  if [ -n "$NFT_RULES" ]; then
    info "nftables rules (first 20 lines):"
    echo "$NFT_RULES" | while IFS= read -r line; do info "  $line"; done
    pass "Firewall" "nftables rules readable"
  else
    warn "Firewall" "Cannot read nftables (not root)"
  fi
else
  info "No firewall tools in container (expected in minimal images)"
  info "Run on HOST to check Docker firewall:"
  info "  sudo iptables -L FORWARD -n -v"
  info "  sudo iptables -L DOCKER-USER -n -v"
  info "  sudo iptables -t nat -L POSTROUTING -n -v"
  warn "Firewall" "No iptables/nft — check host-side rules manually"
fi

# ══════════════════════════════════════════════════════════════════════════════
# 12. QUICK DIAGNOSIS GUIDE
# ══════════════════════════════════════════════════════════════════════════════
header "12. Diagnosis Decision Table"

if ! $JSON_MODE; then
  echo ""
  echo "  ┌─────────────────────────┬────────────────────────────────────────────┐"
  echo "  │ Failure Pattern          │ Likely Cause                               │"
  echo "  ├─────────────────────────┼────────────────────────────────────────────┤"
  echo "  │ No interface / DOWN      │ Docker network detached or misconfigured   │"
  echo "  │ No default route         │ Docker routing broken (restart Colima)     │"
  echo "  │ Gateway ping fails       │ Docker bridge issue (check host iptables)  │"
  echo "  │ DNS port blocked         │ Firewall blocking UDP/TCP 53               │"
  echo "  │ DNS resolves, ping fails │ NAT/routing broken upstream of container   │"
  echo "  │ IP ping ok, host fails   │ DNS resolver misconfigured                 │"
  echo "  │ ICMP ok, TCP blocked     │ Firewall rules blocking specific ports     │"
  echo "  │ TCP ok, HTTP fails       │ Proxy misconfiguration or TLS issue        │"
  echo "  │ Small packets ok, large  │ MTU mismatch (overlay/VPN/WireGuard)       │"
  echo "  │   packets fail           │                                            │"
  echo "  │ Traceroute stuck hop 1   │ Traffic not leaving container namespace    │"
  echo "  │ Traceroute stuck hop N   │ Upstream firewall or ISP issue             │"
  echo "  │ Works via proxy only     │ Correct! Container is isolated by design   │"
  echo "  └─────────────────────────┴────────────────────────────────────────────┘"
  echo ""
  echo "  Host-side commands for parallel diagnosis:"
  echo "    sudo iptables -L FORWARD -n -v"
  echo "    sudo iptables -L DOCKER-USER -n -v"
  echo "    sudo iptables -t nat -L POSTROUTING -n -v"
  echo "    docker network inspect <network_name>"
  echo "    docker inspect <container> --format '{{json .NetworkSettings}}'"
  echo "    ip route show  (inside Colima VM: colima ssh -- ip route show)"
fi

# ══════════════════════════════════════════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════════════════════════════════════════

if $JSON_MODE; then
  echo "{"
  echo "  \"timestamp\": \"$(date -u +%Y-%m-%dT%H:%M:%SZ 2>/dev/null)\","
  echo "  \"container\": \"$(hostname 2>/dev/null)\","
  echo "  \"pass\": $PASS,"
  echo "  \"fail\": $FAIL,"
  echo "  \"warn\": $WARN,"
  echo "  \"results\": ["
  for i in "${!RESULTS[@]}"; do
    if [ "$i" -lt $((${#RESULTS[@]} - 1)) ]; then
      echo "    ${RESULTS[$i]},"
    else
      echo "    ${RESULTS[$i]}"
    fi
  done
  echo "  ]"
  echo "}"
else
  echo ""
  echo -e "${BOLD}╔════════════════════════════════════════╗${NC}"
  echo -e "${BOLD}║            SUMMARY                     ║${NC}"
  echo -e "${BOLD}╠════════════════════════════════════════╣${NC}"
  echo -e "${BOLD}║${NC}  ${GREEN}PASS: $PASS${NC}  ${RED}FAIL: $FAIL${NC}  ${YELLOW}WARN: $WARN${NC}          ${BOLD}║${NC}"
  echo -e "${BOLD}╚════════════════════════════════════════╝${NC}"

  if [ "$FAIL" -eq 0 ]; then
    echo ""
    echo -e "  ${GREEN}${BOLD}All tests passed — network is healthy.${NC}"
  else
    echo ""
    echo -e "  ${RED}${BOLD}$FAIL test(s) failed — review above for the failing layer.${NC}"
    echo ""
    echo "  Diagnostic guide:"
    echo "    See section 12 above for the full diagnosis decision table."
  fi
fi

exit $(( FAIL > 0 ? 1 : 0 ))
