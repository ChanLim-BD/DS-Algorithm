s = input()
answer = 1
for i in s:
    if int(i) == 0 or int(i) == 1:
        answer += int(i)
        continue
    else:
        answer *= int(i)
print(answer)