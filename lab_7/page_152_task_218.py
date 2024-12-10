import numpy as np
from scipy.optimize import linprog

# Матрица затрат
cost_matrix = np.array([
    [1, 7, 9, 5],
    [4, 2, 6, 8],
    [3, 8, 1, 2]
])

# Предложение (запасы)
supply = np.array([120, 280, 160])

# Потребности
demand = np.array([130, 220, 60, 70])

# Коэффициенты целевой функции
c = cost_matrix.flatten()

# Матрица ограничений
A_eq = []
for i in range(len(supply)):
    row = np.zeros(len(supply) * len(demand))
    for j in range(len(demand)):
        row[i * len(demand) + j] = 1
    A_eq.append(row)

for j in range(len(demand)):
    row = np.zeros(len(supply) * len(demand))
    for i in range(len(supply)):
        row[i * len(demand) + j] = 1
    A_eq.append(row)

A_eq = np.array(A_eq)

# Вектор правых частей
b_eq = np.concatenate((supply, demand))

# Границы переменных (все переменные неотрицательны)
bounds = [(0, None) for _ in range(len(supply) * len(demand))]

# Решение задачи линейного программирования
result = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

# Проверка успешного решения
if result.success:
    # Оптимальный план перевозки
    optimal_plan = result.x.reshape(len(supply), len(demand))

    # Вывод результатов
    print("Оптимальный план перевозки:")
    print(optimal_plan)
    print("Минимальные затраты:", result.fun)
else:
    print("Решение не найдено.")