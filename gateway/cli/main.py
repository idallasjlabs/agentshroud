# Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
"""agentshroud-soc — Python CLI for the AgentShroud SOC Shared Command Layer.

Usage:
    agentshroud-soc [OPTIONS] COMMAND [ARGS]

Environment variables:
    AGENTSHROUD_URL    Gateway base URL (default: http://localhost:8080)
    AGENTSHROUD_TOKEN  Bearer token (same as gateway password)

Output format:
    --format table|json|yaml   default: table for TTY, json for pipe
"""
from __future__ import annotations

import json
import os
import sys
from typing import Any, List, Optional

try:
    import click
except ImportError:
    print("click is required. Install with: pip install click", file=sys.stderr)
    sys.exit(1)

from .client import SCLClient, client_from_env


def _is_tty() -> bool:
    return sys.stdout.isatty()


def _default_format() -> str:
    return "table" if _is_tty() else "json"


def _output(data: Any, fmt: str) -> None:
    """Print data in the requested format."""
    if fmt == "json":
        click.echo(json.dumps(data, indent=2, default=str))
        return
    if fmt == "yaml":
        try:
            import yaml
            click.echo(yaml.safe_dump(data, default_flow_style=False))
        except ImportError:
            click.echo(json.dumps(data, indent=2, default=str))
        return
    # Table format — simple key:value or list of dicts
    if isinstance(data, list):
        if not data:
            click.echo("(empty)")
            return
        if isinstance(data[0], dict):
            _print_table(data)
        else:
            for item in data:
                click.echo(str(item))
    elif isinstance(data, dict):
        for k, v in data.items():
            click.echo(f"  {k}: {v}")
    else:
        click.echo(str(data))


def _print_table(rows: List[dict]) -> None:
    if not rows:
        return
    keys = list(rows[0].keys())[:8]  # Cap columns
    widths = {k: max(len(k), max(len(str(r.get(k, ""))) for r in rows)) for k in keys}
    header = "  ".join(k.upper().ljust(widths[k]) for k in keys)
    separator = "  ".join("-" * widths[k] for k in keys)
    click.echo(header)
    click.echo(separator)
    for row in rows:
        click.echo("  ".join(str(row.get(k, "")).ljust(widths[k]) for k in keys))


# ---------------------------------------------------------------------------
# CLI root
# ---------------------------------------------------------------------------

@click.group()
@click.option("--url", envvar="AGENTSHROUD_URL", default="http://localhost:8080", help="Gateway base URL")
@click.option("--token", envvar="AGENTSHROUD_TOKEN", default="", help="Bearer token")
@click.option("--format", "fmt", type=click.Choice(["table", "json", "yaml"]), default=None)
@click.pass_context
def cli(ctx, url: str, token: str, fmt: Optional[str]):
    """AgentShroud SOC CLI — Shared Command Layer."""
    ctx.ensure_object(dict)
    if not token:
        token = os.environ.get("AGENTSHROUD_GATEWAY_PASSWORD", "")
    ctx.obj["client"] = SCLClient(url, token)
    ctx.obj["fmt"] = fmt or _default_format()


# ---------------------------------------------------------------------------
# get commands
# ---------------------------------------------------------------------------

@cli.group()
def get():
    """Retrieve resources."""
    pass


@get.command("services")
@click.pass_context
def get_services(ctx):
    """List all service containers with status."""
    client: SCLClient = ctx.obj["client"]
    _output(client.get_services(), ctx.obj["fmt"])


@get.command("events")
@click.option("--severity", default=None, help="Minimum severity (low/medium/high/critical)")
@click.option("--limit", default=50, show_default=True)
@click.pass_context
def get_events(ctx, severity, limit):
    """Query recent security events."""
    client: SCLClient = ctx.obj["client"]
    _output(client.get_events(severity=severity, limit=limit), ctx.obj["fmt"])


