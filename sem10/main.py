import random
import statistics


class Human:
    def __init__(self, name, surname, age, grades):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = grades

    def __str__(self):
        return f'Имя: {self.name} {self.surname}, возраст: {self.age} лет'

    def __repr__(self):
        return self.name

    def greet(self):
        print(f'Привет, меня зовут {self.name} и мне {self.age} годиков')

    def avg_score(self):
        return statistics.mean(self.grades)


person1 = Human('Слава', 'Олегович', 15, [])
person2 = Human('Вася', 'Олегович', 15, [])
person3 = Human('Коля', 'Олегович', 15, [])
person4 = Human('Витя', 'Олегович', 15, [])
person5 = Human('Миша', 'Олегович', 15, [])


# lst = [person1, person2, person3, person4, person5]
#
# for i in lst:
#     i.grades = [random.randint(1, 10) for j in range(5)]
#
# print(lst)
#
# lst.sort(key=lambda x: x.avg_score())
# print(lst)
#
# print(person1)
# print(person1.avg_score())
# print(person1.greet())

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_a_cords(selfs):
        return [a.x, a.y, b.x, b.y]

    def area(self):
        return (b.x - a.x) * (a.y - b.y)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


a = Point(1, 10)
b = Point(10, 1)

prym = Rectangle(a, b)

print(prym.get_a_cords())
print(prym.area())