money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
count = 0
money_capital -= 1000
while money_capital > 0:
    total_spend = spend + spend * increase
    spend = total_spend
    # print(total_spend)
    money_capital -= abs(salary - total_spend)
    count += 1

print("Количество месяцев, которое можно протянуть без долгов:", count)
