# Определение функций дохода для каждого предприятия
def f1(x):
    if x == 0: return 0
    if x == 40: return 8
    if x == 80: return 10
    if x == 120: return 11
    if x == 160: return 12
    if x == 200: return 18

def f2(x):
    if x == 0: return 0
    if x == 40: return 6
    if x == 80: return 9
    if x == 120: return 11
    if x == 160: return 13
    if x == 200: return 15

def f3(x):
    if x == 0: return 0
    if x == 40: return 3
    if x == 80: return 4
    if x == 120: return 7
    if x == 160: return 11
    if x == 200: return 18

def f4(x):
    if x == 0: return 0
    if x == 40: return 4
    if x == 80: return 6
    if x == 120: return 8
    if x == 160: return 13
    if x == 200: return 16

def f5(x):
    if x == 0: return 0
    if x == 40: return 7
    if x == 80: return 8
    if x == 120: return 11
    if x == 160: return 11
    if x == 200: return 11

def f6(x):
    if x == 0: return 0
    if x == 40: return 5
    if x == 80: return 9
    if x == 120: return 12
    if x == 160: return 13
    if x == 200: return 13

# Определение уравнения Беллмана
def bellman(f, E, x_values):
    Z = [0] * (E + 1)
    X = [0] * (E + 1)
    for e in range(E, -1, -40):
        max_z = 0
        max_x = 0
        for x in x_values:
            if e - x >= 0:
                z = f(x) + Z[e - x]
                if z > max_z:
                    max_z = z
                    max_x = x
        Z[e] = max_z
        X[e] = max_x
    return Z, X

# Основные параметры
E = 200
x_values = [0, 40, 80, 120, 160, 200]

# Расчет для каждого предприятия
Z1, X1 = bellman(f1, E, x_values)
Z2, X2 = bellman(f2, E, x_values)
Z3, X3 = bellman(f3, E, x_values)
Z4, X4 = bellman(f4, E, x_values)
Z5, X5 = bellman(f5, E, x_values)
Z6, X6 = bellman(f6, E, x_values)

# Определение оптимального распределения средств
x1 = X1[E]
x2 = X2[E - x1]
x3 = X3[E - x1 - x2]
x4 = X4[E - x1 - x2 - x3]
x5 = X5[E - x1 - x2 - x3 - x4]
x6 = X6[E - x1 - x2 - x3 - x4 - x5]

# Вывод результатов
print(f"Оптимальное распределение средств:")
print(f"Предприятие 1: {x1} млн. руб.")
print(f"Предприятие 2: {x2} млн. руб.")
print(f"Предприятие 3: {x3} млн. руб.")
print(f"Предприятие 4: {x4} млн. руб.")
print(f"Предприятие 5: {x5} млн. руб.")
print(f"Предприятие 6: {x6} млн. руб.")
print(f"Максимальный доход: {Z1[E]} млн. руб.")