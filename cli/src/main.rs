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

use anyhow::Result;
use clap::{Parser, Subcommand, ValueEnum};
use std::env;

/// AgentShroud SOC CLI
#[derive(Parser)]
#[command(name = "agentshroud-soc", version = "0.9.0", about = "AgentShroud SOC Shared Command Layer")]
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
    Scan {
        scanner: String,
    },
    /// Stream real-time events or logs
    Tail {
        stream: String,
        #[arg(default_value = "")]
        target: String,
        #[arg(long)]
        severity: Option<String>,
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
// HTTP client
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
        let resp = self
            .client
            .get(&url)
            .bearer_auth(&self.token)
            .send()?;
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
        OutputFormat::Json => println!("{}", serde_json::to_string_pretty(data).unwrap_or_default()),
        OutputFormat::Yaml => {
            // Fallback to JSON if serde_yaml not available
            println!("{}", serde_json::to_string_pretty(data).unwrap_or_default());
        }
        OutputFormat::Table => {
            match data {
                serde_json::Value::Array(arr) => {
                    for item in arr {
                        println!("{}", serde_json::to_string_pretty(item).unwrap_or_default());
                        println!("---");
                    }
                }
                _ => println!("{}", serde_json::to_string_pretty(data).unwrap_or_default()),
            }
        }
    }
}

// ---------------------------------------------------------------------------
// Main
// ---------------------------------------------------------------------------

fn main() -> Result<()> {
    let cli = Cli::parse();

    let token = if cli.token.is_empty() {
        env::var("AGENTSHROUD_GATEWAY_PASSWORD").unwrap_or_default()
    } else {
        cli.token.clone()
    };

    let client = SclClient::new(&cli.url, &token);
    let fmt = &cli.format;

    match cli.command {
        Commands::Get { resource } => match resource {
            GetResource::Services => {
                let data = client.get("/services")?;
                print_output(&data, fmt);
            }
            GetResource::Events { severity, limit } => {
                let path = format!("/security/events?limit={}{}", limit,
                    severity.map(|s| format!("&severity={}", s)).unwrap_or_default());
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
                let data = client.post(&format!("/services/{}/restart", name),
                    Some(serde_json::json!({"confirm": true})))?;
                print_output(&data, fmt);
            }
        },
        Commands::Stop { target } => match target {
            ServiceTarget::Service { name, confirm } => {
                if !confirm {
                    eprintln!("Confirmation required. Re-run with --confirm.");
                    std::process::exit(1);
                }
                let data = client.post(&format!("/services/{}/stop", name),
                    Some(serde_json::json!({"confirm": true})))?;
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
                let data = client.post("/users/collaborator",
                    Some(serde_json::json!({"user_id": user_id})))?;
                print_output(&data, fmt);
            }
            AddResource::GroupMember { group_id, user_id } => {
                let data = client.post(&format!("/groups/{}/members", group_id),
                    Some(serde_json::json!({"user_id": user_id})))?;
                print_output(&data, fmt);
            }
        },
        Commands::Set { target } => match target {
            SetTarget::Mode { group_id, mode } => {
                let data = client.post(&format!("/groups/{}/mode", group_id),
                    Some(serde_json::json!({"collab_mode": mode.to_string()})))?;
                print_output(&data, fmt);
            }
            SetTarget::Role { user_id, role } => {
                let data = client.post(&format!("/users/{}/role", user_id),
                    Some(serde_json::json!({"role": role})))?;
                print_output(&data, fmt);
            }
        },
        Commands::Freeze { confirm } => {
            if !confirm {
                eprintln!("Confirmation required. Re-run with --confirm.");
                std::process::exit(1);
            }
            let data = client.post("/killswitch/freeze",
                Some(serde_json::json!({"confirm": true})))?;
            print_output(&data, fmt);
        }
        Commands::Scan { scanner } => {
            let data = client.post(&format!("/scan/{}", scanner),
                Some(serde_json::json!({"confirm": true})))?;
            print_output(&data, fmt);
        }
        Commands::Tail { stream, target: _, severity: _ } => {
            eprintln!("WebSocket tail not yet implemented in Rust CLI. Use Python CLI: agentshroud-soc tail {}", stream);
            std::process::exit(1);
        }
    }

    Ok(())
}
