CREATE TABLE IF NOT EXISTS dim_fund(
    fund_id INTEGER PRIMARY KEY,
    amfi_code TEXT UNIQUE NOT NULL,
    fund_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS fact_nav(
    nav_id INTEGER PRIMARY KEY,
    fund_id INTEGER NOT NULL,
    date_id INTEGER NOT NULL,
    nav REAL NOT NULL,
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);
CREATE TABLE IF NOT EXISTS dim_fund1(
    fund_id INTEGER PRIMARY KEY,
    amfi_code TEXT UNIQUE NOT NULL,
    fund_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS fact_nav1 (
    nav_id INTEGER PRIMARY KEY,
    fund_id INTEGER NOT NULL,
    date_id INTEGER NOT NULL,
    nav REAL NOT NULL,
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE IF NOT EXISTS dim_fund2 (
    fund_id INTEGER PRIMARY KEY,
    amfi_code TEXT UNIQUE NOT NULL,
    fund_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS fact_nav2 (
    nav_id INTEGER PRIMARY KEY,
    fund_id INTEGER NOT NULL,
    date_id INTEGER NOT NULL,
    nav REAL NOT NULL,
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE IF NOT EXISTS dim_fund4 (
    fund_id INTEGER PRIMARY KEY,
    amfi_code TEXT UNIQUE NOT NULL,
    fund_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS fact_nav4 (
    nav_id INTEGER PRIMARY KEY,
    fund_id INTEGER NOT NULL,
    date_id INTEGER NOT NULL,
    nav REAL NOT NULL,
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE IF NOT EXISTS dim_fund3(
    fund_id INTEGER PRIMARY KEY,
    amfi_code TEXT UNIQUE NOT NULL,
    fund_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS fact_nav3 (
    nav_id INTEGER PRIMARY KEY,
    fund_id INTEGER NOT NULL,
    date_id INTEGER NOT NULL,
    nav REAL NOT NULL,
    FOREIGN KEY (fund_id) REFERENCES dim_fund(fund_id),
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id)
);