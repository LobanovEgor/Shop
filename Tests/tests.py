import pytest
from functions_to_test import *


@pytest.mark.parametrize("total_sum, initial_balance, user_input, expected_output", [
    (100, [50, 30, 20], '40;20;40', 'Успешная оплата! Осталось - [10, 10, -20]'),
    (50, [25, 15, 10], '10;20;30', 'Неправильный ввод! Сумма оплаты не соответствует общей сумме'),
    (50, [25, 25, 25], '', ('Неправильный ввод', 'Введите оплату'))
])
def test_pay_func(total_sum, initial_balance, user_input, expected_output):
    assert pay_func(total_sum, initial_balance.copy(), user_input) == expected_output

# Тест проверяет случай sum > balance_sum
def test_check_balance_sum_greater_than_sum():
    balance = [50, 30, 20]
    sum = 100
    assert check_sum_func(balance, sum, False, []) == False

# Тест проверяет случай sum = 0
def test_check_balance_sum_zero():
    balance = [50, 30, 20]
    sum = 0
    assert check_sum_func(balance, sum, False, []) == False

# Тест проверяет случай наличия товара 'Пиво 50 руб' в корзине при disabled = False
def test_check_balance_beer_in_cart_disabled_false():
    balance = [50, 30, 20]
    sum = 70
    assert check_sum_func(balance, sum, False, ['Пиво 50 руб']) == False

# Тест проверяет случай, когда все условия выполняются успешно
def test_check_balance_all_conditions_met():
    balance = [50, 30, 20]
    sum = 70
    assert check_sum_func(balance, sum, True, []) == True

# Тест проверяет случай по умолчанию
def test_check_balance_default():
    balance = [50, 30, 20]
    sum = 30
    assert check_sum_func(balance, sum, False, []) == True


# Тест проверяет случай, когда вес и стоимость фруктов положительные
def test_getWeight_positive_values():
    weight = 3
    fruit_cost = 10
    expected_output = "30 сумма товаров в корзине"

    assert getWeight(weight, fruit_cost) == expected_output


# Тест проверяет случай, когда вес равен 0
def test_getWeight_zero_weight():
    weight = 0
    fruit_cost = 10
    expected_output = "0 сумма товаров в корзине"

    assert getWeight(weight, fruit_cost) == expected_output


# Тест проверяет случай, когда стоимость фруктов равна 0
def test_getWeight_zero_fruit_cost():
    weight = 5
    fruit_cost = 0
    expected_output = "0 сумма товаров в корзине"

    assert getWeight(weight, fruit_cost) == expected_output


# Тест проверяет случай, когда вес и стоимость фруктов отрицательные
def test_getWeight_negative_values():
    weight = -2
    fruit_cost = 10
    expected_output = "-20 сумма товаров в корзине"

    assert getWeight(weight, fruit_cost) == expected_output