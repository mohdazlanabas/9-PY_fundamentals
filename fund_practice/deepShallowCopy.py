# SHALLOW AND DEEP COPYING

import copy

org = [0, 1, 2, 3, 4, 5]
cpy = copy.copy(org)
cpy[0] = -10
print(cpy)
print(org)

org2 = [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]]
cpy2 = copy.deepcopy(org2)
cpy2[0][1] = -10
print(cpy2)
print(org2)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee


p1 = Person("Alex", 27)
p2 = copy.copy(p1)

p2.age = 20
print(p2.age)
print(p1.age)

company = Company(p1, p2)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56
print(company_clone.boss.age)
print(company.boss.age)
