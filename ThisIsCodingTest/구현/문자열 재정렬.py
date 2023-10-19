S = input()
num = 0
string = ''
for s in S:
    if s.isdecimal():
        num += int(s)
    elif s.isalpha():
        string += s
answer = ''.join(sorted(string))
print(answer + str(num))