# Python Objects and Classes

# Introduction to classes and objects
# Python - это язык программирования, ориентированный на объекты и классы.

# Classes
# Класс - это шаблон для создания объектов, определяющий структуру и поведение его объектов.

# Creating classes
# Создание класса в Python осуществляется с помощью ключевого слова class.

class Car:
    # Class attributes (shared by all instances)
    max_speed = 120  # Maximum speed in km/h

    # Constructor method (initialize instance attributes)
    def __init__(self, make, model, color, speed=0):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed  # Initial speed is set to 0

    # Method for accelerating the car
    def accelerate(self, acceleration):
        if self.speed + acceleration <= Car.max_speed:
            self.speed += acceleration
        else:
            self.speed = Car.max_speed

    # Method to get the current speed of the car
    def get_speed(self):
        return self.speed

# Objects
# Объект - это экземпляр класса, имеющий состояние (атрибуты) и поведение (методы).

# Instantiating objects
# Для создания объекта используется имя класса, за которым следуют круглые скобки.

car1 = Car("Toyota", "Camry", "Blue")
car2 = Car("Honda", "Civic", "Red")

# Interacting with objects
# Взаимодействие с объектами происходит через вызов их методов или доступ к их атрибутам.

car1.accelerate(30)
car2.accelerate(20)
print(f"{car1.make} {car1.model} is currently at {car1.get_speed()} km/h.")
print(f"{car2.make} {car2.model} is currently at {car2.get_speed()} km/h.")

# Structure of classes and object code
# Классы и объекты в Python имеют определенную структуру.

class ClassName:
    # Class attributes
    class_attribute = value

    # Constructor
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    # Instance methods
    def method1(self, parameter1, parameter2):
        # Method logic
        pass

    def method2(self, parameter1, parameter2):
        # Method logic
        pass

# Creating objects
object1 = ClassName(arg1, arg2)
object2 = ClassName(arg1, arg2)

# Calling methods on objects
result1 = object1.method1(param1_value, param2_value)
result2 = object2.method2(param1_value, param2_value)

# Accessing and modifying object attributes
attribute_value = object1.attribute1
object1.attribute2 = new_value

# Accessing class attributes
class_attr_value = ClassName.class_attribute
