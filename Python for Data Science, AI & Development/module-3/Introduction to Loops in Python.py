# Introduction to Loops in Python

# What is a Loop?
# В программировании цикл позволяет компьютеру повторять действие многократно.

# How Loop works
# Циклы в Python работают следующим образом:

# For loop
# Цикл for начинается с ключевого слова for, за которым следует переменная, которая будет принимать каждое значение в последовательности.

for val in sequence:
    # statement(s) to be executed in sequence as a part of the loop.

# Например, цикл for для списка цветов:

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
for color in colors:
    print(color)

# Или цикл for для диапазона чисел:

for number in range(1, 11):
    print(number)

# Range Function
# Функция range в Python генерирует упорядоченную последовательность, которая может использоваться в циклах.

for number in range(11):
    print(number)

# The Enumerated For Loop
# Enumerate позволяет отслеживать и элемент, и его позицию в списке.

fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"At position {index}, I found a {fruit}")

# While Loops
# Цикл while повторяет задачу до тех пор, пока определенное условие остается истинным.

# Синтаксис цикла while:
while condition:
    # Code to be executed while the condition is true

# Например, цикл while для подсчета от 1 до 10:

count = 1
while count <= 10:
    print(count)
    count += 1

# The Loop Flow
# Циклы как for, так и while следуют определенной схеме:
# 1. Инициализация
# 2. Условие
# 3. Исполнение
# 4. Обновление
# 5. Повторение

# When to Use Each
# For Loops: Используйте, когда известно количество итераций заранее.
# While Loops: Используйте, когда необходимо выполнить задачу повторно, пока определенное условие остается истинным.

# Summary
# Мы исследовали циклы в Python - специальные инструменты, которые помогают нам делать что-то снова и снова, не уставая. Мы рассмотрели два типа циклов: "for loops" и "while loops".
