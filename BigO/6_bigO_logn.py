def binary_search(array, query):
    lower_bound = 0
    upper_bound = len(array) - 1
    found_bool = False
    while lower_bound <= upper_bound and found_bool == False:

        middle_value = (lower_bound + upper_bound) // 2

        if array[middle_value] == query:
            found_bool = True
            return found_bool

        elif query > array[middle_value]:
            lower_bound = middle_value + 1

        else:
            upper_bound = middle_value - 1

    return found_bool


array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
query = 7

val_found = binary_search(array, query)
