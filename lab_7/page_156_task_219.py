import numpy as np

# Таблица 2.14
potrebnosti = np.array([110, 90, 120, 80, 150])
zapasy = np.array([180, 350, 20])

# Таблица 2.15
# Создаем матрицу разностей
raznosti = np.zeros((3, 5))
for i in range(3):
    for j in range(5):
        raznosti[i, j] = potrebnosti[j] - zapasy[i]

# Таблица 2.16
prom_renta = np.array([
    [7, 12, 4, 8, 5],
    [110, 90, 6, 80, 70],
    [6, 13, 8, 7, 4]
])

# Таблица 2.17
zadachi = np.array([
    [0, 0, 120, 0, 60],
    [110, 90, 0, 80, 70],
    [0, 0, 0, 0, 20]
])

tarify = np.array([
    [7, 12, 4, 8, 5],
    [110, 90, 6, 80, 70],
    [6, 13, 8, 7, 4]
])

# Вычисление общей суммы перевозок
S = np.sum(zadachi * tarify)

print(f"Общая сумма перевозок: {S}")

# Определение оптимального плана задачи
optimal_plan = zadachi

print("Оптимальный план задачи:")
print(optimal_plan)
