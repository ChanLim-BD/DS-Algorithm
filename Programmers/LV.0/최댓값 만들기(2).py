def solution(numbers):
    answer = 0
    tmp1 = []
    tmp2 = []
    for i in numbers:
        if i > 0:
            tmp1.append(i)
        else:
            tmp2.append(i)
    tmp1.sort(reverse=True)
    tmp2.sort(reverse=True)

    if len(tmp1) < 2:
        return tmp2[0] * tmp2[1]
    elif len(tmp2) < 2:
        return tmp1[0] * tmp1[1]
    else:
        if tmp1[0] * tmp1[1] > tmp2[0] * tmp2[1]:
            return tmp1[0] * tmp1[1]
        else:
            return tmp2[0] * tmp2[1]


def solution(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])
