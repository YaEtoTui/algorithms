import numpy as np
from scipy.optimize import linprog

# Матрица игры
A = np.array([[2, 5], [6, 4]])

# Определение нижней границы выигрыша
min_row = np.min(A, axis=1)
v_lower = np.max(min_row)

# Определение верхней границы выигрыша
max_col = np.max(A, axis=0)
v_upper = np.min(max_col)

# Проверка на наличие седловой точки
if v_lower == v_upper:
    v = v_lower
    print(f"Цена игры: {v}")
    print("Оптимальные стратегии находятся в соответствующих строке и столбце.")
else:
    print("Седловой точки нет, используем метод симплекс для нахождения оптимальных стратегий.")

    # Решение задачи линейного программирования для игрока 1 (строит примые)
    m, n = A.shape
    c1 = -np.ones(n)
    A_eq1 = A.T
    b_eq1 = np.ones(m)
    bounds1 = [(0, 1) for _ in range(n)]
    result1 = linprog(c1, A_eq=A_eq1, b_eq=b_eq1, bounds=bounds1, method='simplex')

    # Решение задачи линейного программирования для игрока 2 (выбирает столбцы)
    c2 = np.ones(m)
    A_eq2 = A
    b_eq2 = np.ones(n)
    bounds2 = [(0, 1) for _ in range(m)]
    result2 = linprog(c2, A_eq=A_eq2, b_eq=b_eq2, bounds=bounds2, method='simplex')

    v = 1 / result1.fun
    print(f"Цена игры: {v}")
    print(f"Оптимальная стратегия для игрока 1: {result1.x}")
    print(f"Оптимальная стратегия для игрока 2: {result2.x}")
