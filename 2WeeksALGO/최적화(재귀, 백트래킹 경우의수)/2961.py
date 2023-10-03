# 완전탐색적 사고

# 재료를 1부터 N까지 다 써보면 되겠네?

def recur(idx, dan, zzan, use):
    global answer

    if idx == N:
        if use == 0: # 아무 재료도 사용하지 않았다면
            return
        result = abs(dan - zzan)
        answer = min(answer, result)
        return
        
    # 재료 사용시           단맛                짠맛        사용횟수
    recur(idx+1, dan+ingre[idx][0], zzan*ingre[idx][1], use + 1)
    # 재료 사용 안할 시
    recur(idx+1, dan, zzan, use)

N = int(input())

ingre = [list(map(int, input().split())) for _ in range(N)]

answer = 99999999999999999999

recur(0, 0, 1, 0)