import pandas as pd

def dq01_pk_not_null(df, pk_col):
    """CRITICAL: Primary key must not be null"""
    return df[df[pk_col].isnull()].assign(rule="DQ-01 PK Not Null", severity="CRITICAL")

def dq02_fk_exists(df, fk_col, ref_df, ref_col):
    """CRITICAL: Foreign key must exist in reference table"""
    invalid = df[~df[fk_col].isin(ref_df[ref_col])]
    return invalid.assign(rule="DQ-02 FK Exists", severity="CRITICAL")

def dq03_opm_positive(df, col="opm"):
    """WARNING: Operating margin must be >= 0"""
    return df[df[col] < 0].assign(rule="DQ-03 OPM Positive", severity="WARNING")

def dq04_balance_non_negative(df, col="balance"):
    """WARNING: Balance must be >= 0"""
    return df[df[col] < 0].assign(rule="DQ-04 Balance Non-Negative", severity="WARNING")

def dq05_sales_consistent(df, col="sales"):
    """WARNING: Sales must be > 0"""
    return df[df[col] <= 0].assign(rule="DQ-05 Sales Consistent", severity="WARNING")

# … continue defining DQ-06 … DQ-16
