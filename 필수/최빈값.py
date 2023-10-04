arr = [1,2,3,2,3,2,4,5,1,2,3,3,3,3,2,3,2,3,3,2,2]

#최빈값
dic = dict()
for i in arr:#빈도수 구하기
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

print(dic)
print(max(dic.values()))

mx = max(dic.values()) #빈도수 중 최대값 구하기
mx_dic = [] #최빈값 숫자를 저장할 배열

for i in dic: #빈도수 딕셔너리에서
    if mx == dic[i]: #최빈값의 key저장
        mx_dic.append(i)

print(mx_dic)