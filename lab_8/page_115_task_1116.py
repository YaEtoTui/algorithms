# Данные задачи
# Возможные варианты разреза (количество заготовок 45, 35, 50 см для каждого варианта)
from scipy.optimize import linprog

variants = [
    [2, 0, 0],  # Вариант 1
    [1, 1, 0],  # Вариант 2
    [1, 0, 1],  # Вариант 3
    [0, 3, 0],  # Вариант 4
    [0, 1, 1],  # Вариант 5
    [0, 0, 2],  # Вариант 6
]
# Величина отходов для каждого варианта
waste = [20, 30, 15, 5, 25, 10]
# Требуемое количество заготовок каждого типа (45, 35, 50 см)
demand = [40, 30, 20]
# Целевая функция (минимизировать отходы)
c = waste
# Ограничения: каждая строка variants должна покрывать demand
A_ub = [[-variant[i] for variant in variants] for i in range(3)]
b_ub = [-d for d in demand]

# Ограничения: количество прутьев >= 0
bounds = [(0, None) for _ in variants]

# Решение задачи линейного программирования
result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs')

# Обработка результатов
if result.success:
    print("Решение найдено:")
    for i, count in enumerate(result.x):
        print(f"Вариант {i + 1}: {round(count)} прутьев")
    print(f"Общие отходы: {sum(round(count) * waste[i] for i, count in enumerate(result.x))} см")
else:
    print("Решение не найдено")
