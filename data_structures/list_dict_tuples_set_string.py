# LIST = ARRAYS
# DICTIONARY
# TUPLES
# SETS
# STRING

"""

mylist1 = ["banana", "cherry", "apple"]
print(mylist1)
print("BREAK 1")

mylist2 = [5, True, "apple", "banana"]
print(mylist2)
print("BREAK 2")

item = mylist1[-1]
print(item)
print("BREAK 3")

for i in mylist1:
    print(i)
print(len(mylist1))
print("BREAK 4")

mylist1.append("lemon")
print(mylist1)
print("BREAK 5")

mylist1.insert(1, "berry")
print(mylist1)
print("BREAK 6")

item = mylist1.pop()
print(mylist1)
print("BREAK 7")

item = mylist1.remove("berry")
print(mylist1)
print("BREAK 8")

item = mylist1.reverse()
print(mylist1)
print("BREAK 9")

mylist3 = [3, 2, 4, 1, 6, 5, 7, 9, 0, 8]
mylist3.sort()
print(mylist3)
print("BREAK 10")

mylist4 = [0] * 5
print(mylist4)
print("BREAK 11")

mylist5 = mylist3 + mylist4
print(mylist5)
print("BREAK 12")

mylist6 = mylist5[2:7]
print(mylist6)
print("BREAK 13")

list_copy = mylist1
list_copy.append("lemon")
print(list_copy)
print(mylist1)
print("BREAK 14")

modify_list = [j * j for j in mylist3]
print(mylist3)
print(modify_list)
print("BREAK 15")

"""

"""
# TUPLES

print("BREAK 1")
mytuple1 = tuple(["Max", 28, "Boston"])
print(mytuple1)

print("BREAK 2")
item = mytuple1[2]
print(item)

print("BREAK 3")
for x in mytuple1:
    print(x)

print("BREAK 4")
if "Max" in mytuple1:
    print("Yes")
else:
    print("no")

print("BREAK 5")
mytuple2 = ("a", "p", "p", "l", "e")
print(len(mytuple2))
print(mytuple2.count("p"))
print(mytuple2.index("l"))

print("BREAK 6")
my_list = list(mytuple2)
print(my_list)
mytuple2 = tuple(my_list)
print(mytuple2)

print("BREAK 7")
mytuple3 = (3, 2, 4, 1, 6, 5, 7, 9, 0, 8)
mod_list1 = mytuple3[3:7]
print(mod_list1)

print("BREAK 8")
mod_list2 = mytuple3[::-1]
print(mod_list2)

print("BREAK 9 - Unpacking")
mytuple4 = "Max", 28, "Boston"
name, age, city = mytuple4
print(name)
print(age)
print(city)

print("BREAK 10")
i1, *i2, i3 = mytuple3
print(i1)
print(i2)
print(i3)

print("BREAK 11")
import sys

my_listA = [0, 1, 2, "Hello", True]
my_tupleA = (0, 1, 2, "Hello", True)
print(sys.getsizeof(my_listA), "bytes")
print(sys.getsizeof(my_tupleA), "bytes")

print("BREAK 12")
import timeit

print(timeit.timeit(stmt="[0,1,2,3,4,5,6,7,8,9]", number=100000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5,6,7,8,9)", number=1000000000))

# DICTIONARIES

mydict = {"name": "Max", "age": 28, "city": "new York"}
print(mydict)
value = mydict["name"]
print(value)

mydict["email"] = "maxyz@email.com"
print(mydict)

del mydict["name"]
print(mydict)

mydict.popitem()
print(mydict)

try:
    print(mydict["name"])
except:
    print("Error")

for key in mydict:
    print(key)

for key in mydict.keys():
    print(key)

for value in mydict.values():
    print(value)

for key, value in mydict.items():
    print(key, value)

mydict_cpy = mydict
print(mydict_cpy)

mydict_copy["email"] = "max@xyz.com"
print(mydict_cpy)
print(mydict)

my_dict = {"name": "Min", "age": 28, "email": "min@xyz.com"}
my_dict2 = {"name": "Mary", "age": 83, "city": "Boston"}
my_dict.update(my_dict_2)
print(my_dict)

my_dict3 = {3: 9, 6: 36, 9: 81}
print(mydict3)

value3 = my_dict3[3]
print(value3)


# SETS - Has no duplicates

myset = {1, 2, 3, 4, 1, 2}
print(myset)

myset2 = set(1, 2, 3, 4, 1, 2)
print(myset2)

myset3 = set("Hello")
print(myset)

myset4 = set()
myset4.add(1)
myset.add(2)
myset.add(3)
print(myset4)
print(myset4.pop)

if 2 in myset4:
    prin("yes")

odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8, 0}
primes = {2, 3, 5, 7}
u = odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

setA = {1, 3, 5, 7, 9}
setB = {2, 4, 6, 8, 0}
psetC = {2, 3, 5, 7}
diff = setA.difference(setB)
print(diff)

diff = setB.symetric_difference(setA)
print(diff)


# HASHTABLES (DICTIONARY)
# use {} or dict()
my_dict = {"Dave": "001", "Ava": "002", "Joe": "003"}
print(my_dict)
print(type(my_dict))

new_dict = dict()
print(new_dict)
print(type(new_dict))

new_dict = dict(Dave="001", Ava="002")
print(new_dict)

# Nested Dictionaries
emp_details = {
    "employee": {
        "Dave": {"ID": "001", "Salary": "2000", "Designation": "Executive"},
        "Ava": {"ID": "002", "Salary": "1000", "Designation": "Team Lead"},
    }
}
print(emp_details)

print(my_dict["Dave"])
print(my_dict.keys())
print(my_dict.values())
print(my_dict.get("Ava"))

for x in my_dict:
    print(x)
for x in my_dict.values():
    print(x)
for x, y in my_dict.items():
    print(x, y)

my_dict["Dave"] = "004"
my_dict["Chris"] = "005"
print(my_dict)

import pandas as pandas
df = pandas.DataFrame(emp_details["employee"])
print(df)

#del, pop, popitem, clear
my_dict.pop('Ava')
print(my_dict)
my_dict.popitem()
print(my_dict)
del my_dict['Dave']
print(my_dict)

"""

# STRINGS

my_string = "    Helllo World   "
print(my_string)

char = my_string[2]
print(char)

substring = my_string[2:4]
print(substring)

substring2 = my_string[::-1]
print(substring2)

name = "Tom"
greeting = "Holla"
sentence = greeting + " " + name
print(sentence)

for x in greeting:
    print(x)

if "e" in greeting:
    print("yes")
else:
    print("no")

my_string2 = my_string.strip()
print(my_string2)

print(my_string.upper())
print(my_string.lower())

# as theres pplace in my_string

print(my_string.startswith(" "))

print(my_string.endswith(" "))

print(my_string.find("lo"))

print(my_string.count(" "))

print(my_string.replace(" ", "-"))

my_list = my_string.split(" ")
print(my_list)
new_string = " ".join(my_list)
print(new_string)

my_list2 = ["a"] * 6
print(my_list2)

my_string3 = "".join(my_list2)
print(my_string3)

var = "Tom"
mystring4 = "the variable is %s" % var
print(mystring4)

var2 = 3
mystring5 = "the variable is %d" % var2
print(mystring5)

var3 = 3.14726
mystring6 = "the variable is %f" % var3
print(mystring6)
# can be %.2f
