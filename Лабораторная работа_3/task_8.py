money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0  # количество месяцев, которое можно прожить
nadbavka = spend * increase #надбавка к затратам в рублях
ostatok = money_capital #деньги на первый месяц до получения зарплаты
while ostatok>spend:
        spend+=nadbavka #затраты после надбавки
        ostatok=ostatok+salary-spend #остаток денег после затрат
        month+=1
print(month)