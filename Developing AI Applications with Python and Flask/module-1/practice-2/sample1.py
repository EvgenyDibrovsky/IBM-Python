"""
Этот модуль содержит функции для выполнения математических операций.

Функции:
    add(number1, number2) - возвращает сумму двух чисел.
"""

def add(number1, number2):
    """
    Calculate the sum of two numbers.

    Args:
        number1 (float): The first number to add.
        number2 (float): The second number to add.

    Returns:
        float: The sum of number1 and number2.
    """
    return number1 + number2

# Константы именуются заглавными буквами
NUM1 = 5
NUM2 = 5

# Результат функции присваивается переменной, имя которой в нижнем регистре
total = add(NUM1, NUM2)  # pylint: disable=invalid-name

print(f"The sum of {NUM1} and {NUM2} is {total}")
