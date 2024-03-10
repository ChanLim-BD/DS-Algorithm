# n = int(input())
# guild = list(map(int, input().split()))
# guild.sort()

# group_count = 0
# answer = 0

# for i in guild:             # 1 2 2 2 3 3
#     group_count += 1        # 1 1 2 1 2 3
#     if group_count >= i:
#         answer += 1
#         group_count = 0

# print(answer)

# s = input()
# answer = 1
# for i in s:
#     if int(i) == 0 or int(i) == 1:
#         answer += int(i)
#         continue
#     else:
#         answer *= int(i)
# print(answer)

# s = input()
# count_0 = 0
# count_1 = 0

# if s[0] == '1':
#     count_1 += 1
# else:
#     count_0 += 1

# for i in range(len(s) -1):
#     if s[i] != s[i + 1]:
#         if s[i+1] == '1':
#             count_0 +=1
#         else:
#             count_1 +=1
#     else:
#         continue

# print(min(count_0, count_1))

# n = int(input())
# lst = list(map(int, input().split()))
# lst.sort()

# answer = 1
# for i in lst:
#     if answer < i:
#         break
#     answer += i

# print(answer)

# n, m = map(int, input().split())
# balls = list(map(int, input().split()))

# count = 0

# for i in range(n):
#     for j in range(i, n):
#         if i == j or balls[i] == balls[j]:
#             continue
#         else:
#             count += 1
# print(count)

# import heapq

# food_times = [3, 1, 2]
# k = 5
# q = []
# for i in range(len(food_times)):
#     heapq.heappush(q, (food_times[i], i + 1))

# sum_value = 0
# prev = 0
# length = len(food_times)

#         # 5            3       2        1       5
# while sum_value + ((q[0][0] - prev) * length) <= k:
#     print(q)
#     now = heapq.heappop(q)[0] # 1 | 2
#     sum_value += (now - prev) * length # += (1 - 0) * 3 = 3 | += (2 - 1) * 2 = 2
#     length -= 1 # 2 1
#     prev = now # 1 2

# result = sorted(q, key=lambda x: x[1])
# print(result, k, sum_value)
# print(result[(k-sum_value) % length][1])

# array = [[1,2,3],[4,5,6],[7,8,9]]
# rotate = [[0] * 3 for _ in range(3)]
# for i in range(3):
#     for j in range(3):
#         rotate[j][3 - i - 1] = array[i][j]

# print(rotate)

# array99 = [[0] * (3 * 3) for _ in range(3 * 3)]
# for i in range(3):
#     for j in range(3):
#         array99[i + 3][j + 3] = 999

# for a in array99:
#     print(a)        

# for i in range(3 * 2):
#     for j in range(3 * 2):
#         for y in range(3):
#             for x in range(3):
#                 if array99[i+y][j+x] == 999:
#                     continue
#                 array99[i+y][j+x] = -1

# for a in array99:
#     print(a)

# n = int(input()) # 보드 크기
# k = int(input()) # 사과의 개수
# board = [[0] * (n + 1) for _ in range(n + 1)]

# for _ in range(k):
#     y, x = map(int, input().split())
#     board[y][x] = 1

# l = int(input())
# change = []
# for _ in range(l):
#     x, c = input().split()
#     change.append((int(x), c))

# #     동 남 서 북
# dy = [0, 1, 0, -1]
# dx = [1, 0, -1, 0]

# for b in board:
#     print(b)

# y, x = 1, 1
# board[y][x] = 2
# direction = 0
# time = 0
# index = 0
# q = [(y,x)]

# def turn(direction, c):
#     if c == 'L':
#         direction = (direction - 1) % 4
#     else:
#         direction = (direction + 1) % 4
#     return direction

