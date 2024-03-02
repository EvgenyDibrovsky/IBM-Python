# Working with Data in Python Cheat Sheet

# Чтение и запись файлов
# File opening modes - Режимы открытия файлов
with open("data.txt", "r") as file:  # Чтение
    content = file.read()
    print(content)

with open("output.txt", "w") as file:  # Запись
    file.write("Hello, world!")

with open("log.txt", "a") as file:  # Дописывание
    file.write("Log entry: Something happened.")

with open("data.txt", "r+") as file:  # Обновление
    content = file.read()
    file.write("Updated content: " + content)

# File reading methods - Методы чтения файлов
with open("data.txt", "r") as file:
    lines = file.readlines()  # Чтение всех строк как списка
    next_line = file.readline()  # Чтение следующей строки как строки
    content = file.read()  # Чтение всего содержимого файла как строки

# File writing methods - Методы записи файлов
lines = ["Hello\n", "World\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)  # Запись списка строк в файл

# Iterating over lines - Итерация по строкам файла
with open("data.txt", "r") as file:
    for line in file:
        print(line)

# Open() and close() - Открытие и закрытие файла
file = open("data.txt", "r")
content = file.read()
file.close()

# with open() - Открытие файла с использованием блока with
with open("data.txt", "r") as file:
    content = file.read()

# Pandas
import pandas as pd

# .read_csv() - Чтение данных из файла CSV
df = pd.read_csv("data.csv")

# .read_excel() - Чтение данных из файла Excel
df = pd.read_excel("data.xlsx")

# .to_csv() - Запись DataFrame в файл CSV
df.to_csv("output.csv", index=False)

# Access Columns - Доступ к столбцам DataFrame
df["age"]  # Доступ к одному столбцу
df[["name", "age"]]  # Доступ к нескольким столбцам

# describe() - Статистическое описание числовых столбцов DataFrame
df.describe()

# drop() - Удаление строк или столбцов из DataFrame
df.drop(["age", "salary"], axis=1, inplace=True)  # Удаление столбцов
df.drop(index=[5, 10], axis=0, inplace=True)  # Удаление строк

# dropna() - Удаление строк с отсутствующими значениями
df.dropna(axis=0, inplace=True)

# duplicated() - Поиск дубликатов в DataFrame
duplicate_rows = df[df.duplicated()]

# Filter Rows - Фильтрация строк DataFrame
filtered_df = df[(df["age"] > 30) & (df["salary"] < 50000)]

# groupby() - Группировка данных в DataFrame
grouped = df.groupby(["category", "region"]).agg({"sales": "sum"})

# head() - Показ первых n строк DataFrame
df.head(5)

# info() - Информация о DataFrame
df.info()

# merge() - Слияние двух DataFrame
merged_df = pd.merge(sales, products, on=["product_id", "category_id"])

# print DataFrame - Вывод содержимого DataFrame
print(df)

# replace() - Замена значений в столбце DataFrame
df["status"].replace("In Progress", "Active", inplace=True)

# tail() - Показ последних n строк DataFrame
df.tail(5)

# Numpy
import numpy as np

# Importing NumPy - Импорт библиотеки NumPy
import numpy as np

# np.array() - Создание одно- или многомерного массива
array_1d = np.array([1, 2, 3])  # Одномерный массив
array_2d = np.array([[1, 2], [3, 4]])  # Двумерный массив

# Numpy Array Attributes - Операции с массивами NumPy
np.mean(array)  # Среднее значение элементов массива
np.sum(array)  # Сумма элементов массива
np.min(array)  # Минимальное значение в массиве
np.max(array)  # Максимальное значение в массиве
np.dot(array_1, array_2)  # Скалярное произведение двух массивов
