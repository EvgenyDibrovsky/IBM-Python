# Обработка файлов в Python с использованием функции open()

# Открытие файла с использованием функции open()
# Для чтения текстового файла используется функция open() с двумя основными параметрами:
# Путь к файлу: Указывается имя файла и директория, где он расположен.
# Режим: Указывается цель открытия файла, например 'r' для чтения, 'w' для записи, 'a' для добавления.

# Пример открытия файла:
file = open('file.txt', 'r')

# Использование 'with' statement
# Для упрощения работы с файлами и автоматического закрытия файлов используется конструкция "with".
# Пример открытия файла с использованием 'with':
with open('file.txt', 'r') as file:
    # дальнейший код

# Чтение всего содержимого файла
# С помощью метода read() можно прочитать весь контент файла и сохранить его в переменной.
with open('file.txt', 'r') as file:
    file_content = file.read()
    print(file_content)

# Чтение содержимого файла построчно
# Метод readline() позволяет читать файл построчно.
with open('file.txt', 'r') as file:
    line1 = file.readline()  # Читает первую строку
    line2 = file.readline()  # Читает вторую строку
    print(line1)
    print(line2)

# Чтение определенных символов из файла
# С помощью метода read(size) можно прочитать определенное количество символов.
with open('file.txt', 'r') as file:
    file.seek(10)  # Перемещение к 11-му байту (счет с нуля)
    characters = file.read(5)  # Читает следующие 5 символов
    print(characters)
