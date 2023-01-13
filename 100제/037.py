ls = list(map(str, input().split()))
lss = list(set(ls))
idx = 0
cnt = 0

for i in range(len(lss)):
    if cnt < ls.count(lss[i]):
        cnt = ls.count(lss[i])
        idx = i

print("{}(이)가 총 {}표로 반장이 되었습니다.".format(lss[idx], cnt))
