import numpy as np
from scipy.optimize import linprog

from lp.data_object import DataObject
from lp.input_data import c, a, b, A, j, Y, brand, K, K_2, J, G, OC, CC

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

    # # Бинарные переменные для выбора варианта
    # V_1 = 0
    # V_2 = 0
    # V_3 = 0

    # # Ограничения на выбор одного варианта
    # A_eq.append([0] * len(data_list))
    # b_eq.append(1)

    # # Ограничения на марки угля для каждого варианта
    # k_j_vars = [i for i, data in enumerate(data_list) if data.brand in [K, J]]
    # g_oc_ss_vars = [i for i, data in enumerate(data_list) if data.brand in [G, OC, CC]]
    #
    # A_eq.append([1 if i in k_j_vars else 0 for i in range(len(data_list))])
    # b_eq.append(0.5 * V_1 + 0.2 * V_2 + 0.1 * V_3)
    #
    # A_eq.append([1 if i in g_oc_ss_vars else 0 for i in range(len(data_list))])
    # b_eq.append(0.5 * V_1 + 0.8 * V_2 + 0.9 * V_3)

    # # Ограничения для случаев, когда нет решений
    # A_eq.append([1 if data.brand == K else 0 for data in data_list])
    # b_eq.append(0.5 * V_1)
    #
    # A_eq.append([1 if data.brand == J else 0 for data in data_list])
    # b_eq.append(0.5 * V_1)
    #
    # A_eq.append([1 if data.brand in [OC, CC] else 0 for data in data_list])
    # b_eq.append(0.5 * V_1)

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
        print(f"x{i+1} = {x}")
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