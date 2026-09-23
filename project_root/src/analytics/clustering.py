# src/analytics/clustering.py

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


def run_clustering(input_path: str, output_path: str):
    """
    Perform KMeans clustering on company dataset using 5 features.
    Missing values are imputed with sector median before scaling.
    Features are normalized with StandardScaler (zero mean, unit variance).
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df = pd.read_csv(input_path)

    features = [
        "return_on_equity_pct",
        "debt_to_equity",
        "revenue_cagr_5yr",
        "fcf_cagr_5yr",
        "operating_profit_margin_pct",
    ]

    # ✅ Impute missing values with sector median (or global median fallback)
    if "sector" in df.columns:
        for feature in features:
            df[feature] = df.groupby("sector")[feature].transform(
                lambda x: x.fillna(x.median())
            )
    else:
        for feature in features:
            df[feature] = df[feature].fillna(df[feature].median())

    # ✅ Normalize features with StandardScaler
    X = df[features].copy()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # ✅ Run KMeans with reproducibility
    kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
    df["cluster"] = kmeans.fit_predict(X_scaled)

    # ✅ Map clusters to archetypes
    df["archetype"] = df["cluster"].map(ARCHETYPES)

    df.to_csv(output_path, index=False)
    return df


if __name__ == "__main__":
    clustered_df = run_clustering(
        input_path="data/companies.csv", output_path="data/companies_clustered.csv"
    )
    print(clustered_df.head())
