a, b = map(float, input().split())
while ((a < 0) | (a > 10) | (b < 0) | (b > 10)):
    print("Not Correct.")
else:
    print(a/b)
