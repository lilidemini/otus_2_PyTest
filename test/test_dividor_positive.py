from src.library_1 import dividor

def test_library_dividor_positive():
    assert dividor(10,1) == 10, 'Division result of 10 and 1 is not equal to 10'

def test_library_dividor_zero():
    assert dividor(0,10) == 0, 'Division result of 0 and 10 is not equal to 0'

def test_library_dividor_float():
    assert dividor(0.1, 0.1) == 1, 'Division result of 0.1 and 0.1 is not equal to 1'

def test_library_dividor_endless():
    assert dividor(10, 3) == 3.3333333333333335, 'Division result has remainder'

def test_library_dividor_type():
    assert isinstance(dividor(10, 5), float), 'Wrong type returned, expected type is float'
