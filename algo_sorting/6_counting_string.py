# Sort: Counting
# BigO: O(n)
# Difficulty: Easy
# Recursive: No
# Extra Space: Yes
# Method: Hashing
# Lines Of Code: 

# Count Value Key occurences and store in Index Key
# Add Index Key occurences and store in current Index Key
# Shift clockwise one time
# Good For Strings

# Counting sort is efficient if the range of input data is not significantly greater than the number of objects to be sorted. Consider the situation where the input sequence is between range 1 to 10K and the data is 10, 5, 10K, 5K. It is often used as a sub-routine to another sorting algorithm like radix sort. 

array = "bowelcryptfangshumidjk"
size = len(array)

def countingSort(array):

    output = [0 for i in range(size)]
    count = [0 for i in range(256)]
    answer = ["" for _ in array] #string

    for i in array:
        count[ord(i)] += 1

    for i in range(256):
        count[i] += count[i - 1]

    for i in range(size): #string
        output[count[ord(array[i])] - 1] = array[i]
        count[ord(array[i])] -= 1

    for i in range(size):
        answer[i] = output[i] #string
    return answer

answer = countingSort(array)
print(answer)

