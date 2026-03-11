# MCP Server Configuration for Additional Services

**Services Covered:**
- AWS API (Official Labs MCP Server) - **RECOMMENDED**
- AWS Athena
- AWS RDS (PostgreSQL, MySQL/MariaDB)
- AWS Glue
- AWS Step Functions
- Zabbix

**Last Updated:** 2026-01-26

---

## Overview

This guide covers integrating MCP (Model Context Protocol) servers for AWS services and monitoring platforms.

**For general AWS access, use the official `awslabs.aws-api-mcp-server` (Section 0) instead of building custom servers.**

**Prerequisites:**
- AWS CLI configured with appropriate credentials
- Access to AWS services (Athena, RDS, Glue, Step Functions)
- Zabbix server access (if using Zabbix monitoring)
- Python 3.8+ or Node.js 18+ (depending on MCP server implementation)

---

## Table of Contents

0. [AWS API MCP Server (Official)](#0-aws-api-mcp-server-official) - **RECOMMENDED**
1. [AWS Athena MCP Server](#1-aws-athena-mcp-server)
2. [AWS RDS MCP Server](#2-aws-rds-mcp-server)
3. [AWS Glue MCP Server](#3-aws-glue-mcp-server)
4. [AWS Step Functions MCP Server](#4-aws-step-functions-mcp-server)
5. [Zabbix MCP Server](#5-zabbix-mcp-server)
6. [Configuration by AI Tool](#configuration-by-ai-tool)
7. [Security Best Practices](#security-best-practices)

---

## 0. AWS API MCP Server (Official)

### Overview
The **official AWS Labs MCP server** (`awslabs.aws-api-mcp-server`) provides a comprehensive interface to AWS services. This is the **recommended** approach for AWS integration - use this instead of building custom MCP servers for individual AWS services.

### Use Cases
- Execute any AWS CLI command
- Get AI-powered suggestions for AWS operations
- Query AWS resources across all services
- Safer than direct CLI access (validation built-in)

### Prerequisites

**Install UV package manager:**
```bash
# macOS
brew install uv
hash -r
which uvx  # Should show /opt/homebrew/bin/uvx

# Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
irm https://astral.sh/uv/install.ps1 | iex
```

### Configuration

#### Claude Code (`.mcp.json`)
```json
{
  "mcpServers": {
    "awslabs.aws-api-mcp-server": {
      "command": "/opt/homebrew/bin/uvx",
      "args": [
        "awslabs.aws-api-mcp-server@latest",
        "--readonly"
      ],
      "env": {
        "AWS_PROFILE": "${AWS_PROFILE:-default}",
        "AWS_REGION": "${AWS_REGION:-us-east-1}",
        "FASTMCP_LOG_LEVEL": "${FASTMCP_LOG_LEVEL:-ERROR}"
      }
    }
  }
}
```

#### Gemini CLI (`.gemini/settings.json`)
```json
{
  "mcpServers": {
    "awslabs.aws-api-mcp-server": {
      "command": "/opt/homebrew/bin/uvx",
      "args": ["awslabs.aws-api-mcp-server@latest", "--readonly"],
      "env": {
        "AWS_PROFILE": "default",
        "AWS_REGION": "us-east-1"
      }
    }
  }
}
```

#### Codex CLI (`.codex/config.toml`)
```toml
[mcp_servers.awslabs-aws-api-mcp-server]
command = "/opt/homebrew/bin/uvx"
args = ["awslabs.aws-api-mcp-server@latest", "--readonly"]

[mcp_servers.awslabs-aws-api-mcp-server.env]
AWS_PROFILE = "default"
AWS_REGION = "us-east-1"
```

#### GitHub Copilot CLI (`~/.copilot/mcp-config.json`)
```json
{
  "servers": {
    "awslabs.aws-api-mcp-server": {
      "command": "/opt/homebrew/bin/uvx",
      "args": ["awslabs.aws-api-mcp-server@latest", "--readonly"],
      "env": {
        "AWS_PROFILE": "default",
        "AWS_REGION": "us-east-1"
      }
    }
  }
}
```

### Available Tools

| Tool | Description |
|------|-------------|
| `suggest_aws_commands` | Natural language to AWS CLI command suggestions |
| `call_aws` | Execute validated AWS CLI commands |

### Usage Examples

```bash
# In Claude Code - suggestions
> How do I create an S3 bucket with versioning?

# In Claude Code - direct execution
> List all Lambda functions in us-east-1

# Query resources
> Show me all running EC2 instances

# Complex operations
> Find all S3 buckets larger than 1GB
```

### Comparison: Official vs Custom MCP Servers

| Aspect | awslabs.aws-api-mcp-server | Custom MCP Servers |
|--------|---------------------------|-------------------|
| **Coverage** | All AWS services | Single service each |
| **Maintenance** | AWS Labs maintained | You maintain |
| **Security** | Built-in validation, readonly mode | You implement |
| **Setup** | One config entry | Multiple servers |

**Recommendation:** Use `awslabs.aws-api-mcp-server` for general AWS access. Only build custom MCP servers if you need specialized functionality not available through the AWS CLI.

### Sources
- [awslabs/aws-api-mcp-server on GitHub](https://github.com/awslabs/aws-api-mcp-server)
- [UV Package Manager](https://github.com/astral-sh/uv)

---

## 1. AWS Athena MCP Server

### Overview
Enables AI tools to query AWS Athena, execute SQL queries, check query status, and retrieve results from your data lake.

### Use Cases
- Query data lake tables
- Execute SQL analytics
- Retrieve query history
- Check query execution status
- Generate reports from S3 data

### Implementation Options

#### Option A: Custom Python MCP Server

**Create:** `~/.mcp-servers/aws-athena/server.py`

```python
#!/usr/bin/env python3
"""
AWS Athena MCP Server
Enables AI tools to query Athena and retrieve results
"""

import asyncio
import json
import os
import sys
from typing import Any

import boto3
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Initialize Athena client
athena_client = boto3.client('athena')
s3_client = boto3.client('s3')

# Configuration from environment
ATHENA_DATABASE = os.getenv('ATHENA_DATABASE', 'default')
ATHENA_OUTPUT_LOCATION = os.getenv('ATHENA_OUTPUT_LOCATION')  # s3://bucket/path/
ATHENA_WORKGROUP = os.getenv('ATHENA_WORKGROUP', 'primary')

app = Server("aws-athena")

@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available Athena operations"""
    return [
        Tool(
            name="execute_query",
            description="Execute SQL query in Athena and return results",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "SQL query to execute"
                    },
                    "database": {
                        "type": "string",
                        "description": "Database name (optional, uses default)",
                        "default": ATHENA_DATABASE
                    },
                    "max_results": {
                        "type": "integer",
                        "description": "Maximum number of results to return",
                        "default": 100
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="check_query_status",
            description="Check status of a running Athena query",
            inputSchema={
                "type": "object",
                "properties": {
                    "query_execution_id": {
                        "type": "string",
                        "description": "Query execution ID to check"
                    }
                },
                "required": ["query_execution_id"]
            }
        ),
        Tool(
            name="list_databases",
            description="List available Athena databases",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="list_tables",
            description="List tables in a database",
            inputSchema={
                "type": "object",
                "properties": {
                    "database": {
                        "type": "string",
                        "description": "Database name",
                        "default": ATHENA_DATABASE
                    }
                },
                "required": ["database"]
            }
        ),
        Tool(
            name="describe_table",
            description="Get table schema and metadata",
            inputSchema={
                "type": "object",
                "properties": {
                    "database": {
                        "type": "string",
                        "description": "Database name"
                    },
                    "table": {
                        "type": "string",
                        "description": "Table name"
                    }
                },
                "required": ["database", "table"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Execute Athena operations"""

    if name == "execute_query":
        return await execute_query(
            arguments["query"],
            arguments.get("database", ATHENA_DATABASE),
            arguments.get("max_results", 100)
        )

    elif name == "check_query_status":
        return await check_query_status(arguments["query_execution_id"])

    elif name == "list_databases":
        return await list_databases()

    elif name == "list_tables":
        return await list_tables(arguments.get("database", ATHENA_DATABASE))

    elif name == "describe_table":
        return await describe_table(arguments["database"], arguments["table"])

    else:
        raise ValueError(f"Unknown tool: {name}")

async def execute_query(query: str, database: str, max_results: int) -> list[TextContent]:
    """Execute Athena query and return results"""
    try:
        # Start query execution
        response = athena_client.start_query_execution(
            QueryString=query,
            QueryExecutionContext={'Database': database},
            ResultConfiguration={'OutputLocation': ATHENA_OUTPUT_LOCATION},
            WorkGroup=ATHENA_WORKGROUP
        )

        query_execution_id = response['QueryExecutionId']

        # Wait for query to complete
        while True:
            status_response = athena_client.get_query_execution(
                QueryExecutionId=query_execution_id
            )
            status = status_response['QueryExecution']['Status']['State']

            if status in ['SUCCEEDED', 'FAILED', 'CANCELLED']:
                break

            await asyncio.sleep(1)

        if status != 'SUCCEEDED':
            error_msg = status_response['QueryExecution']['Status'].get('StateChangeReason', 'Unknown error')
            return [TextContent(
                type="text",
                text=f"Query failed: {error_msg}"
            )]

        # Get results
        results = athena_client.get_query_results(
            QueryExecutionId=query_execution_id,
            MaxResults=max_results
        )

        # Format results as table
        rows = results['ResultSet']['Rows']
        if not rows:
            return [TextContent(type="text", text="No results")]

        # Extract column names from first row
        columns = [col['VarCharValue'] for col in rows[0]['Data']]

        # Format data rows
        data_rows = []
        for row in rows[1:]:
            data_rows.append([
                cell.get('VarCharValue', '') for cell in row['Data']
            ])

        # Create markdown table
        table = "| " + " | ".join(columns) + " |\n"
        table += "| " + " | ".join(["---"] * len(columns)) + " |\n"

        for row in data_rows[:max_results]:
            table += "| " + " | ".join(str(cell) for cell in row) + " |\n"

        result_text = f"Query: {query}\n\n{table}\n\nRows: {len(data_rows)}"

        return [TextContent(type="text", text=result_text)]

    except Exception as e:
        return [TextContent(type="text", text=f"Error executing query: {str(e)}")]

async def check_query_status(query_execution_id: str) -> list[TextContent]:
    """Check status of Athena query"""
    try:
        response = athena_client.get_query_execution(
            QueryExecutionId=query_execution_id
        )

        execution = response['QueryExecution']
        status = execution['Status']['State']
        query = execution['Query']

        result = f"Query: {query}\nStatus: {status}\n"

        if status == 'FAILED':
            result += f"Error: {execution['Status'].get('StateChangeReason', 'Unknown')}\n"
        elif status == 'SUCCEEDED':
            stats = execution['Statistics']
            result += f"Data scanned: {stats.get('DataScannedInBytes', 0)} bytes\n"
            result += f"Execution time: {stats.get('EngineExecutionTimeInMillis', 0)} ms\n"

        return [TextContent(type="text", text=result)]

    except Exception as e:
        return [TextContent(type="text", text=f"Error checking status: {str(e)}")]

async def list_databases() -> list[TextContent]:
    """List available databases"""
    try:
        response = athena_client.list_databases(CatalogName='AwsDataCatalog')
        databases = [db['Name'] for db in response['DatabaseList']]

        result = "Available databases:\n" + "\n".join(f"- {db}" for db in databases)
        return [TextContent(type="text", text=result)]

    except Exception as e:
        return [TextContent(type="text", text=f"Error listing databases: {str(e)}")]

async def list_tables(database: str) -> list[TextContent]:
    """List tables in database"""
    try:
        response = athena_client.list_table_metadata(
            CatalogName='AwsDataCatalog',
            DatabaseName=database
        )

        tables = [table['Name'] for table in response['TableMetadataList']]

        result = f"Tables in {database}:\n" + "\n".join(f"- {table}" for table in tables)
        return [TextContent(type="text", text=result)]

    except Exception as e:
        return [TextContent(type="text", text=f"Error listing tables: {str(e)}")]

async def describe_table(database: str, table: str) -> list[TextContent]:
    """Get table schema"""
    try:
        response = athena_client.get_table_metadata(
            CatalogName='AwsDataCatalog',
            DatabaseName=database,
            TableName=table
        )

        metadata = response['TableMetadata']
        columns = metadata['Columns']

        result = f"Table: {database}.{table}\n\n"
        result += "Columns:\n"

        for col in columns:
            result += f"- {col['Name']}: {col['Type']}"
            if 'Comment' in col:
                result += f" ({col['Comment']})"
            result += "\n"

        if 'PartitionKeys' in metadata and metadata['PartitionKeys']:
            result += "\nPartition Keys:\n"
            for key in metadata['PartitionKeys']:
                result += f"- {key['Name']}: {key['Type']}\n"

        return [TextContent(type="text", text=result)]

    except Exception as e:
        return [TextContent(type="text", text=f"Error describing table: {str(e)}")]

async def main():
    """Run MCP server"""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
```

**Install dependencies:**
```bash
pip install mcp boto3
```

**Make executable:**
```bash
chmod +x ~/.mcp-servers/aws-athena/server.py
```

### Configuration

#### Claude Code (`.mcp.json`)
```json
{
  "mcpServers": {
    "aws-athena": {
      "command": "python3",
      "args": ["/Users/username/.mcp-servers/aws-athena/server.py"],
      "env": {
        "AWS_PROFILE": "default",
        "ATHENA_DATABASE": "your_database",
        "ATHENA_OUTPUT_LOCATION": "s3://your-bucket/athena-results/",
        "ATHENA_WORKGROUP": "primary"
      }
    }
  }
}
```

#### Gemini CLI (`.gemini/settings.json`)
```json
{
  "mcpServers": {
    "aws-athena": {
      "command": "python3",
      "args": ["/Users/username/.mcp-servers/aws-athena/server.py"],
      "env": {
        "AWS_PROFILE": "default",
        "ATHENA_DATABASE": "your_database",
        "ATHENA_OUTPUT_LOCATION": "s3://your-bucket/athena-results/",
        "ATHENA_WORKGROUP": "primary"
      }
    }
  }
}
```

#### Codex CLI (`.codex/config.toml`)
```toml
[mcp_servers.aws-athena]
command = "python3"
args = ["/Users/username/.mcp-servers/aws-athena/server.py"]

[mcp_servers.aws-athena.env]
AWS_PROFILE = "default"
ATHENA_DATABASE = "your_database"
ATHENA_OUTPUT_LOCATION = "s3://your-bucket/athena-results/"
ATHENA_WORKGROUP = "primary"
```

#### GitHub Copilot CLI (`~/.copilot/mcp-config.json`)
```json
{
  "servers": {
    "aws-athena": {
      "command": "python3",
      "args": ["/Users/username/.mcp-servers/aws-athena/server.py"],
      "env": {
        "AWS_PROFILE": "default",
        "ATHENA_DATABASE": "your_database",
        "ATHENA_OUTPUT_LOCATION": "s3://your-bucket/athena-results/",
        "ATHENA_WORKGROUP": "primary"
      }
    }
  }
}
```

### Usage Examples

```bash
# Query data
> Use aws-athena to query: SELECT * FROM my_table LIMIT 10

# Check query status
> Check the status of Athena query execution abc123

# List tables
> List all tables in the analytics database

# Describe table schema
> Describe the schema of events table in analytics database
```

---

## 2. AWS RDS MCP Server

### Overview
Enables AI tools to connect to RDS databases (PostgreSQL, MySQL/MariaDB), execute queries, and manage database operations.

### Use Cases
- Query application databases
- Check database schema
- Execute SQL commands
- Monitor database health
- Generate reports from relational data

### Implementation

**Create:** `~/.mcp-servers/aws-rds/server.py`

```python
#!/usr/bin/env python3
"""
AWS RDS MCP Server
Supports PostgreSQL, MySQL, and MariaDB
"""

import asyncio
import json
import os
from typing import Any

import boto3
import psycopg2  # For PostgreSQL
import pymysql  # For MySQL/MariaDB
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Configuration
RDS_DB_TYPE = os.getenv('RDS_DB_TYPE', 'postgresql')  # postgresql, mysql, mariadb
RDS_HOST = os.getenv('RDS_HOST')
RDS_PORT = int(os.getenv('RDS_PORT', '5432'))
RDS_DATABASE = os.getenv('RDS_DATABASE')
RDS_USER = os.getenv('RDS_USER')
RDS_PASSWORD = os.getenv('RDS_PASSWORD')

app = Server("aws-rds")

def get_connection():
    """Get database connection based on type"""
    if RDS_DB_TYPE == 'postgresql':
        return psycopg2.connect(
            host=RDS_HOST,
            port=RDS_PORT,
            database=RDS_DATABASE,
            user=RDS_USER,
            password=RDS_PASSWORD
        )
    elif RDS_DB_TYPE in ['mysql', 'mariadb']:
        return pymysql.connect(
            host=RDS_HOST,
            port=RDS_PORT,
            database=RDS_DATABASE,
            user=RDS_USER,
            password=RDS_PASSWORD
        )
    else:
        raise ValueError(f"Unsupported database type: {RDS_DB_TYPE}")

@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available RDS operations"""
    return [
        Tool(
            name="execute_query",
            description="Execute SELECT query and return results",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "SQL SELECT query"},
                    "max_rows": {"type": "integer", "default": 100}
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="list_tables",
            description="List all tables in the database",
            inputSchema={"type": "object", "properties": {}}
        ),
        Tool(
            name="describe_table",
            description="Get table schema and column information",
            inputSchema={
                "type": "object",
                "properties": {
                    "table": {"type": "string", "description": "Table name"}
                },
                "required": ["table"]
            }
        ),
        Tool(
            name="get_table_count",
            description="Get row count for a table",
            inputSchema={
                "type": "object",
                "properties": {
                    "table": {"type": "string", "description": "Table name"}
                },
                "required": ["table"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Execute RDS operations"""

    if name == "execute_query":
        return await execute_query(arguments["query"], arguments.get("max_rows", 100))
    elif name == "list_tables":
        return await list_tables()
    elif name == "describe_table":
        return await describe_table(arguments["table"])
    elif name == "get_table_count":
        return await get_table_count(arguments["table"])
    else:
        raise ValueError(f"Unknown tool: {name}")

async def execute_query(query: str, max_rows: int) -> list[TextContent]:
    """Execute SELECT query"""
    # Security: Only allow SELECT queries
    if not query.strip().upper().startswith('SELECT'):
        return [TextContent(type="text", text="Error: Only SELECT queries are allowed")]

    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query)

        # Get column names
        columns = [desc[0] for desc in cursor.description]

        # Fetch results
        rows = cursor.fetchmany(max_rows)

        # Format as markdown table
        if not rows:
            return [TextContent(type="text", text="No results")]

        table = "| " + " | ".join(columns) + " |\n"
        table += "| " + " | ".join(["---"] * len(columns)) + " |\n"

        for row in rows:
            table += "| " + " | ".join(str(cell) for cell in row) + " |\n"

        cursor.close()
        conn.close()

        result_text = f"Query: {query}\n\n{table}\n\nRows: {len(rows)}"
        return [TextContent(type="text", text=result_text)]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]

async def list_tables() -> list[TextContent]:
    """List all tables"""
    try:
        conn = get_connection()
        cursor = conn.cursor()

        if RDS_DB_TYPE == 'postgresql':
            cursor.execute("""
                SELECT tablename FROM pg_tables
                WHERE schemaname = 'public'
                ORDER BY tablename
            """)
        else:  # MySQL/MariaDB
            cursor.execute("SHOW TABLES")

        tables = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()

        result = f"Tables in {RDS_DATABASE}:\n" + "\n".join(f"- {table}" for table in tables)
        return [TextContent(type="text", text=result)]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]

async def describe_table(table: str) -> list[TextContent]:
    """Get table schema"""
    try:
        conn = get_connection()
        cursor = conn.cursor()

        if RDS_DB_TYPE == 'postgresql':
            cursor.execute("""
                SELECT column_name, data_type, is_nullable
                FROM information_schema.columns
                WHERE table_name = %s
                ORDER BY ordinal_position
            """, (table,))
        else:  # MySQL/MariaDB
            cursor.execute(f"DESCRIBE {table}")

        columns = cursor.fetchall()
        cursor.close()
        conn.close()

        if not columns:
            return [TextContent(type="text", text=f"Table '{table}' not found")]

        result = f"Schema for {table}:\n\n"
        for col in columns:
            if RDS_DB_TYPE == 'postgresql':
                result += f"- {col[0]}: {col[1]} (nullable: {col[2]})\n"
            else:
                result += f"- {col[0]}: {col[1]}\n"

        return [TextContent(type="text", text=result)]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]

async def get_table_count(table: str) -> list[TextContent]:
    """Get row count"""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = cursor.fetchone()[0]
        cursor.close()
        conn.close()

        return [TextContent(type="text", text=f"Table {table} has {count:,} rows")]

    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]

async def main():
    """Run MCP server"""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
```

**Install dependencies:**
```bash
pip install mcp psycopg2-binary pymysql boto3
```

### Configuration

Add to `.env` (gitignored!):
```bash
RDS_DB_TYPE=postgresql
RDS_HOST=your-rds-instance.region.rds.amazonaws.com
RDS_PORT=5432
RDS_DATABASE=your_database
RDS_USER=your_user
RDS_PASSWORD=your_password
```

**IMPORTANT:** Never commit database credentials to git!

Add to MCP configs (example for Claude):
```json
{
  "mcpServers": {
    "aws-rds": {
      "command": "python3",
      "args": ["/Users/username/.mcp-servers/aws-rds/server.py"],
      "env": {
        "RDS_DB_TYPE": "postgresql",
        "RDS_HOST": "$RDS_HOST",
        "RDS_PORT": "5432",
        "RDS_DATABASE": "$RDS_DATABASE",
        "RDS_USER": "$RDS_USER",
        "RDS_PASSWORD": "$RDS_PASSWORD"
      }
    }
  }
}
```

---

## 3. AWS Glue MCP Server

### Overview
Enables AI tools to interact with AWS Glue for ETL operations, catalog management, and job execution.

### Use Cases
- List Glue databases and tables
- Get table schemas and metadata
- Trigger Glue jobs
- Check job run status
- Query Data Catalog

### Implementation

**Create:** `~/.mcp-servers/aws-glue/server.py`

```python
#!/usr/bin/env python3
"""
AWS Glue MCP Server
Interact with AWS Glue Data Catalog and Jobs
"""

import asyncio
import json
import os
from typing import Any

import boto3
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

glue_client = boto3.client('glue')

app = Server("aws-glue")

@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available Glue operations"""
    return [
        Tool(
            name="list_databases",
            description="List all Glue databases",
            inputSchema={"type": "object", "properties": {}}
        ),
        Tool(
            name="list_tables",
            description="List tables in a Glue database",
            inputSchema={
                "type": "object",
                "properties": {
                    "database": {"type": "string", "description": "Database name"}
                },
                "required": ["database"]
            }
        ),
        Tool(
            name="get_table",
            description="Get table metadata and schema",
            inputSchema={
                "type": "object",
                "properties": {
                    "database": {"type": "string"},
                    "table": {"type": "string"}
                },
                "required": ["database", "table"]
            }
        ),
        Tool(
            name="list_jobs",
            description="List all Glue ETL jobs",
            inputSchema={"type": "object", "properties": {}}
        ),
        Tool(
            name="start_job",
            description="Start a Glue job run",
            inputSchema={
                "type": "object",
                "properties": {
                    "job_name": {"type": "string", "description": "Glue job name"},
                    "arguments": {"type": "object", "description": "Job arguments"}
                },
                "required": ["job_name"]
            }
        ),
        Tool(
            name="get_job_run",
            description="Get status of a job run",
            inputSchema={
                "type": "object",
                "properties": {
                    "job_name": {"type": "string"},
                    "run_id": {"type": "string"}
                },
                "required": ["job_name", "run_id"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Execute Glue operations"""

    if name == "list_databases":
        return await list_databases()
    elif name == "list_tables":
        return await list_tables(arguments["database"])
    elif name == "get_table":
        return await get_table(arguments["database"], arguments["table"])
    elif name == "list_jobs":
        return await list_jobs()
    elif name == "start_job":
        return await start_job(arguments["job_name"], arguments.get("arguments", {}))
    elif name == "get_job_run":
        return await get_job_run(arguments["job_name"], arguments["run_id"])
    else:
        raise ValueError(f"Unknown tool: {name}")

async def list_databases() -> list[TextContent]:
    """List Glue databases"""
    try:
        response = glue_client.get_databases()
        databases = [db['Name'] for db in response['DatabaseList']]

        result = "Glue Databases:\n" + "\n".join(f"- {db}" for db in databases)
        return [TextContent(type="text", text=result)]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]

async def list_tables(database: str) -> list[TextContent]:
    """List tables in database"""
    try:
        response = glue_client.get_tables(DatabaseName=database)
        tables = [table['Name'] for table in response['TableList']]

        result = f"Tables in {database}:\n" + "\n".join(f"- {table}" for table in tables)
        return [TextContent(type="text", text=result)]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]

async def get_table(database: str, table: str) -> list[TextContent]:
    """Get table schema"""
    try:
        response = glue_client.get_table(DatabaseName=database, Name=table)
        table_data = response['Table']

        result = f"Table: {database}.{table}\n\n"
        result += f"Location: {table_data['StorageDescriptor'].get('Location', 'N/A')}\n"
        result += f"Input Format: {table_data['StorageDescriptor'].get('InputFormat', 'N/A')}\n"
        result += f"Output Format: {table_data['StorageDescriptor'].get('OutputFormat', 'N/A')}\n\n"
        result += "Columns:\n"

        for col in table_data['StorageDescriptor']['Columns']:
            result += f"- {col['Name']}: {col['Type']}"
            if 'Comment' in col:
                result += f" ({col['Comment']})"
            result += "\n"

        if 'PartitionKeys' in table_data and table_data['PartitionKeys']:
            result += "\nPartition Keys:\n"
            for key in table_data['PartitionKeys']:
                result += f"- {key['Name']}: {key['Type']}\n"

        return [TextContent(type="text", text=result)]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]

async def list_jobs() -> list[TextContent]:
    """List Glue jobs"""
    try:
        response = glue_client.list_jobs()
        jobs = response['JobNames']

        result = "Glue Jobs:\n" + "\n".join(f"- {job}" for job in jobs)
        return [TextContent(type="text", text=result)]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]

async def start_job(job_name: str, arguments: dict) -> list[TextContent]:
    """Start Glue job"""
    try:
        response = glue_client.start_job_run(
            JobName=job_name,
            Arguments=arguments
        )

        run_id = response['JobRunId']
        result = f"Started job '{job_name}'\nRun ID: {run_id}"
        return [TextContent(type="text", text=result)]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]

async def get_job_run(job_name: str, run_id: str) -> list[TextContent]:
    """Get job run status"""
    try:
        response = glue_client.get_job_run(JobName=job_name, RunId=run_id)
        job_run = response['JobRun']

        result = f"Job: {job_name}\n"
        result += f"Run ID: {run_id}\n"
        result += f"Status: {job_run['JobRunState']}\n"
        result += f"Started: {job_run['StartedOn']}\n"

        if 'CompletedOn' in job_run:
            result += f"Completed: {job_run['CompletedOn']}\n"

        if 'ErrorMessage' in job_run:
            result += f"Error: {job_run['ErrorMessage']}\n"

        return [TextContent(type="text", text=result)]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]

async def main():
    """Run MCP server"""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 4. AWS Step Functions MCP Server

### Overview
Enables AI tools to interact with AWS Step Functions state machines, start executions, and monitor workflow progress.

### Use Cases
- List state machines
- Start workflow executions
- Check execution status
- Get execution history
- Monitor workflow progress

### Implementation

**Create:** `~/.mcp-servers/aws-stepfunctions/server.py`

```python
#!/usr/bin/env python3
"""
AWS Step Functions MCP Server
Manage and monitor Step Functions state machines
"""

import asyncio
import json
import os
from typing import Any

import boto3
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

sfn_client = boto3.client('stepfunctions')

app = Server("aws-stepfunctions")

@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available Step Functions operations"""
    return [
        Tool(
            name="list_state_machines",
            description="List all Step Functions state machines",
            inputSchema={"type": "object", "properties": {}}
        ),
        Tool(
            name="describe_state_machine",
            description="Get state machine details",
            inputSchema={
                "type": "object",
                "properties": {
                    "state_machine_arn": {"type": "string"}
                },
                "required": ["state_machine_arn"]
            }
        ),
        Tool(
            name="start_execution",
            description="Start a state machine execution",
            inputSchema={
                "type": "object",
                "properties": {
                    "state_machine_arn": {"type": "string"},
                    "input_data": {"type": "object"},
                    "name": {"type": "string", "description": "Execution name (optional)"}
                },
                "required": ["state_machine_arn", "input_data"]
            }
        ),
        Tool(
            name="describe_execution",
            description="Get execution status and details",
            inputSchema={
                "type": "object",
                "properties": {
                    "execution_arn": {"type": "string"}
                },
                "required": ["execution_arn"]
            }
        ),
        Tool(
            name="list_executions",
            description="List executions for a state machine",
            inputSchema={
                "type": "object",
                "properties": {
                    "state_machine_arn": {"type": "string"},
                    "status": {"type": "string", "enum": ["RUNNING", "SUCCEEDED", "FAILED", "TIMED_OUT", "ABORTED"]}
                },
                "required": ["state_machine_arn"]
            }
        ),
        Tool(
            name="get_execution_history",
            description="Get execution event history",
            inputSchema={
                "type": "object",
                "properties": {
                    "execution_arn": {"type": "string"}
                },
                "required": ["execution_arn"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Execute Step Functions operations"""

    if name == "list_state_machines":
        return await list_state_machines()
    elif name == "describe_state_machine":
        return await describe_state_machine(arguments["state_machine_arn"])
    elif name == "start_execution":
        return await start_execution(
            arguments["state_machine_arn"],
            arguments["input_data"],
            arguments.get("name")
        )
    elif name == "describe_execution":
        return await describe_execution(arguments["execution_arn"])
    elif name == "list_executions":
        return await list_executions(
            arguments["state_machine_arn"],
            arguments.get("status")
        )
    elif name == "get_execution_history":
        return await get_execution_history(arguments["execution_arn"])
    else:
        raise ValueError(f"Unknown tool: {name}")

async def list_state_machines() -> list[TextContent]:
    """List state machines"""
    try:
        response = sfn_client.list_state_machines()
        machines = response['stateMachines']

        result = "State Machines:\n"
        for machine in machines:
            result += f"\n- {machine['name']}\n"
            result += f"  ARN: {machine['stateMachineArn']}\n"
            result += f"  Type: {machine['type']}\n"

        return [TextContent(type="text", text=result)]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]

async def describe_state_machine(state_machine_arn: str) -> list[TextContent]:
    """Get state machine details"""
    try:
        response = sfn_client.describe_state_machine(stateMachineArn=state_machine_arn)

        result = f"State Machine: {response['name']}\n"
        result += f"ARN: {response['stateMachineArn']}\n"
        result += f"Type: {response['type']}\n"
        result += f"Status: {response['status']}\n"
        result += f"Created: {response['creationDate']}\n"
        result += f"\nDefinition:\n{response['definition']}\n"

        return [TextContent(type="text", text=result)]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]

async def start_execution(state_machine_arn: str, input_data: dict, name: str = None) -> list[TextContent]:
    """Start execution"""
    try:
        params = {
            'stateMachineArn': state_machine_arn,
            'input': json.dumps(input_data)
        }

        if name:
            params['name'] = name

        response = sfn_client.start_execution(**params)

        result = f"Started execution\n"
        result += f"Execution ARN: {response['executionArn']}\n"
        result += f"Start Date: {response['startDate']}\n"

        return [TextContent(type="text", text=result)]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]

async def describe_execution(execution_arn: str) -> list[TextContent]:
    """Get execution status"""
    try:
        response = sfn_client.describe_execution(executionArn=execution_arn)

        result = f"Execution: {response['name']}\n"
        result += f"Status: {response['status']}\n"
        result += f"Started: {response['startDate']}\n"

        if 'stopDate' in response:
            result += f"Stopped: {response['stopDate']}\n"

        if 'output' in response:
            result += f"\nOutput:\n{response['output']}\n"

        if 'error' in response:
            result += f"\nError: {response['error']}\n"
            result += f"Cause: {response['cause']}\n"

        return [TextContent(type="text", text=result)]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]

async def list_executions(state_machine_arn: str, status: str = None) -> list[TextContent]:
    """List executions"""
    try:
        params = {'stateMachineArn': state_machine_arn}
        if status:
            params['statusFilter'] = status

        response = sfn_client.list_executions(**params)
        executions = response['executions']

        result = "Executions:\n"
        for execution in executions[:20]:  # Limit to 20
            result += f"\n- {execution['name']}\n"
            result += f"  Status: {execution['status']}\n"
            result += f"  Started: {execution['startDate']}\n"

        return [TextContent(type="text", text=result)]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]

async def get_execution_history(execution_arn: str) -> list[TextContent]:
    """Get execution history"""
    try:
        response = sfn_client.get_execution_history(executionArn=execution_arn)
        events = response['events']

        result = "Execution History:\n"
        for event in events:
            result += f"\n{event['timestamp']}: {event['type']}\n"
            if 'stateEnteredEventDetails' in event:
                result += f"  State: {event['stateEnteredEventDetails']['name']}\n"

        return [TextContent(type="text", text=result)]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]

async def main():
    """Run MCP server"""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 5. Zabbix MCP Server

### Overview
Enables AI tools to interact with Zabbix monitoring platform for system metrics, alerts, and host management.

### Use Cases
- Query system metrics
- Check alert status
- List monitored hosts
- Get trigger information
- Monitor system health

### Implementation

**Create:** `~/.mcp-servers/zabbix/server.py`

```python
#!/usr/bin/env python3
"""
Zabbix MCP Server
Interact with Zabbix monitoring API
"""

import asyncio
import json
import os
from typing import Any

from pyzabbix import ZabbixAPI
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Configuration
ZABBIX_URL = os.getenv('ZABBIX_URL')  # http://zabbix.example.com
ZABBIX_USER = os.getenv('ZABBIX_USER')
ZABBIX_PASSWORD = os.getenv('ZABBIX_PASSWORD')

zapi = ZabbixAPI(ZABBIX_URL)
zapi.login(ZABBIX_USER, ZABBIX_PASSWORD)

app = Server("zabbix")

@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available Zabbix operations"""
    return [
        Tool(
            name="list_hosts",
            description="List monitored hosts",
            inputSchema={"type": "object", "properties": {}}
        ),
        Tool(
            name="get_host_info",
            description="Get detailed host information",
            inputSchema={
                "type": "object",
                "properties": {
                    "hostname": {"type": "string"}
                },
                "required": ["hostname"]
            }
        ),
        Tool(
            name="get_active_triggers",
            description="Get active triggers (problems/alerts)",
            inputSchema={
                "type": "object",
                "properties": {
                    "severity": {"type": "integer", "description": "Minimum severity (0-5)"},
                    "hostname": {"type": "string", "description": "Filter by hostname (optional)"}
                }
            }
        ),
        Tool(
            name="get_latest_data",
            description="Get latest monitoring data for a host",
            inputSchema={
                "type": "object",
                "properties": {
                    "hostname": {"type": "string"},
                    "item_key": {"type": "string", "description": "Item key (e.g., system.cpu.load)"}
                },
                "required": ["hostname"]
            }
        ),
        Tool(
            name="get_history",
            description="Get historical data for an item",
            inputSchema={
                "type": "object",
                "properties": {
                    "hostname": {"type": "string"},
                    "item_key": {"type": "string"},
                    "time_from": {"type": "integer", "description": "Unix timestamp"},
                    "time_till": {"type": "integer", "description": "Unix timestamp"}
                },
                "required": ["hostname", "item_key"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Execute Zabbix operations"""

    if name == "list_hosts":
        return await list_hosts()
    elif name == "get_host_info":
        return await get_host_info(arguments["hostname"])
    elif name == "get_active_triggers":
        return await get_active_triggers(
            arguments.get("severity", 0),
            arguments.get("hostname")
        )
    elif name == "get_latest_data":
        return await get_latest_data(
            arguments["hostname"],
            arguments.get("item_key")
        )
    elif name == "get_history":
        return await get_history(
            arguments["hostname"],
            arguments["item_key"],
            arguments.get("time_from"),
            arguments.get("time_till")
        )
    else:
        raise ValueError(f"Unknown tool: {name}")

async def list_hosts() -> list[TextContent]:
    """List monitored hosts"""
    try:
        hosts = zapi.host.get(output=['hostid', 'host', 'name', 'status'])

        result = "Monitored Hosts:\n"
        for host in hosts:
            status = "Enabled" if host['status'] == '0' else "Disabled"
            result += f"- {host['host']} ({host['name']}) - {status}\n"

        return [TextContent(type="text", text=result)]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]

async def get_host_info(hostname: str) -> list[TextContent]:
    """Get host details"""
    try:
        hosts = zapi.host.get(filter={'host': hostname}, selectInterfaces=['ip'])

        if not hosts:
            return [TextContent(type="text", text=f"Host '{hostname}' not found")]

        host = hosts[0]
        result = f"Host: {host['host']}\n"
        result += f"Name: {host['name']}\n"
        result += f"ID: {host['hostid']}\n"

        if host.get('interfaces'):
            result += f"IP: {host['interfaces'][0]['ip']}\n"

        return [TextContent(type="text", text=result)]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]

async def get_active_triggers(severity: int, hostname: str = None) -> list[TextContent]:
    """Get active triggers"""
    try:
        params = {
            'only_true': 1,
            'skipDependent': 1,
            'monitored': 1,
            'active': 1,
            'output': 'extend',
            'selectHosts': ['host'],
            'min_severity': severity
        }

        if hostname:
            hosts = zapi.host.get(filter={'host': hostname})
            if hosts:
                params['hostids'] = hosts[0]['hostid']

        triggers = zapi.trigger.get(**params)

        if not triggers:
            return [TextContent(type="text", text="No active triggers")]

        severities = ['Not classified', 'Information', 'Warning', 'Average', 'High', 'Disaster']

        result = "Active Triggers:\n"
        for trigger in triggers:
            severity_name = severities[int(trigger['priority'])]
            host = trigger['hosts'][0]['host'] if trigger.get('hosts') else 'Unknown'
            result += f"\n[{severity_name}] {host}: {trigger['description']}\n"

        return [TextContent(type="text", text=result)]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]

async def get_latest_data(hostname: str, item_key: str = None) -> list[TextContent]:
    """Get latest monitoring data"""
    try:
        hosts = zapi.host.get(filter={'host': hostname})
        if not hosts:
            return [TextContent(type="text", text=f"Host '{hostname}' not found")]

        hostid = hosts[0]['hostid']

        params = {
            'output': 'extend',
            'hostids': hostid,
            'sortfield': 'name'
        }

        if item_key:
            params['search'] = {'key_': item_key}

        items = zapi.item.get(**params)

        if not items:
            return [TextContent(type="text", text="No items found")]

        result = f"Latest Data for {hostname}:\n"
        for item in items[:20]:  # Limit to 20 items
            result += f"\n- {item['name']}\n"
            result += f"  Value: {item.get('lastvalue', 'N/A')}\n"
            result += f"  Key: {item['key_']}\n"

        return [TextContent(type="text", text=result)]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]

async def get_history(hostname: str, item_key: str, time_from: int = None, time_till: int = None) -> list[TextContent]:
    """Get historical data"""
    try:
        hosts = zapi.host.get(filter={'host': hostname})
        if not hosts:
            return [TextContent(type="text", text=f"Host '{hostname}' not found")]

        hostid = hosts[0]['hostid']

        items = zapi.item.get(
            output=['itemid', 'name', 'value_type'],
            hostids=hostid,
            search={'key_': item_key}
        )

        if not items:
            return [TextContent(type="text", text=f"Item '{item_key}' not found")]

        item = items[0]

        params = {
            'output': 'extend',
            'history': item['value_type'],
            'itemids': item['itemid'],
            'sortfield': 'clock',
            'sortorder': 'DESC',
            'limit': 100
        }

        if time_from:
            params['time_from'] = time_from
        if time_till:
            params['time_till'] = time_till

        history = zapi.history.get(**params)

        if not history:
            return [TextContent(type="text", text="No history data found")]

        result = f"History for {hostname} - {item['name']}:\n"
        for record in history[:50]:  # Limit to 50 records
            from datetime import datetime
            timestamp = datetime.fromtimestamp(int(record['clock']))
            result += f"{timestamp}: {record['value']}\n"

        return [TextContent(type="text", text=result)]
    except Exception as e:
        return [TextContent(type="text", text=f"Error: {str(e)}")]

async def main():
    """Run MCP server"""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
```

**Install dependencies:**
```bash
pip install mcp pyzabbix
```

---

## Configuration by AI Tool

### Claude Code

Edit `.mcp.json`:
```json
{
  "mcpServers": {
    "aws-athena": {
      "command": "python3",
      "args": ["/Users/username/.mcp-servers/aws-athena/server.py"],
      "env": {
        "AWS_PROFILE": "default",
        "ATHENA_DATABASE": "your_database",
        "ATHENA_OUTPUT_LOCATION": "s3://your-bucket/athena-results/",
        "ATHENA_WORKGROUP": "primary"
      }
    },
    "aws-rds": {
      "command": "python3",
      "args": ["/Users/username/.mcp-servers/aws-rds/server.py"],
      "env": {
        "RDS_DB_TYPE": "postgresql",
        "RDS_HOST": "$RDS_HOST",
        "RDS_PORT": "5432",
        "RDS_DATABASE": "$RDS_DATABASE",
        "RDS_USER": "$RDS_USER",
        "RDS_PASSWORD": "$RDS_PASSWORD"
      }
    },
    "aws-glue": {
      "command": "python3",
      "args": ["/Users/username/.mcp-servers/aws-glue/server.py"],
      "env": {
        "AWS_PROFILE": "default"
      }
    },
    "aws-stepfunctions": {
      "command": "python3",
      "args": ["/Users/username/.mcp-servers/aws-stepfunctions/server.py"],
      "env": {
        "AWS_PROFILE": "default"
      }
    },
    "zabbix": {
      "command": "python3",
      "args": ["/Users/username/.mcp-servers/zabbix/server.py"],
      "env": {
        "ZABBIX_URL": "http://zabbix.example.com",
        "ZABBIX_USER": "$ZABBIX_USER",
        "ZABBIX_PASSWORD": "$ZABBIX_PASSWORD"
      }
    }
  }
}
```

### Gemini CLI, Codex CLI, GitHub Copilot CLI

Follow the same pattern as shown in each service section above, using the appropriate configuration format for each tool.

---

## Security Best Practices

### 1. Never Commit Credentials
```bash
# Add to .gitignore
.env
*.pem
*.key
*password*
*secret*
.mcp.json
settings.local.json
```

### 2. Use Environment Variables
```bash
# .env file (gitignored)
AWS_PROFILE=default
RDS_HOST=your-rds.amazonaws.com
RDS_USER=your_user
RDS_PASSWORD=your_password
ZABBIX_USER=your_user
ZABBIX_PASSWORD=your_password
```

### 3. IAM Permissions
Grant minimum required permissions:
- Athena: `AmazonAthenaFullAccess` or custom policy
- RDS: Read-only access via IAM database authentication
- Glue: `AWSGlueConsoleFullAccess` or custom policy
- Step Functions: `AWSStepFunctionsReadOnlyAccess` or custom policy

### 4. Network Security
- Use VPC endpoints for AWS services
- Restrict RDS security groups
- Use Zabbix over HTTPS
- Enable MFA for AWS accounts

### 5. Audit and Monitoring
- Enable CloudTrail for AWS API calls
- Monitor MCP server logs
- Review access patterns regularly
- Rotate credentials periodically

---

## Testing MCP Servers

### Test AWS Athena
```bash
# Start Claude Code
claude

# Test query
> Use aws-athena to list all databases

> Use aws-athena to query: SELECT * FROM my_table LIMIT 10
```

### Test AWS RDS
```bash
> Use aws-rds to list all tables

> Use aws-rds to execute query: SELECT COUNT(*) FROM users
```

### Test AWS Glue
```bash
> Use aws-glue to list all databases

> Start the glue job named 'etl-pipeline'
```

### Test AWS Step Functions
```bash
> Use aws-stepfunctions to list all state machines

> Start execution of state machine with ARN arn:aws:states:...
```

### Test Zabbix
```bash
> Use zabbix to list monitored hosts

> Get active triggers for severity 3 or higher
```

---

## Troubleshooting

### Connection Issues
```bash
# Test AWS credentials
aws sts get-caller-identity

# Test RDS connection
psql -h your-rds.amazonaws.com -U user -d database

# Test Zabbix connection
curl -X POST http://zabbix.example.com/api_jsonrpc.php \
  -H "Content-Type: application/json-rpc" \
  -d '{"jsonrpc":"2.0","method":"apiinfo.version","id":1}'
```

### Permission Errors
- Verify IAM roles and policies
- Check security groups
- Ensure MCP server has correct AWS profile

### MCP Server Not Found
- Verify script path in configuration
- Check script permissions (`chmod +x`)
- Test script directly: `python3 ~/.mcp-servers/aws-athena/server.py`

---

## Sources

- [AWS Athena Documentation](https://docs.aws.amazon.com/athena/)
- [AWS RDS Documentation](https://docs.aws.amazon.com/rds/)
- [AWS Glue Documentation](https://docs.aws.amazon.com/glue/)
- [AWS Step Functions Documentation](https://docs.aws.amazon.com/step-functions/)
- [Zabbix API Documentation](https://www.zabbix.com/documentation/current/en/manual/api)
- [MCP Protocol Specification](https://spec.modelcontextprotocol.io/)
- [psycopg2 Documentation](https://www.psycopg.org/docs/)
- [PyMySQL Documentation](https://pymysql.readthedocs.io/)
- [pyzabbix Documentation](https://github.com/lukecyca/pyzabbix)
