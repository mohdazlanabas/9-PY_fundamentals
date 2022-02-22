import time

start_time = time.time()
end_time = time.time()
print("\n Process Time (sec) is %s" % (time.time() - start_time))


def fact(n):
    product = 1
    for i in range(n):
        product = product * (i + 1)
    return product


print(fact(5))


def fact2(n):
    if n == 0:
        return 1
    else:
        return n * fact2(n - 1)


print(fact2(5))
