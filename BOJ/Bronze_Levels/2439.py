import sys
num = int(sys.stdin.readline())

for i in range(1, num+1):
    k = num+1
    for j in range(1, k-i):
        print(" ", end="")
    for j in range(k-i, k):
        print("*", end="")
    print("")
