import streamlit as st
import pandas as pd

# Example peer group DataFrame (replace with your actual data)
data = pd.DataFrame({
    "CompanyID": [101, 102, 103],
    "CompanyName": ["Alpha Ltd", "Beta Corp", "Gamma Inc"],
    "ROE": [18, 12, 15],
    "ROCE": [22, 17, 19],
    "NetProfitMargin": [15, 10, 12],
    "DE": [0.8, 1.2, 1.0],
    "FCF": [75, 60, 70],
    "RevenueCAGR5yr": [10, 8, 9],
    "PATCAGR5yr": [12, 9, 11],
    "CompositeScore": [82, 74, 78]
})

# Assume benchmark company is Alpha Ltd
benchmark_id = 101

# Highlight function
def highlight_benchmark(row):
    return ['background-color: yellow' if row.CompanyID == benchmark_id else '' for _ in row]

# Apply styling
styled_table = data.style.apply(highlight_benchmark, axis=1)

st.write("### Peer Group KPI Comparison")
st.dataframe(styled_table, use_container_width=True)
