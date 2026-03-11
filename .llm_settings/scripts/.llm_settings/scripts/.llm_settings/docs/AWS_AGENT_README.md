# AWS Cloud Management & FinOps Agent

> A Claude Code skill that acts as a Principal AWS Cloud Engineer and FinOps specialist for the GSDE&G team at Fluence Energy.

---

## What This Agent Does

This agent transforms Claude Code into an expert AWS infrastructure analyst and cost optimizer. It knows your entire Fluence Energy AWS environment — the CDAS servers, the FODL data lakehouse, the tagging gaps, the cost centers — and operates with strict safety guardrails to inventory, analyze, and optimize every resource across every region.

### Core Capabilities

**Full-Account Inventory**
Scans every enabled AWS region and catalogs every resource type: EC2 instances, EBS volumes, S3 buckets, RDS databases, Glue jobs, Step Functions, Athena workgroups, Lambda functions, NAT Gateways, VPC Endpoints, EIPs, ENIs, snapshots, and AMIs. Produces structured CSV/JSON inventories with complete tag information.

**Cost Analysis & Optimization**
Queries AWS Cost Explorer and correlates spend to resources by tag, service, and department. Identifies the top cost drivers, calculates savings opportunities, and ranks recommendations by impact and risk. Understands the FY26 40% cost reduction target and the adjusted 53% reduction needed for the remaining 8 months.

**Rightsizing Recommendations**
Pulls CloudWatch metrics (CPU, memory, disk I/O, network, IOPS, throughput, queue length) and AWS Compute Optimizer data to produce evidence-based rightsizing recommendations. Understands the difference between "this instance is oversized" and "this EBS volume is a bottleneck that needs *more* resources, not fewer."

**Tag Governance**
Audits every resource against the required tagging standard (CostCenter, Owner, Environment, System, DataDomain, FOD, CostReductionTarget, DataRetentionTier). Identifies gaps, proposes exact tag values, and applies tags in safe batches with checkpoint logging.

**Script Generation**
Every AWS CLI command or boto3 call the agent uses is captured as a reusable bash and/or python script in the `./scripts/` directory. Change scripts always support `--dry-run` (default) and `--apply` modes with full logging and rollback plans.

---

## Installation

### Directory Structure

Place the skill folder in your Claude Code skills directory:

```
your-project/
├── aws/
│   ├── SKILL.md              ← Agent instructions (Claude Code reads this)
│   └── AWS_AGENT_README.md   ← This file (human documentation)
│
├── scripts/                   ← Agent writes scripts here
│   ├── 00_prereqs_check.sh
│   ├── 01_discover_regions.sh
│   ├── 10_inventory_ec2.sh
│   └── ...
│
├── reports/                   ← Agent writes reports here
│   ├── inventory_all_regions.csv
│   ├── tag_coverage_report.csv
│   ├── rightsizing_recommendations.md
│   └── ...
│
├── logs/                      ← Script execution logs
│
└── docs/
    └── FY26_Cost_Reduction_Plan.md
```

### Prerequisites

The agent expects these tools to be available in the environment where scripts will run:

| Tool | Version | Purpose |
|------|---------|---------|
| AWS CLI | v2+ | All AWS API interactions |
| Python 3 | 3.9+ | boto3 scripts, analysis |
| boto3 | Latest | Python AWS SDK |
| jq | 1.6+ | JSON processing in bash scripts |
| pandas | Optional | Data analysis in python scripts |

### Required IAM Permissions

The agent operates read-only by default. At minimum, the IAM principal running the scripts needs:

