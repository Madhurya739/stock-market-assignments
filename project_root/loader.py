def normalize_year(value):
    """
    Normalize different input formats into a valid year (int).
    Accepts int, float, str. Raises ValueError for invalid inputs.
    Valid range: 1900–2100.
    """
    if value is None:
        raise ValueError("Year cannot be None")

    # Convert booleans explicitly to error
    if isinstance(value, bool):
        raise ValueError("Boolean is not a valid year")

    try:
        # Convert to int safely
        year = int(float(str(value).strip()))
    except Exception:
        raise ValueError(f"Invalid year format: {value}")

    if year < 1900 or year > 2100:
        raise ValueError(f"Year {year} out of valid range (1900–2100)")

    return year
