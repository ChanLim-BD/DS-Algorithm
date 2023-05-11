import math

print(math.gcd(20, 45))
print()
print(math.gcd(20, 60, 100))
print()
print(math.lcm(10, 20))
print()
print(math.lcm(10, 20, 35))
print()


"""
유클리드 호제법 (재귀)
"""

def GCD(x, y):
    while(y):
        x, y = y, x % y
    return x

print(GCD(10, 12))
print()

def LCM(x, y):
    result = (x * y) // GCD(x, y)
    return result

print(LCM(10, 12))
print()