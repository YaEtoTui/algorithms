def f1(x):
    return 0.4 * x

def f2(x):
    return 0.3 * x

def phi1(x):
    return 0.5 * x


def phi2(x):
    return 0.8 * x

# Инициализация параметров
phi0 = 10000
n = 4

# Создание таблицы для хранения максимальных доходов
Z = [{} for _ in range(n + 1)]

# Инициализация последнего шага
for phi in range(phi0 + 1):
    Z[n][phi] = max(f1(x) + f2(phi - x) for x in range(phi + 1))

# Заполнение таблицы снизу вверх
for k in range(n - 1, 0, -1):
    for phi in range(phi0 + 1):
        Z[k][phi] = max(f1(x) + f2(phi - x) + Z[k + 1].get(int(phi1(x) + phi2(phi - x)), 0)
                      for x in range(phi + 1))

# Определение максимального дохода
Z_max = Z[1][phi0]
print("Максимальный доход:", Z_max)