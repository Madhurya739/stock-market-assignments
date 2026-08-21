import pandas as pd
from rules import dq_rules

def run_validations(df, ref_df):
    failures = pd.DataFrame()

    # CRITICAL rules
    failures = pd.concat([
        dq_rules.dq01_pk_not_null(df, "id"),
        dq_rules.dq02_fk_exists(df, "fund_id", ref_df, "fund_id"),
    ])

    # WARNING rules
    failures = pd.concat([
        failures,
        dq_rules.dq03_opm_positive(df),
        dq_rules.dq04_balance_non_negative(df),
        dq_rules.dq05_sales_consistent(df),
        # … add dq06–dq16
    ])

    return failures

if __name__ == "__main__":
    df = pd.read_csv("data/processed/fact_transactions.csv")
    ref_df = pd.read_csv("data/processed/dim_fund.csv")

    failures = run_validations(df, ref_df)
    failures.to_csv("reports/validation_failures.csv", index=False)
    print("Validation complete. Failures exported to reports/validation_failures.csv")
