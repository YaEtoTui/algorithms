import pandas as pd
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.formula.translate import Translator

# Параметры
xi_0 = 10
d = [150, 50, 100, 100]

# Таблица 2
table_2 = pd.DataFrame({
    't': [0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 275, 300],
    'φ(t)': [0, 3, 8, 15, 30, 40, 49, 55, 58, 60, 62, 64, 65],
    'ψ(t)': [0, 22, 32, 35, 50, 70, 90, None, None, None, None, None, None]
})

# Таблица 3
table_3 = pd.DataFrame({
    'ξ1': [0, 1, 2, 3, 4, 5, 6],
    'Z1*(ξ1)': [62, 81, 90, 108, 130, 152, None],
    'x1*': [1, 2, 3, 4, 5, 6, None]
})

# Таблица 4
table_4 = pd.DataFrame({
    'ξ1': [0, 1, 2, 3, 4, 5, 6],
    'ξ2': [0, 1, 2, 3, 4, 5, None],
    'φ(ξ1)': [40, 49, 55, 58, 60, 62, 65],
    'ψ(ξ1+1)': [22, 32, 35, 50, 70, 90, None],
    'Z1*(ξ1)': [62, 81, 90, 108, 130, 152, 165]
})

# Таблица 5
table_5 = pd.DataFrame({
    'ξ2': [0, 1, 2, None, None, None],
    'ξ3': [0, 1, 2, 3, 4, 5],
    'φ(ξ2)': [8, 15, 30, 40, 49, 55],
    'ψ(ξ2)': [0, 22, 32, 35, 50, 70],
    'Z1*(ξ1)': [81, 90, 108, 130, 152, 165],
    'Z2*(ξ2, ξ3)': [89, 120, 142, 157, 174, 188]
})

# Таблица 6
table_6 = pd.DataFrame({
    'ξ3': [0, 1, 2, 3, 4, 5],
    'ξ4': [0, 1, 2, None, None, None],
    'φ(ξ3)': [30, 40, 49, 55, 60, 62],
    'ψ(ξ3)': [0, 22, 32, 35, 50, 70],
    'Z2*(ξ2, ξ3)': [142, 157, 174, 188, 212, 214],
    'Z3*(ξ3, ξ4)': [142, 164, 177, None, None, None]
})

# Таблица 7
table_7 = pd.DataFrame({
    'ξ4': [0, 1, 2],
    'φ(ξ4)': [30, 15, 8],
    'ψ(ξ4)': [0, 22, 32],
    'Z3*(ξ3)': [165, 135, 125],
    'Z4*(ξ4, ξ3)': [195, 172, 165]
})

# Вычисление Z4*(0)
Z4_0 = table_7.loc[table_7['ξ4'] == 0, 'Z4*(ξ4, ξ3)'].values[0]
print(f"Z4*(0) = {Z4_0}")

# Создание Excel файла
with pd.ExcelWriter('output.xlsx', engine='openpyxl') as writer:
    # Создаем один лист
    workbook = writer.book
    worksheet = workbook.create_sheet('All Tables')

    # Добавляем таблицы на лист
    for i, table in enumerate([table_2, table_3, table_4, table_5, table_6, table_7]):
        for r in dataframe_to_rows(table, index=False, header=True):
            worksheet.append(r)
        worksheet.append([])  # Пустая строка между таблицами
