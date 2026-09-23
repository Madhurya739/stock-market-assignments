import pandas as pd
import numpy as np


def free_cash_flow(df: pd.DataFrame):
    """
    Free Cash Flow = operating_activity + investing_activity
    Negative values allowed.
    """
    df["fcf"] = df["operating_activity"] + df["investing_activity"]
    return df


def cfo_quality_score(df: pd.DataFrame):
    """
    CFO Quality Score = (CFO / PAT) averaged over 5 years.
    Classification:
      >1.0 = High Quality
      0.5–1.0 = Moderate
      <0.5 = Accrual Risk
    Return None if PAT = 0.
    """
    ratios = []
    for _, row in df.tail(5).iterrows():
        if row["pat"] == 0:
            ratios.append(np.nan)
        else:
            ratios.append(row["operating_activity"] / row["pat"])
    avg_ratio = np.nanmean(ratios)

    if np.isnan(avg_ratio):
        return None, None
    if avg_ratio > 1.0:
        return avg_ratio, "High Quality"
    elif avg_ratio >= 0.5:
        return avg_ratio, "Moderate"
    else:
        return avg_ratio, "Accrual Risk"


def capex_intensity(df: pd.DataFrame):
    """
    CapEx Intensity = abs(investing_activity) / sales * 100
    Classification:
      <3% = Asset Light
      3–8% = Moderate
      >8% = Capital Intensive
    """
    df["capex_intensity"] = abs(df["investing_activity"]) / df["sales"] * 100
    df["capex_class"] = pd.cut(
        df["capex_intensity"],
        bins=[-np.inf, 3, 8, np.inf],
        labels=["Asset Light", "Moderate", "Capital Intensive"],
    )
    return df


def fcf_conversion_rate(df: pd.DataFrame):
    """
    FCF Conversion Rate = FCF / operating_profit * 100
    Return None if operating_profit = 0.
    """

    def calc(row):
        if row["operating_profit"] == 0:
            return None
        return (row["fcf"] / row["operating_profit"]) * 100

    df["fcf_conversion_rate"] = df.apply(calc, axis=1)
    return df


def classify_capital_allocation(df: pd.DataFrame):
    """
    Capital Allocation 8-pattern classifier based on sign of (CFO, CFI, CFF).
    Pattern labels:
      (+,-,-) = Reinvestor
      (+,-,-) with high CFO/PAT = Shareholder Returns
      (+,+,-) = Liquidating Assets
      (-,+,+) = Distress Signal
      (-,-,+) = Growth Funded by Debt
      (+,+,+) = Cash Accumulator
      (-,-,-) = Pre-Revenue
      (+,-,+) = Mixed
    """
    patterns = []
    for _, row in df.iterrows():
        cfo_sign = "+" if row["operating_activity"] > 0 else "-"
        cfi_sign = "+" if row["investing_activity"] > 0 else "-"
        cff_sign = "+" if row["financing_activity"] > 0 else "-"

        label = None
        if (cfo_sign, cfi_sign, cff_sign) == ("+", "-", "-"):
            # Check CFO/PAT quality
            if row["pat"] != 0 and (row["operating_activity"] / row["pat"]) > 1.2:
                label = "Shareholder Returns"
            else:
                label = "Reinvestor"
        elif (cfo_sign, cfi_sign, cff_sign) == ("+", "+", "-"):
            label = "Liquidating Assets"
        elif (cfo_sign, cfi_sign, cff_sign) == ("-", "+", "+"):
            label = "Distress Signal"
        elif (cfo_sign, cfi_sign, cff_sign) == ("-", "-", "+"):
            label = "Growth Funded by Debt"
        elif (cfo_sign, cfi_sign, cff_sign) == ("+", "+", "+"):
            label = "Cash Accumulator"
        elif (cfo_sign, cfi_sign, cff_sign) == ("-", "-", "-"):
            label = "Pre-Revenue"
        elif (cfo_sign, cfi_sign, cff_sign) == ("+", "-", "+"):
            label = "Mixed"

        patterns.append(
            {
                "company_id": row["company_id"],
                "year": row["year"],
                "cfo_sign": cfo_sign,
                "cfi_sign": cfi_sign,
                "cff_sign": cff_sign,
                "pattern_label": label,
            }
        )

    return pd.DataFrame(patterns)


def export_capital_allocation(df: pd.DataFrame, path="output/capital_allocation.csv"):
    """
    Export capital allocation classification to CSV.
    """
    classified = classify_capital_allocation(df)
    classified.to_csv(path, index=False)
    return classified
