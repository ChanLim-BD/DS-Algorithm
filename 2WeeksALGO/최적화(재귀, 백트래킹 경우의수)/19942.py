def recur(idx, A, B, C, D, E):
    global answer

    if idx == N:
        if a <= A and b <= B and c <= C and d <= D:
            answer = min(answer, E)
        
    #    재료 사용   단백질         지방                탄수화물        비타민          가격
    recur(idx+1, A+ingre[idx][0], B+ingre[idx][1], C+ingre[idx][2], D+ingre[idx][3], E+ingre[idx][4])
    # 재료 사용 안할 시
    recur(idx+1, A,B,C,D,E)

N = int(input())

a,b,c,d = list(map(int, input().split()))

ingre = [list(map(int, input().split())) for _ in range(N)]

answer = 99999999999999999999

recur(0, 0, 0, 0, 0, 0)