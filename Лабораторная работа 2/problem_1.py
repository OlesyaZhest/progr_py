salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_cap = -(salary - spend)
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
for i in range(1, months):
    total_spend = spend + spend * increase
    spend = total_spend
    money_cap -= salary - total_spend
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_cap))
