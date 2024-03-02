# Python Data Structures Cheat Sheet

# List

# append()
# Описание: Добавляет элемент в конец списка.
# Синтаксис: 
list_name.append(element)
# Пример: 
fruits = ["apple", "banana", "orange"]
fruits.append("mango")
print(fruits)

# copy()
# Описание: Создает поверхностную копию списка.
# Пример: 
my_list = [1, 2, 3, 4, 5]
new_list = my_list.copy()
print(new_list)

# count()
# Описание: Подсчитывает количество вхождений элемента в список.
# Пример: 
my_list = [1, 2, 2, 3, 4, 2, 5, 2]
count = my_list.count(2)
print(count)

# Creating a list
# Описание: Создание списка.
# Пример: 
fruits = ["apple", "banana", "orange", "mango"]

# del
# Описание: Удаляет элемент списка по индексу.
# Пример: 
my_list = [10, 20, 30, 40, 50]
del my_list[2]
print(my_list)

# extend()
# Описание: Добавляет элементы из итерируемого объекта в список.
# Синтаксис: 
list_name.extend(iterable)
# Пример: 
fruits = ["apple", "banana", "orange"]
more_fruits = ["mango", "grape"]
fruits.extend(more_fruits)
print(fruits)

# Indexing
# Описание: Доступ к элементам списка по индексу.
# Пример: 
my_list = [10, 20, 30, 40, 50]
print(my_list[0])  # Первый элемент
print(my_list[-1])  # Последний элемент

# insert()
# Описание: Вставляет элемент на определенную позицию.
# Синтаксис: 
list_name.insert(index, element)
# Пример: 
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 6)
print(my_list)

# Modifying a list
# Описание: Модификация элементов списка.
# Пример: 
my_list = [10, 20, 30, 40, 50]
my_list[1] = 25
print(my_list)

# pop()
# Описание: Удаляет и возвращает элемент по индексу.
# Пример 1: 
my_list = [10, 20, 30, 40, 50]
removed_element = my_list.pop(2)
print(removed_element)
print(my_list)
# Пример 2: 
removed_element = my_list.pop()
print(removed_element)
print(my_list)

# remove()
# Описание: Удаляет первое вхождение элемента.
# Пример: 
my_list = [10, 20, 30, 40, 50]
my_list.remove(30)
print(my_list)

# reverse()
# Описание: Меняет порядок элементов на обратный.
# Пример: 
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)

# Slicing
# Описание: Получение среза списка.
# Синтаксис: 
list_name[start:end:step]
# Пример: 
my_list = [1, 2, 3, 4, 5]
print(my_list[1:4])
print(my_list[:3])
print(my_list[2:])
print(my_list[::2])

# sort()
# Описание: Сортировка элементов списка.
# Пример 1: 
my_list = [5, 2, 8, 1, 9]
my_list.sort()
print(my_list)
# Пример 2: 
my_list.sort(reverse=True)
print(my_list)

# Dictionary

# Accessing Values
# Описание: Доступ к значениям в словаре по ключам.
# Синтаксис: 
Value = dict_name["key_name"]
# Пример: 
name = person["name"]
age = person["age"]

# Add or modify
# Описание: Добавляет или модифицирует пары ключ-значение.
# Синтаксис: 
dict_name[key] = value
# Пример: 
person["Country"] = "USA"
person["city"] = "Chicago"

# clear()
# Описание: Очищает словарь.
# Синтаксис: 
dict_name.clear()
# Пример: 
grades.clear()

# copy()
# Описание: Создает поверхностную копию словаря.
# Синтаксис: 
new_dict = dict_name.copy()
# Пример: 
new_person = person.copy()

# Creating a Dictionary
# Описание: Создание словаря.
# Пример: 
dict_name = {}
person = {"name": "John", "age": 30, "city": "New York"}

# del
# Описание: Удаляет пару ключ-значение.
# Синтаксис: 
del dict_name[key]
# Пример: 
del person["Country"]

# items()
# Описание: Получение всех пар ключ-значение.
# Синтаксис: 
items_list = list(dict_name.items())
# Пример: 
info = list(person.items())

# key existence
# Описание: Проверка наличия ключа в словаре.
# Пример: 
if "name" in person:
    print("Name exists in the dictionary.")

# keys()
# Описание: Получение всех ключей из словаря.
# Синтаксис: 
keys_list = list(dict_name.keys())
# Пример: 
person_keys = list(person.keys())

# update()
# Описание: Обновляет или добавляет пары ключ-значение.
# Синтаксис: 
dict_name.update({key: value})
# Пример: 
person.update({"Profession": "Doctor"})

# values()
# Описание: Получение всех значений из словаря.
# Синтаксис: 
values_list = list(dict_name.values())
# Пример: 
person_values = list(person.values())

# Sets

# add()
# Описание: Добавляет элемент в множество.
# Синтаксис: 
set_name.add(element)
# Пример: 
fruits.add("mango")

# clear()
# Описание: Удаляет все элементы из множества.
# Синтаксис: 
set_name.clear()
# Пример: 
fruits.clear()

# copy()
# Описание: Создает поверхностную копию множества.
# Синтаксис: 
new_set = set_name.copy()
# Пример: 
new_fruits = fruits.copy()

# Defining Sets
# Описание: Создание множества.
# Пример: 
empty_set = set()
fruits = {"apple", "banana", "orange"}

# discard()
# Описание: Удаляет элемент из множества.
# Синтаксис: 
set_name.discard(element)
# Пример: 
fruits.discard("apple")

# issubset()
# Описание: Проверяет, является ли множество подмножеством другого.
# Синтаксис: 
is_subset = set1.issubset(set2)
# Пример: 
is_subset = fruits.issubset(colors)

# issuperset()
# Описание: Проверяет, является ли множество надмножеством другого.
# Синтаксис: 
is_superset = set1.issuperset(set2)
# Пример: 
is_superset = colors.issuperset(fruits)

# pop()
# Описание: Удаляет и возвращает произвольный элемент из множества.
# Синтаксис: 
removed_element = set_name.pop()
# Пример: 
removed_fruit = fruits.pop()

# remove()
# Описание: Удаляет определенный элемент из множества.
# Синтаксис: 
set_name.remove(element)
# Пример: 
fruits.remove("banana")

# Set Operations
# Описание: Выполнение операций над множествами.
# Синтаксис: 
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
sym_diff_set = set1.symmetric_difference(set2)
# Пример: 
combined = fruits.union(colors)
common = fruits.intersection(colors)
unique_to_fruits = fruits.difference(colors)
sym_diff = fruits.symmetric_difference(colors)

# update()
# Описание: Добавляет элементы из итерируемого объекта в множество.
# Синтаксис: 
set_name.update(iterable)
# Пример: 
fruits.update(["kiwi", "grape"])
