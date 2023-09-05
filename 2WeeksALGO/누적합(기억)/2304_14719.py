# N = int(input())

# arr = []

# for _ in range(N):
#     x, y = map(int, input().split())
#     arr.append([x, y])

# sorted_arr = sorted(arr, key=lambda x : x[0])

# print(sorted_arr)

# prefix = [0 for _ in range(sorted_arr[N-1][0] - sorted_arr[0][0])]

# for i in range(len(sorted_arr) - 1):
#     if sorted_arr[i+1][1] > sorted_arr[i][1]:

########################################################################################################################

n = int(input())

graph = [0]*100
x_list = []
y_list = []

for i in range(n):
    x, y = map(int,input().split())
    graph[x] = y
    x_list.append(x)
    y_list.append(y)

# print(graph)
# print(x_list)
# print(y_list)

maxHeight = max(y_list)
maxWidth = max(x_list)
prefix = [0]*(maxWidth+2)
suffix = [0]*(maxWidth+2)

maxPoint = []

#prefix, suffix계산
h = 0
for f in range(1, maxWidth+3):
    if(graph[f] == maxHeight):
        maxPoint.append(f)
        break
    h = max(h, graph[f])
    prefix[f] = prefix[f-1] + h

h = 0
for b in range(maxWidth, 0, -1):
    if(graph[b] == maxHeight):
        maxPoint.append(b)
        break
    h = max(h, graph[b])
    suffix[b] = suffix[b+1] + h

print(graph)
print(prefix)
print(suffix)
print(maxPoint)

#정답 합치기

answer = max(prefix) + max(suffix)
answer += (maxPoint[1] - maxPoint[0] + 1)*maxHeight

print(answer)
