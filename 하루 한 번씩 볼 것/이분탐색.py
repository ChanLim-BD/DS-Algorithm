def solution(n, times):
    a, b = 0, 1
    while not is_ok(n, times, b):
        a, b = b, 2*b        
    while a < b:
        m = (a + b)//2
        a, b = (a, m) if is_ok(n, times, m) else (m + 1,b)
    return a

def is_ok(n, times, x):
    return n <= sum(x//i for i in times)


print(solution(6, [7, 10]))
###

# 1) n보다 큰 최소의 자연수 찾기
def solution(n):
    a,b = 0,1
    while not is_ok(n, b):
        a,b = b, 2*b
    while a<b:
        m = (a+b)//2
        a,b = (a,m) if is_ok(n, m) else (m+1,b)
    return a

def is_ok(n, x):
    return True if x>n else False

# 2) n보다 작은 최대의 자연수 찾기

def solution(n):
    a,b = 0,1
    while is_ok(n, b):
        a,b = b, 2*b
    while a<b:
        m = (a+b+1)//2
        a,b = (m,b) if is_ok(n, m) else (a,m-1)
    return a

def is_ok(n, x):
    return True if x<n else False