# Module 1 Cheat Sheet: Python Basics

# Comments
# Описание: Комментарии - это строки текста, которые Python интерпретатор игнорирует при выполнении кода.
# Пример: 
# This is a comment

# Concatenation
# Описание: Объединяет строки.
# Синтаксис: 
concatenated_string = string1 + string2
# Пример: 
result = "Hello" + " John"

# Data Types
# Описание: - Integer - Float - Boolean - String
# Примеры:
x = 7  # Integer Value 
y = 12.4  # Float Value 
is_valid = True  # Boolean Value 
is_valid = False  # Boolean Value 
F_Name = "John"  # String Value

# Indexing
# Описание: Доступ к символу по определённому индексу.
# Пример: 
my_string = "Hello"
char = my_string[0]

# len()
# Описание: Возвращает длину строки.
# Синтаксис: 
len(string_name)
# Пример:
my_string = "Hello"
length = len(my_string)

# lower()
# Описание: Преобразует строку в нижний регистр.
# Пример:
my_string = "Hello"
lowercase_text = my_string.lower()

# print()
# Описание: Выводит сообщение или переменную в `()`.
# Примеры:
print("Hello, world")
print(a + b)

# Python Operators
# Описание: - Addition (+): Складывает два значения.
#            - Subtraction (-): Вычитает одно значение из другого.
#            - Multiplication (*): Умножает два значения.
#            - Division (/): Делит одно значение на другое, возвращает float.
#            - Floor Division (//): Делит одно значение на другое, возвращает целое число.
#            - Modulo (%): Возвращает остаток от деления.
# Примеры:
x = 9
y = 4
result_add = x + y  # Addition
result_sub = x - y  # Subtraction
result_mul = x * y  # Multiplication
result_div = x / y  # Division
result_fdiv = x // y  # Floor Division
result_mod = x % y  # Modulo

# replace()
# Описание: Заменяет подстроки.
# Пример:
my_string = "Hello"
new_text = my_string.replace("Hello", "Hi")

# Slicing
# Описание: Извлекает часть строки.
# Синтаксис: 
substring = string_name[start:end]
# Пример: 
substring = my_string[0:5]

# split()
# Описание: Разделяет строку на список на основе разделителя.
# Пример:
my_string = "Hello, world"
split_text = my_string.split(",")

# strip()
# Описание: Удаляет пробелы в начале и в конце строки.
# Пример:
my_string = " Hello "
trimmed = my_string.strip()

# upper()
# Описание: Преобразует строку в верхний регистр.
# Пример:
my_string = "Hello"
uppercase_text = my_string.upper()

# Variable Assignment
# Описание: Назначает значение переменной.
# Синтаксис: 
variable_name = value
# Примеры:
name = "John"  # assigning John to variable name
x = 5  # assigning 5 to variable x
