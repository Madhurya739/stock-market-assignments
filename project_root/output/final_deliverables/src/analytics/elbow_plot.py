# src/analytics/elbow_plot.py

import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def generate_elbow_plot(input_path: str, output_path: str):
    """
    Generate elbow plot (inertia vs k) for KMeans clustering.
    Saves plot as reports/elbow_plot.png.
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

    # ✅ Impute missing values with global median
    for feature in features:
        df[feature] = df[feature].fillna(df[feature].median())

    # ✅ Normalize features
    X = df[features].copy()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # ✅ Compute inertia for k=2..10
    inertias = []
    ks = range(2, 11)
    for k in ks:
        kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
        kmeans.fit(X_scaled)
        inertias.append(kmeans.inertia_)

    # ✅ Plot elbow curve
    plt.figure(figsize=(8, 6))
    plt.plot(ks, inertias, marker="o")
    plt.xlabel("Number of clusters (k)")
    plt.ylabel("Inertia")
    plt.title("Elbow Plot for KMeans")
    plt.grid(True)

    plt.savefig(output_path)
    plt.close()

    return inertias


if __name__ == "__main__":
    inertias = generate_elbow_plot(
        input_path="data/companies.csv", output_path="reports/elbow_plot.png"
    )
    print("Inertias:", inertias)
    print("Check elbow: k=5 should be near the bend.")
