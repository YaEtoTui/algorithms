def calculate_F(t):
    x1, x2, x3, x4, x5 = 0, 0, 0, 9 - 12 * t, 6 + 9 * t
    if x4 < 0 or x5 < 0:
        return float('-inf')

    max_val = max(4 + 6 * t, 9 - 12 * t, 6 + 9 * t)
    F = (2 + t) * (x1 + x2 + x3) + (3 - t) * x2 + 3 * (2 + 4 * t) * x5 + max_val
    return F

def find_optimal_t():
    t_min = -2 / 3
    t_max = 3 / 4
    best_t = t_min
    best_F = calculate_F(t_min)

    step = 0.001  # Шаг для поиска
    t = t_min
    while t <= t_max:
        current_F = calculate_F(t)
        if current_F > best_F:
            best_F = current_F
            best_t = t
        t += step

    return best_t, best_F

optimal_t, optimal_F = find_optimal_t()
print(f"Оптимальное значение t: {optimal_t}")
print(f"Максимальное значение F: {optimal_F}")
