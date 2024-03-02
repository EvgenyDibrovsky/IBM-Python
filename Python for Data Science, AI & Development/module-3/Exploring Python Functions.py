# Exploring Python Functions

# Introduction to functions
# Функция - это фундаментальный строительный блок, который инкапсулирует определенные действия или вычисления.

# Purpose of functions
# Функции способствуют модульности кода и его повторному использованию.

# Benefits of using functions
# Модульность, повторное использование, удобочитаемость, упрощение отладки, абстракция, совместная работа, облегчение обслуживания.

# How functions take inputs, perform tasks, and produce outputs
# Inputs (Parameters)
# Функции могут принимать данные в качестве входных данных. Эти входные данные называются параметрами или аргументами.

# Performing tasks
# После получения входных данных (параметров) функция выполняет заранее определенные действия или вычисления.

# Producing outputs
# После выполнения своих задач функция может производить вывод. Этот вывод является результатом операций, проведенных внутри функции.

# Example: Function to calculate the total
def calculate_total(a, b):  # Parameters: a and b
    total = a + b           # Task: Addition
    return total            # Output: Sum of a and b
result = calculate_total(5, 7)
print(result)  # Output: 12

# Python's built-in functions
# Python имеет богатый набор встроенных функций, которые предлагают широкий спектр функциональности.

# Using built-in functions like len(), sum(), max(), min()
string_length = len("Hello, World!")  # Output: 13
list_length = len([1, 2, 3, 4, 5])    # Output: 5
total = sum([10, 20, 30, 40, 50])     # Output: 150
highest = max([5, 12, 8, 23, 16])     # Output: 23
lowest = min([5, 12, 8, 23, 16])      # Output: 5

# Defining your functions
# Создание функции начинается с def, за которым следует имя функции и скобки.

# Syntax to define a function
def function_name():
    pass

# Function Parameters
# Параметры функций подобны входным данным для функций. Они находятся в скобках при определении функции.

# Example: Function with parameters
def greet(name):
    print("Hello, " + name)
greet("Alice")

# Docstrings (Documentation Strings)
# Docstrings объясняют, что делает функция, и помещаются внутри тройных кавычек под определением функции.

# Example: Function with docstring
def multiply(a, b):
    """
    This function multiplies two numbers.
    Input: a (number), b (number)
    Output: Product of a and b
    """
    print(a * b)
multiply(2,6)

# Return statement
# Return возвращает значение из функции.

# Example: Function with return statement
def add(a, b):
    return a + b
sum_result = add(3, 5)

# Understanding scopes and variables
# Область видимости определяет, где переменная может быть видна и использована.

# Global Scope vs Local Scope
global_variable = "I'm global"
def example_function():
    local_variable = "I'm local"
    print(global_variable)
    print(local_variable)
example_function()
print(global_variable)
# print(local_variable)  # Error

# Using functions with loops
# Функции могут содержать код с циклами, что делает сложные задачи более организованными.

# Example: Function with a loop
def print_numbers(limit):
    for i in range(1, limit+1):
        print(i)
print_numbers(5)

# Modifying data structure using functions
# Использование функций для модификации структур данных.

# Example: Functions to modify a list
my_list = []
def add_element(data_structure, element):
    data_structure.append(element)
def remove_element(data_structure, element):
    if element in data_structure:
        data_structure.remove(element)
    else:
        print(f"{element} not found in the list.")
add_element(my_list, 42)
add_element(my_list, 17)
add_element(my_list, 99)
print("Current list:", my_list)
remove_element(my_list, 17)
remove_element(my_list, 55)
print("Updated list:", my_list)
