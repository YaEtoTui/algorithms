import pandas as pd

# Данные задачи
monthly_salaries = [2000, 3000, 3000, 2000]
monthly_expenses = [1000, 2000, 3000, 4000]
initial_savings = 18000
annual_interest_rate = 19 / 100
monthly_interest_rate = annual_interest_rate / 12
monthly_storage_fee = 1

# Инициализация переменных
total_savings = initial_savings
total_expenses = 0

# Список для хранения ежемесячных данных
monthly_data = []

# Расчет ежемесячных данных
for month in range(4):
    salary = monthly_salaries[month]
    expense = monthly_expenses[month]
    interest = total_savings * monthly_interest_rate
    storage_fee = monthly_storage_fee if total_savings > 0 else 0

    total_savings += salary - expense + interest - storage_fee
    total_expenses += expense

    monthly_data.append({
        'Месяц': month + 1,
        'Зарплата': salary,
        'Расходы': expense,
        'Проценты': interest,
        'Комиссия за хранение': storage_fee,
        'Общие накопления': total_savings
    })

# Создание DataFrame для отчета
report_df = pd.DataFrame(monthly_data)

# Вывод отчета
print("Ежемесячный отчет:")
print(report_df)

# Вывод итоговых данных
print("\nИтоговые данные:")
print(f"Общие накопления на конец периода: {total_savings:.2f} руб.")
print(f"Общие расходы за период: {total_expenses:.2f} руб.")

# Формулы
print("\nФормулы:")
print("Ежемесячные накопления: Общие накопления + Зарплата - Расходы + Проценты - Комиссия за хранение")
print("Проценты: Общие накопления * Месячная процентная ставка")
print("Месячная процентная ставка: Годовая процентная ставка / 12")
print("Комиссия за хранение: 1 руб., если Общие накопления > 0")

# Сохранение отчета в Excel
report_df.to_excel("monthly_report.xlsx", index=False)

# Добавление листа с формулами
with pd.ExcelWriter("monthly_report.xlsx", mode='a') as writer:
    formulas_df = pd.DataFrame({
        'Описание': [
            "Ежемесячные накопления",
            "Проценты",
            "Месячная процентная ставка",
            "Комиссия за хранение"
        ],
        'Формула': [
            "=D2 + Ежемесячная зарплата - Ежемесячные расходы + Проценты - Комиссия за хранение",
            "=Общие накопления * Месячная процентная ставка",
            "=Годовая процентная ставка / 12",
            "=ЕСЛИ(Общие накопления > 0; 1; 0)"
        ]
    })
    formulas_df.to_excel(writer, sheet_name='Формулы', index=False)

print("\nОтчет сохранен в файл monthly_report.xlsx")
