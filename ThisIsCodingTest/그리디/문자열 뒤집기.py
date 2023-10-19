S = input()
answer = 0
for i in range(len(S) - 1):
    if S[i] == '0':
        if S[i + 1] == '0':
            continue
        else:
            answer += 1
print(answer)

###

S = input()
count0 = 0
count1 = 0

if S[0] == '1': # 처음 문자열의 여부 
    count0 += 1
else:
    count1 += 1

for i in range(len(S) - 1): # 이후 문자열을 확인 (처음 문자열을 확인했으니 다음부터는 이전 문자열을 보고 파악)
    if S[i] != S[i + 1]:
        if S[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1
    else:
        continue
    
print(min(count0, count1))