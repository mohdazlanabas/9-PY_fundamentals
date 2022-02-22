to = (int(input("Enter the number of elements: ")))

p = range(to)

fibonacci = []

for i in p:

    if(i == 0):
        n = 0
        fibonacci.append(n)
    elif(i == 1):
        n = 1
        fibonacci.append(n)
    elif(i > 1):
        n = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(n)

print(fibonacci)
