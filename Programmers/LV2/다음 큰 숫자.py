def solution(n):
    answer = 0
    b_n = bin(n)[2:]
    boundary = len(b_n) + 1
    
    for i in range(n+1, 2 ** boundary):
        if bin(n)[2:].count('1') == bin(i)[2:].count('1'):
            answer = i
            break
    return answer