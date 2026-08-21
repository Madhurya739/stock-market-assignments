df = pd.read_csv("companies.csv")
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
df = df[['company_id','company_name','year']]
df = df.rename(columns={'company_id':'ticker'})
df.to_sql("dim_company", conn, if_exists="append", index=False)
