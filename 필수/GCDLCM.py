def GCD1(a, b):
    if a % b == 0:
        return b
    elif b == 0:
        return a
    else:
        return GCD1(b, a % b)
    
def GCD2(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def LCM(a, b):
    return a * b // GCD2(a, b)

a, b = map(int, input().split())

print(GCD1(a, b))
print(GCD2(a, b))
print(LCM(a, b))