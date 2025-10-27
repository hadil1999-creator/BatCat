import pytest
from batcat.core import add_numbers, get_date_with_delta

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_get_date_with_delta():
    from datetime import date, timedelta
    today = date.today()
    assert get_date_with_delta(0) == today.strftime('%Y/%m/%d')
    assert get_date_with_delta(1) == (today - timedelta(days=1)).strftime('%Y/%m/%d')