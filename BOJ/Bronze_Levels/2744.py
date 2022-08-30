import sys
s = sys.stdin.readline()

ans = []

for ch in s:
    if ch.isupper():
        ans.append(ch.lower())
    else:
        ans.append(ch.upper())

print(''.join(ans))

"""
파이썬 python list to string 리스트를 문자열로 변경

separator.join(iterable)

list = ['a', 'b', 'c']

str = ''
separtor = ','
for idx, val in enumerate(list):
    str += val + ('' if idx == len(list) -1 else separtor)

print(str)
# print: a,b,c

"""
