# Функции дохода для каждого предприятия
def f1(x):
    if x == 0:
        return 0
    elif x == 40:
        return 8
    elif x == 80:
        return 10
    elif x == 120:
        return 11
    elif x == 160:
        return 12
    elif x == 200:
        return 18
    else:
        return 0

def f2(x):
    if x == 0:
        return 0
    elif x == 40:
        return 6
    elif x == 80:
        return 9
    elif x == 120:
        return 11
    elif x == 160:
        return 13
    elif x == 200:
        return 15
    else:
        return 0

def f3(x):
    if x == 0:
        return 0
    elif x == 40:
        return 3
    elif x == 80:
        return 4
    elif x == 120:
        return 7
    elif x == 160:
        return 11
    elif x == 200:
        return 18
    else:
        return 0

def f4(x):
    if x == 0:
        return 0
    elif x == 40:
        return 4
    elif x == 80:
        return 6
    elif x == 120:
        return 8
    elif x == 160:
        return 13
    elif x == 200:
        return 16
    else:
        return 0

# Функция для вычисления максимального дохода
def max_profit(n, total_funds, functions):
    # Инициализация таблицы для хранения максимального дохода
    dp = [[0] * (total_funds + 1) for _ in range(n + 1)]

    # Заполнение таблицы
    for i in range(1, n + 1):
        for j in range(total_funds + 1):
            max_val = 0
            for k in range(0, j + 1, 40):
                max_val = max(max_val, functions[i - 1](k) + dp[i - 1][j - k])
            dp[i][j] = max_val

    # Восстановление оптимального распределения
    allocation = [0] * n
    remaining_funds = total_funds
    for i in range(n, 0, -1):
        for k in range(0, remaining_funds + 1, 40):
            if dp[i][remaining_funds] == functions[i - 1](k) + dp[i - 1][remaining_funds - k]:
                allocation[i - 1] = k
                remaining_funds -= k
                break

    return dp[n][total_funds], allocation

# Основные параметры
total_funds = 200
n = 4
functions = [f1, f2, f3, f4]

# Вычисление максимального дохода и оптимального распределения
max_profit_value, allocation = max_profit(n, total_funds, functions)

print(f"Максимальный доход: {max_profit_value}")
print(f"Оптимальное распределение: {allocation}")