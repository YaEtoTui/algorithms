import numpy as np
from scipy.optimize import linear_sum_assignment

# Ввод количества грузов в каждом магазине
gruz1 = [180, 60, 80]
gruz2 = [120, 40, 60, 80]

# Ввод стоимости перевозки единицы груза между магазинами
cost_matrix = np.array([
    [2, 3, 4, 3],
    [5, 3, 1, 2],
    [2, 1, 4, 2]
])

# Функция для вычисления минимальной стоимости перевозки
def min_cost_transportation(gruz1, gruz2, cost_matrix):
    # Создаем матрицу стоимостей для linear_sum_assignment
    max_len = max(len(gruz1), len(gruz2))
    extended_cost_matrix = np.zeros((max_len, max_len))
    extended_cost_matrix[:len(gruz1), :len(gruz2)] = cost_matrix

    # Используем linear_sum_assignment для нахождения минимальной стоимости
    row_ind, col_ind = linear_sum_assignment(extended_cost_matrix)

    # Вычисляем минимальную стоимость
    total_cost = 0
    for i in range(len(row_ind)):
        if i < len(gruz1) and col_ind[i] < len(gruz2):
            total_cost += extended_cost_matrix[row_ind[i], col_ind[i]] * min(gruz1[row_ind[i]], gruz2[col_ind[i]])
            gruz1[row_ind[i]] -= min(gruz1[row_ind[i]], gruz2[col_ind[i]])
            gruz2[col_ind[i]] -= min(gruz1[row_ind[i]], gruz2[col_ind[i]])

    return total_cost

# Вычисляем минимальную стоимость перевозки
min_cost = min_cost_transportation(gruz1, gruz2, cost_matrix)
print("Минимальная стоимость перевозки:", min_cost)
