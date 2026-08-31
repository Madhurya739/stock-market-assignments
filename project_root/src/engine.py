import yaml
import pandas as pd
import numpy as np

def load_config(config_path="screener_config.yaml"):
    """Load screener thresholds from YAML config file."""
    with open(config_path, "r") as f:
        return yaml.safe_load(f)

def apply_filters(financial_ratios: pd.DataFrame, config_path="screener_config.yaml"):
    """
    Apply screener filters to financial_ratios DataFrame.
    Supports 15 metrics with special handling for D/E and ICR.
    Returns sorted DataFrame with composite_quality_score.
    """
    config = load_config(config_path)
    df = financial_ratios.copy()

    # --- Define filters ---
    filters = {
        "roe": ("min", "ROE min"),
        "de_ratio": ("max", "D/E max"),
        "fcf": ("min", "FCF min"),
        "revenue_cagr_5yr": ("min", "Revenue CAGR 5yr min"),
        "pat_cagr_5yr": ("min", "PAT CAGR 5yr min"),
        "opm": ("min", "OPM min"),
        "pe": ("max", "P/E max"),
        "pb": ("max", "P/B max"),
        "dividend_yield": ("min", "Dividend Yield min"),
        "icr": ("min", "ICR min"),
        "market_cap": ("min", "Market Cap min"),
        "net_profit": ("min", "Net Profit min"),
        "eps_cagr": ("min", "EPS CAGR min"),
        "asset_turnover": ("min", "Asset Turnover min"),
        "sales": ("min", "Sales min"),
    }

    mask = pd.Series(True, index=df.index)

    # --- Apply filters ---
    for col, (mode, key) in filters.items():
        if key not in config:
            continue
        threshold = config[key]

        if col == "de_ratio":
            # Skip Financials sector for D/E filter
            sector_mask = df["broad_sector"] != "Financials"
            mask &= (df[col] <= threshold) | ~sector_mask

        elif col == "icr":
            # Treat Debt Free label as infinity
            icr_values = df[col].replace("Debt Free", np.inf)
            mask &= icr_values.astype(float) >= threshold

        else:
            if mode == "min":
                mask &= df[col] >= threshold
            elif mode == "max":
                mask &= df[col] <= threshold

    df = df[mask].copy()

    # --- Composite Quality Score ---
    score_components = []
    for col, (mode, _) in filters.items():
        if col in df.columns and df[col].dtype != object:
            if mode == "min":
                norm = (df[col] - df[col].min()) / (df[col].max() - df[col].min() + 1e-9)
            else:  # max filter → inverse normalization
                norm = (df[col].max() - df[col]) / (df[col].max() - df[col].min() + 1e-9)
            score_components.append(norm)

    if score_components:
        df["composite_quality_score"] = pd.concat(score_components, axis=1).mean(axis=1)
    else:
        df["composite_quality_score"] = 0

    # --- Sort by composite score ---
    df = df.sort_values(by="composite_quality_score", ascending=False)

    return df
