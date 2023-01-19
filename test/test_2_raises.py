import pytest
from src.library import zero_division

# ПРОВЕРКА ОЖИДАЕМЫХ ИСКЛЮЧЕНИЙ
# assert в контексте pytest.raises - для проверки, что вызвано ожидаемое исключение
# !нужно импортировать бибилиотеку pytest: import pytest


# 1. запустить тест с assert, чтобы в полученном трейсбеке получить исключение ZeroDivisionError
def test_zero_exeption():
    assert zero_division(1) == 8

# 2. переписать тест на проверку получение исключения ZeroDivisionError
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        zero_division(4)
