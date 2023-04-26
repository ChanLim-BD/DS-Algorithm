def solution(num, total):
    answer = []
    if num % 2 == 1:
        center = total // num
        addition = (num - 1) // 2
        for i in range(center - addition, center + addition + 1):
            answer.append(i)
    else:
        cen_l = total // num
        cen_r = (total // num) + 1
        addition = (num - 2) // 2
        for i in range(cen_l - addition, cen_r + addition + 1):
            answer.append(i)
    return answer
