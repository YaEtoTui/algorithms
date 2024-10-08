from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus, value

from data_object import DataObject
from input_data import c, a, b, A, j, Y

# Создание объекта данных
data_list = [DataObject(c_j, a_j, b_j, A_jc, j_i, y_j) for c_j, a_j, b_j, A_jc, j_i, y_j in zip(c, a, b, A, j, Y)]

# Погрешность
infelicity = 0.5
data_filter_list = [data for data in data_list if (8 - infelicity <= data.A <= 9 + infelicity)
                    and ((data.Y is not None) and (17 - infelicity <= data.Y <= 19 + infelicity))
                    ]


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
            print(data.a)
        if data.b is not None:
            problem += data.x >= data.b
            print(data.b)

    # Решение задачи
    problem.solve()

    # Вывод результатов
    print(f"Статус: {LpStatus[problem.status]}")
    print("============================")
    print(f"Оптимальная стоимость: {value(problem.objective)}")
    print("Оптимальные переменные:")
    test_x_sum = 0
    for v in problem.variables():
        if v.varValue != 0:
            test_x_sum += v.varValue
            print(f"{v.name} = {v.varValue}")
    print("============================")
    print("sum(x) =", test_x_sum)


if not data_filter_list:
    print("Решений нет")
else:
    find_solution()