// Copyright © 2026 Isaiah Dallas Jefferson, Jr. AgentShroud™. All rights reserved.
//! agentshroud-soc — Rust CLI for the AgentShroud SOC Shared Command Layer (v1.0.0 target).
//!
//! v0.9.0: Python CLI is the shipped implementation (gateway/cli/main.py).
//! This crate provides feature-parity by v1.0.0 with performance improvements.
//!
//! Usage:
//!   agentshroud-soc get services
//!   agentshroud-soc restart service bot --confirm
//!   agentshroud-soc tail events --severity HIGH
//!   agentshroud-soc freeze --confirm
//!
//! Command Center (SCRUM-94):
//!   agentshroud-soc status                     # gateway health + version
//!   agentshroud-soc approvals list             # pending high-risk approvals
//!   agentshroud-soc approvals approve <id>     # approve a pending action
//!   agentshroud-soc approvals deny <id>        # deny a pending action
//!   agentshroud-soc cves                       # agent CVE registry summary
//!   agentshroud-soc deploy-status              # version + service deploy state

use anyhow::Result;
use clap::{Parser, Subcommand, ValueEnum};
use std::env;

/// AgentShroud SOC CLI
#[derive(Parser)]
#[command(
    name = "agentshroud-soc",
    version = "1.0.0",
    about = "AgentShroud SOC Shared Command Layer"
)]
struct Cli {
    /// Gateway base URL
    #[arg(long, env = "AGENTSHROUD_URL", default_value = "http://localhost:8080")]
    url: String,

    /// Bearer token (gateway password)
    #[arg(long, env = "AGENTSHROUD_TOKEN", default_value = "")]
    token: String,

    /// Output format
    #[arg(long, value_enum, default_value = "table")]
    format: OutputFormat,

    #[command(subcommand)]
    command: Commands,
}

#[derive(Clone, ValueEnum)]
enum OutputFormat {
    Table,
    Json,
    Yaml,
}

#[derive(Subcommand)]
enum Commands {
    /// Retrieve resources
    Get {
        #[command(subcommand)]
        resource: GetResource,
    },
    /// Restart a service
    Restart {
        #[command(subcommand)]
        target: ServiceTarget,
    },
    /// Stop a service
    Stop {
        #[command(subcommand)]
        target: ServiceTarget,
    },
    /// Approve an egress request
    Approve { id: String },
    /// Deny an egress request
    Deny { id: String },
    /// Add resources
    Add {
        #[command(subcommand)]
        resource: AddResource,
    },
    /// Set configuration
    Set {
        #[command(subcommand)]
        target: SetTarget,
    },
    /// Emergency freeze: pause all bot containers
    Freeze {
        #[arg(long)]
        confirm: bool,
    },
    /// Run a security scan
    Scan { scanner: String },
    /// Stream real-time events or logs
    Tail {
        stream: String,
        #[arg(default_value = "")]
        target: String,
        #[arg(long)]
        severity: Option<String>,
    },

    // ---- Command Center (SCRUM-94) ----
    /// Gateway health + version (command center)
    Status,
    /// Manage the human-in-the-loop approval queue (command center)
    Approvals {
        #[command(subcommand)]
        action: ApprovalAction,
    },
    /// Agent CVE registry summary (command center)
    Cves {
        /// Bot identifier (defaults to gateway's registered agent)
        #[arg(long)]
        bot_id: Option<String>,
    },
    /// Version + service deploy state (command center)
    DeployStatus,
}

#[derive(Subcommand)]
enum ApprovalAction {
    /// List pending approval requests
    List,
    /// Approve a pending request by id
    Approve {
        id: String,
        #[arg(long, default_value = "")]
        reason: String,
    },
    /// Deny a pending request by id
    Deny {
        id: String,
        #[arg(long, default_value = "")]
        reason: String,
    },
}

#[derive(Subcommand)]
enum GetResource {
    Services,
    Events {
        #[arg(long)]
        severity: Option<String>,
        #[arg(long, default_value = "50")]
        limit: u32,
    },
    Risk,
    Correlation,
    Health,
    Users,
    Groups,
    EgressPending,
    Logs {
        service: String,
        #[arg(long, default_value = "50")]
        tail: u32,
    },
}

#[derive(Subcommand)]
enum ServiceTarget {
    Service {
        name: String,
        #[arg(long)]
        confirm: bool,
    },
}

#[derive(Subcommand)]
enum AddResource {
    Collaborator { user_id: String },
    GroupMember { group_id: String, user_id: String },
}

