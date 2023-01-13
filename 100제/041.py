num = int(input())


def chech_prime(n):
    if n <= 1:
        return "NO"
    i = 2
    소수 = True
    while (i**2) < n:
        if n % i == 0:
            소수 = False
            break
        i += 1
    if 소수:
        return "YES"
    else:
        return "NO"


print(chech_prime(num))
