# Sort: Counting
# BigO: O(n)
# Difficulty: Easy
# Recursive: No
# Extra Space: Yes
# Method: Hashing
# Lines Of Code: 17

#1 Count Value Key occurences and store in Index Key
#2 Add Index Key occurences and store in current Index Key
#3 Shift clockwise one time

# Counting sort is efficient if the range of input data is not significantly greater than the number of objects to be sorted. Consider the situation where the input sequence is between range 1 to 10K and the data is 10, 5, 10K, 5K. It is often used as a sub-routine to another sorting algorithm like radix sort. 

array = [3,5,1,6,7,8,3,2,4,2,5,9,0]
size = len(array)

def countingSort(array):
    
    output = [0 for i in range(size)]
    count = [0 for i in range(256)]
    
    for i in array:
        count[array[i]] += 1

    for i in range(1,10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1
        
    for i in range(size):
        array[i] = output[i]

countingSort(array)
print(array)
