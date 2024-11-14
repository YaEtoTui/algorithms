# Функция для вычисления производительности в зависимости от количества механизмов
def productivity(v_type, count):
    if v_type == 1:
        if count == 1:
            return 5
        elif count == 2:
            return 9
        elif count == 3:
            return 12
        elif count == 4:
            return 14
        elif count == 5:
            return 15
        elif count == 6:
            return 18
        elif count == 7:
            return 20
        elif count == 8:
            return 24
        elif count == 9:
            return 27
        elif count == 10:
            return 30
        elif count == 11:
            return 34
        elif count == 12:
            return 38
    elif v_type == 2:
        if count == 1:
            return 7
        elif count == 2:
            return 9
        elif count == 3:
            return 11
        elif count == 4:
            return 13
        elif count == 5:
            return 16
        elif count == 6:
            return 19
        elif count == 7:
            return 21
        elif count == 8:
            return 22
        elif count == 9:
            return 25
        elif count == 10:
            return 28
        elif count == 11:
            return 35
        elif count == 12:
            return 40
    elif v_type == 3:
        if count == 1:
            return 6
        elif count == 2:
            return 10
        elif count == 3:
            return 13
        elif count == 4:
            return 15
        elif count == 5:
            return 16
        elif count == 6:
            return 18
        elif count == 7:
            return 21
        elif count == 8:
            return 22
        elif count == 9:
            return 25
        elif count == 10:
            return 26
        elif count == 11:
            return 29
        elif count == 12:
            return 33
    return 0


# Основная функция для поиска оптимального распределения
def optimal_distribution(total_mechanisms):
    max_productivity = 0
    best_distribution = (0, 0, 0)

    # Перебор всех возможных распределений механизмов
    for x1 in range(total_mechanisms + 1):
        for x2 in range(total_mechanisms - x1 + 1):
            x3 = total_mechanisms - x1 - x2

            # Проверяем только валидные распределения (x3 не может быть отрицательным)
            if x3 < 0:
                continue

            # Вычисляем общую производительность для текущего распределения
            total_productivity = productivity(1, x1) + productivity(2, x2) + productivity(3, x3)

            # Если текущая производительность больше максимальной, обновляем значения
            if total_productivity > max_productivity:
                max_productivity = total_productivity
                best_distribution = (x1, x2, x3)

    return best_distribution, max_productivity


# Задаем общее количество механизмов
total_mechanisms = 12

# Находим оптимальное распределение
distribution, max_prod = optimal_distribution(total_mechanisms)

# Выводим результаты
print(
    f"Оптимальное распределение механизмов: Вид 1: {distribution[0]}, Вид 2: {distribution[1]}, Вид 3: {distribution[2]}")
print(f"Максимальная производительность: {max_prod} тыс. м³")