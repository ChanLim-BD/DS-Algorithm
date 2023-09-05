'''
공약수 

1. 갭을 줄여도 된다.

2. 최대 공약수라는 말은 두 수 중 하나로 나누어서 나머지가 생기지 않는다.

3. 한 수를 가능한 만큼 갭을 줄인다.
'''

def _gcd(a,b):
    while a % b != 0: # 나머지가 0이 되는 순간 멈춘다. 
        tmp = a % b
        a = b
        b = tmp
    return b 

def _lcm(a,b):
    return a * b // _gcd(a, b)


A, B = map(int, input().split())

print(_gcd(A, B), _lcm(A, B))