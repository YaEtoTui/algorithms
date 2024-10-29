from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus, value, LpBinary

from data_object import DataObject
from input_data import c, a, b, A, j, Y, brand, K, J, G, OC, CC

# Создание объекта данных
data_list = [DataObject(c_j, a_j, b_j, A_jc, j_i, y_j, brand_j) for c_j, a_j, b_j, A_jc, j_i, y_j, brand_j in zip(c, a, b, A, j, Y, brand)]

def find_solution(data_list):
    # Создание задачи минимизации
    problem = LpProblem("Minimize_Coke_Cost", LpMinimize)

    # Создание переменных (x_j) для каждой марки угля и добавление их в data_filter
    for data in data_list:
        data.set_x(LpVariable(f"x{data.j}", lowBound=0))

    # Целевая функция
    problem += lpSum(data.c * data.x for data in data_list)

    x = [x.x for x in data_list]
    # Ограничение на сумму долей
    problem += lpSum(x) == 1

    # Ограничения на минимальное и максимальное участие
    for data in data_list:
        if data.a is not None:
            problem += data.x <= data.a
        if data.b is not None:
            problem += data.x >= data.b

    # Бинарные переменные для выбора варианта
    V_1 = LpVariable("V_1", cat=LpBinary)
    V_2 = LpVariable("V_2", cat=LpBinary)
    V_3 = LpVariable("V_3", cat=LpBinary)

    # Ограничения на выбор одного варианта
    problem += V_1 + V_2 + V_3 == 1

    # Ограничения на марки угля для каждого варианта
    k_j_vars = [data.x for data in data_list if data.brand in [K, J]]
    g_oc_ss_vars = [data.x for data in data_list if data.brand in [G, OC, CC]]

    problem += lpSum(k_j_vars) == 0.5 * V_1 + 0.2 * V_2 + 0.1 * V_3
    problem += lpSum(g_oc_ss_vars) == 0.5 * V_1 + 0.8 * V_2 + 0.9 * V_3

    # # Ограничения для случаев, когда нет решений
    # problem += lpSum([data.x for data in data_list if data.brand in [K]]) == 0.5 * V_1
    # problem += lpSum([data.x for data in data_list if data.brand in [J]]) == 0.5 * V_1
    # problem += lpSum([data.x for data in data_list if data.brand in [OC, CC]]) == 0.5 * V_1

    # Решение задачи
    problem.solve()

    # Вывод результатов
    print(f"Статус: {LpStatus[problem.status]}")
    print("============================")
    print(f"Оптимальная стоимость: {value(problem.objective)}")
    print("Оптимальные переменные:")
    x_sum = 0
    for v in problem.variables():
        if v.name.__contains__("x"):
            x_sum += v.varValue
        print(f"{v.name} = {v.varValue}")
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