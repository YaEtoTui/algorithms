from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpStatus, value

# Данные задачи
c = [8.3, 7.3, 6.3, 9.6, 8.6, 7.6, 8.9, 7.9, 6.9, 8.6, 7.6, 6.6,
     10.5, 9.5, 8.5, 9.2, 7.2, 6.2, 7.5, 6.5, 5.5, 9.0, 8.0, 7.0,
     7.0, 6.0, 5.0, 6.0]
a = [0.10, 0.10, 0.04, 0.10, 0.25, 0.30, 0.30, 0.05]  # Максимальные участия, пример
b = [0, 0.10, 0.02, 0, 0.10, 0, 0.20, 0.05]         # Минимальные участия, пример

Q = 100  # Общее количество капитальных вложений
P = 200  # Общая потребность в коксе

# Создание задачи минимизации
problem = LpProblem("Minimize_Coke_Cost", LpMinimize)

# Создание переменных (xj) для каждой марки угля
x = [LpVariable(f"x{i+1}", lowBound=0) for i in range(28)]

# Целевая функция
problem += lpSum(c[i] * x[i] for i in range(28))

# Ограничение на сумму долей
problem += lpSum(x) == 1

# Ограничения на минимальное и максимальное участие
# Это пример, используйте фактические данные
for i, (a_i, b_i) in enumerate(zip(a, b)):
    if a_i is not None:
        problem += x[i] <= a_i
    if b_i is not None:
        problem += x[i] >= b_i

# Ограничение на капитальные вложения
problem += lpSum(a[i] * x[i] for i in range(len(a))) <= Q / P

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