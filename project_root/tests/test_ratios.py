import pytest
from src.analytics import ratios

def test_net_profit_margin_normal():
    assert ratios.net_profit_margin(50, 200) == 25.0

def test_net_profit_margin_zero_sales():
    assert ratios.net_profit_margin(50, 0) is None

def test_operating_profit_margin_normal():
    assert ratios.operating_profit_margin(40, 200) == 20.0

def test_operating_profit_margin_mismatch_logs(caplog):
    with caplog.at_level("WARNING"):
        ratios.operating_profit_margin(40, 200, opm_percentage=25)
    assert "OPM mismatch" in caplog.text

def test_return_on_equity_normal():
    assert ratios.return_on_equity(100, 300, 200) == pytest.approx(20.0)

def test_return_on_equity_negative_equity():
    assert ratios.return_on_equity(100, -300, -200) is None

def test_return_on_capital_employed_normal():
    assert ratios.return_on_capital_employed(150, 300, 200, 500) == pytest.approx(15.0)

def test_return_on_assets_zero_assets():
    assert ratios.return_on_assets(100, 0) is None
