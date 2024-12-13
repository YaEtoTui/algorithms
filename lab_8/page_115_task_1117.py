# Данные задачи
# Производительность оборудования (количество изделий в час)
from scipy.optimize import linprog

productivity = {
    "I": [8, 7, 4, 5],
    "II": [6, 8, 6, 4],
}
# Затраты на производство одного изделия (руб.)
costs = {
    "I": [2.7, 2.6, 2.7, 2.4],
    "II": [2.6, 2.7, 2.6, 2.5],
}
# Ограничения на время работы оборудования (часы)
time_limits = {
    "I": 80,
    "II": 60,
}
# Минимальные требования по количеству изделий
min_requirements = [240, 160, 150, 220]
# Формируем целевую функцию (минимизация затрат)
c = costs["I"] + costs["II"]
# Ограничения на минимальное количество изделий (>=)
A_ub = []
b_ub = []
# Каждое изделие должно быть произведено в достаточном количестве
for i in range(4):
    constraint = [0] * 8
    constraint[i] = -productivity["I"][i]  # Для оборудования I
    constraint[i + 4] = -productivity["II"][i]  # Для оборудования II
    A_ub.append(constraint)
    b_ub.append(-min_requirements[i])
# Ограничения на время работы оборудования
A_ub.append([1] * 4 + [0] * 4)
b_ub.append(time_limits["I"])
A_ub.append([0] * 4 + [1] * 4)
b_ub.append(time_limits["II"])
# Ограничения на неотрицательность переменных
bounds = [(0, None) for _ in range(8)]
# Решение задачи линейного программирования
result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")
# Обработка результатов
if result.success:
    production_I = result.x[:4]
    production_II = result.x[4:]
    print("Решение найдено:")
    for i in range(4):
        print(f"Изделие {i + 1}: на оборудовании I: {round(production_I[i], 2)} ч, на оборудовании II: {round(production_II[i], 2)} ч")
    print(f"Общие затраты: {round(result.fun, 2)} руб.")
else:
    print("Решение не найдено")
