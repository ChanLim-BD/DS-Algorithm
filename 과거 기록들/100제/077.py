def sol(strings):
    result = []
    for i in range(1, len(strings)+1):  # 1 ~ len
        for j in range(i):  # 0 ~ i
            result.append(strings[j:j+len(strings)-i+1])
    return result


input1 = input()
input2 = input()
# 문자열 나열될 수 있는 모든 경우의수 만들기
list1 = set(sol(input1))
list2 = set(sol(input2))
print(list1)
print(list2)
# 경우의 수 교집합
answers = list1.intersection(list2)
# 가장 긴 교집합
answer = max(answers, key=len)
print(len(answer))
