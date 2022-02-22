import random

a = random.random()
print(a)

b = random.uniform(1, 10)
print(b)

c = random.randint(1, 10)
print(c)

d = random.randrange(1, 10)
print(d)

e = random.normalvariate(0, 1)
print(e)

mylist = list("ABCDEFGH")
print(mylist)
f = random.choice(mylist)
print(f)
g = random.sample(mylist, 3)
print(g)
random.shuffle(mylist)
print(mylist)

random.seed(1)
print(random.random())
print(random.randint(1, 10))

import secrets

h = secrets.randbelow(10)
print(h)

i = secrets.randbits(4)
print(i)

k = secrets.choice(mylist)
print(k)

import numpy as np

l = np.random.rand(3)
print(l)

m = np.random.randint(0, 10, 3)
print(m)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
np.random.shuffle(arr)
print(arr)
