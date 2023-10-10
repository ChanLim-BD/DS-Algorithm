n = int(input())
N = [list(map(int, input().split())) for _ in range(n)]

N.sort(key=lambda x : (x[1], x[0]))

for n in N:
    print(n[0], n[1])

'''
5
0 4
1 2
1 -1
2 2
3 3
'''