import logging

logger = logging.getLogger(__name__)

# ---------------- Profitability Ratios ----------------

def net_profit_margin(net_profit: float, sales: float) -> float | None:
    if sales == 0:
        return None
    return (net_profit / sales) * 100

def operating_profit_margin(operating_profit: float, sales: float, opm_percentage: float | None = None) -> float | None:
    if sales == 0:
        return None
    opm = (operating_profit / sales) * 100
    if opm_percentage is not None and abs(opm - opm_percentage) > 1:
        logger.warning("OPM mismatch: computed=%.2f, provided=%.2f", opm, opm_percentage)
    return opm

def return_on_equity(net_profit: float, equity_capital: float, reserves: float) -> float | None:
    base = equity_capital + reserves
    if base <= 0:
        return None
    return (net_profit / base) * 100

def return_on_capital_employed(ebit: float, equity: float, reserves: float, borrowings: float, broad_sector: str | None = None) -> float | None:
    base = equity + reserves + borrowings
    if base == 0:
        return None
    roce = (ebit / base) * 100
    if broad_sector == "Financials":
        logger.info("ROCE computed for Financials sector — compare with sector benchmark.")
    return roce

def return_on_assets(net_profit: float, total_assets: float) -> float | None:
    if total_assets == 0:
        return None
    return (net_profit / total_assets) * 100

# ---------------- Leverage & Efficiency Ratios ----------------

def debt_to_equity(borrowings: float, equity_capital: float, reserves: float, broad_sector: str | None = None) -> tuple[float, bool]:
    base = equity_capital + reserves
    if base <= 0:
        return None, False
    if borrowings == 0:
        return 0.0, False
    de_ratio = borrowings / base
    high_leverage_flag = de_ratio > 5 and broad_sector != "Financials"
    return de_ratio, high_leverage_flag

def interest_coverage_ratio(operating_profit: float, other_income: float, interest: float) -> tuple[float | None, str | None, bool]:
    if interest == 0:
        return None, "Debt Free", False
    icr = (operating_profit + other_income) / interest
    warning_flag = icr < 1.5
    return icr, None, warning_flag

def net_debt(borrowings: float, investments: float) -> float:
    return borrowings - investments

def asset_turnover(sales: float, total_assets: float) -> float | None:
    if total_assets == 0:
        return None
    return sales / total_assets
