"""
computers[i][i] 부분은 고려하지 않고,

computers[i][j]와 [j][i]가 1이면 연결된 상태이므로, 이걸 체크한다.
"""

from collections import deque
check = set([0])

def bfs(i, computers, n):
    global check
    dq = deque()
    dq.append(i)
    while dq:
        pop = dq.popleft()
        for j in range(n):  # 0, 1, 2
            if computers[pop][j] == 1 and pop != j and j not in check:
                       #  0 (0, 1, 2)
                       #  1 (0, 1, 2)
                dq.append(j)
                check.add(j)
    return

def solution(n, computers):
    global check                        # {0}
    answer = 0
    bfs(0, computers, n)
    answer += 1
    while len(check) != n:
        print(check)
        for i in range(n):     # 0, 1, 2
            if i not in check:
                check.add(i)
                bfs(i, computers, n)
                answer+=1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

##############################

# 유니온 파인드

def solution1(n, computers):
    parents = [i for i in range(n)] # [0, 1, 2]

    def find(a):
        if parents[a] == a:             
            return a
        parents[a] = find(parents[a])
        return parents[a]

    def union(a, b):
        aP = find(a)
        bP = find(b)

        if aP < bP:
            parents[bP] = aP
        else:
            parents[aP] = bP

    for row in range(n):
        for col in range(n):
            if row == col:
                continue
            if computers[row][col]:
                union(row, col)

    ans = set()
    for i in range(n):
        ans.add(find(parents[i]))
    return len(ans)