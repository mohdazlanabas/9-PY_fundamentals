# Sort: Shell
# BigO: O(n^2)
# Difficulty: Medium
# Recursive: No
# Extra Space: No
# Method: Insertion
# Lines Of Code: 15

# optimsed insertion sort
# similar to comb, has gap but replacement via insertion sort


array = [64, 34, 25, 12, 22, 11, 90]
size = len(array)


def shellSort(array, n):

    interval = n // 2

    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


shellSort(array, size)
print(array)
