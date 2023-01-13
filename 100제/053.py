data = list(input())

op = 0
cl = 0

# print(ord('(')) 40
# print(ord(')')) 41

for i in data:
    if ord(i) == 40:
        op += 1
    elif ord(i) == 41:
        cl += 1

print(op, cl)

if op == cl:
    print('YES')
else:
    print('NO')


'''
def math(e):
    if e.count('(') != e.count(')'):
        return False
    괄호 = []
    for i in e:
        if i == '(':
            괄호.append('(')
        if i == ')':
            if len(괄호) == 0:
                return False
            괄호.pop()
    return True

n = input()
if math(n) == True:
	print("YES")
else:
	print("NO")
'''
