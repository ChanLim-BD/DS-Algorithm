def solution(myStr):
    tmp = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split()
    if len(tmp) == 0:
        tmp.append("EMPTY")
    return tmp