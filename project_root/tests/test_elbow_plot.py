import os
from src.analytics.elbow_plot import generate_elbow_plot


def test_generate_elbow_plot_creates_file(tmp_path):
    # Arrange: create dummy input CSV
    input_path = tmp_path / "companies.csv"
    output_path = tmp_path / "elbow_plot.png"

    import pandas as pd
    import numpy as np

    # Minimal synthetic dataset
    df = pd.DataFrame(
        {
            "return_on_equity_pct": np.random.rand(50) * 20,
            "debt_to_equity": np.random.rand(50),
            "revenue_cagr_5yr": np.random.rand(50) * 10,
            "fcf_cagr_5yr": np.random.rand(50) * 5,
            "operating_profit_margin_pct": np.random.rand(50) * 15,
        }
    )
    df.to_csv(input_path, index=False)

    # Act: generate elbow plot
    inertias = generate_elbow_plot(str(input_path), str(output_path))

    # Assert: file exists
    assert os.path.exists(output_path)

    # Assert: inertia decreases monotonically
    assert all(inertias[i] >= inertias[i + 1] for i in range(len(inertias) - 1))
