nums = '0123456789'
cnt = []

A = int(input())
B = int(input())
C = int(input())

result = list(str(A * B * C))

for n in nums:
    cnt.append(result.count(n))

for c in cnt:
    print(c)