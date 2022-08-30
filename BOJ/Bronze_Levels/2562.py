a = []

for i in range(9):
    b = int(input())
    a.append(b)

print(max(a))
print(a.index(max(a)) + 1)


"""
IndexError: list assignment index out of range는

빈 리스트에 인덱스를 지정했을 때 나오는 에러이다.
"""
