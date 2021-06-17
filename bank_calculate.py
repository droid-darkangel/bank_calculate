def calculate_income(rate, money, month):
    if money<0:
        return 0
    for i in range(1, month+1):
        money = round(money+money*rate/100/12, 2)
    
    return money

while True:
    data = input('Вы будете считать? Yes/No: ')
    if data.lower() == 'yes':
        money = int(input('Введите сумму: '))
        rate = int(input('Введите процентную ставку: '))
        period = int(input('Введите период ведения счёта в месяцах: '))
        result = calculate_income(rate, money, period)
        print(f'Параметры счёта:\nСумма: {money}\nСтавка в процентах: {rate}\nПериод: {period}\nСумма на счёте в конце периода: {result}')

    elif data.lower() == 'no':
        break
print('Работа завершена')