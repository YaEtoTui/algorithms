from itertools import product

# Данные производительности для каждого типа работ (I, II, III)
productivity = {
    'I': [5, 9, 12, 14, 15, 18, 20, 24, 27],
    'II': [7, 9, 11, 13, 16, 19, 21, 22, 25],
    'III': [6, 10, 13, 15, 16, 18, 21, 22, 25]
}

# Инициализация максимальной производительности и оптимального распределения
max_productivity = 0
optimal_distribution = None

# Перебираем все возможные комбинации (x1, x2, x3) такие, что x1 + x2 + x3 = 9 и x1, x2, x3 >= 1
for x1, x2, x3 in product(range(1, 10), repeat=3):  # x1, x2, x3 от 1 до 9 включительно
    if x1 + x2 + x3 == 9:  # проверка на выполнение ограничения
        # Считаем суммарную производительность для текущей комбинации
        total_productivity = productivity['I'][x1-1] + productivity['II'][x2-1] + productivity['III'][x3-1]
        # Обновляем максимальную производительность и распределение, если текущая комбинация лучше
        if total_productivity > max_productivity:
            max_productivity = total_productivity
            optimal_distribution = (x1, x2, x3)

# Результаты
print(f"Максимальная производительность: {max_productivity}")
print(f"Оптимальное распределение: Работы I = {optimal_distribution[0]}, Работы II = {optimal_distribution[1]}, Работы III = {optimal_distribution[2]}")