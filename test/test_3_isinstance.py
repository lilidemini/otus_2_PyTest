# isinstance() - функция, созданная для проверки принадлежности аргумента к типу данных

# ОТЛИЧИЕ type() и isinstance():
# type() возвращает тип переданного аргумента
# isinstance() возвращает True или False,  можно проверить принадлежность к нескольким типам данных

number = 1
list = [1, 'Lili', [333, 456]]

# проверим, что значение в переменной number целое число
def test_check_int_type_number():
    assert isinstance(number, int), 'Wrong type returned, expected integer'

# проверим, что значение с индексом 1 в переменной list целое число или строка
def test_check_different_type_list():
    assert isinstance(list[1], (int, str)), 'Wrong type returned, expected integer'
