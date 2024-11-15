# Определяем функции выпуска для отрасли I и II
def production_I(S, x_I):
    return S + 0.1 * x_I  # Пример функции для отрасли I

def production_II(S, x_II):
    return 0.2 * S * x_II  # Пример функции для отрасли II

# Функция динамического программирования
def maximize_consumption(N, S, ξ):
    dp = {}

    def F(t, S, ξ):
        if t == N:
            return 0  # В последний год не производим
        if (t, S, ξ) in dp:
            return dp[(t, S, ξ)]

        max_consumption = 0
        for x_I in range(0, ξ + 1):
            x_II = ξ - x_I
            new_S = production_I(S, x_I)
            consumption = production_II(S, x_II)
            max_consumption = max(max_consumption, consumption + F(t + 1, new_S, ξ))

        dp[(t, S, ξ)] = max_consumption
        return max_consumption

    return F(0, S, ξ)

# Пример вызова функции
N = 5  # планирование на 5 лет
S_0 = 10  # начальное количество машин
ξ_0 = 100  # начальный бюджет
print(maximize_consumption(N, S_0, ξ_0))