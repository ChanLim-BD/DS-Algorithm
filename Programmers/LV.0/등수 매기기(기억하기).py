"""https://gomming.tistory.com/28"""


def solution(score):
    x = []
    for s in score:
        x.append(s[0] + s[1])
    y = sorted(x, reverse=True)
    p_ind = []
    for i in x:
        p_ind.append(y.index(i)+1)
    return p_ind
