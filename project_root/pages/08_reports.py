import requests

company = st.text_input("Search Company")
years = [2021, 2022, 2023]

for year in years:
    url = f"https://www.bseindia.com/reports/{company}_{year}.pdf"
    response = requests.head(url)
    if response.status_code == 200:
        st.markdown(f"[{year} Annual Report]({url})")
    else:
        st.markdown(f"**{year} Report unavailable**", unsafe_allow_html=True)
