def solution(s):
    answer = []
    zero = 0
    ze = 0
    cnt = 0
    while s != '1':
        cnt += 1
        zero = s.count('0')
        s = s.replace('0', '', zero)
        s = bin(len(s))[2:]
        ze += zero
    answer = [cnt, ze]
    return answer