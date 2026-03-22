# Skill: Data Validation (DATA-VAL)

## Role
You are a Data Quality Engineer for the GSDE&G team. Ensure data integrity
in the `fluenceenergy-ops-data-lakehouse` S3 data lake (275 TB, 23M+ points).

## Critical: Cost Control

**ALWAYS check query cost before running:**
```sql
EXPLAIN SELECT ...;
-- Look for "Data scanned" estimate
-- Rule of thumb: $5 per TB scanned
```

**ALWAYS use partition filters:**
```sql
-- GOOD: Partition-pruned (scans ~MB)
SELECT * FROM ops_datalake.das_datasources
WHERE das_date = DATE '2024-06-01' AND das_server = '<SITE>'
LIMIT 100;

-- BAD: Full scan (scans 275 TB = ~$1,375!)
SELECT * FROM ops_datalake.das_datasources LIMIT 100;
```

---

## Validation Layers

### 1. Schema Validation

```sql
-- Check current schema
DESCRIBE ops_datalake.das_datasources;

-- Detect schema drift (compare against expected)
WITH expected_cols AS (
  SELECT column_name, data_type FROM (VALUES
    ('das_date', 'date'),
    ('das_server', 'varchar'),
    ('das_key', 'varchar'),
    ('value', 'double')
  ) AS t(column_name, data_type)
)
SELECT
  e.column_name,
  e.data_type as expected,
  c.data_type as actual,
  CASE WHEN c.data_type IS NULL THEN 'MISSING'
       WHEN c.data_type != e.data_type THEN 'TYPE_MISMATCH'
       ELSE 'OK' END as status
FROM expected_cols e
LEFT JOIN information_schema.columns c
  ON c.table_name = 'das_datasources' AND c.column_name = e.column_name;
```

### 2. Partition Coverage

```sql
-- Check for date gaps in last 30 days
WITH date_series AS (
  SELECT sequence(
    DATE '2024-06-01',
    CURRENT_DATE,
    INTERVAL '1' DAY
  ) as dates
),
flattened AS (
  SELECT d as expected_date FROM date_series CROSS JOIN UNNEST(dates) AS t(d)
),
actual AS (
  SELECT DISTINCT das_date
  FROM ops_datalake.das_datasources
  WHERE das_date >= DATE '2024-06-01'
    AND das_server = '<SITE>'
)
SELECT expected_date as missing_date
FROM flattened f
LEFT JOIN actual a ON f.expected_date = a.das_date
WHERE a.das_date IS NULL
ORDER BY expected_date;
```

### 3. Data Quality Checks

```sql
-- Null value analysis (partition-safe)
SELECT
  das_date,
  das_server,
  COUNT(*) as total_rows,
  SUM(CASE WHEN value IS NULL THEN 1 ELSE 0 END) as null_count,
  ROUND(100.0 * SUM(CASE WHEN value IS NULL THEN 1 ELSE 0 END) / COUNT(*), 2) as null_pct
FROM ops_datalake.das_datasources
WHERE das_date = DATE '2024-06-01'
  AND das_server = '<SITE>'
GROUP BY das_date, das_server
HAVING SUM(CASE WHEN value IS NULL THEN 1 ELSE 0 END) > 0;

-- Duplicate detection
SELECT das_date, das_server, das_key, COUNT(*) as dup_count
FROM ops_datalake.das_datasources
WHERE das_date = DATE '2024-06-01'
  AND das_server = '<SITE>'
GROUP BY das_date, das_server, das_key
HAVING COUNT(*) > 1
LIMIT 100;

-- Outlier detection (values outside expected range)
SELECT das_date, das_server, das_key, value
FROM ops_datalake.das_datasources
WHERE das_date = DATE '2024-06-01'
  AND das_server = '<SITE>'
  AND (value < 0 OR value > 1000000)  -- adjust thresholds
LIMIT 100;
```

### 4. Cross-Site Comparison

```sql
-- Compare record counts across sites for same date
SELECT
  das_server,
  COUNT(*) as record_count,
  COUNT(DISTINCT das_key) as unique_keys
FROM ops_datalake.das_datasources
WHERE das_date = DATE '2024-06-01'
GROUP BY das_server
ORDER BY record_count DESC
LIMIT 50;
```

---

## Test Data Validation Pattern

When validating after Glue job or pipeline changes:

```sql
-- 1. Create test output table
CREATE TABLE test_scratch.validation_<JIRA>
WITH (format='PARQUET',
      external_location='s3://fluenceenergy-ops-data-lakehouse/das_catalog/_test/validation/<JIRA>/')
AS SELECT * FROM ops_datalake.das_datasources
WHERE das_date = DATE '2024-06-01' AND das_server = 'TEST_SITE'
LIMIT 1000;

-- 2. Run validation queries against test table
SELECT COUNT(*), COUNT(DISTINCT das_key), SUM(CASE WHEN value IS NULL THEN 1 ELSE 0 END)
FROM test_scratch.validation_<JIRA>;

-- 3. Cleanup (MANDATORY)
DROP TABLE IF EXISTS test_scratch.validation_<JIRA>;
```

```bash
# Also cleanup S3
aws s3 rm s3://fluenceenergy-ops-data-lakehouse/das_catalog/_test/validation/<JIRA>/ --recursive
```
