N, M = map(int, input().split())
nonhear = set()
nonsee = set()

for _ in range(N):
    nonhear.add(input())

for _ in range(M):
    nonsee.add(input())

nonhearsee = sorted(list(nonhear & nonsee))

print(len(nonhearsee))

for n in nonhearsee:
    print(n)