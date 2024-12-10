import numpy as np

# Исходные данные
supply = np.array([280, 175, 125, 130])
demand = np.array([90, 180, 310, 130])
cost_matrix = np.array([
    [4, 5, 3, 7],
    [7, 6, 2, 9],
    [1, 3, 9, 8],
    [2, 4, 5, 6]
])

# Метод северо-западного угла
def north_west_corner(supply, demand, cost_matrix):
    n = len(supply)
    m = len(demand)
    solution = np.zeros((n, m), dtype=int)
    i = 0
    j = 0

    while i < n and j < m:
        if supply[i] <= demand[j]:
            solution[i, j] = supply[i]
            demand[j] -= supply[i]
            i += 1
        else:
            solution[i, j] = demand[j]
            supply[i] -= demand[j]
            j += 1

    return solution, cost_matrix * solution

# Вычисление начального решения
solution, total_cost = north_west_corner(supply.copy(), demand.copy(), cost_matrix)

# Вывод результатов
print("Начальное решение (метод северо-западного угла):")
print(solution)
print("Общая стоимость:", np.sum(total_cost))

# Метод потенциалов и аппроксимация Фогеля требуют более сложных вычислений и могут быть реализованы отдельно.
