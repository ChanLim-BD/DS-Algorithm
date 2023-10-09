'''
본인은 본인 모자 모름, 앞 뒤 상태만 확인 가능
검은색 1 흰색 2 불확실 0

앞의 리스트는 각 사람이 본 검은 모자 수

뒤의 리스트는 각 사람이 쓴 모자의 색깔 여부

[1, 1, 2, 1] -> [2, 1, 1, 1]
[1, 1, 1] -> [0, 1, 0]
'''

n = [1, 1, 2, 1]

if n[1] == 1:
    if len(n) > 3:
        if n[3] > 1:
            print(1)
        else:
            print(2)
    else:
        print(0)
else:
    if n[-2] == 0:
        print(2)
    

for i in range(1, len(n) -1):
    if n[i-1] == 1:
        if n[i+1] == 1 or n[i+1] == 2:
            print(1)
        else:
            print(0)
    elif n[i-1] == 0 and n[i+1] == 0:
        print(2)
    else:
        print(1)

if n[-2] == 1:
    if len(n) > 3:
        if n[3] > 1:
            print(1)
        else:
            print(2)
    else:
        print(0)
else:
    if n[-2] == 0:
        print(2)
    