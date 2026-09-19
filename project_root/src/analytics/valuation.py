import pandas as pd

def compute_sector_median_pe(df: pd.DataFrame, year: int) -> pd.DataFrame:
    """
    Compute sector median P/E for each broad_sector in the given year.
    Assumes columns: Company, broad_sector, year, MarketCap, NetProfit
    """
    # Filter for latest year
    df_year = df[df["year"] == year].copy()

    # Compute P/E for each company
    df_year["PE"] = df_year["MarketCap"] / df_year["NetProfit"]

    # Group by sector and compute median
    sector_medians = (
        df_year.groupby("broad_sector")["PE"]
        .median()
        .reset_index()
        .rename(columns={"PE": "Median_PE"})
    )

    return sector_medians


if __name__ == "__main__":
    # Example usage
    market_df = pd.read_excel("data/market_cap.xlsx")

    latest_year = market_df["year"].max()
    sector_pe = compute_sector_median_pe(market_df, latest_year)

    # Save to valuation output
    valuation_output = "data/valuation_output.csv"
    sector_pe.to_csv(valuation_output, index=False)

    print(f"Sector median P/E for {latest_year} saved to {valuation_output}")
