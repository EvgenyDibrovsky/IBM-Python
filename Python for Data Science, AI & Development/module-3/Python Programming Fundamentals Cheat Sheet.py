# Шпаргалка по основам программирования на Python

# AND
# Возвращает `True`, если и statement1, и statement2 истинны.
statement1 and statement2
# Пример:
marks = 90
attendance_percentage = 87
if marks >= 80 and attendance_percentage >= 85:
    print("qualify for honors")
else:
    print("Not qualified for honors")

# Определение класса
# Определяет шаблон для создания объектов.
class ClassName:  # Атрибуты и методы класса
# Пример:
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age

# Определение функции
# Блок кода, выполняющий определенную задачу.
def function_name(parameters):  # Тело функции
# Пример:
def greet(name): 
    print("Hello,", name)

# Equal(==)
# Проверяет равенство двух значений.
variable1 == variable2
# Примеры:
5 == 5  # Возвращает True
age = 25 
age == 30  # Возвращает False

# Цикл For
# Повторно выполняет блок кода определенное количество раз.
for variable in sequence:  # Код для повторения
# Примеры:
for num in range(1, 10): 
    print(num)
fruits = ["apple", "banana", "orange", "grape", "kiwi"] 
for fruit in fruits:
    print(fruit)

# Вызов функции
# Выполняет код внутри функции с предоставленными аргументами.
function_name(arguments)
# Пример:
greet("Alice")

# Больше или равно (>=)
# Проверяет, что значение переменной больше или равно другой переменной.
variable1 >= variable2
# Примеры:
5 >= 5 and 9 >= 5  # Возвращает True
quantity = 105 
minimum = 100 
quantity >= minimum  # Возвращает True

# Больше (>)
# Проверяет, что значение переменной больше другой переменной.
variable1 > variable2
# Примеры:
9 > 6  # Возвращает True
age = 20 
max_age = 25 
age > max_age  # Возвращает False

# Условие If
# Выполняет блок кода, если условие истинно.
if condition:  # Блок кода для if
# Пример:
if temperature > 30: 
    print("It's a hot day!")

# Условие If-Elif-Else
# Выполняет первый блок кода, если condition1 истинно, в противном случае проверяет condition2 и так далее.
if condition1:
    # Код, если condition1 истинно
elif condition2:
    # Код, если condition2 истинно
else:
    # Код, если ни одно условие не истинно
# Пример:
score = 85
if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B.")
else:
    print("You need to work harder.")

# Условие If-Else
# Выполняет первый блок кода, если условие истинно, в противном случае второй блок.
if condition:  # Код, если условие истинно
else:  # Код, если условие ложно
# Пример:
if age >= 18:
    print("You're an adult.")
else:
    print("You're not an adult yet.")

# Меньше или равно (<=)
# Проверяет, что значение переменной меньше или равно другой переменной.
variable1 <= variable2
# Примеры:
5 <= 5 and 3 <= 5  # Возвращает True
size = 38 
max_size = 40 
size <= max_size  # Возвращает True

# Меньше (<)
# Проверяет, что значение переменной меньше другой переменной.
variable1 < variable2
# Примеры:
4 < 6  # Возвращает True
score = 60 
passing_score = 65 
score < passing_score  # Возвращает True

# Управление циклами
# `break` немедленно завершает цикл. `continue` пропускает остаток текущей итерации и переходит к следующей.
for:  # Код для повторения
    if condition:
        break 
for:  # Код для повторения
    if condition:
        continue
# Примеры:
for num in range(1, 6):
    if num == 3:
        break
    print(num)
for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# NOT
# Возвращает `True`, если переменная ложна, и наоборот.
!variable
# Пример:
!isLocked  # Возвращает True, если переменная ложна (т.е. разблокирована).

# Не равно (!=)
# Проверяет, что два значения не равны.
variable1 != variable2
# Примеры:
a = 10 
b = 20 
a != b  # Возвращает True
count=0 
count != 0  # Возвращает False

# Создание объекта
# Создает экземпляр класса (объект) с помощью конструктора класса.
object_name = ClassName(arguments)
# Пример:
person1 = Person("Alice", 25)

# OR
# Возвращает `True`, если хотя бы одно из условий истинно.
statement1 || statement2
# Пример:
Grade = 12 
grade == 11 or grade == 12  # Возвращает True

# Функция range()
# Генерирует последовательность чисел в заданном диапазоне.
range(stop) 
range(start, stop) 
range(start, stop, step)
# Примеры:
range(5)  # Генерирует последовательность от 0 до 4.
range(2, 10)  # Генерирует последовательность от 2 до 9.
range(1, 11, 2)  # Генерирует нечетные числа от 1 до 9.

# Оператор Return
# Возвращает значение из функции.
return value
# Пример:
def add(a, b): 
    return a + b 
result = add(3, 5)

# Блок Try-Except
# Пытается выполнить код в блоке try. Если происходит исключение указанного типа, выполняется код в блоке except.
try: 
    # Код, который может вызвать исключение
except ExceptionType: 
    # Код для обработки исключения
# Пример:
try: 
    num = int(input("Enter a number: ")) 
except ValueError: 
    print("Invalid input. Please enter a valid number.")

# Try-Except с Else
# Код в блоке `else` выполняется, если в блоке try не произошло исключений.
try: 
    # Код, который может вызвать исключение
except ExceptionType: 
    # Код для обработки исключения
else: 
    # Код, который выполняется, если исключений нет
# Пример:
try: 
    num = int(input("Enter a number: ")) 
except ValueError: 
    print("Invalid input. Please enter a valid number") 
else: 
    print("You entered:", num)

# Try-Except с Finally
# Код в блоке `finally` всегда выполняется, независимо от того, произошло исключение или нет.
try: 
    # Код, который может вызвать исключение
except ExceptionType: 
    # Код для обработки исключения
finally: 
    # Код, который всегда выполняется
# Пример:
try: 
    file = open("data.txt", "r") 
    data = file.read() 
except FileNotFoundError: 
    print("File not found.") 
finally: 
    file.close()

# Цикл While
# Повторно выполняет блок кода, пока условие остается истинным.
while condition:  # Код для повторения
# Пример:
count = 0 
while count < 5: 
    print(count) 
    count += 1