@get.command("risk")
@click.pass_context
def get_risk(ctx):
    """Show current risk score and level."""
    client: SCLClient = ctx.obj["client"]
    _output(client.get_risk(), ctx.obj["fmt"])


@get.command("correlation")
@click.pass_context
def get_correlation(ctx):
    """Show SOC correlation summary."""
    client: SCLClient = ctx.obj["client"]
    _output(client.get_correlation(), ctx.obj["fmt"])


@get.command("health")
@click.pass_context
def get_health(ctx):
    """Aggregate health report."""
    client: SCLClient = ctx.obj["client"]
    _output(client.get_health(), ctx.obj["fmt"])


@get.command("users")
@click.pass_context
def get_users(ctx):
    """List all contributors with roles and groups."""
    client: SCLClient = ctx.obj["client"]
    _output(client.get_users(), ctx.obj["fmt"])


@get.command("groups")
@click.pass_context
def get_groups(ctx):
    """List team groups."""
    client: SCLClient = ctx.obj["client"]
    _output(client.get_groups(), ctx.obj["fmt"])


@get.command("egress-pending")
@click.pass_context
def get_egress_pending(ctx):
    """Show pending egress approval requests."""
    client: SCLClient = ctx.obj["client"]
    _output(client.get_egress_pending(), ctx.obj["fmt"])


@get.command("logs")
@click.argument("service")
@click.option("--tail", default=50, show_default=True)
@click.pass_context
def get_logs(ctx, service, tail):
    """Get container logs for a service."""
    client: SCLClient = ctx.obj["client"]
    result = client.get_logs(service, tail=tail)
    lines = result.get("lines", []) if isinstance(result, dict) else []
    for line in lines:
        click.echo(line)


# ---------------------------------------------------------------------------
# restart / stop / start
# ---------------------------------------------------------------------------

@cli.group()
def restart():
    """Restart a service."""
    pass


@restart.command("service")
@click.argument("name")
@click.option("--confirm", is_flag=True, default=False)
@click.pass_context
def restart_service(ctx, name, confirm):
    """Restart a service container."""
    client: SCLClient = ctx.obj["client"]
    result = client.restart_service(name, confirm=confirm)
    if isinstance(result, dict) and result.get("code") == "CONFIRMATION_REQUIRED":
        click.echo(f"Confirmation required: {result.get('message')}")
        click.echo(f"Re-run with --confirm to proceed.")
    else:
        _output(result, ctx.obj["fmt"])


@cli.group()
def stop():
    """Stop a service."""
    pass


@stop.command("service")
@click.argument("name")
@click.option("--confirm", is_flag=True, default=False)
@click.pass_context
def stop_service(ctx, name, confirm):
    """Stop a service container."""
    client: SCLClient = ctx.obj["client"]
    result = client.stop_service(name, confirm=confirm)
    if isinstance(result, dict) and result.get("code") == "CONFIRMATION_REQUIRED":
        click.echo(f"Confirmation required. Re-run with --confirm.")
    else:
        _output(result, ctx.obj["fmt"])


# ---------------------------------------------------------------------------
# approve / deny
# ---------------------------------------------------------------------------

@cli.command("approve")
@click.argument("target")
@click.pass_context
def approve(ctx, target):
    """Approve an egress request by ID."""
    client: SCLClient = ctx.obj["client"]
    _output(client.approve_egress(target), ctx.obj["fmt"])


@cli.command("deny")
@click.argument("target")
@click.pass_context
def deny(ctx, target):
    """Deny an egress request by ID."""
    client: SCLClient = ctx.obj["client"]
    _output(client.deny_egress(target), ctx.obj["fmt"])


# ---------------------------------------------------------------------------
# add / remove
# ---------------------------------------------------------------------------

@cli.group()
def add():
    """Add resources."""
    pass


