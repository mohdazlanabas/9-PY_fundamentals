# Sort: Quick
# BigO: O(nlogn)
# Difficulty: Easy
# Recursive: Yes
# Extra Space: No
# Method: Partitioning
# Lines Of Code: 21

#1 Iterate once
#2 Pick a number, set as pivot point
#3 sort left
#4 sort right
#5 merge

# Quicksort is preferred over Mergesort if used outside Linked List

array = [64, 34, 25, 12, 22, 11, 90]
n = len(array)

def partition(start, end, array):
    pivot_index = start
    pivot = array[pivot_index]

    while start < end:
        while start < n and array[start] <= pivot:
            start += 1
        while array[end] > pivot:
            end -= 1
        if start < end:
            array[start], array[end] = array[end], array[start]
    array[end], array[pivot_index] = array[pivot_index], array[end]
    return end
def quick_sort(start, end, array):
    if start < end:
        p = partition(start, end, array)
        quick_sort(start, p - 1,  array)
        quick_sort(p + 1, end, array)
quick_sort(0, len(array) - 1, array)
print(array)
