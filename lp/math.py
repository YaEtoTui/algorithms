from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus, value

from data_object import DataObject
from input_data import c, a, b, A, j, Y, brand, K, K_2, J, G, OC, CC

# Создание объекта данных
data_list = [DataObject(c_j, a_j, b_j, A_jc, j_i, y_j, brand_j) for c_j, a_j, b_j, A_jc, j_i, y_j, brand_j in zip(c, a, b, A, j, Y, brand)]

def find_solution():
    # Создание задачи минимизации
    problem = LpProblem("Minimize_Coke_Cost", LpMinimize)

    # Создание переменных (x_j) для каждой марки угля и добавление их в data_filter
    for data in data_filter_list:
        data.set_x(LpVariable(f"x{data.j}", lowBound=0))

    # Целевая функция
    problem += lpSum(data.c * data.x for data in data_filter_list)

    x = [x.x for x in data_filter_list]
    # Ограничение на сумму долей
    problem += lpSum(x) == 1

    # Ограничения на минимальное и максимальное участие
    for data in data_filter_list:
        if data.a is not None:
            problem += data.x <= data.a
        if data.b is not None:
            problem += data.x >= data.b

    # Решение задачи
    problem.solve()

    # Вывод результатов
    print(f"Статус: {LpStatus[problem.status]}")
    print("============================")
    print(f"Оптимальная стоимость: {value(problem.objective)}")
    print("Оптимальные переменные:")
    test_x_sum = 0
    for v in problem.variables():
        test_x_sum += v.varValue
        print(f"{v.name} = {v.varValue}")
    print("============================")
    print("sum(x) =", test_x_sum)

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
        find_solution()
else:
    find_solution()