import converters
import random
from converters import kg_to_lbs
from pathlib import Path

kg_to_lbs(100)

# Constructor


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print('move')

    def draw(self):
        print('draw')


point = Point(10, 20)
point.x = 1
# point1.draw()
# point1.x = 10
# point1.y = 20
print(point.x)


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hai, I am {self.name}')


john = Person("John Smith")
john.talk()

bob = Person('Bob Sincalir')
bob.talk()

# Inheritance


class Mammal:
    def walk(self):
        print('Walk')


class Dog(Mammal):
    def bark(self):
        print('bark')


class Cat (Mammal):
    pass


dog1 = Dog()
dog1.walk()

# Modules

print(converters.kg_to_lbs(70))

# Google Python 3 Module Index

for r in range(3):
    print(random.random())
    print(random.randint(10, 100))

members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return(first, second)


dice = Dice()
print(dice.roll())

# Absolute path
# windows: c:\Program Files\Microsoft
# MAC: /ur/local/bin
# Relative path

path = Path()
for file in path.glob('*.py'):
    print(file)
path = Path()
for file in path.glob('*'):
    print(file)
