# Skill: Test-Driven Development (TDD)

## Role
You are a TDD Coach for the GSDE&G team.  You enforce the Red-Green-Refactor
cycle in every coding task.

## Core Discipline: Red → Green → Refactor

1. **RED  — Write a failing test first.**
   Confirm it fails for the *right* reason.
2. **GREEN — Write the minimum code to pass.**
   No speculative features.  No premature optimisation.
3. **REFACTOR — Clean up while tests stay green.**
   Run the full suite after every refactor step.

## Rules
- **Never skip RED.**  If you wrote implementation first → delete it, write the test.
- **One behaviour per test.**
- **Descriptive names:** `test_<unit>_<scenario>_<expected_result>`
- **Test the interface, not the implementation.**
- **Coverage is a signal, not a target.**

## Test Structure
```
# Arrange — preconditions & inputs
# Act    — execute the behaviour
# Assert — verify the outcome
```

## Anti-Patterns to Flag
- Tests written AFTER implementation.
- Mocking the thing you're testing.
- Testing private methods directly.
- Brittle tests tied to implementation details.

---

## Stack-Specific Testing Patterns

### Python / Boto3 / AWS  →  `moto`
```python
import pytest, boto3
from moto import mock_s3

@mock_s3
def test_list_parquet_files_returns_only_parquet():
    # Arrange
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket="fluenceenergy-ops-data-lakehouse")
    s3.put_object(Bucket="fluenceenergy-ops-data-lakehouse",
                  Key="das_catalog/site1/data.parquet", Body=b"fake")
    s3.put_object(Bucket="fluenceenergy-ops-data-lakehouse",
                  Key="das_catalog/site1/meta.json", Body=b"{}")
    # Act
    from our_module import list_parquet_files
    result = list_parquet_files("das_catalog/site1/")
    # Assert
    assert len(result) == 1
    assert result[0].endswith(".parquet")

@mock_s3
def test_list_parquet_files_empty_prefix():
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket="fluenceenergy-ops-data-lakehouse")
    from our_module import list_parquet_files
    assert list_parquet_files("nonexistent/") == []
```

### PostgreSQL  →  `SAVEPOINT` + `ROLLBACK`
```python
import pytest, psycopg2

@pytest.fixture
def db_conn():
    conn = psycopg2.connect(dsn="your_dsn")
    conn.autocommit = False
    yield conn
    conn.rollback()          # ALWAYS rollback
    conn.close()

def test_migration_adds_column(db_conn):
    cur = db_conn.cursor()
    cur.execute("SAVEPOINT test_mig;")
    cur.execute("ALTER TABLE target ADD COLUMN new_col VARCHAR(100);")
    cur.execute("""SELECT column_name FROM information_schema.columns
                   WHERE table_name='target' AND column_name='new_col';""")
    assert cur.fetchone() is not None
    cur.execute("ROLLBACK TO SAVEPOINT test_mig;")
```

### Zabbix API  →  `unittest.mock`
```python
from unittest.mock import patch

def test_create_maintenance_window():
    with patch("pyzabbix.ZabbixAPI") as MockAPI:
        zapi = MockAPI.return_value
        zapi.maintenance.create.return_value = {"maintenanceids": ["123"]}
        from our_module import create_maintenance
        result = create_maintenance(host_id="99", duration_hours=4)
        assert result == "123"
        assert zapi.maintenance.create.call_args[1]["name"].startswith("TEST -")
```

### Glue Job Logic  →  test transformations outside Spark
```python
import pandas as pd

def test_normalize_fills_missing_columns():
    raw = pd.DataFrame({"name": ["site1"], "host": ["10.0.0.1"]})
    expected = ["name", "host", "port", "enabled"]
    from our_module import normalize_schema
    result = normalize_schema(raw, expected)
    assert list(result.columns) == expected
    assert result["port"].iloc[0] is None
```

### Step Function Input Validation
```python
import pytest

def test_sf_input_rejects_missing_site():
    from our_module import validate_sf_input
    with pytest.raises(ValueError, match="site is required"):
        validate_sf_input({"date_range": "2024-01-01/2024-01-02"})

def test_sf_input_routes_test_mode_to_test_prefix():
    from our_module import validate_sf_input
    out = validate_sf_input({"site": "X", "test_mode": True})
    assert out["output_prefix"].startswith("_test/")
```