#[derive(Subcommand)]
enum SetTarget {
    Mode {
        group_id: String,
        #[arg(value_enum)]
        mode: CollabMode,
    },
    Role {
        user_id: String,
        role: String,
    },
}

#[derive(Clone, ValueEnum)]
enum CollabMode {
    LocalOnly,
    ProjectScoped,
    FullAccess,
}

impl std::fmt::Display for CollabMode {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            CollabMode::LocalOnly => write!(f, "local_only"),
            CollabMode::ProjectScoped => write!(f, "project_scoped"),
            CollabMode::FullAccess => write!(f, "full_access"),
        }
    }
}

// ---------------------------------------------------------------------------
// HTTP transport abstraction
// ---------------------------------------------------------------------------

/// HTTP verb for a gateway call. Kept minimal — the command center only issues
/// GET and POST requests against the gateway REST surface.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Method {
    Get,
    Post,
}

/// A raw HTTP response from the gateway: status code + body text.
#[derive(Debug, Clone)]
pub struct HttpResponse {
    pub status: u16,
    pub body: String,
}

/// Transport seam so command logic can be unit-tested against a fake gateway
/// without any real network I/O.
pub trait HttpTransport {
    fn request(
        &self,
        method: Method,
        url: &str,
        token: &str,
        body: Option<&serde_json::Value>,
    ) -> Result<HttpResponse>;
}

/// Production transport backed by `reqwest`'s blocking client.
struct ReqwestTransport {
    client: reqwest::blocking::Client,
}

impl ReqwestTransport {
    fn new() -> Self {
        Self {
            client: reqwest::blocking::Client::new(),
        }
    }
}

impl HttpTransport for ReqwestTransport {
    fn request(
        &self,
        method: Method,
        url: &str,
        token: &str,
        body: Option<&serde_json::Value>,
    ) -> Result<HttpResponse> {
        let mut req = match method {
            Method::Get => self.client.get(url),
            Method::Post => self.client.post(url),
        };
        if !token.is_empty() {
            req = req.bearer_auth(token);
        }
        if let Some(b) = body {
            req = req.json(b);
        }
        let resp = req.send()?;
        let status = resp.status().as_u16();
        let text = resp.text()?;
        Ok(HttpResponse { status, body: text })
    }
}

// ---------------------------------------------------------------------------
// Gateway client (command center) — talks to the gateway REST root
// ---------------------------------------------------------------------------

/// Join a gateway base URL with an absolute API path, tolerating trailing/leading
/// slashes. Pure so it can be unit-tested.
pub fn build_url(base_url: &str, path: &str) -> String {
    format!(
        "{}/{}",
        base_url.trim_end_matches('/'),
        path.trim_start_matches('/')
    )
}

/// Map a non-2xx HTTP status into a human-readable command-center error message.
/// Returns `None` for success (2xx). Pure so it can be unit-tested.
pub fn map_http_error(status: u16, body: &str) -> Option<String> {
    if (200..300).contains(&status) {
        return None;
    }
    let detail = serde_json::from_str::<serde_json::Value>(body)
        .ok()
        .and_then(|v| v.get("detail").and_then(|d| d.as_str()).map(str::to_string))
        .unwrap_or_default();
    let msg = match status {
        401 => {
            "authentication failed (401): check AGENTSHROUD_TOKEN / gateway password".to_string()
        }
        403 => "forbidden (403): token lacks permission for this action".to_string(),
        404 => "not found (404): resource or request id does not exist".to_string(),
        409 => "conflict (409): approval state changed — refresh and retry".to_string(),
        _ => format!("gateway returned HTTP {status}"),
    };
    if detail.is_empty() {
        Some(msg)
    } else {
        Some(format!("{msg}: {detail}"))
    }
}

/// A client that speaks to the gateway REST root (not the `/soc/v1` sub-API).
/// Generic over the transport so tests inject a fake.
pub struct GatewayClient<T: HttpTransport> {
    base_url: String,
    token: String,
    transport: T,
}

impl<T: HttpTransport> GatewayClient<T> {
    pub fn new(base_url: &str, token: &str, transport: T) -> Self {
        Self {
            base_url: base_url.trim_end_matches('/').to_string(),
            token: token.to_string(),
            transport,
        }
    }

    /// GET an absolute gateway path, returning parsed JSON or a mapped error.
    pub fn get(&self, path: &str) -> Result<serde_json::Value> {
        let url = build_url(&self.base_url, path);
        let resp = self
            .transport
            .request(Method::Get, &url, &self.token, None)?;
        if let Some(err) = map_http_error(resp.status, &resp.body) {
            anyhow::bail!(err);
        }
        Ok(serde_json::from_str(&resp.body).unwrap_or(serde_json::Value::Null))
    }

