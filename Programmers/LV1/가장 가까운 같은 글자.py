def solution(s):
    answer = []
    tmp = dict()
    for i in range(len(s)):
        if s[i] not in tmp:
            answer.append(-1)
        else:
            answer.append(i - tmp[s[i]])
        tmp[s[i]] = i
        
    return answer