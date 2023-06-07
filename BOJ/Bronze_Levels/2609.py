def GCD(x, y):
    while(y):
        x, y = y, x % y
    return x

def LCM(x, y):
    result = (x * y) // GCD(x, y)
    return result

X, Y = map(int, input().split())

print(GCD(X, Y))
print(LCM(X, Y))

