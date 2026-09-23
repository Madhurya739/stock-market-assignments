# src/analytics/cluster_labels.py

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


def generate_cluster_labels(input_path: str, output_path: str):
    """
    Run KMeans clustering and export cluster labels with distance from centroid.
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

    # Fill missing values with median
    for feature in features:
        df[feature] = df[feature].fillna(df[feature].median())

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[features])

    # Run KMeans
    kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
    cluster_ids = kmeans.fit_predict(X_scaled)

    # Compute distances from centroid
    distances = []
    for i, x in enumerate(X_scaled):
        centroid = kmeans.cluster_centers_[cluster_ids[i]]
        dist = ((x - centroid) ** 2).sum() ** 0.5
        distances.append(dist)

    # Build output DataFrame
    output_df = pd.DataFrame(
        {
            "company_id": df.index + 1,  # or use df["company"] if you want names
            "cluster_id": cluster_ids,
            "cluster_name": [ARCHETYPES[c] for c in cluster_ids],
            "distance_from_centroid": distances,
        }
    )

    output_df.to_csv(output_path, index=False)
    return output_df


if __name__ == "__main__":
    clustered_labels = generate_cluster_labels(
        input_path="data/companies.csv", output_path="output/cluster_labels.csv"
    )
    print(clustered_labels.head())