    /// POST JSON to an absolute gateway path, returning parsed JSON or a mapped error.
    pub fn post(&self, path: &str, body: Option<serde_json::Value>) -> Result<serde_json::Value> {
        let url = build_url(&self.base_url, path);
        let resp = self
            .transport
            .request(Method::Post, &url, &self.token, body.as_ref())?;
        if let Some(err) = map_http_error(resp.status, &resp.body) {
            anyhow::bail!(err);
        }
        Ok(serde_json::from_str(&resp.body).unwrap_or(serde_json::Value::Null))
    }
}

// ---------------------------------------------------------------------------
// Command center formatting (pure functions — unit tested)
// ---------------------------------------------------------------------------

fn json_str(v: &serde_json::Value, key: &str) -> String {
    v.get(key)
        .and_then(|x| x.as_str())
        .map(str::to_string)
        .unwrap_or_else(|| "unknown".to_string())
}

/// Format the `/status` payload into a compact status line.
pub fn format_status(v: &serde_json::Value) -> String {
    let status = json_str(v, "status");
    let version = json_str(v, "version");
    format!("gateway: {status}  version: {version}")
}

/// Format a list of pending approvals into a table. Accepts either a JSON array
/// or a single object; renders "No pending approvals." when empty.
pub fn format_approvals(v: &serde_json::Value) -> String {
    let items: Vec<serde_json::Value> = match v {
        serde_json::Value::Array(a) => a.clone(),
        serde_json::Value::Null => vec![],
        other => vec![other.clone()],
    };
    if items.is_empty() {
        return "No pending approvals.".to_string();
    }
    let mut out = String::from(
        "ID                                    ACTION            AGENT       DESCRIPTION\n",
    );
    for item in &items {
        let id = json_str(item, "request_id");
        let action = json_str(item, "action_type");
        let agent = json_str(item, "agent_id");
        let desc = json_str(item, "description");
        out.push_str(&format!("{id:<38}{action:<18}{agent:<12}{desc}\n"));
    }
    out.trim_end().to_string()
}

/// Format an approval decision result.
pub fn format_decision(v: &serde_json::Value, approved: bool) -> String {
    let id = json_str(v, "request_id");
    let status = json_str(v, "status");
    let verb = if approved { "approved" } else { "denied" };
    format!("Request {id} {verb} (status: {status})")
}

/// Format the CVE registry summary. Handles the `{"error": "..."}` shape the
/// gateway returns for an unknown bot id.
pub fn format_cves(v: &serde_json::Value) -> String {
    if let Some(err) = v.get("error").and_then(|e| e.as_str()) {
        return format!("CVE registry error: {err}");
    }
    let total = v
        .get("total")
        .and_then(|t| t.as_u64())
        .or_else(|| {
            v.get("cves")
                .and_then(|c| c.as_array())
                .map(|a| a.len() as u64)
        })
        .unwrap_or(0);
    let mut counts: Vec<(String, u64)> = Vec::new();
    for key in ["fully_mitigated", "partially_mitigated", "not_mitigated"] {
        if let Some(n) = v.get(key).and_then(|x| x.as_u64()) {
            counts.push((key.to_string(), n));
        }
    }
    let mut out = format!("CVE registry: {total} tracked");
    if !counts.is_empty() {
        let parts: Vec<String> = counts.iter().map(|(k, n)| format!("{k}={n}")).collect();
        out.push_str(&format!("  ({})", parts.join(", ")));
    }
    out
}

/// Format the deploy-status view from a `/api/v1/versions/current` payload plus
/// an optional `/soc/v1/services` list.
pub fn format_deploy_status(version: &serde_json::Value, services: &serde_json::Value) -> String {
    let current = version
        .get("version")
        .and_then(|x| x.as_str())
        .unwrap_or("unknown");
    let mut out = format!("deployed version: {current}\n");
    let svc_list: Vec<serde_json::Value> = match services {
        serde_json::Value::Array(a) => a.clone(),
        _ => vec![],
    };
    if svc_list.is_empty() {
        out.push_str("services: (none reported)");
    } else {
        out.push_str("services:\n");
        for s in &svc_list {
            let name = json_str(s, "name");
            let status = json_str(s, "status");
            out.push_str(&format!("  {name:<20} {status}\n"));
        }
        out = out.trim_end().to_string();
    }
    out
}

