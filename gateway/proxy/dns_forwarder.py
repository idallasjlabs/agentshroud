"""
AgentShroud DNS Forwarder — Lightweight DNS proxy for gateway container.

Routes all DNS queries from pihole through the gateway, providing:
  - Complete audit trail of every DNS query
  - Single egress point for all container traffic
  - Domain-level logging before resolution

Architecture:
  Pihole (172.21.0.10) → Gateway DNS Forwarder (:5353) → Upstream (8.8.8.8:53)

This replaces pihole's direct 8.8.8.8/8.8.4.4 upstream with a gateway-proxied
path. Every query is logged with timestamp, source, domain, query type, and
response code.

No external dependencies — uses only Python standard library.

Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""

import asyncio
import logging
import socket
import struct
import time
from typing import Optional, Tuple

try:
    from .dns_blocklist import DNSBlocklist
except ImportError:
    DNSBlocklist = None

logger = logging.getLogger("agentshroud.dns_forwarder")

# ── Configuration ────────────────────────────────────────────────────────────
LISTEN_HOST = "0.0.0.0"
LISTEN_PORT = 5353
UPSTREAM_DNS = [("8.8.8.8", 53), ("8.8.4.4", 53)]
UPSTREAM_TIMEOUT = 5.0
MAX_PACKET_SIZE = 4096

# DNS query types
QTYPES = {
    1: "A", 2: "NS", 5: "CNAME", 6: "SOA", 12: "PTR", 15: "MX",
    16: "TXT", 28: "AAAA", 33: "SRV", 35: "NAPTR", 43: "DS",
    46: "RRSIG", 47: "NSEC", 48: "DNSKEY", 65: "HTTPS", 255: "ANY",
}

# DNS response codes
RCODES = {
    0: "NOERROR", 1: "FORMERR", 2: "SERVFAIL", 3: "NXDOMAIN",
    4: "NOTIMP", 5: "REFUSED",
}


def parse_domain_name(data: bytes, offset: int) -> Tuple[str, int]:
    """Parse a DNS domain name from wire format, handling compression pointers."""
    labels = []
    original_offset = offset
    jumped = False
    max_jumps = 10  # Prevent infinite loops from malformed packets

    for _ in range(max_jumps):
        if offset >= len(data):
            break
        length = data[offset]

        if length == 0:
            offset += 1
            break
        elif (length & 0xC0) == 0xC0:
            # Compression pointer
            if not jumped:
                original_offset = offset + 2
            pointer = struct.unpack("!H", data[offset:offset + 2])[0] & 0x3FFF
            offset = pointer
            jumped = True
        else:
            offset += 1
            labels.append(data[offset:offset + length].decode("ascii", errors="replace"))
            offset += length

    domain = ".".join(labels)
    return domain, original_offset if jumped else offset


def parse_query(data: bytes) -> Optional[Tuple[str, int, int]]:
    """Extract domain name and query type from a DNS query packet.
    
    Returns: (domain, qtype, qclass) or None if parsing fails.
    """
    try:
        if len(data) < 12:
            return None

        # DNS header: ID(2) + FLAGS(2) + QDCOUNT(2) + ANCOUNT(2) + NSCOUNT(2) + ARCOUNT(2)
        qdcount = struct.unpack("!H", data[4:6])[0]
        if qdcount == 0:
            return None

        # Parse first question
        domain, offset = parse_domain_name(data, 12)
        if offset + 4 > len(data):
            return None

        qtype, qclass = struct.unpack("!HH", data[offset:offset + 4])
        return domain, qtype, qclass

    except Exception:
        return None


async def forward_query(data: bytes) -> Optional[bytes]:
    """Forward a DNS query to upstream resolvers with failover."""
    for upstream_host, upstream_port in UPSTREAM_DNS:
        try:
            # Create UDP socket for upstream
            loop = asyncio.get_event_loop()
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(UPSTREAM_TIMEOUT)

            await loop.run_in_executor(
                None, sock.sendto, data, (upstream_host, upstream_port)
            )

            response = await asyncio.wait_for(
                loop.run_in_executor(None, sock.recv, MAX_PACKET_SIZE),
                timeout=UPSTREAM_TIMEOUT,
            )

            sock.close()
            return response

        except (asyncio.TimeoutError, socket.error, OSError) as e:
            logger.warning(f"Upstream {upstream_host}:{upstream_port} failed: {e}")
            try:
                sock.close()
            except Exception:
                pass
            continue

    return None


class DNSForwarderProtocol(asyncio.DatagramProtocol):
    """UDP protocol handler for DNS forwarding with optional blocklist."""

    def __init__(self, blocklist=None):
        self.transport = None
        self.query_count = 0
        self.start_time = time.time()
        self.blocked_count = 0
        self.blocklist = blocklist

    def connection_made(self, transport):
        self.transport = transport

    def datagram_received(self, data: bytes, addr: Tuple[str, int]):
        """Handle incoming DNS query."""
        asyncio.ensure_future(self._handle_query(data, addr))

    async def _handle_query(self, data: bytes, addr: Tuple[str, int]):
        """Process a single DNS query: log, forward, respond."""
        self.query_count += 1
        source_ip, source_port = addr

        # Parse the query for logging
        parsed = parse_query(data)
        if parsed:
            domain, qtype, qclass = parsed
            qtype_name = QTYPES.get(qtype, f"TYPE{qtype}")
            logger.info(
                f"DNS query #{self.query_count} from {source_ip}:{source_port} "
                f"— {domain} {qtype_name}"
            )
        else:
            domain = "UNPARSEABLE"
            qtype_name = "?"
            logger.warning(
                f"DNS query #{self.query_count} from {source_ip}:{source_port} "
                f"— could not parse query"
            )

        # Check blocklist before forwarding
        if self.blocklist and parsed and self.blocklist.is_blocked(domain):
            self.blocked_count += 1
            logger.info(
                f"DNS BLOCKED #{self.query_count} {domain} {qtype_name} "
                f"from {source_ip} (blocklist)"
            )
            # Return 0.0.0.0 for A queries, :: for AAAA, NXDOMAIN for others
            if len(data) >= 12:
                blocked_resp = bytearray(data)
                # Set QR=1 (response), AA=1 (authoritative), RD=1
                blocked_resp[2] = 0x85
                blocked_resp[3] = 0x80  # RA=1, RCODE=0 (NOERROR)
                # Set ANCOUNT=1
                blocked_resp[6] = 0x00
                blocked_resp[7] = 0x01
                # Append answer: pointer to question name + A record 0.0.0.0
                if qtype == 1:  # A record
                    answer = b'\xc0\x0c'  # Name pointer to offset 12
                    answer += b'\x00\x01'  # Type A
                    answer += b'\x00\x01'  # Class IN
                    answer += b'\x00\x00\x00\x3c'  # TTL 60s
                    answer += b'\x00\x04'  # RDLENGTH 4
                    answer += b'\x00\x00\x00\x00'  # 0.0.0.0
                    self.transport.sendto(bytes(blocked_resp) + answer, addr)
                elif qtype == 28:  # AAAA record
                    answer = b'\xc0\x0c'
                    answer += b'\x00\x1c'  # Type AAAA
                    answer += b'\x00\x01'  # Class IN
                    answer += b'\x00\x00\x00\x3c'  # TTL 60s
                    answer += b'\x00\x10'  # RDLENGTH 16
                    answer += b'\x00' * 16  # ::
                    self.transport.sendto(bytes(blocked_resp) + answer, addr)
                else:
                    # NXDOMAIN for other types
                    blocked_resp[3] = 0x83  # RCODE=3 (NXDOMAIN)
                    blocked_resp[6] = 0x00
                    blocked_resp[7] = 0x00  # ANCOUNT=0
                    self.transport.sendto(bytes(blocked_resp), addr)
            return

        # Forward to upstream
        start = time.monotonic()
        response = await forward_query(data)
        elapsed_ms = (time.monotonic() - start) * 1000

        if response:
            # Extract response code
            if len(response) >= 4:
                flags = struct.unpack("!H", response[2:4])[0]
                rcode = flags & 0x0F
                rcode_name = RCODES.get(rcode, f"RCODE{rcode}")
            else:
                rcode_name = "?"

            logger.info(
                f"DNS response #{self.query_count} {domain} {qtype_name} "
                f"→ {rcode_name} ({elapsed_ms:.1f}ms)"
            )

            # Send response back to client
            self.transport.sendto(response, addr)
        else:
            # All upstreams failed — return SERVFAIL
            logger.error(
                f"DNS SERVFAIL #{self.query_count} {domain} {qtype_name} "
                f"— all upstreams failed ({elapsed_ms:.1f}ms)"
            )

            if len(data) >= 12:
                # Build SERVFAIL response: copy query ID, set QR=1 + RCODE=2
                servfail = bytearray(data[:12])
                servfail[2] = 0x81  # QR=1, RD=1
                servfail[3] = 0x02  # RCODE=SERVFAIL
                self.transport.sendto(bytes(servfail), addr)

    def error_received(self, exc):
        logger.error(f"DNS forwarder protocol error: {exc}")


async def start_dns_forwarder(
    host: str = LISTEN_HOST,
    port: int = LISTEN_PORT,
    blocklist: object = None,
) -> asyncio.DatagramTransport:
    """Start the DNS forwarding server with optional blocklist.

    Returns the transport for lifecycle management.
    """
    loop = asyncio.get_event_loop()
    transport, protocol = await loop.create_datagram_endpoint(
        lambda: DNSForwarderProtocol(blocklist=blocklist),
        local_addr=(host, port),
    )

    logger.info(
        f"DNS forwarder listening on {host}:{port} "
        f"→ upstream {', '.join(f'{h}:{p}' for h, p in UPSTREAM_DNS)}"
    )

    return transport


# ── Standalone mode (for testing) ────────────────────────────────────────────
if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    async def main():
        transport = await start_dns_forwarder()
        logger.info("DNS forwarder running. Press Ctrl+C to stop.")
        try:
            await asyncio.Event().wait()  # Run forever
        except asyncio.CancelledError:
            pass
        finally:
            transport.close()

    asyncio.run(main())
