# src/screener/engine.py
import pandas as pd
from src.screener.presets import presets, apply_preset


def run_all_presets(financial_ratios: pd.DataFrame):
    """Run all presets and return a dictionary of results."""
    results = {}
    for preset in presets:
        results[preset] = apply_preset(financial_ratios, preset)
    return results


def summarize_presets(financial_ratios: pd.DataFrame, sample_size: int = 5):
    """Summarize preset results with counts and sample companies."""
    results = run_all_presets(financial_ratios)

    summary_data = []
    for preset, df in results.items():
        summary_data.append(
            {
                "Preset": preset,
                "Companies Returned": len(df),
                "Sample Companies": ", ".join(
                    (
                        df["company_name"]
                        if "company_name" in df.columns
                        else df["company_id"].astype(str)
                    ).head(sample_size)
                ),
            }
        )

    return pd.DataFrame(summary_data)
