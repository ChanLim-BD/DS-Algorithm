"""
N = 3
trans = True

for i in range(N):              # 0     1     2     
    if trans:
        for j in range(i+1):        # 0     10    210
            print(j, i)
        for k in range(i)[::-1]:    # 0     01    012
            print(i, k)
        trans = False
    else:
        for j in range(i+1):        # 0     10    210
            print(i, j)
        for k in range(i)[::-1]:    # 0     01    012
            print(k, i)
        trans = True
"""

n = 7
h = True
tmp = 1

graph = [[0] * n for _ in range(n)]

graph[0][0] = 1

# print(graph)

for i in range(1, n):                       
    if h == True:
        for j in range(i + 1):
            tmp += 1
            # print(i, j, tmp)
            graph[i][j] = tmp
            if i == j:
                for k in range(i)[::-1]:
                    tmp += 1
                    # print(k, i, tmp)
                    graph[k][i] = tmp
        h = False
    else:
        for j in range(i + 1):
            tmp += 1
            # print(j, i, tmp)
            graph[j][i] = tmp
            if i == j:
                for k in range(i)[::-1]:
                    tmp += 1
                    # print(i, k, tmp)
                    graph[i][k] = tmp
        h = True

print()
print(tmp)
for g in graph:
    print(g)