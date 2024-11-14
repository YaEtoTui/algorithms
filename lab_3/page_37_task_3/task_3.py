import numpy as np


def f1(x):
    x_values = [0, 50, 100, 150, 200, 250, 300, 350, 400]
    f1_values = [0, 6, 10, 15, 26, 28, 38, 45, 49]

    for i in range(len(x_values) - 1):
        if x_values[i] <= x <= x_values[i + 1]:
            x1, x2 = x_values[i], x_values[i + 1]
            y1, y2 = f1_values[i], f1_values[i + 1]
            return y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    return 0


def f2(x):
    x_values = [0, 50, 100, 150, 200, 250, 300, 350, 400]
    f2_values = [0, 8, 12, 20, 28, 35, 40, 46, 48]

    for i in range(len(x_values) - 1):
        if x_values[i] <= x <= x_values[i + 1]:
            x1, x2 = x_values[i], x_values[i + 1]
            y1, y2 = f2_values[i], f2_values[i + 1]
            return y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    return 0


def solve_stage(available_funds, next_stage_values=None, step=50):
    best_value = float('-inf')
    best_x = 0
    best_y = 0

    for x in range(0, int(available_funds) + step, step):
        for y in range(0, int(available_funds) + step - x, step):
            if x + y <= available_funds:
                current_value = f1(x) + f2(y)

                if next_stage_values is not None:
                    next_funds = int(round(0.6 * x + 0.2 * y) / step) * step
                    next_funds_index = int(next_funds / step)
                    if next_funds_index < len(next_stage_values):
                        current_value += next_stage_values[next_funds_index]

                if current_value > best_value:
                    best_value = current_value
                    best_x = x
                    best_y = y

    return best_x, best_y, best_value


def solve_dynamic_programming():
    max_funds = 400
    step = 50
    n_states = int(max_funds / step) + 1

    # Массивы для хранения значений для каждого этапа
    V3 = np.zeros(n_states)  # значения для 3-го года
    V2 = np.zeros(n_states)  # значения для 2-го года
    V1 = np.zeros(n_states)  # значения для 1-го года

    # Решение для 3-го года
    solutions3 = {}
    for i in range(n_states):
        funds = i * step
        x, y, value = solve_stage(funds)
        V3[i] = value
        solutions3[funds] = (x, y)

    # Решение для 2-го года
    solutions2 = {}
    for i in range(n_states):
        funds = i * step
        x, y, value = solve_stage(funds, V3, step)
        V2[i] = value
        solutions2[funds] = (x, y)

    # Решение для 1-го года
    x1, y1, value1 = solve_stage(max_funds, V2, step)

    # Восстановление пути решения
    path = []
    # Первый год
    path.append((1, x1, y1))
    funds2 = int(round((0.6 * x1 + 0.2 * y1) / step) * step)

    # Второй год
    x2, y2 = solutions2[funds2]
    path.append((2, x2, y2))
    funds3 = int(round((0.6 * x2 + 0.2 * y2) / step) * step)

    # Третий год
    x3, y3 = solutions3[funds3]
    path.append((3, x3, y3))

    return path


# Запуск решения
solution = solve_dynamic_programming()

# Вывод результатов
for year, x, y in solution:
    print(f"\nГод {year}:")
    print(f"Предприятие 1: {x}")
    print(f"Предприятие 2: {y}")
    print(f"Прибыль: {f1(x) + f2(y)}")
    if year < 3:
        next_funds = int(round((0.6 * x + 0.2 * y) / 50) * 50)
        print(f"Средства на следующий год: {next_funds}")
