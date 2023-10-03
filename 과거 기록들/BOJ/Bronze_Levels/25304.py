import sys
totalPrice = int(sys.stdin.readline())
kind = int(sys.stdin.readline())
sum = 0

for i in range(kind):
    p, n = map(int, sys.stdin.readline().split(" "))
    sum += p * n

if totalPrice == sum:
    print("Yes")
else:
    print("No")
