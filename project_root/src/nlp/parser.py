import re
import pandas as pd
import os

# Regex pattern: e.g. "10 Years: 21%"
PATTERN = re.compile(r"(\d+)\s*Years?:?\s*([\d.]+)%")

TARGET_FIELDS = [
    "compounded_sales_growth",
    "compounded_profit_growth",
    "stock_price_cagr",
    "roe"
]

def parse_text_entry(company_id: str, metric_type: str, text: str):
    """
    Parse a single text entry using regex.
    Returns dict with parsed values or None if failure.
    """
    match = PATTERN.search(str(text))
    if match:
        return {
            "company_id": company_id,
            "metric_type": metric_type,
            "period_years": int(match.group(1)),
            "value_pct": float(match.group(2))
        }
    return None


def main(input_file="analysis.xlsx",
         parsed_file="output/analysis_parsed.csv",
         failures_file="output/parse_failures.csv"):
    """
    Parse analysis.xlsx text fields and export results.
    """
    # Ensure output directory exists
    os.makedirs(os.path.dirname(parsed_file), exist_ok=True)

    df = pd.read_excel(input_file)
    parsed_rows, failed_rows = [], []

    for _, row in df.iterrows():
        company_id = row.get("company_id")
        for metric in TARGET_FIELDS:
            text = row.get(metric, "")
            result = parse_text_entry(company_id, metric, text)
            if result:
                parsed_rows.append(result)
            else:
                failed_rows.append({
                    "company_id": company_id,
                    "metric_type": metric,
                    "raw_text": text
                })

    # Save parsed results
    pd.DataFrame(parsed_rows).to_csv(parsed_file, index=False)

    # Save failures
    pd.DataFrame(failed_rows).to_csv(failures_file, index=False)

    print(f"Parsing complete. Parsed: {len(parsed_rows)}, Failures: {len(failed_rows)}")


if __name__ == "__main__":
    main()
