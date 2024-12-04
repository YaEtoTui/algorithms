import sympy as sp

# Определяем переменные
x1, x2, x3, l1, l2 = sp.symbols('x1 x2 x3 l1 l2')

# Функция Лагранжа
L = x1 * x2 * x3 + l1 * (x1 + x2 + x3 - 5) + l2 * (x1 * x2 + x2 * x3 + x1 * x3 - 8)

# Частные производные
eq1 = sp.diff(L, x1)
eq2 = sp.diff(L, x2)
eq3 = sp.diff(L, x3)
eq4 = sp.diff(L, l1)
eq5 = sp.diff(L, l2)

# Система уравнений
equations = [eq1, eq2, eq3, eq4, eq5]

# Решаем систему уравнений
solutions = sp.solve(equations, (x1, x2, x3, l1, l2))

# Выводим решения
for sol in solutions:
    x1_val, x2_val, x3_val, l1_val, l2_val = sol
    f_val = x1_val * x2_val * x3_val
    print(f"x1 = {x1_val}, x2 = {x2_val}, x3 = {x3_val}, l1 = {l1_val}, l2 = {l2_val}, f = {f_val}")
