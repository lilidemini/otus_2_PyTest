import pytest

# параметризованный тест - выполняется одна и та же функция,
# но с разными значениями аргумента

# создадим один параметризованный тест
# на проверку функции деления вместо нескольких тестов
# с использованием декоратора parametrize

@pytest.mark.parametrize('a, b, expected',
                         [(10,1,10),(0,10,0),(0.1,0.1,1),(10,3,3.3333333333333335)])

# при запуске одной функции ниже выполнится 4 теста
def test_parametrize_dividor(a, b , expected):
    assert a / b == expected


