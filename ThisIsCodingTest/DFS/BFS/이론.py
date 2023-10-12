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

def fac_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fac_recur(n):
    if n <= 1:
        return 1
    return n * fac_recur(n - 1)

print(fac_iter(5), fac_recur(5))

graph = [[] for _ in range(3)]

graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)

# 인접 행렬 방식은 모든 관계를 저장하므로 노드 개수가 많을수록 메모리가 불필요하게 낭비된다. 그 대신 두 노드의 관계를 빠르게 알 수 있다.
# 인접 리스트 방식은 필요한 관계만 저장하므로 메모리가 효율적으로 사용된다. 다만 두 노드의 관계를 빠르게 알 수 없다.

def dfs(graph, v, visited):
    visited[v] = True
    print(v, ent = ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True