"""
5
1 2
2 3
3 4
4 5
4
1 1
1 2
2 1
2 2
"""

import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

print(tree)

q = int(input())
for _ in range(q):
    t, k = map(int, input().split())
    if t == 1:
        if (len(tree[k]) < 2):
            print("no")
        else:
            print("yes")

    elif t == 2:   # 우선 입력으로 주어지는 정보는 트리임이 보장된다고 했으므로 모든 간선은 단절선이 된다!
        print("yes")