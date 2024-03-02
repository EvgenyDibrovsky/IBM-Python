# Conditions and Branching

# 1. Comparison operations
# Операции сравнения используются для сравнения значений и принятия решений на основе результатов.

# Equality operator
# Оператор равенства == проверяет равенство двух значений.
age = 25
if age == 25:
    print("You are 25 years old.")
# Код проверяет, равна ли переменная age 25 и выводит соответствующее сообщение.

# Inequality operator
# Оператор неравенства != проверяет, не равны ли два значения.
if age != 30:
    print("You are not 30 years old.")
# Код проверяет, не равна ли переменная age 30 и выводит соответствующее сообщение.

# Greater than and less than
# Сравнение одного значения с другим на больше или меньше.
if age >= 20:
    print("Yes, the Age is greater than 20")
# Код проверяет, больше или равна ли переменная age 20 и выводит соответствующее сообщение.

# 2. Branching
# Ветвление позволяет принимать решения в программе на основе условий.

# The IF statement
# Пример: вход в бар. Если возраст больше определенного, то вход разрешен, иначе нет.
age = 20
if age >= 21:
    print("You can enter the bar.")
else:
    print("Sorry, you cannot enter.")
# Используется if-else для принятия решения на основе переменной age.

# The ELIF Statement
# Иногда необходимо проверить несколько условий.
if age >= 21:
    print("You can enter the bar.")
elif age >= 18:
    print("You can watch a movie.")
else:
    print("Sorry, you cannot do either.")
# Пример с использованием elif для проверки нескольких условий.

# Real-life example: Automated Teller Machine (ATM)
# Пример использования ветвления в банкомате.
user_choice = "Withdraw Cash"
if user_choice == "Withdraw Cash":
    amount = int(input("Enter the amount to withdraw: "))
    if amount % 10 == 0:
        dispense_cash(amount)
    else:
        print("Please enter a multiple of 10.")
else:
    print("Thank you for using the ATM.")
# Ветвление используется для принятия решений на основе ввода пользователя.

# 3. Logical operators
# Логические операторы используются для объединения и манипуляции условиями.

# The NOT operator
# Оператор NOT отрицает условие.
is_do_not_disturb = True
if not is_do_not_disturb:
    send_notification("New message received")
# Пример: настройки уведомлений в смартфоне.

# The AND operator
# Оператор AND проверяет, что все условия истинны.
has_valid_id_card = True
has_matching_fingerprint = True
if has_valid_id_card and has_matching_fingerprint:
    open_high_security_door()
# Пример: контроль доступа в защищенное помещение.

# The OR operator
# Оператор OR проверяет, истинно ли хотя бы одно условие.
friend1_likes_comedy = True
friend2_likes_action = False
friend3_likes_drama = False
if friend1_likes_comedy or friend2_likes_action or friend3_likes_drama:
    choose_movie()
# Пример: выбор фильма для просмотра с друзьями.
