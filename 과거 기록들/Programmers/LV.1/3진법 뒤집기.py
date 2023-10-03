def solution(n):
    ls = []
    while(n):
        ls.append(n % 3)
        n = n // 3
    
    ans = 0
    z = 1
    for i in ls:
        num = ((3 ** (len(ls)-z) * i))
        z += 1
        ans += num
    return ans


def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer