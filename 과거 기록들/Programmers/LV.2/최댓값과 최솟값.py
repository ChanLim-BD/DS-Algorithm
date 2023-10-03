def solution(s):
    answer = ''
    ls = list(map(int, s.split(" ")))
    max_s, min_s = max(ls), min(ls)
    ls = [str(min_s), str(max_s)]
    return ' '.join(ls)

def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))