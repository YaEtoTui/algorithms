from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus, value
from data_object import DataObject
from input_data import c, a, b, A, Q, P

# Создание объекта данных
data_list = [DataObject(c_j, a_j, b_j, A_jc) for c_j, a_j, b_j, A_jc in zip(c, a, b, A)]

data_filter = []
for data in data_list:
    if (8 <= data.A <= 9):
        data_filter += data

# Создание задачи минимизации
problem = LpProblem("Minimize_Coke_Cost", LpMinimize)

# Создание переменных (x_j) для каждой марки угля
x = [LpVariable(f"x{i+1}", lowBound=0) for i in range(28)]

# Целевая функция
problem += lpSum(c[i] * x[i] for i in range(28))

# Ограничение на сумму долей
problem += lpSum(x) == 1

# Ограничения на минимальное и максимальное участие
for i, (a_i, b_i) in enumerate(zip(a, b)):
    if a_i is not None:
        problem += x[i] <= a_i
        print(a_i)
    if b_i is not None:
        problem += x[i] >= b_i
        print(b_i)

# # Ограничение на капитальные вложения
# problem += lpSum(q[i] * x[i] for i in range(len(a))) <= Q / P

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