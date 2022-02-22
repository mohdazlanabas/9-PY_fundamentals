#  First In First Out

que = []

# IN

que.append("eat")
print(que)
que.append("sleep")
print(que)
que.append("code")
print(que)
que.append("drink")
print(que)

# OUT

# Careful: This is slow!
que.pop(0)
print(que)
que.pop(0)
print(que)
que.pop(0)
print(que)
