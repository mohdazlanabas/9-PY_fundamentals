from collections import deque

# Last In First Out

stack = deque()

# IN

stack.append("eat")
print(stack)
stack.append("sleep")
print(stack)
stack.append("code")
print(stack)
stack.append("drink")
print(stack)

# OUT

stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
