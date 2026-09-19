import streamlit as st
import plotly.express as px
import pandas as pd   # ✅ Import pandas

# Example DataFrame (replace with your actual 92 companies + 8 patterns)
df = pd.DataFrame({
    "Company": ["Alpha", "Beta", "Gamma"],
    "Pattern": ["Growth", "Dividends", "Buybacks"],
    "Value": [100, 200, 150]
})

# Treemap visualization
fig = px.treemap(
    df,
    path=["Pattern", "Company"],
    values="Value",
    title="Capital Allocation Map"
)
st.plotly_chart(fig, width="stretch")

# Dropdown to list companies in a selected pattern
selected_pattern = st.selectbox("Select Capital Allocation Pattern", df["Pattern"].unique())
st.write("Companies in this pattern:", df[df["Pattern"] == selected_pattern]["Company"].tolist())
