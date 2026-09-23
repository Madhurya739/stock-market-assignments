import pytest
from src.analytics import ratios


# --- Return on Equity (ROE) ---
def test_return_on_equity_positive_equity():
    assert ratios.return_on_equity(100, 300, 200) == pytest.approx(20.0)


def test_return_on_equity_negative_equity():
    assert ratios.return_on_equity(100, -300, -200) is None


# --- Debt-to-Equity (D/E) ---
def test_debt_to_equity_debt_free():
    assert ratios.debt_to_equity(0, 500, 200) == 0


def test_debt_to_equity_high_leverage_flag():
    result = ratios.debt_to_equity(6000, 1000, 200)
    assert result > 5
    assert ratios.high_leverage_flag(6000, 1000, 200, sector="Manufacturing") is True


def test_debt_to_equity_financials_no_flag():
    assert ratios.high_leverage_flag(6000, 1000, 200, sector="Financials") is False


# --- Interest Coverage Ratio (ICR) ---
def test_interest_coverage_ratio_normal():
    assert ratios.interest_coverage_ratio(500, 100) == pytest.approx(5.0)


def test_interest_coverage_ratio_interest_zero():
    assert ratios.interest_coverage_ratio(500, 0) is None


def test_interest_coverage_ratio_debt_free_label():
    assert ratios.icr_label(500, 0) == "Debt Free"


def test_interest_coverage_ratio_warning_flag():
    assert ratios.icr_warning_flag(100, 200) is True


# --- CAGR (Compound Annual Growth Rate) ---
def test_cagr_normal_calculation():
    assert ratios.cagr(100, 200, 3) == pytest.approx((200 / 100) ** (1 / 3) - 1)


def test_cagr_turnaround_flag():
    assert ratios.cagr_turnaround_flag(-100, 200, 3) is True


def test_cagr_decline_to_loss():
    assert ratios.cagr_decline_to_loss(200, -50, 2) is True


# --- Operating Profit Margin (OPM) ---
def test_operating_profit_margin_normal():
    assert ratios.operating_profit_margin(40, 200) == 20.0


def test_operating_profit_margin_mismatch_logs(caplog):
    with caplog.at_level("WARNING"):
        ratios.operating_profit_margin(40, 200, opm_percentage=25)
    assert "divergence" in caplog.text.lower()


# --- CFO Quality Score ---
def test_cfo_quality_score_positive_cfo():
    assert ratios.cfo_quality_score(500, 400) == pytest.approx(1.25)


def test_cfo_quality_score_negative_cfo():
    assert ratios.cfo_quality_score(-100, 400) < 0


def test_cfo_quality_score_zero_cfo():
    assert ratios.cfo_quality_score(0, 400) == 0


def test_cfo_quality_score_high_quality():
    assert ratios.cfo_quality_score(1000, 400) > 2


def test_cfo_quality_score_low_quality():
    assert ratios.cfo_quality_score(100, 400) < 0.5
