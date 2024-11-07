# Данные доходов для каждого предприятия
income_table = [
    [8, 10, 11, 12, 18],  # f1(x) - доход для первого предприятия
    [6, 9, 11, 13, 15],   # f2(x) - доход для второго предприятия
    [3, 4, 7, 11, 18],    # f3(x) - доход для третьего предприятия
    [4, 6, 8, 13, 16]     # f4(x) - доход для четвертого предприятия
]

# Параметры задачи
total_budget = 200  # Максимальный бюджет
increment = 40  # Кратность финансирования
num_enterprises = len(income_table)  # Количество предприятий
funding_levels = len(income_table[0])  # Количество уровней финансирования для каждого предприятия

# Функция для вычисления оптимального распределения бюджета
def optimal_distribution(budget):
    dp = [[0] * (budget // increment + 1) for _ in range(num_enterprises + 1)]
    allocation = [[0] * (budget // increment + 1) for _ in range(num_enterprises + 1)]

    for i in range(1, num_enterprises + 1):
        for j in range(1, budget // increment + 1):
            current_budget = j * increment
            dp[i][j] = dp[i-1][j]
            for k in range(funding_levels):
                cost = (k + 1) * increment
                if cost <= current_budget:
                    potential_income = income_table[i-1][k] + dp[i-1][j - (cost // increment)]
                    if potential_income > dp[i][j]:
                        dp[i][j] = potential_income
                        allocation[i][j] = cost

    distribution = [0] * num_enterprises
    remaining_budget = budget // increment
    for i in range(num_enterprises, 0, -1):
        distribution[i-1] = allocation[i][remaining_budget]
        remaining_budget -= distribution[i-1] // increment

    return dp[num_enterprises][budget // increment], distribution

# Функция для расчета оптимального распределения при изменении бюджета
def solve_with_delta(delta_epsilon):
    adjusted_budget = total_budget + delta_epsilon
    max_income, distribution = optimal_distribution(adjusted_budget)
    distribution = [f"{amount} млн руб." for amount in distribution]
    return max_income, distribution

# Результаты для разных значений delta_epsilon
delta_values = [-80, 40, 80]
for delta in delta_values:
    max_income, distribution = solve_with_delta(delta)
    print(f"При delta_epsilon = {delta}:")
    print(f"Максимальный доход: {max_income}")
    print(f"Распределение бюджета: {distribution}\n")

