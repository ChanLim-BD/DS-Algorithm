"""
유니온 파인드

- 두 노드, 두 숫자, 두 무언가

= 같은 집합 안에 있나요?

_Union, _Find

= 가장 위에 있는 조상을 파악해서,
= 이 친구들이 연결되어 있는가?

최적화

_find 최적화 = 경로 단축

_union 최적화 = Union by Rank
"""
"""
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""

N, M = map(int, input().split())

rank = [0 for _ in range(N + 1)] # 노드,

par = [i for i in range(N + 1)]
# [0 ,1 ,2, 3, 4, 5, 6, 7]

def _union(A, B): # 최대 높이를 확인해서 합쳐준다. 효과적으로,
    A = _find(A)
    B = _find(B)

    if A == B:
        return
    
    if rank[A] < rank[B]:
        par[A] = B
    elif rank[B] < rank[A]:
        par[B] = A
    else:
        par[A] = B
        rank[B] += 1
    

def _find(A):
    if par[A] == A: # 만약에 스스로를 부모라 칭한다면
        return A
    else:
        par[A] = _find(par[A])
        return _find(par[A])

for _ in range(M):
    X,A,B = map(int, input().split())

    if X == 0:
        _union(A, B)
    else:
        if _find(A) == _find(B):
            print("YES")
        else:
            print("NO")

print(rank)