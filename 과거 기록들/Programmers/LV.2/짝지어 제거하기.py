def solution(st):
    tmp = []
    for s in st:
        if s not in tmp:
            tmp.append(s)
        elif tmp[-1] == s:
            tmp.pop()
    if not tmp:
        return 1
    else:
        return 0
    
print(solution('baabaa'))