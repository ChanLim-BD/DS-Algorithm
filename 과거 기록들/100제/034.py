num = list(map(int, input().split()))

l = [int(i) for i in num]

if l != sorted(l):
    print("NO")

else:
    print("YES")
