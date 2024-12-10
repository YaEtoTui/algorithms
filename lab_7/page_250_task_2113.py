import pulp

# Задача 2.112: Максимизация

# Создаем задачу максимизации
prob_max = pulp.LpProblem("Maximization_Problem", pulp.LpMaximize)

# Переменные
x1 = pulp.LpVariable('x1', lowBound=0)
x2 = pulp.LpVariable('x2', lowBound=0)
x3 = pulp.LpVariable('x3', lowBound=0)

# Целевая функция
prob_max += 5*x1 + 7*x2 + 8*x3, "F"

# Ограничения
prob_max += x1 + x2 + 5*x3 <= 18
prob_max += 3*x1 + 2*x2 + x3 <= 16
prob_max += 4*x1 + 3*x2 + x3 <= 24

# Решаем задачу
prob_max.solve()

# Результаты
print("Status:", pulp.LpStatus[prob_max.status])
print("x1 =", pulp.value(x1))
print("x2 =", pulp.value(x2))
print("x3 =", pulp.value(x3))
print("F =", pulp.value(prob_max.objective))

# Задача 2.113: Минимизация

# Создаем задачу минимизации
prob_min = pulp.LpProblem("Minimization_Problem", pulp.LpMinimize)

# Переменные
y1 = pulp.LpVariable('y1', lowBound=0)
y2 = pulp.LpVariable('y2', lowBound=0)
y3 = pulp.LpVariable('y3', lowBound=0)

# Целевая функция
prob_min += 18*y1 + 16*y2 + 24*y3, "F*"

# Ограничения
prob_min += y1 + 3*y2 + 4*y3 >= 5
prob_min += y1 + 2*y2 + 3*y3 >= 7
prob_min += 5*y1 + y2 + y3 >= 8

# Решаем задачу
prob_min.solve()

# Результаты
print("Status:", pulp.LpStatus[prob_min.status])
print("y1 =", pulp.value(y1))
print("y2 =", pulp.value(y2))
print("y3 =", pulp.value(y3))
print("F* =", pulp.value(prob_min.objective))
