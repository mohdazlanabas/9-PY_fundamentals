# array is list in python, simplified
# tuples (immutable) also in this file

array1 = ["i", [10, 20, 30, 40, 50]]
list1 = ["a", "b", "c", 1, 2, 3, 4, 5, 6]
tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print(array1)
print(list1)
print(tuple1)

# print only the array
for x in array1:
    print(x)

print(array1[0])

array1.insert(1, 60)
print(array1)
