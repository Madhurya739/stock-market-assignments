# src/analytics/cluster_profiling.py

import os
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

ARCHETYPES = {
    0: "High Growth",
    1: "Stable Performers",
    2: "Undervalued",
    3: "Risky Bets",
    4: "Cash Rich",
}


def profile_clusters(input_path: str, output_path: str):
    """TODO: Add docstring."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df = pd.read_csv(input_path)

    features = [
        "return_on_equity_pct",
        "debt_to_equity",
        "revenue_cagr_5yr",
        "fcf_cagr_5yr",
        "operating_profit_margin_pct",
    ]

    # Fill missing values with median
    for feature in features:
        df[feature] = df[feature].fillna(df[feature].median())

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[features])

    # Run KMeans
    kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
    df["cluster_id"] = kmeans.fit_predict(X_scaled)
    df["cluster_name"] = df["cluster_id"].map(ARCHETYPES)

    # ✅ Compute mean and median per cluster
    profiling = df.groupby(["cluster_id", "cluster_name"])[features].agg(
        ["mean", "median"]
    )

    profiling.to_csv(output_path)
    return profiling


if __name__ == "__main__":
    stats = profile_clusters(
        input_path="data/companies.csv", output_path="reports/cluster_profiling.csv"
    )
    print(stats)
