import streamlit as st
from src.dashboard.data_loader import load_screener_data

data = load_screener_data()
st.dataframe(data)
