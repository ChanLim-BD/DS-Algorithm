def solution(n):
    x = sorted(list(map(int, str(n))), reverse=True)
    ans = ''
    for i in x:
        ans += str(i)
    return int(ans)