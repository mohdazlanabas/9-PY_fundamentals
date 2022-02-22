# COLLECTIONS

import operator
from itertools import (
    product,
    permutations,
    combinations,
    combinations_with_replacement,
    accumulate,
    groupby,
    count,
    cycle,
    repeat,
)
from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

print("COLLECTIONS")
# Collections

a = "aaaaaabbbbbbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(2))
print(list(my_counter.elements()))

# namestuple

Point = namedtuple("Point", "x,y")
pt = Point(1, -4)
print(pt)
print(pt.x)

# OrderedDict

ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["d"] = 4
print(ordered_dict)

# defautdict

d = defaultdict(int)
d["a"] = 1
d["b"] = 2
print(d["b"])

e = deque()
e.append(1)
e.append(2)
print(e)
e.appendleft(3)
print(e)
e.pop()
print(e)

# .popleft
# .clear

e.extend([4, 5, 6, 7])
print(e)

e.extendleft([8, 9, 0])
print(e)

e.rotate(1)
print(e)
# rotateleft
# roateright

print("ITERTOOLS")
# ITERTOOLS


a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))

# prodb = product(a, b, repeat=2)
# print(list(prodb))

c = [1, 2, 3]
perm = permutations(c)
print(list(perm))

comb = combinations(c, 2)
print(list(comb))

comb_wr = combinations_with_replacement(c, 2)
print(list(comb_wr))

d = [1, 2, 5, 3, 4]
acc = accumulate(d)
print(d)
print(list(acc))

acc2 = accumulate(d, func=max)
print(list(acc2))


def smaller_than_3(x):
    return x < 3


e = [1, 2, 3, 4]
group_obj = groupby(e, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

persons = (
    {"name": "Tim", "age": 23},
    {"name": "Dan", "age": 25},
    {"name": "Lisa", "age": 27},
    {"name": "Claire", "age": 29},
)

for i in count(10):
    print(i)
    if i == 15:
        break

f = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for j in cycle(f):
    print(j)
    if j == 5:
        break

# LAMBDA arguments:expression


def add10(x):
    return x + 10


def mult(s, t):
    return s * t


print(mult(2, 7))

# EXCEPTIONS

try:
    g = 5 / 0
except:
    print("an error happened")

try:
    h = 5 / 0
except Exception as e:
    print(e)

try:
    j = 5 / 1
    k = j + 4
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("everything is ok")
finally:
    print("proceed")


class ValueToHighError(Exception):
    pass


class ValueToSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueToHighError("value to high")
    if x < 5:
        raise ValueToSmallError("value to small")


try:
    test_value(200)
except ValueToHighError as e:
    print(e)
except ValueToSmallError as e:
    print(e.message, e.value)
