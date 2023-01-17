# point = list(int(input()))
# dish = int(input())

point = [1, 1, 3, 2, 5]
dish = 3


def solution(point, dish):
    dish -= 1
    answer = 0
    s = sorted(point)  # [1, 1, 2, 3, 5]
    while True:
        p = point.pop(0)
        if s[0] == p:
            if dish == 0:
                break
            dish -= 1
            s.pop(0)
        else:
            point.append(p)
            if dish == 0:
                dish = len(point)-1
            else:
                dish -= 1
        answer += 1
    return answer


print(solution(point, dish))
