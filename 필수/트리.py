"""
Tree = 나무 !

Tree = Root + Seed

족보 (가족관계도) = 조상 + 후손

1. 트리의 조건
- 모든 노드들은 연결되어 있다.
- 사이클이 발생하면 안된다.

2.
조상이 정해진 트리 = 루티드 트리
조상이 정해지지 않은 트리 = 트리
"""

N = int(input())

graph = [[] for _ in range(130)]

for _ in range(N):
    a, b, c = map(str, input().split())
    # 아스키 코드!
    a = ord(a)
    b = ord(b)
    c = ord(c)

    graph[a].append(b)
    graph[a].append(c)

"""
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
"""

def recur1(node): # 전위 : 부모로부터 정보를 순서 계산
    if node == 46:
        return
    
    print(chr(node), end = "")
    recur1(graph[node][0])
    recur1(graph[node][1])

recur1(65)

print()

def recur2(node): # 후위 : 자식의 정보를 부모에게
    if node == 46:
        return
    
    recur2(graph[node][0])
    recur2(graph[node][1])
    print(chr(node), end = "")
    

recur2(65)