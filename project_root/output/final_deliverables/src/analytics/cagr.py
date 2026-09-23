import pandas as pd


def compute_cagr(start: float, end: float, years: int):
    """
    Compute CAGR with edge case handling.
    Formula: ((end/start) ** (1/n) - 1) * 100
    Returns (cagr_value, flag)
    """
    # Edge case: insufficient years
    if years <= 0:
        return None, "INSUFFICIENT"

    # Edge case: zero base
    if start == 0:
        return None, "ZERO_BASE"

    # Edge case: both negative
    if start < 0 and end < 0:
        return None, "BOTH_NEGATIVE"

    # Edge case: decline to loss
    if start > 0 and end < 0:
        return None, "DECLINE_TO_LOSS"

    # Edge case: turnaround
    if start < 0 and end > 0:
        return None, "TURNAROUND"

    # Normal case
    try:
        cagr = ((end / start) ** (1 / years) - 1) * 100
        return cagr, None
    except Exception:
        return None, "ERROR"


def compute_metric_cagr(df: pd.DataFrame, metric: str, years_list=[3, 5, 10]):
    """
    Compute CAGR for a given metric across multiple horizons.
    df must have columns: ['year', metric]
    Returns DataFrame with CAGR values and flags.
    """
    df = df.sort_values("year").reset_index(drop=True)
    results = {}

    for n in years_list:
        if len(df) < n + 1:
            results[f"{metric}_cagr_{n}yr"] = None
            results[f"{metric}_cagr_{n}yr_flag"] = "INSUFFICIENT"
            continue

        start = df.iloc[-(n + 1)][metric]
        end = df.iloc[-1][metric]

        cagr, flag = compute_cagr(start, end, n)
        results[f"{metric}_cagr_{n}yr"] = cagr
        results[f"{metric}_cagr_{n}yr_flag"] = flag

    return pd.DataFrame([results])
