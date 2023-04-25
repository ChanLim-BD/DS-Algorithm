def solution(num, k):
    ls = []
    st = str(num)
    for i in st:
        ls.append(int(i))
    if k in ls:
        return ls.index(k) + 1
    else:
        return -1
