from scipy.optimize import linprog

from lp.input_data import c, a, b, A, Y

def find_solution(data_filter_list):
    # Коэффициенты целевой функции
    c_filtered = [c[i] for i in data_filter_list]

    # Коэффициенты ограничений
    A_eq = [[1 for _ in data_filter_list]]  # Сумма долей равна 1
    b_eq = [1]

    # Ограничения на минимальное и максимальное участие
    bounds = [(b[i] if b[i] is not None else 0, a[i] if a[i] is not None else 1) for i in data_filter_list]

    # Решение задачи линейного программирования
    result = linprog(c_filtered, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='simplex')

    # Вывод результатов
    print(f"Статус: {result.message}")
    print("============================")
    print(f"Оптимальная стоимость: {result.fun}")
    print("Оптимальные переменные:")
    for i, x in enumerate(result.x):
        print(f"x{data_filter_list[i] + 1} = {x}")
    print("============================")
    print("sum(x) =", sum(result.x))

infelicity = 0.5  # Погрешность
# Фильтрация данных
data_filter_list = [i for i in range(len(c)) if (8 - infelicity <= A[i] <= 9 + infelicity)
                    and ((Y[i] is not None) and (17 - infelicity <= Y[i] <= 18 + infelicity))]

if not data_filter_list:
    print("Решений нет при 17 <= Y <= 18\n")
    data_filter_list = [i for i in range(len(c)) if (8 - infelicity <= A[i] <= 9 + infelicity)
                        and ((Y[i] is not None) and (7 - infelicity <= Y[i] <= 14 + infelicity))]
    if not data_filter_list:
        print("Решений нет при 7 <= Y <= 14")
    else:
        find_solution(data_filter_list)
else:
    find_solution(data_filter_list)