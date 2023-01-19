import pytest
from src.library import dividor

def test_library_dividor_negative():
    assert dividor(-4,2) == -2, 'Division result of 10 and 1 is not equal to 10'

def test_library_dividor_zero_error():
    with pytest.raises(ZeroDivisionError):
        dividor(1,0), 'Error is wrong, expected ZeroDivisionError'
