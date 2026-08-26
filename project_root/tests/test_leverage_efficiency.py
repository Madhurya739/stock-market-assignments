import pytest
from src.analytics import ratios

def test_debt_to_equity_debt_free():
    de, flag = ratios.debt_to_equity(0, 200, 100)
    assert de == 0.0
    assert flag is False

def test_debt_to_equity_high_leverage_flag():
    de, flag = ratios.debt_to_equity(2000, 100, 200, broad_sector="Manufacturing")
    assert de > 5
    assert flag is True

def test_debt_to_equity_financials_no_flag():
    de, flag = ratios.debt_to_equity(2000, 100, 200, broad_sector="Financials")
    assert de > 5
    assert flag is False

def test_interest_coverage_ratio_normal():
    icr, label, flag = ratios.interest_coverage_ratio(300, 50, 100)
    assert icr == pytest.approx(3.5)
    assert label is None
    assert flag is False

def test_interest_coverage_ratio_interest_zero():
    icr, label, flag = ratios.interest_coverage_ratio(300, 50, 0)
    assert icr is None
    assert label == "Debt Free"
    assert flag is False

def test_interest_coverage_ratio_warning_flag():
    icr, label, flag = ratios.interest_coverage_ratio(100, 0, 100)
    assert icr == pytest.approx(1.0)
    assert flag is True

def test_net_debt():
    assert ratios.net_debt(500, 200) == 300

def test_asset_turnover_zero_assets():
    assert ratios.asset_turnover(1000, 0) is None
