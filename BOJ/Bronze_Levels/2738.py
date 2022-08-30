a, b = map(int, input().split())
l = []
r = []
for _ in range(a*2):
    l.append(list(map(int, input().split())))

for i in range(len(l) // 2):
    for j in range(b):
        r.append(l[i][j]+l[i+a][j])
        
for i in range(len(r)):
    if i % a != a-1:
        print(r[i], end=' ')
    else:
        print(r[i], end='\n')
