import pytest
from mycalendar.date import Date


def test_date_valid_and_display_format():
    d = Date(12, 31, 2024)
    assert d.month == 12
    assert d.day == 31
    assert d.year == 2024
    assert d.display_date() == "12/31/2024"  # tanpa zero padding


def test_date_invalid_any_sets_default():
    # month invalid
    d1 = Date(13, 5, 2024)
    assert (d1.month, d1.day, d1.year) == (1, 1, 1970)

    # day invalid
    d2 = Date(5, 0, 2024)
    assert (d2.month, d2.day, d2.year) == (1, 1, 1970)

    # type invalid
    d3 = Date("x", 10, 2024)  # type error -> default
    assert (d3.month, d3.day, d3.year) == (1, 1, 1970)


def test_date_properties_are_read_only():
    d = Date(1, 2, 2023)
    with pytest.raises(AttributeError):
        d.month = 3  # tidak ada setter publik
    with pytest.raises(AttributeError):
        d.day = 10
    with pytest.raises(AttributeError):
        d.year = 2025
