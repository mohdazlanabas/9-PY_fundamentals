# Sort: Radix
# BigO: O(nk)
# Difficulty: Medium
# Recursive: can be both
# Extra Space: Yes
# Method: Non Comparative
# Lines Of Code: 26

#1 Iterate once check length and index
#2 Move the small number to correct Index
#3 Move the overlapp large number to correct position

# bubble, selection, insertion sort is easy BigO(n^2)
# quick, merge sort is medium BigO(nlogn)
# counting is liner sorting BigO(n)
# Anything bigger tham n^2 use Radix
# Efficient but need space

array = [3,5,1,6,7,8,3,2,4,2,5,9,0]
size = len(array)

def countingSort(array, exp1):
    
    output = [0] * (size)
    count = [0] * (10)
    
    for i in range(0, size):
        index = array[i] // exp1
        count[index % 10] += 1
        
    for i in range(1, 10):
        count[i] += count[i - 1]
        
    i = size - 1
    while i >= 0:
        index = array[i] // exp1
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1
        
    i = 0
    for i in range(0, size):
        array[i] = output[i]

def radixSort(array):
    max1 = max(array)
    exp = 1
    while max1 / exp > 1:
        countingSort(array, exp)
        exp *= 10

radixSort(array)
print(array)

# for i in range(len(array)):
#    print(array[i], end=" ")
