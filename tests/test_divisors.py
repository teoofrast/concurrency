import pytest

from divisors import find_divisors, divisor


def test_find_divisors():
    """
    Тест работы функций find_divisors
    """
    assert find_divisors(1_000_000, 1, int(1_000_000 ** 0.5)) == [1, 2, 4, 5, 8, 10, 16, 20, 25, 32, 40, 50, 64, 80,
                                                                  100, 125, 160, 200, 250, 320, 400, 500, 625, 800,
                                                                  1000, 1250, 1600, 2000, 2500, 3125, 4000, 5000, 6250,
                                                                  8000, 10000, 12500, 15625, 20000, 25000, 31250, 40000,
                                                                  50000, 62500, 100000, 125000, 200000, 250000, 500000,
                                                                  1000000]


def test_negative_find_divisors():
    """
    Тест работы функций find_divisors вне заданного диапазона чисел
    """
    with pytest.raises(ValueError):
        find_divisors(999999999, 1, int(999999999 ** 0.5))


def test_negative_number_find_divisors():
    """
    Тест работы функций find_divisors с отрицательным числом
    """
    with pytest.raises(ValueError):
        find_divisors(-1, 1, int(-1 ** 0.5))


def test_string_find_divisors():
    """
    Тест работы функций find_divisors со строковым типом данных
    """
    with pytest.raises(TypeError):
        find_divisors("hello", 1, int("hello" ** 0.5))


def test_list_find_divisors():
    """
    Тест работы функций find_divisors со списком
    """
    with pytest.raises(TypeError):
        find_divisors([1, 2], 1, int([1, 2] ** 0.5))


def test_divisor():
    """
    Тест работы функций divisor
    """
    assert divisor(1_000_000) == [1, 2, 4, 5, 8, 10, 16, 20, 25, 32, 40, 50, 64, 80,
                                  100, 125, 160, 200, 250, 320, 400, 500, 625, 800,
                                  1000, 1250, 1600, 2000, 2500, 3125, 4000, 5000, 6250,
                                  8000, 10000, 12500, 15625, 20000, 25000, 31250, 40000,
                                  50000, 62500, 100000, 125000, 200000, 250000, 500000,
                                  1000000]


def test_negative_divisor():
    """
    Тест работы функций divisor вне заданного диапазона чисел
    """
    with pytest.raises(ValueError):
        divisor(1)


def test_negative_number_divisor():
    """
    Тест работы функций divisor с отрицательным числом
    """
    with pytest.raises(TypeError):
        divisor(-1)


def test_string_divisor():
    """
    Тест работы функций divisor со строковым типом данных
    """
    with pytest.raises(TypeError):
        divisor("hello")


def test_list_divisor():
    """
    Тест работы функций divisor со списком
    """
    with pytest.raises(TypeError):
        divisor([1, 2])
