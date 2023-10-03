# 모든 날에 상담을 받거나, 안받거나 모든 경우의 수를 확인해준다.

def recur(idx, price):
    global answer

    if idx > N-1:
        if idx > N:
            return
        answer = max(answer, price)
        return

    # 상담을 한다면,
    recur(idx + interview[idx][0], price + interview[idx][1])
    # 상담을 안한다면,
    recur(idx+1, price)


N = int(input())

interview =[list(map(int, input().split())) for _ in range(N)]

answer = 0

recur(0, 0)

print(answer)