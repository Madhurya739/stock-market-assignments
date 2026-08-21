import pytest
from loader import normalize_year, normalize_ticker

# --- normalize_year tests ---
def test_valid_year_int():
    assert normalize_year(2020) == 2020

def test_valid_year_str():
    assert normalize_year("2021") == 2021

def test_valid_year_float():
    assert normalize_year(2022.0) == 2022

def test_year_out_of_range():
    with pytest.raises(ValueError):
        normalize_year(3000)

def test_invalid_year_string():
    with pytest.raises(ValueError):
        normalize_year("abcd")

# --- normalize_ticker tests ---
def test_ticker_uppercase():
    assert normalize_ticker("aapl") == "AAPL"

def test_ticker_strip_spaces():
    assert normalize_ticker("  msft ") == "MSFT"

def test_ticker_with_dot():
    assert normalize_ticker("brk.b") == "BRK.B"

def test_ticker_with_dash():
    assert normalize_ticker("rds-a") == "RDS-A"

def test_ticker_invalid_type():
    with pytest.raises(ValueError):
        normalize_ticker(123)