# while True:
#     ny = y + dy[direction]
#     nx = x + dx[direction]
#     if 1 <= ny <= n and 1 <= nx <= n and board[ny][nx] != 2:
#         if board[ny][nx] == 0:
#             board[ny][nx] = 2
#             q.append((y,x))
#             py, px = q.pop(0)
#             board[py][px] = 0
#         if board[ny][nx] == 1:
#             board[ny][nx] =2
#             q.append((ny, nx))
#     else:
#         time += 1
#         break
#     y, x = ny, nx
#     time += 1

#     if index < 1 and time == change[index][0]:
#         direction = turn(direction, change[index][1])
#         index += 1

# print(time)

# def recur1(number):
#     if number == M:
#         print(*arr1)
#         return
    
#     for i in range(1, N+1):
#         arr1.append(i)
#         recur1(number+1)
#         arr1.pop()

# N, M = map(int, input().split())
# arr1 = []

# recur1(0)

# import sys
# sys.setrecursionlimit(10**7)
# input = sys.stdin.readline

# N, M = map(int, input().split())
# graph = [[False] * (N + 1) for _ in range(N + 1)]
# visited = [False] * (N + 1)
# answer = 0

# for _ in range(M):
#     u, v = map(int, input().split())
#     graph[u][v] = True
#     graph[v][u] = True

# def dfs(idx):
#     global visited, graph
#     visited[idx] = True
    
#     for i in range(1, N + 1):
#         if not visited[i] and graph[idx][i] == True:
#             dfs(i)
#     return 1
    
# for i in range(1, N + 1):
#     if visited[i] == False:
#         answer += dfs(i)

# print(answer)

# import sys
# sys.setrecursionlimit(10**7)
# input = sys.stdin.readline

# N, M, R = map(int, input().split())
# V = [i for i in range(1, N + 1)]
# E = []
# visited = [0] * (N + 1)
# cnt = 0

# for _ in range(M):
#     y, x = map(int, input().split())
#     E.append((y, x))

# def dfs(v, e, r):
#     global cnt
#     cnt += 1
#     visited[r] = cnt
#     for i in v:
#         if not visited[i] and (r, i) in e:
#             dfs(v, e, i)

# dfs(V, E, R)

# for i in range(1, N + 1):
#     print(visited[i])



# import sys
# sys.setrecursionlimit(10**7)
# input = sys.stdin.readline

# N, M, R = map(int, input().split())
# line = [[] for _ in range(N+1)]
# visited = [0] * (N+1)  # 저장값
# cnt = 1

# for _ in range(M):
#     a, b = map(int, input().split())
#     line[a].append(b)  # 양 방향 간선
#     line[b].append(a)  # 양 방향 간선

# def dfs(t):
#     global cnt
#     visited[t] = cnt
#     line[t].sort(reverse=True)
#     for i in line[t]:
#         if visited[i] == 0:
#             cnt += 1
#             dfs(i)

# dfs(R)

# for i in range(1, N+1):
#     print(visited[i])


#################################

# import sys
# sys.setrecursionlimit(10**7)
# input = sys.stdin.readline

# n = int(input())
# target = list(map(int, input().split()))
# m = int(input())

# graph = [[] for _ in range(n + 1)] # 인접 리스트
# for _ in range(m):                 # 인접 리스트 세팅
#     y, x = map(int, input().split())
#     graph[y].append(x)
#     graph[x].append(y)

# visited = [0] * (n + 1)            # 방문 여부
# result = [0] * (n + 1)             # 촌수 저장

# print(graph)

# def dfs(t): # 촌수 계산 대상
#     visited[t] = 1
#     for i in graph[t]:
#         if not visited[i]:
#             result[i] = result[t] + 1
#             dfs(i)

# dfs(target[0])

# print(result)

# if result[target[1]] > 0:
#     print(result[target[1]])
# else:
#     print(-1)

# import sys
# sys.setrecursionlimit(10**7)
# input = sys.stdin.readline

# n = int(input())
# graph = [[] * (n + 1) for _ in range(n + 1)]
# visited = [False] * (n + 1)

# for _ in range(1, n):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# parent = [0] * (n + 1)

