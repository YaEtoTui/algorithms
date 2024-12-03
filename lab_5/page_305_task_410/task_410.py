import openpyxl
from openpyxl.styles import Font, Alignment

# Исходные данные
S = 700  # Объем капиталовложений
n = 3    # Количество предприятий

# Прирост выпуска продукции f_i(X_i) в зависимости от объема капиталовложений (тыс. руб.)
f = [
    [0, 30, 50, 80, 110, 150, 170, 190, 210],  # Предприятие 1
    [0, 40, 50, 90, 120, 180, 220, 240],       # Предприятие 2
    [0, 30, 50, 90, 120, 180, 220, 240]        # Предприятие 3
]

# Объем капиталовложений X_i
X = [0, 100, 200, 300, 400, 500, 600, 700]

# Функция для нахождения максимального прироста выпуска продукции
def max_increase(S, n, f, X):
    # Таблица для хранения максимальных значений прироста выпуска продукции
    dp = [[0] * (S + 1) for _ in range(n + 1)]
    choices = [[(0, 0)] * (S + 1) for _ in range(n + 1)]  # Таблица для хранения выборов

    # Заполняем таблицу
    for i in range(1, n + 1):
        for j in range(1, S + 1):
            max_increase = 0
            choice = (0, 0)
            for x in X:
                if x <= j:
                    value = f[i-1][X.index(x)] + dp[i-1][j-x]
                    if value > max_increase:
                        max_increase = value
                        choice = (i, x)
            dp[i][j] = max_increase
            choices[i][j] = choice

    return dp, choices

# Вычисляем максимальный прирост выпуска продукции
dp, choices = max_increase(S, n, f, X)

# Выводим результаты
max_increase_value = dp[n][S]
print(f"Максимальный прирост выпуска продукции: {max_increase_value} тыс. руб.")

# Отслеживаем, какие значения использовались для заполнения таблицы dp
used_values = []
i, j = n, S
while i > 0 and j > 0:
    predp, x = choices[i][j]
    if predp != 0 and x != 0:
        used_values.append((predp, x))
        j -= x
        i -= 1

print("Использованные значения:")
for predp, x in reversed(used_values):
    print(f"Предприятие {predp}, Объем капиталовложений X={x}")

# Создаем новый Excel файл и лист
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Отчет"

# Записываем исходные данные
ws.append(["Объем капиталовложений (S)", S])
ws.append(["Количество предприятий (n)", n])
ws.append([])  # Пустая строка для разделения

# Записываем таблицу прироста выпуска продукции
ws.append(["Предприятие"] + [f"X={x}" for x in X])
for i, row in enumerate(f, start=1):
    ws.append([f"Предприятие {i}"] + row)

ws.append([])  # Пустая строка для разделения

# Записываем таблицу dp
ws.append(["dp"] + [i for i in range(S + 1)])
for i, row in enumerate(dp):
    ws.append([f"Предприятие {i}"] + row)

ws.append([])  # Пустая строка для разделения

# Записываем максимальный прирост выпуска продукции
ws.append(["Максимальный прирост выпуска продукции", max_increase_value])

# Записываем формулы
ws.append([])  # Пустая строка для разделения
ws.append(["Формулы для подсчета:"])
ws.append(["1. Создаем таблицу dp размером (n+1) x (S+1), где n - количество предприятий, S - объем капиталовложений."])
ws.append(["2. Заполняем таблицу dp следующим образом:"])
ws.append(["   dp[i][j] = max(f_i(X) + dp[i-1][j-X]) для всех X <= j"])
ws.append(["3. Максимальный прирост выпуска продукции находится в ячейке dp[n][S]."])

# Сохраняем Excel файл
wb.save("report.xlsx")

print("Отчет сохранен в файл report.xlsx")
