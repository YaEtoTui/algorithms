import numpy as np
from scipy.optimize import linprog

# Целевая функция в виде коэффициентов
c = np.array([2, 5, -4, 2])

# Матрица неравенств
A_ub = np.array([
    [2, 1, 0, 0],    # 2x1 + x2 <= 20
    [-1, -3, 0, 0],   # -x1 + 3x2 <= 27
    [0, 0, 2, 3],     # 2x3 + 3x4 <= 28
    [0, 0, -1, 2],    # -x3 + 2x4 <= 12
    [-1, 0, 0, 0],    # -x1 <= 0 (эквивалентно x1 >= 0)
    [0, -1, 0, 0],    # -x2 <= 0 (эквивалентно x2 >= 0)
    [0, 0, -1, 0],    # -x3 <= 0 (эквивалентно x3 >= 0)
    [0, 0, 0, -1]     # -x4 <= 0 (эквивалентно x4 >= 0)
])

# Вектор правых частей неравенств
b_ub = np.array([20, -27, 28, 12, 0, 0, 0, 0])

# Границы переменных
bounds = [(0, None), (0, None), (0, None), (0, None)]

# Параметры оптимизации
options = {'disp': True}

# Решение задачи
result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, options=options)

# Вывод результата
if result.success:
    print("Оптимальное решение найдено:")
    print("x =", result.x)
    print("F(x) =", result.fun)
else:
    print("Оптимальное решение не найдено.")