@add.command("collaborator")
@click.argument("user_id")
@click.pass_context
def add_collaborator(ctx, user_id):
    """Add a collaborator by Telegram user ID."""
    client: SCLClient = ctx.obj["client"]
    _output(client.add_collaborator(user_id), ctx.obj["fmt"])


@add.command("group-member")
@click.argument("group_id")
@click.argument("user_id")
@click.pass_context
def add_group_member(ctx, group_id, user_id):
    """Add a user to a group."""
    client: SCLClient = ctx.obj["client"]
    _output(client.add_group_member(group_id, user_id), ctx.obj["fmt"])


# ---------------------------------------------------------------------------
# set
# ---------------------------------------------------------------------------

@cli.group()
def set():
    """Set configuration values."""
    pass


@set.command("mode")
@click.argument("group_id")
@click.argument("mode", type=click.Choice(["local_only", "project_scoped", "full_access"]))
@click.pass_context
def set_mode(ctx, group_id, mode):
    """Set collaboration mode for a group."""
    client: SCLClient = ctx.obj["client"]
    _output(client.set_group_mode(group_id, mode), ctx.obj["fmt"])


# ---------------------------------------------------------------------------
# Emergency operations
# ---------------------------------------------------------------------------

@cli.command()
@click.option("--confirm", is_flag=True, default=False)
@click.pass_context
def freeze(ctx, confirm):
    """Emergency freeze: pause all bot containers."""
    client: SCLClient = ctx.obj["client"]
    result = client.freeze(confirm=confirm)
    if isinstance(result, dict) and result.get("code") == "CONFIRMATION_REQUIRED":
        click.echo("Confirmation required. Re-run with --confirm.")
    else:
        _output(result, ctx.obj["fmt"])


@cli.command()
@click.argument("scanner", type=click.Choice(["trivy", "clamav", "openscap", "all"]))
@click.pass_context
def scan(ctx, scanner):
    """Trigger a security scan."""
    client: SCLClient = ctx.obj["client"]
    _output(client.run_scan(scanner), ctx.obj["fmt"])


# ---------------------------------------------------------------------------
# Live streaming (WebSocket tail)
# ---------------------------------------------------------------------------

@cli.command("tail")
@click.argument("stream", type=click.Choice(["events", "logs"]))
@click.argument("target", default="")
@click.option("--severity", default=None)
@click.option("--url", envvar="AGENTSHROUD_URL", default="http://localhost:8080")
@click.option("--token", envvar="AGENTSHROUD_TOKEN", default="")
@click.pass_context
def tail(ctx, stream, target, severity, url, token):
    """Stream real-time events or logs via WebSocket."""
    if not token:
        token = ctx.obj.get("client", SCLClient(url, "")).token
    click.echo(f"Connecting to {url}/soc/v1/ws ... (Ctrl-C to stop)")
    try:
        import asyncio
        asyncio.run(_tail_ws(url, token, stream, target, severity))
    except KeyboardInterrupt:
        click.echo("\nDisconnected.")
    except ImportError:
        click.echo("asyncio required for streaming.")


async def _tail_ws(url, token, stream, target, severity):
    try:
        import websockets
    except ImportError:
        print("websockets package required: pip install websockets")
        return
    ws_url = url.replace("http://", "ws://").replace("https://", "wss://")
    ws_url = f"{ws_url}/soc/v1/ws?token={token}"
    async with websockets.connect(ws_url) as ws:
        filter_types = ["security_event"] if stream == "events" else ["log_event"]
        await ws.send(json.dumps({"subscribe": filter_types}))
        async for message in ws:
            try:
                ev = json.loads(message)
                if ev.get("type") == "keepalive":
                    continue
                summary = ev.get("summary", "")
                sev = ev.get("severity", "info")
                ts = ev.get("timestamp", "")[:19]
                click.echo(f"[{ts}] [{sev.upper():8s}] {summary}")
            except Exception:
                click.echo(message)


def main():
    cli(auto_envvar_prefix="AGENTSHROUD")


if __name__ == "__main__":
    main()
