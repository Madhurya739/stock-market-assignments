import pytest
from loader import normalize_year


# --- Valid cases ---
def test_valid_int_year():
    assert normalize_year(2020) == 2020


def test_valid_float_year():
    assert normalize_year(2020.0) == 2020


def test_valid_str_year():
    assert normalize_year("2021") == 2021


def test_valid_str_float_year():
    assert normalize_year("2022.0") == 2022


def test_valid_whitespace_str():
    assert normalize_year(" 2023 ") == 2023


def test_min_valid_year():
    assert normalize_year(1900) == 1900


def test_max_valid_year():
    assert normalize_year(2100) == 2100


def test_large_float_rounds():
    assert normalize_year(2020.999) == 2020


# --- Invalid cases ---
def test_year_below_range():
    with pytest.raises(ValueError):
        normalize_year(1800)


def test_year_above_range():
    with pytest.raises(ValueError):
        normalize_year(2200)


def test_non_numeric_string():
    with pytest.raises(ValueError):
        normalize_year("abcd")


def test_empty_string():
    with pytest.raises(ValueError):
        normalize_year("")


def test_none_input():
    with pytest.raises(ValueError):
        normalize_year(None)


def test_boolean_true():
    with pytest.raises(ValueError):
        normalize_year(True)


def test_boolean_false():
    with pytest.raises(ValueError):
        normalize_year(False)


def test_special_characters():
    with pytest.raises(ValueError):
        normalize_year("2020!")


def test_negative_year():
    with pytest.raises(ValueError):
        normalize_year(-2020)


def test_float_string_invalid():
    with pytest.raises(ValueError):
        normalize_year("20.20.20")


def test_list_input():
    with pytest.raises(ValueError):
        normalize_year([2020])
