import numpy as np

# Исходные данные
cost_matrix = np.array([
    [7, 8, 1, 2],
    [4, 5, 9, 8],
    [9, 2, 3, 6]
])
supply = np.array([120, 140, 170])
demand = np.array([50, 190, 110, 140])

# Инициализация опорного плана
basic_plan = np.zeros_like(cost_matrix)


# Функция для нахождения минимального элемента в матрице
def find_min_element(matrix, supply, demand):
    min_value = float('inf')
    min_pos = (-1, -1)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if supply[i] > 0 and demand[j] > 0 and matrix[i, j] < min_value:
                min_value = matrix[i, j]
                min_pos = (i, j)
    return min_pos, min_value


# Основной алгоритм
while np.any(supply > 0) and np.any(demand > 0):
    min_pos, min_value = find_min_element(cost_matrix, supply, demand)
    i, j = min_pos

    # Определение минимального значения для перемещения
    quantity = min(supply[i], demand[j])

    # Обновление опорного плана
    basic_plan[i, j] = quantity

    # Обновление запасов и потребностей
    supply[i] -= quantity
    demand[j] -= quantity

# Вывод опорного плана
print("Опорный план:")
print(basic_plan)

# Проверка суммы опорного плана
total_cost = np.sum(basic_plan * cost_matrix)
print("Общая стоимость: ", total_cost)
