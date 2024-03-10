import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def recur(idx,A,B,C,D,E):
    global answer, used, answer_used

    if A >= a and B >= b and C >= c and D >= d:
        if answer > E:
            answer = min(answer, E)
            answer_used = []
            for i in used:
                answer_used.append(i)            
    if idx == n:
        return
    
    used.append(idx + 1)
    recur(idx + 1, A + nutrient[idx][0], B + nutrient[idx][1], C + nutrient[idx][2], D + nutrient[idx][3], E + nutrient[idx][4])
    used.pop()
    recur(idx + 1, A, B, C, D, E)


n = int(input())

a, b, c, d = map(int, input().split())

nutrient = [list(map(int, input().split())) for _ in range(n)]
used = []
answer_used = []
answer = 9999999999999

recur(0, 0, 0, 0, 0, 0)

answer_used.sort()

if answer_used:
    print(answer)
    print(*answer_used)
else:
    print(-1)