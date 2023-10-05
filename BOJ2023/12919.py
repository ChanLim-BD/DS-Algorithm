def dfs(string):
    if string == s:
        return True

    if len(string) > 1 and string[0] == 'B' and dfs((string[1:])[::-1]):
        return True

    if len(string) > 1 and string[-1] == 'A' and dfs(string[:-1]):
        return True
    return False

s = input()
t = input()
if dfs(t):
    print(1)
else:
    print(0)

'''
BAAAAABAA
BAABAAAAAB
'''