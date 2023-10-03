from collections import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


from collections import Counter

letter = 'sdadfhjklasjfkldjfklsdjfkldjfkaljfkdjaflkdjflksdjklfdjaklfdj'

c = Counter(letter)
print(c)
print(c['d'])

A, B = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0 for _ in range(A+1)]

for i in range(A):
    prefix[i+1] = prefix[i] + arr[i]