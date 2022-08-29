a, b = map(int, input().split())
while ((a < 0) | (a > 10000) | (b < 0) | (b > 10000)):
    print("Not Correct.")
else:
    print(a+b)
    print(a-b)
    print(a*b)
    print(int(a/b))
    print(a % b)
