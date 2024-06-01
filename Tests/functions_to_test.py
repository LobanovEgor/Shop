def pay_func(total_sum, balance, user_input):
    entry = user_input
    if entry == '':
        return 'Неправильный ввод', 'Введите оплату'
    else:
        entry = entry.split(';')
        entry = list(map(int, entry))
        if sum(entry) != total_sum:
            return 'Неправильный ввод!', 'Сумма оплаты не соответствует общей сумме'
        else:
            for i in range(len(entry)):
                balance[i] -= entry[i]
            return f'Успешная оплата! Осталось - {balance}'

def check_sum_func(balance, sum, disabled, cart):
    balance_sum = 0
    for i in balance:
        balance_sum += i
        if sum > balance_sum:
            return False
        elif sum == 0:
            return False
        elif 'Пиво 50 руб' in cart and disabled == False:
            return False
        else:
            return True
def getWeight(weight, fruit_cost):
    if weight < 0:
        return 'Вес не может быть меньше нуля!'
    sum = fruit_cost * weight
    sum_to_pay = f'{sum} сумма товаров в корзине'
    return sum_to_pay