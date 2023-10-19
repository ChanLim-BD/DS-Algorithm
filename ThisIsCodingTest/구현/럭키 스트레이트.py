N = input() 

if len(N) % 2 == 0:
    front, end = N[0:len(N) // 2], N[len(N) // 2:]
    if sum(list(map(int, front))) == sum(list(map(int, end))):
        print("LUCKY")
    else:
        print("READY")
else:
    exit(0)