**Read-Only (Discovery & Analysis):**
- `ec2:Describe*`
- `rds:Describe*`
- `s3:ListAllMyBuckets`, `s3:GetBucketLocation`, `s3:GetBucketTagging`, `s3:ListBucket`, `s3:GetStorageLensConfiguration`
- `elasticfilesystem:Describe*`
- `glue:Get*`, `glue:List*`
- `athena:List*`, `athena:Get*`
- `states:List*`, `states:Describe*`
- `lambda:List*`, `lambda:Get*`
- `cloudwatch:GetMetricData`, `cloudwatch:GetMetricStatistics`, `cloudwatch:ListMetrics`
- `compute-optimizer:GetEC2InstanceRecommendations`, `compute-optimizer:GetEBSVolumeRecommendations`
- `ce:GetCostAndUsage`, `ce:GetCostForecast`, `ce:GetSavingsPlansUtilization`
- `tag:GetResources`, `tag:GetTagKeys`, `tag:GetTagValues`
- `iam:ListAccountAliases`
- `organizations:DescribeOrganization` (optional, for multi-account)

**Write (Remediation — Only Used With `--apply`):**
- `ec2:CreateTags`, `ec2:ModifyVolume`, `ec2:ModifyInstanceAttribute`, `ec2:StopInstances`, `ec2:StartInstances`
- `rds:AddTagsToResource`, `rds:ModifyDBInstance`
- `s3:PutBucketLifecycleConfiguration`, `s3:PutBucketTagging`
- `tag:TagResources`

---

## How to Use

### Triggering the Agent

The agent activates when you ask Claude Code anything related to AWS. Examples:

```
"Inventory all EC2 instances across every region"
"Which EBS volumes are running at 100% utilization?"
"Show me the top 10 cost drivers for Global Services"
"Tag all FODL resources with FOD=true"
"Right-size our RDS instances based on the last 30 days of metrics"
"Generate a script to apply S3 lifecycle policies to the data lakehouse"
"How are we tracking against the FY26 40% cost reduction target?"
"Find all unattached EBS volumes and orphaned snapshots"
```

### Typical Workflows

**1. Full Account Inventory**

Ask: *"Run a complete inventory of all AWS resources across all regions with tags."*

The agent will:
- Enumerate all enabled regions
- Scan EC2, EBS, S3, RDS, Glue, Step Functions, Athena, Lambda, and misc resources per region
- Compile `reports/inventory_all_regions.csv` with all tags
- Produce `reports/tag_coverage_report.csv` showing missing required tags
- Generate all discovery scripts in `./scripts/`

**2. Cost Reduction Analysis**

Ask: *"Analyze our Global Services costs and recommend optimizations to hit the 40% reduction target."*

The agent will:
- Query Cost Explorer by CostCenter tag
- Identify top cost drivers ranked by monthly spend
- Pull CloudWatch metrics for EC2, EBS, and RDS utilization
- Produce `reports/top_cost_drivers_summary.md` and `reports/rightsizing_recommendations.md`
- Estimate savings per recommendation
- Generate analysis scripts

**3. EBS Performance Tuning**

Ask: *"Our EBS volumes on the DAS servers are at 100% busy. Diagnose and fix."*

The agent will:
- Pull `VolumeReadOps`, `VolumeWriteOps`, `VolumeQueueLength`, `BurstBalance`, `VolumeThroughputPercentage` metrics
- Diagnose whether the bottleneck is IOPS, throughput, or instance EBS bandwidth
- Recommend gp2→gp3 migration with specific IOPS/throughput values (observed p95 + 20-30% headroom)
- Generate `scripts/31_tune_ebs.py` for analysis and `scripts/42_apply_ebs_modify.sh` for remediation

**4. Tag Remediation**

Ask: *"Audit all tags and apply FOD=true to every FODL resource."*

The agent will:
- Use Resource Groups Tagging API to dump all current tags
- Cross-reference against the required tagging standard
- Produce `reports/tag_remediation_plan.json` with exact tags per resource
- Present the plan for approval
- Apply tags in batches of ≤25 with checkpoint logging (only after `--apply` confirmation)

**5. Orphaned Resource Cleanup**

Ask: *"Find all orphaned resources we can safely remove."*

