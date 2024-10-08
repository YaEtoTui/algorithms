# Данные задачи
c = [
    8.3, 7.3, 6.3, 9.6, 8.6, 7.6, 8.9, 7.9, 6.9, 8.6,
    7.6, 6.6, 10.5, 9.5, 8.5, 9.2, 8.2, 7.2, 7.5, 6.5,
    5.5, 9.0, 8.0, 7.0, 7.0, 6.0, 5.0, 6.0
]  # Удельные затраты
a = [
    None, None, None, 0.10, 0.10, 0.10, None, None, None, 0.25,
    0.25, 0.25, 0.10, 0.10, 0.10, 0.30, 0.30, 0.30, 0.30, 0.30,
    0.30, None, None, None, 0.10, 0.10, 0.10, 0.05
]  # Максимальные участия
b = [
    0.10, 0.10, 0.10, 0.02, 0.02, 0.02, 0.04, 0.04, 0.04, 0.10,
    0.10, 0.10, 0.05, 0.05, 0.05, 0.20, 0.20, 0.20, None, None,
    None, 0.05, 0.05, 0.05, None, None, None, None
]  # Минимальные участия

A = [
    10.43, 10.20, 10.68, 7.56, 7.40, 7.68, 12.57, 12.47, 13.17, 10.34,
    10.31, 10.41, 12.69, 13.02, 13.86, 9.22, 9.48, 9.79, 8.80, 8.87,
    9.48, 11.81, 11.83, 12.21, 9.15, 9.11, 9.77, 8.64
]  # Зольность

j = [j + 1 for j in range(28)]

Y = [
    14.0, 14.2, 14.4, 10.0, 10.2, 10.4, 14.0, 14.2, 14.4, 7.0,
    7.2, 7.4, 30.0, 30.3, 30.6, 28.0, 28.3, 28.6, 13.0, 13.2,
    13.4, 7.0, 7.2, 7.4, None, None, 6.0, None
]  # Толщина

K = "K"
K_2 = "K2"
J = "Ж"
G = "Г"
OC = "ОС"
CC = "СС"

brand = [
    K, K, K, K, K, K, K, K, K, K_2,
    K_2, K_2, J, J, J, J, J, J, G, G,
    G, OC, OC, OC, CC, CC, CC, OC
]  # Марка угля

Q = 100  # Общее количество капитальных вложений
P = 200  # Общая потребность в коксе