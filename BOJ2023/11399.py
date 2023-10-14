N = int(input())
line = list(map(int, input().split()))

line.sort() # 1, 2, 3, 3, 4

answer = 0

for i in range(1, N + 1):
    '''
    line[0]
    line[0] + line[1]
    line[0] + line[1] + line[2]
    line[0] + line[1] + line[2] + line[3]
    line[0] + line[1] + line[2] + line[3] + line[4]
    ''' 
    tmp = 0   
    for j in range(i):
        tmp += line[j]
    answer += tmp
print(answer)