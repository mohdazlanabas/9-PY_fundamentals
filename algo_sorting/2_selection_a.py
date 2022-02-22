# Sort: Selection
# BigO: O(n^2)
# Difficulty: Easy
# Recursive: No
# Extra Space: No
# Method: Selection
# Lines Of Code: 8

#1 no iteration no key assignmemt
#2 move smallest number to left most position
#3 pick next smaller number

array = [64, 34, 25, 12, 22, 11, 90]
n = len(array)
for i in range(n):
    min_idx = i
    for j in range (i+1,n):
        if array[min_idx] > array[j]:
            min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]    
print(array)