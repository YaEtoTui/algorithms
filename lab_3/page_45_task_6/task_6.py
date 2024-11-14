# Таблицы значений функций f1, f2, f3 из таблицы 7
f1_table = [2.1, 3.2, 4.3, 5.1, 5.1]
f2_table = [
    [2.2, 2.8, 3.1, 4.3, 6],
    [3.1, 4.2, 5.3, 5.8, 7.1, 8],
    [3.3, 4.5, 6.1, 7.3, None],
    [3.5, 4.8, 6.7, None, None],
    [5.4, 5.9, None, None, None]
]
f3_table = [
    [3.4, 3.8, 4.2, 5.0, 5.0],
    [3.7, 4.1, 4.5, 5.3, 5.3],
    [3.7, 4.1, 4.5, 5.4, None],
    [4.0, 4.5, 4.8, None, None],
    [4.2, 4.8, None, None, None],
    [4.6, None, None, None, None],
    [None, None, None, None, None]
]

# Функция для максимизации Z3 при данных затратах eta2
def Z3_star(eta2):
    max_value = 0
    for x1_plus_x2 in range(eta2 + 1):
        if x1_plus_x2 < len(f3_table) and eta2 < len(f3_table[x1_plus_x2]) and f3_table[x1_plus_x2][eta2] is not None:
            max_value = max(max_value, f3_table[x1_plus_x2][eta2])
    return max_value

# Функция для максимизации Z2 при данных затратах eta1 и значении x2
def Z2_star(x2, eta1):
    max_value = 0
    eta2 = eta1 + x2
    if x2 < len(f2_table) and eta1 < len(f2_table[x2]) and f2_table[x2][eta1] is not None:
        max_value = f2_table[x2][eta1] + Z3_star(eta2)
    return max_value

# Функция для максимизации Z1 при данных затратах eta0 и значении x1
def Z1_star(x1, eta0):
    max_value = 0
    eta1 = eta0 + x1
    if x1 < len(f1_table):
        max_value = f1_table[x1]
        # Итерируем по x2, чтобы найти максимум по Z2
        max_value += max(Z2_star(x2, eta1) for x2 in range(6 - x1 + 1))
    return max_value

# Максимизация функции Z по x1
Z_max = max(Z1_star(x1, 0) for x1 in range(6))
print("Максимальный выпуск продукции:", Z_max)