import streamlit as st
import pandas as pd

# Assume 'filtered' is your DataFrame after applying filters
# Example filtered dataset
filtered = pd.DataFrame({
    "company_id": [101, 102, 103],
    "name": ["Alpha Ltd", "Beta Corp", "Gamma Inc"],
    "sector": ["IT", "Finance", "Energy"],
    "composite_score": [78.4, 65.9, 82.1],
    "ROE": [18, 12, 22],
    "DE": [0.5, 1.8, 0.9],
    "FCF": [200, 150, 300]
})

# Show result count above table
count = len(filtered)
st.markdown(f"**{count} companies match your filters**")

# Show results table
st.dataframe(filtered)
