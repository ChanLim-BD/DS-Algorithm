def solution(my_string):
    ans = ""
    for s in my_string:
        if s in "abcdefghijklmnopqrstuvwxyz":
            ans += s.upper()
        else:
            ans += s.lower()
    return ans
