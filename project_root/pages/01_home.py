import streamlit as st
import plotly.express as px
import pandas as pd

st.title("🏠 Home")

# --- Example dataset with 11 sectors ---
data = {
    "ticker": ["TCS", "INFY", "HDFCBANK", "RELIANCE", "SUNPHARMA", "ITC", "ONGC", "MARUTI", "L&T", "HINDUNILVR", "SBIN"],
    "sector": ["IT", "IT", "Financials", "Energy", "Pharma", "Consumer Goods", "Energy", "Automobile", "Infrastructure", "Consumer Goods", "Financials"]
}
companies_df = pd.DataFrame(data)

# --- Sector breakdown donut chart ---
st.subheader("Sector Breakdown")

sector_counts = companies_df.groupby("sector").size().reset_index(name="count")

fig = px.pie(
    sector_counts,
    names="sector",
    values="count",
    hole=0.4,  # donut style
    title="Company Count by Sector"
)

# Updated parameter (instead of use_container_width)
st.plotly_chart(fig, width="stretch")
