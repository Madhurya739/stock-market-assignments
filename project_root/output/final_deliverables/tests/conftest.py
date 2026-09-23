import pandas as pd
import numpy as np
import pytest


@pytest.fixture
def sample_data(tmp_path):
    sectors = ["Technology", "Finance", "Healthcare", "Energy", "Consumer"]

    data = {
        "company": [f"Company_{i+1}" for i in range(92)],
        "sector": [sectors[i % len(sectors)] for i in range(92)],
        "return_on_equity_pct": [
            10 + (i % 15) if i % 10 != 0 else np.nan for i in range(92)
        ],
        "debt_to_equity": [
            0.5 + (i % 5) * 0.1 if i % 12 != 0 else np.nan for i in range(92)
        ],
        "revenue_cagr_5yr": [5 + (i % 10) if i % 8 != 0 else np.nan for i in range(92)],
        "fcf_cagr_5yr": [3 + (i % 8) if i % 7 != 0 else np.nan for i in range(92)],
        "operating_profit_margin_pct": [
            12 + (i % 20) if i % 6 != 0 else np.nan for i in range(92)
        ],
    }

    df = pd.DataFrame(data)
    input_path = tmp_path / "companies.csv"
    output_path = tmp_path / "companies_clustered.csv"
    df.to_csv(input_path, index=False)

    return input_path, output_path