The agent will:
- Find EC2 instances stopped for >30 days
- Find EBS volumes not attached to any instance
- Find snapshots older than retention policy
- Find unused Elastic IPs
- Produce `reports/orphaned_resources.csv` with estimated monthly savings
- Generate candidate lists — **never deletes automatically**

---

## Safety Model

The agent is designed to be safe by default. Here is what it will and will not do:

### Always Safe (No Approval Needed)

- Read and inventory any resource in any region
- Pull CloudWatch metrics and Compute Optimizer recommendations
- Query Cost Explorer and billing data
- Generate reports, CSVs, and markdown summaries
- Write scripts to `./scripts/`

### Requires Explicit Approval

- Applying tags (presented in batches for review first)
- Resizing EC2 instances (requires maintenance window guidance)
- Modifying EBS volumes (requires performance baseline documentation)
- Resizing RDS instances (requires maintenance window guidance)
- Applying S3 lifecycle policies (requires backup verification)
- Stopping long-idle instances

### Never Done Automatically

- Terminating EC2 instances (candidates list only, per-instance confirmation)
- Deleting EBS volumes or snapshots (candidates list only)
- Deleting S3 objects (lifecycle policies only, never direct deletion)
- Any destructive action without a rollback plan

### Change Script Safety

Every change script the agent produces:

- Defaults to `--dry-run` mode — shows what would change without changing anything
- Requires explicit `--apply` flag to make changes
- Logs every action to `./logs/` with timestamps
- Outputs a change plan as CSV/JSON before execution
- Includes rollback guidance or a companion `rollback_*.sh` script

---

## Script Naming Convention

Scripts follow a numbered convention that reflects the workflow order:

| Range | Category | Examples |
|-------|----------|---------|
| `00-09` | Prerequisites & setup | `00_prereqs_check.sh`, `01_discover_regions.sh` |
| `10-19` | Discovery & inventory | `10_inventory_ec2.sh`, `12_inventory_s3.py` |
| `20-29` | Cost analysis | `20_cost_by_tag.py`, `22_cost_untagged.py` |
| `30-39` | Rightsizing analysis | `30_rightsize_ec2.py`, `31_tune_ebs.py` |
| `40-49` | Remediation (changes) | `40_apply_tags.sh`, `42_apply_ebs_modify.sh` |
| `50-59` | Rollback | `50_rollback_ec2_resize.sh` |
| `99` | Reporting | `99_generate_full_report.py` |

Every script includes: shebang, description header with usage instructions, argument parsing, error handling, logging, and structured output.

---

## Tagging Standard

The agent enforces and audits against this tagging standard:

| Tag | Required | Values | Purpose |
|-----|----------|--------|---------|
| `CostCenter` | ✅ | `GlobalServices`, `GSDE`, `GSPerformanceAnalytics`, `ServicesTeam`, `Technology`, `NetworkIT`, `Marketing`, `Americas` | Department cost attribution |
| `Owner` | ✅ | Team or individual name | Who is responsible |
| `Environment` | ✅ | `prod`, `dev`, `test`, `staging`, `decommissioned` | Lifecycle stage |
| `System` | ✅ | `CDAS`, `FODL`, `Zabbix`, `Mango`, etc. | Which system this belongs to |
| `DataDomain` | ✅ | `GlobalServicesData`, `OperationalData`, `PerformanceData` | Data classification |
| `FOD` | ✅ | `true` / `false` | Fluence Operational Data flag for FY26 cost tracking |
| `CostReductionTarget` | Conditional | `FY26` or empty | In scope for 40% reduction |
| `DataRetentionTier` | Conditional | `hot`, `warm`, `cold`, `archive` | S3 storage tier classification |

---

## FY26 Cost Reduction Context

The agent is pre-loaded with full context on the FY26 initiative:

