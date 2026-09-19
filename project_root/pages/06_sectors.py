import streamlit as st
import plotly.express as px
import pandas as pd

# Sector dropdown
sector = st.selectbox("Select Sector", ["IT", "Pharma", "Banking"])

# Example DataFrame (replace with your actual sector data)
df = pd.DataFrame({
    "Company": ["A", "B", "C"],
    "Revenue": [1000, 2000, 1500],
    "ROE": [12, 18, 15],
    "MarketCap": [5000, 8000, 6000],
    "SubSector": ["Software", "Hardware", "Services"]
})

# Bubble chart
bubble = px.scatter(
    df,
    x="Revenue",
    y="ROE",
    size="MarketCap",
    color="SubSector",
    hover_name="Company",
    title=f"{sector} Sector Analysis"
)
st.plotly_chart(bubble, width="stretch")

# Median KPI bar chart
median_vals = df[["Revenue", "ROE", "MarketCap"]].median()
bar = px.bar(
    median_vals,
    x=median_vals.index,
    y=median_vals.values,
    title=f"{sector} Median KPIs"
)
st.plotly_chart(bar, width="stretch")
