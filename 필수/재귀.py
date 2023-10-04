def test(x):
    if x == 0:
        print(x, end = ' ')
        return x
    print(x, end = ' ')
    test(x-1)
    
def recur(number, output):
    if number == M:
        print(output)
        return
    
    for i in range(1, N+1):
        recur(number+1, output+str(i)+" ")

N, M = map(int, input().split())

recur(0, "")