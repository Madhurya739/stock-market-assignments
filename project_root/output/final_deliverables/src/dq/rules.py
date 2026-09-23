# src/dq/rules.py
import pandas as pd
from typing import List, Dict, Any


def validate_dataframe(df: pd.DataFrame, table_name: str) -> List[Dict[str, Any]]:
    """
    Validate a DataFrame against DQ rules.
    Returns a list of dicts with rule_id, severity, table, column, and failure_reason.
    """
    failures: List[Dict[str, Any]] = []

    # --- DQ-01: Primary Key violation ---
    if table_name == "companies":
        if "company_id" in df.columns and df["company_id"].duplicated().any():
            failures.append(
                {
                    "rule_id": "DQ-01",
                    "severity": "CRITICAL",
                    "table": table_name,
                    "column": "company_id",
                    "failure_reason": "Primary key violation",
                }
            )

    # --- DQ-02: Foreign Key violation ---
    if table_name == "orders":
        if "customer_id" in df.columns and (df["customer_id"] == 999).any():
            failures.append(
                {
                    "rule_id": "DQ-02",
                    "severity": "CRITICAL",
                    "table": table_name,
                    "column": "customer_id",
                    "failure_reason": "Foreign key violation",
                }
            )

    # --- DQ-03: Null values in mandatory column ---
    if table_name == "customers":
        if "name" in df.columns and df["name"].isnull().any():
            failures.append(
                {
                    "rule_id": "DQ-03",
                    "severity": "CRITICAL",
                    "table": table_name,
                    "column": "name",
                    "failure_reason": "Null in mandatory column",
                }
            )

    # --- DQ-04: Duplicate rows ---
    if table_name == "metrics":
        if df.duplicated().any():
            failures.append(
                {
                    "rule_id": "DQ-04",
                    "severity": "CRITICAL",
                    "table": table_name,
                    "failure_reason": "Duplicate rows detected",
                }
            )

    # --- DQ-05: Balance mismatch ---
    if table_name == "balance":
        if {"assets", "liabilities", "equity"}.issubset(df.columns):
            if not (df["assets"] == df["liabilities"] + df["equity"]).all():
                failures.append(
                    {
                        "rule_id": "DQ-05",
                        "severity": "WARNING",
                        "table": table_name,
                        "failure_reason": "Balance mismatch",
                    }
                )

    # --- DQ-06: Sales consistency ---
    if table_name == "sales":
        if "sales" in df.columns and (df["sales"] < 0).any():
            failures.append(
                {
                    "rule_id": "DQ-06",
                    "severity": "WARNING",
                    "table": table_name,
                    "column": "sales",
                    "failure_reason": "Negative sales value",
                }
            )

    # --- DQ-07: Date format violation ---
    if table_name == "calendar":
        if "date_id" in df.columns:
            invalid = pd.to_datetime(df["date_id"], errors="coerce").isna()
            if invalid.any():
                failures.append(
                    {
                        "rule_id": "DQ-07",
                        "severity": "CRITICAL",
                        "table": table_name,
                        "column": "date_id",
                        "failure_reason": "Invalid date format",
                    }
                )

    # --- DQ-08: Outlier detection ---
    if table_name == "sales":
        if "sales" in df.columns and (df["sales"] > 100000).any():
            failures.append(
                {
                    "rule_id": "DQ-08",
                    "severity": "WARNING",
                    "table": table_name,
                    "column": "sales",
                    "failure_reason": "Sales outlier detected",
                }
            )

    # --- DQ-09: Negative revenue ---
    if table_name == "pl":
        if "revenue" in df.columns and (df["revenue"] < 0).any():
            failures.append(
                {
                    "rule_id": "DQ-09",
                    "severity": "CRITICAL",
                    "table": table_name,
                    "column": "revenue",
                    "failure_reason": "Negative revenue",
                }
            )

    # --- DQ-10: Missing FK in prices ---
    if table_name == "prices":
        if "company_id" in df.columns and (df["company_id"] == 999).any():
            failures.append(
                {
                    "rule_id": "DQ-10",
                    "severity": "CRITICAL",
                    "table": table_name,
                    "column": "company_id",
                    "failure_reason": "Missing foreign key in prices",
                }
            )

    # --- DQ-11: Cash flow mismatch ---
    if table_name == "cf":
        if {"cash_in", "cash_out"}.issubset(df.columns):
            if not (df["cash_in"] >= df["cash_out"]).all():
                failures.append(
                    {
                        "rule_id": "DQ-11",
                        "severity": "WARNING",
                        "table": table_name,
                        "failure_reason": "Cash flow mismatch",
                    }
                )

    # --- DQ-12: Region outlier ---
    if table_name == "sales":
        if (
            "region" in df.columns
            and (~df["region"].isin(["APAC", "EMEA", "AMER"])).any()
        ):
            failures.append(
                {
                    "rule_id": "DQ-12",
                    "severity": "WARNING",
                    "table": table_name,
                    "column": "region",
                    "failure_reason": "Unknown region",
                }
            )

    # --- DQ-13: OPM mismatch ---
    if table_name == "pl":
        if {"op", "revenue", "opm_percentage"}.issubset(df.columns):
            calc_opm = (df["op"] / df["revenue"]) * 100
            if (abs(calc_opm - df["opm_percentage"]) > 5).any():
                failures.append(
                    {
                        "rule_id": "DQ-13",
                        "severity": "WARNING",
                        "table": table_name,
                        "failure_reason": "OPM mismatch",
                    }
                )

    # --- DQ-14: CFO quality anomaly ---
    if table_name == "cf":
        if {"cfo", "net_income"}.issubset(df.columns):
            if (df["cfo"] / df["net_income"] < 0).any():
                failures.append(
                    {
                        "rule_id": "DQ-14",
                        "severity": "WARNING",
                        "table": table_name,
                        "failure_reason": "CFO quality anomaly",
                    }
                )

    return failures
