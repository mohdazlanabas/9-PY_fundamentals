# Sort: Bucket
# BigO: O(n^2)
# Difficulty: Easy
# Recursive: 
# Extra Space: 
# Method: Exchanging
# Lines Of Code: 

#1 No Iteration
#2 similar to bubble sort but larger gap between comb ends
#3 after each iteration the comb ends reducs by 1.3
#4 until it becomes single space

array2 = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434, 0.2]
slot_num = 10  

def insertionSort(array):
    for i in range(len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array

def bucketSort(array2):
    arr = []
    # 10 means 10 slots, each
    # slot's size is 0.1
    for i in range(slot_num):
        arr.append([])
    for j in array2:
        index_array2 = int(slot_num * j)
        arr[index_array2].append(j)
    # sort the numbers in each slot
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            array2[k] = arr[i][j]
            k += 1
    return array2

print(bucketSort(array2))
