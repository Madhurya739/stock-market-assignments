# Performance Notes

## Dashboard & API Bottlenecks
- **Company Profile load time**: Some tickers exceeded 3s due to unindexed queries on large tables.
- **Screener API under concurrency**: 10 concurrent calls completed, but average latency increased to ~2.8s. Bottleneck traced to full table scans in `fact_performance`.

## Root Causes
- Missing indexes on frequently filtered columns (`company_id`, `year`).
- Queries performing joins without supporting indexes, leading to sequential scans.
- Streamlit dashboard waiting on API responses without caching.

## Optimisations Applied
- Added composite index on `(company_id, year)` in `fact_performance` and `fact_aum`.
- Added individual indexes on `company_id` in `fact_transactions`.
- Enabled query plan analysis (`EXPLAIN QUERY PLAN`) to confirm index usage.
- Implemented caching layer in Streamlit for repeated API calls (per ticker).

## Next Steps
- Monitor latency under 50+ concurrent calls.
- Consider partitioning historical data by year for faster lookups.
- Add automated regression tests to ensure performance thresholds (<3s per profile, <10s for 10 concurrent screener calls).