// ---------------------------------------------------------------------------
// SOC HTTP client (existing /soc/v1 sub-API)
// ---------------------------------------------------------------------------

struct SclClient {
    base_url: String,
    token: String,
    client: reqwest::blocking::Client,
}

impl SclClient {
    fn new(base_url: &str, token: &str) -> Self {
        Self {
            base_url: format!("{}/soc/v1", base_url.trim_end_matches('/')),
            token: token.to_string(),
            client: reqwest::blocking::Client::new(),
        }
    }

    fn get(&self, path: &str) -> Result<serde_json::Value> {
        let url = format!("{}/{}", self.base_url, path.trim_start_matches('/'));
        let resp = self.client.get(&url).bearer_auth(&self.token).send()?;
        Ok(resp.json()?)
    }

    fn post(&self, path: &str, body: Option<serde_json::Value>) -> Result<serde_json::Value> {
        let url = format!("{}/{}", self.base_url, path.trim_start_matches('/'));
        let mut req = self.client.post(&url).bearer_auth(&self.token);
        if let Some(b) = body {
            req = req.json(&b);
        }
        Ok(req.send()?.json()?)
    }
}

// ---------------------------------------------------------------------------
// Output helpers
// ---------------------------------------------------------------------------

fn print_output(data: &serde_json::Value, fmt: &OutputFormat) {
    match fmt {
        OutputFormat::Json => {
            println!("{}", serde_json::to_string_pretty(data).unwrap_or_default())
        }
        OutputFormat::Yaml => {
            // Fallback to JSON if serde_yaml not available
            println!("{}", serde_json::to_string_pretty(data).unwrap_or_default());
        }
        OutputFormat::Table => match data {
            serde_json::Value::Array(arr) => {
                for item in arr {
                    println!("{}", serde_json::to_string_pretty(item).unwrap_or_default());
                    println!("---");
                }
            }
            _ => println!("{}", serde_json::to_string_pretty(data).unwrap_or_default()),
        },
    }
}

/// Resolve the effective bearer token: explicit --token/env wins, else fall back
/// to the gateway password env var. Pure so it can be unit-tested.
pub fn resolve_token(cli_token: &str, env_password: Option<&str>) -> String {
    if !cli_token.is_empty() {
        cli_token.to_string()
    } else {
        env_password.unwrap_or("").to_string()
    }
}

// ---------------------------------------------------------------------------
// Command center dispatch (pure over transport — unit tested)
// ---------------------------------------------------------------------------

/// Run the `status` command against a gateway client. Returns display text.
pub fn run_status<T: HttpTransport>(client: &GatewayClient<T>) -> Result<String> {
    let data = client.get("/status")?;
    Ok(format_status(&data))
}

/// Run `approvals list`.
pub fn run_approvals_list<T: HttpTransport>(client: &GatewayClient<T>) -> Result<String> {
    let data = client.get("/approve/pending")?;
    Ok(format_approvals(&data))
}

/// Run `approvals approve <id>` / `approvals deny <id>`.
pub fn run_approvals_decide<T: HttpTransport>(
    client: &GatewayClient<T>,
    id: &str,
    approved: bool,
    reason: &str,
) -> Result<String> {
    let body = serde_json::json!({
        "request_id": id,
        "approved": approved,
        "reason": reason,
    });
    let data = client.post(&format!("/approve/{id}/decide"), Some(body))?;
    Ok(format_decision(&data, approved))
}

/// Run `cves`.
pub fn run_cves<T: HttpTransport>(
    client: &GatewayClient<T>,
    bot_id: Option<&str>,
) -> Result<String> {
    let path = match bot_id {
        Some(b) => format!("/soc/v1/agent-cves?bot_id={b}"),
        None => "/soc/v1/agent-cves".to_string(),
    };
    let data = client.get(&path)?;
    Ok(format_cves(&data))
}

