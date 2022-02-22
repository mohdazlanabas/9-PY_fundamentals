# Sort: Insertion
# BigO: O(n^2)
# Difficulty: Easy
# Recursive: No
# Extra Space: No
# Method: Inserting
# Lines Of Code: 12

#1 No Iterations
#2 check number
#3 if smaller swap
#4 go back swap samall number to the end
#5 move to next set
#6 repeat 2 3 4 5

array = [64, 34, 25, 12, 22, 11, 90]
n = len(array)
def insertionSort(array):
    for i in range(n):
        key = array[i]
        j = i - 1

        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
            array[j + 1] = key
insertionSort(array)
print(array)
