import os
import logging
import pandas as pd

# Configure logging once
os.makedirs("output", exist_ok=True)
logging.basicConfig(filename="output/ratio_edge_cases.log", level=logging.INFO)


def process_ratios(df: pd.DataFrame):
    """
    Pipeline:
    1. Suppress D/E warning for Financials sector
    2. Compute ROCE and cross-check vs source
    3. Compute ROE and cross-check vs source
    4. Log anomalies with category tags
    """

    def leverage_flag(row):
        if row["broad_sector"] == "Financials":
            return False
        de_ratio = row["borrowings"] / (row["equity_capital"] + row["reserves"])
        return de_ratio > 5

    df["high_leverage_flag"] = df.apply(leverage_flag, axis=1)

    for _, row in df.iterrows():
        # --- ROCE check ---
        computed_roce = (
            row["ebit"] / (row["equity_capital"] + row["reserves"] + row["borrowings"])
        ) * 100
        source_roce = row["roce_percentage"]

        if abs(computed_roce - source_roce) > 5:
            logging.info(
                f"{row['company_id']} {row['year']} ROCE anomaly: "
                f"computed={computed_roce:.2f}, source={source_roce:.2f} | Category=Formula Discrepancy"
            )

        # --- ROE check ---
        computed_roe = (
            row["net_profit"] / (row["equity_capital"] + row["reserves"])
        ) * 100
        source_roe = row["roe_percentage"]

        if abs(computed_roe - source_roe) > 5:
            # Example categorisation: source issue
            logging.info(
                f"{row['company_id']} {row['year']} ROE anomaly: "
                f"computed={computed_roe:.2f}, source={source_roe:.2f} | Category=Data Source Issue"
            )

        # Store computed values for analytics
        df.loc[row.name, "computed_roce"] = computed_roce
        df.loc[row.name, "computed_roe"] = computed_roe

    return df
