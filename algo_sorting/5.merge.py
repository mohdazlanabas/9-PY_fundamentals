# Sort: Merge
# BigO: O(nlogn)
# Difficulty: Medium
# Recursive: Yes
# Extra Space: Yes
# Method: Merge
# Lines Of Code: 30

# Divide & conquer

#1 terate once Check length
#2 Split to half
#3 Sort Left
#4 Sort Right
#5 Repeat 2,3,4
#6 Move lowest right set to left side at right position

# Merge Sort is useful for sorting linked lists in O(nLogn)time

array = [64, 34, 25, 12, 22, 11, 90]
def mergeSort(array):
    n = len(array) # n needs to be local
    print("Splitting ", array)
    if n > 1:
        mid = n // 2
        lefthalf = array[:mid]
        righthalf = array[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                array[k] = lefthalf[i]
                i = i + 1
            else:
                array[k] = righthalf[j]
                j = j + 1
            k = k + 1
        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j < len(righthalf):
            array[k] = righthalf[j]
            j = j + 1
            k = k + 1
    print("Merging ", array)
mergeSort(array)
print(array)
