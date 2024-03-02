# Introduction to Pandas for Data Analysis

# Что такое Pandas?
# Pandas - это популярная библиотека Python для манипуляции и анализа данных.

# Особенности и функционал Pandas:
# - Структуры данных: DataFrame и Series.
# - Импорт и экспорт данных: Чтение и запись данных из различных источников.
# - Слияние и присоединение данных: Объединение DataFrames с помощью merge и join.
# - Эффективная индексация: Быстрый доступ к данным.
# - Создание пользовательских структур данных.

# Импорт Pandas
import pandas as pd

# Загрузка данных
df = pd.read_csv('your_file.csv')

# Что такое Series?
# Series - одномерный массив с метками, который можно рассматривать как один столбец данных.

# Создание Series
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)

# Доступ к элементам в Series
print(s[2])           # Доступ по метке
print(s.iloc[3])      # Доступ по позиции
print(s[1:4])         # Доступ к диапазону элементов

# Атрибуты и методы Series
# values, index, shape, size, mean(), sum(), min(), max(), unique(), nunique(), sort_values(), sort_index(), isnull(), notnull(), apply()

# Что такое DataFrames?
# DataFrame - двумерная структура данных с столбцами, которые могут иметь разные типы данных.

# Создание DataFrame из словарей
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)

# Выбор столбцов
print(df['Name'])  # Доступ к столбцу 'Name'

# Доступ к строкам
print(df.iloc[2])   # Доступ к строке по позиции
print(df.loc[1])    # Доступ к строке по метке

# Срезы
print(df[['Name', 'Age']])  # Выбор конкретных столбцов
print(df[1:3])              # Выбор конкретных строк

# Уникальные элементы
unique_ages = df['Age'].unique()

# Фильтрация по условиям
high_age = df[df['Age'] > 25]

# Сохранение DataFrame
df.to_csv('trading_data.csv', index=False)

# Атрибуты и методы DataFrame
# shape, info(), describe(), head(), tail(), mean(), sum(), min(), max(), sort_values(), groupby(), fillna(), drop(), rename(), apply()

# Для более подробной информации обратитесь к официальной документации Pandas.
