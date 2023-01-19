from src.library import increase_by_1, even_number

# ПРОВЕРКА ФАКТИЧЕСКИХ ЗНАЧЕНИЙ ОЖИДАЕМЫМ
# assert - оператор для проверки соответствия ожидаемых результатов фактическим

# тест пройдет
def test_answer_positive():
    assert increase_by_1(3) == 4

# тест НЕ пройдет: упадет assert, в трейсбэке увидим аналитическую инфу
def test_answer_negative():
    assert increase_by_1(4) == 4

# тест НЕ пройдет: упадет assert, в трейсбэке увидим текст сообщения об ошибке в кавычках
def test_check_comment():
    assert increase_by_1(1) == 4, "Unexpected sum of the number increased by 1"

def test_even_numver():
    assert even_number(4) == 0, "Value is odd, expected even"
