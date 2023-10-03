def solution(p):
    answer = 0
    while p != []:
        p0 = p[0]                   # 25
        minute = p0 // 10 + 1       # 3분 후

        for i in range(len(p)):     # 0, 1, 2, 3, 4, 5
            # [25, 5, 20, 45, 15, 55] -> [-5, -25, -10, 15, -15, 25]
            p[i] -= 10 * minute

        while p != [] and p[0] < 0:
            # [15, -15, 25]
            p.pop(0)

        if p != []:
            # [35, -15, 25]
            p[0] += 20

        answer += minute
    return answer


p1 = [25, 5, 20, 45, 15, 55]

print(solution(p1))
