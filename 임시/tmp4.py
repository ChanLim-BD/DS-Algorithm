# ex = [1,2,3,3,3,2,3,3,6,6,4,2,4,3,1,5,6,7,3,3,6,6,4,2,4,3,1,5,6,7,3,3,6,6,4,2,4,3,1,5,6,7]
# x = {}

# for i in ex:
#     count = ex.count(i)
#     x[i] = count

# print(x)                                                # {1: 4, 2: 5, 3: 12, 6: 9, 4: 6, 5: 3, 7: 3}
# print(sorted(x, key = lambda i : x[i], reverse=True))   # [3[12], 6[9], 4[6], 2[5], 1[4], 5[3], 7[3]]

# def is_prime(n):
#     if n == 0 or n == 1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# print(is_prime(47))

# N, K = map(int, input().split()) # 4 7
# stuff = [[0, 0]]
# knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

# for _ in range(N):
#     stuff.append(list(map(int, input().split())))

# ###

# for i in range(1, N+1):
#     for j in range(1, K+1):
#         weight = stuff[i][0]
#         value = stuff[i][1]

#         if j < weight:
#             knapsack[i][j] = knapsack[i - 1][j] # weight보다 작으면 위의 값을 그대로 갖는다.
#         else:
#             knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])


# def solution(triangle):
#     answer = 0
#     height = len(triangle)
#     dp = [0] * (height + 1)
    
#     for i in range(height + 1):
#         # dp[0] = triangle[0][0]
#         # dp[1] = min(triangle[1][0], triangle[1][1])
#         # dp[2] = min(triangle[2][0], triangle[2][1], triangle[2][2])
#         if i == 0:
#             dp[i] == triangle[i][i]
#         dp[i] = min(triangle[i])
    
#     answer = sum(dp)
#     return answer

# print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

# def recur1(number):
#     if number == M:
#         print(*arr1)
#         return
    
#     for i in range(1, N+1):
#         arr1.append(i)
#         recur1(number+1)
#         arr1.pop()

# N, M = 3, 4

# arr1 = []

# recur1(0)

# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)

# n, m = map(int, input().split())
# start = int(input())
# graph = [[] for i in range(n + 1)]
# distance = [INF] * (n + 1)

# for _ in range(m):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))

# def dijkstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q:
#         dist, now = heapq.heappush(q)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost < distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (cost, i[0]))

# def recur1(number):
#     if number == M:
#         print(arr1)
#         return
    
#     for i in range(1, N+1):
#         arr1.append(i)
#         recur1(number+1)
#         arr1.pop()

# N, M = 2, 4

# arr1 = []

# recur1(0)

# def div(n):
#     tmp = 0
#     for i in range(1, int(n ** 0.5) + 1):
#         if n % i == 0:
#             tmp += 1
#             if i ** 2 != n:
#                 tmp += 1
#     return tmp

# print(div(9))



# def sol(s):
#     answer = []
#     tmp = {}
#     for i in range(len(s)):
#         if s[i] not in tmp:
#             answer.append(-1)
#         else:
#             answer.append(i - tmp[s[i]])
#         tmp[s[i]] = i
#     print(tmp)
#     return answer

# print(sol('sdskdjsjkdhjsadjsk'))

lst = ['azaaaaaaaa', 'ahaaaaaaaa', 'fbffffffffff', 'ddddddddddd']
print(sorted(lst, key=lambda x:x[1]))
