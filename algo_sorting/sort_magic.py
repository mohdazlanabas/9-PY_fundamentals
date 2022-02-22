# Bubble Sort
for j in range(n - i - 1):
    if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]
                
# Selection Sort
for idx in range(i + 1, n):
    if array[idx] < array[min_idx]:
        min_idx = idx
array[i], array[min_idx] = array[min_idx], array[i]