- **Target:** 40% full-year cost reduction on Global Services AWS resources
- **Adjusted target:** ~53% reduction for the remaining 8 months (4 months of FY26 have elapsed at full spend)
- **In-scope departments:** Services Team (~$169K/mo), GSDataEngineering (~$66K/mo), GSPerformanceAnalytics (~$3K/mo)
- **Out-of-scope:** Technology/CPO, Network/IT, Marketing, Americas (inventory and tag only)
- **Total monthly target savings:** ~$95K/mo across Global Services

### Key Savings Levers the Agent Pursues

| Lever | Est. Monthly Savings | Approach |
|-------|---------------------|----------|
| EC2 Rightsizing | ~$56K | Graviton migration, instance downsizing, terminate stopped |
| S3 Lifecycle | ~$20K | Intelligent-Tiering, Glacier Deep Archive for 2016–2024 data |
| RDS Optimization | ~$8K | Consolidate 14 MySQL instances, Reserved Instances |
| Data Transfer | ~$6K | VPC endpoints, review cross-region DR replication |
| Orphaned Resources | ~$5K | Unattached EBS, old snapshots, stopped instances |

---

## Infrastructure the Agent Understands

### CDAS (Central Data Acquisition Systems)
- 37+ EC2 instances (mostly r5.4xlarge @ ~$1.01/hr each)
- Running Mango Automation (3rd party data acquisition)
- MySQL RDS backends for configuration and metadata
- EBS volumes storing proprietary NoSQL format data
- Owned by the Services Team

### FODL (Fluence Operational Data Lakehouse)
- 2x r6g.16xlarge extraction servers (enst01as01pr, enst01as02pr @ ~$3.22/hr each)
- PostgreSQL RDS metadata store (fe-gsdl-poc-database, db.t3.2xlarge)
- 14 MySQL RDS instances for CDAS metadata
- S3 Parquet data lake (~275TB total, ~3TB/day ingestion, data from 2016–present)
- Athena query layer, Step Functions + Glue ETL pipelines
- Owned by GSDataEngineering

---

## Multi-Account & Future Proofing

All scripts accept `--profile` and `--role-arn` parameters for cross-account use via STS AssumeRole. Reports are structured to support aggregation across multiple AWS accounts if the organization scales to that model.

---

## Customization

### Modifying the Tagging Standard

Edit the **Tagging Standard** section in `SKILL.md` to add, remove, or rename required tags. The agent will audit and remediate against whatever tags are listed there.

### Changing Cost Reduction Targets

Update the **FY26 Cost Reduction Context** section in `SKILL.md` with new targets, department scopes, or monthly spend figures as they change.

### Adding New AWS Services

The agent already covers the major cost-driving services. To add coverage for additional services (e.g., ECS, EKS, DynamoDB), add them to the **Deliverables > Scripts** section in `SKILL.md` with appropriate inventory script numbers.

### Adjusting Safety Guardrails

The **Guardrails** table at the bottom of `SKILL.md` controls what the agent can and cannot do. Modify the conditions to tighten or relax safety as your team's comfort level evolves.

---

## Troubleshooting

| Issue | Resolution |
|-------|-----------|
| Agent doesn't scan all regions | Verify `SKILL.md` Rule 1 is intact; check IAM permissions for `ec2:DescribeRegions` |
| Scripts fail with permission errors | Verify the IAM principal has the required read/write permissions listed above |
| Agent tries to delete resources | This should never happen — the guardrails explicitly prevent it. If it does, check that `SKILL.md` hasn't been modified |
| Tag remediation plan is empty | Verify `resourcegroupstaggingapi` permissions and that resources exist in the expected regions |
| Cost Explorer returns no data | Cost allocation tags must be activated in the AWS Billing console (takes 24 hours to propagate) |
| Agent recommends downsizing a bottlenecked resource | Report this — the EBS performance analysis pattern should catch this. The agent should recommend *more* resources for bottlenecked volumes, not fewer |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | February 2026 | Initial release — full inventory, cost analysis, rightsizing, tagging, FY26 cost reduction context |
