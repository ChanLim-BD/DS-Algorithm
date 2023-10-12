T = int(input())
array = [int(input()) for _ in range(T)]

print(*sorted(array, reverse=True))