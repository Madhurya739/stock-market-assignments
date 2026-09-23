# src/analytics/ratios.py
import logging

# other imports...

# rest of your code...

import warnings

warnings.filterwarnings("ignore")


def return_on_equity(net_income, assets, equity):
    """TODO: Add docstring."""
    if equity <= 0:
        return None
    return (net_income / (assets + equity)) * 100


def debt_to_equity(debt, equity, assets):
    """TODO: Add docstring."""
    if equity == 0:
        return None
    return debt / equity


def high_leverage_flag(debt, equity, assets, sector):
    """TODO: Add docstring."""
    ratio = debt_to_equity(debt, equity, assets)
    if sector.lower() != "financials" and ratio > 5:
        return True
    return False


def interest_coverage_ratio(ebit, interest):
    """TODO: Add docstring."""
    if interest == 0:
        return None
    return ebit / interest


def icr_label(ebit, interest):
    """TODO: Add docstring."""
    if interest == 0:
        return "Debt Free"
    return "Normal"


def icr_warning_flag(ebit, interest):
    """TODO: Add docstring."""
    if interest > ebit:
        return True
    return False


def cagr(start_value, end_value, years):
    """TODO: Add docstring."""
    if start_value <= 0 or years <= 0:
        return None
    return (end_value / start_value) ** (1 / years) - 1


def cagr_turnaround_flag(start_value, end_value, years):
    """TODO: Add docstring."""
    return start_value < 0 and end_value > 0


def cagr_decline_to_loss(start_value, end_value, years):
    """TODO: Add docstring."""
    return start_value > 0 and end_value < 0


def operating_profit_margin(op, revenue, opm_percentage=None):
    """TODO: Add docstring."""
    if revenue == 0:
        return None
    margin = (op / revenue) * 100
    if opm_percentage is not None and abs(margin - opm_percentage) >= 5:
        logging.warning("OPM divergence detected")
    return margin


def cfo_quality_score(cfo, net_income):
    """TODO: Add docstring."""
    if net_income == 0:
        return None
    return cfo / net_income
