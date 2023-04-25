def solution(rsp):
    table = str.maketrans('025', '502')
    ans = rsp.translate(table)
    return ans
