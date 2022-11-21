salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

money_capital = 0  # количество денег, чтобы прожить 10 месяцев

for _ in range(months):
    delta = spend - salary  # расходы текущего месяца, покрываемые подушкой безопасности
    money_capital += delta  # подушка безопасности на текущий месяц
    spend *= 1 + increase  # увеличение расходов в текущем месяце из-за роста цен

print(round(money_capital))
