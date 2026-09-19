import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Example: company search + metric selector
company = st.text_input("Search Company")
metrics = st.multiselect("Select up to 3 metrics", ["Revenue", "PAT", "ROE", "FCF"], max_selections=3)

# Example data (replace with actual)
years = list(range(2016, 2026))
values = [100, 110, 120, 115, 130, 140, 150, 160, 170, 180]

fig = go.Figure()
for metric in metrics:
    fig.add_trace(go.Scatter(
        x=years,
        y=values,
        mode="lines+markers+text",
        text=[f"{(values[i]/values[i-1]-1)*100:.1f}%" if i>0 else "" for i in range(len(values))],
        textposition="top center",
        name=metric
    ))

fig.update_layout(title=f"{company} Trend Analysis", xaxis_title="Year", yaxis_title="Value")
st.plotly_chart(fig, width="stretch")
