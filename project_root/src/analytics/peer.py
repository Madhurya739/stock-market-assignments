# src/analytics/peer.py

import pandas as pd

def compute_peer_percentiles(filepath="peer_groups.xlsx"):
    """
    Load peer_groups.xlsx and compute percentile ranks for 10 metrics
    within each of 11 peer groups.
    """

    # Load peer group data
    df = pd.read_excel(filepath)

    # Define metrics to rank
    metrics = [
        "ROE", "ROCE", "NPM",
        "FCF_CAGR", "CFO_PAT", "Revenue_CAGR_5yr",
        "PAT_CAGR_5yr", "DE", "ICR", "PE"
    ]

    # Compute percentile ranks within each peer group
    for metric in metrics:
        df[f"{metric}_PERCENT_RANK"] = df.groupby("peer_group")[metric].rank(
            pct=True, method="average"
        ) * 100  # scale to 0–100

    return df
