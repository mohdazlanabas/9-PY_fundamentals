import heapq

# a node ype solution
# min is parent less than child
# max is parent more thn child


array = []
heapq.heappush(array, (2, "code"))
heapq.heappush(array, (1, "eat"))
heapq.heappush(array, (3, "sleep"))
heapq.heappush(array, (0, "drink"))

while array:
    next_item = heapq.heappop(array)
    print(next_item)

# heapq.heapify convert list to heap
# heapq.heapush add elelements to heap
# heapq.heappop - return samllest data element
# heapq.heapreplace - replace smallest data element
