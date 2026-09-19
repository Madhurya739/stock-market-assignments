# src/analytics/cashflow_kpis.py

"""
Cash Flow Intelligence Module
Implements key cash flow KPIs and capital allocation pattern classification.
"""

import pandas as pd
from typing import Dict, Optional


class CashFlowKPIs:
    @staticmethod
    def free_cash_flow(cfo: float, cfi: float) -> float:
        """
        Free Cash Flow = CFO + CFI
        Negative values are allowed.
        """
        return cfo + cfi

    @staticmethod
    def cfo_quality_score(cfo_series: pd.Series, pat_series: pd.Series) -> Optional[float]:
        """
        CFO Quality Score = (CFO / PAT) averaged over 5 years.
        >1.0 = High Quality, 0.5–1.0 = Moderate, <0.5 = Accrual Risk.
        Returns None if PAT = 0 in any year.
        """
        ratios = []
        for cfo, pat in zip(cfo_series, pat_series):
            if pat == 0:
                return None
            ratios.append(cfo / pat)
        return sum(ratios) / len(ratios)

    @staticmethod
    def capex_intensity(cfi: float, sales: float) -> Optional[float]:
        """
        CapEx Intensity = abs(CFI) / sales * 100
        <3% = Asset Light, 3–8% = Moderate, >8% = Capital Intensive.
        """
        if sales == 0:
            return None
        return abs(cfi) / sales * 100

    @staticmethod
    def fcf_conversion_rate(fcf: float, op_profit: float) -> Optional[float]:
        """
        FCF Conversion Rate = FCF / Operating Profit * 100
        Returns None if Operating Profit = 0.
        """
        if op_profit == 0:
            return None
        return fcf / op_profit * 100

    @staticmethod
    def classify_capital_allocation(cfo: float, cfi: float, cff: float, cfo_pat_ratio: Optional[float] = None) -> str:
        """
        Classify capital allocation pattern based on signs of CFO, CFI, CFF.
        Pattern labels:
        (+,-,-) = Reinvestor
        (+,-,-) with high CFO/PAT (>1.5) = Shareholder Returns
        (+,+,-) = Liquidating Assets
        (-,+,+) = Distress Signal
        (-,-,+) = Growth Funded by Debt
        (+,+,+) = Cash Accumulator
        (-,-,-) = Pre-Revenue
        (+,-,+) = Mixed
        """
        s_cfo = "+" if cfo > 0 else "-"
        s_cfi = "+" if cfi > 0 else "-"
        s_cff = "+" if cff > 0 else "-"

        pattern = (s_cfo, s_cfi, s_cff)

        if pattern == ("+", "-", "-"):
            if cfo_pat_ratio and cfo_pat_ratio > 1.5:
                return "Shareholder Returns"
            return "Reinvestor"
        elif pattern == ("+", "+", "-"):
            return "Liquidating Assets"
        elif pattern == ("-", "+", "+"):
            return "Distress Signal"
        elif pattern == ("-", "-", "+"):
            return "Growth Funded by Debt"
        elif pattern == ("+", "+", "+"):
            return "Cash Accumulator"
        elif pattern == ("-", "-", "-"):
            return "Pre-Revenue"
        elif pattern == ("+", "-", "+"):
            return "Mixed"
        else:
            return "Unclassified"


def generate_capital_allocation_csv(df: pd.DataFrame, output_path: str = "output/capital_allocation.csv"):
    """
    Generate capital allocation classification CSV.
    Expects DataFrame with columns: company_id, year, cfo, cfi, cff, pat, sales, op_profit.
    """
    records = []
    for _, row in df.iterrows():
        fcf = CashFlowKPIs.free_cash_flow(row["cfo"], row["cfi"])
        cfo_quality = CashFlowKPIs.cfo_quality_score(pd.Series([row["cfo"]]), pd.Series([row["pat"]]))
        capex_int = CashFlowKPIs.capex_intensity(row["cfi"], row["sales"])
        fcf_conv = CashFlowKPIs.fcf_conversion_rate(fcf, row["op_profit"])
        pattern = CashFlowKPIs.classify_capital_allocation(row["cfo"], row["cfi"], row["cff"], cfo_pat_ratio=cfo_quality)

        records.append({
            "company_id": row["company_id"],
            "year": row["year"],
            "cfo_sign": "+" if row["cfo"] > 0 else "-",
            "cfi_sign": "+" if row["cfi"] > 0 else "-",
            "cff_sign": "+" if row["cff"] > 0 else "-",
            "pattern_label": pattern,
            "fcf": fcf,
            "cfo_quality_score": cfo_quality,
            "capex_intensity_pct": capex_int,
            "fcf_conversion_pct": fcf_conv,
        })

    out_df = pd.DataFrame(records)
    out_df.to_csv(output_path, index=False)
    return out_df


# Example usage
if __name__ == "__main__":
    sample_data = pd.DataFrame([
        {"company_id": "C001", "year": 2025, "cfo": 1200, "cfi": -400, "cff": -200, "pat": 800, "sales": 5000, "op_profit": 1000},
        {"company_id": "C002", "year": 2025, "cfo": -300, "cfi": 200, "cff": 500, "pat": 100, "sales": 2000, "op_profit": 400},
    ])
    df_out = generate_capital_allocation_csv(sample_data)
    print(df_out)
