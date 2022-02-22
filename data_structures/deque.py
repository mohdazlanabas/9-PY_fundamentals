import collections

DoubleEnded = collections.deque(["Monday", "Tuesday", "Wednesday"])
print(DoubleEnded)
DoubleEnded.append("Thursday")
print("Append at right - ")
print(DoubleEnded)

DoubleEnded.appendleft("Sunday")
print("Append at left - ")
print(DoubleEnded)

DoubleEnded.pop()
print("Deleting from right - ")
print(DoubleEnded)

DoubleEnded.popleft()
print("Deleting from left - ")
print(DoubleEnded)
