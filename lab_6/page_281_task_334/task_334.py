import numpy as np
from scipy.optimize import minimize
import pandas as pd

# Целевая функция
def objective(x):
    return -x[0]**2 - x[1]**2

# Градиент целевой функции
def gradient(x):
    return np.array([-2*x[0], -2*x[1]])

# Ограничения
constraints = (
    {'type': 'ineq', 'fun': lambda x: x[0] + 0.5*x[1] - 1},
    {'type': 'ineq', 'fun': lambda x: 4 - x[0] - 0.5*x[1]},
    {'type': 'ineq', 'fun': lambda x: 6 - x[0] - x[1]},
    {'type': 'ineq', 'fun': lambda x: x[0]},
    {'type': 'ineq', 'fun': lambda x: x[1]}
)

# Начальная точка
x0 = np.array([1, 1])

# Решение задачи
result = minimize(objective, x0, method='SLSQP', jac=gradient, constraints=constraints)

# Вывод результата
print("Решение:", result.x)
print("Значение функции в точке решения:", -objective(result.x))

# Сохранение результата в Excel
df = pd.DataFrame({
    'x1': [result.x[0]],
    'x2': [result.x[1]],
    'f(x)': [-objective(result.x)]
})
df.to_excel('solution.xlsx', index=False)
