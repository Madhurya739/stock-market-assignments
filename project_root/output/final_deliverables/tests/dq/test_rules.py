import pandas as pd
from src.dq import rules


# Helper to run validation and extract rule_ids
def run_validation(df, table_name):
    failures = rules.validate_dataframe(df, table_name)
    return [f["rule_id"] for f in failures], [f["severity"] for f in failures]


# --- DQ-01: Primary Key violation ---
def test_dq01_primary_key_violation():
    df = pd.DataFrame({"company_id": [1, 1], "name": ["A", "B"]})
    rule_ids, severities = run_validation(df, "companies")
    assert "DQ-01" in rule_ids
    assert "CRITICAL" in severities


# --- DQ-02: Foreign Key violation ---
def test_dq02_foreign_key_violation():
    df = pd.DataFrame({"order_id": [1], "customer_id": [999]})
    rule_ids, severities = run_validation(df, "orders")
    assert "DQ-02" in rule_ids
    assert "CRITICAL" in severities


# --- DQ-03: Null values in mandatory column ---
def test_dq03_null_mandatory_column():
    df = pd.DataFrame({"id": [1, 2], "name": ["X", None]})
    rule_ids, severities = run_validation(df, "customers")
    assert "DQ-03" in rule_ids
    assert "CRITICAL" in severities


# --- DQ-04: Duplicate rows ---
def test_dq04_duplicate_rows():
    df = pd.DataFrame({"id": [1, 1], "value": [10, 10]})
    rule_ids, severities = run_validation(df, "metrics")
    assert "DQ-04" in rule_ids
    assert "CRITICAL" in severities


# --- DQ-05: Balance mismatch ---
def test_dq05_balance_mismatch():
    df = pd.DataFrame({"assets": [100], "liabilities": [80], "equity": [30]})
    rule_ids, severities = run_validation(df, "balance")
    assert "DQ-05" in rule_ids
    assert "WARNING" in severities


# --- DQ-06: Sales consistency ---
def test_dq06_sales_consistency():
    df = pd.DataFrame({"region": ["APAC"], "sales": [-100]})
    rule_ids, severities = run_validation(df, "sales")
    assert "DQ-06" in rule_ids
    assert "WARNING" in severities


# --- DQ-07: Date format violation ---
def test_dq07_date_format_violation():
    df = pd.DataFrame({"date_id": ["2026-99-99"]})
    rule_ids, severities = run_validation(df, "calendar")
    assert "DQ-07" in rule_ids
    assert "CRITICAL" in severities


# --- DQ-08: Outlier detection ---
def test_dq08_outlier_detection():
    df = pd.DataFrame({"sales": [999999]})
    rule_ids, severities = run_validation(df, "sales")
    assert "DQ-08" in rule_ids
    assert "WARNING" in severities


# --- DQ-09: Negative revenue ---
def test_dq09_negative_revenue():
    df = pd.DataFrame({"revenue": [-50]})
    rule_ids, severities = run_validation(df, "pl")
    assert "DQ-09" in rule_ids
    assert "CRITICAL" in severities


# --- DQ-10: Missing FK in prices ---
def test_dq10_missing_fk_prices():
    df = pd.DataFrame({"company_id": [999], "price": [100]})
    rule_ids, severities = run_validation(df, "prices")
    assert "DQ-10" in rule_ids
    assert "CRITICAL" in severities


# --- DQ-11: Cash flow mismatch ---
def test_dq11_cash_flow_mismatch():
    df = pd.DataFrame({"cash_in": [100], "cash_out": [200]})
    rule_ids, severities = run_validation(df, "cf")
    assert "DQ-11" in rule_ids
    assert "WARNING" in severities


# --- DQ-12: Region outlier ---
def test_dq12_region_outlier():
    df = pd.DataFrame({"region": ["UNKNOWN"], "sales": [100]})
    rule_ids, severities = run_validation(df, "sales")
    assert "DQ-12" in rule_ids
    assert "WARNING" in severities


# --- DQ-13: OPM mismatch ---
def test_dq13_opm_mismatch():
    df = pd.DataFrame({"op": [40], "revenue": [200], "opm_percentage": [50]})
    rule_ids, severities = run_validation(df, "pl")
    assert "DQ-13" in rule_ids
    assert "WARNING" in severities


# --- DQ-14: CFO quality anomaly ---
def test_dq14_cfo_quality_anomaly():
    df = pd.DataFrame({"cfo": [-100], "net_income": [400]})
    rule_ids, severities = run_validation(df, "cf")
    assert "DQ-14" in rule_ids
    assert "WARNING" in severities