/// Run `deploy-status`.
pub fn run_deploy_status<T: HttpTransport>(client: &GatewayClient<T>) -> Result<String> {
    let version = client.get("/api/v1/versions/current")?;
    // Services are best-effort: a missing/failed services call should not sink the
    // whole command, so treat an error as "no services reported".
    let services = client
        .get("/soc/v1/services")
        .unwrap_or(serde_json::Value::Null);
    Ok(format_deploy_status(&version, &services))
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

fn main() -> Result<()> {
    let cli = Cli::parse();

    let token = resolve_token(
        &cli.token,
        env::var("AGENTSHROUD_GATEWAY_PASSWORD").ok().as_deref(),
    );

    let fmt = &cli.format;

    // Command-center subcommands use the gateway REST root client; everything
    // else uses the existing /soc/v1 SclClient.
    match cli.command {
        Commands::Status => {
            let gw = GatewayClient::new(&cli.url, &token, ReqwestTransport::new());
            println!("{}", run_status(&gw)?);
            return Ok(());
        }
        Commands::Approvals { ref action } => {
            let gw = GatewayClient::new(&cli.url, &token, ReqwestTransport::new());
            let out = match action {
                ApprovalAction::List => run_approvals_list(&gw)?,
                ApprovalAction::Approve { id, reason } => {
                    run_approvals_decide(&gw, id, true, reason)?
                }
                ApprovalAction::Deny { id, reason } => {
                    run_approvals_decide(&gw, id, false, reason)?
                }
            };
            println!("{out}");
            return Ok(());
        }
        Commands::Cves { ref bot_id } => {
            let gw = GatewayClient::new(&cli.url, &token, ReqwestTransport::new());
            println!("{}", run_cves(&gw, bot_id.as_deref())?);
            return Ok(());
        }
        Commands::DeployStatus => {
            let gw = GatewayClient::new(&cli.url, &token, ReqwestTransport::new());
            println!("{}", run_deploy_status(&gw)?);
            return Ok(());
        }
        _ => {}
    }

    let client = SclClient::new(&cli.url, &token);

    match cli.command {
        Commands::Get { resource } => match resource {
            GetResource::Services => {
                let data = client.get("/services")?;
                print_output(&data, fmt);
            }
            GetResource::Events { severity, limit } => {
                let path = format!(
                    "/security/events?limit={}{}",
                    limit,
                    severity
                        .map(|s| format!("&severity={}", s))
                        .unwrap_or_default()
                );
                let data = client.get(&path)?;
                print_output(&data, fmt);
            }
            GetResource::Risk => {
                let data = client.get("/security/risk")?;
                print_output(&data, fmt);
            }
            GetResource::Correlation => {
                let data = client.get("/security/correlation")?;
                print_output(&data, fmt);
            }
            GetResource::Health => {
                let data = client.get("/health")?;
                print_output(&data, fmt);
            }
            GetResource::Users => {
                let data = client.get("/users")?;
                print_output(&data, fmt);
            }
            GetResource::Groups => {
                let data = client.get("/groups")?;
                print_output(&data, fmt);
            }
            GetResource::EgressPending => {
                let data = client.get("/egress/pending")?;
                print_output(&data, fmt);
            }
            GetResource::Logs { service, tail } => {
                let path = format!("/services/{}/logs?tail={}", service, tail);
                let data = client.get(&path)?;
                if let Some(lines) = data.get("lines").and_then(|l| l.as_array()) {
                    for line in lines {
                        println!("{}", line.as_str().unwrap_or(""));
                    }
                }
            }
        },
        Commands::Restart { target } => match target {
            ServiceTarget::Service { name, confirm } => {
                if !confirm {
                    eprintln!("Confirmation required. Re-run with --confirm.");
                    std::process::exit(1);
                }
                let data = client.post(
                    &format!("/services/{}/restart", name),
                    Some(serde_json::json!({"confirm": true})),
                )?;
                print_output(&data, fmt);
            }
        },
        Commands::Stop { target } => match target {
            ServiceTarget::Service { name, confirm } => {
                if !confirm {
                    eprintln!("Confirmation required. Re-run with --confirm.");
                    std::process::exit(1);
                }
                let data = client.post(
                    &format!("/services/{}/stop", name),
                    Some(serde_json::json!({"confirm": true})),
                )?;
                print_output(&data, fmt);
            }
        },
        Commands::Approve { id } => {
            let data = client.post(&format!("/egress/{}/approve", id), None)?;
            print_output(&data, fmt);
        }
        Commands::Deny { id } => {
            let data = client.post(&format!("/egress/{}/deny", id), None)?;
            print_output(&data, fmt);
        }
        Commands::Add { resource } => match resource {
            AddResource::Collaborator { user_id } => {
                let data = client.post(
                    "/users/collaborator",
                    Some(serde_json::json!({"user_id": user_id})),
                )?;
                print_output(&data, fmt);
            }
            AddResource::GroupMember { group_id, user_id } => {
                let data = client.post(
                    &format!("/groups/{}/members", group_id),
                    Some(serde_json::json!({"user_id": user_id})),
                )?;
                print_output(&data, fmt);
            }
        },
        Commands::Set { target } => match target {
            SetTarget::Mode { group_id, mode } => {
                let data = client.post(
                    &format!("/groups/{}/mode", group_id),
                    Some(serde_json::json!({"collab_mode": mode.to_string()})),
                )?;
                print_output(&data, fmt);
            }
            SetTarget::Role { user_id, role } => {
                let data = client.post(
                    &format!("/users/{}/role", user_id),
                    Some(serde_json::json!({"role": role})),
                )?;
                print_output(&data, fmt);
            }
        },
        Commands::Freeze { confirm } => {
            if !confirm {
                eprintln!("Confirmation required. Re-run with --confirm.");
                std::process::exit(1);
            }
            let data = client.post(
                "/killswitch/freeze",
                Some(serde_json::json!({"confirm": true})),
            )?;
            print_output(&data, fmt);
        }
        Commands::Scan { scanner } => {
            let data = client.post(
                &format!("/scan/{}", scanner),
                Some(serde_json::json!({"confirm": true})),
            )?;
            print_output(&data, fmt);
        }
        Commands::Tail {
            stream,
            target: _,
            severity: _,
        } => {
            eprintln!("WebSocket tail not yet implemented in Rust CLI. Use Python CLI: agentshroud-soc tail {}", stream);
            std::process::exit(1);
        }

        // Command-center variants handled above; unreachable here.
        Commands::Status
        | Commands::Approvals { .. }
        | Commands::Cves { .. }
        | Commands::DeployStatus => unreachable!("handled in command-center dispatch"),
    }

    Ok(())
}

// ---------------------------------------------------------------------------
// Tests
// ---------------------------------------------------------------------------

#[cfg(test)]
mod tests {
    use super::*;
    use std::cell::RefCell;

    /// A fake transport that records requests and returns scripted responses.
    /// No real network I/O — satisfies the TDD "inject a fake HTTP client" rule.
    struct FakeTransport {
        response: HttpResponse,
        calls: RefCell<Vec<(Method, String, Option<serde_json::Value>)>>,
    }

    impl FakeTransport {
        fn ok(body: &str) -> Self {
            Self {
                response: HttpResponse {
                    status: 200,
                    body: body.to_string(),
                },
                calls: RefCell::new(Vec::new()),
            }
        }

        fn with(status: u16, body: &str) -> Self {
            Self {
                response: HttpResponse {
                    status,
                    body: body.to_string(),
                },
                calls: RefCell::new(Vec::new()),
            }
        }
    }

    impl HttpTransport for FakeTransport {
        fn request(
            &self,
            method: Method,
            url: &str,
            _token: &str,
            body: Option<&serde_json::Value>,
        ) -> Result<HttpResponse> {
            self.calls
                .borrow_mut()
                .push((method, url.to_string(), body.cloned()));
            Ok(self.response.clone())
        }
    }

    // ---- build_url ----

    #[test]
    fn build_url_trims_slashes() {
        assert_eq!(
            build_url("http://gw:8080/", "/status"),
            "http://gw:8080/status"
        );
        assert_eq!(
            build_url("http://gw:8080", "status"),
            "http://gw:8080/status"
        );
    }

    // ---- map_http_error ----

    #[test]
    fn map_http_error_none_on_success() {
        assert!(map_http_error(200, "{}").is_none());
        assert!(map_http_error(204, "").is_none());
    }

    #[test]
    fn map_http_error_401_message() {
        let msg = map_http_error(401, "").unwrap();
        assert!(msg.contains("authentication failed"));
        assert!(msg.contains("401"));
    }

    #[test]
    fn map_http_error_includes_detail() {
        let msg = map_http_error(404, r#"{"detail":"Approval request not found"}"#).unwrap();
        assert!(msg.contains("404"));
        assert!(msg.contains("Approval request not found"));
    }

    #[test]
    fn map_http_error_generic_status() {
        let msg = map_http_error(500, "boom").unwrap();
        assert!(msg.contains("HTTP 500"));
    }

    // ---- resolve_token ----

    #[test]
    fn resolve_token_prefers_cli() {
        assert_eq!(resolve_token("cli-tok", Some("env-tok")), "cli-tok");
    }

    #[test]
    fn resolve_token_falls_back_to_env() {
        assert_eq!(resolve_token("", Some("env-tok")), "env-tok");
    }

    #[test]
    fn resolve_token_empty_when_none() {
        assert_eq!(resolve_token("", None), "");
    }

    // ---- status ----

    #[test]
    fn status_parses_and_formats() {
        let t = FakeTransport::ok(r#"{"status":"healthy","version":"1.0.0"}"#);
        let gw = GatewayClient::new("http://gw:8080", "tok", t);
        let out = run_status(&gw).unwrap();
        assert_eq!(out, "gateway: healthy  version: 1.0.0");
    }

    #[test]
    fn status_hits_correct_path() {
        let t = FakeTransport::ok(r#"{"status":"healthy","version":"1.0.0"}"#);
        let gw = GatewayClient::new("http://gw:8080", "tok", t);
        run_status(&gw).unwrap();
        let calls = gw.transport.calls.borrow();
        assert_eq!(calls.len(), 1);
        assert_eq!(calls[0].0, Method::Get);
        assert_eq!(calls[0].1, "http://gw:8080/status");
    }

    #[test]
    fn status_errors_when_gateway_down() {
        let t = FakeTransport::with(503, r#"{"detail":"service unavailable"}"#);
        let gw = GatewayClient::new("http://gw:8080", "tok", t);
        let err = run_status(&gw).unwrap_err().to_string();
        assert!(err.contains("HTTP 503"));
        assert!(err.contains("service unavailable"));
    }

    #[test]
    fn status_errors_on_401() {
        let t = FakeTransport::with(401, "");
        let gw = GatewayClient::new("http://gw:8080", "tok", t);
        let err = run_status(&gw).unwrap_err().to_string();
        assert!(err.contains("authentication failed"));
    }

    // ---- approvals list ----

    #[test]
    fn approvals_list_formats_rows() {
        let body = r#"[
            {"request_id":"abc-1","action_type":"email_sending","agent_id":"openclaw","description":"send report"},
            {"request_id":"abc-2","action_type":"file_deletion","agent_id":"hermes","description":"rm old.log"}
        ]"#;
        let t = FakeTransport::ok(body);
        let gw = GatewayClient::new("http://gw:8080", "tok", t);
        let out = run_approvals_list(&gw).unwrap();
        assert!(out.contains("abc-1"));
        assert!(out.contains("email_sending"));
        assert!(out.contains("rm old.log"));
        let calls = gw.transport.calls.borrow();
        assert_eq!(calls[0].1, "http://gw:8080/approve/pending");
    }

    #[test]
    fn approvals_list_empty() {
        let t = FakeTransport::ok("[]");
        let gw = GatewayClient::new("http://gw:8080", "tok", t);
        let out = run_approvals_list(&gw).unwrap();
        assert_eq!(out, "No pending approvals.");
    }

    #[test]
    fn approvals_list_errors_on_401() {
        let t = FakeTransport::with(401, "");
        let gw = GatewayClient::new("http://gw:8080", "tok", t);
        assert!(run_approvals_list(&gw).is_err());
    }

    // ---- approvals decide ----

    #[test]
    fn approve_sends_correct_body_and_path() {
        let t = FakeTransport::ok(r#"{"request_id":"abc-1","status":"approved"}"#);
        let gw = GatewayClient::new("http://gw:8080", "tok", t);
        let out = run_approvals_decide(&gw, "abc-1", true, "looks good").unwrap();
        assert!(out.contains("approved"));
        assert!(out.contains("abc-1"));
        let calls = gw.transport.calls.borrow();
        assert_eq!(calls[0].0, Method::Post);
        assert_eq!(calls[0].1, "http://gw:8080/approve/abc-1/decide");
        let body = calls[0].2.as_ref().unwrap();
        assert_eq!(body["approved"], serde_json::Value::Bool(true));
        assert_eq!(body["request_id"], "abc-1");
        assert_eq!(body["reason"], "looks good");
    }

    #[test]
    fn deny_sends_false_and_formats() {
        let t = FakeTransport::ok(r#"{"request_id":"abc-2","status":"rejected"}"#);
        let gw = GatewayClient::new("http://gw:8080", "tok", t);
        let out = run_approvals_decide(&gw, "abc-2", false, "").unwrap();
        assert!(out.contains("denied"));
        let calls = gw.transport.calls.borrow();
        let body = calls[0].2.as_ref().unwrap();
        assert_eq!(body["approved"], serde_json::Value::Bool(false));
    }

    #[test]
    fn decide_errors_on_404() {
        let t = FakeTransport::with(404, r#"{"detail":"Approval request not found"}"#);
        let gw = GatewayClient::new("http://gw:8080", "tok", t);
        let err = run_approvals_decide(&gw, "missing", true, "")
            .unwrap_err()
            .to_string();
        assert!(err.contains("not found"));
    }

    #[test]
    fn decide_errors_on_409_conflict() {
        let t = FakeTransport::with(409, r#"{"detail":"Conflict: approval state changed"}"#);
        let gw = GatewayClient::new("http://gw:8080", "tok", t);
        let err = run_approvals_decide(&gw, "abc-1", true, "")
            .unwrap_err()
            .to_string();
        assert!(err.contains("conflict"));
    }

    // ---- cves ----

    #[test]
    fn cves_formats_summary() {
        let body = r#"{"total":3,"fully_mitigated":2,"partially_mitigated":1,"not_mitigated":0}"#;
        let t = FakeTransport::ok(body);
        let gw = GatewayClient::new("http://gw:8080", "tok", t);
        let out = run_cves(&gw, None).unwrap();
        assert!(out.contains("3 tracked"));
        assert!(out.contains("fully_mitigated=2"));
        let calls = gw.transport.calls.borrow();
        assert_eq!(calls[0].1, "http://gw:8080/soc/v1/agent-cves");
    }

    #[test]
    fn cves_with_bot_id_appends_query() {
        let t = FakeTransport::ok(r#"{"total":0}"#);
        let gw = GatewayClient::new("http://gw:8080", "tok", t);
        run_cves(&gw, Some("openclaw")).unwrap();
        let calls = gw.transport.calls.borrow();
        assert_eq!(
            calls[0].1,
            "http://gw:8080/soc/v1/agent-cves?bot_id=openclaw"
        );
    }

    #[test]
    fn cves_reports_unknown_bot_error() {
        let t = FakeTransport::ok(r#"{"error":"unknown bot_id: nope"}"#);
        let gw = GatewayClient::new("http://gw:8080", "tok", t);
        let out = run_cves(&gw, Some("nope")).unwrap();
        assert!(out.contains("unknown bot_id: nope"));
    }

    #[test]
    fn cves_counts_array_when_no_total() {
        let body = r#"{"cves":[{"id":"CVE-1"},{"id":"CVE-2"}]}"#;
        let t = FakeTransport::ok(body);
        let gw = GatewayClient::new("http://gw:8080", "tok", t);
        let out = run_cves(&gw, None).unwrap();
        assert!(out.contains("2 tracked"));
    }

    // ---- deploy-status ----

    #[test]
    fn deploy_status_formats_version_and_services() {
        // First call (version) returns current; second (services) returns list.
        // FakeTransport returns the same response for every call, so drive the
        // two-branch formatter directly.
        let version: serde_json::Value = serde_json::json!({"version": "1.2.0"});
        let services: serde_json::Value = serde_json::json!([
            {"name": "gateway", "status": "running"},
            {"name": "openclaw", "status": "running"}
        ]);
        let out = format_deploy_status(&version, &services);
        assert!(out.contains("deployed version: 1.2.0"));
        assert!(out.contains("gateway"));
        assert!(out.contains("openclaw"));
    }

    #[test]
    fn deploy_status_no_services() {
        let version = serde_json::json!({"version": "1.2.0"});
        let out = format_deploy_status(&version, &serde_json::Value::Null);
        assert!(out.contains("deployed version: 1.2.0"));
        assert!(out.contains("(none reported)"));
    }

    #[test]
    fn deploy_status_reads_version_endpoint() {
        let t = FakeTransport::ok(r#"{"version":"1.2.0"}"#);
        let gw = GatewayClient::new("http://gw:8080", "tok", t);
        let out = run_deploy_status(&gw).unwrap();
        assert!(out.contains("deployed version: 1.2.0"));
        let calls = gw.transport.calls.borrow();
        // version endpoint is called first
        assert_eq!(calls[0].1, "http://gw:8080/api/v1/versions/current");
    }

    #[test]
    fn deploy_status_errors_when_version_unauthorized() {
        let t = FakeTransport::with(401, "");
        let gw = GatewayClient::new("http://gw:8080", "tok", t);
        assert!(run_deploy_status(&gw).is_err());
    }

    // ---- formatting edge cases ----

    #[test]
    fn format_status_handles_missing_fields() {
        let out = format_status(&serde_json::json!({}));
        assert!(out.contains("unknown"));
    }

    #[test]
    fn format_approvals_single_object() {
        let obj = serde_json::json!({"request_id":"x","action_type":"a","agent_id":"g","description":"d"});
        let out = format_approvals(&obj);
        assert!(out.contains("x"));
    }
}
