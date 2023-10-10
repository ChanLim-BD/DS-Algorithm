K = int(input())

stack = []

for _ in range(K):
    i = int(input())
    if i == 0:
        if not stack:
            continue
        stack.pop()
    else:
        stack.append(i)

print(sum(stack))