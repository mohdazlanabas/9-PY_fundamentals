array = [64, 34, 25, 12, 22, 11, 90]
n = len(array)

def insertionSort(array):
    for i in range(1, n):
        key = array[i]
        j = i-1
        while j >=0 and key < array[j] :
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key

insertionSort(array)
print(array)
