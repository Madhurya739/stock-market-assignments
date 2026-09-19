import streamlit as st
import pandas as pd

# --- Example dataset ---
companies = [
    {"ticker": "TCS", "name": "Tata Consultancy Services", "sector": "IT", "sub_sector": "Software Services", "about": "Global IT services leader."},
    {"ticker": "INFY", "name": "Infosys", "sector": "IT", "sub_sector": "Software Services", "about": "Consulting and outsourcing services."},
    {"ticker": "HDFCBANK", "name": "HDFC Bank", "sector": "Financials", "sub_sector": "Banking", "about": "Leading private sector bank."},
]
companies_df = pd.DataFrame(companies)

st.title("🏢 Company Profile")

# --- Search box ---
search_query = st.text_input("Search company by name or ticker")

if search_query:
    matches = companies_df[
        companies_df["ticker"].str.contains(search_query, case=False) |
        companies_df["name"].str.contains(search_query, case=False)
    ]
    if not matches.empty:
        selected = st.selectbox("Select company", matches["ticker"] + " — " + matches["name"])
        chosen_ticker = selected.split(" — ")[0]
        company = companies_df[companies_df["ticker"] == chosen_ticker].iloc[0]

        # --- Company card ---
        st.subheader(company["name"])
        st.markdown(f"**Sector:** {company['sector']}")
        st.markdown(f"**Sub‑Sector:** {company['sub_sector']}")
        st.markdown(f"**NSE Ticker:** {company['ticker']}")
        st.markdown(f"**About:** {company['about']}")

    else:
        # --- Friendly message if ticker not found ---
        st.error("❌ Ticker not found — please try another")
