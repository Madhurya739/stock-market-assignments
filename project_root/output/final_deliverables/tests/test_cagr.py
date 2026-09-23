import pandas as pd
from src.analytics.cagr import compute_cagr, compute_metric_cagr


def test_normal_cagr():
    val, flag = compute_cagr(100, 200, 3)
    assert round(val, 2) == 25.99
    assert flag is None


def test_turnaround_flag():
    val, flag = compute_cagr(-100, 200, 3)
    assert val is None
    assert flag == "TURNAROUND"


def test_decline_to_loss_flag():
    val, flag = compute_cagr(100, -50, 3)
    assert val is None
    assert flag == "DECLINE_TO_LOSS"


def test_both_negative_flag():
    val, flag = compute_cagr(-100, -200, 3)
    assert val is None
    assert flag == "BOTH_NEGATIVE"


def test_zero_base_flag():
    val, flag = compute_cagr(0, 200, 3)
    assert val is None
    assert flag == "ZERO_BASE"


def test_insufficient_years_flag():
    val, flag = compute_cagr(100, 200, 0)
    assert val is None
    assert flag == "INSUFFICIENT"


def test_metric_cagr_normal():
    df = pd.DataFrame(
        {"year": [2018, 2019, 2020, 2021], "revenue": [100, 120, 150, 200]}
    )
    result = compute_metric_cagr(df, "revenue", [3])
    assert result["revenue_cagr_3yr"].iloc[0] is not None
    assert result["revenue_cagr_3yr_flag"].iloc[0] is None


def test_metric_cagr_insufficient():
    df = pd.DataFrame({"year": [2020, 2021], "eps": [5, 6]})
    result = compute_metric_cagr(df, "eps", [3])
    assert result["eps_cagr_3yr"].iloc[0] is None
    assert result["eps_cagr_3yr_flag"].iloc[0] == "INSUFFICIENT"


def test_metric_cagr_decline_to_loss():
    df = pd.DataFrame({"year": [2018, 2019, 2020, 2021], "pat": [100, 80, 50, -20]})
    result = compute_metric_cagr(df, "pat", [3])
    assert result["pat_cagr_3yr"].iloc[0] is None
    assert result["pat_cagr_3yr_flag"].iloc[0] == "DECLINE_TO_LOSS"


def test_metric_cagr_turnaround():
    df = pd.DataFrame({"year": [2018, 2019, 2020, 2021], "pat": [-100, -50, 0, 200]})
    result = compute_metric_cagr(df, "pat", [3])
    assert result["pat_cagr_3yr"].iloc[0] is None
    assert result["pat_cagr_3yr_flag"].iloc[0] == "TURNAROUND"
