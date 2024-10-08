import numpy as np

def print_tableau(tableau):
    """
    Функция для вывода таблицы симплекс-метода на консоль.
    """
    print("Таблица симплекс-метода:")
    print(tableau)
    print("\n")

def simplex(c, A, b):
    """
    Реализация симплекс-метода для решения задачи линейного программирования.

    Параметры:
    c -- вектор коэффициентов целевой функции
    A -- матрица коэффициентов ограничений
    b -- вектор правых частей ограничений
    bounds -- границы для переменных x (минимальное и максимальное участие марки угля в шихте)

    Возвращает:
    optimal_value -- оптимальное решение
    obj -- значение целевой функции в оптимальной точке
    """
    m, n = A.shape
    tableau = np.zeros((m+1, n+m+1))
    tableau[:-1, :n] = A
    tableau[:-1, n:n+m] = np.eye(m)
    tableau[:-1, -1] = b
    tableau[-1, :n] = -c

    print_tableau(tableau)  # Вывод начальной таблицы

    while True:
        # Выбор входящей переменной (переменная с наименьшим индексом)
        pivot_col = np.argmin(tableau[-1, :-1])
        if tableau[-1, pivot_col] >= 0:
            break

        # Выбор исходящей переменной (минимальное соотношение)
        ratios = np.full(m, np.inf)
        for i in range(m):
            if tableau[i, pivot_col] > 0:
                ratios[i] = tableau[i, -1] / tableau[i, pivot_col]

        if np.all(ratios == np.inf):
            raise ValueError("Задача не имеет решения (неограниченная задача).")

        pivot_row = np.argmin(ratios)

        # Преобразование таблицы
        tableau[pivot_row, :] /= tableau[pivot_row, pivot_col]
        for i in range(m + 1):
            if i != pivot_row:
                tableau[i, :] -= tableau[i, pivot_col] * tableau[pivot_row, :]

        print_tableau(tableau)  # Вывод таблицы после каждого шага

    # Извлечение решения
    x = np.zeros(n)
    for i in range(n):
        col = tableau[:-1, i]
        if np.count_nonzero(col) == 1 and np.sum(col) == 1:
            x[i] = tableau[np.argmax(col), -1]

    obj = tableau[-1, -1]
    return x, obj

# Пример данных
c = np.array([
    7.6 * 0.1,
    7.5 * 0.05,
    6.5 * 0.3,
    5.5 * 0.3,
    7 * 0.1,
    6 * 0.1,
    6 * 0.05
])  # Удельные эксплуатационные затраты
# Ограничения
A = np.array([
    [
        0.1, 0.05, 0.3, 0.3, 0.1, 0.1, 0.05  # 7
    ],  # 1-ое ограничение

    # 2-ое ограничение
    [
        0.1, 0, 0, 0, 0, 0, 0
    ],
    [
        0, 0.05, 0, 0, 0, 0, 0
    ],
    [
        0, 0, 0.3, 0, 0, 0, 0
    ],
    [
        0, 0, 0, 0.3, 0, 0, 0
    ],
    [
        0, 0, 0, 0, 0.1, 0, 0
    ],
    [
        0, 0, 0, 0, 0, 0.1, 0
    ],
    [
        0, 0, 0, 0, 0, 0, 0.05
    ]

])
b = np.array([
    1,

    0.1,
    0.3,
    0.3,
    0.3,
    0.1,
    0.1,
    0.05

])  # Правая часть ограничений

# Решение задачи
optimal_value, obj = simplex(c, A, b)
print("Оптимальное решение:", optimal_value)
print("Минимальные затраты на 1т чугуна:", obj)