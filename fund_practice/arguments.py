def print_name(name):
    print(name)


print_name("Alex")


def foo(a, b, c):
    print(a, b, c)


foo(1, 2, 3)


def foo2(d, e, *args, **kwargs):
    print(d, e)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


foo2(1, 2, 3, 4, 5, six=6, seven=7)


def foo3(f, g, h):
    print(f, g, h)


my_list = [1, 2, 3]
foo3(*my_list)

my_dict = {"f": 6, "g": 7, "h": 8}
foo3(**my_dict)


def foo4(x):
    x = 5


var = 10
foo4(var)
print(var)


def foo5(a_list):
    a_list.append(4)
    a_list[0] = 100


my_list2 = [1, 2, 3]
foo5(my_list2)
print(my_list2)
