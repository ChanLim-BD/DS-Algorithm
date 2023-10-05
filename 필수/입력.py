a = input()                             # qwer
print(a)                                # qwer

i = int(input())                        # 1234
print(i)                                # 1234

b = list(input())                       # qwer
print(b)                                # ['q', 'w', 'e', 'r']

e = list(input().split())               # 12313432123456     | 123 123 444 555
print(e)                                # ['12313432123456'] | ['123', '123', '444', '555']

f = list(map(int, input()))             # 12313432123456
print(f)                                # [1, 2, 3, 1, 3, 4, 3, 2, 1, 2, 3, 4, 5, 6]

c = list(map(int, input().split()))     # 12313432123456   | 123 123 444 555
print(c)                                # [12313432123456] | [123, 123, 444, 555]

d = [int(input()) for _ in range(5)]    # 123 enter 456 enter 146 enter 34342 enter 76 enter
print(d)                                # [123, 456, 146, 34342, 76]

graph = [[0] * 19 for _ in range(19)]
graph = [list(map(int, input().split())) for _ in range(19)]

food = [1, 3, 4, 6]
answer = ''

for i in range(1, len(food)):           # 순차적 출력
    answer += str(i) * (food[i] // 2)
answer += '0'
for i in range(1, len(food))[::-1]:     # 역순 출력 
    answer += str(i) * (food[i] // 2)