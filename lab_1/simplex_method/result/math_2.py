from scipy.optimize import linprog

from lab_1.lp.data_object import DataObject
from lab_1.lp.input_data import c, a, b, A, j, Y, brand

# Создание объекта данных
data_list = [DataObject(c_j, a_j, b_j, A_jc, j_i, y_j, brand_j) for c_j, a_j, b_j, A_jc, j_i, y_j, brand_j in zip(c, a, b, A, j, Y, brand)]

def find_solution(data_list):
    # Коэффициенты целевой функции
    c_coeffs = [data.c for data in data_list]

    # Ограничения
    A_eq = []
    b_eq = []
    A_ub = []
    b_ub = []

    # Ограничение на сумму долей
    A_eq.append([1] * len(data_list))
    b_eq.append(1)

    # Ограничения на минимальное и максимальное участие
    for i, data in enumerate(data_list):
        if data.a is not None:
            A_ub.append([0] * i + [1] + [0] * (len(data_list) - i - 1))
            b_ub.append(data.a)
        if data.b is not None:
            A_ub.append([0] * i + [-1] + [0] * (len(data_list) - i - 1))
            b_ub.append(-data.b)


    # Решение задачи
    result = linprog(c_coeffs, A_eq=A_eq, b_eq=b_eq, A_ub=A_ub, b_ub=b_ub, method='simplex')

    # Вывод результатов
    print(f"Статус: {result.message}")
    print("============================")
    print(f"Оптимальная стоимость: {result.fun}")
    print("Оптимальные переменные:")
    x_sum = 0
    for i, x in enumerate(result.x):
        x_sum += x
        print(f"x{data_list[i].j} = {x}")
    print("============================")
    print("sum(x) =", x_sum)

infelicity = 0.5 # Погрешность
data_filter_list = [data for data in data_list if (8 - infelicity <= data.A <= 9 + infelicity)
                    and ((data.Y is not None) and (17 - infelicity <= data.Y <= 18 + infelicity))
                    ]

if not data_filter_list:
    print("Решений нет при 17 <= Y <= 18\n")
    data_filter_list = [data for data in data_list if (8 - infelicity <= data.A <= 9 + infelicity)
                        and ((data.Y is not None) and (7 - infelicity <= data.Y <= 14 + infelicity))
                        ]
    if not data_filter_list:
        print("Решений нет при 7 <= Y <= 14")
    else:
        find_solution(data_filter_list)
else:
    find_solution(data_filter_list)