# def dfs(idx):
#     visited[idx] = True
#     for i in graph[idx]:
#         if not visited[i]:
#             parent[i] = idx
#             dfs(i)

# dfs(1)

# for i in range(2, len(parent)):
#     print(parent[i])

# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# T = int(input())
# MAX = 50 + 10

# dy = [0, 1, 0, -1]
# dx = [1, 0, -1, 0]

# def dfs(y, x):
#     global visited, graph
#     visited[y][x] = True

#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if graph[ny][nx] and not visited[ny][nx]:
#             dfs(ny, nx)

# while T > 0:
#     T -= 1
#     M, N, K = map(int, input().split())

#     graph = [[False] * MAX for _ in range(MAX)]
#     visited = [[False] * MAX for _ in range(MAX)]
    
#     for _ in range(K):
#         x, y = map(int, input().split())
#         graph[y + 1][x + 1] = True

#     answer = 0
#     for i in range(1, N + 1):
#         for j in range(1, M + 1):
#             if graph[i][j] and not visited[i][j]:
#                 dfs(i, j)
#                 answer += 1

#     print(answer)

# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# dy = [0, 1, 0, -1, 1, 1, -1, -1]
# dx = [1, 0, -1, 0, 1, -1, 1, -1]

# def dfs(y, x):
#     global graph
#     graph[y][x] = 0
#     for i in range(len(dy)):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if 0 <= ny < h and 0 <= nx < w and graph[ny][nx] == 1:
#             graph[ny][nx] = 0
#             dfs(ny, nx)

# while True:
#     answer = 0
#     w, h = map(int, input().split())
#     if w == 0 and h == 0:
#         break

#     graph = [list(map(int, input().split())) for _ in range(h)]

#     for i in range(h):
#         for j in range(w):
#             if graph[i][j] == 1:
#                 dfs(i, j)
#                 answer += 1
#     print(answer)


# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# N = int(input())
# board = [list(map(int, input().split())) for _ in range(N)]
# check = [[False] * N for _ in range(N)]

# dy = [1, 0]
# dx = [0, 1]

# def dfs(y, x):
#     check[y][x] = True
#     if board[y][x] == -1:
#         return
#     for i in range(2):
#         ny = y + board[y][x] * dy[i]
#         nx = x + board[y][x] * dx[i]
#         if 0 <= ny < N and 0 <= nx < N and check[ny][nx] == False:
#             check[ny][nx] = True
#             dfs(ny, nx)

# dfs(0, 0)

# if check[-1][-1] == True:
#     print("HaruHaru")
# else:
#     print("Hing")
# import sys
# from collections import deque
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline

# n = int(input())
# m = int(input())
# graph = [[] * (n + 1) for _ in range(n + 1)]
# visited = [False] * (n + 1)

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# answer = 0 

# def bfs(x):
#     global graph, visited, answer
#     q = deque(graph[x])
#     print(q)
#     visited[x] = True
#     answer += 1 

#     while q:
#         for i in graph[q.pop()]:
#             if visited[i] == False:
#                 visited[i] = True
#                 q.append(i)
#                 answer += 1
# bfs(1)

# print(answer - 1)

# board = [[0,0,0,0,0,0],
#          [0,0,0,0,0,0],
#          [0,0,0,0,0,0],
#          [0,0,0,0,1,0],
#          [0,0,0,0,0,0],]

# count = sum(b.count(0) for b in board)

# print(count)

# import sys
# from collections import deque
# input = sys.stdin.readline

# n, k = map(int, input().split())
# board = []
# locate = []

# for i in range(n):
#     board.append(list(map(int, input().split())))
#     for j in range(n):
#         if board[i][j] != 0:
#             locate.append((board[i][j], 0, i, j))

# locate.sort()
# q = deque(locate) # [(1, 0, 0, 0), (2, 0, 0, 2), (3, 0, 2, 0)]

# target_s, target_x, target_y = map(int, input().split())

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]

