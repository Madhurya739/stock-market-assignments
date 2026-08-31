roe_col = "ROE (%)"        # replace with the exact name from your printout
de_col = "Debt/Equity"     # replace with the exact name from your printout

filtered = df[(df[roe_col] > 15) & (df[de_col] < 1)]

# Sort if composite score exists
if "Composite_Score" in filtered.columns:
    filtered = filtered.sort_values(by="Composite_Score", ascending=False)

# Take top 5
top5 = filtered.head(5)

# Add Pass column
top5 = top5.assign(Pass=top5.apply(lambda row: "✅" if row[roe_col] > 15 and row[de_col] < 1 else "❌", axis=1))

print(top5[["Company", roe_col, de_col, "Pass"]])
