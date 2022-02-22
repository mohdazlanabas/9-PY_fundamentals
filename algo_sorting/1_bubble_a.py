
# Sort: Bubble
# BigO: O(n^2)
# Difficulty: Easy
# Recursive: No
# Extra Space: No
# Method: Exchanging
# Lines Of Code: 9

#1 no iteration no key assignmemt
#2 swap small number and imediate next big number
#3 repeat

array = [64, 34, 25, 12, 22, 11, 90]
n = len(array)
def bubblesort(array):
    # (n) as we dont need space for last swap
    for i in range(n-1):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
bubblesort(array)
print(array)