# while q:
#     virus, s, x, y = q.popleft()
#     if s == target_s:
#         break
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < n and 0 <= ny < n:
#             if board[nx][ny] == 0:
#                 board[nx][ny] = virus
#                 q.append((virus, s+1, nx, ny))

# print(board[target_x-1][target_y-1])

# import sys
# input = sys.stdin.readline

# N, K = map(int, input().split())
# stuff = [[0, 0]]
# dp = [[0] * (K + 1) for _ in range(N + 1)]

# for _ in range(N):
#     stuff.append(list(map(int, input().split())))

# for i in range(1, N + 1):
#     for j in range(1, K + 1):
#         weight, value = stuff[i]

#         if j < weight:
#             dp[i][j] = dp[i - 1][j]
#         else:
#             dp[i][j] = max(value + dp[i - 1][j - weight], dp[i - 1][j])

# print(dp[N][K])

# a1, h1 = map(int, input().split())
# a2, h2 = map(int, input().split())

# a, b = h1//a2 + (1 if h1%a2 else 0), h2//a1 + (1 if h2%a1 else 0)

# if a == b:
#     print("DRAW")
# elif a > b:
#     print("PLAYER A")
# else:
#     print("PLAYER B")

# n, m = map(int, input().split())
# rs = []
# chk = [False] * (n + 1)


# def func(num):
#     if num == m:
#         print(' '.join(map(str, rs)))
#         return
#     for i in range(1, n + 1):
#         if chk[i] == False:
#             chk[i] = True
#             rs.append(i)
#             func(num + 1)
#             chk[i] = False
#             rs.pop()

# func(0)

# n = int(input())
# m = int(input())
# graph = [[] * (n + 1) for _ in range(n + 1)]
# visited = [False] * (n + 1)

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# answer = 0 

# def dfs(graph, visited, answer ,x):
#     visited[x] = True
#     answer += 1

#     for i in graph[x]:
#         if not visited[i]:
#             dfs(i)

# dfs(graph, visited, answer, 4)
# print(visited)
# print(answer - 1)

# def getSpamEmails(subjects, spam_words):
#     answer = []
#     for subject in subjects:
#         check = 0
#         words = list(subject.split())
        
#         for sp in spam_words:
#             for w in words:
#                 if sp.lower() == w.lower():
#                     check += 1
        
#         if check >= 2:
#             answer.append('spam')
#         else:
#             answer.append('not_spam')

#     return answer

# print(getSpamEmails(
#     ['Let it go', 'The right thing to do'], ['to', 'do', 'right', 'go', 'let']))

# for i in []:
#     print("dd")

# things = set(i for i in range(1 , 11))
# arr = [1,3,8]
# can = sorted(list(things - set(arr)))

# tmp, cnt = 0, 0
# for i in can:
#     tmp += i
#     if tmp > 10:
#         break
#     cnt += 1

# print(tmp, cnt)

# def max_t(transaction):
#     transaction.sort(reverse=True)
#     print(transaction)
#     current = 0
#     count = 0
    
#     for t in transaction:
#         current += t
#         if current < 0:
#             break
#         count += 1
    
#     print(count)

# max_t([3,2,-5,-6,-1,4])

# import sys
# sys.setrecursionlimit(10 ** 8)
# input = sys.stdin.readline

# dy = [0, 1, 0, -1]
# dx = [1, 0, -1, 0]

# def recur(y, x):

#     if dp[y][x] != 0:
#         return dp[y][x]

#     for i in range(4):
#         ny, nx = y + dy[i], x + dx[i]
#         if 0 <= ny < n and 0 <= nx < n:
#             if graph[y][x] < graph[ny][nx]:
#                 dp[y][x] = max(dp[y][x], recur(ny, nx) + 1)

#     return dp[y][x]

# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]
# dp = [[0 for _ in range(n)] for _ in range(n)]

# for y in range(n):
#     for x in range(n):
#         recur(y, x)

