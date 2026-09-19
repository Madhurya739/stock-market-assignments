import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import PatternFill

def valuation_summary(filepath: str, output_path: str = "output/valuation_summary.xlsx"):
    # Load and normalize headers
    df = pd.read_excel(filepath, header=0)
    df.columns = (
        df.columns.astype(str)
        .str.strip()
        .str.lower()
        .str.replace(r"\s+", "_", regex=True)
    )

    # --- Core ratios ---
    df["pe"] = df["marketcap"] / df["netprofit"]
    df["pb"] = df["marketcap"] / df["bookvalue"]
    df["ev_ebitda"] = df["marketcap"] / df["ebitda"]
    df["fcf_yield_pct"] = (df["fcf"] / df["marketcap"]) * 100

    # --- Sector median PE (latest year) ---
    latest_year = df["year"].max()
    sector_medians = (
        df[df["year"] == latest_year]
        .groupby("broad_sector")["pe"]
        .median()
        .reset_index()
        .rename(columns={"pe": "sector_median_pe"})
    )
    df = df.merge(sector_medians, on="broad_sector", how="left")

    # --- 5yr median PE per company ---
    median_pe_5yr = (
        df.groupby("company")["pe"]
        .median()
        .reset_index()
        .rename(columns={"pe": "5yr_median_pe"})
    )
    df = df.merge(median_pe_5yr, on="company", how="left")

    # --- Relative PE vs sector median ---
    df["pe_vs_sector_median_pct"] = (df["pe"] / df["sector_median_pe"]) * 100

    # --- Flags ---
    def flag(row):
        if row["pe"] > row["sector_median_pe"] * 1.5:
            return "Caution"
        elif row["pe"] < row["sector_median_pe"] * 0.7:
            return "Discount"
        else:
            return "Fair"
    df["flag"] = df.apply(flag, axis=1)

    # --- Final selection ---
    summary = df[[
        "company", "broad_sector", "pe", "pb", "ev_ebitda",
        "fcf_yield_pct", "5yr_median_pe", "pe_vs_sector_median_pct", "flag"
    ]].copy()

    summary = summary.rename(columns={
        "company": "company_name",
        "broad_sector": "sector"
    })
    summary.insert(0, "company_id", range(1, len(summary) + 1))

    # Export to Excel
    summary.to_excel(output_path, index=False)

    # --- Apply conditional formatting ---
    wb = load_workbook(output_path)
    ws = wb.active

    red_fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")   # Caution
    green_fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid") # Discount
    yellow_fill = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")# Fair

    for row in range(2, ws.max_row + 1):  # skip header
        cell = ws[f"J{row}"]  # flag column (10th col after company_id)
        if cell.value == "Caution":
            cell.fill = red_fill
        elif cell.value == "Discount":
            cell.fill = green_fill
        elif cell.value == "Fair":
            cell.fill = yellow_fill

    wb.save(output_path)
    print(f"Valuation summary with conditional formatting written to {output_path}")
    return summary

# Example usage
if __name__ == "__main__":
    summary_df = valuation_summary(r"C:\Users\YourName\Desktop\market_cap.xlsx")
    print(summary_df)
