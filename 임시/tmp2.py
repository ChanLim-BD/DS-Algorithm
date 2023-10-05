def str_sort(strings, n):
    strings.sort()
    return sorted(strings, key=lambda x:x[n])


print(str_sort(["abce", "abcd", "cdx"], 2))

"""
["abce", "abcd", "cdx"]
"""