N, P = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]

info.sort(key = lambda x:(x[0]**2 + x[1]**2)**0.5)

ans = -1

for inf in info:
    if P + inf[2] >= 1000000:
        ans = round(((inf[0] - 0)**2 + (inf[1] - 0)**2)**0.5, 3)
        break
    P += inf[2]

if ans < 0:
    print(-1)
else:
    print(f"{ans:.3f}")