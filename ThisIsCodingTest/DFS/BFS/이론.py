from collections import deque

stack = []

stack.append(5)
stack.append(1)
stack.append(4)
stack.append(2)
stack.append(5)
stack.pop()
stack.append(2)
stack.append(5)
stack.pop()

print(stack)
print(stack[::-1])

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(1)
queue.append(7)
queue.popleft()
queue.append(1)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
print(list(queue))