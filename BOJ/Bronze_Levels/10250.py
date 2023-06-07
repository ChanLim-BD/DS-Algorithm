T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())

    x = str(N % H)
    y = str((N // H) + 1).zfill(2)

    if N % H == 0:
        x = str(H)
        y = str(N // H).zfill(2)
    
    print(x + y)