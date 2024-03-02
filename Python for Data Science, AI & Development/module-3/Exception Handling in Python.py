# Exception Handling in Python

# Understanding Exceptions
# Исключения - это сигналы о том, что произошло что-то неожиданное во время выполнения программы.

# Errors vs. Exceptions
# Ошибки обычно связаны с проблемами системы, в то время как исключения связаны с ошибками в коде и могут быть обработаны.

# Common Exceptions in Python
# ZeroDivisionError: Попытка деления на ноль.
# ValueError: Использование неподходящего значения.
# FileNotFoundError: Попытка доступа к несуществующему файлу.
# IndexError: Обращение за пределы допустимого индекса в списке.
# KeyError: Обращение к несуществующему ключу в словаре.
# TypeError: Использование объекта несовместимым образом.
# AttributeError: Обращение к несуществующему атрибуту или методу объекта.
# ImportError: Попытка импортировать отсутствующий модуль.

# Handling Exceptions
# Python предоставляет механизм try-except для обработки исключений.

# Example: ZeroDivisionError handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
print("outside of try and except block")

# Example: ValueError handling
try:
    num = int("abc")
except ValueError:
    print("Error: Invalid conversion to integer")

# Example: FileNotFoundError handling
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found")

# Example: IndexError handling
try:
    my_list = [1, 2, 3]
    missing = my_list[5]
except IndexError:
    print("Error: Index out of range")

# Example: KeyError handling
try:
    my_dict = {"name": "Alice", "age": 30}
    missing = my_dict["city"]
except KeyError:
    print("Error: Key not found in the dictionary")

# Example: TypeError handling
try:
    result = "hello" + 5
except TypeError:
    print("Error: Incompatible types for concatenation")

# Example: AttributeError handling
try:
    text = "example"
    missing = text.some_method()
except AttributeError:
    print("Error: Method or attribute not found")

# Example: ImportError handling
try:
    import non_existent_module
except ImportError:
    print("Error: Module not found")

# Tips for Effective Exception Handling
# 1. Only use try-except blocks around code that is likely to raise an exception.
# 2. Be as specific as possible in exception types to avoid masking other issues.
# 3. Use meaningful error messages to make the cause of the exception clear.
