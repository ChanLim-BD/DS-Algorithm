N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)

count = 0

while K:
    for c in coins:
        if c <= K:
            tmp = K // c
            K -= tmp * c
        else:
            tmp = 0
            continue
        count += tmp

print(count)