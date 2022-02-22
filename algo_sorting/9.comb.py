# Sort: Comb
# BigO: O(n^2)
# Difficulty: Easy
# Recursive: No
# Extra Space: No
# Method: Exchanging
# Lines Of Code: 13

#1 Gap start with array len
#2 Swap large with small
#3 Move right
#4 gap reduce by 1.25
#5 Repeat 2,3,4

# Extension of Bubble sort

array = [64, 34, 25, 12, 22, 11, 90]
def combsort(array):
    gap = len(array)
    swaps = True
    while gap > 1 or swaps:
        gap = max(1, int(gap / 1.25))  # minimum gap is 1.25
        swaps = False

        for i in range(len(array) - gap):
            j = i + gap
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                swaps = True


combsort(array)
print(array)