# print(max(map(max, dp)) + 1)


# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# def recur(idx):
#     if idx == n-1:
#         return 0 
#     if idx > n-1:
#         return -99999
#     if dp[idx] != 0:
#         return dp[idx]

#     dp[idx] = max(recur(idx + interview[idx][0]) + interview[idx][1], recur(idx + 1))
    
#     return dp[idx]

# n = int(input())
# interview = [list(map(int, input().split())) for _ in range(n)]
# dp = [0 for _ in range(n + 1)]

# print(recur(0))

# dp2 = [0 for _ in range(n + 1)]

# for idx in range(n + 1)[::-1]:
#     if idx + interview[idx][0] > n:
#         dp[idx] = dp[idx + 1]
#     else:
#         dp[idx] = max(dp[idx + interview[idx][0]] + interview[idx][1], dp[idx+1])

# def recur1(idx, weight):
#     if weight > b:
#         return -99999
#     if idx == n:
#         return 0
#     if dp[idx][weight] != -1:
#         return dp[idx][weight]

#     dp[idx][weight] = max(recur1(idx + 1, weight + items[idx][0])+ items[idx][1], recur1(idx + 1, weight))

#     return dp[idx][weight]


# n, b = map(int, input().split())
# items = [list(map(int, input().split())) for _ in range(n)]
# dp = [[-1 for _ in range(100_001)] for _ in range(n)]

# print(recur1(0, 0))




# answer_used.sort()

# if answer_used:
#     print(answer)
#     print(*answer_used)
# else:
#     print(-1)



# def recur(idx, ssin, sson, use):
#     global answer

#     if idx == n:
#         if use == 0:
#             return
#         result = abs(ssin - sson)
#         answer = min(answer, result)
#         return
    
#     # 재료를 사용한다면,
#     recur(idx + 1, ssin * ingre[idx][0], sson + ingre[idx][1], use + 1)
#     # 재료를 사용하지 않았다면,
#     recur(idx + 1, ssin, sson, use)

# n = int(input())
# ingre = [list(map(int, input().split())) for _ in range(n)]

# answer = 9999999999999

# recur(0, 1, 0, 0)
# print(answer)



# def recur(idx, price):

#     if idx == n - 1:
#         answer = max(answer, price)

#     if idx > n - 1:
#         return
    
#     recur(idx + interview[idx][0], price + interview[idx][1])
#     recur(idx + 1, price)

# n = int(input())
# interview = [list(map(int, input().split())) for _ in range(n)]
# dp = [0] * (n + 1)

# import sys
# from collections import deque
# sys.setrecursionlimit(10 ** 6)
# input = sys.stdin.readline

# n = int(input())
# m = int(input())

# graph = [[] for _ in range(n + 1)]

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# visited = [False] * (n + 1)

# q = deque()

# q.append(1)

# while q:
#     node = q.popleft()
#     visited[node] = True

#     for nxt in graph[node]:
#         if visited[nxt] == True:
#             continue
#         q.append(nxt)

# print(visited)

# import sys
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline

# def recur(idx):
#     if idx == n-1:
#         return 0 
#     if idx > n-1:
#         return -99999
#     if dp[idx] != 0:
#         return dp[idx]

#     dp[idx] = max(recur(idx + interview[idx][0]) + interview[idx][1], recur(idx + 1))
    
#     return dp[idx]

# n = int(input())
# interview = [list(map(int, input().split())) for _ in range(n)]
# dp = [0 for _ in range(n + 1)]

# print(recur(0))

# dp2 = [0 for _ in range(n + 1)]

# for idx in range(n + 1)[::-1]:
#     if idx + interview[idx][0] > n:
#         dp[idx] = dp[idx + 1]
#     else:
#         dp[idx] = max(dp[idx + interview[idx][0]] + interview[idx][1], dp[idx+1])

import heapq

heap_items = [100, 15, 30, 50, 40, 10, 40]
heapq.heapify(heap_items)

print(heap_items)