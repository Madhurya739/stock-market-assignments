import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page setup ---
st.set_page_config(page_title="Nifty 100 Analytics", layout="wide")

st.title("🏠 Home")

# --- Sample data (replace with db.get_companies()) ---
data = {
    "ticker": ["TCS", "INFY", "HDFCBANK", "RELIANCE", "SUNPHARMA", "ITC", "ONGC", "MARUTI", "L&T", "HINDUNILVR", "SBIN"],
    "name": ["Tata Consultancy Services", "Infosys", "HDFC Bank", "Reliance Industries", "Sun Pharma", "ITC", "ONGC", "Maruti Suzuki", "Larsen & Toubro", "Hindustan Unilever", "State Bank of India"],
    "sector": ["IT", "IT", "Financials", "Energy", "Pharma", "Consumer Goods", "Energy", "Automobile", "Infrastructure", "Consumer Goods", "Financials"],
    "ROE": [18.5, 17.2, 15.1, 12.3, 14.8, 19.0, 11.5, 16.7, 13.2, 20.1, 12.9],
    "PE": [22.3, 21.5, 18.7, 19.2, 20.4, 17.8, 15.6, 23.1, 16.9, 25.0, 14.7],
    "DE": [0.1, 0.2, 0.5, 0.7, 0.3, 0.0, 0.6, 0.4, 0.8, 0.0, 0.9],
    "Revenue_CAGR_5yr": [12.0, 11.5, 10.2, 9.8, 8.7, 7.5, 6.9, 13.1, 9.2, 8.8, 7.9]
}
companies_df = pd.DataFrame(data)

selected_year = st.sidebar.selectbox("Select Year", list(range(2019, 2025)))

# --- Filter data by year ---
df_year = companies_df[companies_df["year"] == selected_year]

# --- KPI calculations ---
avg_roe = companies_df["ROE"].mean()
median_pe = companies_df["PE"].median()
median_de = companies_df["DE"].median()
total_companies = len(companies_df)
median_rev_cagr = companies_df["Revenue_CAGR_5yr"].median()
debt_free_count = (companies_df["DE"] == 0).sum()

# --- KPI tiles ---
col1, col2, col3, col4, col5, col6 = st.columns(6)
col1.metric("Average ROE", f"{avg_roe:.2f}%")
col2.metric("Median P/E", f"{median_pe:.2f}")
col3.metric("Median D/E", f"{median_de:.2f}")
col4.metric("Total Companies", total_companies)
col5.metric("Median Revenue CAGR (5yr)", f"{median_rev_cagr:.2f}%")
col6.metric("Debt-Free Companies", debt_free_count)

st.write("---")

# --- Sector breakdown donut chart ---
st.subheader("Sector Breakdown")
sector_counts = companies_df.groupby("sector").size().reset_index(name="count")

fig = px.pie(
    sector_counts,
    names="sector",
    values="count",
    hole=0.4,
    title="Company Count by Sector"
)

st.plotly_chart(fig, width="stretch")
